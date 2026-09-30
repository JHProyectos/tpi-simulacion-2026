"""Fase 4: genera flexsim/inputs.xlsx con las Global Tables del modelo.

Convención de tiempo del modelo: t = 0 a las 11:40 (empiezan a llegar quienes
hacen fila antes de abrir), apertura del puesto en t = 1200 s (12:00) y cierre
en t = 10200 s (14:30). Todas las columnas *_s están en segundos de modelo.

Cada hoja es una tabla con encabezados en la fila 1 y solo valores (sin
fórmulas), lista para Excel Import/Export. La hoja LEEME explica el origen de
cada tabla según supuestos/supuestos.json.

Uso: python analisis/generar_inputs_flexsim.py   (desde la raíz del TPI)
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from organizar_por_tipo import GRUPOS, ORDEN_GRUPOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data" / "real" / "TP-SIM - ds_app.csv"
COMPLETO = RAIZ / "data" / "final" / "reservas_completo.csv"
SUPUESTOS = RAIZ / "supuestos" / "supuestos.json"
VALIDACION = RAIZ / "data" / "procesado" / "tiempo_validacion.json"
SALIDA = RAIZ / "flexsim" / "inputs.xlsx"
TZ = "America/Argentina/Cordoba"

T_APERTURA = 1200          # 12:00 en tiempo de modelo
T_CIERRE = 1200 + 9000     # 14:30
N_FRANJAS = 16             # 12:00 a 14:30 inclusive, de a 10 minutos
PERFILES = {               # S03
    "Pico": lambda f: f >= "2026-08-10",
    "Bajo": lambda f: f < "2026-08-01",
}
EXCLUIR = {"2026-08-18"}   # S23: interrupción de 14 min en el puesto; se usa en el escenario E5
COL_GRUPO = {"Estudiantes": "Estudiantes", "Becas Nutrirse": "BecasNutrirse",
             "Becas personal": "BecasPersonal", "Personal": "Personal"}


def cargar():
    df = pd.read_csv(CSV, na_values=["NULL"])
    df["checked_at"] = pd.to_datetime(df["checked_at"], format="ISO8601", utc=True).dt.tz_convert(TZ)
    df["grupo"] = df["customer_types"].map(GRUPOS)
    df["seg_dia"] = (df["checked_at"] - df["checked_at"].dt.normalize()).dt.total_seconds()
    minutos = df["checked_at"].dt.hour * 60 + df["checked_at"].dt.minute - 720
    # Los pocos check-ins antes de las 12:00 van a la primera franja; los posteriores al cierre se descartan.
    df["franja"] = (minutos // 10).clip(lower=0)
    return df[df["franja"] < N_FRANJAS]


def validaciones_por_franja(df, perfil):
    sub = df[df["event_date"].map(PERFILES[perfil]) & ~df["event_date"].isin(EXCLUIR)]
    dias = sub["event_date"].nunique()
    tabla = (sub.groupby(["franja", "grupo"]).size().unstack(fill_value=0)
               .reindex(index=range(N_FRANJAS), columns=ORDEN_GRUPOS, fill_value=0))
    por_dia = sub.groupby(["event_date", "franja"]).size().unstack(fill_value=0).reindex(columns=range(N_FRANJAS), fill_value=0)
    return tabla / dias, por_dia, dias


def hhmm(franja):
    m = 720 + 10 * franja
    return f"{m // 60:02d}:{m % 60:02d}"


def main():
    sup = json.loads(SUPUESTOS.read_text(encoding="utf-8"))
    S = {x["id"]: x for x in sup["supuestos"]}
    val = json.loads(VALIDACION.read_text(encoding="utf-8"))
    df = cargar()
    cola = S["S09"]["parametros"]
    cola_previa = {"Pico": cola["cola_pico"], "Bajo": cola["cola_bajo"]}

    hojas = {}
    ref_rows = []
    cola_rows = []
    for perfil in PERFILES:
        media, por_dia, dias = validaciones_por_franja(df, perfil)
        # La primera franja valida también a la fila formada antes de abrir (S09):
        # esas personas se descuentan de las llegadas de la franja y se reparten por grupo.
        primera = media.iloc[0]
        reparto = (primera / primera.sum() * cola_previa[perfil]).round().astype(int)
        reparto.iloc[0] += cola_previa[perfil] - reparto.sum()
        llegadas = media.copy()
        llegadas.iloc[0] = (primera - reparto).clip(lower=0)
        filas = []
        for i in range(N_FRANJAS):
            fila = {"Franja": hhmm(i), "Inicio_s": T_APERTURA + 600 * i, "Fin_s": T_APERTURA + 600 * (i + 1)}
            for g in ORDEN_GRUPOS:
                fila[COL_GRUPO[g]] = round(float(llegadas.iloc[i][g]), 2)
            fila["Total"] = round(sum(fila[COL_GRUPO[g]] for g in ORDEN_GRUPOS), 2)
            filas.append(fila)
        hojas[f"TasaLlegadas_{perfil}"] = pd.DataFrame(filas)
        for g in ORDEN_GRUPOS:
            cola_rows.append({"Perfil": perfil, "Grupo": COL_GRUPO[g], "Personas": int(reparto[g]),
                              "LlegadaDesde_s": 0, "LlegadaHasta_s": T_APERTURA})
        for i in range(N_FRANJAS):
            ref_rows.append({"Perfil": perfil, "Franja": hhmm(i), "Inicio_s": T_APERTURA + 600 * i,
                             "ValidacionesMedia": round(float(media.iloc[i].sum()), 2),
                             "ValidacionesMin": int(por_dia[i].min()), "ValidacionesMax": int(por_dia[i].max()),
                             "DiasPerfil": int(dias)})
    hojas["ColaPrevia"] = pd.DataFrame(cola_rows)

    # S22: demora del primer check-in de cada día respecto de las 12:00 (negativos = 0).
    inicio = df.groupby("event_date")["seg_dia"].min() - 12 * 3600
    hojas["DemoraApertura"] = pd.DataFrame({"Fecha": inicio.index,
                                            "Demora_s": inicio.clip(lower=0).round(1).to_numpy()})

    # Mezcla de tipos dentro de cada grupo (S04), con menú (S13) y retiro para llevar (S14).
    p13, p14 = S["S13"]["parametros"], S["S14"]["parametros"]
    conteo = df.groupby(["grupo", "customer_types"]).size()
    mix = []
    for g in ORDEN_GRUPOS:
        sub = conteo[g].sort_values(ascending=False)
        for tipo, n in sub.items():
            mix.append({"Grupo": COL_GRUPO[g], "Tipo": tipo, "SinTACC": int("sin TACC" in tipo),
                        "PropEnGrupo": round(n / sub.sum(), 5),
                        "PLlevar": p14["p_llevar_vianda"] if tipo in p14["tipos_vianda"] else p14["p_llevar_resto"],
                        "PVegetariano": p13["p_vegetariano"]})
    hojas["MixTipos"] = pd.DataFrame(mix)

    def lognormal(proceso, mediana, sigma, supuesto, unidad="s"):
        return {"Proceso": proceso, "Distribucion": "lognormal2", "Location": 0, "Scale": mediana, "Shape": sigma,
                "Mediana_s": mediana, "Media_s": round(mediana * math.exp(sigma ** 2 / 2), 2),
                "ExprFlexSim": f"lognormal2(0, {mediana}, {sigma}, getstream(activity))", "Supuesto": supuesto}

    vl = val["lognormal"]
    mediana_val = round(math.exp(vl["mu"]), 2)
    p15, p17 = S["S15"]["parametros"], S["S17"]["parametros"]
    hojas["TiemposServicio"] = pd.DataFrame([
        lognormal("Validacion", mediana_val, vl["sigma"], "S07 (derivado)"),
        lognormal("MostradorVegetariano", p15["mediana_s"], p15["sigma"], "S15 (generado)"),
        lognormal("MostradorNoVegetariano", p15["mediana_s"], p15["sigma"], "S15 (generado)"),
        lognormal("ConsumoSalon", p17["mediana_min"] * 60, p17["sigma"], "S17 (generado)"),
    ])

    asientos = S["S16"]["parametros"]["asientos"]
    factor_qr = S["S21"]["parametros"]["factor"]
    falla = S["S23"]["parametros"]
    h, m = map(int, falla["desde"].split(":"))
    falla_desde = T_APERTURA + (h * 60 + m - 720) * 60
    falla_hasta = falla_desde + falla["duracion_min"] * 60
    escenarios = [
        ("E0", "Base: 1 puesto", 1, 0, 0, 0, 1.0, 0, 0, "actual"),
        ("E1", "2 puestos todo el turno", 2, 0, 0, 0, 1.0, 0, 0, "actual"),
        ("E2", "2 puestos de 12:00 a 13:30", 1, 1, T_APERTURA, T_APERTURA + 5400, 1.0, 0, 0, "actual"),
        ("E3", "Autoatención por QR", 1, 0, 0, 0, factor_qr, 0, 0, "actual"),
        ("E4", "Reordenamiento del layout", 1, 0, 0, 0, 1.0, 0, 0, "alternativo"),
        ("E5", "Interrupción del puesto (caso real 18/8)", 1, 0, 0, 0, 1.0, falla_desde, falla_hasta, "actual"),
    ]
    filas = []
    for perfil in PERFILES:
        total = float(hojas[f"TasaLlegadas_{perfil}"]["Total"].sum()) + cola_previa[perfil]
        for cod, desc, base, extra, desde, hasta, factor, int_desde, int_hasta, layout in escenarios:
            filas.append({"Escenario": f"{cod}_{perfil}", "Descripcion": desc, "Perfil": perfil,
                          "PuestosBase": base, "PuestosExtra": extra, "ExtraDesde_s": desde, "ExtraHasta_s": hasta,
                          "FactorValidacion": factor, "InterrupcionDesde_s": int_desde,
                          "InterrupcionHasta_s": int_hasta, "ColaPrevia": cola_previa[perfil],
                          "LlegadasDia": round(total), "Asientos": asientos, "Layout": layout})
    hojas["Escenarios"] = pd.DataFrame(filas)

    hojas["Salon"] = pd.DataFrame([
        {"Parametro": "Asientos", "Valor": asientos, "Unidad": "asientos", "Supuesto": "S16 (medición propia)"},
        {"Parametro": "VelocidadCaminata", "Valor": S["S19"]["parametros"]["velocidad_m_s"], "Unidad": "m/s", "Supuesto": "S19 (generado)"},
        {"Parametro": "ReglaAsiento", "Valor": "libre_mas_cercano_al_mostrador", "Unidad": "", "Supuesto": "S18 (generado)"},
        {"Parametro": "SinAsientoLibre", "Valor": "espera_de_pie", "Unidad": "", "Supuesto": "S18 (generado)"},
        {"Parametro": "InicioModelo", "Valor": "11:40", "Unidad": "hora", "Supuesto": "S09"},
        {"Parametro": "Apertura_s", "Valor": T_APERTURA, "Unidad": "s", "Supuesto": "S01"},
        {"Parametro": "Cierre_s", "Valor": T_CIERRE, "Unidad": "s", "Supuesto": "S01"},
    ])
    hojas["Referencia_Validaciones"] = pd.DataFrame(ref_rows)

    chequeo = chequeo_asientos(p17)
    escribir(hojas, sup, chequeo)
    print(f"OK: {SALIDA.relative_to(RAIZ)}")
    for perfil in PERFILES:
        t = hojas[f"TasaLlegadas_{perfil}"]
        print(f"  {perfil}: llegadas en franjas {t['Total'].sum():.0f} + cola previa {cola_previa[perfil]}")
    print(f"  Chequeo salón (pico): ocupación máxima estimada {chequeo['mediana']} asientos "
          f"(rango {chequeo['min']}–{chequeo['max']}) de {asientos}")


def chequeo_asientos(p17):
    """Estimación previa al modelo: personas sentadas a la vez en días pico, con los
    check-ins reales, el retiro para llevar generado y el consumo medio (S17)."""
    d = pd.read_csv(COMPLETO)
    d = d[(d["status"] == "used") & (d["para_llevar_gen"] == False) & d["event_date"].map(PERFILES["Pico"])]  # noqa: E712
    t = pd.to_datetime(d["checked_at"], format="ISO8601", utc=True)
    segundos = (t - t.dt.normalize()).dt.total_seconds()
    consumo = p17["mediana_min"] * 60 * math.exp(p17["sigma"] ** 2 / 2) + 60  # + 1 min de mostrador y caminata
    maximos = []
    for _, g in segundos.groupby(d["event_date"]):
        entradas = np.sort(g.to_numpy())
        # Sentados en el instante de cada entrada: quienes entraron en los últimos `consumo` segundos.
        ocupados = np.searchsorted(entradas, entradas, side="right") - np.searchsorted(entradas, entradas - consumo, side="right")
        maximos.append(int(ocupados.max()))
    s = pd.Series(maximos)
    return {"mediana": int(s.median()), "min": int(s.min()), "max": int(s.max())}


def escribir(hojas, sup, chequeo):
    wb = Workbook()
    leeme = wb.active
    leeme.title = "LEEME"
    lineas = [
        ("Tablas de entrada para FlexSim: TPI Simulación, Comedor Universitario UNC", "titulo"),
        (f"Generado por analisis/generar_inputs_flexsim.py a partir de supuestos/supuestos.json v{sup['version']}. No editar a mano: cambiar el JSON y regenerar.", ""),
        ("", ""),
        ("Tiempo de modelo", "sub"),
        ("t = 0 s a las 11:40 (llega la fila previa), apertura del puesto en t = 1200 s (12:00), cierre en t = 10200 s (14:30). Unidades del modelo: segundos.", ""),
        ("", ""),
        ("Cómo importar", "sub"),
        ("Toolbox > Connectivity > Excel Import/Export. Una Global Table por hoja, con el mismo nombre, tomando la fila 1 como encabezados de columna. La hoja LEEME no se importa.", ""),
        ("", ""),
        ("Hojas", "sub"),
        ("TasaLlegadas_Pico / _Bajo: llegadas esperadas a la fila por franja de 10 min y por grupo (media por día). Derivado de los registros (S08), sin el 18/8 (S23). En la franja 12:00 ya se descontó la cola previa. Uso sugerido: tiempo entre llegadas exponential(0, 600 / valor, getstream(activity)); si el valor es 0, no generar llegadas en esa franja.", ""),
        ("ColaPrevia: personas que llegan entre 11:40 y 12:00, por grupo y perfil (S09, generado). Llegada uniforme en [LlegadaDesde_s, LlegadaHasta_s].", ""),
        ("MixTipos: proporción de cada tipo dentro de su grupo (derivado, S04), probabilidad de retiro para llevar (S14, generado) y de menú vegetariano (S13, generado).", ""),
        ("TiemposServicio: parámetros lognormal2(location, scale, shape) con scale = mediana. Validación derivada de los registros (S07); mostrador (S15) y consumo (S17) generados. Verificar en la ayuda de FlexSim que scale = e^mu.", ""),
        ("DemoraApertura: demora real del primer check-in de cada uno de los 32 días, en segundos (S22, derivado). El puesto se habilita en Apertura_s + un valor elegido al azar de esta tabla.", ""),
        ("Escenarios: E0 a E5 para cada perfil. PuestosExtra se habilita entre ExtraDesde_s y ExtraHasta_s. FactorValidacion multiplica el tiempo de validación (E3, S21). En E5 el puesto se detiene entre InterrupcionDesde_s e InterrupcionHasta_s (caso real del 18/8, S23).", ""),
        ("Salon: asientos (S16, medición propia), velocidad de caminata (S19) y regla de asiento (S18).", ""),
        ("Referencia_Validaciones: validaciones reales por franja (media, mínimo y máximo por día, sin el 18/8). Es la curva contra la que se valida el modelo en la fase 6.", ""),
        ("", ""),
        ("Chequeo previo del salón", "sub"),
        (f"Con los check-ins reales de los días pico, el retiro para llevar generado y el consumo medio de S17, la ocupación máxima estimada es de {chequeo['mediana']} asientos por día (rango {chequeo['min']} a {chequeo['max']}) sobre 432. Es una cota aproximada: no incluye caminata ni la espera en el mostrador.", ""),
    ]
    for i, (texto, estilo) in enumerate(lineas, start=1):
        c = leeme.cell(row=i, column=1, value=texto)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if estilo == "titulo":
            c.font = Font(bold=True, size=14)
        elif estilo == "sub":
            c.font = Font(bold=True, size=11, color="1F5F8B")
    leeme.column_dimensions["A"].width = 130

    encabezado = PatternFill("solid", fgColor="E1EDF6")
    for nombre, tabla in hojas.items():
        ws = wb.create_sheet(nombre)
        ws.append(list(tabla.columns))
        for fila in tabla.itertuples(index=False):
            ws.append([v.item() if hasattr(v, "item") else v for v in fila])
        for j, col in enumerate(tabla.columns, start=1):
            ws.cell(row=1, column=j).font = Font(bold=True)
            ws.cell(row=1, column=j).fill = encabezado
            ancho = max(len(str(col)), *(len(str(v)) for v in tabla[col])) + 2
            ws.column_dimensions[get_column_letter(j)].width = min(ancho, 45)
        ws.freeze_panes = "A2"
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)


if __name__ == "__main__":
    main()
