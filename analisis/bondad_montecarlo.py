"""Prueba de bondad de ajuste (chi-cuadrado) de los tiempos entre llegadas y
Monte Carlo de la categoría de cliente, con los datos reales del comedor.

Entrada: data/procesado/ds_app_organizado.csv (reservas retiradas, jul-sep 2026)
Salida:  analisis/Prueba de Bondad de Ajuste y Monte Carlo (datos reales).docx
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from docx import Document
from docx.shared import Pt

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data/procesado/ds_app_organizado.csv"
SALIDA = RAIZ / "analisis/Prueba de Bondad de Ajuste y Monte Carlo (datos reales).docx"
DIA = "2026-07-01"
ALFA = 0.05
K = 8              # intervalos equiprobables por prueba
SEMILLA = 2026
REPLICAS = 1000

def num(x, d=2):
    """Número con coma decimal y punto de miles."""
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def chi2_exponencial(dt):
    """Chi-cuadrado contra Exp(λ = 1/media) con K intervalos equiprobables."""
    n = len(dt)
    media = dt.mean()
    lam = 1 / media
    # límites: cuantiles de la exponencial -> cada intervalo tiene p = 1/K
    lims = [-np.log(1 - i / K) / lam for i in range(K)] + [np.inf]
    obs = np.histogram(dt, bins=lims)[0]
    esp = np.full(K, n / K)
    contrib = (obs - esp) ** 2 / esp
    chi = contrib.sum()
    gl = K - 1 - 1
    crit = stats.chi2.ppf(1 - ALFA, gl)
    return dict(n=n, media=media, lam=lam, lims=lims, obs=obs, esp=esp,
                contrib=contrib, chi=chi, gl=gl, crit=crit,
                p=stats.chi2.sf(chi, gl), cv=dt.std(ddof=1) / media)

def tabla(doc, encabezado, filas):
    t = doc.add_table(rows=1, cols=len(encabezado))
    t.style = "Light Grid Accent 1"
    for c, txt in zip(t.rows[0].cells, encabezado):
        c.text = txt
    for f in filas:
        for c, txt in zip(t.add_row().cells, f):
            c.text = str(txt)
    doc.add_paragraph()

def main():
    d = pd.read_csv(CSV)
    d["checked"] = pd.to_datetime(d.checked_at, format="ISO8601").dt.tz_localize(None)
    doc = Document()
    doc.styles["Normal"].font.size = Pt(11)
    doc.add_heading("Prueba de Bondad de Ajuste y Monte Carlo", 0)
    doc.add_paragraph(
        "Fuente: registro real de la app del comedor (ds_app_organizado.csv, 34.509 "
        "reservas retiradas entre julio y septiembre de 2026). Todos los valores de este "
        "documento se calculan con el script analisis/bondad_montecarlo.py; no hay datos generados.")

    # ---------------- 1. Chi-cuadrado ----------------
    x = d.loc[d.event_date == DIA, "checked"].sort_values()
    dt_all = x.diff().dt.total_seconds().iloc[1:].to_numpy()
    franja_ini = x.iloc[1:].dt.floor("30min").to_numpy()
    # la franja 14:30 tiene sólo 5 llegadas: se une a la de 14:00
    franja_ini = np.where(pd.to_datetime(franja_ini).hour * 60 + pd.to_datetime(franja_ini).minute >= 14 * 60 + 30,
                          np.datetime64(f"{DIA}T14:00"), franja_ini)

    doc.add_heading("1. Prueba Chi-cuadrado del tiempo entre llegadas", 1)
    doc.add_paragraph(
        f"Se toman las {len(x)} validaciones del {DIA[8:]}/07/2026 (primera {x.iloc[0]:%H:%M:%S}, "
        f"última {x.iloc[-1]:%H:%M:%S}) y se calculan los {len(dt_all)} tiempos entre llegadas "
        f"consecutivas (Δt). Se prueba si Δt sigue una distribución Exponencial, primero en todo el "
        f"servicio y después dentro de cada franja de 30 minutos.")
    doc.add_paragraph(
        f"Método: λ se estima como 1/x̄. Se usan k = {K} intervalos equiprobables (cada uno con "
        f"probabilidad teórica 1/{K}), así Ei = n/{K} ≥ 5 en todos. Grados de libertad: "
        f"gl = k − 1 − m = {K} − 1 − 1 = {K-2}. Nivel de significación α = {ALFA}.")
    doc.add_paragraph("H0: Δt se distribuye Exponencial con λ = 1/x̄.\nH1: Δt no sigue una distribución Exponencial.")

    g = chi2_exponencial(dt_all)
    doc.add_heading("1.1 Todo el servicio", 2)
    doc.add_paragraph(f"n = {g['n']}, x̄ = {num(g['media'])} s, λ = {num(g['lam'],4)} llegadas/s, "
                      f"coeficiente de variación = {num(g['cv'])} (en la exponencial vale 1).")
    filas = []
    for i in range(K):
        hi = "∞" if np.isinf(g["lims"][i+1]) else num(g["lims"][i+1])
        filas.append([f"[{num(g['lims'][i])} ; {hi})", g["obs"][i], num(g["esp"][i]), num(g["contrib"][i])])
    filas.append(["Total", g["n"], num(g["n"]), num(g["chi"])])
    tabla(doc, ["Intervalo Δt (s)", "Oi", "Ei", "(Oi − Ei)² / Ei"], filas)
    rech = g["chi"] > g["crit"]
    doc.add_paragraph(
        f"χ²calc = {num(g['chi'])}; χ²crít(0,05; {g['gl']}) = {num(g['crit'],3)}; valor p = {num(g['p'],4)}. "
        + ("Se rechaza H0." if rech else "No se rechaza H0."))

    doc.add_heading("1.2 Por franja horaria", 2)
    filas, res = [], []
    for ini in sorted(set(franja_ini)):
        m = franja_ini == ini
        r = chi2_exponencial(dt_all[m])
        t0 = pd.Timestamp(ini)
        fin = "14:35" if t0.hour == 14 else f"{(t0 + pd.Timedelta(minutes=30)):%H:%M}"
        etiqueta = f"{t0:%H:%M} – {fin}"
        res.append((etiqueta, r))
        filas.append([etiqueta, r["n"], num(r["media"]), num(r["lam"], 4), num(r["cv"]),
                      num(r["chi"]), num(r["crit"], 3), num(r["p"], 4),
                      "Rechaza" if r["chi"] > r["crit"] else "No rechaza"])
    tabla(doc, ["Franja (hs)", "n", "x̄ (s)", "λ (1/s)", "CV", "χ²calc", "χ²crít", "p", "H0"], filas)
    no_rech = [e for e, r in res if r["chi"] <= r["crit"]]
    doc.add_heading("1.3 Conclusión", 2)
    medias = ", ".join(f"{e}: {num(r['media'])} s" for e, r in res)
    doc.add_paragraph(
        f"El tiempo medio entre llegadas cambia a lo largo del servicio ({medias}). "
        + ("Con una sola exponencial para todo el horario se rechaza H0, porque mezcla franjas con tasas distintas. "
           if rech else "Aun con una sola exponencial global no se rechaza H0, pero la media varía entre franjas. ")
        + (f"Dentro de las franjas no se rechaza H0 en: {', '.join(no_rech)}. " if no_rech else
           "Tampoco se ajusta dentro de cada franja. ")
        )
    q = np.percentile(dt_all, [5, 50])
    doc.add_paragraph(
        "Motivo del rechazo: el registro guarda la hora de validación (checked_at), no la de llegada a la fila. "
        "Mientras hay cola, una persona valida apenas termina la anterior, así que Δt mide el tiempo de "
        f"atención del puesto y no el tiempo entre arribos. Por eso casi no hay Δt cortos (percentil 5 = "
        f"{num(q[0])} s, mediana = {num(q[1])} s), y la exponencial exige muchos valores cercanos a 0. "
        f"Hay {int((dt_all < 2).sum())} Δt menores a 2 s de {len(dt_all)}, y el coeficiente de variación "
        f"global es {num(g['cv'])}.")
    doc.add_paragraph(
        "Implicancia para el modelo: estos datos no permiten estimar directamente la distribución de "
        "llegadas a la fila, porque están filtrados por la cola. Las medias por franja sirven como cota "
        "inferior de la tasa de llegada en hora pico (la fila nunca se vacía). Para las llegadas se mantiene "
        "el supuesto de Poisson con λ variable por franja, a validar con observación de campo (conteo de "
        "personas que se suman a la fila por minuto). Los Δt de las franjas con cola sirven, en cambio, "
        "como estimación del tiempo de validación.")

    # ---------------- 2. Monte Carlo ----------------
    doc.add_heading("2. Monte Carlo: categoría de cliente", 1)
    d["mes"] = d.event_date.str[:7]
    ct = pd.crosstab(d.customer_types, d.mes)
    ct["Total"] = ct.sum(axis=1)
    ct = ct.sort_values("Total", ascending=False)
    N = ct["Total"].sum()
    ultimo = d.event_date.max()
    doc.add_paragraph(
        f"Raciones retiradas por categoría y mes. Septiembre está incompleto: el registro termina "
        f"el {ultimo[8:]}/{ultimo[5:7]}/2026. Por eso se usa el total del período y no los meses por separado.")
    filas = [[c, *[num(v, 0) for v in ct.loc[c, ["2026-07", "2026-08", "2026-09"]]],
              num(ct.loc[c, "Total"], 0), num(ct.loc[c, "Total"] / N * 100) + " %"] for c in ct.index]
    tot = ct.sum()
    filas.append(["Total", num(tot["2026-07"], 0), num(tot["2026-08"], 0), num(tot["2026-09"], 0), num(N, 0), "100,00 %"])
    tabla(doc, ["Categoría", "Julio", "Agosto", "Septiembre*", "Total", "%"], filas)

    # intervalos de 4 dígitos: u en 0000..9999
    p = ct["Total"] / N
    acum = p.cumsum()
    lim_sup = np.round(acum.to_numpy() * 10000).astype(int) - 1
    lim_sup[-1] = 9999
    lim_inf = np.r_[0, lim_sup[:-1] + 1]
    doc.add_paragraph(
        "Con dos dígitos (00–99) las categorías de menos de 0,5 % quedan sin intervalo, así que se usan "
        "números aleatorios de cuatro dígitos u ∈ [0000, 9999]. Cada categoría recibe "
        "un intervalo de largo proporcional a su probabilidad (transformada inversa discreta).")
    filas = []
    for i, c in enumerate(ct.index):
        largo = lim_sup[i] - lim_inf[i] + 1
        rango = f"{lim_inf[i]:04d} – {lim_sup[i]:04d}" if largo > 0 else "(sin intervalo: p < 0,00005)"
        filas.append([c, num(ct.loc[c, "Total"], 0), num(p.iloc[i], 4), num(acum.iloc[i], 4), rango])
    tabla(doc, ["Categoría", "Raciones", "Pi", "Fi", "Intervalo u"], filas)

    rng = np.random.default_rng(SEMILLA)
    u = rng.integers(0, 10000, REPLICAS)
    idx = np.searchsorted(lim_sup, u)
    sim = pd.Series(ct.index[idx])
    doc.add_paragraph(
        f"Se simulan {REPLICAS} clientes con un generador pseudoaleatorio (numpy, semilla {SEMILLA}, "
        "reproducible). Primeros 10 clientes:")
    tabla(doc, ["Cliente", "u", "Categoría simulada"], [[i+1, f"{u[i]:04d}", sim[i]] for i in range(10)])

    frec = sim.value_counts().reindex(ct.index, fill_value=0)
    filas = [[c, frec[c], num(frec[c] / REPLICAS * 100) + " %", num(p[c] * 100) + " %"] for c in ct.index]
    tabla(doc, ["Categoría", "Frecuencia simulada", "% simulado", "% teórico"], filas)

    # chi2 simulado vs teórico, agrupando categorías con Ei < 5
    esp = p * REPLICAS
    grandes = esp >= 5
    O = list(frec[grandes]) + [frec[~grandes].sum()]
    E = list(esp[grandes]) + [esp[~grandes].sum()]
    chi = sum((o - e) ** 2 / e for o, e in zip(O, E))
    gl = len(O) - 1
    crit = stats.chi2.ppf(1 - ALFA, gl)
    doc.add_paragraph(
        f"Verificación: χ² entre lo simulado y lo teórico, agrupando en «Otras» las categorías con Ei < 5 "
        f"({len(O)} clases, gl = {gl}): χ²calc = {num(chi)}; χ²crít = {num(crit,3)}. "
        + ("No se rechaza que la simulación reproduzca la distribución real de categorías."
           if chi <= crit else "Se rechaza: revisar el generador."))

    doc.save(SALIDA)
    print("OK", SALIDA)
    print("global", g["chi"], g["crit"], g["media"])
    for e, r in res:
        print(e, r["n"], round(r["media"], 2), round(r["chi"], 2), round(r["crit"], 2))
    print("mc", chi, crit)

if __name__ == "__main__":
    main()
