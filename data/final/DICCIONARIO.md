# Diccionario de datos: `reservas_completo.csv`

Dataset completo de reservas: las **34.509 filas reales** sin modificar, más las filas generadas con IA para los estados que el export real no trae. Se genera con `python analisis/generar_datos.py` (semilla fija, parámetros en `supuestos/supuestos.json`).

Hay dos niveles de origen:
- **Por fila:** la columna `origen_fila` dice si la reserva existe en el registro real (`real`) o fue generada (`generado_ia`).
- **Por columna:** la tabla de abajo dice de dónde sale cada valor. En las filas reales, todas las columnas son reales o derivadas.

Se sacaron las columnas `menu_gen` y `para_llevar_gen`: el menú solo se distingue por sin TACC, que ya está en `sin_tacc` (S13), y el retiro para llevar queda fuera del alcance (D02). El retiro de varias raciones por persona (S21) no se genera en el dataset: es un parámetro del modelo.

| Columna | Filas reales | Filas generadas | Descripción |
|---|---|---|---|
| `reserva_id` | Derivado | Generado | `R-` + `customer_id` en las reales y `G-` + correlativo en las generadas |
| `origen_fila` | — | — | `real` o `generado_ia` |
| `event_date` | **Real** | Generado (S11, S12) | Día de servicio. Las generadas usan los mismos días que las reales |
| `grupo` | Derivado | Generado | Familia de cliente (`analisis/organizar_por_tipo.py`) |
| `customer_types` | **Real** | Generado | En las generadas se muestrea de las reservas reales del mismo día y grupo |
| `sin_tacc` | Derivado | Derivado | `True` si el tipo es una variante sin TACC |
| `status` | **Real** (`used`) | Generado (`no_show`, `canceled`) | Estado final de la reserva |
| `reserved_at` | **Real** | Generado | En las generadas: hora de una reserva real del mismo día y grupo ± 60 s |
| `canceled_at` | **Real** | Generado (S12) | En las reales solo aparece cuando la persona canceló y volvió a reservar (`re_reserva`). En las `canceled`: uniforme entre la reserva y las 11:00 |
| `checked_at` | **Real** | Vacío | Hora de validación en el puesto de control. Las no retiradas no la tienen |
| `re_reserva` | Derivado | `False` | `True` en las 313 reservas reales con `canceled_at` anterior a la reserva |
| `customer_id` | **Real** | Vacío | Id del registro original (único por fila, no identifica personas) |

## Controles que hace el script
- Las filas reales del archivo final coinciden con el CSV original (misma cantidad y mismos `checked_at`).
- El CSV original no cambia: se compara su hash SHA-256 antes y después (queda guardado en `resumen.json`).

## Archivos relacionados
- `data/generado/reservas_generadas.csv`: solo las filas generadas.
- `data/final/resumen.json`: conteos y tasas obtenidas, que usa el reporte.
