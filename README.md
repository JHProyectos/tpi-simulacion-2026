# TPI Simulación 2026: Comedor Universitario UNC

Estudio de simulación de la fila de validación del Comedor Universitario UNC (reserva previa online y atención presencial), modelado en FlexSim con Process Flow.

- Plan y avance: [`PLAN.md`](PLAN.md)
- Supuestos y fuentes de datos: [`supuestos/SUPUESTOS.md`](supuestos/SUPUESTOS.md)

## Estructura

| Carpeta | Contenido |
|---|---|
| `data/real/` | Registros de la organización, **sin modificar** |
| `data/procesado/` | Datos derivados de los reales con scripts (organizados por tipo, intervalos, etc.) |
| `data/generado/` | Datos sintéticos generados con IA; cada uno tiene su supuesto en `supuestos/` |
| `analisis/` | Scripts de Python que producen `data/procesado/`, `reporte/` y `supuestos/SUPUESTOS.md` |
| `supuestos/` | Registro de supuestos: `supuestos.json` es la fuente y `SUPUESTOS.md` se genera a partir de él |
| `flexsim/` | Modelo de FlexSim y tablas de entrada |
| `reporte/` | Reporte del dataset y del origen de cada dato del modelo (HTML) |
| `entregas/` | Consignas y documentos entregados a la cátedra |
| `imagenes/`, `3d/` | Fotos del comedor y modelos de SketchUp |
| `obsoletos/` | Versiones anteriores, solo como referencia |

## Regenerar lo derivado

Requiere Python 3 con `pandas` (`python -m pip install pandas`). Desde la raíz:

```bash
python analisis/tiempo_validacion.py
python analisis/render_supuestos.py
python analisis/organizar_por_tipo.py
```
