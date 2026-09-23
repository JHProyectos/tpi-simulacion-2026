# Plan de trabajo: TPI Simulación, Comedor Universitario UNC

**Pregunta de estudio:** ¿cuántos puestos de validación deben operar a la vez, y con qué horario límite de reserva, para que la espera en la fila de validación no supere un valor aceptable en el horario pico del almuerzo?

Responsables: **[Grupo]** Jonatan y Juan · **[Referente]** integrante que trabaja en el comedor · **[Claude]** apoyo con IA (declarado en la sección 12).

Los supuestos y las fuentes de datos se registran en [`supuestos/SUPUESTOS.md`](supuestos/SUPUESTOS.md). La fuente única es `supuestos/supuestos.json`.

---

## Fase 0 · Organización del proyecto
- [x] [Claude] Estructura de carpetas: `data/real`, `data/procesado`, `data/generado`, `analisis`, `supuestos`, `flexsim`, `reporte`, `entregas`, `imagenes`, `3d`, `obsoletos`
- [x] [Claude] Dataset original movido a `data/real/` sin modificar
- [x] [Claude] Scripts actualizados a las rutas nuevas
- [x] [Claude] `README.md` y `PLAN.md`
- [ ] [Grupo] Revisar y mergear la rama `fases-0-2-organizacion-y-supuestos`

## Fase 1 · Relevamiento con el referente
- [x] [Referente] ¿Dónde se registra `checked_at`? → En el puesto de control (validación)
- [x] [Referente] ¿Las viandas usan la misma fila? → Sí, todo pasa por la misma fila
- [x] [Referente] ¿Cuántos puestos operan? → Habitualmente 1 (de 2 disponibles)
- [x] [Grupo] ¿Se puede cronometrar? → No; los tiempos se derivan de los datos o se generan
- [x] [Claude] Estimar el tiempo de validación con los datos reales → media de 3,9 s, capacidad de ~924 por hora (`analisis/tiempo_validacion.py`)
- [ ] [Referente] Estimación de ausentismo (reservas no retiradas), para reemplazar S11
- [ ] [Referente] Estimación del porcentaje de menú vegetariano (S13) y de retiro para llevar (S14)
- [ ] [Grupo] Si la foto de `imagenes/` es de la web de la UNC y no la tomó el grupo, corregir la fuente en la sección 7

## Fase 2 · Registro de supuestos
- [x] [Claude] `supuestos/supuestos.json` con valor, base, origen y rango de sensibilidad de cada variable
- [x] [Claude] `analisis/render_supuestos.py`, que genera `SUPUESTOS.md`
- [ ] [Grupo] Revisar y aprobar los supuestos propuestos (S08, S09, S11–S15)
- [ ] [Grupo] Resolver **D01**: cómo compatibilizar la espera de 10 a 15 minutos con el tiempo de servicio real
- [ ] [Grupo] Resolver **D02**: si el mostrador entra en el alcance
- [ ] [Grupo] Resolver **D03**: perfiles de demanda (bajo y pico)
- [ ] [Grupo] Resolver **D04**: cómo tratar el escenario del horario límite

## Fase 3 · Dataset ampliado (real + generado)
- [ ] [Claude] Script con semilla fija que genere `data/generado/` y `data/final/reservas_completo.csv`
  - [ ] Filas reales intactas, con `origen = real`
  - [ ] Ausentismo como filas `no_show` (S11) y cancelaciones como filas `canceled` (S12), con `origen = generado_ia`
  - [ ] Atributos `menu_gen` (S13) y `para_llevar_gen` (S14) en cada reserva
- [ ] [Claude] Diccionario de datos (`data/final/DICCIONARIO.md`) que diga, columna por columna, si es real, derivada o generada
- [ ] [Claude] Actualizar el reporte con la distinción entre datos reales y generados
- [ ] [Grupo] Revisar que los datos generados sean coherentes con los reales

## Fase 4 · Tablas para FlexSim
- [ ] [Claude] `flexsim/inputs.xlsx`
  - [ ] `TasaLlegadas`: franja de 10 min × grupo, por perfil de demanda
  - [ ] `MixTipos`: proporciones por tipo, menú y para llevar
  - [ ] `TiemposServicio`: parámetros de validación (y de mostrador si D02 = B)
  - [ ] `Escenarios`: puestos, demanda y cola previa a la apertura
- [ ] [Grupo] Importar con Excel Import/Export a Global Tables

## Fase 5 · Modelo base en FlexSim (Process Flow)
- [ ] [Grupo] Configurar el modelo en segundos, con t = 0 a las 11:40 y apertura a las 12:00
- [ ] [Grupo] Inter-Arrival Source por grupo con tasa por franja (S08) y llegadas previas a la apertura (S09)
- [ ] [Grupo] Asignar labels: grupo, tipo, sin TACC, menú, para llevar
- [ ] [Grupo] Cola y Resource `PuestosValidacion` (1 unidad) con tiempo lognormal (S07)
- [ ] [Grupo] Salida (y mostrador si D02 = B)
- [ ] [Grupo] Layout 3D: cola en serpentina con Path y mesas desde los `.skp` de `3d/` (si no importa, exportar a `.obj`)
- [ ] [Grupo] Registrar las salidas: espera en la cola, cola máxima, utilización, validaciones por franja, reservas no utilizadas
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
  - [ ] E4: horario límite, según D04
  - [ ] Cada escenario en perfil bajo y perfil pico
- [ ] [Claude] Procesar resultados: intervalos de confianza, comparación entre escenarios y gráficos
- [ ] [Grupo] Análisis de sensibilidad de los supuestos generados (rangos en `SUPUESTOS.md`)

## Fase 8 · Informe y entregas
- [ ] [Claude] Borrador de las secciones 7 y 8 de la entrega a partir de `SUPUESTOS.md`
- [ ] [Grupo] Actualizar la **sección 12 (declaración de IA)**: ahora incluye procesamiento del dataset, generación de datos sintéticos y análisis de resultados
- [ ] [Grupo] Corregir en la sección 8 el tiempo de validación (12–18 s → ~3,9 s derivado de los datos)
- [ ] [Grupo] Conclusiones y recomendación de configuración
- [ ] [Grupo] Revisión final y entrega
