"""Procesa el informe HTML del Experimenter de FlexSim (ReporteCompleto.html).

Lee los datos por réplica (8 medidas x 12 escenarios x 30 réplicas), escribe
flexsim/experimenter/replicas.csv y flexsim/experimenter/RESULTADOS.md con medias,
intervalos de confianza al 95 % y comparaciones pareadas entre escenarios.

Uso:  python -I analisis/procesar_experimenter.py
"""
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "flexsim" / "experimenter"
HTML = CARPETA / "ReporteCompleto.html"

# t de Student bilateral al 95 % para n-1 grados de libertad (n = 30 -> 29)
T95 = {9: 2.262, 14: 2.145, 19: 2.093, 24: 2.064, 29: 2.045, 49: 2.010, 99: 1.984}

MEDIDAS = {
    "TiempoTotal_min": ("Tiempo total medio en el sistema", "min", 2),
    "EsperaMaxCaja_min": ("Espera máxima en la caja desde la apertura", "min", 2),
    "EsperaServicio_min": ("Espera media en la fila de servicio", "min", 3),
    "CajaBloqueada_min": ("Tiempo con la caja bloqueada", "min", 2),
    "UtilizacionCaja_pct": ("Utilización de la caja", "%", 1),
    "ColaCajaMax": ("Cola máxima en la caja", "personas", 1),
    "ColaServicioMax": ("Cola máxima en el servicio", "personas", 1),
    "PersonasDia": ("Personas del día", "personas", 0),
}

# (comparación, escenario A, escenario B): se mide B - A
COMPARACIONES = [
    ("E1 contra E0: segundo puesto todo el turno", "E0", "E1"),
    ("E2 contra E0: segundo puesto de 12:00 a 13:30", "E0", "E2"),
    ("E3 contra E0: validación por QR", "E0", "E3"),
    ("E4 contra E0: 4.ª persona sirviendo", "E0", "E4"),
    ("E5 contra E0: segundo puesto y 4.ª persona", "E0", "E5"),
    ("E5 contra E1: sumar la 4.ª persona al segundo puesto", "E1", "E5"),
]
MEDIDAS_COMPARADAS = ["TiempoTotal_min", "EsperaMaxCaja_min", "EsperaServicio_min", "ColaServicioMax"]


def cargar():
    t = HTML.read_text(encoding="utf-8")
    i = t.find("var pfmData =") + len("var pfmData = ")
    m = re.search(r"\]\s*;\s*var validStatData", t[i:])
    pfm = json.loads(t[i:i + m.start() + 1])
    j = t.find("var scenarioData =") + len("var scenarioData = ")
    m = re.search(r"\]\s*;", t[j:])
    esc = json.loads(t[j:j + m.start() + 1])
    nombres = [e["name"] for e in sorted(esc, key=lambda e: e["id"])]
    datos = {p["name"]: np.array(p["data"], dtype=float) for p in pfm}
    return nombres, datos


def t_crit(gl):
    for k in sorted(T95):
        if gl <= k:
            return T95[k]
    return 1.96


def fmt(x, dec):
    return f"{x:.{dec}f}".replace(".", ",")


def media_ic(v):
    n = len(v)
    m = v.mean()
    h = t_crit(n - 1) * v.std(ddof=1) / math.sqrt(n)
    return m, h


def pareada(a, b):
    d = b - a
    n = len(d)
    m = d.mean()
    s = d.std(ddof=1)
    h = t_crit(n - 1) * s / math.sqrt(n)
    return m, h


def main():
    nombres, datos = cargar()
    nrep = next(iter(datos.values())).shape[1]
    idx = {n: k for k, n in enumerate(nombres)}

    # --- CSV por réplica ---
    lineas = ["Escenario,Rep," + ",".join(datos)]
    for n, k in idx.items():
        for r in range(nrep):
            lineas.append(f"{n},{r + 1}," + ",".join(f"{datos[med][k, r]:.6g}" for med in datos))
    (CARPETA / "replicas.csv").write_text("\n".join(lineas) + "\n", encoding="utf-8")

    out = []
    w = out.append
    w("# Resultados del Experimenter")
    w("")
    w("[TOC]")
    w("")
    w(f"Generado con `analisis/procesar_experimenter.py` a partir de `flexsim/experimenter/ReporteCompleto.html`. "
      f"Son {len(nombres)} escenarios por {nrep} réplicas, simulación terminante de un día (11:40 a 16:00, calentamiento 0). "
      f"Los intervalos son de confianza al 95 % con la t de Student. Las réplicas por escenario comparten los mismos números "
      f"aleatorios (las personas del día son idénticas entre escenarios del mismo perfil), por eso las comparaciones son **pareadas**.")
    w("")

    for perfil in ("Pico", "Bajo"):
        esc = [n for n in nombres if n.endswith(perfil)]
        w(f"## Perfil {perfil.lower()}")
        w("")
        w("Media de las réplicas, con el semiancho del intervalo de confianza al 95 % (±).")
        w("")
        cols = [m for m in MEDIDAS if m != "PersonasDia"]
        w("| Escenario | " + " | ".join(f"{MEDIDAS[m][0]} ({MEDIDAS[m][1]})" for m in cols) + " |")
        w("|---|" + "---|" * len(cols))
        for n in esc:
            celdas = []
            for m in cols:
                mu, h = media_ic(datos[m][idx[n]])
                celdas.append(f"{fmt(mu, MEDIDAS[m][2])} ± {fmt(h, MEDIDAS[m][2])}")
            w(f"| {n.split('_')[0]} | " + " | ".join(celdas) + " |")
        w("")

        w(f"### Comparaciones pareadas, perfil {perfil.lower()}")
        w("")
        w("Diferencia media (escenario menos base) con su intervalo. **Significativa** si el intervalo no incluye el cero.")
        w("")
        w("| Comparación | Medida | Diferencia media | Intervalo 95 % | ¿Significativa? |")
        w("|---|---|---|---|---|")
        for titulo, a, b in COMPARACIONES:
            for m in MEDIDAS_COMPARADAS:
                d, h = pareada(datos[m][idx[f"{a}_{perfil}"]], datos[m][idx[f"{b}_{perfil}"]])
                dec = MEDIDAS[m][2]
                sig = "sí" if abs(d) > h else "no"
                w(f"| {titulo} | {MEDIDAS[m][0]} ({MEDIDAS[m][1]}) | {fmt(d, dec)} | "
                  f"[{fmt(d - h, dec)}; {fmt(d + h, dec)}] | {sig} |")
        w("")

    for m, titulo in (("EsperaMaxCaja_min", "Espera máxima en la caja (min), perfil pico"),
                      ("ColaServicioMax", "Cola máxima en el servicio (personas), perfil pico"),
                      ("TiempoTotal_min", "Tiempo total medio (min), perfil pico")):
        w(f"### {titulo}")
        w("")
        w("```grafico")
        w("tipo: barras")
        w(f"titulo: {titulo}")
        w("unidad: " + MEDIDAS[m][1])
        w("")
        w("Escenario, Media")
        for n in [x for x in nombres if x.endswith("Pico")]:
            w(f"{n.split('_')[0]}, {media_ic(datos[m][idx[n]])[0]:.3f}")
        w("```")
        w("")

    w("## Réplicas necesarias")
    w("")
    w("Semiancho relativo del intervalo (semiancho dividido por la media) con las 30 réplicas. "
      "Si es menor que 5 % la precisión alcanza; si es mayor, hay que subir las réplicas con $n \\approx (t\\,s/h)^2$.")
    w("")
    w("| Medida | Peor semiancho relativo (pico) | Escenario |")
    w("|---|---|---|")
    for m in MEDIDAS:
        if m == "PersonasDia":
            continue
        peor, ep = 0, ""
        for n in [x for x in nombres if x.endswith("Pico")]:
            mu, h = media_ic(datos[m][idx[n]])
            if mu > 1e-9 and h / mu > peor:
                peor, ep = h / mu, n.split("_")[0]
        w(f"| {MEDIDAS[m][0]} | {fmt(100 * peor, 1)} % | {ep} |")
    w("")
    (CARPETA / "RESULTADOS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("OK:", CARPETA / "RESULTADOS.md", "y", CARPETA / "replicas.csv")


if __name__ == "__main__":
    sys.exit(main())
