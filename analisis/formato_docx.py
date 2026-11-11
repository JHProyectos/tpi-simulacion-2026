"""Ajustes de formato sobre el docx ya editado a mano (no lo regenera desde el .md).

- encabezado: logo de la UTN a la izquierda y número de página a la derecha;
  pie con «TPI · Simulación» y los integrantes.
- --apa: además, guarda una copia con formato APA 7 (estudiante).

Uso:
    python analisis/formato_docx.py          # solo encabezado y pie, en el mismo archivo
    python analisis/formato_docx.py --apa    # además genera ..._APA.docx
"""
import copy
import sys
from pathlib import Path

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ = Path(__file__).resolve().parent.parent
DOCX = RAIZ / "entregas/entrega-final/TPI_Simulacion_Entrega_Final.docx"
APA = RAIZ / "entregas/entrega-final/TPI_Simulacion_Entrega_Final_APA.docx"
LOGO = RAIZ / "imagenes/logo-utn.png"
PIE = "TPI · Simulación · Jonatan Harbertz y Juan Chavez"
NEGRO = RGBColor(0, 0, 0)
CUERPO = [None]


def campo(run, instr):
    for tipo in ("begin", None, "end"):
        if tipo:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), tipo)
        else:
            e = OxmlElement("w:instrText")
            e.set(qn("xml:space"), "preserve")
            e.text = instr
        run._r.append(e)


def limpiar(parte):
    for p in parte.paragraphs[1:]:
        p._p.getparent().remove(p._p)
    p = parte.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    return p


def encabezado(doc, fuente=None):
    sec = doc.sections[0]
    ancho = sec.page_width - sec.left_margin - sec.right_margin
    h = limpiar(sec.header)
    h.paragraph_format.tab_stops.add_tab_stop(ancho, WD_TAB_ALIGNMENT.RIGHT)
    h.add_run().add_picture(str(LOGO), height=Cm(1.1))
    h.add_run("\t")
    r = h.add_run()
    campo(r, "PAGE")
    f = limpiar(sec.footer)
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = f.add_run(PIE)
    r.font.size = Pt(9)
    for run in h.runs + f.runs:
        if fuente:
            run.font.name = fuente
    # la carátula queda sin encabezado ni pie
    sec.different_first_page_header_footer = True


# ---------------------------------------------------------------- APA

def tiene_imagen(p):
    return bool(p._p.xpath(".//w:drawing"))


def es_pie(p):
    return bool(p.runs) and all(r.italic for r in p.runs if r.text.strip()) and p.alignment == WD_ALIGN_PARAGRAPH.CENTER \
        and p.runs[0].font.size == Pt(9)


def insertar_antes(elem, texto="", negrita=False, cursiva=False):
    p = OxmlElement("w:p")
    elem.addprevious(p)
    par = Paragraph(p, CUERPO[0])
    if texto:
        r = par.add_run(texto)
        r.bold, r.italic = negrita, cursiva
    return par


def formato_etiqueta(par, cursiva=False):
    pf = par.paragraph_format
    pf.first_line_indent = Cm(0)
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(0)
    pf.keep_with_next = True
    par.alignment = WD_ALIGN_PARAGRAPH.LEFT


def apa(doc):
    fuente = "Times New Roman"
    CUERPO[0] = doc._body
    for s in doc.sections:
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.54)
    st = doc.styles["Normal"]
    st.font.name = fuente
    st.font.size = Pt(12)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), fuente)
    st.element.rPr.rFonts.set(qn("w:hAnsi"), fuente)
    pf = st.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)

    # renglones del índice en simple y sin espacio extra (a nivel estilo, porque Word
    # rearma el índice al actualizarlo); así el cierre del campo no desborda a otra hoja
    for nombre in ("toc 1", "toc 2"):
        try:
            ts = doc.styles[nombre]
        except KeyError:
            continue
        ts.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        ts.paragraph_format.space_after = Pt(0)
        ts.paragraph_format.space_before = Pt(0)

    # Títulos APA: nivel 1 centrado en negrita; nivel 2 a la izquierda en negrita;
    # nivel 3 a la izquierda en negrita y cursiva. Todos en negro y a 12 pt.
    for nombre, centro, cur in (("Heading 1", True, False), ("Heading 2", False, False), ("Heading 3", False, True)):
        h = doc.styles[nombre]
        h.font.name, h.font.size, h.font.bold, h.font.italic = fuente, Pt(12), True, cur
        h.font.color.rgb = NEGRO
        rpr = h.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is not None:
            for a in list(fonts.attrib):
                fonts.attrib.pop(a)
            for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
                fonts.set(qn(a), fuente)
        h.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if centro else WD_ALIGN_PARAGRAPH.LEFT
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(0)
        h.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE

    body = doc.element.body
    cuerpo = list(body.iterchildren())
    # dónde termina la carátula (antes del «Índice»)
    pars = doc.paragraphs
    i_indice = next(k for k, p in enumerate(pars) if p.text.strip() == "Índice")

    # --- carátula APA de estudiante
    titulo = next(p for p in pars[:i_indice] if "La fila de un comedor" in p.text)
    for p in pars[:i_indice]:
        for r in p.runs:
            r.font.name = fuente
            r.font.color.rgb = NEGRO
        p.paragraph_format.first_line_indent = Cm(0)
    for r in titulo.runs:
        r.font.size = Pt(16)
    datos = next(p for p in pars[:i_indice] if "Integrantes" in p.text)
    for r in list(datos.runs):
        r._r.getparent().remove(r._r)
    for linea in ("Jonatan Harbertz y Juan Chavez",
                  "Universidad Tecnológica Nacional, Facultad Regional Venado Tuerto",
                  "Ingeniería en Sistemas de Información",
                  "Simulación: Trabajo Práctico Integrador, entrega final",
                  "11 de noviembre de 2026"):
        r = datos.add_run(linea)
        r.font.name = fuente
        datos.add_run().add_break()
    for p in pars[:i_indice]:
        if p.text.startswith("Ingeniería en Sistemas de Información ·") or p.text.startswith("Simulación\n"):
            for r in list(p.runs):
                if "Ingeniería" in r.text or r.text.startswith("Simulación") or "Entrega final" in r.text:
                    r._r.getparent().remove(r._r)

    # --- párrafos del cuerpo: sangría de primera línea 1,27 cm, a la izquierda
    i_cuerpo = next(k for k, p in enumerate(pars) if p.style.name == "Heading 1")
    # los párrafos vacíos de la carátula y el índice (y los que llevan el salto de
    # página) con interlineado doble desbordan la página y dejan hojas en blanco
    # el salto de página después del índice pasa a «salto antes» del párrafo siguiente
    i_ind = next(k for k, p in enumerate(pars) if p.text.strip() == "Índice")
    for k in range(i_ind + 1, i_cuerpo):
        p = pars[k]
        if not p.style.name.startswith("toc") and not p.text.strip() and p._p.xpath('.//w:br[@w:type="page"]'):
            pars[k + 1].paragraph_format.page_break_before = True
            p._p.getparent().remove(p._p)
            break
    pars = doc.paragraphs
    i_cuerpo = next(k for k, p in enumerate(pars) if p.style.name == "Heading 1")
    for p in pars[:i_cuerpo]:
        if not p.text.strip() and not tiene_imagen(p):
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(0)
            ant = p._p.getprevious()
            if p._p.xpath('.//w:fldChar[@w:fldCharType="end"]') and ant is not None and ant.tag == qn("w:p"):
                # el cierre del campo del índice pasa al último renglón del índice
                for r in p._p.xpath("./w:r"):
                    ant.append(r)
                p._p.getparent().remove(p._p)
                continue
            if False:
                # cierre del campo del índice: que no ocupe lugar
                p.paragraph_format.line_spacing = Pt(1)
                p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        elif p.style.name.startswith("toc") or p.text.strip() != "Índice":
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE if p.style.name.startswith("toc") else p.paragraph_format.line_spacing_rule
    for p in pars[i_cuerpo:]:
        for r in p.runs:
            if r.font.name not in ("Consolas",):
                r.font.name = fuente
            if r.font.size and r.font.size < Pt(12) and not r.italic and r.font.name != "Consolas":
                r.font.size = Pt(12)
        if p.style.name == "Normal" and p.text.strip() and not tiene_imagen(p) and not es_pie(p):
            pf = p.paragraph_format
            if pf.first_line_indent is None or pf.first_line_indent >= 0:
                if pf.left_indent in (None, 0):
                    pf.first_line_indent = Cm(1.27)
            if p.alignment != WD_ALIGN_PARAGRAPH.CENTER:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if p.style.name.startswith("List"):
            p.paragraph_format.space_after = Pt(0)

    # --- figuras: «Figura n» en negrita y el título en cursiva, arriba de la imagen
    ultimo_titulo = ""
    nfig = 0
    pars = doc.paragraphs
    for k, p in enumerate(pars):
        if k < i_cuerpo:
            continue
        if p.style.name.startswith("Heading"):
            ultimo_titulo = p.text.split(" ", 1)[-1] if p.text[:1].isdigit() else p.text
            continue
        if not tiene_imagen(p):
            continue
        sig = pars[k + 1] if k + 1 < len(pars) else None
        ancho = max((int(e.get("cx")) for e in p._p.xpath(".//wp:extent")), default=0)
        es_formula = ancho < Cm(11) and not (sig is not None and es_pie(sig))
        if es_formula:
            continue
        nfig += 1
        if sig is not None and es_pie(sig):
            titulo_fig = sig.text.strip()
            sig._p.getparent().remove(sig._p)
        else:
            titulo_fig = ultimo_titulo
        e = insertar_antes(p._p, f"Figura {nfig}", negrita=True)
        formato_etiqueta(e)
        t = insertar_antes(p._p, titulo_fig, cursiva=True)
        formato_etiqueta(t)
        for x in (e, t):
            for r in x.runs:
                r.font.name = fuente
        p.paragraph_format.first_line_indent = Cm(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # --- tablas: «Tabla n» y título en cursiva arriba; interlineado simple adentro
    ntab = 0
    ultimo_titulo = ""
    for el in list(body.iterchildren()):
        if el.tag == qn("w:p"):
            par = Paragraph(el, doc._body)
            if par.style.name.startswith("Heading"):
                ultimo_titulo = par.text.split(" ", 1)[-1] if par.text[:1].isdigit() else par.text
            continue
        if el.tag != qn("w:tbl"):
            continue
        ntab += 1
        tabla = Table(el, doc._body)
        tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
        e = insertar_antes(el, f"Tabla {ntab}", negrita=True)
        formato_etiqueta(e)
        t = insertar_antes(el, ultimo_titulo, cursiva=True)
        formato_etiqueta(t)
        for x in (e, t):
            for r in x.runs:
                r.font.name = fuente
        for fila in tabla.rows:
            for c in fila.cells:
                for cp in c.paragraphs:
                    cp.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
                    cp.paragraph_format.first_line_indent = Cm(0)
                    for r in cp.runs:
                        r.font.name = fuente
                        r.font.size = Pt(10)

    # --- referencias, antes de los anexos
    anexo = next((p for p in doc.paragraphs if p.style.name.startswith("Heading") and p.text.startswith("Anexo")), None)
    ancla = anexo._p if anexo is not None else None
    refs = [
        "Anthropic. (2026). Claude (versión Opus) [Modelo de lenguaje de gran tamaño]. https://claude.ai",
        "Autodesk. (2026). FlexSim 2026 (versión 26.0, licencia Education) [Software]. https://www.flexsim.com",
        "Artlist. (2026). Artlist AI [Herramienta de generación de imágenes]. https://artlist.io",
    ]
    if ancla is not None:
        h = insertar_antes(ancla, "Referencias")
        h.style = doc.styles["Heading 1"]
        for ref in refs:
            p = insertar_antes(ancla, ref)
            p.paragraph_format.left_indent = Cm(1.27)
            p.paragraph_format.first_line_indent = Cm(-1.27)
            for r in p.runs:
                r.font.name = fuente
        # cada anexo empieza en página nueva
        anexo.paragraph_format.page_break_before = True
    return doc


def main():
    doc = docx.Document(DOCX)
    encabezado(doc)
    doc.save(DOCX)
    print("Encabezado y pie:", DOCX.name)
    if "--apa" in sys.argv:
        doc = docx.Document(DOCX)
        apa(doc)
        encabezado(doc, "Times New Roman")
        doc.save(APA)
        print("APA:", APA.name)


if __name__ == "__main__":
    main()
