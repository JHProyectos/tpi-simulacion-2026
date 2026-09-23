# Plan de trabajo: TPI Simulación, Comedor Universitario UNC

**Pregunta de estudio (propuesta, D05):** ¿qué combinación de puestos de validación, organización de la fila y personas en el servicio de comida reduce el tiempo total desde la llegada hasta retirar la bandeja en el pico, sin que mejorar la caja solo traslade la cola al mostrador?

**Alcance (D02, revisada):** llegada → fila de caja, que se forma antes de la apertura → caja (puesto de validación), donde se presenta un DNI por ración → fila de servicio → mostrador → salida. El salón y el retiro para llevar quedan fuera del estudio: se mencionan en el informe, pero no se modelan (S14, S16–S19).

**Pedido de la cátedra:** ver la dinámica en FlexSim. Si se mejora la validación, la cola puede pasar al servicio de comida; hay que probar si agregar gente en el servicio acelera el proceso completo en lugar de solo correr el cuello de botella (E1 contra E5).

**Caso de estudio (D06):** habilitar los 2 puestos con una fila para cada uno según el tipo de cliente (propuesta: viandas de Becas Nutrirse contra el resto) y compararlo contra los 2 puestos con fila única.

Responsables: **[Grupo]** Jonatan y Juan · **[Referente]** integrante que trabaja en el comedor · **[Claude]** apoyo con IA (declarado en la sección 12).

Los supuestos y las fuentes de datos se registran en [`supuestos/SUPUESTOS.md`](supuestos/SUPUESTOS.md). La fuente única es `supuestos/supuestos.json`. La página con los datos, el alcance y el cálculo del cuello de botella está en [`web/index.html`](web/index.html).

---

## Fase 0 · Organización del proyecto
- [x] [Claude] Estructura de carpetas: `data/real`, `data/procesado`, `data/generado`, `analisis`, `supuestos`, `flexsim`, `reporte`, `web`, `entregas`, `imagenes`, `3d`, `obsoletos`
- [x] [Claude] Dataset original movido a `data/real/` sin modificar
- [x] [Claude] Scripts actualizados a las rutas nuevas
- [x] [Claude] `README.md` y `PLAN.md`
- [x] [Grupo] Revisar y mergear la rama `fases-0-2-organizacion-y-supuestos` (mergeada en `main`)
- [x] [Claude] Reporte como HTML estático independiente en `web/index.html`, listo para publicar en Vercel
- [ ] [Grupo] Publicar `web/` en Vercel (ver README)

## Fase 1 · Relevamiento con el referente
- [x] [Referente] ¿Dónde se registra `checked_at`? → En el puesto de control (validación)
- [x] [Referente] ¿Las viandas usan la misma fila? → Sí, todo pasa por la misma fila
- [x] [Referente] ¿Cuántos puestos operan? → Habitualmente 1 (de 2 disponibles)
- [x] [Grupo] ¿Se puede cronometrar? → No; los tiempos se derivan de los datos o se generan
- [x] [Claude] Estimar el tiempo de validación con los datos reales → media de 3,9 s por DNI, capacidad de ~924 raciones por hora (`analisis/tiempo_validacion.py`)
- [x] [Referente] ¿La cocina limita la demanda? → No, la capacidad de preparación supera ampliamente la demanda (S20)
- [x] [Grupo] ¿Qué distingue al menú? → Solo con o sin TACC, que ya viene en el tipo de cliente (S13)
- [x] [Grupo] ¿Una persona puede retirar por otras? → Sí, presentando los DNI de quienes reservaron (S21)
- [x] [Claude] ¿Se ve el retiro múltiple en los datos? → No: casi no hay check-ins a menos de 1,5 s del anterior (0,2 %); cada DNI se valida por separado
- [ ] [Referente] Estimación de ausentismo (reservas no retiradas), para reemplazar S11
- [ ] [Referente] Retiro múltiple: ¿con qué frecuencia pasa y cuántos DNI como máximo? ¿Es más común en las viandas? (S21)
- [ ] [Referente] Servicio de comida: ¿cuántas personas sirven (S22), cuánto se tarda en servir una bandeja (S15) y las viandas salen del mismo mostrador?
- [ ] [Referente] ¿Cuántas personas entran en la fila entre la caja y el mostrador? (S23)
- [ ] [Referente] ¿Es factible separar la fila en dos según el tipo de cliente? ¿Cuál división tiene sentido en el comedor? (D06)
- [ ] [Grupo] Si la foto de `imagenes/` es de la web de la UNC y no la tomó el grupo, corregir la fuente en la sección 7

## Fase 2 · Registro de supuestos
- [x] [Claude] `supuestos/supuestos.json` con valor, base, origen y rango de sensibilidad de cada variable
- [x] [Claude] `analisis/render_supuestos.py`, que genera `SUPUESTOS.md` (con una sección aparte para lo que queda fuera del alcance)
- [x] [Claude] Sección «Qué es real y qué es supuesto» en el reporte
- [x] [Claude] Supuestos del servicio: tiempo por ración en el mostrador (S15), retiro múltiple (S21), personas sirviendo (S22) y espacio de la fila de servicio (S23)
- [ ] [Grupo] Revisar y aprobar los supuestos propuestos (S08, S11, S12, S15, S21, S22)
- [x] [Grupo] **D01** → la fila se forma antes de que empiece la atención (S09)
- [x] [Grupo] **D02** → revisada: el sistema llega hasta el mostrador; el salón queda fuera
- [x] [Grupo] **D03** → se simulan los dos perfiles, bajo y pico (por defecto)
- [x] [Grupo] **D04** → el horario límite sirve para planificar la cocina y no afecta la cola: sale de los escenarios; las reservas definen la demanda
- [ ] [Grupo] **D05**: reformular la pregunta de estudio y el alcance (secciones 3 y 4)
- [ ] [Grupo] **D06**: definir cómo se dividen las dos filas del caso de estudio

## Fase 3 · Dataset ampliado (real + generado)
- [x] [Claude] `analisis/generar_datos.py` (semilla 2026, parámetros leídos de `supuestos.json`) genera `data/generado/` y `data/final/reservas_completo.csv`
  - [x] 34.509 filas reales intactas, con `origen_fila = real` (verificado con hash del CSV original)
  - [x] 2.987 filas `no_show` (S11) y 1.183 filas `canceled` (S12), con `origen_fila = generado_ia`
  - [x] Se sacaron las columnas `menu_gen` y `para_llevar_gen` (el menú vegetariano no existe y el retiro para llevar queda fuera)
- [x] [Claude] Diccionario de datos (`data/final/DICCIONARIO.md`) con el origen de cada columna
- [x] [Claude] Reporte con la sección «Qué es real y qué es supuesto» y el resumen del dataset completo
- [ ] [Grupo] Revisar que los datos generados sean coherentes con los reales
- [ ] [Claude] Regenerar si cambian los valores de S11 o S12 (un comando)
- El retiro múltiple (S21) no se genera en el dataset: es un parámetro del modelo

## Fase 4 · Tablas para FlexSim
- [ ] [Claude] `flexsim/inputs.xlsx`
  - [ ] `TasaLlegadas`: franja de 10 min × grupo, por perfil de demanda, en personas (raciones ÷ raciones por persona, S21)
  - [ ] `MixTipos`: proporciones por tipo de cliente, con su grupo y sin TACC
  - [ ] `Raciones`: distribución de raciones por persona según el grupo (S21)
  - [ ] `TiemposServicio`: validación por DNI (S07) y servicio por ración (S15)
  - [ ] `Escenarios`: puestos, organización de la fila, personas sirviendo, demanda (reservas − ausentes) y cola previa a la apertura
- [ ] [Grupo] Importar con Excel Import/Export a Global Tables

## Fase 5 · Modelo base en FlexSim (Process Flow)
- [ ] [Grupo] Configurar el modelo en segundos, con t = 0 a las 11:40 y apertura a las 12:00
- [ ] [Grupo] Inter-Arrival Source por grupo con tasa por franja (S08) y llegadas previas a la apertura (S09)
- [ ] [Grupo] Asignar las labels en el Source, desde el origen: grupo, tipo, sin_tacc y raciones (S13, S21)
- [ ] [Grupo] FilaCaja y Resource `PuestosValidacion` (1 unidad): el tiempo es la suma de una muestra de S07 por cada ración
- [ ] [Grupo] FilaServicio con capacidad máxima (S23): si se llena, la caja se bloquea
- [ ] [Grupo] Resource `ServicioComida` (2 unidades, S22): el tiempo es la suma de una muestra de S15 por cada ración; después sale del sistema
- [ ] [Grupo] Variante E4: dos filas de caja con un puesto cada una, según la label tipo
- [ ] [Grupo] Layout 3D para mostrar la dinámica: fila de caja en serpentina con Path, caja, fila de servicio y mostrador con las personas que sirven. El salón, si se incluye, es solo decorativo
- [ ] [Grupo] Registrar las salidas: espera en cada fila (total y por tipo), cola máxima en cada fila, tiempo total en el sistema, utilización de la caja y del servicio, tiempo con la caja bloqueada, validaciones por franja, raciones reservadas no retiradas
- [ ] [Claude] Apoyo con la lógica de Process Flow y con el código de los triggers

## Fase 6 · Calibración y validación
- [ ] [Claude] Script que compare lo que exporta FlexSim contra los datos reales: curva de validaciones por franja y total del día
- [ ] [Grupo] Calibrar S08 y S09 hasta reproducir la curva real
- [ ] [Grupo] Chequear la cola máxima contra 60 a 70 personas (S10) y aplicar la ley de Little
- [ ] [Grupo] Chequear que en el escenario base no se forme cola en el servicio (S10)
- [ ] [Grupo] Documentar la validación en el informe

## Fase 7 · Escenarios y experimentación
- [ ] [Grupo] Configurar el Experimenter con 20 a 30 réplicas por escenario
  - [ ] E0: base, 1 puesto, fila única, 2 personas en el servicio
  - [ ] E1: 2 puestos durante todo el turno, fila única (¿se corre la cola al mostrador?)
  - [ ] E2: 2 puestos solo de 12:00 a 13:30
  - [ ] E3: validación por QR (menos tiempo por DNI)
  - [ ] E4: 2 puestos, una fila por tipo de cliente (caso de estudio, D06)
  - [ ] E5: 2 puestos y 3 personas en el servicio (¿se acelera el proceso completo?)
  - [ ] Cada escenario en perfil bajo y perfil pico
- [ ] [Grupo] Opcional: diseño factorial de puestos (1, 2) × personas en el servicio (2, 3) para separar el efecto de cada recurso
- [ ] [Claude] Procesar resultados: intervalos de confianza, comparación entre escenarios (E1 contra E5 en tiempo total; E4 contra E1 por tipo de cliente) y gráficos
- [ ] [Grupo] Análisis de sensibilidad de los supuestos generados, sobre todo S15, S21 y S22 (rangos en `SUPUESTOS.md`)

## Fase 8 · Informe y entregas
- [ ] [Claude] Borrador de las secciones 7 y 8 de la entrega a partir de `SUPUESTOS.md`
- [ ] [Grupo] Actualizar las secciones 3 y 4 (pregunta y alcance) según D02, D04, D05 y D06
- [ ] [Grupo] Mencionar en el alcance lo que queda fuera (salón, retiro para llevar) y por qué
- [ ] [Grupo] Actualizar la sección 6: el horario límite sale de los escenarios (D04) y se suman el caso de dos filas (E4) y el refuerzo del servicio (E5)
- [ ] [Grupo] Actualizar la **sección 12 (declaración de IA)**: ahora incluye procesamiento del dataset, generación de datos sintéticos y análisis de resultados
- [ ] [Grupo] Corregir en la sección 8 el tiempo de validación (12–18 s → ~3,9 s por DNI, derivado de los datos)
- [ ] [Grupo] Conclusiones y recomendación de configuración
- [ ] [Grupo] Revisión final y entrega
