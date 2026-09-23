# Plan de trabajo: TPI Simulación, Comedor Universitario UNC

**Pregunta de estudio (propuesta, D05):** ¿cuántos puestos de validación deben operar en simultáneo para que la espera en la fila no supere un valor aceptable en el pico, y alcanza la capacidad del salón para absorber el flujo resultante?

**Flujo en el alcance (D02):** fila, que se forma antes de la apertura → puesto de validación → mostrador (línea vegetariana o no vegetariana) → asiento en el salón, o salida si es para llevar.

Responsables: **[Grupo]** Jonatan y Juan · **[Referente]** integrante que trabaja en el comedor · **[Claude]** apoyo con IA (declarado en la sección 12).

Los supuestos y las fuentes de datos se registran en [`supuestos/SUPUESTOS.md`](supuestos/SUPUESTOS.md). La fuente única es `supuestos/supuestos.json`.

---

## Fase 0 · Organización del proyecto
- [x] [Claude] Estructura de carpetas: `data/real`, `data/procesado`, `data/generado`, `analisis`, `supuestos`, `flexsim`, `reporte`, `entregas`, `imagenes`, `3d`, `obsoletos`
- [x] [Claude] Dataset original movido a `data/real/` sin modificar
- [x] [Claude] Scripts actualizados a las rutas nuevas
- [x] [Claude] `README.md` y `PLAN.md`
- [x] [Grupo] Revisar y mergear la rama `fases-0-2-organizacion-y-supuestos` (mergeada en `main`)

## Fase 1 · Relevamiento con el referente
- [x] [Referente] ¿Dónde se registra `checked_at`? → En el puesto de control (validación)
- [x] [Referente] ¿Las viandas usan la misma fila? → Sí, todo pasa por la misma fila
- [x] [Referente] ¿Cuántos puestos operan? → Habitualmente 1 (de 2 disponibles)
- [x] [Grupo] ¿Se puede cronometrar? → No; los tiempos se derivan de los datos o se generan
- [x] [Claude] Estimar el tiempo de validación con los datos reales → media de 3,9 s, capacidad de ~924 por hora (`analisis/tiempo_validacion.py`)
- [ ] [Referente] Estimación de ausentismo (reservas no retiradas), para reemplazar S11
- [ ] [Referente] Estimación del porcentaje de menú vegetariano (S13) y de retiro para llevar (S14)
- [ ] [Referente] Estimación del tiempo de consumo en el salón (S17)
- [x] [Referente] ¿La cocina limita la demanda? → No, la capacidad de preparación supera ampliamente la demanda (S20)
- [ ] [Grupo] Si la foto de `imagenes/` es de la web de la UNC y no la tomó el grupo, corregir la fuente en la sección 7

## Fase 2 · Registro de supuestos
- [x] [Claude] `supuestos/supuestos.json` con valor, base, origen y rango de sensibilidad de cada variable
- [x] [Claude] `analisis/render_supuestos.py`, que genera `SUPUESTOS.md`
- [x] [Claude] Sección «Qué es real y qué es supuesto» en el reporte
- [ ] [Grupo] Revisar y aprobar los supuestos propuestos (S08, S11–S15, S17–S19)
- [x] [Grupo] **D01** → la fila se forma antes de que empiece la atención (S09)
- [x] [Grupo] **D02** → mostrador y salón entran en el alcance; se agregan S16–S19
- [x] [Grupo] **D03** → se simulan los dos perfiles, bajo y pico (por defecto)
- [x] [Grupo] **D04** → el horario límite sirve para planificar la cocina y no afecta la cola: sale de los escenarios; las reservas definen la demanda
- [ ] [Grupo] **D05**: reformular la pregunta de estudio y el alcance (secciones 3 y 4)
- [ ] [Grupo] Contar los asientos del layout 3D y cargar el valor en S16

## Fase 3 · Dataset ampliado (real + generado)
- [x] [Claude] `analisis/generar_datos.py` (semilla 2026, parámetros leídos de `supuestos.json`) genera `data/generado/` y `data/final/reservas_completo.csv`
  - [x] 34.509 filas reales intactas, con `origen_fila = real` (verificado con hash del CSV original)
  - [x] 2.987 filas `no_show` (S11) y 1.183 filas `canceled` (S12), con `origen_fila = generado_ia`
  - [x] Atributos `menu_gen` (S13) y `para_llevar_gen` (S14) en cada reserva
- [x] [Claude] Diccionario de datos (`data/final/DICCIONARIO.md`) con el origen de cada columna
- [x] [Claude] Reporte con la sección «Qué es real y qué es supuesto» y el resumen del dataset completo
- [ ] [Grupo] Revisar que los datos generados sean coherentes con los reales
- [ ] [Claude] Regenerar si cambian los valores de S11–S14 (un comando)

## Fase 4 · Tablas para FlexSim
- [ ] [Claude] `flexsim/inputs.xlsx`
  - [ ] `TasaLlegadas`: franja de 10 min × grupo, por perfil de demanda
  - [ ] `MixTipos`: proporciones por tipo, menú y para llevar
  - [ ] `TiemposServicio`: validación (S07), mostrador (S15) y consumo en el salón (S17)
  - [ ] `Escenarios`: puestos, demanda (reservas − ausentes) y cola previa a la apertura
  - [ ] `Salon`: asientos y distancias, cuando esté S16
- [ ] [Grupo] Importar con Excel Import/Export a Global Tables

## Fase 5 · Modelo base en FlexSim (Process Flow)
- [ ] [Grupo] Configurar el modelo en segundos, con t = 0 a las 11:40 y apertura a las 12:00
- [ ] [Grupo] Inter-Arrival Source por grupo con tasa por franja (S08) y llegadas previas a la apertura (S09)
- [ ] [Grupo] Asignar labels: grupo, tipo, sin TACC, menú, para llevar
- [ ] [Grupo] Cola y Resource `PuestosValidacion` (1 unidad) con tiempo lognormal (S07)
- [ ] [Grupo] Mostrador con 2 líneas según la label menu (S15)
- [ ] [Grupo] Para llevar → salida; resto → asiento libre más cercano (S18), consumo (S17) y salida
- [ ] [Grupo] Espera de pie si no hay asiento libre (indicador de capacidad del salón)
- [ ] [Grupo] Layout 3D: cola en serpentina con Path y mesas desde los `.skp` de `3d/` (si no importa, exportar a `.obj`)
- [ ] [Grupo] Registrar las salidas: espera en la cola, cola máxima, utilización del puesto y del mostrador, validaciones por franja, ocupación del salón, tiempo sin asiento, permanencia total, raciones no retiradas
- [ ] [Claude] Apoyo con la lógica de Process Flow y con el código de los triggers

## Fase 6 · Calibración y validación
- [ ] [Claude] Script que compare lo que exporta FlexSim contra los datos reales: curva de validaciones por franja y total del día
- [ ] [Grupo] Calibrar S08 y S09 hasta reproducir la curva real
- [ ] [Grupo] Chequear la cola máxima contra 60 a 70 personas (S10) y aplicar la ley de Little
- [ ] [Grupo] Documentar la validación en el informe

## Fase 7 · Escenarios y experimentación
- [ ] [Grupo] Configurar el Experimenter con 20 a 30 réplicas por escenario
  - [ ] E0: base, 1 puesto
  - [ ] E1: 2 puestos durante todo el turno
  - [ ] E2: 2 puestos solo de 12:00 a 13:30
  - [ ] E3: autoatención por QR (menos tiempo de validación o un puesto extra)
  - [ ] E4: reordenamiento del layout de mesas (escenario 4 de la Entrega 1)
  - [ ] Cada escenario en perfil bajo y perfil pico
- [ ] [Claude] Procesar resultados: intervalos de confianza, comparación entre escenarios y gráficos
- [ ] [Grupo] Análisis de sensibilidad de los supuestos generados (rangos en `SUPUESTOS.md`)

## Fase 8 · Informe y entregas
- [ ] [Claude] Borrador de las secciones 7 y 8 de la entrega a partir de `SUPUESTOS.md`
- [ ] [Grupo] Actualizar las secciones 3 y 4 (pregunta y alcance) según D02, D04 y D05
- [ ] [Grupo] Actualizar la sección 6: el horario límite sale de los escenarios (D04) y entra el layout del salón
- [ ] [Grupo] Actualizar la **sección 12 (declaración de IA)**: ahora incluye procesamiento del dataset, generación de datos sintéticos y análisis de resultados
- [ ] [Grupo] Corregir en la sección 8 el tiempo de validación (12–18 s → ~3,9 s derivado de los datos)
- [ ] [Grupo] Conclusiones y recomendación de configuración
- [ ] [Grupo] Revisión final y entrega
