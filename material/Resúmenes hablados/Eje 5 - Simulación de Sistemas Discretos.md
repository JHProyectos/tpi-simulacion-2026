# Eje 5. Simulación de sistemas discretos

Bueno, vamos con el eje cinco, el de colas. ¿Por qué importa tanto? Porque en el parcial te aparece dos veces: en la teoría, mayormente multiple choice y quizás alguna pregunta de desarrollo, y en la práctica, la tabla de simulación que hacés a mano con calculadora. Esa es la que más pesa.

Lo que el profe sacó: la notación de Kendall, así que no la estudies, y las medidas de desempeño como tema de teoría, porque se evalúan con la práctica. Además, de la teoría salieron todas las fórmulas de cálculo: ahí se evalúan los conceptos, y las cuentas las vas a encontrar solo en la parte de la tabla.

Esto dura unos treinta y tres minutos, y hay cuatro ideas centrales. La primera: las colas se forman por la variabilidad, aunque la capacidad media alcance. La segunda: en la tabla, cada cliente empieza en el mayor valor entre su llegada y el fin del anterior. La tercera: los tiempos de espera se promedian sobre los clientes, y las cantidades en cola y la utilización, en el tiempo. Y la cuarta, la que ata todo: la Ley de Little une esas dos maneras de promediar y sirve para verificar.

En cada tema te marco lo importante, la trampa y, si puede caer de desarrollo, cómo armar la respuesta. Hay cuatro dibujos, pero todo lo que muestran está contado en el texto.

## Por qué existen las colas

Casi todos los sistemas que se estudian con simulación discreta son sistemas de colas: una línea de producción, una guardia, una caja de supermercado. ¿Cuándo aparece una cola? Cuando un recurso compartido tiene que atender más pedidos de los que puede procesar en ese momento.

Y acá el apunte desarma un malentendido. Uno piensa: si la capacidad alcanza en promedio, no debería haber cola. Es falso. Las llegadas y los servicios no están sincronizados: a veces llegan tres juntos, a veces una atención se estira. Esa desincronización es la variabilidad, y es la razón de que existan las colas y de que haga falta simular.

Pensalo como un peaje. Si los autos llegaran como un reloj y cada cobro durara siempre lo mismo, no se juntaría nadie. Pero vienen tres pegados, o uno no encuentra las monedas, y se arma la fila aunque en promedio el cajero dé abasto.

**Lo importante.** La causa de las colas es la variabilidad, no la falta de capacidad media.

**Ojo, trampa.** Si una opción dice que con capacidad media de sobra no se forma cola, es falsa: es justo el malentendido del apunte. Y desconfiá de la que dice que solo hay cola con el servidor al cien por ciento.

**Si te toca de desarrollo.** Definí la cola. Planteá el malentendido de la capacidad media y explicá la variabilidad con un ejemplo. Y cerrá con la idea del apunte: que la atención media sea de tres minutos no significa que cada una dure tres, y esa diferencia es la que genera las colas y obliga a simular.

## Los elementos de un sistema de colas

Son seis.

Primero, la fuente de entrada: la población de donde vienen los clientes. Lo habitual es suponerla infinita. Se toma finita cuando los clientes potenciales son pocos y las llegadas dependen de cuántos ya están adentro. Pensá en un técnico que atiende las cinco máquinas de un taller: si tres ya están rotas, quedan solo dos que se pueden romper.

Segundo, el cliente: la entidad que pide servicio, con atributos como instante de llegada, tipo o prioridad.

Tercero, el patrón de llegadas. Ojo acá: se define por la distribución del tiempo entre llegadas, no por el instante de llegada. Como con el colectivo: no importa a qué hora pasó cada uno, sino cada cuánto pasan. Es la conexión con el eje tres.

Cuarto, la cola, con su capacidad, finita o infinita, y su disciplina. Quinto, el servidor: cuántos hay, si son idénticos y la distribución del tiempo de servicio. Y por último, el proceso de servicio: duración, canales, disponibilidad y si hay estaciones en secuencia.

Abajo lo tenés dibujado. Fijate en dos tramos que vas a usar toda la práctica. El rato en la fila es la espera en cola; promediada sobre los clientes, da Wq. El rato desde que llega hasta que se va, fila más atención, es el tiempo en el sistema; promediado, da W.

![Sistema de colas con fuente de entrada, cola, servidor y salida](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje5-sistema-colas.svg)

*Figura 1. El recorrido de un cliente. Arriba, los tiempos que dan Wq y W; abajo, las cantidades que dan Lq, la utilización y L.*

**Lo importante.** Llegadas y servicios se describen con distribuciones de probabilidad, no con valores fijos.

**Ojo, trampa.** Si te dicen que el patrón de llegadas se modela con el instante de llegada de cada cliente, es falso: es la distribución del tiempo entre llegadas. Y no mezcles fuente finita, que es tener pocos clientes potenciales, con cola de capacidad limitada, que es tener poco lugar para esperar.

## Disciplina de cola

La disciplina decide a quién le toca cuando se libera el servidor: es el «el que sigue» del sistema. No cambia cuánto trabajo hay; cambia quién espera y cuánto. Por eso es una palanca de diseño barata.

Son cinco. La primera, FIFO: primero en llegar, primero atendido, como la fila del banco. Es la más común y la que se percibe como justa; no optimiza nada, pero reparte la espera parejo.

La segunda, LIFO: último en llegar, primero atendido. Como una pila de platos, donde agarrás el de arriba. Aparece en pilas de material. La espera media global no cambia, pero se vuelve muy desigual.

La tercera, la aleatoria: poco usada a propósito, sirve de referencia teórica.

La cuarta, por prioridad: es la de una guardia médica. Mejora al grupo prioritario a costa del resto, y la media global puede incluso empeorar.

Y la quinta, primero el trabajo más corto, como dejar pasar en la caja al que lleva un solo producto. Reduce la espera media del conjunto, pero puede postergar indefinidamente a los largos: el del changuito lleno, si siguen llegando los de un producto, no pasa nunca.

Con prioridad hay que definir algo más. Expropiativa es cuando el prioritario interrumpe el servicio en curso: le saca el lugar al que se estaba atendiendo. No expropiativa es cuando espera a que termine y pasa adelante en la cola. Dan resultados distintos.

**Lo importante.** La disciplina no cambia el trabajo, cambia quién espera. Y cada una tiene su efecto: sabételos de memoria.

**Ojo, trampa.** Dos salen derecho del apunte. «LIFO aumenta la espera media»: falso, la media no cambia. «La prioridad reduce la espera media global»: falso, puede empeorarla. La que baja la media es la del trabajo más corto.

## Configuraciones

Cómo organizás colas y servidores no es un dato del sistema: es una decisión de diseño. Hay cuatro. La primera, una cola y un servidor, el caso de los ejercicios. La segunda, una cola y varios servidores, como un banco con fila única. La tercera, varias colas y varios servidores, como las cajas del súper. Y la cuarta, servidores en serie, como una línea de producción.

Con la misma cantidad de servidores, una cola única suele dar mejor resultado que las filas separadas. ¿Por qué? Porque comparte la capacidad. Con filas separadas puede pasar que una caja se quede sin nadie mientras en la de al lado hay gente esperando. Con fila única, nunca: el primero de la fila va al servidor que se libere. Y no cuesta plata, solo reorganización.

**Lo importante.** A igual cantidad de servidores, la cola única le gana a las filas separadas porque comparte la capacidad.

**Ojo, trampa.** Las opciones suelen tener bien la conclusión y mal el motivo: no gana porque atienda más rápido ni porque tenga más servidores. Cuidado con el absoluto: el apunte dice «suele». Y no confundas el banco, que es una cola con varios servidores, con el súper, que son varias colas.

**Si te toca de desarrollo.** Nombrá las cuatro configuraciones con su ejemplo. Planteá la comparación entre fila única y filas separadas. Explicá el mecanismo: el servidor libre mientras hay gente esperando en otra fila. Y cerrá con que es una mejora sin agregar recursos, igual que elegir la disciplina.

## Dos maneras de promediar

Prestá atención, porque el apunte lo marca como el concepto más importante del eje y el que más se confunde. Las medidas de desempeño con sus cuentas no entran como teoría: las ves en la práctica. Lo que sí entra es esta idea. Wq, la espera promedio en cola, y Lq, la cantidad promedio en cola, suenan los dos a «el promedio de la cola», pero no son lo mismo.

Por un lado, Wq y W, que es el tiempo promedio en el sistema, son promedios por entidad: miran cuánto estuvo cada cliente y promedian sobre los clientes. Es como preguntarle a cada uno, a la salida, cuánto esperó. Da minutos.

Por el otro, Lq, L, que es la cantidad promedio en el sistema, y la utilización son promedios en el tiempo: miran cuántos clientes había y promedian a lo largo de la corrida. Es como una cámara que filma la cola toda la corrida: cada cantidad pesa según cuánto tiempo estuvo en pantalla. Da clientes.

¿Y por qué no sirve promediar unas fotos de la cola en instantes elegidos? Porque una foto no sabe cuánto duró lo que muestra: le daría el mismo peso a dos clientes durante medio minuto que a uno durante ocho minutos.

¿Cómo se leen? Wq igual a un minuto: un cliente cualquiera esperó, en promedio, un minuto. Lq igual a cero coma cuatro: si mirás la cola en un momento al azar, encontrás en promedio cero coma cuatro personas. Lo primero le interesa al cliente; lo segundo, a quien dimensiona la sala de espera. Abajo tenés las dos maneras lado a lado.

![Comparación entre promediar sobre los clientes y promediar en el tiempo](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje5-dos-promedios.svg)

*Figura 2. Las dos maneras de promediar: sobre los clientes, en minutos, y en el tiempo, en clientes.*

**Lo importante.** Dos preguntas, dos maneras de promediar: sobre los clientes o a lo largo del tiempo. Y la utilización va con Lq y L.

**Ojo, trampa.** La trampa número uno del eje son los pares cruzados: «Lq es un promedio sobre los clientes», «Wq es un promedio en el tiempo», «la utilización es un promedio por entidad». Todas falsas. También «Lq se obtiene promediando la cola en los instantes de llegada», que el apunte descarta. Y mirá las unidades: Lq en minutos o Wq en clientes es un error.

**Si te toca de desarrollo.** Decí que hay dos tipos de promedio y por qué se confunden. Explicá Wq y W, por entidad, en minutos. Después Lq, L y la utilización, como promedios en el tiempo de una función escalonada, donde cada valor pesa según cuánto duró, en clientes. Mostrá por qué no se muestrean instantes. Y cerrá con la lectura de cada uno.

## Las tres funciones escalonadas

Para promediar en el tiempo, cada cantidad es una función escalonada que cambia a lo largo de la corrida. Hay tres, y conviene no mezclarlas.

La primera, B de t, vale uno si el servidor está ocupado y cero si está libre, como el cartel de ocupado de un probador. De ella sale la utilización.

La segunda, Q de t, cuenta los que esperan en la fila: sube cuando llega alguien que tiene que esperar y baja cuando uno pasa a ser atendido. De ella sale Lq.

Y la tercera, N de t, cuenta los que están en el sistema, o sea, los que esperan más el que se atiende. De ella sale L.

Fijate que eso último vale en todo instante: contás las cabezas de la fila, le sumás la del mostrador, y tenés a todos los de adentro. Y como vale instante a instante, vale también para los promedios.

Esto ahorra trabajo, porque no hace falta dibujar N de t. Y sirve de control: si medís las tres áreas y la suma no cierra, hay un error en algún gráfico. La cuenta la hacés en la práctica, en el paso cuatro.

**Lo importante.** Las tres funciones y su relación: en el sistema están los que esperan más el que se atiende, en todo instante y, por eso, también en promedio.

**Ojo, trampa.** Q de t no sube con cada llegada, solo con las que tienen que esperar: si el servidor está libre, el que llega pasa derecho. Y baja cuando alguien pasa al servidor, no cuando se va.

## Ley de Little

Arrancamos por una observación del apunte: el área bajo Q de t coincide exactamente con la suma de las esperas, y el área bajo N de t, con la suma de las permanencias. ¿Casualidad? No.

Imaginate que cada cliente, mientras espera, apoya sobre el gráfico una tira de altura uno, tan larga como su espera. El área bajo Q de t son esas tiras apiladas. La podés medir cliente por cliente o barriendo el tiempo de izquierda a derecha: es la misma superficie. Eso sí, el apunte lo plantea con el sistema vacío al principio y al final, así cada cliente aporta justo el tiempo que estuvo presente.

De ahí sale la Ley de Little, que une las dos maneras de promediar: relaciona la cantidad promedio de clientes, que es un promedio en el tiempo, con el tiempo promedio de permanencia, que es un promedio sobre los clientes, a través de la tasa de llegada. La intuición: si entra mucha gente por minuto y cada uno se queda mucho, adentro hay mucha gente. La cuenta la hacés en la práctica, en el paso cinco.

Y es muy general: no supone ninguna distribución, disciplina ni cantidad de servidores. Vale para cualquier sistema estable.

Ahora, la advertencia metodológica. Para que sea una verificación de verdad, los dos lados tienen que salir por caminos independientes: uno promediando esperas sobre los clientes y el otro sumando rectángulos bajo la curva. Si sacás Lq dividiendo la suma de esperas por el tiempo total simulado, la igualdad se cumple siempre por álgebra y no comprueba nada. Es como pesarte dos veces en la misma balanza para ver si la balanza anda.

¿Y para qué sirve? En el eje cuatro se dijo que verificar es comprobar que el modelo está bien construido. Little es la primera técnica concreta: si los indicadores no la cumplen, hay un error en el modelo o en la forma de recolectar los estadísticos.

**Lo importante.** Qué relaciona, lo general que es y su uso para verificar.

**Ojo, trampa.** «Solo vale con un servidor», «requiere llegadas exponenciales», «solo con FIFO»: todo falso, le agregan a la ley un supuesto que no tiene. Es verificación, no validación: no compara el modelo con el sistema real. Y la igualdad entre área y suma de esperas el apunte la explica para un sistema que arranca y termina vacío.

**Si te toca de desarrollo.** Decí en palabras qué relaciona: la cantidad promedio en el sistema, la tasa de llegada y el tiempo promedio de permanencia. Explicá de dónde sale: con el sistema vacío al principio y al final, el área es la suma de los tiempos de cada cliente. Remarcá su generalidad. Presentala como la primera técnica de verificación. Y cerrá con la advertencia de los caminos independientes.

## La práctica: la tabla paso a paso

Acá está el corazón del eje. Los tres ejercicios del práctico piden lo mismo, y el tres tiene el formato y el puntaje del ejercicio de colas del parcial. Acá sí van las medidas de desempeño con sus cuentas, porque el profe las evalúa con este ejercicio. Va la receta.

### Antes de arrancar

Leé bien el enunciado: un dato es el instante de llegada y el otro es la duración de la atención, no el instante en que termina. Es la diferencia entre «el turno es a las diez» y «el turno dura diez minutos». El apunte dice que confundirlos es el error más frecuente, y te arruina toda la tabla.

### Paso uno: la tabla

Para cada cliente, en orden, cuatro columnas. Primero, el inicio: el mayor valor entre su llegada y el fin del anterior. Pensalo como la puerta de un consultorio: para entrar tienen que pasar dos cosas, que llegues vos y que salga el anterior. Lo que pase último manda.

Después, el fin: inicio más duración. Tercero, la espera, su Wq: inicio menos llegada. Y por último, la permanencia, su W: fin menos llegada.

Al final sumás duraciones, esperas y permanencias. Control rápido: la suma de permanencias es la suma de esperas más la de duraciones.

**Ojo, trampa.** El empate. Si un cliente llega justo cuando termina el anterior, empieza en ese instante y su espera es cero. La convención de la cátedra, que viene del eje cuatro, es procesar primero el fin de servicio y después la llegada, así el recurso ya está libre. Como en el ascensor: primero bajan, después suben. En la tabla sale solo, por la regla del máximo; donde te puede pisar es al contar la cola.

### Paso dos: el horizonte

T es el instante en que se retira el último cliente, o sea, el fin del último servicio. Es la hora de bajar la persiana: cuando se va el último, no cuando llega.

**Ojo, trampa.** T no es la última llegada ni la suma de duraciones. En el ejercicio uno las dos dan veinte, pero T es veinticinco. Con veinte, la utilización te daría uno, y eso tiene que hacerte ruido.

### Paso tres: los indicadores

Son siete. Wq: suma de esperas dividida por la cantidad de clientes. W: suma de permanencias dividida por la cantidad de clientes. Utilización: suma de duraciones dividida por T. Tiempo ocioso: T menos la suma de duraciones. Lambda, la tasa de llegada: clientes dividido T. Proporción que espera: clientes con espera mayor que cero, dividido el total. Y la cola máxima: la mayor cantidad de gente esperando a la vez.

**Ojo, trampa.** Acá todo gira alrededor del divisor.

La primera: Wq y W van por clientes; la utilización, lambda, Lq y L, por T. En el ejercicio uno, si dividís el área de la cola por los ocho clientes en vez de por los veinticinco minutos, te da dos, que es justo Wq. Ese número va a estar de distractor.

La segunda: lambda va en clientes por minuto, no al revés.

La tercera: la cola máxima es un pico, como la temperatura máxima del día; Lq es un promedio.

Y la cuarta: el que llega justo cuando el otro termina no cuenta entre los que esperaron.

### Paso cuatro: gráficos y áreas

Tres gráficos sobre el mismo eje de tiempo: las llegadas como marcas, B de t como bloques entre cero y uno, y Q de t como escalones.

Para el área de Q armás la tabla de tramos. Cortás el tiempo en cada llegada, inicio y fin. En cada tramo multiplicás cuántos había en cola por cuánto duró, y sumás todo. Lq es esa área dividida por T. La utilización sale del área de B. Y L es Lq más la utilización.

**Ojo, trampa.** Tres cosas.

La primera: el área de Q te va a coincidir con la suma de esperas, y es un buen control. Pero si te piden Lq por área y vos dividís la suma de esperas por T, no hiciste lo pedido y Little queda circular.

La segunda: el empate al contar la cola. En el ejercicio dos, en el minuto veintidós termina el cliente cinco, entra el seis y llega el ocho. Con el fin primero, la cola queda en dos. Si procesás primero la llegada, por un instante contás tres, y la cola máxima te sale mal. Al área no le cambia nada; al máximo, sí.

Y la tercera: L es Lq más la utilización, no Lq más uno, porque no siempre hay alguien en servicio.

### Paso cinco: verificar con Little

Comparás Lq por área contra lambda por Wq, y L contra lambda por W.

**Ojo, trampa.** Se multiplica, no se divide. Y usá lambda como fracción. En el ejercicio dos es ocho treintavos; si lo redondeás a cero coma veintisiete y multiplicás por tres, te da cero coma ochenta y uno, y parece que no cierra.

## Los ejercicios del práctico

### Ejercicio uno: mesa de entradas

Los datos. Llegadas: cero, siete, ocho, nueve, once, catorce, quince y veinte. Duraciones: dos, tres, dos, dos, dos, dos, cinco y dos.

La tabla. Inicios: cero, siete, diez, doce, catorce, dieciséis, dieciocho y veintitrés. Esperas: cero, cero, dos, tres, tres, dos, tres y tres, que suman dieciséis. Las permanencias suman treinta y seis.

Abajo tenés la corrida dibujada, un renglón por cliente. Mirá al tres: llega en el ocho, pero el dos termina en el diez, así que empieza en el diez y espera dos. Desde ahí, cada uno arranca cuando termina el anterior.

![Barras en el tiempo del ejercicio uno, con la espera y la atención de cada cliente](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje5-ej1-gantt.svg)

*Figura 3. Ejercicio uno, un renglón por cliente: en naranja la espera, en azul la atención.*

Los resultados. T, veinticinco. Wq, dos minutos; W, cuatro coma cinco. Utilización, veinte dividido veinticinco, cero coma ocho; ocioso, cinco minutos. Lambda, cero coma treinta y dos. Esperan seis de ocho. Cola máxima, dos. Lq, cero coma sesenta y cuatro; L, uno coma cuarenta y cuatro. Little cierra.

Y abajo, los tres gráficos de la consigna. B de t está en cero solo entre el dos y el siete, los cinco minutos ociosos, y su área da veinte. El área de Q de t, sumando rectángulos, da dieciséis, igual que la suma de esperas: dividida por veinticinco, da el cero coma sesenta y cuatro.

![Llegadas, ocupación del servidor y cola en el tiempo del ejercicio uno](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje5-ej1-funciones.svg)

*Figura 4. Ejercicio uno: llegadas, servidor ocupado y cola, sobre el mismo eje de tiempo.*

### Ejercicio dos: farmacia de turno

Los datos. Llegadas: cero, uno, cinco, trece, catorce, dieciséis, dieciocho y veintidós. Duraciones: tres, dos, dos, cuatro, cinco, tres, tres y dos.

La tabla. Inicios: cero, tres, cinco, trece, diecisiete, veintidós, veinticinco y veintiocho. Esperas: cero, dos, cero, cero, tres, seis, siete y seis, que suman veinticuatro. Las permanencias suman cuarenta y ocho.

Los resultados. T, treinta. Wq, tres minutos; W, seis. Utilización, veinticuatro dividido treinta, cero coma ocho; ocioso, seis minutos. Lambda, ocho treintavos. Esperan cinco de ocho. Cola máxima, dos. Lq, cero coma ocho; L, uno coma seis.

### Ejercicio dos, consigna efe

¿Qué pasa si cada atención dura un minuto menos? Quedan dos, uno, uno, tres, cuatro, dos, dos y uno. T baja a veinticinco. La suma de esperas, de veinticuatro a trece. Wq, de tres a más o menos uno coma seis. Y la utilización, de cero coma ocho a cero coma sesenta y cuatro. A mí Lq me dio cero coma cincuenta y dos.

El tiempo de atención bajó un tercio y la espera, casi a la mitad. Como T cambió, compará indicadores, no áreas en bruto. Lo calculé yo con la misma regla; revisalo con tu hoja.

### Ejercicio tres: formato parcial

Los datos. Llegadas: cero, cinco, siete, ocho, dieciséis, diecisiete, dieciocho y veintidós. Duraciones: tres, dos, tres, tres, tres, dos, dos y dos.

La tabla. Inicios: cero, cinco, siete, diez, dieciséis, diecinueve, veintiuno y veintitrés. Esperas: cero, cero, cero, dos, cero, dos, tres y uno, que suman ocho. Las permanencias suman veintiocho.

Los resultados. T, veinticinco. Wq, un minuto; W, tres coma cinco. Utilización, cero coma ocho; ocioso, cinco minutos. Lambda, cero coma treinta y dos. Esperan cuatro de ocho. Cola máxima, dos. Lq, cero coma treinta y dos; L, uno coma doce. Little cierra.

Ojo con el visitante tres: llega en el siete, justo cuando termina el dos, así que no espera. Lo calculé yo; revisalo con tu hoja.

La consigna e: el jefe dice que, con el operador ocupado el ochenta por ciento, el puesto está bien dimensionado. ¿Qué le contestás? Que la utilización sola no alcanza. La mitad de los visitantes esperó, hubo dos en cola, y las esperas aparecen cuando llegan varios juntos: es la variabilidad.

Y el argumento más fuerte está en el propio práctico: los tres ejercicios tienen utilización cero coma ocho, y Wq da dos, tres y un minuto. Mismo número, tres esperas distintas. Sumale que una sola corrida con ocho visitantes es poca evidencia, y que si un minuto de espera es aceptable depende de un criterio de servicio que el enunciado no da.

## Preguntas tipo multiple choice

Pregunta uno. ¿Qué es correcto sobre Wq y Lq? La a: los dos son promedios en el tiempo. La b: Wq es un promedio sobre los clientes, en minutos, y Lq un promedio en el tiempo, en clientes. La c: Lq se obtiene promediando el largo de la cola en algunos instantes. La d: miden lo mismo con distinta unidad. ¿Cuál va? La b. ¿Y la tramposa? La c, que suena lógica, pero el apunte la descarta porque no pondera cuánto duró cada valor.

Pregunta dos. La utilización del servidor es... La a: un promedio por entidad, como Wq. La b: un promedio en el tiempo, como Lq y L. La c: la suma de duraciones dividida por la cantidad de clientes. La d: la proporción de clientes que no esperaron. Va la b, porque mira cuánto tiempo estuvo ocupado el servidor a lo largo de la corrida. La tramposa es la a, porque se arma con la duración de cada cliente.

Pregunta tres. La Ley de Little... La a: solo vale con un servidor. La b: requiere llegadas exponenciales. La c: vale para cualquier sistema estable, sin suponer distribución, disciplina ni cantidad de servidores. La d: solo vale con FIFO. Va la c. Las otras tres le agregan a la ley un supuesto que no tiene.

Pregunta cuatro. Según el apunte, comprobar Little en un modelo sirve para... La a: validarlo contra el sistema real. La b: verificar que está bien construido. La c: estimar la distribución de llegadas. La d: elegir la disciplina. Va la b. La tramposa es la a, porque verificar no es validar.

Pregunta cinco. Un alumno calcula Lq dividiendo la suma de esperas por T, y después comprueba que da igual a lambda por Wq. ¿Qué pasa? La a: es una verificación válida y más rápida. La b: la igualdad se cumple siempre por álgebra y no comprueba nada. La c: Little no se va a cumplir. La d: Lq da distinto que por área. Va la b: es la advertencia metodológica. La tramposa es la a, porque el número está bien, pero la comprobación es circular. Es pesarte dos veces en la misma balanza.

Pregunta seis. Sobre las disciplinas, ¿cuál es correcta? La a: LIFO aumenta la espera media. La b: la prioridad reduce siempre la espera media global. La c: primero el trabajo más corto reduce la espera media, pero puede postergar indefinidamente a los largos. La d: cambiar la disciplina reduce el trabajo del servidor. Va la c. La a y la b son las dos trampas del apunte: LIFO no cambia la media, y la prioridad puede empeorarla.

Pregunta siete. Con los mismos servidores, una cola única frente a una fila por servidor... La a: es peor, porque el cliente no elige. La b: suele ser mejor, porque nunca queda un servidor ocioso con gente esperando en otra fila. La c: es mejor porque atiende más rápido. La d: da igual. Va la b. La tramposa es la c: conclusión bien, motivo mal.

Pregunta ocho. Un recurso tiene, en promedio, capacidad suficiente para la demanda. Según el apunte... La a: no se forma cola, porque la capacidad media alcanza. La b: se forma cola igual, porque las llegadas y los servicios no están sincronizados. La c: solo se forma cola si el servidor está al cien por ciento. La d: que haya cola depende solo de la disciplina. Va la b: la causa es la variabilidad. La tramposa es la a, que es justo el malentendido que el apunte desarma. Acordate del peaje.

Pregunta nueve. Para modelar el patrón de llegadas hay que definir... La a: el instante de llegada de cada cliente. La b: la distribución del tiempo entre llegadas. La c: la capacidad de la cola. La d: la cantidad de servidores. Va la b, que es la conexión con el eje tres. La tramposa es la a: lo que se modela es cada cuánto llegan, no a qué hora llegó cada uno.

Pregunta diez. En un modelo con prioridad, la prioridad es expropiativa cuando... La a: el prioritario interrumpe el servicio en curso. La b: el prioritario espera a que termine el servicio actual y pasa adelante en la cola. La c: se atiende primero el trabajo más corto. La d: da lo mismo, porque las dos variantes dan iguales resultados. Va la a. La tramposa es la b, que es la no expropiativa. Y la d es falsa: el apunte dice que son sistemas distintos y dan resultados distintos.

Pregunta once. La cantidad de clientes en cola, Q de t... La a: sube con cada llegada. La b: sube cuando llega alguien que tiene que esperar y baja cuando uno pasa a ser atendido. La c: baja cuando un cliente se va del sistema. La d: es un número fijo para toda la corrida. Va la b. Acá hay dos tramposas, la a y la c: si el servidor está libre, el que llega no pasa por la fila, y la fila baja cuando alguien pasa al servidor, no cuando se va. La d tampoco: el apunte dice que la cola no es un número, sino una función escalonada que cambia a lo largo de la corrida.

## Lo que puede entrar en desarrollo

Si tuviera que apostar, van en este orden.

Primero, promediar por entidad contra promediar en el tiempo: Wq y W sobre los clientes, en minutos; Lq, L y la utilización a lo largo del tiempo, en clientes; por qué no sirve muestrear instantes; y que en el sistema están los que esperan más el que se atiende.

Segundo, la Ley de Little: qué relaciona, de dónde sale, lo general que es, su uso como primera técnica de verificación y la advertencia de los dos caminos independientes.

Tercero, por qué un recurso con utilización razonable puede tener colas, que es la consigna e del ejercicio tres con otro nombre: la variabilidad como causa; el dato del práctico, misma utilización con Wq de dos, tres y un minuto; y qué mirar en cambio.

Y cuarto, las decisiones de diseño baratas: la cola única contra las filas separadas, con su motivo, y la disciplina, que no cambia el trabajo pero sí quién espera.

## Lo mínimo que te tenés que llevar

Quedate con estas seis.

Uno: las colas aparecen por la variabilidad, aunque la capacidad media alcance. Por eso se simula.

Dos: en la tabla, instante no es duración. Cada cliente empieza en el mayor valor entre su llegada y el fin del anterior. Y ante un empate va primero el fin de servicio: primero bajan, después suben.

Tres: en la tabla, Wq y W se dividen por la cantidad de clientes. Lq, L, la utilización y lambda se dividen por T, que es cuando se va el último.

Cuatro: en la tabla, L es Lq más la utilización.

Cinco: Little, que en la tabla comprobás con L igual a lambda por W, vale para cualquier sistema estable, y verifica de verdad solo con dos caminos independientes.

Seis: la cola única le gana a varias filas con los mismos servidores. Y la utilización sola no dice si un sistema está bien dimensionado.

Eso es el eje cinco. Mañana, en la tabla, despacio y con la regla del máximo. Suerte.
