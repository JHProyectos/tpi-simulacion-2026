# FlexSim

El modelo (`.fsm`) y sus tablas de entrada van en esta carpeta. Ver las fases 4 y 5 en [`PLAN.md`](../PLAN.md).

**Cómo armar el modelo:** [`GUIA_FLEXSIM.md`](GUIA_FLEXSIM.md), paso a paso por etapas, con el código de cada actividad y los valores de referencia para verificar. Los valores salen de `python analisis/referencia_modelo.py`, una réplica mínima del modelo en Python.

## `inputs.xlsx`

Lo genera `python analisis/generar_inputs_flexsim.py`; no se edita a mano. Cada hoja es una Global Table: importarlas con **Toolbox > Connectivity > Excel Import/Export**, con la fila 1 como encabezados de columna. La hoja `LEEME` explica cada tabla y no se importa.

Tiempo de modelo: `t = 0` a las 11:40, apertura en `t = 1200 s` (12:00) más la demora de apertura, cierre en `t = 10200 s` (14:30).
