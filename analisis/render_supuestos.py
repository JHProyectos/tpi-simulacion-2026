"""Genera supuestos/SUPUESTOS.md a partir de supuestos/supuestos.json.

El JSON es la fuente única: se edita ahí y se vuelve a correr este script.
Uso: python analisis/render_supuestos.py   (desde la raíz del TPI)
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "supuestos" / "supuestos.json"
SALIDA = RAIZ / "supuestos" / "SUPUESTOS.md"

ETIQUETA_ORIGEN = {
    "registro": "Registro de la organización",
    "derivado": "Derivado de registros",
    "referente": "Estimación del referente",
    "generado": "Generado (IA)",
}


def celda(texto):
    return str(texto).replace("|", "\\|").replace("\n", " ")


def main():
    d = json.loads(FUENTE.read_text(encoding="utf-8"))
    sup = d["supuestos"]
    out = [
        "# Registro de supuestos y fuentes de datos",
        "",
        f"> Generado desde `supuestos/supuestos.json` (v{d['version']}, {d['actualizado']}). "
        "No editar a mano: modificar el JSON y correr `python analisis/render_supuestos.py`.",
        "",
        "## Orígenes",
        "",
    ]
    for clave, desc in d["origenes"].items():
        n = sum(1 for s in sup if s["origen"] == clave)
        out.append(f"- **{ETIQUETA_ORIGEN[clave]}** (`{clave}`, {n}): {desc}")

    out += ["", "## Resumen", "",
            "| ID | Variable | Origen | Valor | Estado |",
            "|---|---|---|---|---|"]
    for s in sup:
        out.append(f"| {s['id']} | {celda(s['variable'])} | {ETIQUETA_ORIGEN[s['origen']]} "
                   f"| {celda(s['valor'])} | {s['estado']} |")

    out += ["", "## Detalle", ""]
    for s in sup:
        out += [f"### {s['id']} · {s['variable']}", "",
                f"- **Origen:** {ETIQUETA_ORIGEN[s['origen']]}",
                f"- **Valor:** {s['valor']}",
                f"- **Base:** {s['base']}"]
        for clave, rotulo in [("sensibilidad", "Rango de sensibilidad"),
                              ("generacion", "Cómo se genera"),
                              ("flexsim", "En FlexSim"),
                              ("nota", "Nota")]:
            if clave in s:
                out.append(f"- **{rotulo}:** {s[clave]}")
        out += [f"- **Usado en:** {', '.join(s['usado_en'])} · **Estado:** {s['estado']}", ""]

    out += ["## Decisiones abiertas", ""]
    for dec in d["decisiones_abiertas"]:
        out += [f"### {dec['id']} · {dec['tema']} ({dec['estado']})", ""]
        if "detalle" in dec:
            out += [dec["detalle"], ""]
        out += [f"- {o}" for o in dec["opciones"]]
        out += ["", f"**Recomendación:** {dec['recomendacion']}", ""]

    SALIDA.write_text("\n".join(out), encoding="utf-8")
    print(f"OK: {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
