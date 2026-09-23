"""Organiza el dataset de reservas del comedor por tipo de cliente y genera
los datos agregados que consume el reporte (reporte/datos.json).

Uso: python analisis/organizar_por_tipo.py   (desde la raíz del TPI)
"""
import json
import re
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data" / "real" / "TP-SIM - ds_app.csv"
PROCESADO = RAIZ / "data" / "procesado"
SALIDA_TIPOS = PROCESADO / "por_tipo"
SALIDA_JSON = RAIZ / "reporte" / "datos.json"
TZ = "America/Argentina/Cordoba"

# Cada tipo del sistema se agrupa en una de cuatro familias de cliente.
GRUPOS = {
    "Estudiante de Grado": "Estudiantes",
    "Estudiante de Grado sin TACC": "Estudiantes",
    "Estudiante de Grado Centro sin TACC": "Estudiantes",
    "Estudiante Preuniversitario Monserrat": "Estudiantes",
    "Usuario de Postgrado": "Estudiantes",
    "Becas Nutrirse Vianda": "Becas Nutrirse",
    "Becas Nutrirse Vianda sin TACC": "Becas Nutrirse",
    "Becas Nodocentes": "Becas personal",
    "Becas Nodocentes sin TACC": "Becas personal",
    "Becas Docentes": "Becas personal",
    "Docente": "Personal",
    "Docente sin TACC": "Personal",
    "Nodocente": "Personal",
    "Nodocente sin TACC": "Personal",
}
ORDEN_GRUPOS = ["Estudiantes", "Becas Nutrirse", "Becas personal", "Personal"]


def cargar():
    df = pd.read_csv(CSV, na_values=["NULL"])
    for c in ["reserved_at", "canceled_at", "checked_at"]:
        df[c] = pd.to_datetime(df[c], format="ISO8601", utc=True).dt.tz_convert(TZ)
    df["event_date"] = pd.to_datetime(df["event_date"]).dt.date
    df["grupo"] = df["customer_types"].map(GRUPOS)
    sin_mapear = df.loc[df["grupo"].isna(), "customer_types"].unique()
    if len(sin_mapear):
        raise ValueError(f"Tipos sin grupo asignado: {sin_mapear}")
    df["sin_tacc"] = df["customer_types"].str.contains("sin TACC")
    df["anticipacion_min"] = (df["checked_at"] - df["reserved_at"]).dt.total_seconds() / 60
    df["re_reserva"] = df["canceled_at"].notna()
    return df


def slug(texto):
    return re.sub(r"[^a-z0-9]+", "_", texto.lower()).strip("_")


def exportar_csvs(df):
    SALIDA_TIPOS.mkdir(parents=True, exist_ok=True)
    orden = df.assign(g=pd.Categorical(df["grupo"], ORDEN_GRUPOS, ordered=True))
    orden = orden.sort_values(["g", "customer_types", "event_date", "checked_at"]).drop(columns="g")
    cols = ["grupo", "customer_types", "sin_tacc", "event_date", "reserved_at",
            "canceled_at", "checked_at", "anticipacion_min", "status", "customer_id"]
    orden[cols].to_csv(PROCESADO / "ds_app_organizado.csv", index=False)
    for grupo, sub in orden.groupby("grupo", sort=False):
        sub[cols].to_csv(SALIDA_TIPOS / f"{slug(grupo)}.csv", index=False)


def minutos_del_dia(serie):
    return serie.dt.hour * 60 + serie.dt.minute + serie.dt.second / 60


def resumen(df):
    dias = sorted(df["event_date"].unique())
    n_dias = len(dias)

    por_tipo = []
    for tipo, g in df.groupby("customer_types"):
        por_tipo.append({
            "tipo": tipo,
            "grupo": GRUPOS[tipo],
            "sin_tacc": bool(g["sin_tacc"].iloc[0]),
            "n": int(len(g)),
            "dias_con_uso": int(g["event_date"].nunique()),
            "prom_dia": round(len(g) / n_dias, 1),
            "reserva_mediana": round(float(minutos_del_dia(g["reserved_at"]).median()), 1),
            "checkin_mediana": round(float(minutos_del_dia(g["checked_at"]).median()), 1),
            "anticipacion_media": round(float(g["anticipacion_min"].mean()), 1),
            "re_reservas": int(g["re_reserva"].sum()),
        })
    por_tipo.sort(key=lambda r: (ORDEN_GRUPOS.index(r["grupo"]), -r["n"]))

    diario = (df.groupby(["event_date", "grupo"]).size().unstack(fill_value=0)
                .reindex(columns=ORDEN_GRUPOS, fill_value=0))
    por_dia = [{"fecha": str(f), **{k: int(v) for k, v in fila.items()}}
               for f, fila in diario.iterrows()]

    # Llegadas (check-in) en franjas de 10 minutos, promedio por día de servicio.
    franja = (minutos_del_dia(df["checked_at"]) // 10 * 10).astype(int)
    llegadas = (df.assign(franja=franja).groupby(["franja", "grupo"]).size()
                  .unstack(fill_value=0).reindex(columns=ORDEN_GRUPOS, fill_value=0))
    llegadas = llegadas.reindex(range(int(llegadas.index.min()), int(llegadas.index.max()) + 10, 10),
                                fill_value=0)
    por_franja = [{"min": int(m), **{k: round(v / n_dias, 2) for k, v in fila.items()}}
                  for m, fila in llegadas.iterrows()]

    # Tiempos entre llegadas consecutivas dentro de cada día (insumo de simulación).
    ordenado = df.sort_values("checked_at")
    ia = ordenado.groupby("event_date")["checked_at"].diff().dt.total_seconds().dropna()
    pico = ordenado[ordenado["checked_at"].dt.hour.isin([12, 13])]
    ia_pico = pico.groupby("event_date")["checked_at"].diff().dt.total_seconds().dropna()
    ia_pico = ia_pico[ia_pico < 600]

    def describir(s):
        return {"n": int(len(s)), "media": round(float(s.mean()), 2),
                "mediana": round(float(s.median()), 2), "desvio": round(float(s.std()), 2),
                "cv": round(float(s.std() / s.mean()), 2),
                "p90": round(float(s.quantile(.9)), 2), "max": round(float(s.max()), 1)}

    dia_semana = (pd.to_datetime(pd.Series(df["event_date"])).dt.dayofweek
                  .value_counts().sort_index())
    dias_por_dow = pd.Series(pd.to_datetime(pd.Series(dias)).dt.dayofweek).value_counts()
    nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    por_dow = [{"dia": nombres[d], "total": int(dia_semana[d]), "dias": int(dias_por_dow[d]),
                "prom": round(dia_semana[d] / dias_por_dow[d], 1)} for d in dia_semana.index]

    hora_reserva = df["reserved_at"].dt.hour.value_counts().sort_index()
    hora_checkin = df["checked_at"].dt.hour.value_counts().sort_index()

    return {
        "totales": {
            "registros": int(len(df)), "dias": n_dias, "desde": str(dias[0]), "hasta": str(dias[-1]),
            "tipos": int(df["customer_types"].nunique()),
            "sin_tacc": int(df["sin_tacc"].sum()),
            "re_reservas": int(df["re_reserva"].sum()),
            "status": {k: int(v) for k, v in df["status"].value_counts().items()},
            "ids_unicos": int(df["customer_id"].nunique()),
            "prom_dia": round(len(df) / n_dias, 1),
            "max_dia": max(por_dia, key=lambda r: sum(r[g] for g in ORDEN_GRUPOS))["fecha"],
        },
        "grupos": [{"grupo": g, "n": int((df["grupo"] == g).sum()),
                    "tipos": int(df.loc[df["grupo"] == g, "customer_types"].nunique())}
                   for g in ORDEN_GRUPOS],
        "por_tipo": por_tipo,
        "por_dia": por_dia,
        "por_franja": por_franja,
        "por_dow": por_dow,
        "entre_llegadas": {"total": describir(ia), "pico_12_14": describir(ia_pico)},
        "anticipacion": describir(df["anticipacion_min"]),
        "hora_reserva": {int(k): int(v) for k, v in hora_reserva.items()},
        "hora_checkin": {int(k): int(v) for k, v in hora_checkin.items()},
    }


def main():
    df = cargar()
    exportar_csvs(df)
    SALIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    agregados = resumen(df)
    validacion = PROCESADO / "tiempo_validacion.json"
    if not validacion.exists():
        raise FileNotFoundError("Falta data/procesado/tiempo_validacion.json: correr antes analisis/tiempo_validacion.py")
    agregados["validacion"] = json.loads(validacion.read_text(encoding="utf-8"))
    datos = json.dumps(agregados, ensure_ascii=False, indent=1)
    SALIDA_JSON.write_text(datos, encoding="utf-8")
    supuestos = (RAIZ / "supuestos" / "supuestos.json").read_text(encoding="utf-8")
    plantilla = (SALIDA_JSON.parent / "plantilla.html").read_text(encoding="utf-8")
    html = plantilla.replace("__DATOS__", datos).replace("__SUPUESTOS__", supuestos)
    (SALIDA_JSON.parent / "reporte.html").write_text(html, encoding="utf-8")
    print(f"OK: {len(df)} registros -> data/procesado/, reporte/")


if __name__ == "__main__":
    main()
