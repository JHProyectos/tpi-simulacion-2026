"""Validación del modelo de FlexSim (fase 6).

Lee las tres tablas de salida que exporta FlexSim (flexsim/salidas.xlsx, sección 15 de la guía)
y las contrasta de tres maneras:

1. Verificación interna: los tiempos de cada persona van en orden, las tablas coinciden entre
   sí, la cola termina vacía y la cantidad de personas es la esperada.
2. Validación contra la realidad: la curva de raciones por franja contra los registros reales
   (hoja Referencia_Validaciones) y, en el escenario base, los valores observados en campo (S10).
3. Verificación contra la réplica independiente (analisis/referencia_modelo.py): una corrida de
   FlexSim tiene que caer dentro de lo que dan N réplicas de la réplica de Python.

Escribe un informe en flexsim/validacion_<escenario>.md.

Uso (desde la raíz del TPI):
    python analisis/validar_modelo.py [--escenario E0_Pico] [--salidas flexsim/salidas.xlsx]
                                      [--replicas 30] [--little 4.8]

Los umbrales de aceptación están como constantes al principio: son una propuesta del grupo y se
pueden ajustar, pero hay que declararlos en el informe.
"""
import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import referencia_modelo as ref  # noqa: E402

RAIZ = ref.RAIZ
T_FIN = 15600
FRANJA_S = 600

# Umbrales (propuesta del grupo)
UMBRAL_R_CURVA = 0.90          # correlación entre la curva del modelo y la real
UMBRAL_MAPE = 0.15             # error relativo medio por franja (sin la última, casi vacía)
UMBRAL_TOTAL = 0.05            # diferencia del total de raciones contra el real
MAX_FUERA_RANGO = 2            # franjas fuera del rango [mín, máx] de los días reales
Z_REPLICA = 2.0                # desvíos estándar de la réplica que se aceptan
COLA_S10 = (60, 70)            # cola máxima en la caja, escenario base pico (S10)
COLA_S10_ACEPTABLE = (55, 75)
ESPERA_PREVIA_S10 = (10, 15)   # espera media de la cola previa, en minutos (S10)

COLUMNAS = ["Raciones", "tLlegada", "tInicioVal", "tFinVal", "tEntraServicio", "tInicioServicio", "tSalida"]
NUMERICAS = COLUMNAS


def leer_salidas(ruta):
    hojas = pd.read_excel(ruta, sheet_name=None)
    for h in ("Salida_Personas", "Salida_Franjas", "Salida_Dia"):
        if h not in hojas:
            sys.exit(f"Falta la hoja {h} en {ruta}. Revisá la sección 15 de la guía.")
    p = hojas["Salida_Personas"].rename(columns={"tEntradaServicio": "tEntraServicio"})
    faltan = [c for c in COLUMNAS if c not in p.columns]
    if faltan:
        sys.exit(f"Salida_Personas no tiene las columnas {faltan}.")
    for c in NUMERICAS:
        p[c] = pd.to_numeric(p[c], errors="coerce")
    p = p[p["Raciones"].fillna(0) > 0].reset_index(drop=True)   # saca la fila plantilla
    if p.empty:
        sys.exit("Salida_Personas no tiene personas: hay que correr el modelo antes de exportar.")
    return p, hojas["Salida_Franjas"], hojas["Salida_Dia"]


def medidas(p, apertura, esc):
    """Mismos indicadores para FlexSim y para la réplica, calculados con las mismas fórmulas."""
    espera = (p["tInicioVal"] - p["tLlegada"]) / 60
    desde = (p["tInicioVal"] - np.maximum(p["tLlegada"], apertura)) / 60
    previa = p["tLlegada"] < ref.T_APERTURA
    srv = (p["tInicioServicio"] - p["tEntraServicio"]) / 60
    puestos = int(esc["PuestosBase"] + esc["PuestosExtra"])
    return {
        "Personas": len(p),
        "Raciones": int(p["Raciones"].sum()),
        "EsperaCaja_min": espera.mean(),
        "EsperaColaPrevia_min": espera[previa].mean() if previa.any() else float("nan"),
        "EsperaCajaDesdeApertura_min": desde.mean(),
        "EsperaCajaDesdeAperturaMax_min": desde.max(),
        "ColaCajaMax": ref.maximo_simultaneo(p["tLlegada"].to_numpy(), p["tInicioVal"].to_numpy()),
        "EsperaServicio_min": srv.mean(),
        "EsperaServicioMax_min": srv.max(),
        "ColaServicioMax": ref.maximo_simultaneo(p["tEntraServicio"].to_numpy(), p["tInicioServicio"].to_numpy()),
        "UtilCaja_pct": 100 * (p["tFinVal"] - p["tInicioVal"]).sum() / (puestos * (p["tFinVal"].max() - apertura)),
        "UtilServicio_pct": 100 * (p["tSalida"] - p["tInicioServicio"]).sum()
        / (esc["Servidores"] * (p["tSalida"].max() - p["tEntraServicio"].min())),
    }


def franjas_modelo(p):
    f = np.clip(((p["tFinVal"] - ref.T_APERTURA) // FRANJA_S).astype(int), 0, 15)
    return np.bincount(f, weights=p["Raciones"], minlength=16)


def estado(ok):
    return "OK" if ok else "REVISAR"


def verificacion_interna(p, franjas_tabla, dia, esc, medidas_flexsim):
    filas = []
    t = p[["tLlegada", "tInicioVal", "tFinVal", "tEntraServicio", "tInicioServicio", "tSalida"]].to_numpy()
    orden = bool((np.diff(t, axis=1) >= -1e-6).all()) and not np.isnan(t).any()
    filas.append(("Los tiempos de cada persona van en orden (llegada ≤ inicio caja ≤ fin caja ≤ fila servicio ≤ inicio servicio ≤ salida)",
                  "todas las personas" if orden else "hay personas con tiempos desordenados o vacíos", estado(orden)))

    esperadas = float(esc["PersonasDia"])
    tol = 3 * math.sqrt(max(esperadas - float(esc["ColaPrevia"]), 1))
    n = len(p)
    filas.append((f"Personas del día (esperadas {esperadas:.0f}, tolerancia ±{tol:.0f}: 3 desvíos de un Poisson)",
                  f"{n}", estado(abs(n - esperadas) <= tol)))
    rac, rac_esp = int(p["Raciones"].sum()), float(esc["RacionesDia"])
    filas.append((f"Raciones del día (esperadas {rac_esp:.0f}, tolerancia ±5 %)",
                  f"{rac}", estado(abs(rac - rac_esp) <= 0.05 * rac_esp)))

    tabla = pd.to_numeric(franjas_tabla["Raciones"], errors="coerce").fillna(0).to_numpy()[:16]
    calc = franjas_modelo(p)
    filas.append(("Salida_Franjas coincide con las raciones que se calculan desde Salida_Personas",
                  "coinciden" if np.allclose(tabla, calc) else f"difieren (tabla {tabla.sum():.0f}, personas {calc.sum():.0f})",
                  estado(np.allclose(tabla, calc))))

    d = dia.iloc[0]
    cola_tabla = float(d["ColaCajaMax"])
    filas.append(("ColaCajaMax de Salida_Dia coincide con la calculada desde Salida_Personas",
                  f"tabla {cola_tabla:.0f}, personas {medidas_flexsim['ColaCajaMax']}",
                  estado(cola_tabla == medidas_flexsim["ColaCajaMax"])))
    filas.append(("Al final de la corrida no queda nadie en la fila de caja ni en la de servicio",
                  f"EnFilaCaja {d['EnFilaCaja']:.0f}, EnFilaServicio {d['EnFilaServicio']:.0f}",
                  estado(d["EnFilaCaja"] == 0 and d["EnFilaServicio"] == 0)))
    ultima = p["tSalida"].max()
    filas.append((f"Todos salen antes de las 16:00 (t = {T_FIN})", f"última salida a t = {ultima:.0f} s",
                  estado(ultima <= T_FIN)))
    return filas


def contra_realidad(p, dia, esc, ref_val, med):
    """Devuelve (filas de la tabla de chequeos, DataFrame de la curva por franja)."""
    perfil = esc["Perfil"]
    real = ref_val[ref_val["Perfil"] == perfil].reset_index(drop=True)
    modelo = franjas_modelo(p)
    m, r = modelo[:len(real)], real["RacionesMedia"].to_numpy()
    curva = pd.DataFrame({"Franja": real["Franja"], "Real": r, "Modelo": m,
                          "Min": real["RacionesMin"], "Max": real["RacionesMax"]})
    fuera = int(((m < curva["Min"]) | (m > curva["Max"])).sum())
    corr = float(np.corrcoef(m, r)[0, 1])
    mape = float(np.mean(np.abs(m[:-1] - r[:-1]) / r[:-1]))
    total = float(m.sum() / r.sum() - 1)

    filas = [
        (f"Curva de raciones por franja: correlación con la real (mínimo {UMBRAL_R_CURVA})", f"{corr:.3f}", estado(corr >= UMBRAL_R_CURVA)),
        (f"Error relativo medio por franja, sin la última (máximo {UMBRAL_MAPE:.0%})", f"{mape:.1%}", estado(mape <= UMBRAL_MAPE)),
        (f"Total de raciones contra el real (±{UMBRAL_TOTAL:.0%})", f"{total:+.1%}", estado(abs(total) <= UMBRAL_TOTAL)),
        (f"Franjas fuera del rango de los días reales (máximo {MAX_FUERA_RANGO} de {len(real)})", f"{fuera}", estado(fuera <= MAX_FUERA_RANGO)),
    ]
    if esc["Escenario"] == "E0_Pico":
        cola = med["ColaCajaMax"]
        lo, hi = COLA_S10
        alo, ahi = COLA_S10_ACEPTABLE
        est = "OK" if lo <= cola <= hi else ("ACEPTABLE" if alo <= cola <= ahi else "REVISAR")
        filas.append((f"Cola máxima en la caja (S10: {lo} a {hi} personas; aceptable {alo} a {ahi})", f"{cola}", est))
        prev = med["EsperaColaPrevia_min"]
        filas.append((f"Espera media de la cola previa (S10: {ESPERA_PREVIA_S10[0]} a {ESPERA_PREVIA_S10[1]} min)",
                      f"{prev:.1f} min", estado(ESPERA_PREVIA_S10[0] <= prev <= ESPERA_PREVIA_S10[1])))
    return filas, curva


def contra_replica(t, esc, med, n):
    rng = np.random.default_rng(2026)
    filas = []
    for _ in range(n):
        r = ref.replica(rng, t, esc)
        filas.append(medidas(r["log"], r["apertura"], esc))
    df = pd.DataFrame(filas)
    out = []
    for k, v in med.items():
        media, desvio = df[k].mean(), df[k].std()
        desvio = max(desvio, 0.02 * abs(media), 1e-9)
        z = (v - media) / desvio
        out.append((k, v, media, desvio, z, estado(abs(z) <= Z_REPLICA)))
    return out


def fmt(x):
    return f"{x:.1f}" if isinstance(x, (float, np.floating)) else str(x)


def tabla_md(encabezado, filas):
    s = "| " + " | ".join(encabezado) + " |\n|" + "---|" * len(encabezado) + "\n"
    for f in filas:
        s += "| " + " | ".join(fmt(c) for c in f) + " |\n"
    return s


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--escenario", default="E0_Pico", help="nombre en la tabla Escenarios (la corrida exportada)")
    ap.add_argument("--salidas", default=str(RAIZ / "flexsim" / "salidas.xlsx"))
    ap.add_argument("--replicas", type=int, default=30)
    ap.add_argument("--little", type=float, help="contenido medio de «Esperar en la fila» según FlexSim (estadística de la actividad)")
    a = ap.parse_args()

    t = pd.read_excel(ref.XLSX, sheet_name=None)
    esc = t["Escenarios"].set_index("Escenario", drop=False).loc[a.escenario]
    p, franjas_tabla, dia = leer_salidas(a.salidas)
    apertura = float(dia.iloc[0]["Apertura_s"])
    med = medidas(p, apertura, esc)

    interna = verificacion_interna(p, franjas_tabla, dia, esc, med)
    realidad, curva = contra_realidad(p, dia, esc, t["Referencia_Validaciones"], med)
    replica = contra_replica(t, esc, med, a.replicas)

    l_log = (p["tInicioVal"] - p["tLlegada"]).sum() / T_FIN
    little = [("L = Σ espera / T, desde Salida_Personas", f"{l_log:.2f} personas"),
              ("L = N · W / T", f"{len(p) * (p['tInicioVal'] - p['tLlegada']).mean() / T_FIN:.2f} personas")]
    if a.little is not None:
        little.append(("Contenido medio de «Esperar en la fila» (FlexSim, lo ingresaste a mano)", f"{a.little:.2f} personas"))
        little.append(("Diferencia", estado(abs(a.little - l_log) <= 0.10 * l_log) + f" ({a.little / l_log - 1:+.1%})"))

    malos = [f for f in interna + realidad if f[2] == "REVISAR"] + [r for r in replica if r[5] == "REVISAR"]

    md = f"# Validación del modelo: {a.escenario}\n\n[TOC]\n\n"
    md += (f"Corrida exportada en `{Path(a.salidas).name}`: {len(p)} personas, {med['Raciones']} raciones, "
           f"apertura a t = {apertura:.0f} s. Generado con `analisis/validar_modelo.py`.\n\n")
    md += "## 1. Verificación interna\n\n" + tabla_md(["Chequeo", "Resultado", "Estado"], interna) + "\n"
    md += "## 2. Contra los datos reales\n\n" + tabla_md(["Chequeo", "Resultado", "Estado"], realidad) + "\n"
    md += "Curva de raciones validadas por franja de 10 minutos desde las 12:00:\n\n```grafico\ntipo: lineas\n"
    md += f"titulo: Raciones por franja, {esc['Perfil']} ({a.escenario})\nunidad: raciones\n\nFranja, Registros reales, Modelo\n"
    for _, f in curva.iterrows():
        md += f"{f['Franja']}, {f['Real']:.1f}, {f['Modelo']:.1f}\n"
    md += "```\n\n" + tabla_md(["Franja", "Real (media)", "Modelo", "Mín real", "Máx real"], curva.round(1).values.tolist()) + "\n"
    md += ("La primera franja da menos que la real porque la caja abre con demora (S25). "
           "El último valor corresponde a las 14:30, con muy pocas llegadas.\n\n")
    md += f"## 3. Contra la réplica independiente ({a.replicas} réplicas)\n\n"
    md += (f"Una corrida de FlexSim es una sola muestra: se acepta si queda a menos de {Z_REPLICA:.0f} desvíos estándar "
           "de la media de la réplica. Con 12 indicadores, es esperable que alguno salga apenas del rango por azar.\n\n")
    md += tabla_md(["Indicador", "FlexSim", "Réplica (media)", "Desvío", "z", "Estado"],
                   [(k, round(v, 2), round(m, 2), round(d, 2), round(z, 2), e) for k, v, m, d, z, e in replica]) + "\n"
    md += "## 4. Ley de Little\n\n" + tabla_md(["Cálculo", "Valor"], little) + "\n"
    md += ("Las dos primeras filas son el mismo cálculo y no prueban nada por sí solas: lo que valida es contrastarlas con el "
           "contenido medio que mide FlexSim en `Esperar en la fila` (opción `--little`).\n\n")
    md += f"## 5. Resumen\n\n{len(malos)} chequeo(s) para revisar.\n"
    salida = RAIZ / "flexsim" / f"validacion_{a.escenario}.md"
    salida.write_text(md, encoding="utf-8", newline="\n")

    print(f"Validación de {a.escenario}: {len(p)} personas, {med['Raciones']} raciones\n")
    for titulo, filas in (("Verificación interna", interna), ("Contra la realidad", realidad)):
        print(titulo)
        for f in filas:
            print(f"  [{f[2]:>8}] {f[0]}: {f[1]}")
        print()
    print("Contra la réplica")
    for k, v, m, d, z, e in replica:
        print(f"  [{e:>8}] {k}: FlexSim {v:.2f} | réplica {m:.2f} ± {d:.2f} (z = {z:+.2f})")
    print(f"\n{len(malos)} chequeo(s) para revisar. Informe en {salida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
