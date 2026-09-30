"""Réplica mínima del modelo de FlexSim en Python, para verificar el armado (fase 5).

No reemplaza a FlexSim: da el orden de magnitud que tiene que dar cada escenario
para detectar errores de armado. Usa la misma lógica y las mismas tablas
(flexsim/inputs.xlsx) que la guía flexsim/GUIA_FLEXSIM.md:

- Cola previa uniforme entre 11:40 y 12:00 (S09) y llegadas Poisson por franja (S08).
- Apertura a las 12:00 más una demora real elegida al azar (S22).
- Validación lognormal (S07) × factor del escenario (S21), FIFO, con 1 o 2 puestos.
  E2: el puesto extra cierra a las 13:30 después de atender a quienes ya estaban
  en la fila. E5: si el puesto toma a alguien durante la interrupción, espera a que termine.
- Mostrador con 2 líneas (S13, S15) y salón con 432 asientos (S14, S16, S17), sin caminata.

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


def replica(rng, t, esc):
    perfil = esc["Perfil"]
    tasas = t[f"TasaLlegadas_{perfil}"]
    ts = t["TiemposServicio"].set_index("Proceso")
    mix = t["MixTipos"]
    p_llevar = (mix["PropEnGrupo"] * mix["PLlevar"]).groupby(mix["Grupo"]).sum()
    p_veg = float(mix["PVegetariano"].iloc[0])

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
    orden = np.argsort(llegada)
    llegada, grupo = llegada[orden], grupo[orden]
    n = len(llegada)

    # Validación: FIFO sobre los puestos disponibles.
    apertura = T_APERTURA + rng.choice(t["DemoraApertura"]["Demora_s"].to_numpy())
    servicio = lognormal(rng, ts.loc["Validacion"], n) * esc["FactorValidacion"]
    libres = [apertura] * int(esc["PuestosBase"])
    if esc["PuestosExtra"]:
        libres += [max(apertura, esc["ExtraDesde_s"])] * int(esc["PuestosExtra"])
    heapq.heapify(libres)
    cierre_extra = esc["ExtraHasta_s"] if esc["PuestosExtra"] else math.inf
    desde, hasta = esc["InterrupcionDesde_s"], esc["InterrupcionHasta_s"]
    inicio_val, fin_val = np.empty(n), np.empty(n)
    for i in range(n):
        if llegada[i] >= cierre_extra:
            # El token de control entra a la fila a las 13:30: toma el próximo puesto que
            # se libera y no lo devuelve.
            heapq.heappop(libres)
            cierre_extra = math.inf
        inicio = max(llegada[i], heapq.heappop(libres))
        if desde <= inicio < hasta:
            inicio = hasta
        inicio_val[i], fin_val[i] = inicio, inicio + servicio[i]
        heapq.heappush(libres, fin_val[i])

    # Mostrador: una línea por menú, 1 servidor cada una.
    veg = rng.random(n) < p_veg
    fin_most = np.empty(n)
    for linea, proceso in ((veg, "MostradorVegetariano"), (~veg, "MostradorNoVegetariano")):
        idx = np.flatnonzero(linea)
        idx = idx[np.argsort(fin_val[idx])]
        entrega = lognormal(rng, ts.loc[proceso], len(idx))
        libre = 0.0
        for k, i in enumerate(idx):
            libre = max(fin_val[i], libre) + entrega[k]
            fin_most[i] = libre

    # Salón: los que se quedan toman el primer asiento libre; si no hay, esperan de pie.
    llevar = rng.random(n) < p_llevar.reindex(grupo).to_numpy()
    idx = np.flatnonzero(~llevar)
    idx = idx[np.argsort(fin_most[idx])]
    consumo = lognormal(rng, ts.loc["ConsumoSalon"], len(idx))
    asientos = [0.0] * int(esc["Asientos"])
    sentado, salida = np.full(n, np.nan), fin_most.copy()
    for k, i in enumerate(idx):
        sentado[i] = max(fin_most[i], heapq.heappop(asientos))
        salida[i] = sentado[i] + consumo[k]
        heapq.heappush(asientos, salida[i])

    espera = (inicio_val - llegada) / 60
    previa = llegada < T_APERTURA
    usados = int(esc["PuestosBase"]) + int(esc["PuestosExtra"])
    return {
        "Personas": n,
        "EsperaMedia_min": espera.mean(),
        "EsperaMax_min": espera.max(),
        "EsperaColaPrevia_min": espera[previa].mean(),
        "EsperaResto_min": espera[~previa].mean(),
        "EsperaDesdeApertura_min": ((inicio_val - np.maximum(llegada, apertura)) / 60).mean(),
        "EsperaDesdeAperturaMax_min": ((inicio_val - np.maximum(llegada, apertura)) / 60).max(),
        "PctEsperaMas10_min": 100 * (espera > 10).mean(),
        "ColaMax": maximo_simultaneo(llegada, inicio_val),
        "UtilPuesto_pct": 100 * servicio.sum() / (usados * (fin_val.max() - apertura)),
        "OcupacionMax": maximo_simultaneo(sentado[idx], salida[idx]),
        "DePieMax": maximo_simultaneo(fin_most[idx], sentado[idx]),
        "EsperaAsientoMedia_min": ((sentado[idx] - fin_most[idx]) / 60).mean(),
        "PermanenciaMedia_min": ((salida - llegada) / 60).mean(),
        "franjas": np.bincount(np.clip(((fin_val - T_APERTURA) // 600).astype(int), 0, 15), minlength=16),
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
        df = pd.DataFrame([{k: v for k, v in r.items() if k != "franjas"} for r in res])
        fila = {"Escenario": esc["Escenario"]}
        fila.update(df.mean().round(1).to_dict())
        filas.append(fila)
        franjas[esc["Escenario"]] = np.mean([r["franjas"] for r in res], axis=0).round(1)
    tabla = pd.DataFrame(filas)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", 20)
    print(f"Media de {replicas} réplicas por escenario (verificación, no validación):\n")
    print(tabla.to_string(index=False))
    ref = t["Referencia_Validaciones"]
    print("\nValidaciones por franja: E0 (modelo) contra registros reales (media por día)")
    for perfil in ("Pico", "Bajo"):
        real = ref[ref["Perfil"] == perfil]
        print(f"\n{perfil}")
        for i, (_, r) in enumerate(real.iterrows()):
            print(f"  {r['Franja']}  modelo {franjas[f'E0_{perfil}'][i]:6.1f}   real {r['ValidacionesMedia']:6.1f}")


if __name__ == "__main__":
    main()
