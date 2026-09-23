# Registro de supuestos y fuentes de datos

> Generado desde `supuestos/supuestos.json` (v0.6, 2026-09-23). No editar a mano: modificar el JSON y correr `python analisis/render_supuestos.py`.

## Orígenes

- **Registro de la organización** (`registro`, 1): Registros de la organización: dataset de reservas del comedor (data/real/TP-SIM - ds_app.csv), sin modificar.
- **Derivado de registros** (`derivado`, 6): Calculado por el grupo a partir de los registros de la organización, con un script reproducible en analisis/.
- **Estimación del referente** (`referente`, 6): Estimación de un referente que conoce el proceso (integrante del grupo que trabaja en el comedor).
- **Generado (IA)** (`generado`, 6): Dato generado por el grupo con apoyo de IA (Claude), a partir de la base que se indica en cada caso.

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
| S07 | Tiempo de validación por ración (por DNI) | Derivado de registros | Lognormal con mu = 1,205 y sigma = 0,494: mediana 3,3 s y media 3,8 s. En la muestra, la mediana es 2,9 s, el percentil 5 es 1,9 s y el percentil 95 es 9,7 s. | confirmado |
| S08 | Tasa de llegadas a la fila por franja de 10 minutos | Derivado de registros | Valor inicial: validaciones promedio por franja y por grupo (reporte/datos.json, campo por_franja), escaladas a la demanda del perfil (S03). Son raciones: la tasa de personas es la de raciones dividida por las raciones promedio por persona del grupo (S21). Después se calibra (S09, D01). | propuesto |
| S09 | Cola formada antes de la apertura | Generado (IA) | Llegadas uniformes entre las 11:40 y las 12:00. Cantidad inicial: 65 personas en el perfil pico y 30 en el perfil bajo. | aceptado (valores a calibrar) |
| S10 | Objetivo de validación del modelo (cola y espera observadas) | Estimación del referente | Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico. Hoy la cola se forma antes de la caja y no en el mostrador. | confirmado |
| S11 | Ausentismo (reservas no retiradas) | Generado (IA) | Estudiantes 10 %, Becas Nutrirse 5 %, Becas personal 6 %, Personal 8 % sobre el total de reservas no canceladas. | propuesto |
| S12 | Cancelaciones definitivas | Generado (IA) | 3 % del total de reservas. | propuesto |
| S13 | Menú: con o sin TACC | Derivado de registros | El menú solo se distingue por ser con o sin TACC, y eso viene del tipo de cliente (dato real): 1 % de las raciones es sin TACC. No hay menú vegetariano. | confirmado |
| S15 | Tiempo de servicio en el mostrador por ración | Generado (IA) | Lognormal con una mediana de 5 s y sigma de 0,4 (media de unos 5,4 s) por ración y por persona que sirve. Quien retira varias raciones suma una muestra por ración. | propuesto |
| S20 | Capacidad de la cocina | Estimación del referente | No es restrictiva: la capacidad de preparación supera ampliamente la demanda. | confirmado |
| S21 | Retiro de más de una ración por persona | Generado (IA) | Becas Nutrirse Vianda: 80 % retira 1 ración, 15 % retira 2 y 5 % retira 3 (1,25 raciones por persona). Resto de los tipos: 95 % retira 1 y 5 % retira 2 (1,05 por persona). | propuesto |
| S22 | Personas sirviendo en el mostrador | Generado (IA) | 2 en el escenario base. Se prueba con 3 (E5). | propuesto |
| S23 | Espacio de la fila entre la caja y el mostrador | Estimación del referente | Pendiente: cuántas personas entran entre la caja y el mostrador. | pendiente |

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
- **Nota:** Es la situación actual (escenario base). Después de la caja hay una segunda fila, la del servicio de comida (S15, S22). Como caso de estudio se propone separar dos filas según el tipo de cliente (E4, D06).
- **Usado en:** modelo · **Estado:** confirmado

### S06 · Puestos de validación activos

- **Origen:** Estimación del referente
- **Valor:** 1 en el escenario base (hay 2 disponibles).
- **Base:** Relevamiento con el referente: habitualmente opera un solo puesto.
- **En FlexSim:** Resource PuestosValidacion con Count = 1 (base) o 2 (escenarios E1, E2, E4 y E5)
- **Usado en:** modelo · **Estado:** confirmado

### S07 · Tiempo de validación por ración (por DNI)

- **Origen:** Derivado de registros
- **Valor:** Lognormal con mu = 1,205 y sigma = 0,494: mediana 3,3 s y media 3,8 s. En la muestra, la mediana es 2,9 s, el percentil 5 es 1,9 s y el percentil 95 es 9,7 s.
- **Base:** El check-in se registra en el puesto de control y opera un solo puesto (S05, S06). En las 13 franjas de 10 minutos con 140 o más validaciones, el puesto está ocupado todo el tiempo, así que el intervalo entre check-ins es el tiempo de servicio (1.959 intervalos). Script: analisis/tiempo_validacion.py.
- **Rango de sensibilidad:** 3 a 5 s de media
- **En FlexSim:** lognormal2(0, 3.34, 0.494, stream) por cada ración de la persona (label raciones, S21): quien retira 2 raciones suma 2 muestras. Verificar en la ayuda de FlexSim que scale = e^mu. Alternativa: ajustar data/procesado/intervalos_saturados.csv con ExpertFit.
- **Nota:** Es un tiempo por DNI, no por persona: en los datos casi no hay check-ins a menos de 1,5 s del anterior (0,2 %), así que cada DNI se valida por separado aunque lo presente la misma persona (S21). Reemplaza el supuesto de 12 a 18 s de la Entrega 1, que no es compatible con el ritmo real observado: hasta 168 validaciones en 10 minutos con un solo puesto.
- **Usado en:** modelo · **Estado:** confirmado

### S08 · Tasa de llegadas a la fila por franja de 10 minutos

- **Origen:** Derivado de registros
- **Valor:** Valor inicial: validaciones promedio por franja y por grupo (reporte/datos.json, campo por_franja), escaladas a la demanda del perfil (S03). Son raciones: la tasa de personas es la de raciones dividida por las raciones promedio por persona del grupo (S21). Después se calibra (S09, D01).
- **Base:** Cuando el puesto no está saturado, las llegadas son aproximadamente iguales a las validaciones. En las franjas saturadas, las validaciones subestiman las llegadas; por eso el valor se calibra.
- **En FlexSim:** Inter-Arrival Source por grupo con exponential(0, 600 / tasa_personas, stream), leyendo la tasa de la Global Table TasaLlegadas según la franja actual. El Source asigna las labels grupo, tipo, sin_tacc y raciones desde el origen.
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
- **Valor:** Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico. Hoy la cola se forma antes de la caja y no en el mostrador.
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
- **En FlexSim:** No entran a la fila: las llegadas del día son las reservas menos los ausentes. Se reporta como raciones reservadas que no se retiran (D04).
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S12 · Cancelaciones definitivas

- **Origen:** Generado (IA)
- **Valor:** 3 % del total de reservas.
- **Base:** El export real no trae cancelaciones definitivas. Los 313 casos reales de cancelar y volver a reservar (0,9 %) muestran que la función se usa. Se supone un valor bajo porque la ventana de reserva es corta (3 horas).
- **Rango de sensibilidad:** 1 % a 6 %
- **Cómo se genera:** Filas nuevas con status = canceled y canceled_at uniforme entre reserved_at y las 11:00.
- **En FlexSim:** No entran a la fila. Solo cambian el conteo de reservas.
- **Usado en:** dataset · **Estado:** propuesto

### S13 · Menú: con o sin TACC

- **Origen:** Derivado de registros
- **Valor:** El menú solo se distingue por ser con o sin TACC, y eso viene del tipo de cliente (dato real): 1 % de las raciones es sin TACC. No hay menú vegetariano.
- **Base:** Relevamiento con el grupo. Reemplaza la propuesta anterior de un 12 % de menú vegetariano, que se descarta.
- **En FlexSim:** Label sin_tacc asignada en el Source junto con el tipo. Es informativa: no cambia la fila ni el tiempo de servicio.
- **Usado en:** modelo · **Estado:** confirmado

### S15 · Tiempo de servicio en el mostrador por ración

- **Origen:** Generado (IA)
- **Valor:** Lognormal con una mediana de 5 s y sigma de 0,4 (media de unos 5,4 s) por ración y por persona que sirve. Quien retira varias raciones suma una muestra por ración.
- **Base:** No se puede medir. Hoy la cola se forma antes de la caja y no en el mostrador (S10), así que la capacidad del servicio tiene que superar el ritmo máximo observado en la caja: 168 raciones en 10 minutos (1.008 por hora). Con 2 personas sirviendo, eso pide menos de 7,1 s por ración. Con 5 s de mediana la capacidad es de unas 1.330 raciones por hora: alcanza con 1 puesto de validación (924 por hora) pero no con 2 (1.848 por hora). Es el caso que pide estudiar la cátedra: si se mejora la caja, la cola puede pasar al mostrador. Pendiente de una estimación del referente.
- **Rango de sensibilidad:** 3 a 8 s de mediana
- **En FlexSim:** lognormal2(0, 5, 0.4, stream) por cada ración, en el Resource ServicioComida (S22)
- **Usado en:** modelo · **Estado:** propuesto

### S20 · Capacidad de la cocina

- **Origen:** Estimación del referente
- **Valor:** No es restrictiva: la capacidad de preparación supera ampliamente la demanda.
- **Base:** Relevamiento con el referente del comedor.
- **En FlexSim:** No se modela la cocina: el mostrador siempre tiene bandejas disponibles, y la velocidad del servicio depende solo de quienes sirven (S15, S22).
- **Usado en:** modelo · **Estado:** confirmado

### S21 · Retiro de más de una ración por persona

- **Origen:** Generado (IA)
- **Valor:** Becas Nutrirse Vianda: 80 % retira 1 ración, 15 % retira 2 y 5 % retira 3 (1,25 raciones por persona). Resto de los tipos: 95 % retira 1 y 5 % retira 2 (1,05 por persona).
- **Base:** Una persona puede retirar las raciones de otras si presenta sus DNI. En los datos no se distingue: casi no hay check-ins a menos de 1,5 s del anterior (0,2 %), así que cada DNI se valida por separado y un retiro de 2 raciones se ve igual que 2 personas. Se supone más frecuente en las viandas porque se retiran para llevar. Pendiente de una estimación del referente (frecuencia y máximo de DNI por persona).
- **Rango de sensibilidad:** Viandas de 1,0 a 1,5 raciones por persona; resto de 1,0 a 1,15
- **En FlexSim:** Label raciones asignada en el Source con una Empirical Distribution según el grupo. Multiplica el tiempo de validación (S07) y el de servicio (S15). La tasa de llegadas de personas es la de raciones dividida por la media (S08).
- **Usado en:** modelo · **Estado:** propuesto

### S22 · Personas sirviendo en el mostrador

- **Origen:** Generado (IA)
- **Valor:** 2 en el escenario base. Se prueba con 3 (E5).
- **Base:** Supuesto del grupo, pendiente de confirmar con el referente. Junto con S15 define la capacidad del servicio.
- **Rango de sensibilidad:** 1 a 4 personas
- **En FlexSim:** Resource ServicioComida con Count = 2 (base) o 3 (E5), con una fila única delante
- **Usado en:** modelo · **Estado:** propuesto

### S23 · Espacio de la fila entre la caja y el mostrador

- **Origen:** Estimación del referente
- **Valor:** Pendiente: cuántas personas entran entre la caja y el mostrador.
- **Base:** Relevamiento del layout real. Sirve para ver si una cola en el servicio termina frenando la validación.
- **En FlexSim:** Capacidad máxima de la cola FilaServicio. Si se llena, la caja no deja pasar a nadie más (bloqueo) y la cola vuelve a crecer antes de la caja.
- **Usado en:** modelo · **Estado:** pendiente

## Fuera del alcance

El sistema termina al retirar la bandeja en el mostrador (D02). Estas variables no entran al modelo; se conservan como referencia para mencionarlas en el informe.

- **S14 · Consumo en el salón o para llevar.** Lo que hace la persona después de retirar la bandeja queda fuera del sistema (D02). Propuesta anterior: Becas Nutrirse Vianda 90 % para llevar; resto de los tipos 15 %.
- **S16 · Capacidad de asientos del salón.** El salón queda fuera del sistema (D02). Se puede mencionar como línea de trabajo futura. No se releva.
- **S17 · Tiempo de consumo en el salón.** El salón queda fuera del sistema (D02). Propuesta anterior: lognormal con una mediana de 20 min y sigma de 0,35.
- **S18 · Regla de elección de asiento.** El salón queda fuera del sistema (D02). Propuesta anterior: asiento libre más cercano al mostrador; si no hay, espera de pie.
- **S19 · Velocidad de caminata en el salón.** El salón queda fuera del sistema (D02). Propuesta anterior: 1,2 m/s.

## Decisiones abiertas

### D01 · Cómo compatibilizar la espera de 10 a 15 minutos con el tiempo de servicio real (resuelta)

Con 3,9 s por persona, una cola de 65 se vacía en unos 4 minutos. Para esperar de 10 a 15 minutos haría falta una cola de 150 a 230 personas, o que la gente llegue antes de la apertura.

- A) Las personas llegan antes de las 12:00 y la espera incluye el tiempo hasta la apertura (S09). Se puede comprobar en el modelo.
- B) Los 10 a 15 minutos son una percepción: se toma como objetivo la cola de 60 a 70 personas y se reporta la diferencia.
- C) La cola real en el pico es más larga que 60 a 70 personas.

**Recomendación:** Decidido: la fila se forma antes de que empiece la atención (S09). Se valida contra la curva real de validaciones por franja y contra la espera observada (S10).

### D02 · ¿Dónde termina el sistema? (resuelta (revisada))

Primero se incluyeron el mostrador y el salón (C). Después se recortó hasta la caja (A). La cátedra pidió incluir el servicio de comida: si se mejora la validación, la cola puede pasar al mostrador, y hay que ver si agregar gente en el servicio acelera el proceso completo en lugar de solo mover el cuello de botella.

- A) El sistema termina en la caja (puesto de validación).
- B) Hasta el servicio de comida: fila, caja, fila de servicio y mostrador. El salón queda fuera.
- C) Incluir el mostrador y el salón: dónde se sienta la gente y cuánto tiempo ocupa el asiento.

**Recomendación:** Decidido: B. Sistema = llegadas + fila + caja + fila de servicio + mostrador. El salón y el retiro para llevar (S14, S16 a S19) quedan fuera y se mencionan en el informe.

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

La pregunta de la Entrega 1 incluye el horario límite de reserva, que según D04 no afecta la cola. Con D02 revisada, el sistema llega hasta el mostrador.

- Propuesta: ¿qué combinación de puestos de validación, organización de la fila y personas en el servicio de comida reduce el tiempo total desde la llegada hasta retirar la bandeja en el pico, sin que mejorar la caja solo traslade la cola al mostrador?

**Recomendación:** Ajustar la pregunta y el alcance (sección 4) en la próxima entrega.

### D06 · Caso de estudio: dos filas según el tipo de cliente (abierta)

Con 2 puestos, en lugar de una fila única, cada puesto atiende su propia fila según el tipo de cliente. El tipo es un dato real del registro. Becas Nutrirse Vianda es el 42 % de las retiradas y su check-in mediano es unos 17 minutos más tardío que el de los estudiantes de grado.

- A) Fila de viandas (Becas Nutrirse Vianda) y fila general (el resto). Reparto de 42 % y 58 %.
- B) Fila de estudiantes y fila de becas y personal. Reparto de 49 % y 51 %.
- C) Comparar A y B contra 2 puestos con fila única (E1).

**Recomendación:** Proponer A, que separa el flujo con un patrón de llegada distinto, y compararla contra 2 puestos con fila única (E1): la fila única suele dar menos espera promedio, así que la separación se justifica solo si reduce la espera de algún grupo.
