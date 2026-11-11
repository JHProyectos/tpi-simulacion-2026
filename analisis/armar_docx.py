"""Genera entregas/entrega-final/TPI_Simulacion_Entrega_Final.docx desde INFORME_fuente.md.

Convierte el subconjunto de Markdown que usa el informe: títulos, párrafos con
**negrita**, *cursiva* y `código`, listas, tablas, citas, fórmulas ($...$ y
$$...$$), imágenes (@@IMG) y gráficos (```grafico). Las citas que empiezan con
**Pendiente:** son notas internas y no pasan al docx.

Uso: python analisis/armar_docx.py
"""
import io
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "entregas/entrega-final/INFORME_fuente.md"
SALIDA = RAIZ / "entregas/entrega-final/TPI_Simulacion_Entrega_Final.docx"
CARATULA = RAIZ / "3d/video/artlist/00_vista-lineas_ia_tinta_cartel.png"
ANCHO = Cm(16)
ACENTO = RGBColor(0x1F, 0x4E, 0x79)

# LaTeX simple a texto, para las fórmulas en línea.
LATEX = [(r"\chi", "χ"), (r"\alpha", "α"), (r"\bar{x}", "x̄"), (r"\pm", "±"), (r"\cdot", "·"),
         (r"\approx", "≈"), (r"\;", " "), (r"\,", " "), ("{,}", ","), (r"\sum", "Σ"), (r"\sqrt", "√")]


def latex_a_texto(s):
    for a, b in LATEX:
        s = s.replace(a, b)
    s = re.sub(r"_\{([^}]*)\}", lambda m: "".join(SUB.get(c, c) for c in m.group(1)), s)
    s = re.sub(r"_(\w)", lambda m: SUB.get(m.group(1), m.group(1)), s)
    s = re.sub(r"\^\{?(\d)\}?", lambda m: SUP[m.group(1)], s)
    return s.replace("{", "").replace("}", "")


SUB = dict(zip("0123456789i", "₀₁₂₃₄₅₆₇₈₉ᵢ"))
SUP = dict(zip("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))


def fuente_base(doc):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.15
    for n, tam in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 12)):
        h = doc.styles[n]
        h.font.name = "Calibri"
        h.font.size = Pt(tam)
        h.font.color.rgb = ACENTO
        h.element.rPr.rFonts.set(qn("w:asciiTheme"), "")
        h.paragraph_format.space_before = Pt(14 if n == "Heading 1" else 10)


def agregar_texto(p, texto, tam=None, todo_negrita=False):
    """Agrega runs con **negrita**, *cursiva*, `código` y $fórmula$."""
    patron = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*[^*]+?\*|`[^`]+`|\$[^$]+\$)")
    for parte in patron.split(texto):
        if not parte:
            continue
        b = i = code = False
        if parte.startswith("***"):
            parte, b, i = parte[3:-3], True, True
        elif parte.startswith("**"):
            parte, b = parte[2:-2], True
        elif parte.startswith("*") and len(parte) > 1:
            parte, i = parte[1:-1], True
        elif parte.startswith("`"):
            parte, code = parte[1:-1], True
        elif parte.startswith("$"):
            parte, i = latex_a_texto(parte[1:-1]), True
        # negrita/cursiva anidadas dentro de un tramo
        for sub in re.split(r"(\*[^*]+?\*)", parte) if b else [parte]:
            if not sub:
                continue
            r = p.add_run(sub[1:-1] if (b and sub.startswith("*")) else sub)
            r.bold = b or todo_negrita
            r.italic = i or (b and sub.startswith("*"))
            if code:
                r.font.name = "Consolas"
                r.font.size = Pt(9.5)
            if tam:
                r.font.size = tam


def sombrear(celda_o_parr, color):
    pr = celda_o_parr._tc.get_or_add_tcPr() if hasattr(celda_o_parr, "_tc") else celda_o_parr._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    pr.append(shd)


def tabla(doc, filas):
    filas = [[c.strip() for c in f.strip().strip("|").split("|")] for f in filas]
    enc, datos = filas[0], [f for f in filas[2:]]
    t = doc.add_table(rows=1 + len(datos), cols=len(enc))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    tam = Pt(9) if len(enc) > 4 else Pt(10)
    for j, txt in enumerate(enc):
        c = t.rows[0].cells[j]
        c.paragraphs[0].paragraph_format.space_after = Pt(0)
        agregar_texto(c.paragraphs[0], txt.replace("**", ""), tam, todo_negrita=True)
        sombrear(c, "D9E2F3")
    for i, f in enumerate(datos, 1):
        for j in range(len(enc)):
            c = t.rows[i].cells[j]
            c.paragraphs[0].paragraph_format.space_after = Pt(0)
            agregar_texto(c.paragraphs[0], f[j] if j < len(f) else "", tam)
    # repetir encabezado si la tabla cruza de página
    trpr = t.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement("w:tblHeader")
    h.set(qn("w:val"), "true")
    trpr.append(h)
    doc.add_paragraph()


def imagen(doc, ruta, box, alt, ancho=ANCHO):
    im = ImageOps.exif_transpose(Image.open(RAIZ / ruta)).convert("RGB")
    if box:
        im = im.crop(box)
    im.thumbnail((1600, 1600))
    buf = io.BytesIO()
    im.save(buf, "JPEG" if ruta.startswith("3d/") else "PNG", quality=85)
    buf.seek(0)
    # capturas chicas: no estirarlas más que su tamaño natural (~96 dpi)
    natural = Cm(im.width / 96 * 2.54)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    ancho_final = min(ancho, natural)
    alto_max = Cm(12)
    if ancho_final * im.height / im.width > alto_max:
        ancho_final = int(alto_max * im.width / im.height)
    p.add_run().add_picture(buf, width=ancho_final)
    pie = doc.add_paragraph()
    pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = pie.add_run(alt)
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def grafico(doc, lineas):
    conf, datos, en_datos = {}, [], False
    for l in lineas:
        if not l.strip():
            en_datos = True
            continue
        if en_datos:
            datos.append([c.strip() for c in l.split(",")])
        else:
            k, v = l.split(":", 1)
            conf[k.strip()] = v.strip()
    enc, filas = datos[0], datos[1:]
    cats = [f[0] for f in filas]
    fig, ax = plt.subplots(figsize=(7.5, 3.6), dpi=200)
    colores = ["#1F4E79", "#E07B39", "#7F7F7F"]
    for k, serie in enumerate(enc[1:], 1):
        vals = [float(f[k]) for f in filas]
        if conf.get("tipo") == "lineas":
            ax.plot(cats, vals, marker="o", ms=3, label=serie, color=colores[k - 1])
        else:
            cols = [{"E0": "#595959", "E5": "#1F4E79"}.get(c, "#9DB3CC") for c in cats]
            bars = ax.bar(cats, vals, color=cols)
            ax.bar_label(bars, fmt="%.1f", fontsize=8)
    if conf.get("tipo") == "lineas":
        ax.legend(frameon=False, fontsize=8)
        plt.setp(ax.get_xticklabels(), rotation=45, fontsize=7)
    ax.set_ylabel(conf.get("unidad", ""))
    ax.set_title(conf.get("titulo", ""), fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(buf, width=Cm(15))


def formula(doc, tex):
    fig = plt.figure(figsize=(0.01, 0.01), dpi=250)
    fig.text(0, 0, f"${tex.replace('{,}', ',').replace(chr(92) + ';', chr(92) + ' ')}$", fontsize=13)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    buf.seek(0)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    pic = run.add_picture(buf)
    pic.width, pic.height = int(pic.width * 0.8), int(pic.height * 0.8)


def campo_indice(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    for tipo, txt in (("begin", None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ("separate", None),
                      (None, None), ("end", None)):
        if tipo:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), tipo)
            r._r.append(e)
        elif txt:
            e = OxmlElement("w:instrText")
            e.set(qn("xml:space"), "preserve")
            e.text = txt
            r._r.append(e)
        else:
            t = OxmlElement("w:t")
            t.text = "Clic derecho > Actualizar campo para generar el índice."
            r._r.append(t)


def caratula(doc, lineas):
    """lineas: los párrafos de datos que van antes del primer ---."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for txt, tam, neg in (("Simulación", 14, False), ("Trabajo Práctico Integrador · Entrega final", 13, False)):
        r = p.add_run(txt + "\n")
        r.font.size, r.bold = Pt(tam), neg
        r.font.color.rgb = RGBColor(0x40, 0x40, 0x40)
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_before = Pt(12)
    r = t.add_run("La fila de un comedor universitario")
    r.font.size, r.bold = Pt(26), True
    r.font.color.rgb = ACENTO
    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run("Puestos de validación y personas en el servicio en el horario pico")
    r.font.size, r.italic = Pt(13), True
    im = doc.add_paragraph()
    im.alignment = WD_ALIGN_PARAGRAPH.CENTER
    im.paragraph_format.space_before = Pt(18)
    buf = io.BytesIO()
    foto = Image.open(CARATULA).convert("RGB")
    foto.thumbnail((2000, 2000))
    foto.save(buf, "JPEG", quality=85)
    buf.seek(0)
    im.add_run().add_picture(buf, width=Cm(16))
    datos = doc.add_paragraph()
    datos.alignment = WD_ALIGN_PARAGRAPH.CENTER
    datos.paragraph_format.space_before = Pt(24)
    for l in lineas:
        agregar_texto(datos, l)
        datos.add_run().add_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Ingeniería en Sistemas de Información · 4.º nivel · 2026")
    r.font.size = Pt(10)
    p.add_run().add_break(WD_BREAK.PAGE)


def main():
    lineas = FUENTE.read_text(encoding="utf-8").splitlines()
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = Cm(2.2)
    sec.left_margin = sec.right_margin = Cm(2.5)
    fuente_base(doc)

    # Carátula: los datos en negrita del encabezado del .md (líneas **X:** ...)
    corte = lineas.index("---")
    datos = [l for l in lineas[:corte] if l.startswith("**") and "Cátedra" not in l]
    caratula(doc, datos)
    h = doc.add_paragraph()
    r = h.add_run("Índice")
    r.bold, r.font.size, r.font.color.rgb = True, Pt(16), ACENTO
    campo_indice(doc)
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    # nota introductoria (la cita de antes del primer ---)
    intro = [l[2:] for l in lineas[:corte] if l.startswith("> ")]

    i = corte + 1
    pend_cita = intro
    if pend_cita:
        p = doc.add_paragraph()
        agregar_texto(p, " ".join(pend_cita))
        p.runs and None
        for r in p.runs:
            r.italic = True
    while i < len(lineas):
        l = lineas[i]
        if not l.strip() or l.strip() == "---" or l.strip() == "[TOC]":
            i += 1
            continue
        if l.startswith("# "):
            i += 1
            continue
        m = re.match(r"(#{2,4}) (.*)", l)
        if m:
            nivel = len(m.group(1)) - 1
            if nivel == 1 and not m.group(2).startswith("1."):
                doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE) if m.group(2).startswith("Anexo") else None
            doc.add_heading(m.group(2), level=nivel)
            i += 1
            continue
        if l.startswith("@@IMG "):
            ruta, box, alt = [p.strip() for p in l[6:].split("|", 2)]
            imagen(doc, ruta, tuple(int(v) for v in box.split(",")) if box else None, alt)
            i += 1
            continue
        if l.startswith("```"):
            tipo = l[3:].strip()
            j = i + 1
            while not lineas[j].startswith("```"):
                j += 1
            if tipo == "grafico":
                grafico(doc, lineas[i + 1:j])
            i = j + 1
            continue
        if l.startswith("$$"):
            j = i
            tex = l.strip("$")
            while not lineas[j].rstrip().endswith("$$") or (j == i and l.strip() == "$$"):
                j += 1
                tex += " " + lineas[j].strip("$")
            formula(doc, tex.strip())
            i = j + 1
            continue
        if l.startswith("|"):
            j = i
            while j < len(lineas) and lineas[j].startswith("|"):
                j += 1
            tabla(doc, lineas[i:j])
            i = j
            continue
        if l.startswith(">"):
            bloque = []
            while i < len(lineas) and lineas[i].startswith(">"):
                bloque.append(lineas[i][1:].strip())
                i += 1
            texto = " ".join(b for b in bloque if b)
            if texto.startswith("**Pendiente:**"):
                continue
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            sombrear(p, "EEF3F8")
            agregar_texto(p, texto)
            continue
        m = re.match(r"(\s*)(- |\d+\. )(.*)", l)
        if m:
            if m.group(2) == "- ":
                p = doc.add_paragraph(style="List Bullet 2" if len(m.group(1)) >= 2 else "List Bullet")
            else:
                # numeración escrita a mano: los estilos numerados de Word siguen contando entre listas
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.9)
                p.paragraph_format.first_line_indent = Cm(-0.6)
                p.add_run(m.group(2).strip() + "  ")
            p.paragraph_format.space_after = Pt(2)
            agregar_texto(p, m.group(3))
            i += 1
            continue
        # párrafo: une líneas seguidas
        texto = [l]
        i += 1
        while i < len(lineas) and lineas[i].strip() and not re.match(r"(#|@@|```|\||>|\s*- |\d+\. |\$\$|---)", lineas[i]):
            texto.append(lineas[i])
            i += 1
        agregar_texto(doc.add_paragraph(), " ".join(texto))

    # número de página al pie
    pie = sec.footer.paragraphs[0]
    pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = pie.add_run()
    for tipo, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipo:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), tipo)
        else:
            e = OxmlElement("w:instrText")
            e.text = txt
        r._r.append(e)
    sec.different_first_page_header_footer = True
    # que Word actualice el índice al abrir
    upd = OxmlElement("w:updateFields")
    upd.set(qn("w:val"), "true")
    doc.settings.element.append(upd)
    doc.save(SALIDA)
    print("Listo:", SALIDA.relative_to(RAIZ))


if __name__ == "__main__":
    main()
