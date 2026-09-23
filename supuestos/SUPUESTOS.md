# Registro de supuestos y fuentes de datos

> Generado desde `supuestos/supuestos.json` (v0.3, 2026-09-23). No editar a mano: modificar el JSON y correr `python analisis/render_supuestos.py`.

## Orígenes

- **Registro de la organización** (`registro`, 1): Registros de la organización: dataset de reservas del comedor (data/real/TP-SIM - ds_app.csv), sin modificar.
- **Derivado de registros** (`derivado`, 5): Calculado por el grupo a partir de los registros de la organización, con un script reproducible en analisis/.
- **Estimación del referente** (`referente`, 6): Estimación de un referente que conoce el proceso (integrante del grupo que trabaja en el comedor).
- **Generado (IA)** (`generado`, 9): Dato generado por el grupo con apoyo de IA (Claude), a partir de la base que se indica en cada caso.

## Resumen

| ID | Variable | Origen | Valor | Estado |
|---|---|---|---|---|
| S00 | Reservas retiradas (dataset base) | Registro de la organización | 34.509 reservas retiradas entre el 1 de julio y el 1 de septiembre de 2026 (32 días de servicio), con fecha, hora de reserva, hora de check-in y tipo de cliente. | confirmado |
| S01 | Horario de servicio | Estimación del referente | Lunes a viernes de 12:00 a 14:30 | confirmado |
| S02 | Ventana de reservas (horario límite) | Derivado de registros | 8:00 a 11:00. El 99,6 % de las reservas reales cae en esa franja. | confirmado |
| S03 | Demanda diaria (reservas retiradas por día) | Derivado de registros | Perfil bajo: 723 por día (mediana de julio, 15 días). Perfil pico: 1.543 por día (mediana desde el 10 de agosto, 12 días, rango 1.485–1.607). | confirmado |
| S04 | Composición de la demanda por grupo y tipo | Derivado de registros | Estudiantes 48,8 %, Becas Nutrirse 42,1 %, Becas personal 6,8 %, Personal 2,3 %. Detalle por tipo en reporte/datos.json. | confirmado |
| S05 | Fila única para todos los tipos | Estimación del referente | Todos los tipos, incluidas las viandas de Becas Nutrirse, hacen la misma fila y validan en el mismo puesto. | confirmado |
| S06 | Puestos de validación activos | Estimación del referente | 1 en el escenario base (hay 2 disponibles). | confirmado |
| S07 | Tiempo de validación por persona | Derivado de registros | Lognormal con mu = 1,205 y sigma = 0,494: mediana 3,3 s y media 3,8 s. En la muestra, la mediana es 2,9 s, el percentil 5 es 1,9 s y el percentil 95 es 9,7 s. | confirmado |
| S08 | Tasa de llegadas a la fila por franja de 10 minutos | Derivado de registros | Valor inicial: validaciones promedio por franja y por grupo (reporte/datos.json, campo por_franja), escaladas a la demanda del perfil (S03). Después se calibra (S09, D01). | propuesto |
| S09 | Cola formada antes de la apertura | Generado (IA) | Llegadas uniformes entre las 11:40 y las 12:00. Cantidad inicial: 65 personas en el perfil pico y 30 en el perfil bajo. | aceptado (valores a calibrar) |
| S10 | Objetivo de validación del modelo (cola y espera observadas) | Estimación del referente | Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico. | confirmado |
| S11 | Ausentismo (reservas no retiradas) | Generado (IA) | Estudiantes 10 %, Becas Nutrirse 5 %, Becas personal 6 %, Personal 8 % sobre el total de reservas no canceladas. | propuesto |
| S12 | Cancelaciones definitivas | Generado (IA) | 3 % del total de reservas. | propuesto |
| S13 | Menú vegetariano / no vegetariano | Generado (IA) | 12 % vegetariano, igual para todos los grupos. Independiente de sin TACC, que es un dato real. | propuesto |
| S14 | Consumo en el salón o para llevar | Generado (IA) | Becas Nutrirse Vianda: 50 % para llevar. Resto de los tipos: 15 % para llevar. En total, cerca del 30 % de las retiradas. | propuesto |
| S15 | Tiempo de entrega en el mostrador | Generado (IA) | Lognormal con una mediana de 2,5 s y sigma de 0,4 por línea (vegetariana y no vegetariana). | propuesto |
| S16 | Capacidad de asientos del salón | Estimación del referente | Pendiente: conteo de mesas y sillas del layout modelado en 3D. | pendiente |
| S17 | Tiempo de consumo en el salón | Generado (IA) | Lognormal con una mediana de 20 min y sigma de 0,35 (media de unos 21 min). | propuesto |
| S18 | Regla de elección de asiento | Generado (IA) | Toma el asiento libre más cercano al mostrador. Si no hay asientos libres, espera de pie hasta que se libere uno. | propuesto |
| S19 | Velocidad de caminata | Generado (IA) | 1,2 m/s dentro del salón. | propuesto |
| S20 | Capacidad de la cocina | Estimación del referente | No es restrictiva: la capacidad de preparación supera ampliamente la demanda. | confirmado |

## Detalle

### S00 · Reservas retiradas (dataset base)

- **Origen:** Registro de la organización
- **Valor:** 34.509 reservas retiradas entre el 1 de julio y el 1 de septiembre de 2026 (32 días de servicio), con fecha, hora de reserva, hora de check-in y tipo de cliente.
- **Base:** Export del sistema de reservas del comedor, sin modificar.
- **En FlexSim:** Fuente de S02, S03, S04, S07 y S08, y referencia para validar el modelo
- **Nota:** Solo trae status = used, y customer_id es único por fila (no identifica personas).
- **Usado en:** dataset, modelo, validacion · **Estado:** confirmado

### S01 · Horario de servicio

- **Origen:** Estimación del referente
- **Valor:** Lunes a viernes de 12:00 a 14:30
- **Base:** Operación habitual del comedor. El dataset es consistente: el 99,96 % de los check-ins cae entre las 12:00 y las 14:59.
- **En FlexSim:** Duración de la réplica: 9000 s desde las 12:00 (más el período previo a la apertura, ver S09)
- **Usado en:** modelo · **Estado:** confirmado

### S02 · Ventana de reservas (horario límite)

- **Origen:** Derivado de registros
- **Valor:** 8:00 a 11:00. El 99,6 % de las reservas reales cae en esa franja.
- **Base:** Distribución horaria de reserved_at en los registros reales.
- **En FlexSim:** No es un parámetro del modelo: el horario de corte existe para planificar cuánta comida preparar (D04).
- **Usado en:** dataset · **Estado:** confirmado

### S03 · Demanda diaria (reservas retiradas por día)

- **Origen:** Derivado de registros
- **Valor:** Perfil bajo: 723 por día (mediana de julio, 15 días). Perfil pico: 1.543 por día (mediana desde el 10 de agosto, 12 días, rango 1.485–1.607).
- **Base:** Conteo diario de los registros reales, 32 días de servicio.
- **En FlexSim:** Global Table Escenarios, columna DemandaDia
- **Usado en:** modelo · **Estado:** confirmado

### S04 · Composición de la demanda por grupo y tipo

- **Origen:** Derivado de registros
- **Valor:** Estudiantes 48,8 %, Becas Nutrirse 42,1 %, Becas personal 6,8 %, Personal 2,3 %. Detalle por tipo en reporte/datos.json.
- **Base:** Frecuencias de customer_types en los registros reales.
- **En FlexSim:** Global Table MixTipos y Empirical Distribution para la label tipo
- **Usado en:** modelo · **Estado:** confirmado

### S05 · Fila única para todos los tipos

- **Origen:** Estimación del referente
- **Valor:** Todos los tipos, incluidas las viandas de Becas Nutrirse, hacen la misma fila y validan en el mismo puesto.
- **Base:** Relevamiento con el referente del comedor.
- **En FlexSim:** Una sola cola antes del Resource PuestosValidacion
- **Usado en:** modelo · **Estado:** confirmado

### S06 · Puestos de validación activos

- **Origen:** Estimación del referente
- **Valor:** 1 en el escenario base (hay 2 disponibles).
- **Base:** Relevamiento con el referente: habitualmente opera un solo puesto.
- **En FlexSim:** Resource PuestosValidacion con Count = 1 (base) o 2 (escenario)
- **Usado en:** modelo · **Estado:** confirmado

### S07 · Tiempo de validación por persona

- **Origen:** Derivado de registros
- **Valor:** Lognormal con mu = 1,205 y sigma = 0,494: mediana 3,3 s y media 3,8 s. En la muestra, la mediana es 2,9 s, el percentil 5 es 1,9 s y el percentil 95 es 9,7 s.
- **Base:** El check-in se registra en el puesto de control y opera un solo puesto (S05, S06). En las 13 franjas de 10 minutos con 140 o más validaciones, el puesto está ocupado todo el tiempo, así que el intervalo entre check-ins es el tiempo de servicio (1.959 intervalos). Script: analisis/tiempo_validacion.py.
- **Rango de sensibilidad:** 3 a 5 s de media
- **En FlexSim:** lognormal2(0, 3.34, 0.494, stream). Verificar en la ayuda de FlexSim que scale = e^mu. Alternativa: ajustar data/procesado/intervalos_saturados.csv con ExpertFit.
- **Nota:** Reemplaza el supuesto de 12 a 18 s de la Entrega 1, que no es compatible con el ritmo real observado: hasta 168 validaciones en 10 minutos con un solo puesto.
- **Usado en:** modelo · **Estado:** confirmado

### S08 · Tasa de llegadas a la fila por franja de 10 minutos

- **Origen:** Derivado de registros
- **Valor:** Valor inicial: validaciones promedio por franja y por grupo (reporte/datos.json, campo por_franja), escaladas a la demanda del perfil (S03). Después se calibra (S09, D01).
- **Base:** Cuando el puesto no está saturado, las llegadas son aproximadamente iguales a las validaciones. En las franjas saturadas, las validaciones subestiman las llegadas; por eso el valor se calibra.
- **En FlexSim:** Inter-Arrival Source por grupo con exponential(0, 600 / tasa_franja, stream), leyendo la tasa de la Global Table TasaLlegadas según la franja actual
- **Usado en:** modelo · **Estado:** propuesto

### S09 · Cola formada antes de la apertura

- **Origen:** Generado (IA)
- **Valor:** Llegadas uniformes entre las 11:40 y las 12:00. Cantidad inicial: 65 personas en el perfil pico y 30 en el perfil bajo.
- **Base:** Decisión del grupo (D01): la fila se forma antes de que empiece la atención. Estimación del referente: cola de 60 a 70 personas en el pico. En los datos reales, la primera franja (12:00 a 12:10) valida una mediana de 92 personas, cerca de la capacidad del puesto: eso indica que ya hay cola al abrir. Con 65 llegadas uniformes entre las 11:40 y las 12:00 y 3,9 s por validación, la espera promedio de ese grupo es de unos 12 minutos, dentro de lo observado (S10).
- **Rango de sensibilidad:** 30 a 150 personas
- **En FlexSim:** Source adicional en el período previo; el Resource habilita la atención a las 12:00
- **Usado en:** modelo · **Estado:** aceptado (valores a calibrar)

### S10 · Objetivo de validación del modelo (cola y espera observadas)

- **Origen:** Estimación del referente
- **Valor:** Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico.
- **Base:** Observación directa del referente en un día normal.
- **En FlexSim:** Se compara contra la longitud máxima de la cola y la espera promedio en el pico
- **Nota:** Es compatible con el tiempo de servicio real si la fila se forma antes de la apertura (D01, S09): quien llega a las 11:40 espera la apertura más su turno. Con una cola de 65 que se vacía en unos 4 minutos, la espera promedio de los que llegan antes de abrir ronda los 12 minutos.
- **Usado en:** validacion · **Estado:** confirmado

### S11 · Ausentismo (reservas no retiradas)

- **Origen:** Generado (IA)
- **Valor:** Estudiantes 10 %, Becas Nutrirse 5 %, Becas personal 6 %, Personal 8 % sobre el total de reservas no canceladas.
- **Base:** El export real solo trae reservas retiradas (status = used), así que no hay dato. Se supone un valor mayor para estudiantes porque la reserva no tiene penalidad por no asistir, y menor para las becas porque el beneficio está asociado a la persona. Pendiente de pedirle una estimación al referente.
- **Rango de sensibilidad:** 3 % a 15 %
- **Cómo se genera:** Filas nuevas con status = no_show. La cantidad por día y grupo es retiradas × p / (1 − p). reserved_at se muestrea de las reservas reales del mismo día y grupo. checked_at queda vacío.
- **En FlexSim:** No entran a la fila: las llegadas del día son las reservas menos los ausentes. Salida: raciones preparadas que no se retiran (D04).
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S12 · Cancelaciones definitivas

- **Origen:** Generado (IA)
- **Valor:** 3 % del total de reservas.
- **Base:** El export real no trae cancelaciones definitivas. Los 313 casos reales de cancelar y volver a reservar (0,9 %) muestran que la función se usa. Se supone un valor bajo porque la ventana de reserva es corta (3 horas).
- **Rango de sensibilidad:** 1 % a 6 %
- **Cómo se genera:** Filas nuevas con status = canceled y canceled_at uniforme entre reserved_at y las 11:00.
- **En FlexSim:** No entran a la fila. Solo cambian el conteo de reservas.
- **Usado en:** dataset · **Estado:** propuesto

### S13 · Menú vegetariano / no vegetariano

- **Origen:** Generado (IA)
- **Valor:** 12 % vegetariano, igual para todos los grupos. Independiente de sin TACC, que es un dato real.
- **Base:** El dataset no distingue menú. Supuesto del grupo, pendiente de una estimación del referente.
- **Rango de sensibilidad:** 5 % a 25 %
- **Cómo se genera:** Atributo menu_gen asignado a cada reserva, real o generada, con una Bernoulli de p = 0,12.
- **En FlexSim:** Label menu: define la línea del mostrador (vegetariana o no vegetariana)
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S14 · Consumo en el salón o para llevar

- **Origen:** Generado (IA)
- **Valor:** Becas Nutrirse Vianda: 50 % para llevar. Resto de los tipos: 15 % para llevar. En total, cerca del 30 % de las retiradas.
- **Base:** Criterio del grupo: el retiro para llevar no supera el 30 % del total. Como las viandas son el 42 % de las retiradas (dato real), no pueden llevarse todas: se supone que la mitad come en el salón. Para el resto, supuesto del grupo. Pendiente de confirmar con el referente qué hacen las viandas. Es la variable que más pesa en la ocupación del salón.
- **Rango de sensibilidad:** 20 % a 40 % del total
- **Cómo se genera:** Atributo para_llevar_gen asignado a cada reserva retirada.
- **En FlexSim:** Label para_llevar: después del mostrador, sale del comedor o busca asiento (S16–S18)
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S15 · Tiempo de entrega en el mostrador

- **Origen:** Generado (IA)
- **Valor:** Lognormal con una mediana de 2,5 s y sigma de 0,4 por línea (vegetariana y no vegetariana).
- **Base:** No se puede medir. La cola observada se forma antes de la validación y no en el mostrador, así que el mostrador tiene que atender al menos al ritmo del puesto (3,9 s). Con el 88 % del flujo en la línea no vegetariana, se elige un valor menor.
- **En FlexSim:** Delay en cada línea del mostrador (vegetariana y no vegetariana), 1 servidor por línea
- **Usado en:** modelo · **Estado:** propuesto

### S16 · Capacidad de asientos del salón

- **Origen:** Estimación del referente
- **Valor:** Pendiente: conteo de mesas y sillas del layout modelado en 3D.
- **Base:** Relevamiento del layout real del comedor, modelado por el grupo.
- **En FlexSim:** Cantidad de asientos (objetos o Resource) en el salón
- **Usado en:** modelo · **Estado:** pendiente

### S17 · Tiempo de consumo en el salón

- **Origen:** Generado (IA)
- **Valor:** Lognormal con una mediana de 20 min y sigma de 0,35 (media de unos 21 min).
- **Base:** No se puede medir. Supuesto del grupo para un almuerzo en un comedor universitario con bandeja servida, pendiente de una estimación del referente.
- **Rango de sensibilidad:** 12 a 35 min de mediana
- **En FlexSim:** lognormal2(0, 1200, 0.35, stream) en segundos, desde que se sienta hasta que libera el asiento
- **Usado en:** modelo · **Estado:** propuesto

### S18 · Regla de elección de asiento

- **Origen:** Generado (IA)
- **Valor:** Toma el asiento libre más cercano al mostrador. Si no hay asientos libres, espera de pie hasta que se libere uno.
- **Base:** Supuesto de comportamiento del grupo. Es la regla más simple de justificar y permite medir si falta capacidad.
- **En FlexSim:** Asignación del asiento libre más cercano; espera registrada como indicador (tiempo sin asiento)
- **Usado en:** modelo · **Estado:** propuesto

### S19 · Velocidad de caminata

- **Origen:** Generado (IA)
- **Valor:** 1,2 m/s dentro del salón.
- **Base:** Velocidad de marcha habitual de un peatón adulto, reducida por la circulación entre mesas.
- **Rango de sensibilidad:** 0,8 a 1,4 m/s
- **En FlexSim:** Velocidad de las personas; los tiempos de traslado salen de las distancias del layout
- **Usado en:** modelo · **Estado:** propuesto

### S20 · Capacidad de la cocina

- **Origen:** Estimación del referente
- **Valor:** No es restrictiva: la capacidad de preparación supera ampliamente la demanda.
- **Base:** Relevamiento con el referente del comedor.
- **En FlexSim:** No se modela la cocina; el mostrador siempre tiene bandejas disponibles
- **Usado en:** modelo · **Estado:** confirmado

## Decisiones abiertas

### D01 · Cómo compatibilizar la espera de 10 a 15 minutos con el tiempo de servicio real (resuelta)

Con 3,9 s por persona, una cola de 65 se vacía en unos 4 minutos. Para esperar de 10 a 15 minutos haría falta una cola de 150 a 230 personas, o que la gente llegue antes de la apertura.

- A) Las personas llegan antes de las 12:00 y la espera incluye el tiempo hasta la apertura (S09). Se puede comprobar en el modelo.
- B) Los 10 a 15 minutos son una percepción: se toma como objetivo la cola de 60 a 70 personas y se reporta la diferencia.
- C) La cola real en el pico es más larga que 60 a 70 personas.

**Recomendación:** Decidido: la fila se forma antes de que empiece la atención (S09). Se valida contra la curva real de validaciones por franja y contra la espera observada (S10).

### D02 · ¿El mostrador de entrega entra en el alcance? (resuelta)

La sección 4 de la Entrega 1 termina el sistema en la validación, pero las secciones 5, 8 y 9 hablan del mostrador y de su ocupación.

- A) El sistema termina en la validación. El mostrador y las mesas quedan solo en la animación 3D.
- B) Incluir el mostrador con dos líneas (S13, S15).
- C) Incluir el mostrador y el salón: dónde se sienta la gente y cuánto tiempo ocupa el asiento.

**Recomendación:** Decidido: C. El flujo completo entra en el alcance: fila, validación, mostrador (2 líneas), salón o salida. Agrega los supuestos S16 a S19. Ojo: si se habilita un segundo puesto, el cuello de botella puede pasar a los asientos.

### D03 · Perfiles de demanda a simular (resuelta (por defecto))

- Perfil bajo: 723 por día (julio)
- Perfil pico: 1.543 por día (agosto)

**Recomendación:** Se corren los dos perfiles. El pico responde la pregunta de estudio y el bajo sirve de contraste.

### D04 · Escenario del horario límite de reserva (resuelta)

En los datos reales, la hora de reserva casi no predice la hora de llegada (correlación de 0,13). Quien reserva a las 8:00 valida en una mediana de 13:02, y quien reserva después de las 10 valida en una mediana de 13:17. Según el referente, el horario de corte existe para saber cuánta comida preparar, y la capacidad de la cocina supera ampliamente la demanda (S20).

- A) Modelarlo como un cambio en la cantidad de reservas del día, no en la hora de llegada.
- B) Sacarlo de los escenarios y justificarlo con este dato.
- C) Usar la reserva para definir la demanda: llegadas = reservas − ausentes. El ausentismo se reporta como raciones preparadas y no retiradas.

**Recomendación:** Decidido: B + C. El horario límite sale de los escenarios de la cola, y las reservas definen cuánta gente llega.

### D05 · Reformular la pregunta de estudio (sección 3) (abierta)

La pregunta de la Entrega 1 incluye el horario límite de reserva, que según D04 no afecta la cola. Además, con D02 el salón pasa a ser parte del sistema.

- Propuesta: ¿cuántos puestos de validación deben operar en simultáneo para que la espera en la fila no supere un valor aceptable en el pico, y alcanza la capacidad del salón para absorber el flujo resultante?

**Recomendación:** Ajustar la pregunta y el alcance (sección 4) en la próxima entrega.
