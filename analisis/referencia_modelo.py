"""Réplica mínima del modelo de FlexSim en Python, para verificar el armado (fase 5).

No reemplaza a FlexSim: da el orden de magnitud que tiene que dar cada escenario
para detectar errores de armado. Usa la misma lógica y las mismas tablas
(flexsim/inputs.xlsx) que la guía flexsim/GUIA_FLEXSIM.md:

- Cola previa uniforme entre 11:40 y 12:00 (S09) y llegadas de personas Poisson por franja (S08).
- Cada persona tiene un tipo (S04) y una cantidad de raciones (S21).
- Caja: abre a las 12:00 más una demora real elegida al azar (S25). Tiempo = una muestra
  de S07 por ración × factor del escenario (S24). Fila única FIFO con 1 o 2 puestos;
  en E2 el puesto extra cierra a las 13:30 después de atender a quienes ya estaban en la fila.
- Mostrador: fila única FIFO con 3 o 4 personas sirviendo (S22). Tiempo = una muestra de
  S15 por ración. Una fracción de las personas (S27) retira menú vegetariano, que sirve una
  sola persona a la vez; el resto lo atiende cualquiera. La fila de servicio no tiene límite
  mientras S23 esté pendiente, así que la réplica no modela el bloqueo de la caja.

Uso: python analisis/referencia_modelo.py [replicas]   (desde la raíz del TPI)
"""
import heapq
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
XLSX = RAIZ / "flexsim" / "inputs.xlsx"
T_APERTURA = 1200
GRUPOS = ["Estudiantes", "BecasNutrirse", "BecasPersonal", "Personal"]


def lognormal(rng, fila, n):
    return rng.lognormal(math.log(fila["Scale"]), fila["Shape"], n)


def suma_por_racion(rng, fila, raciones):
    """Una muestra por ración, sumadas por persona."""
    muestras = lognormal(rng, fila, int(raciones.sum()))
    return np.add.reduceat(muestras, np.concatenate([[0], np.cumsum(raciones)[:-1]]))


def fifo(llegada, servicio, libres, cierre_extra=math.inf):
    """Fila FIFO con varios servidores. `libres` es la hora en que se habilita cada uno.
    Si `cierre_extra` es finito, en ese instante un token de control se pone en la fila y
    se queda con el próximo servidor que se libera (E2)."""
    libres = list(libres)
    heapq.heapify(libres)
    inicio, fin = np.empty(len(llegada)), np.empty(len(llegada))
    for i in np.argsort(llegada, kind="stable"):
        if llegada[i] >= cierre_extra:
            heapq.heappop(libres)
            cierre_extra = math.inf
        inicio[i] = max(llegada[i], heapq.heappop(libres))
        fin[i] = inicio[i] + servicio[i]
        heapq.heappush(libres, fin[i])
    return inicio, fin


def mostrador(llegada, servicio, veg, servidores):
    """Fila única FIFO con `servidores` personas. La comida vegetariana la sirve una sola persona
    a la vez (PuestoVeg en FlexSim), y esa persona cuenta como una de las que sirven (S22)."""
    libres = [0.0] * int(servidores)
    heapq.heapify(libres)
    veg_libre = 0.0
    inicio, fin = np.empty(len(llegada)), np.empty(len(llegada))
    for i in np.argsort(llegada, kind="stable"):
        listo = max(llegada[i], veg_libre) if veg[i] else llegada[i]
        inicio[i] = max(listo, heapq.heappop(libres))
        fin[i] = inicio[i] + servicio[i]
        heapq.heappush(libres, fin[i])
        if veg[i]:
            veg_libre = fin[i]
    return inicio, fin


def replica(rng, t, esc):
    perfil = esc["Perfil"]
    tasas = t[f"TasaLlegadas_{perfil}"]
    ts = t["TiemposServicio"].set_index("Proceso")
    mix = t["MixTipos"]

    # Llegadas: cola previa + Poisson por franja, cada una con su grupo.
    cp = t["ColaPrevia"][t["ColaPrevia"]["Perfil"] == perfil]
    n_prev = int(esc["ColaPrevia"])
    llegada = [rng.uniform(0, T_APERTURA, n_prev)]
    grupo = [rng.choice(cp["Grupo"].to_numpy(), n_prev, p=(cp["Personas"] / cp["Personas"].sum()).to_numpy())]
    for _, f in tasas.iterrows():
        n = rng.poisson(f["Total"])
        pesos = f[GRUPOS].to_numpy(dtype=float)
        llegada.append(rng.uniform(f["Inicio_s"], f["Fin_s"], n))
        grupo.append(rng.choice(GRUPOS, n, p=pesos / pesos.sum()))
    llegada, grupo = np.concatenate(llegada), np.concatenate(grupo)
    n = len(llegada)

    # Tipo dentro del grupo y raciones por persona.
    vianda = np.zeros(n, dtype=bool)
    raciones = np.ones(n, dtype=int)
    for g, sub in mix.groupby("Grupo"):
        idx = np.flatnonzero(grupo == g)
        sub = sub.reset_index(drop=True)
        filas = rng.choice(len(sub), len(idx), p=(sub["PropEnGrupo"] / sub["PropEnGrupo"].sum()).to_numpy())
        vianda[idx] = sub["EsVianda"].to_numpy()[filas] == 1
        probs = sub[["P1Racion", "P2Raciones", "P3Raciones"]].to_numpy()[filas]
        u = rng.random(len(idx))
        raciones[idx] = 1 + (u > probs[:, 0]) + (u > probs[:, 0] + probs[:, 1])

    # Caja: fila única.
    apertura = T_APERTURA + rng.choice(t["DemoraApertura"]["Demora_s"].to_numpy())
    serv_caja = suma_por_racion(rng, ts.loc["Validacion"], raciones) * esc["FactorValidacion"]
    libres = [apertura] * int(esc["PuestosBase"]) + [max(apertura, esc["ExtraDesde_s"])] * int(esc["PuestosExtra"])
    cierre = esc["ExtraHasta_s"] if esc["PuestosExtra"] else math.inf
    inicio_val, fin_val = fifo(llegada, serv_caja, libres, cierre)
    puestos = int(esc["PuestosBase"] + esc["PuestosExtra"])

    # Mostrador: menú vegetariano por persona (S27).
    veg = rng.random(n) < esc["ProbVegetariano"]
    serv_mostrador = suma_por_racion(rng, ts.loc["ServicioRacion"], raciones)
    inicio_srv, salida = mostrador(fin_val, serv_mostrador, veg, esc["Servidores"])

    espera_caja = (inicio_val - llegada) / 60
    espera_srv = (inicio_srv - fin_val) / 60
    desde_apertura = (inicio_val - np.maximum(llegada, apertura)) / 60
    franjas = np.bincount(np.clip(((fin_val - T_APERTURA) // 600).astype(int), 0, 15), weights=raciones, minlength=16)
    return {
        "Personas": n,
        "Raciones": int(raciones.sum()),
        "EsperaCaja_min": espera_caja.mean(),
        "EsperaColaPrevia_min": espera_caja[llegada < T_APERTURA].mean(),
        "EsperaCajaDesdeApertura_min": desde_apertura.mean(),
        "EsperaCajaDesdeAperturaMax_min": desde_apertura.max(),
        "ColaCajaMax": maximo_simultaneo(llegada, inicio_val),
        "EsperaServicio_min": espera_srv.mean(),
        "EsperaServicioMax_min": espera_srv.max(),
        "ColaServicioMax": maximo_simultaneo(fin_val, inicio_srv),
        "TiempoTotalDesdeApertura_min": ((salida - np.maximum(llegada, apertura)) / 60).mean(),
        "UtilCaja_pct": 100 * serv_caja.sum() / (puestos * (fin_val.max() - apertura)),
        "UtilServicio_pct": 100 * serv_mostrador.sum() / (esc["Servidores"] * (salida.max() - fin_val.min())),
        "EsperaServicioVeg_min": espera_srv[veg].mean() if veg.any() else float("nan"),
        "franjas": franjas,
        # registro por persona, con las mismas columnas que Salida_Personas de FlexSim
        "apertura": apertura,
        "log": pd.DataFrame({
            "Raciones": raciones, "Fila": np.where(vianda, "Viandas", "General"), "Veg": veg,
            "tLlegada": llegada, "tInicioVal": inicio_val, "tFinVal": fin_val,
            "tEntraServicio": fin_val, "tInicioServicio": inicio_srv, "tSalida": salida,
        }),
    }


def maximo_simultaneo(entra, sale):
    """Máximo de personas presentes a la vez entre `entra` y `sale`."""
    ev = np.concatenate([np.column_stack([entra, np.ones(len(entra))]), np.column_stack([sale, -np.ones(len(sale))])])
    ev = ev[np.lexsort((ev[:, 1], ev[:, 0]))]   # a igual tiempo, primero las salidas
    return int(np.cumsum(ev[:, 1]).max()) if len(ev) else 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    replicas = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    t = pd.read_excel(XLSX, sheet_name=None)
    rng = np.random.default_rng(2026)
    filas, franjas = [], {}
    for _, esc in t["Escenarios"].iterrows():
        res = [replica(rng, t, esc) for _ in range(replicas)]
        df = pd.DataFrame([{k: v for k, v in r.items() if k not in ("franjas", "log", "apertura")} for r in res])
        fila = {"Escenario": esc["Escenario"]}
        fila.update(df.mean().round(1).to_dict())
        filas.append(fila)
        franjas[esc["Escenario"]] = np.mean([r["franjas"] for r in res], axis=0).round(1)
    tabla = pd.DataFrame(filas).set_index("Escenario").T
    pd.set_option("display.width", 220)
    pd.set_option("display.max_columns", 20)
    print(f"Media de {replicas} réplicas por escenario (verificación, no validación):\n")
    print(tabla.to_string())
    ref = t["Referencia_Validaciones"]
    print("\nRaciones validadas por franja: E0 (modelo) contra registros reales (media por día)")
    for perfil in ("Pico", "Bajo"):
        real = ref[ref["Perfil"] == perfil]
        print(f"\n{perfil}")
        for i, (_, r) in enumerate(real.iterrows()):
            print(f"  {r['Franja']}  modelo {franjas[f'E0_{perfil}'][i]:6.1f}   real {r['RacionesMedia']:6.1f}")


if __name__ == "__main__":
    main()
