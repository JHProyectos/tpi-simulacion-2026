# Trabajo Práctico Integrador: la fila de un comedor universitario

[TOC]

**Cátedra:** Simulación · 4.º nivel, Ingeniería en Sistemas de Información · 2026

**Integrantes:** Jonatan Harbertz y Juan Chavez

**Sistema estudiado:** atención del almuerzo en un comedor universitario con reserva previa por internet: fila de caja, validación de la reserva y retiro de la comida en el mostrador.

**Herramienta:** FlexSim 2026, módulo Process Flow.

> Este informe sigue los puntos de la consigna de la Entrega 1, actualizados con lo que se construyó, se midió y se decidió después. Al final de cada punto se aclara qué cambió respecto de la Entrega 1. Por pedido de la consigna, la organización no se nombra.

---

## 1. Presentación del proyecto

El comedor sirve almuerzos subsidiados a estudiantes, becarios y personal de la universidad, de lunes a viernes de **12:00 a 14:30**. El almuerzo se **reserva antes por internet**, entre las 8 y las 11 de la mañana del mismo día.

El recorrido de una persona dentro del comedor es secuencial:

1. Llega y se suma a la **fila de caja**. En el horario pico, la fila ya está armada antes de que abra la atención.
2. En el **puesto de validación** presenta un DNI por cada ración que retira (una persona puede retirar por otras).
3. Pasa a la **fila de servicio** y retira la comida en el **mostrador**: en bandeja, o en su propio recipiente si es una vianda. El menú vegetariano se sirve en un puesto aparte del mostrador.
4. Sale hacia el salón, o se va si retiró para llevar.

Para el video, el grupo dibujó el comedor en 3D a partir de su relevamiento. Las imágenes de este informe son esos renders, mejorados con IA (sección 14): muestran la distribución, no son fotos.

@@IMG 3d/video/artlist/01_vista-general_ia.png | | Render del comedor: salón con mesas largas a los lados, el pasillo central con cordones para la fila y la zona de servicio al fondo

Vista desde arriba: la cocina al fondo, la zona de servicio con los puestos y el mostrador, y el salón con las mesas largas:

@@IMG 3d/video/artlist/09_vista-flexsim_ia.png | | Render aéreo del comedor: cocina al fondo, zona de servicio con los puestos y el mostrador, y el salón con las mesas largas

---

## 2. Problemática

### Pregunta de estudio

> **¿Qué combinación de puestos de validación y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?**

### Por qué esa pregunta

En el horario pico se forma una fila de **60 a 70 personas** antes del puesto de validación, con una espera estimada de **10 a 15 minutos** para quienes llegan antes de la apertura (estimación del referente, S10). El comedor tiene dos puestos de validación, pero **habitualmente funciona uno solo**.

La respuesta obvia es habilitar el segundo puesto. Pero si la caja atiende más rápido, la gente llega antes al mostrador, y la cola puede **correrse de lugar** en vez de desaparecer. Por eso el estudio no mira solo la espera en la caja: mide también la cola del mostrador y el **tiempo total** desde que la persona llega hasta que retira la comida, y prueba qué pasa si además se suma una persona más sirviendo.

**Cambios respecto de la Entrega 1:** la pregunta original combinaba los puestos de validación con el horario límite de reserva. Al analizar los registros, el horario límite (8 a 11) resultó ser una herramienta para planificar cuánta comida preparar, sin efecto sobre la fila del mediodía (decisión D04), así que salió de la pregunta. En su lugar entró el mostrador, a pedido de la cátedra, para ver si mejorar la caja solo traslada el cuello de botella.

---

## 3. Alcance del modelo

**Empieza** cuando la persona llega a la fila de caja, antes de la apertura de las 12:00.

**Termina** cuando la persona retira la comida en el mostrador.

> **Supuesto:** que la cola previa empiece a formarse a las 11:40 es una suposición del grupo (S09), no un dato medido. Los registros solo muestran la hora de validación, no la de llegada. Se eligió 11:40 porque, con la cola arrancando a esa hora, el modelo reproduce la fila de 60 a 70 personas y la espera de 10 a 15 minutos que observa el referente (sección 9).

@@IMG 3d/video/artlist/08_recorrido-cenital_ia.png | | Render cenital de la zona de servicio: los puestos de validación arriba, el paso hacia el mostrador y el comienzo del salón abajo

**Dentro del alcance:**

- Llegadas por franja de 10 minutos y por tipo de cliente, incluida la cola que se forma antes de la apertura.
- La demora real del inicio de la atención (la caja casi nunca abre a las 12:00 en punto).
- Uno o dos puestos de validación, con un tiempo por DNI y retiro de varias raciones por persona.
- La fila de servicio y el mostrador, con personas sirviendo y un puesto de menú vegetariano.
- Dos perfiles de demanda: un día **pico** y un día **bajo**.

**Fuera del alcance:**

- El sistema de reservas por internet y el horario límite (D04).
- La cocina: su capacidad supera ampliamente la demanda (S20).
- El salón: la ocupación de mesas y el tiempo de almuerzo.
- Costos e inversión: el criterio de comparación es el tiempo de las personas.
- Interrupciones del puesto: hubo un corte de 14 minutos el 18 de agosto (S26), pero es un caso aislado y no entra en los escenarios.

**Cambios respecto de la Entrega 1:** el sistema terminaba en la validación y empezaba en la reserva online. Ahora empieza en la fila y llega hasta el mostrador (decisión D02).

---

## 4. Estado actual (escenario base, E0)

| Elemento | Situación actual | Fuente |
|---|---|---|
| Horario de atención | 12:00 a 14:30, con la cola formándose desde las 11:40 | Referente (S01), registros (S25) |
| Fila de caja | Una sola para todos los tipos de cliente, viandas incluidas | Referente (S05) |
| Puestos de validación | 1 activo de 2 disponibles | Referente (S06) |
| Validación | Un DNI por ración; unos 4 segundos por DNI | Registros (S07) |
| Personas sirviendo | 3; una de ellas está en el puesto vegetariano y, si está libre, también sirve el menú general | Referente (S22) |
| Servicio | Unos 17 segundos por ración | Referente (S15) |
| Demanda | Día pico: unas 1.380 personas y 1.550 raciones. Día bajo: unas 610 personas y 690 raciones | Registros (S03, S08) |

@@IMG flexsim/capturas/fila-de-caja-flexsim.jpg | | Modelo visual de FlexSim a las 12:09 del día pico: la fila de caja por el pasillo con cordones entre las mesas, hasta los dos puestos de validación

@@IMG 3d/video/artlist/07b_mostrador-completo_ia.png | | Render del mostrador de servicio, con las bandejas de comida detrás del vidrio

**Cambios respecto de la Entrega 1:** se suponía un tiempo de validación de 12 a 18 segundos por persona, calculado a ojo desde el largo de la cola. Con los registros reales del puesto bajó a unos 4 segundos por DNI. Ese cambio movió todo el análisis: la caja tiene más capacidad de lo que creíamos, y el problema del pico se explica por la **concentración de llegadas** alrededor de la apertura más que por la lentitud del puesto.

---

## 5. Escenarios propuestos

Cada escenario se corre en los dos perfiles de demanda, así que son 12 combinaciones. Todos comparten los mismos datos de llegada; solo cambia lo que se indica.

| Escenario | Puestos de validación | Personas sirviendo | Qué se prueba |
|---|---|---|---|
| **E0** (base) | 1 | 3 | La situación actual |
| **E1** | 2 todo el turno | 3 | Habilitar el segundo puesto |
| **E2** | 2 de 12:00 a 13:30, después 1 | 3 | El segundo puesto solo en el pico |
| **E3** | 1, con validación por QR | 3 | Un puesto más rápido en lugar de uno más (60 % del tiempo actual, S24) |
| **E4** | 1 | 4 | Reforzar solo el mostrador |
| **E5** | 2 todo el turno | 4 | Reforzar la caja y el mostrador juntos |

Las comparaciones que responden la pregunta son **E1 contra E0** (¿la cola se corre al mostrador?) y **E5 contra E1** (¿una persona más sirviendo lo evita?).

**Cambios respecto de la Entrega 1:** salieron el horario límite de reserva (D04) y el reordenamiento de mesas, que quedaba fuera del alcance nuevo. Entraron el segundo puesto solo en el pico (E2) y los escenarios del mostrador (E4 y E5).

---

## 6. Fuentes de datos

Cada dato del modelo tiene un identificador (S00 a S33) en el registro de supuestos del proyecto, con su valor, su origen y la base sobre la que se eligió.

| Origen | Qué datos | Ejemplos |
|---|---|---|
| **Registros de la organización** | Export del sistema de reservas: 34.509 raciones retiradas en 32 días de servicio (julio a septiembre de 2026), con hora de reserva, hora de validación y tipo de cliente | S00 |
| **Derivados de los registros** | Calculados a partir de los registros, con procesamiento generado con IA (sección 14) | Demanda por día (S03), composición por tipo (S04), tiempo de validación (S07), llegadas por franja (S08), demora de apertura (S25) |
| **Estimación del referente** | Un integrante del grupo trabaja en el comedor | Fila única (S05), puestos activos (S06), cola observada (S10), personas sirviendo (S22) |
| **Medición propia** | Una visita al comedor de un compañero | Servicio de 15 a 30 segundos (base de S15) |
| **Generados con IA** | Valores supuestos, con la base declarada en cada caso | Cola previa (S09), retiro de varias raciones (S21), factor QR (S24), proporción vegetariana (S27), llegadas concentradas al inicio (S32) |

Los registros originales no se modificaron. Los datos generados están marcados como tales en una columna de origen y nunca se mezclan con los reales sin esa marca.

> **Pendiente:** el referente todavía tiene que confirmar S15 (tiempo de servicio, cronometrando solo el servicio), S21 (retiro de varias raciones), S23 (cuántas personas entran entre la caja y el mostrador), S32 y S33.

---

## 7. Datos de entrada

### 7.1 Llegadas: prueba de bondad de ajuste

Antes de elegir cómo representar las llegadas, se probó si se reparten de manera pareja a lo largo del turno. Se usó la prueba **chi-cuadrado** sobre las **1.175 raciones** consumidas el **1 de julio de 2026**, agrupadas en 6 franjas de 30 minutos.

| Franja | Observadas ($O_i$) | Probabilidad teórica ($p_i$) | Esperadas ($E_i$) | $(O_i - E_i)^2 / E_i$ |
|---|---|---|---|---|
| 12:00 – 12:30 | 304 | 0,1667 | 195,83 | 59,74 |
| 12:30 – 13:00 | 236 | 0,1667 | 195,83 | 8,24 |
| 13:00 – 13:30 | 276 | 0,1667 | 195,83 | 32,82 |
| 13:30 – 14:00 | 191 | 0,1667 | 195,83 | 0,12 |
| 14:00 – 14:30 | 163 | 0,1667 | 195,83 | 5,50 |
| 14:30 – 15:00 | 5 | 0,1667 | 195,83 | 185,96 |
| **Total** | **1.175** | **1,0000** | **1.175,00** | **292,39** |

- $H_0$: las raciones se reparten de manera uniforme entre las seis franjas del turno.
- $H_1$: el reparto difiere significativamente del uniforme.
- Grados de libertad: $k - 1 = 6 - 1 = 5$. No se estima ningún parámetro a partir de la muestra, porque la distribución bajo $H_0$ queda definida sin ajustar nada. Nivel de significación: $\alpha = 0{,}05$.

$$\chi^2_{calc} = \sum \frac{(O_i - E_i)^2}{E_i} = 292{,}39 \;>\; \chi^2_{0,05;\,5} = 11{,}070$$

**Se rechaza $H_0$** con un 95 % de confianza. La demanda está concentrada al principio del turno y se apaga al final: en la primera media hora se sirven 304 raciones y en la última, 5. Esa última franja sola aporta 186 de los 292,39.

**Qué se hizo con este resultado en el modelo:** como las llegadas no se reparten parejo, el modelo no usa una tasa única. Usa **una tasa distinta para cada franja de 10 minutos** y para cada grupo de clientes, calculada desde los registros reales (S08). Dentro de cada franja las llegadas son de Poisson; es decir, el modelo trabaja con un proceso de Poisson **no homogéneo**, cuya tasa sigue la forma real del día.

Los valores observados se obtienen de `data/final/reservas_completo.csv`, contando los registros con `status = used` según la media hora de `checked_at`.

### 7.2 Tipo de cliente: método de Monte Carlo

Cada persona que llega recibe un tipo de cliente al azar, con las proporciones de los registros. Así funciona la asignación por Monte Carlo: se calcula la probabilidad acumulada de cada tipo y se le asigna un rango de números aleatorios de cuatro dígitos.

| Tipo de cliente | Registros | Probabilidad | Acumulada | Rango |
|---|---|---|---|---|
| Estudiante de Grado | 16.629 | 48,19 % | 48,19 % | 0000 – 4818 |
| Becas Nutrirse Vianda | 14.375 | 41,66 % | 89,84 % | 4819 – 8983 |
| Becas No Docentes | 1.870 | 5,42 % | 95,26 % | 8984 – 9525 |
| No Docente | 487 | 1,41 % | 96,67 % | 9526 – 9666 |
| Becas Docentes | 446 | 1,29 % | 97,97 % | 9667 – 9796 |
| Docente | 304 | 0,88 % | 98,85 % | 9797 – 9884 |
| Estudiante de Grado sin TACC | 183 | 0,53 % | 99,38 % | 9885 – 9937 |
| Becas Nutrirse Vianda sin TACC | 137 | 0,40 % | 99,77 % | 9938 – 9976 |
| Becas No Docentes sin TACC | 29 | 0,08 % | 99,86 % | 9977 – 9985 |
| Estudiante Preuniversitario | 24 | 0,07 % | 99,93 % | 9986 – 9992 |
| Usuario de Posgrado | 14 | 0,04 % | 99,97 % | 9993 – 9996 |

Una corrida de 20 números aleatorios da, por ejemplo, 11 estudiantes de grado (55 % contra 48,19 % esperado), 9 becas Nutrirse vianda (45 % contra 41,66 %) y ninguno de los tipos chicos (0 % contra 10,15 %). Con tan pocas corridas manda la variabilidad y los tipos con menos del 5 % pueden no aparecer; al aumentar la cantidad, las frecuencias se acercan a las de la tabla, como dice la ley de los grandes números.

En FlexSim, esta asignación la hace la tabla `MixTipos`: el modelo elige primero el grupo (estudiantes, becas Nutrirse, becas del personal o personal) según la franja, y después el tipo dentro del grupo. Con el tipo quedan definidos si la persona retira vianda y cuántas raciones retira.

### 7.3 Resto de las variables

| Variable | Distribución en el modelo | Fuente |
|---|---|---|
| Llegadas por franja de 10 min y grupo | Poisson, con la tasa de cada franja (proceso no homogéneo) | Registros (S08) |
| Llegadas del inicio del pico | De 12:00 a 12:40, una persona cada 4 s en promedio (Poisson) | Generado (S32) |
| Cola previa a la apertura | Pico: 40 personas uniformes entre 11:55 y 12:00. Bajo: 30 entre 11:40 y 12:00 | Generado y calibrado (S09) |
| Demora de la apertura | Se sortea entre las demoras reales de los 32 días (media 1,9 min, máximo 7,3 min) | Registros (S25) |
| Tiempo de validación por DNI | Lognormal: mediana 3,34 s, media 3,77 s | Registros (S07) |
| Raciones por persona | Becas Nutrirse vianda: 1, 2 o 3 (80 %, 15 %, 5 %). Resto: 1 o 2 (95 %, 5 %) | Generado (S21) |
| Menú vegetariano | 12 % de las personas | Generado (S27) |
| Tiempo de servicio por ración | Lognormal: mediana 17,3 s; el 90 % entre 15 y 20 s | Referente (S15) |
| Tope de la fila de caja | 50 personas; el resto espera en el hall y su espera cuenta igual | Referente (S33) |

El tiempo de validación sale de los registros: es el tiempo entre una validación y la siguiente cuando hay fila (el puesto nunca está ocioso en esos casos). Sobre esas diferencias se ajustó una lognormal, que reproduce la cola larga de los casos lentos (el percentil 95 es 9,7 s).

> **Pendiente:** insertar el histograma de los tiempos de validación con la lognormal ajustada, si se quiere mostrar el ajuste.

---

## 8. Construcción del modelo en FlexSim

El modelo está hecho en **FlexSim 2026** con el módulo **Process Flow**, que la cátedra pidió priorizar sobre el modelado por objetos. Cada persona es un *token* que recorre una secuencia de actividades, y los puestos, la fila de servicio y las personas sirviendo son **recursos** que el token toma y libera.

### 8.1 Configuración del modelo

El reloj arranca a las **11:40**, cuando empieza a formarse la cola previa, y cada réplica termina a las **16:00** (15.600 segundos), con margen de sobra para que todos salgan. El tiempo está en segundos y las distancias en metros.

@@IMG flexsim/capturas/avance-01.png | | Ventana Model Units de FlexSim: tiempo en segundos, longitud en metros e inicio a las 11:40

### 8.2 Tablas de entrada

Todos los datos de entrada se calcularon a partir de los registros y del registro de supuestos (con el procesamiento descripto en la sección 14), y se exportaron a una planilla, `inputs.xlsx`, con una hoja por tabla. En FlexSim se importaron como **Global Tables** con la herramienta *Excel Import/Export*. Así, si cambia un supuesto, se regenera la planilla y se vuelve a importar, sin tocar el modelo.

@@IMG flexsim/capturas/avance-05.png | | Global Table TasaLlegadas_Bajo importada: franjas de 10 minutos y personas por grupo de cliente

Las tablas son: `TasaLlegadas_Pico` y `TasaLlegadas_Bajo` (llegadas por franja y grupo), `ColaPrevia`, `DemoraApertura`, `MixTipos`, `TiemposServicio` y `Escenarios`. La última tiene una fila por escenario y perfil, y dice cuántos puestos y cuántas personas sirviendo usa cada uno.

### 8.3 El parámetro `Escenario`

El modelo tiene un único parámetro, `Escenario`, un entero de 1 a 12 que indica qué fila de la tabla `Escenarios` usa la corrida. Todo lo que cambia entre escenarios se lee de esa fila al empezar cada réplica. Esto permite que el Experimenter recorra los 12 escenarios cambiando un solo número.

@@IMG flexsim/capturas/Captura parametro Escenario.png | | Parámetro Escenario del modelo: entero de 1 a 12 que apunta a la tabla Escenarios

### 8.4 Recursos y control de los puestos

El Process Flow tiene cuatro recursos: `PuestosValidacion`, `EspacioFilaServicio`, `ServicioComida` (las personas que sirven) y `PuestoVeg` (el puesto vegetariano).

Los puestos no están abiertos todo el tiempo: los controlan dos columnas de actividades que corren aparte del flujo de las personas.

- **Inicio del día:** lee el escenario, crea la cola previa, **bloquea los puestos** hasta la apertura (que se sortea con la demora real) y después los libera.
- **Puesto extra (E2):** abre el segundo puesto a las 12:00 y lo vuelve a bloquear a las 13:30.

@@IMG flexsim/capturas/Captura de pantalla 2026-11-08 203020.png | 290,85,1080,440 | Recursos del Process Flow arriba y las dos columnas de control: inicio del día y puesto extra

### 8.5 El recorrido de cada persona

La columna de la derecha es el recorrido de la persona:

1. **Llegadas:** dos fuentes crean los tokens. Una genera la cola previa entre las 11:40 y las 12:00, y la otra las llegadas por franja.
2. **Asignar tipo y raciones:** el Monte Carlo de la sección 7.2.
3. **Esperar en la fila:** toma un puesto de validación (si no hay uno libre, espera en la fila de caja).
4. **Validar:** demora un tiempo de validación por cada ración.
5. **Entrar a la fila de servicio** y liberar el puesto.
6. **¿Es vegetariano?:** si lo es, toma el puesto vegetariano; si no, va directo.
7. **Esperar servidor** y **Servir raciones:** un tiempo de servicio por ración.
8. **Registrar y salir:** anota sus tiempos en la tabla de salida.

@@IMG flexsim/capturas/Captura de pantalla 2026-11-08 203020.png | 1150,85,1722,883 | Recorrido de la persona en el Process Flow: las dos fuentes de llegadas, la validación, la decisión del menú vegetariano, el servicio y la salida

Así queda el Process Flow completo:

@@IMG flexsim/capturas/Captura de pantalla 2026-11-08 203020.png | | Process Flow completo al final de una réplica: tablas en el Toolbox, recursos arriba, columnas de control a la izquierda y el recorrido de la persona a la derecha

### 8.6 Tablas de salida e indicadores

Cada persona, al salir, escribe una fila en `Salida_Personas` con sus tiempos: llegada, inicio y fin de la validación, entrada a la fila de servicio, inicio del servicio y salida. Además, `Salida_Dia` guarda los máximos del día (cola de caja, cola de servicio, hora de apertura).

A partir de esas tablas, cinco **User Commands** calculan los indicadores al final de cada réplica, y una **Performance Measure Table** los expone al Experimenter.

@@IMG flexsim/capturas/Captura de pantalla 2026-11-11 064914.png | | User Commands del modelo: TiempoTotalMin, EsperaMaxCajaMin, EsperaServicioMin, CajaBloqueadaMin y UtilizacionCajaPct

| Indicador | Qué mide |
|---|---|
| `TiempoTotal_min` | Tiempo medio desde que la persona llega hasta que retira la comida |
| `EsperaMaxCaja_min` | La mayor espera en la caja contada desde la apertura (deja afuera la espera previa a las 12:00, que no depende de los puestos) |
| `EsperaServicio_min` | Espera media en la fila de servicio |
| `CajaBloqueada_min` | Tiempo en que la caja no puede atender porque la fila de servicio está llena |
| `UtilizacionCaja_pct` | Porcentaje del tiempo en que los puestos abiertos están ocupados |
| `ColaCajaMax` y `ColaServicioMax` | Personas en cada fila en su peor momento |
| `PersonasDia` | Personas atendidas en el día |

### 8.7 Animación 3D

Para el video se armó aparte una versión visual del modelo, con el dibujo del comedor importado desde SketchUp y personas del módulo **People** de FlexSim que caminan, hacen la fila y retiran la comida. Esa versión no sortea nada: reproduce una tabla de llegadas ya calculada (*replay*), con la hora de llegada, el puesto y los tiempos de cada persona.

En la planta del modelo visual se ven las ubicaciones (*Locations*) que usan las personas: `Caja_Loc1` en el puesto de validación, el `PasoCentral` hacia el mostrador, `Mostrador_Loc1` a `Mostrador_Loc4` (el cuarto se usa en E4 y E5) con los servidores detrás, y la `Salida`.

@@IMG flexsim/capturas/planta-locations-people.png | | Planta del modelo visual en FlexSim con las ubicaciones del módulo People: Caja_Loc1, PasoCentral, Mostrador_Loc1 a Mostrador_Loc4, los servidores y la salida

@@IMG flexsim/capturas/Captura de pantalla 2026-11-08 233706.png | | Schedule Source Llegadas del modelo visual: 1.376 llegadas con su hora, el puesto y los tiempos de validación de cada persona

> La animación es ilustrativa. Todos los números del informe salen del modelo de análisis y del Experimenter, no de la animación.

---

## 9. Verificación y validación

**Verificación** (¿el modelo hace lo que diseñamos?). Sobre una corrida del escenario base se comprobó que:

- los tiempos de cada persona van en orden (llegada, validación, servicio, salida);
- la cantidad de personas y de raciones del día queda dentro de lo esperado (1.369 personas contra 1.381 esperadas);
- al final no queda nadie en ninguna fila y todos salen antes de las 16:00.

**Validación** (¿el modelo se parece al comedor real?). Se comparó el escenario base con los registros y con lo observado por el referente:

| Chequeo | Modelo | Real | Resultado |
|---|---|---|---|
| Curva de raciones por franja de 10 min (correlación) | 0,946 | mínimo 0,9 | OK |
| Total de raciones del día | −1,5 % | ±5 % | OK |
| Cola máxima en la caja | 66 personas | 60 a 70 (S10) | OK |
| Espera de quienes llegan antes de la apertura | 13,0 min | 10 a 15 min (S10) | OK |

```grafico
tipo: lineas
titulo: Raciones validadas por franja, día pico (E0)
unidad: raciones

Franja, Registros reales, Modelo
12:00, 103.5, 100.0
12:10, 134.9, 109.0
12:20, 124.8, 132.0
12:30, 119.3, 126.0
12:40, 117.8, 115.0
12:50, 104.6, 98.0
13:00, 119.3, 118.0
13:10, 126.9, 136.0
13:20, 119.8, 123.0
13:30, 99.0, 94.0
13:40, 75.4, 94.0
13:50, 75.5, 68.0
14:00, 72.4, 87.0
14:10, 81.7, 70.0
14:20, 62.4, 49.0
14:30, 8.4, 3.0
```

La primera franja del modelo da algo menos que la real porque la caja abre con demora (S25).

> **Pendiente:** esta validación se hizo con una corrida anterior al ajuste del tiempo de servicio (S15). Hay que repetirla con el modelo final (`comedor_unc_3`) y actualizar la tabla. Los valores de la caja no deberían cambiar, porque el ajuste solo tocó el mostrador.

---

## 10. Experimentación

### 10.1 Tipo de simulación

Es una simulación **terminante**: cada réplica es un día de servicio que empieza vacío a las 11:40 y termina a las 16:00. Por eso no hay período de calentamiento (*warmup* = 0): el arranque vacío es parte del sistema real, porque el comedor está vacío antes de la cola previa.

### 10.2 Configuración del Experimenter

En el **Experimenter** de FlexSim se creó un *job*, `Escenarios_E0_E5`, con los 12 escenarios (los 6 escenarios en los dos perfiles), cada uno con su valor del parámetro `Escenario`.

@@IMG flexsim/capturas/Captura de pantalla 2026-11-11 062548.png | | Experimenter: job Escenarios_E0_E5 con warmup 0, parada a las 16:00, 30 réplicas por escenario y los 12 escenarios de E0_Pico a E5_Bajo

### 10.3 Corrida piloto

Antes de la corrida completa se hizo una corrida piloto de 5 réplicas por escenario, para verificar que los indicadores salieran con valores razonables. Ya con esas 5 réplicas se veía el efecto principal, que la corrida completa confirmó.

En los gráficos de FlexSim los escenarios se numeran de S1 a S12: S1 a S6 son E0 a E5 en el día pico, y S7 a S12 son E0 a E5 en el día bajo.

### 10.4 Corrida completa: 30 réplicas

Después se corrieron **30 réplicas por escenario**: 360 días simulados. El Experimenter las reparte entre los núcleos del procesador y las corre en paralelo.

@@IMG flexsim/capturas/Captura de pantalla 2026-11-11 062615.png | | Experimenter corriendo las 30 réplicas: réplicas completas en verde, en curso en rojo y en cola en azul

**Números aleatorios comunes.** La réplica número *n* de cada escenario usa la misma semilla, así que las personas que llegan ese día son las mismas en todos los escenarios del mismo perfil. Lo único que cambia es la configuración de puestos y servidores. Esto permite **comparaciones pareadas**: la diferencia entre dos escenarios se calcula réplica por réplica, y el intervalo de confianza de la diferencia sale mucho más angosto que si se compararan dos promedios independientes.

**Intervalos de confianza.** Para cada indicador se calcula la media de las 30 réplicas y su intervalo de confianza al 95 % con la *t* de Student:

$$\bar{x} \pm t_{0,025;\,29} \cdot \frac{s}{\sqrt{30}}, \qquad t_{0,025;\,29} = 2{,}045$$

Una diferencia entre escenarios es **significativa** si su intervalo no incluye el cero.

Los resultados se exportaron desde el Experimenter (*Generate Report*) y se procesaron para calcular las medias, los intervalos y las comparaciones pareadas (sección 14).

@@IMG flexsim/capturas/Captura de pantalla 2026-11-11 063234.png | 150,0,1125,632 | Resultados de las 30 réplicas: diagrama de caja de la espera media en la fila de servicio por escenario

@@IMG flexsim/capturas/Captura de pantalla 2026-11-11 063359.png | | Resultados de las 30 réplicas: diagrama de caja del tiempo total en el sistema por escenario

### 10.5 ¿Alcanzan 30 réplicas?

Se mide la precisión con el **semiancho relativo** del intervalo: el semiancho dividido por la media. Si es menor que 5 %, la precisión alcanza; si no, la cantidad de réplicas necesaria se estima con $n \approx (t \, s / h)^2$, donde $h$ es el semiancho buscado.

| Indicador | Peor semiancho relativo (pico) | Escenario |
|---|---|---|
| Espera máxima en la caja | 4,7 % | E2 |
| Cola máxima en la caja | 3,6 % | E0 |
| Utilización de la caja | 1,3 % | E3 |
| Tiempo total medio | 8,3 % | E4 |
| Cola máxima en el servicio | 10,3 % | E5 |
| Espera media en el servicio | 17,2 % | E3 |

Los indicadores de la caja ya tienen buena precisión. Los del servicio y el tiempo total quedan por encima del 5 %, pero eso no cambia las conclusiones: las comparaciones pareadas entre escenarios dan intervalos que no tocan el cero (sección 11).

> **Pendiente:** decidir si se corren más réplicas para los indicadores del servicio, o si se deja así con esta justificación.

---

## 11. Resultados

### 11.1 Día pico

Media de las 30 réplicas con el semiancho del intervalo de confianza al 95 %.

| Escenario | Tiempo total medio (min) | Espera máx. en caja (min) | Cola máx. en caja (personas) | Cola máx. en servicio (personas) | Espera media en servicio (min) | Utilización de la caja (%) |
|---|---|---|---|---|---|---|
| **E0** base | 1,14 ± 0,09 | 4,89 ± 0,23 | 70,6 ± 2,5 | 4,8 ± 0,5 | 0,016 | 62,5 |
| **E1** 2 puestos | 0,98 ± 0,07 | 2,42 ± 0,11 | 70,5 ± 2,5 | 30,8 ± 1,9 | 0,086 | 31,2 |
| **E2** 2 puestos hasta 13:30 | 0,99 ± 0,07 | 2,42 ± 0,11 | 70,5 ± 2,5 | 30,8 ± 1,9 | 0,084 | 31,2 |
| **E3** validación por QR | 0,96 ± 0,07 | 2,93 ± 0,14 | 70,6 ± 2,5 | 22,7 ± 2,2 | 0,069 | 37,5 |
| **E4** 4 sirviendo | 1,13 ± 0,09 | 4,89 ± 0,23 | 70,6 ± 2,5 | 3,1 ± 0,2 | 0,004 | 62,5 |
| **E5** 2 puestos y 4 sirviendo | **0,92 ± 0,06** | **2,42 ± 0,11** | 70,5 ± 2,5 | 16,2 ± 1,7 | 0,027 | 31,2 |

```grafico
tipo: barras
titulo: Espera máxima en la caja desde la apertura, día pico
unidad: min

Escenario, Media
E0, 4.89
E1, 2.42
E2, 2.42
E3, 2.93
E4, 4.89
E5, 2.42
```

```grafico
tipo: barras
titulo: Cola máxima en la fila de servicio, día pico
unidad: personas

Escenario, Media
E0, 4.8
E1, 30.8
E2, 30.8
E3, 22.7
E4, 3.1
E5, 16.2
```

### 11.2 Comparaciones pareadas, día pico

Diferencia media (escenario menos base) con su intervalo al 95 %.

| Comparación | Tiempo total (min) | Espera máx. en caja (min) | Cola máx. en servicio (personas) |
|---|---|---|---|
| E1 contra E0: segundo puesto | −0,16 [−0,20; −0,13] | −2,47 [−2,58; −2,35] | **+26,0** [24,1; 27,9] |
| E2 contra E0: segundo puesto hasta 13:30 | −0,15 [−0,18; −0,12] | −2,47 [−2,58; −2,35] | +26,0 [24,1; 27,9] |
| E3 contra E0: validación por QR | −0,18 [−0,21; −0,14] | −1,96 [−2,05; −1,87] | +17,9 [15,7; 20,1] |
| E4 contra E0: 4.ª persona sirviendo | −0,01 [−0,01; −0,01] | 0,00 (no significativa) | −1,7 [−2,2; −1,2] |
| E5 contra E0: 2 puestos y 4 sirviendo | **−0,22** [−0,27; −0,18] | −2,47 [−2,58; −2,35] | +11,3 [9,7; 12,9] |
| E5 contra E1: sumar la 4.ª persona | −0,06 [−0,07; −0,05] | 0,00 (no significativa) | **−14,6** [−15,7; −13,6] |

Todas las diferencias son significativas, salvo las dos marcadas: sumar una persona en el mostrador no cambia la espera en la caja, como era de esperar.

### 11.3 Día bajo

| Escenario | Tiempo total medio (min) | Espera máx. en caja (min) | Cola máx. en servicio (personas) | Utilización de la caja (%) |
|---|---|---|---|---|
| **E0** base | 0,98 ± 0,08 | 2,54 ± 0,19 | 3,2 ± 0,4 | 28,1 |
| **E1** 2 puestos | 0,93 ± 0,08 | 1,25 ± 0,10 | 16,1 ± 1,9 | 14,0 |
| **E2** 2 puestos hasta 13:30 | 0,93 ± 0,08 | 1,25 ± 0,10 | 16,1 ± 1,9 | 14,0 |
| **E3** validación por QR | 0,91 ± 0,08 | 1,52 ± 0,12 | 11,9 ± 1,6 | 16,8 |
| **E4** 4 sirviendo | 0,97 ± 0,08 | 2,54 ± 0,19 | 2,2 ± 0,3 | 28,1 |
| **E5** 2 puestos y 4 sirviendo | 0,91 ± 0,07 | 1,25 ± 0,10 | 9,2 ± 1,4 | 14,0 |

En el día bajo, con un solo puesto, la espera máxima en la caja es de 2,5 minutos y el puesto está ocupado menos del 30 % del tiempo. El patrón es el mismo que en el pico, pero en una escala que no justifica cambios.

### 11.4 Qué muestran los resultados

1. **En la situación actual, la caja es el cuello de botella del pico, y el mostrador no.** La cola de la caja llega a unas 70 personas y la del mostrador no pasa de 5.
2. **Habilitar el segundo puesto traslada la cola.** E1 reduce a la mitad la espera máxima en la caja (de 4,9 a 2,4 min), pero la cola del mostrador pasa de 5 a **31 personas**. Es exactamente el efecto que planteaba la pregunta.
3. **Reforzar solo el mostrador no sirve.** E4 casi no cambia nada, porque con un solo puesto al mostrador le llega gente a un ritmo que ya puede atender.
4. **La combinación es la mejor.** E5 (2 puestos y 4 personas sirviendo) logra el menor tiempo total y la misma mejora en la caja que E1, con la mitad de la cola en el mostrador que E1 (16 personas en lugar de 31).
5. **El segundo puesto alcanza con abrirlo en el pico.** E2 (segundo puesto de 12:00 a 13:30) da los mismos resultados que E1: después de las 13:30, la demanda la cubre un solo puesto.
6. **El QR es una alternativa intermedia.** E3 mejora la caja menos que un segundo puesto (2,9 contra 2,4 min) y traslada menos cola al mostrador (23 personas).
7. **La cola de la caja antes de la apertura no cambia en ningún escenario** (unas 70 personas): se forma antes de las 12:00 y depende de cuándo llega la gente, no de cuántos puestos hay.

---

## 12. Conclusiones y respuesta a la pregunta

> **¿Qué combinación de puestos de validación y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?**

**Con 2 puestos de validación en el pico (de 12:00 a 13:30) y 4 personas sirviendo.** Es la configuración que reduce más el tiempo total (−0,22 min por persona en promedio) y que reduce a la mitad la espera máxima en la caja (de 4,9 a 2,4 minutos).

Sin la cuarta persona sirviendo, el segundo puesto solo cambia la cola de lugar: la del mostrador pasa de 5 a 31 personas. Con la cuarta persona baja a 16. **El traslado se reduce a la mitad, pero no desaparece del todo**: la cola del mostrador sigue siendo mayor que en la situación actual, aunque avanza rápido (la espera media en el servicio queda por debajo de los 2 segundos).

Para el día bajo, la configuración actual (1 puesto y 3 personas sirviendo) alcanza.

**Recomendación operativa:** abrir el segundo puesto de 12:00 a 13:30 en los días de mucha demanda y sumar una persona al mostrador en ese mismo horario.

**Qué no resuelve ningún escenario:** la espera de quienes llegan antes de la apertura, que en el modelo es de unos 13 minutos. Esa espera depende de la hora a la que llega la gente y de la demora en abrir, no de la capacidad de atención. Abrir puntual a las 12:00 la acortaría (hoy la caja abre en promedio 1,9 minutos tarde).

> **Pendiente:** confirmar si conviene agregar un escenario con 2 puestos solo en el pico y 4 personas sirviendo también solo en el pico (E2 + E4), que es lo que se recomienda, y otro con 5 personas sirviendo para ver si la cola del mostrador vuelve al nivel actual.

### Limitaciones

- El tiempo de servicio (S15) es una estimación de una sola visita; el resultado del mostrador depende mucho de ese valor.
- La capacidad de la fila de servicio (S23) no está medida: en el modelo no tiene límite, por eso el indicador de caja bloqueada da cero en todos los escenarios. Si el espacio real es chico, la cola del mostrador de E1 bloquearía la caja y el segundo puesto rendiría menos.
- El retiro de varias raciones por persona (S21), la proporción vegetariana (S27) y la concentración de llegadas al inicio del pico (S32) son datos generados, a confirmar con el referente.
- Las diferencias de tiempo total son chicas en promedio (unos 13 segundos por persona) porque la mayoría de la gente llega cuando no hay fila. El beneficio se concentra en quienes llegan en el pico, y por eso se mira también la espera máxima.

---

## 13. Software de simulación

| Herramienta | Uso |
|---|---|
| **FlexSim 2026** (licencia Education), módulo Process Flow | Modelo de análisis, Experimenter y estadísticas |
| FlexSim, módulo People | Animación 3D con personas para el video |
| SketchUp | Dibujo del comedor, importado a FlexSim |
| Planilla de cálculo | Prueba chi-cuadrado y tablas de Monte Carlo |

---

## 14. Declaración de uso de inteligencia artificial

El grupo usó **Claude (Anthropic)** durante el proyecto, con estas finalidades:

- **Procesamiento de datos:** todo el código en Python del proyecto lo generó Claude: el que procesa los registros, ajusta las distribuciones, arma las tablas para FlexSim, verifica las corridas y calcula los intervalos a partir de los resultados del Experimenter. El grupo revisó los resultados, no escribió ese código.
- **Generación de datos:** proponer valores para lo que no se pudo medir (S09, S11, S12, S21, S24, S27, S32). Cada uno está marcado como generado en el registro de supuestos, con la base sobre la que se eligió.
- **Apoyo en la construcción del modelo:** guías paso a paso para armar el Process Flow, el código de los User Commands y la configuración del Experimenter. El modelo lo construyó el grupo en FlexSim.
- **Imágenes:** los renders del comedor salen del modelo 3D del grupo y se mejoraron con IA generativa (Artlist) para el video y este informe.
- **Redacción:** ordenar y redactar este informe y el guion del video, a partir de las decisiones y los resultados del grupo.

Las decisiones metodológicas (alcance, pregunta, escenarios, qué supuestos aceptar) las tomó el grupo. Los resultados salen de las corridas de FlexSim, no de la IA.

---

## Anexo A. Registro de supuestos

| ID | Variable | Origen | Estado |
|---|---|---|---|
| S00 | Reservas retiradas (registros base) | Registros | Confirmado |
| S01 | Horario de servicio, 12:00 a 14:30 | Referente | Confirmado |
| S02 | Ventana de reservas, 8:00 a 11:00 | Derivado | Confirmado |
| S03 | Demanda diaria por perfil | Derivado | Confirmado |
| S04 | Composición de la demanda por tipo | Derivado | Confirmado |
| S05 | Fila única para todos los tipos | Referente | Confirmado |
| S06 | 1 puesto de validación activo | Referente | Confirmado |
| S07 | Tiempo de validación por DNI | Derivado | Confirmado |
| S08 | Llegadas por franja de 10 minutos | Derivado | Propuesto |
| S09 | Cola previa a la apertura | Generado | Calibrado |
| S10 | Cola y espera observadas (validación) | Referente | Confirmado |
| S15 | Tiempo de servicio por ración | Referente | Propuesto |
| S20 | La cocina no limita | Referente | Confirmado |
| S21 | Varias raciones por persona | Generado | Propuesto |
| S22 | 3 personas sirviendo | Referente | Confirmado |
| S23 | Espacio de la fila de servicio | Referente | Pendiente |
| S24 | Validación con QR (60 % del tiempo) | Generado | Propuesto |
| S25 | Demora de la apertura | Derivado | Confirmado |
| S26 | Interrupción del 18 de agosto | Derivado | Confirmado |
| S27 | 12 % de menú vegetariano | Generado | Propuesto |
| S32 | Llegadas concentradas al inicio del pico | Generado | Propuesto |
| S33 | Tope de 50 personas en la fila de caja | Referente | Propuesto |

El detalle de cada uno (valor, base y uso en el modelo) está en el registro de supuestos del repositorio.
