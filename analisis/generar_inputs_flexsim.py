"""Fase 4: genera flexsim/inputs.xlsx con las Global Tables del modelo.

Alcance (D02 revisada): llegada → fila de caja → caja (un DNI por ración) →
fila de servicio → mostrador → salida. El salón queda fuera.

Convención de tiempo del modelo: t = 0 a las 11:40 (empiezan a llegar quienes
hacen fila antes de abrir), apertura de la caja en t = 1200 s (12:00) más la
demora de apertura (S25) y cierre en t = 10200 s (14:30). Todas las columnas
*_s están en segundos de modelo.

Las llegadas se cuentan en personas: los registros reales cuentan validaciones
(una por ración), así que se dividen por las raciones promedio por persona del
grupo (S21).

Cada hoja es una tabla con encabezados en la fila 1 y solo valores (sin
fórmulas), lista para Excel Import/Export. La hoja LEEME explica el origen de
cada tabla según supuestos/supuestos.json.

Uso: python analisis/generar_inputs_flexsim.py   (desde la raíz del TPI)
"""
import json
import math
import sys
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from organizar_por_tipo import GRUPOS, ORDEN_GRUPOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "data" / "real" / "TP-SIM - ds_app.csv"
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
COL_GRUPO = {"Estudiantes": "Estudiantes", "Becas Nutrirse": "BecasNutrirse",
             "Becas personal": "BecasPersonal", "Personal": "Personal"}
SIN_LIMITE = 999           # capacidad de la fila de servicio mientras S23 esté pendiente


def cargar():
    df = pd.read_csv(CSV, na_values=["NULL"])
    df["checked_at"] = pd.to_datetime(df["checked_at"], format="ISO8601", utc=True).dt.tz_convert(TZ)
    df["grupo"] = df["customer_types"].map(GRUPOS)
    df["seg_dia"] = (df["checked_at"] - df["checked_at"].dt.normalize()).dt.total_seconds()
    minutos = df["checked_at"].dt.hour * 60 + df["checked_at"].dt.minute - 720
    # Los pocos check-ins antes de las 12:00 van a la primera franja; los posteriores al cierre se descartan.
    df["franja"] = (minutos // 10).clip(lower=0)
    return df[df["franja"] < N_FRANJAS]


def validaciones_por_franja(df, perfil, excluir):
    sub = df[df["event_date"].map(PERFILES[perfil]) & ~df["event_date"].isin(excluir)]
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
    excluir = {S["S26"]["parametros"]["fecha"]}

    # Tipos dentro de cada grupo (S04), con sin TACC (S13) y raciones por persona (S21).
    p21 = S["S21"]["parametros"]
    conteo = df.groupby(["grupo", "customer_types"]).size()
    mix, media_grupo = [], {}
    for g in ORDEN_GRUPOS:
        sub = conteo[g].sort_values(ascending=False)
        # Las proporciones reales son de raciones; se pasan a personas dividiendo por las raciones de cada tipo.
        filas = []
        for tipo, n in sub.items():
            dist = p21["raciones_vianda"] if tipo in p21["tipos_vianda"] else p21["raciones_resto"]
            media = sum(int(k) * v for k, v in dist.items())
            filas.append((tipo, n, dist, media))
        personas = sum(n / m for _, n, _, m in filas)
        media_grupo[g] = sum(n for _, n, _, _ in filas) / personas
        for tipo, n, dist, media in filas:
            vianda = tipo in p21["tipos_vianda"]
            mix.append({"Grupo": COL_GRUPO[g], "Tipo": tipo, "SinTACC": int("sin TACC" in tipo),
                        "PropEnGrupo": round(n / media / personas, 5), "EsVianda": int(vianda),
                        "FilaE4": "Viandas" if vianda else "General",
                        "P1Racion": dist.get("1", 0), "P2Raciones": dist.get("2", 0), "P3Raciones": dist.get("3", 0),
                        "RacionesMedia": round(media, 3)})

    hojas = {}
    ref_rows, cola_rows, resumen = [], [], {}
    for perfil in PERFILES:
        media, por_dia, dias = validaciones_por_franja(df, perfil, excluir)
        # Validaciones (raciones) → personas, dividiendo por las raciones promedio del grupo (S08, S21).
        personas = media.copy()
        for g in ORDEN_GRUPOS:
            personas[g] = media[g] / media_grupo[g]
        # La primera franja atiende también a la fila formada antes de abrir (S09):
        # esas personas se descuentan de las llegadas de la franja y se reparten por grupo.
        primera = personas.iloc[0]
        reparto = (primera / primera.sum() * cola_previa[perfil]).round().astype(int)
        reparto.iloc[0] += cola_previa[perfil] - reparto.sum()
        personas.iloc[0] = (primera - reparto).clip(lower=0)
        filas = []
        for i in range(N_FRANJAS):
            fila = {"Franja": hhmm(i), "Inicio_s": T_APERTURA + 600 * i, "Fin_s": T_APERTURA + 600 * (i + 1)}
            for g in ORDEN_GRUPOS:
                fila[COL_GRUPO[g]] = round(float(personas.iloc[i][g]), 2)
            fila["Total"] = round(sum(fila[COL_GRUPO[g]] for g in ORDEN_GRUPOS), 2)
            filas.append(fila)
        hojas[f"TasaLlegadas_{perfil}"] = pd.DataFrame(filas)
        total_personas = sum(f["Total"] for f in filas) + cola_previa[perfil]
        resumen[perfil] = (round(total_personas), round(float(media.values.sum())))
        for g in ORDEN_GRUPOS:
            cola_rows.append({"Perfil": perfil, "Grupo": COL_GRUPO[g], "Personas": int(reparto[g]),
                              "LlegadaDesde_s": 0, "LlegadaHasta_s": T_APERTURA})
        for i in range(N_FRANJAS):
            ref_rows.append({"Perfil": perfil, "Franja": hhmm(i), "Inicio_s": T_APERTURA + 600 * i,
                             "RacionesMedia": round(float(media.iloc[i].sum()), 2),
                             "RacionesMin": int(por_dia[i].min()), "RacionesMax": int(por_dia[i].max()),
                             "DiasPerfil": int(dias)})
    hojas["ColaPrevia"] = pd.DataFrame(cola_rows)

    # S25: demora del primer check-in de cada día respecto de las 12:00 (negativos = 0).
    inicio = df.groupby("event_date")["seg_dia"].min() - 12 * 3600
    hojas["DemoraApertura"] = pd.DataFrame({"Fecha": inicio.index,
                                            "Demora_s": inicio.clip(lower=0).round(1).to_numpy()})
    hojas["MixTipos"] = pd.DataFrame(mix)

    def lognormal(proceso, mediana, sigma, supuesto):
        return {"Proceso": proceso, "Distribucion": "lognormal2", "Location": 0, "Scale": mediana, "Shape": sigma,
                "Mediana_s": mediana, "Media_s": round(mediana * math.exp(sigma ** 2 / 2), 2),
                "ExprFlexSim": f"lognormal2(0, {mediana}, {sigma}, getstream(activity))", "Por": "ración",
                "Supuesto": supuesto}

    vl = val["lognormal"]
    p15 = S["S15"]["parametros"]
    hojas["TiemposServicio"] = pd.DataFrame([
        lognormal("Validacion", round(math.exp(vl["mu"]), 2), vl["sigma"], "S07 (derivado)"),
        lognormal("ServicioRacion", p15["mediana_s"], p15["sigma"], "S15 (generado)"),
    ])

    factor_qr = S["S24"]["parametros"]["factor"]
    serv = S["S22"]["parametros"]
    base, extra = serv["servidores_base"], serv["servidores_extra"]
    prob_veg = S["S27"]["parametros"]["prob_veg"]
    # Toda la gente hace la misma fila de caja. Servidores = personas sirviendo, una de las cuales atiende
    # la comida vegetariana (S22). ProbVegetariano es la proporción de personas con menú vegetariano (S27).
    escenarios = [
        ("E0", f"Base: 1 puesto, {base} personas sirviendo", 1, 0, 0, 0, 1.0, base),
        ("E1", f"2 puestos, {base} personas sirviendo", 2, 0, 0, 0, 1.0, base),
        ("E2", f"2 puestos de 12:00 a 13:30, {base} personas sirviendo", 1, 1, T_APERTURA, T_APERTURA + 5400, 1.0, base),
        ("E3", f"1 puesto con validación por QR, {base} personas sirviendo", 1, 0, 0, 0, factor_qr, base),
        ("E4", f"1 puesto, {extra} personas sirviendo", 1, 0, 0, 0, 1.0, extra),
        ("E5", f"2 puestos, {extra} personas sirviendo", 2, 0, 0, 0, 1.0, extra),
    ]
    filas = []
    for perfil in PERFILES:
        for cod, desc, pb, pe, desde, hasta, factor, servidores in escenarios:
            filas.append({"Escenario": f"{cod}_{perfil}", "Descripcion": desc, "Perfil": perfil,
                          "PuestosBase": pb, "PuestosExtra": pe, "ExtraDesde_s": desde, "ExtraHasta_s": hasta,
                          "FactorValidacion": factor, "ProbVegetariano": prob_veg, "Servidores": servidores,
                          "CapacidadFilaServicio": SIN_LIMITE, "ColaPrevia": cola_previa[perfil],
                          "PersonasDia": resumen[perfil][0], "RacionesDia": resumen[perfil][1]})
    hojas["Escenarios"] = pd.DataFrame(filas)
    hojas["Referencia_Validaciones"] = pd.DataFrame(ref_rows)

    escribir(hojas, sup, media_grupo)
    print(f"OK: {SALIDA.relative_to(RAIZ)}")
    for perfil in PERFILES:
        print(f"  {perfil}: {resumen[perfil][0]} personas por día ({resumen[perfil][1]} raciones), "
              f"cola previa {cola_previa[perfil]}")
    print("  Raciones por persona: " + ", ".join(f"{COL_GRUPO[g]} {m:.3f}" for g, m in media_grupo.items()))


def escribir(hojas, sup, media_grupo):
    wb = Workbook()
    leeme = wb.active
    leeme.title = "LEEME"
    lineas = [
        ("Tablas de entrada para FlexSim: TPI Simulación, Comedor Universitario UNC", "titulo"),
        (f"Generado por analisis/generar_inputs_flexsim.py a partir de supuestos/supuestos.json v{sup['version']}. No editar a mano: cambiar el JSON y regenerar.", ""),
        ("", ""),
        ("Alcance y tiempo de modelo", "sub"),
        ("Llegada → fila de caja → caja → fila de servicio → mostrador → salida (D02). t = 0 s a las 11:40 (llega la fila previa), apertura de la caja en t = 1200 s (12:00) más la demora de apertura, cierre en t = 10200 s (14:30). Unidades del modelo: segundos.", ""),
        ("", ""),
        ("Cómo importar", "sub"),
        ("Toolbox > Connectivity > Excel Import/Export. Una Global Table por hoja, con el mismo nombre. Use Column Headers tildado, Use Row Headers destildado, Starting Row y Starting Column en 1, Total Rows = filas de datos + 1. La hoja LEEME no se importa.", ""),
        ("", ""),
        ("Hojas", "sub"),
        ("TasaLlegadas_Pico / _Bajo: PERSONAS que llegan a la fila por franja de 10 min y por grupo (media por día). Derivado de los registros (S08): validaciones reales, sin el 18/8 (S26), divididas por las raciones promedio por persona del grupo (S21). En la franja 12:00 ya se descontó la cola previa. "
         + "Raciones por persona: " + ", ".join(f"{COL_GRUPO[g]} {m:.3f}" for g, m in media_grupo.items()) + ".", ""),
        ("ColaPrevia: personas que llegan entre 11:40 y 12:00, por grupo y perfil (S09, generado). Llegada uniforme en [LlegadaDesde_s, LlegadaHasta_s].", ""),
        ("MixTipos: proporción de personas de cada tipo dentro de su grupo (derivado de S04, corregido por raciones), sin TACC (S13, real), si es vianda (informativo: todos hacen la misma fila) y la distribución de raciones por persona: P1Racion, P2Raciones, P3Raciones (S21, generado).", ""),
        ("TiemposServicio: parámetros lognormal2(location, scale, shape) con scale = mediana, POR RACIÓN. Validación por DNI derivada de los registros (S07); servicio en el mostrador generado (S15). Quien retira varias raciones suma una muestra por ración.", ""),
        ("DemoraApertura: demora real del primer check-in de cada uno de los 32 días, en segundos (S25, derivado). La caja se habilita en 1200 s + un valor elegido al azar de esta tabla.", ""),
        ("Escenarios: E0 a E5 para cada perfil. PuestosBase y PuestosExtra son puestos de la caja, con una fila única; el extra se habilita entre ExtraDesde_s y ExtraHasta_s (E2). FactorValidacion multiplica el tiempo de validación (E3, S24). ProbVegetariano = proporción de personas con menú vegetariano (S27). Servidores = personas sirviendo, una de ellas a cargo de la comida vegetariana (S22). "
         f"CapacidadFilaServicio = {SIN_LIMITE} (sin límite) hasta que el referente estime S23.", ""),
        ("Referencia_Validaciones: raciones validadas por franja en los registros reales (media, mínimo y máximo por día, sin el 18/8). Es la curva contra la que se valida el modelo en la fase 6.", ""),
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
