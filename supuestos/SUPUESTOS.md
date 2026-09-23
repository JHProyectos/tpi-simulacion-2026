# Registro de supuestos y fuentes de datos

> Generado desde `supuestos/supuestos.json` (v0.1, 2026-09-23). No editar a mano: modificar el JSON y correr `python analisis/render_supuestos.py`.

## Orígenes

- **Registro de la organización** (`registro`, 1): Registros de la organización: dataset de reservas del comedor (data/real/TP-SIM - ds_app.csv), sin modificar.
- **Derivado de registros** (`derivado`, 5): Calculado por el grupo a partir de los registros de la organización, con un script reproducible en analisis/.
- **Estimación del referente** (`referente`, 4): Estimación de un referente que conoce el proceso (integrante del grupo que trabaja en el comedor).
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
| S07 | Tiempo de validación por persona | Derivado de registros | Lognormal con mu = 1,205 y sigma = 0,494: mediana 3,3 s y media 3,8 s. En la muestra, la mediana es 2,9 s, el percentil 5 es 1,9 s y el percentil 95 es 9,7 s. | confirmado |
| S08 | Tasa de llegadas a la fila por franja de 10 minutos | Derivado de registros | Valor inicial: validaciones promedio por franja y por grupo (reporte/datos.json, campo por_franja), escaladas a la demanda del perfil (S03). Después se calibra (S09, D01). | propuesto |
| S09 | Cola formada antes de la apertura | Generado (IA) | Llegadas uniformes entre las 11:40 y las 12:00. Cantidad inicial: 65 personas en el perfil pico y 30 en el perfil bajo. | propuesto |
| S10 | Objetivo de validación del modelo (cola y espera observadas) | Estimación del referente | Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico. | a revisar |
| S11 | Ausentismo (reservas no retiradas) | Generado (IA) | Estudiantes 10 %, Becas Nutrirse 5 %, Becas personal 6 %, Personal 8 % sobre el total de reservas no canceladas. | propuesto |
| S12 | Cancelaciones definitivas | Generado (IA) | 3 % del total de reservas. | propuesto |
| S13 | Menú vegetariano / no vegetariano | Generado (IA) | 12 % vegetariano, igual para todos los grupos. Independiente de sin TACC, que es un dato real. | propuesto |
| S14 | Consumo en el salón o para llevar | Generado (IA) | Becas Nutrirse Vianda: 100 % para llevar. Resto de los tipos: 15 % para llevar. | propuesto |
| S15 | Tiempo de entrega en el mostrador | Generado (IA) | Lognormal con una mediana de 2,5 s y sigma de 0,4 por línea (vegetariana y no vegetariana). | propuesto |

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
- **En FlexSim:** Parámetro de escenario (ver D04)
- **Usado en:** dataset, modelo · **Estado:** confirmado

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
- **Base:** Estimación del referente: una cola de 60 a 70 personas en el pico. En los datos reales, la primera franja (12:00 a 12:10) valida una mediana de 92 personas, cerca de la capacidad del puesto: eso indica que ya hay cola al abrir.
- **Rango de sensibilidad:** 30 a 150 personas
- **En FlexSim:** Source adicional en el período previo; el Resource habilita la atención a las 12:00
- **Usado en:** modelo · **Estado:** propuesto

### S10 · Objetivo de validación del modelo (cola y espera observadas)

- **Origen:** Estimación del referente
- **Valor:** Cola de 60 a 70 personas antes del puesto; espera estimada de 10 a 15 minutos en el pico.
- **Base:** Observación directa del referente en un día normal.
- **En FlexSim:** Se compara contra la longitud máxima de la cola y la espera promedio en el pico
- **Nota:** No es compatible con el tiempo de servicio real (ver D01): con 3,9 s por persona, una cola de 65 se vacía en unos 4 minutos.
- **Usado en:** validacion · **Estado:** a revisar

### S11 · Ausentismo (reservas no retiradas)

- **Origen:** Generado (IA)
- **Valor:** Estudiantes 10 %, Becas Nutrirse 5 %, Becas personal 6 %, Personal 8 % sobre el total de reservas no canceladas.
- **Base:** El export real solo trae reservas retiradas (status = used), así que no hay dato. Se supone un valor mayor para estudiantes porque la reserva no tiene penalidad por no asistir, y menor para las becas porque el beneficio está asociado a la persona. Pendiente de pedirle una estimación al referente.
- **Rango de sensibilidad:** 3 % a 15 %
- **Cómo se genera:** Filas nuevas con status = no_show. La cantidad por día y grupo es retiradas × p / (1 − p). reserved_at se muestrea de las reservas reales del mismo día y grupo. checked_at queda vacío.
- **En FlexSim:** No entran a la fila: se descuentan de las reservas. Salida: reservas no utilizadas.
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
- **En FlexSim:** Label menu, usada para la línea del mostrador (si entra en el alcance, D02)
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S14 · Consumo en el salón o para llevar

- **Origen:** Generado (IA)
- **Valor:** Becas Nutrirse Vianda: 100 % para llevar. Resto de los tipos: 15 % para llevar.
- **Base:** Vianda es comida para llevar por definición del beneficio. Para el resto, supuesto del grupo, pendiente de una estimación del referente.
- **Rango de sensibilidad:** 5 % a 30 % en el resto
- **Cómo se genera:** Atributo para_llevar_gen asignado a cada reserva retirada.
- **En FlexSim:** Label para_llevar, que decide si la persona sale o va a una mesa (si entra en el alcance, D02)
- **Usado en:** dataset, modelo · **Estado:** propuesto

### S15 · Tiempo de entrega en el mostrador

- **Origen:** Generado (IA)
- **Valor:** Lognormal con una mediana de 2,5 s y sigma de 0,4 por línea (vegetariana y no vegetariana).
- **Base:** No se va a medir. La cola observada se forma antes de la validación y no en el mostrador, así que el mostrador tiene que atender al menos al ritmo del puesto (3,9 s). Se elige un valor apenas menor.
- **En FlexSim:** Delay en cada línea del mostrador (si entra en el alcance, D02)
- **Usado en:** modelo · **Estado:** propuesto

## Decisiones abiertas

### D01 · Cómo compatibilizar la espera de 10 a 15 minutos con el tiempo de servicio real (abierta)

Con 3,9 s por persona, una cola de 65 se vacía en unos 4 minutos. Para esperar de 10 a 15 minutos haría falta una cola de 150 a 230 personas, o que la gente llegue antes de la apertura.

- A) Las personas llegan antes de las 12:00 y la espera incluye el tiempo hasta la apertura (S09). Se puede comprobar en el modelo.
- B) Los 10 a 15 minutos son una percepción: se toma como objetivo la cola de 60 a 70 personas y se reporta la diferencia.
- C) La cola real en el pico es más larga que 60 a 70 personas.

**Recomendación:** A combinada con B: modelar la llegada previa a la apertura y validar contra la curva real de validaciones por franja, que es el dato más fuerte. La espera de 10 a 15 minutos se reporta como observación del referente.

### D02 · ¿El mostrador de entrega entra en el alcance? (abierta)

La sección 4 de la Entrega 1 termina el sistema en la validación, pero las secciones 5, 8 y 9 hablan del mostrador y de su ocupación.

- A) El sistema termina en la validación. El mostrador y las mesas quedan solo en la animación 3D.
- B) Incluir el mostrador con dos líneas (S13, S15).

**Recomendación:** A, porque la cola y la pregunta de estudio están en la validación. Menú y para llevar se generan igual (cuestan poco) y quedan como labels en la animación.

### D03 · Perfiles de demanda a simular (abierta)

- Perfil bajo: 723 por día (julio)
- Perfil pico: 1.543 por día (agosto)

**Recomendación:** Correr los dos. El pico es el caso que responde la pregunta de estudio.

### D04 · Escenario del horario límite de reserva (abierta)

En los datos reales, la hora de reserva casi no predice la hora de llegada (correlación de 0,13). Quien reserva a las 8:00 valida en una mediana de 13:02, y quien reserva después de las 10 valida en una mediana de 13:17.

- A) Modelarlo como un cambio en la cantidad de reservas del día, no en la hora de llegada.
- B) Sacarlo de los escenarios y justificarlo con este dato.

**Recomendación:** A, con un supuesto explícito sobre cuánta demanda se gana o se pierde al mover el corte.
