# Locución nueva para estirar el video

[TOC]

Tres escenas que hoy no están en el video y que el informe ya tiene resueltas. No hay que inventar ningún dato: todo sale de `entregas/entrega-final/INFORME.md`, secciones 7.1, 7.3 y 9.

Son **3:30 de locución**, todas con voz de Jonatan. Con esto los tres films pasan de 7:19 a 10:49, y con los tramos de captura de FlexSim el video pasa los 12 minutos.

| Escena nueva | Va en | Dura | Film queda en |
|---|---|---|---|
| Bondad de ajuste de las llegadas | Parte A, después de la ficha | 1:15 | 3:46 |
| Las distribuciones del modelo | Parte B, antes de la corrida | 0:50 | 2:51 |
| Verificación, validación y réplicas | Parte B, al final | 1:25 | — |

Ninguno de los dos films se acerca al tope de 300 s.

## Por qué estas tres y no otras

Son las tres cosas que una cátedra de Simulación busca en un TPI y que el video hoy no muestra: que probaste las distribuciones de entrada en vez de suponerlas, que separás verificación de validación, y que justificás el número de réplicas. El video actual muestra los resultados pero no el método, y el método es la mitad de la nota.

La primera además tiene algo que queda muy bien contado: **la prueba da que no**, y el modelo cambió por eso.

---

## Escena 1 · Bondad de ajuste de las llegadas

Va en la **Parte A**, después de la ficha del escenario base. En pantalla: la tabla de las seis franjas, y la fila de las 14:00 destacada cuando la nombrás.

> Antes de modelar las llegadas probamos si se podían representar con una sola distribución teórica para todo el turno. Tomamos una muestra de mil ciento setenta y seis raciones de un día de servicio, la agrupamos en seis franjas de media hora y le aplicamos una prueba de chi-cuadrado, con un nivel de significación del cinco por ciento.
>
> El resultado fue un chi-cuadrado calculado de trescientos cinco con nueve, contra un valor crítico de nueve con cuarenta y ocho, para cuatro grados de libertad. Se rechaza la hipótesis nula.
>
> La franja que más pesa es la de las dos de la tarde: llegaron ciento sesenta y cinco personas donde la distribución teórica esperaba cincuenta y tres. Es una demanda tardía que el supuesto no contemplaba.
>
> Así que la prueba nos dijo que no, y el modelo cambió por eso. En lugar de una tasa única para todo el turno, usamos una tasa distinta para cada franja de diez minutos y para cada grupo de clientes, sacada de los registros. Dentro de cada franja las llegadas son de Poisson. Es decir, el modelo trabaja con un proceso de Poisson no homogéneo, cuya tasa sigue la forma real del día.

---

## Escena 2 · Las distribuciones del modelo

Va en la **Parte B**, antes de la corrida del escenario base. En pantalla: la tabla de variables, un renglón por vez.

> Estas son las variables aleatorias del modelo y de dónde sale cada una.
>
> El tiempo de validación por DNI es una lognormal, con una mediana de tres coma treinta y cuatro segundos y una media de tres coma setenta y siete. Sale de los registros del puesto.
>
> La demora de la apertura no la supusimos: se sortea entre las demoras reales de los treinta y dos días que tenemos registrados, con una media de casi dos minutos y un máximo de siete y medio.
>
> Las raciones por persona salen de la composición de las becas: los de vianda retiran una, dos o tres; el resto, casi siempre una.
>
> Y la cola previa a la apertura está calibrada, no medida. Es el supuesto que declaramos.

---

## Escena 3 · Verificación, validación y réplicas

Va en la **Parte B**, al final, antes de pasar a los escenarios alternativos. En pantalla: dos columnas, verificación a la izquierda y validación a la derecha, y al final la placa de las 30 réplicas.

> Antes de usar el modelo para decidir algo hay que probar dos cosas distintas.
>
> La primera es la verificación: ¿el modelo hace lo que nosotros diseñamos? Revisamos que los tiempos de cada persona fueran en orden, llegada, validación, servicio y salida; que la cantidad de personas del día diera dentro de lo esperado, mil trescientas sesenta y nueve contra mil trescientas ochenta y una; y que al final no quedara nadie en ninguna fila.
>
> La segunda es la validación: ¿el modelo se parece al comedor real? Ahí comparamos cuatro cosas contra los registros. La curva de raciones por franja, con una correlación de cero coma noventa y cinco. El total del día, que difiere un uno y medio por ciento. La cola máxima en la caja, sesenta y seis personas contra las sesenta a setenta que se observan. Y la espera de los que llegan antes de abrir, trece minutos contra los diez a quince reales.
>
> Una aclaración sobre cómo lo corrimos. Es una simulación terminante: cada réplica es un día completo, que arranca vacío a las once y cuarenta y termina a las cuatro de la tarde. Por eso no hay período de calentamiento. El comedor vacío antes de la cola es parte del sistema real, no un transitorio que haya que descartar. Y corrimos treinta réplicas de cada escenario, que es lo que nos permite dar los intervalos de confianza al noventa y cinco por ciento.

---

## Antes de grabar

- **Leelas en voz alta cronometrando.** Están calculadas a 2,6 palabras por segundo, que es el ritmo al que hablás en los audios que ya grabaste. Si te sale más lento, las escenas se estiran y no pasa nada.
- **Grabá cada escena en un archivo aparte**, con el mismo micrófono y en el mismo lugar que las otras, y dejá tres segundos de silencio al principio y al final. Guardalas como `jonatan/jonatan-e10-ajuste.wav`, `jonatan-e11-distribuciones.wav` y `jonatan-e12-verificacion.wav`.
- Si te trabás, **repetí la oración entera** en vez de retomar a mitad: así el corte queda limpio.

## Un pendiente del informe

La sección 7.1 tiene una nota del propio informe que todavía no está resuelta: **de dónde sale la probabilidad teórica de cada franja** y **qué día es la muestra de 1.176 raciones**. Si lo decís en el video, es la primera pregunta que te van a hacer. Conviene cerrarlo antes de grabar esta escena.
