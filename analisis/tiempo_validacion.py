"""Estima el tiempo de validación en el puesto de control a partir de los
registros reales (dato DERIVADO, no generado).

Razonamiento: el check-in (`checked_at`) se registra en el puesto de control y
habitualmente opera un solo puesto (confirmado por el referente). En las franjas
de 10 minutos con mayor cantidad de validaciones el puesto está ocupado todo el
tiempo, así que el intervalo entre dos check-ins consecutivos es el tiempo de
servicio de esa validación.

Salidas:
  data/procesado/intervalos_saturados.csv  muestra para ajustar en ExpertFit
  data/procesado/tiempo_validacion.json    parámetros usados en supuestos.json

Uso: python analisis/tiempo_validacion.py   (desde la raíz del TPI)
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data" / "real" / "TP-SIM - ds_app.csv"
PROCESADO = RAIZ / "data" / "procesado"
TZ = "America/Argentina/Cordoba"

UMBRAL_FRANJA = 140   # validaciones en 10 min para considerar el puesto saturado
MAX_INTERVALO = 30    # s; intervalos mayores son huecos sin cola, no servicio


def main():
    df = pd.read_csv(CSV, na_values=["NULL"])
    df["checked_at"] = pd.to_datetime(df["checked_at"], format="ISO8601", utc=True).dt.tz_convert(TZ)
    df = df.sort_values("checked_at")
    df["intervalo_s"] = df.groupby("event_date")["checked_at"].diff().dt.total_seconds()
    df["franja"] = df["checked_at"].dt.floor("10min")
    por_franja = df.groupby("franja").size()
    saturadas = por_franja[por_franja >= UMBRAL_FRANJA]

    muestra = df[df["franja"].isin(saturadas.index) & (df["intervalo_s"] < MAX_INTERVALO)]
    muestra = muestra.dropna(subset=["intervalo_s"])
    PROCESADO.mkdir(parents=True, exist_ok=True)
    muestra[["event_date", "checked_at", "intervalo_s"]].to_csv(
        PROCESADO / "intervalos_saturados.csv", index=False)

    x = muestra["intervalo_s"]
    log = np.log(x)
    mu, sigma = float(log.mean()), float(log.std())
    resultado = {
        "criterio": f"franjas de 10 min con >= {UMBRAL_FRANJA} validaciones; intervalos < {MAX_INTERVALO} s",
        "franjas_saturadas": int(len(saturadas)),
        "n_intervalos": int(len(x)),
        "empirico": {
            "media_s": round(float(x.mean()), 2),
            "mediana_s": round(float(x.median()), 2),
            "desvio_s": round(float(x.std()), 2),
            "p05_s": round(float(x.quantile(.05)), 2),
            "p95_s": round(float(x.quantile(.95)), 2),
        },
        "lognormal": {
            "mu": round(mu, 3),
            "sigma": round(sigma, 3),
            "mediana_s": round(float(np.exp(mu)), 2),
            "media_s": round(float(np.exp(mu + sigma ** 2 / 2)), 2),
        },
        "capacidad_1_puesto_por_hora": round(3600 / float(x.mean())),
        "maximo_observado_10min": int(por_franja.max()),
    }
    (PROCESADO / "tiempo_validacion.json").write_text(
        json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resultado, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
