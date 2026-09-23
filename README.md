# TPI Simulación 2026: Comedor Universitario UNC

Estudio de simulación de la fila de validación del Comedor Universitario UNC (reserva previa online y atención presencial), modelado en FlexSim con Process Flow. El sistema va desde la llegada a la fila, pasando por la caja (puesto de validación) y la fila del servicio de comida, hasta retirar la bandeja en el mostrador. El salón queda fuera del estudio.

- Plan y avance: [`PLAN.md`](PLAN.md)
- Supuestos y fuentes de datos: [`supuestos/SUPUESTOS.md`](supuestos/SUPUESTOS.md)
- Página con los datos, el alcance y los supuestos: [`web/index.html`](web/index.html)

## Estructura

| Carpeta | Contenido |
|---|---|
| `data/real/` | Registros de la organización, **sin modificar** |
| `data/procesado/` | Datos derivados de los reales con scripts (organizados por tipo, intervalos, etc.) |
| `data/generado/` | Datos sintéticos generados con IA; cada uno tiene su supuesto en `supuestos/` |
| `data/final/` | Dataset completo (real + generado) con el origen de cada fila y columna: ver `DICCIONARIO.md` |
| `analisis/` | Scripts de Python que producen `data/procesado/`, `reporte/datos.json`, `web/index.html` y `supuestos/SUPUESTOS.md` |
| `supuestos/` | Registro de supuestos: `supuestos.json` es la fuente y `SUPUESTOS.md` se genera a partir de él |
| `flexsim/` | Modelo de FlexSim y tablas de entrada |
| `reporte/` | Plantilla de la página (`plantilla.html`) y datos agregados (`datos.json`) |
| `web/` | Página generada (`index.html`): un HTML estático autocontenido, lo único que se publica |
| `entregas/` | Consignas y documentos entregados a la cátedra |
| `imagenes/`, `3d/` | Fotos del comedor y modelos de SketchUp |
| `obsoletos/` | Versiones anteriores, solo como referencia |

## Regenerar lo derivado

Requiere Python 3 con `pandas` (`python -m pip install pandas`). Desde la raíz:

```bash
python analisis/tiempo_validacion.py
python analisis/render_supuestos.py
python analisis/generar_datos.py
python analisis/organizar_por_tipo.py
```

## Publicar la página en Vercel

`web/index.html` no depende de nada más: tiene los datos adentro y solo carga las fuentes de Google Fonts. Para publicarla:

1. En Vercel, **Add New → Project** e importar este repositorio.
2. En **Root Directory**, elegir `web`. Así se publica solo la página y no los CSV de `data/`.
3. **Framework Preset:** Other. Sin build command ni output directory.
4. **Deploy.** Cada push a `main` vuelve a publicar la página.

Otra opción, sin conectar el repo: `npx vercel web` desde la raíz.
