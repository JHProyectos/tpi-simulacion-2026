"""Fase 3: completa el dataset real con los datos generados declarados en
supuestos/supuestos.json (S11 a S14). Las filas reales no se modifican.

Salidas:
  data/generado/reservas_generadas.csv  solo las filas sintéticas (no_show, canceled)
  data/final/reservas_completo.csv      reales + generadas, con origen por fila y por columna
  data/final/resumen.json               conteos que usa el reporte

Uso: python analisis/generar_datos.py   (desde la raíz del TPI)
"""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data" / "real" / "TP-SIM - ds_app.csv"
SUPUESTOS = RAIZ / "supuestos" / "supuestos.json"
GENERADO = RAIZ / "data" / "generado"
FINAL = RAIZ / "data" / "final"
TZ = "America/Argentina/Cordoba"

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from organizar_por_tipo import GRUPOS, ORDEN_GRUPOS  # noqa: E402

COLUMNAS_REALES = ["event_date", "reserved_at", "canceled_at", "checked_at", "status",
                   "customer_id", "customer_types"]


def parametros():
    d = json.loads(SUPUESTOS.read_text(encoding="utf-8"))
    s = {x["id"]: x for x in d["supuestos"]}
    return d["semilla"], {k: s[k]["parametros"] for k in ("S11", "S12", "S13", "S14")}


def huella(df):
    """Hash de las columnas reales, para verificar que no se alteraron."""
    texto = df[COLUMNAS_REALES].astype(str).to_csv(index=False)
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def cargar_real():
    crudo = pd.read_csv(CSV, na_values=["NULL"])
    df = crudo.copy()
    for c in ["reserved_at", "canceled_at", "checked_at"]:
        df[c] = pd.to_datetime(df[c], format="ISO8601", utc=True).dt.tz_convert(TZ)
    df["grupo"] = df["customer_types"].map(GRUPOS)
    df["origen_fila"] = "real"
    df["reserva_id"] = "R-" + df["customer_id"].astype(str).str.zfill(5)
    return crudo, df


def hora(dia, hhmm):
    return pd.Timestamp(f"{dia} {hhmm}", tz=TZ)


def generar_filas(real, p, rng):
    """Filas no_show (S11) y canceled (S12), muestreando tipo y hora de reserva
    de las reservas reales del mismo día y grupo."""
    filas = []
    p_ns = p["S11"]["p_no_show"]
    p_c = p["S12"]["p_cancelacion"]
    for (dia, grupo), sub in real.groupby(["event_date", "grupo"]):
        n_real = len(sub)
        # Retiradas = (1 - p_ns) de las no canceladas; no canceladas = (1 - p_c) del total.
        n_ns = rng.binomial(round(n_real / (1 - p_ns[grupo])), p_ns[grupo])
        n_c = rng.binomial(round((n_real + n_ns) / (1 - p_c)), p_c)
        for estado, n in (("no_show", n_ns), ("canceled", n_c)):
            if n == 0:
                continue
            base = sub.iloc[rng.integers(0, n_real, n)]
            jitter = pd.Series(pd.to_timedelta(rng.uniform(-60, 60, n), unit="s"))
            inicio, corte = hora(dia, "08:00"), hora(dia, "11:00")
            reservado = base["reserved_at"].reset_index(drop=True) + jitter
            # Si el jitter cae antes de la apertura de reservas, se refleja hacia adentro.
            reservado = reservado.where(reservado >= inicio, inicio + (inicio - reservado)).dt.round("ms")
            gen = pd.DataFrame({
                "event_date": dia,
                "reserved_at": reservado.to_numpy(),
                "customer_types": base["customer_types"].to_numpy(),
                "grupo": grupo,
                "status": estado,
            })
            gen["canceled_at"] = pd.NaT
            gen["checked_at"] = pd.NaT
            if estado == "canceled":
                # Cancelación uniforme entre la reserva y el corte; si reservó después
                # del corte, dentro de los 30 minutos siguientes.
                fin = gen["reserved_at"].where(gen["reserved_at"] >= corte, corte)
                fin = fin.where(gen["reserved_at"] < corte, gen["reserved_at"] + pd.Timedelta(minutes=30))
                frac = rng.uniform(0.02, 1, len(gen))
                gen["canceled_at"] = (gen["reserved_at"] + (fin - gen["reserved_at"]) * frac).dt.round("ms")
            filas.append(gen)
    gen = pd.concat(filas, ignore_index=True)
    gen["canceled_at"] = pd.to_datetime(gen["canceled_at"]).dt.tz_convert(TZ)
    gen["checked_at"] = pd.to_datetime(gen["checked_at"], utc=True).dt.tz_convert(TZ)
    gen = gen.sort_values(["event_date", "reserved_at"]).reset_index(drop=True)
    gen["origen_fila"] = "generado_ia"
    gen["reserva_id"] = "G-" + (gen.index + 1).astype(str).str.zfill(5)
    gen["customer_id"] = pd.NA
    return gen


def asignar_atributos(df, p, rng):
    """Columnas generadas sobre todas las filas: menú (S13) y para llevar (S14)."""
    df["menu_gen"] = np.where(rng.random(len(df)) < p["S13"]["p_vegetariano"], "vegetariano", "no_vegetariano")
    vianda = df["customer_types"].isin(p["S14"]["tipos_vianda"])
    prob = np.where(vianda, p["S14"]["p_llevar_vianda"], p["S14"]["p_llevar_resto"])
    llevar = rng.random(len(df)) < prob
    # Solo tiene sentido para quien retira la comida.
    df["para_llevar_gen"] = pd.Series(llevar, index=df.index).where(df["status"] == "used")
    return df


def main():
    semilla, p = parametros()
    rng = np.random.default_rng(semilla)
    crudo, real = cargar_real()
    huella_antes = huella(crudo)

    gen = generar_filas(real, p, rng)
    completo = pd.concat([real, gen], ignore_index=True)
    completo = completo.sort_values(["event_date", "reserved_at", "reserva_id"]).reset_index(drop=True)
    completo = asignar_atributos(completo, p, rng)
    completo["sin_tacc"] = completo["customer_types"].str.contains("sin TACC")
    completo["re_reserva"] = (completo["origen_fila"] == "real") & completo["canceled_at"].notna()

    cols = ["reserva_id", "origen_fila", "event_date", "grupo", "customer_types", "sin_tacc",
            "status", "reserved_at", "canceled_at", "checked_at", "re_reserva",
            "menu_gen", "para_llevar_gen", "customer_id"]
    completo = completo[cols]

    # Verificación: las filas reales del archivo final coinciden con el CSV original.
    reales = completo[completo["origen_fila"] == "real"].sort_values("customer_id")
    control = crudo.sort_values("customer_id").reset_index(drop=True)
    assert len(reales) == len(control), "Se perdieron o duplicaron filas reales"
    assert (reales["checked_at"].reset_index(drop=True)
            == pd.to_datetime(control["checked_at"], format="ISO8601", utc=True).dt.tz_convert(TZ)).all()
    assert huella(pd.read_csv(CSV, na_values=["NULL"])) == huella_antes, "El CSV original cambió"

    GENERADO.mkdir(parents=True, exist_ok=True)
    FINAL.mkdir(parents=True, exist_ok=True)
    completo[completo["origen_fila"] == "generado_ia"].to_csv(GENERADO / "reservas_generadas.csv", index=False)
    completo.to_csv(FINAL / "reservas_completo.csv", index=False)

    usados = completo[completo["status"] == "used"]
    no_cancel = completo[completo["status"] != "canceled"]
    resumen = {
        "semilla": semilla,
        "total_reservas": int(len(completo)),
        "por_estado": {e: {"n": int((completo["status"] == e).sum()),
                           "origen": "real" if e == "used" else "generado_ia"}
                       for e in ["used", "no_show", "canceled"]},
        "ausentismo_por_grupo": {g: round(float((no_cancel[no_cancel["grupo"] == g]["status"] == "no_show").mean()), 4)
                                 for g in ORDEN_GRUPOS},
        "cancelacion": round(float((completo["status"] == "canceled").mean()), 4),
        "vegetariano": round(float((completo["menu_gen"] == "vegetariano").mean()), 4),
        "para_llevar": round(float(usados["para_llevar_gen"].astype(bool).mean()), 4),
        "comen_en_salon_por_dia": {
            "pico": round(float((~usados["para_llevar_gen"].astype(bool)).groupby(usados["event_date"]).sum()
                                .loc[lambda s: s.index >= "2026-08-10"].median()), 1),
        },
        "huella_csv_real": huella_antes,
    }
    (FINAL / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
