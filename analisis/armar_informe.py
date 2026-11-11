"""Arma entregas/entrega-final/INFORME.md a partir de INFORME_fuente.md.

En la fuente, cada imagen va en una línea sola con este formato:

    @@IMG ruta/desde/la/raiz.png | izq,arriba,der,abajo | Texto alternativo

El recorte es opcional (dejarlo vacío usa la imagen entera). El script recorta,
achica y embebe la imagen como data URI, para que el .md se vea completo en el
Lector MD sin depender de la carpeta.

Uso: python analisis/armar_informe.py
"""
import base64
import io
from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "entregas/entrega-final/INFORME_fuente.md"
SALIDA = RAIZ / "entregas/entrega-final/INFORME.md"


def img_md(ruta, alt, box=None, max_side=1400):
    im = ImageOps.exif_transpose(Image.open(RAIZ / ruta))
    if box:
        im = im.crop(box)
    im.thumbnail((max_side, max_side))
    # Los renders de 3d/ son fotos: van en JPEG aunque el original sea PNG.
    es_png = ruta.lower().endswith(".png") and not ruta.startswith("3d/")
    if not es_png:
        max_side = min(max_side, 1200)
    fmt = "PNG" if es_png else "JPEG"
    if fmt == "JPEG" and im.mode != "RGB":
        im = im.convert("RGB")
    buf = io.BytesIO()
    if fmt == "PNG":
        # Capturas de pantalla: 256 colores alcanzan y pesan mucho menos.
        im = im.convert("RGB").quantize(256)
        im.save(buf, fmt, optimize=True)
    else:
        im.save(buf, fmt, quality=80, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"![{alt.replace(']', ')')}](data:image/{fmt.lower()};base64,{b64})", len(buf.getvalue())


def main():
    salida, total = [], 0
    for linea in FUENTE.read_text(encoding="utf-8").splitlines():
        if linea.startswith("@@IMG "):
            ruta, box, alt = [p.strip() for p in linea[6:].split("|", 2)]
            box = tuple(int(v) for v in box.split(",")) if box else None
            md, peso = img_md(ruta, alt, box)
            total += peso
            print(f"{peso / 1024:6.0f} KB  {ruta}")
            salida.append(md)
        else:
            salida.append(linea)
    SALIDA.write_text("\n".join(salida) + "\n", encoding="utf-8", newline="\n")
    print(f"Listo: {SALIDA.relative_to(RAIZ)} ({total / 1024:.0f} KB de imágenes)")


if __name__ == "__main__":
    main()
