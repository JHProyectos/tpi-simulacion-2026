# Eje 5. Simulación de sistemas discretos

Bueno, vamos con el eje cinco, el de colas. En el parcial te aparece dos veces: la teoría, mayormente en multiple choice y quizás con alguna pregunta de desarrollo, y la práctica, la tabla de simulación que hacés a mano con calculadora. El profe sacó la notación de Kendall, así que no la estudies, y las medidas de desempeño como tema de teoría, porque se evalúan con la práctica. Además, de la teoría salen todas las fórmulas de cálculo y se evalúan los conceptos: las cuentas las vas a encontrar solo en la parte de la tabla. Esto dura unos veintiocho minutos. Hay cuatro ideas centrales. Una: las colas se forman por la variabilidad, aunque la capacidad media alcance. Dos: en la tabla, cada cliente empieza en el mayor valor entre su llegada y el fin del anterior. Tres: los tiempos de espera se promedian sobre los clientes, y las cantidades en cola y la utilización se promedian en el tiempo. Cuatro: la Ley de Little une esas dos maneras de promediar y sirve para verificar. En cada tema te marco lo importante, la trampa y, si puede caer de desarrollo, cómo armar la respuesta.

## Por qué existen las colas

Casi todos los sistemas que se estudian con simulación discreta son sistemas de colas: una línea de producción, una guardia, una caja de supermercado. Una cola aparece cuando un recurso compartido tiene que atender más pedidos de los que puede procesar en ese momento. Y el apunte desarma un malentendido: uno piensa que si la capacidad alcanza en promedio, no debería haber cola. Es falso. Las llegadas y los servicios no están sincronizados: a veces llegan tres juntos, a veces una atención se estira. Esa desincronización es la variabilidad, y es la razón de que existan las colas y de que haga falta simular.

**Lo importante.** La causa de las colas es la variabilidad, no la falta de capacidad media.

**Ojo, trampa.** «Si la capacidad media supera a la demanda media, no se forma cola»: falso, es justo el malentendido del apunte. Desconfiá también de «solo hay cola cuando el servidor está al cien por ciento».

**Si te toca de desarrollo.** Definí la cola. Planteá el malentendido de la capacidad media. Explicá la variabilidad con un ejemplo. Y cerrá con la idea del apunte: que la atención media sea de tres minutos no significa que cada una dure tres, y esa diferencia es la que genera las colas y obliga a simular.

## Los elementos de un sistema de colas

Son seis. La fuente de entrada, la población de donde vienen los clientes: lo habitual es suponerla infinita, y se toma finita cuando los clientes potenciales son pocos y las llegadas dependen de cuántos ya están adentro. El cliente, la entidad que pide servicio, con atributos como instante de llegada, tipo o prioridad. El patrón de llegadas, que se define por la distribución del tiempo entre llegadas, no por el instante de llegada; es la conexión con el eje tres. La cola, con su capacidad, finita o infinita, y su disciplina. El servidor, con cuántos hay, si son idénticos y la distribución del tiempo de servicio. Y el proceso de servicio: duración, canales, disponibilidad y si hay estaciones en secuencia.

**Lo importante.** Llegadas y servicios se describen con distribuciones de probabilidad, no con valores fijos.

**Ojo, trampa.** «El patrón de llegadas se modela con el instante de llegada de cada cliente»: falso, es la distribución del tiempo entre llegadas. Y no mezcles fuente finita, que es tener pocos clientes potenciales, con cola de capacidad limitada.

## Disciplina de cola

La disciplina decide a quién le toca cuando se libera el servidor. No cambia cuánto trabajo hay; cambia quién espera y cuánto. Por eso es una palanca de diseño barata.

FIFO, primero en llegar, primero atendido: la más común y la que se percibe como justa; no optimiza nada, pero reparte la espera parejo. LIFO, último en llegar, primero atendido: aparece en pilas de material; la espera media global no cambia, pero se vuelve muy desigual. Aleatoria: poco usada a propósito, sirve de referencia teórica. Por prioridad: mejora al grupo prioritario a costa del resto, y la media global puede incluso empeorar; es la de una guardia médica. Y primero el trabajo más corto: reduce la espera media del conjunto, pero puede postergar indefinidamente a los largos.

Con prioridad hay que definir si es expropiativa, cuando el prioritario interrumpe el servicio en curso, o no expropiativa, cuando espera a que termine y pasa adelante en la cola. Dan resultados distintos.

**Lo importante.** La disciplina no cambia el trabajo, cambia quién espera. Y cada una tiene su efecto: sabételos de memoria.

**Ojo, trampa.** Dos salen del apunte. «LIFO aumenta la espera media»: falso, la media no cambia. «La prioridad reduce la espera media global»: falso, puede empeorarla. La que baja la media es la del trabajo más corto.

## Configuraciones

Organizar colas y servidores es una decisión de diseño, no un dato del sistema. Hay cuatro: una cola y un servidor, el caso de los ejercicios; una cola y varios servidores, como un banco con fila única; varias colas y varios servidores, como las cajas del súper; y servidores en serie, como una línea de producción.

Con la misma cantidad de servidores, una cola única suele dar mejor resultado que las filas separadas. ¿Por qué? Porque comparte la capacidad: nunca queda un servidor ocioso mientras otro tiene gente esperando. Y no cuesta plata, solo reorganización.

**Lo importante.** A igual cantidad de servidores, la cola única le gana a las filas separadas porque comparte la capacidad.

**Ojo, trampa.** Las opciones suelen tener bien la conclusión y mal el motivo: no gana porque atienda más rápido ni porque tenga más servidores. Cuidado con el absoluto: el apunte dice «suele». Y no confundas el banco, que es una cola con varios servidores, con el súper, que son varias colas.

**Si te toca de desarrollo.** Nombrá las cuatro configuraciones con su ejemplo. Planteá la comparación entre fila única y filas separadas. Explicá el mecanismo del servidor libre con gente esperando en otra fila. Cerrá con que es una mejora sin agregar recursos, igual que elegir la disciplina.

## Dos maneras de promediar

El apunte lo marca como el concepto más importante del eje y el que más se confunde. Las medidas de desempeño, con sus cuentas, no entran como teoría: las ves en la práctica. Lo que sí entra es esta idea. Wq, la espera promedio en cola, y Lq, la cantidad promedio en cola, parecen los dos «el promedio de la cola», pero no son lo mismo.

Wq y W, que es el tiempo promedio en el sistema, son promedios por entidad: se fijan cuánto esperó cada cliente y promedian sobre los clientes. Da minutos. Lq, L, que es la cantidad promedio en el sistema, y la utilización son promedios en el tiempo: se fijan cuántos clientes había y promedian a lo largo de la corrida. Da clientes.

Por eso Lq no se obtiene promediando el largo de la cola en algunos instantes elegidos: le daría el mismo peso a dos clientes durante medio minuto que a uno durante ocho minutos. Cada valor tiene que pesar según cuánto duró.

Cómo se leen: Wq igual a un minuto quiere decir que un cliente cualquiera esperó, en promedio, un minuto. Lq igual a cero coma cuatro quiere decir que si mirás la cola en un momento al azar, encontrás en promedio cero coma cuatro personas. Lo primero le interesa al cliente; lo segundo, a quien dimensiona la sala de espera.

**Lo importante.** Dos preguntas, dos maneras de promediar: sobre los clientes o a lo largo del tiempo. Y la utilización va con Lq y L.

**Ojo, trampa.** La trampa número uno del eje son los pares cruzados: «Lq es un promedio sobre los clientes», «Wq es un promedio en el tiempo», «la utilización es un promedio por entidad». Todas falsas. También «Lq se obtiene promediando la cola en los instantes de llegada», que el apunte descarta. Y mirá las unidades: Lq en minutos o Wq en clientes es un error.

**Si te toca de desarrollo.** Decí que hay dos tipos de promedio y por qué se confunden. Explicá Wq y W, por entidad, en minutos. Explicá Lq, L y la utilización, como promedios en el tiempo de una función escalonada, donde cada valor pesa según cuánto duró, en clientes. Mostrá por qué no se muestrean instantes. Y cerrá con la lectura de cada uno.

## Las tres funciones escalonadas

B de t vale uno si el servidor está ocupado y cero si está libre; de ella sale la utilización. Q de t cuenta los que esperan en la fila: sube cuando llega alguien que tiene que esperar y baja cuando uno pasa a ser atendido; de ella sale Lq. N de t cuenta los que están en el sistema, o sea, los que esperan más el que se atiende; de ella sale L.

Mirándolas juntas aparece una relación que vale en todo instante: los que están en el sistema son los que esperan más el que se está atendiendo. Y como vale instante a instante, vale también para los promedios.

Esto ahorra trabajo, porque no hace falta dibujar N de t, y sirve de control: si medís las tres áreas y la suma no cierra, hay un error en algún gráfico. La cuenta la hacés en la práctica, en el paso cuatro.

**Lo importante.** Las tres funciones y su relación: en el sistema están los que esperan más el que se atiende, en todo instante y, por eso, también en promedio.

**Ojo, trampa.** Q de t no sube con cada llegada, solo con las que esperan; y baja cuando alguien pasa al servidor, no cuando se va.

## Ley de Little

El apunte parte de una observación: el área bajo Q de t coincide exactamente con la suma de las esperas, y el área bajo N de t, con la suma de las permanencias. No es casualidad: si el sistema arranca y termina vacío, cada cliente aporta al área justo el tiempo que estuvo presente. Sumar por clientes o sumar a lo largo del tiempo son dos formas de recorrer la misma superficie.

De ahí sale la Ley de Little, que une las dos maneras de promediar: relaciona la cantidad promedio de clientes, que es un promedio en el tiempo, con el tiempo promedio de permanencia, que es un promedio sobre los clientes, a través de la tasa de llegada. La cuenta la hacés en la práctica, en el paso cinco. Y es muy general: no supone ninguna distribución, disciplina ni cantidad de servidores. Vale para cualquier sistema estable.

La advertencia metodológica: para que sea una verificación de verdad, los dos lados de la igualdad tienen que salir por caminos independientes, uno promediando esperas sobre los clientes y el otro sumando rectángulos bajo la curva. Si sacás Lq dividiendo la suma de esperas por el tiempo total simulado, la igualdad se cumple siempre por álgebra y no comprueba nada.

Y su valor: en el eje cuatro se dijo que verificar es comprobar que el modelo está bien construido. Little es la primera técnica concreta: si los indicadores no la cumplen, hay un error en el modelo o en la forma de recolectar los estadísticos.

**Lo importante.** Qué relaciona, su generalidad y su uso para verificar.

**Ojo, trampa.** «Solo vale con un servidor», «requiere llegadas exponenciales», «solo con FIFO»: todo falso. Es verificación, no validación: no compara el modelo con el sistema real. Y la igualdad entre área y suma de esperas el apunte la explica para un sistema que arranca y termina vacío.

**Si te toca de desarrollo.** Decí en palabras qué relaciona: la cantidad promedio en el sistema, la tasa de llegada y el tiempo promedio de permanencia. Explicá de dónde sale: con el sistema vacío al principio y al final, el área es la suma de los tiempos de cada cliente. Remarcá su generalidad. Presentala como la primera técnica de verificación. Y cerrá con la advertencia de los caminos independientes.

## La práctica: la tabla paso a paso

Los tres ejercicios del práctico piden lo mismo, y el tres tiene el formato y el puntaje del ejercicio de colas del parcial. Acá sí van las medidas de desempeño con sus cuentas, porque el profe las evalúa con este ejercicio. Va la receta.

### Antes de arrancar

Leé bien el enunciado: un dato es el instante de llegada y el otro es la duración de la atención, no el instante en que termina. El apunte dice que confundirlos es el error más frecuente y arruina toda la tabla.

### Paso uno: la tabla

Para cada cliente, en orden: inicio es el mayor valor entre su llegada y el fin del anterior. Fin es inicio más duración. Espera, su Wq, es inicio menos llegada. Permanencia, su W, es fin menos llegada. Después sumá duraciones, esperas y permanencias. Control rápido: la suma de permanencias es la suma de esperas más la de duraciones.

**Ojo, trampa.** El empate: si un cliente llega justo cuando termina el anterior, empieza en ese instante y su espera es cero. La convención de la cátedra, que viene del eje cuatro, es procesar primero el fin de servicio y después la llegada, así el recurso ya está libre. En la tabla sale solo por la regla del máximo; donde te puede pisar es al contar la cola.

### Paso dos: el horizonte

T es el instante en que se retira el último cliente, o sea, el fin del último servicio.

**Ojo, trampa.** No es la última llegada ni la suma de duraciones. En el ejercicio uno las dos dan veinte, pero T es veinticinco. Con veinte, la utilización te daría uno, y eso tiene que hacerte ruido.

### Paso tres: los indicadores

Wq: suma de esperas dividida por la cantidad de clientes. W: suma de permanencias dividida por la cantidad de clientes. Utilización: suma de duraciones dividida por T. Ocioso: T menos la suma de duraciones. Lambda, la tasa de llegada: clientes dividido T. Proporción que espera: clientes con espera mayor que cero, dividido el total. Cola máxima: la mayor cantidad de gente esperando a la vez.

**Ojo, trampa.** El divisor. Wq y W van por clientes; la utilización, lambda, Lq y L, por T. En el ejercicio uno, si dividís el área de la cola por los ocho clientes en vez de por los veinticinco minutos, te da dos, que es justo Wq: ese número va a estar de distractor. Lambda va en clientes por minuto, no al revés. La cola máxima es un pico; Lq es un promedio. Y el que llega justo cuando el otro termina no cuenta entre los que esperaron.

### Paso cuatro: gráficos y áreas

Tres gráficos sobre el mismo eje de tiempo: las llegadas como marcas, B de t como bloques entre cero y uno, y Q de t como escalones. Para el área de Q armás la tabla de tramos: cortás en cada llegada, inicio y fin, multiplicás cuántos había en cola por cuánto duró el tramo, y sumás. Lq es esa área dividida por T. La utilización sale del área de B. Y L es Lq más la utilización.

**Ojo, trampa.** El área de Q te va a coincidir con la suma de esperas, y es un buen control. Pero si te piden Lq por área y vos dividís la suma de esperas por T, no hiciste lo pedido y Little queda circular. Otra: el empate al contar la cola. En el ejercicio dos, en el minuto veintidós termina el cliente cinco, entra el seis y llega el ocho. Con el fin primero, la cola queda en dos. Si procesás primero la llegada, por un instante contás tres y la cola máxima te sale mal. Al área no le cambia nada; al máximo, sí. Y L es Lq más la utilización, no Lq más uno: no siempre hay alguien en servicio.

### Paso cinco: verificar con Little

Comparás Lq por área contra lambda por Wq, y L contra lambda por W.

**Ojo, trampa.** Se multiplica, no se divide. Y usá lambda como fracción. En el ejercicio dos es ocho treintavos; si lo redondeás a cero coma veintisiete y multiplicás por tres, te da cero coma ochenta y uno y parece que no cierra.

## Los ejercicios del práctico

### Ejercicio uno: mesa de entradas

Llegadas: cero, siete, ocho, nueve, once, catorce, quince y veinte. Duraciones: dos, tres, dos, dos, dos, dos, cinco y dos. Inicios: cero, siete, diez, doce, catorce, dieciséis, dieciocho y veintitrés. Esperas: cero, cero, dos, tres, tres, dos, tres y tres, que suman dieciséis. Las permanencias suman treinta y seis.

T, veinticinco. Wq, dos minutos; W, cuatro coma cinco. Utilización, veinte dividido veinticinco, cero coma ocho; ocioso, cinco minutos. Lambda, cero coma treinta y dos. Esperan seis de ocho. Cola máxima, dos. Lq, cero coma sesenta y cuatro; L, uno coma cuarenta y cuatro. Little cierra.

### Ejercicio dos: farmacia de turno

Llegadas: cero, uno, cinco, trece, catorce, dieciséis, dieciocho y veintidós. Duraciones: tres, dos, dos, cuatro, cinco, tres, tres y dos. Inicios: cero, tres, cinco, trece, diecisiete, veintidós, veinticinco y veintiocho. Esperas: cero, dos, cero, cero, tres, seis, siete y seis, que suman veinticuatro. Las permanencias suman cuarenta y ocho.

T, treinta. Wq, tres minutos; W, seis. Utilización, veinticuatro dividido treinta, cero coma ocho; ocioso, seis minutos. Lambda, ocho treintavos. Esperan cinco de ocho. Cola máxima, dos. Lq, cero coma ocho; L, uno coma seis.

### Ejercicio dos, consigna efe

Cada atención dura un minuto menos: dos, uno, uno, tres, cuatro, dos, dos y uno. T baja a veinticinco; la suma de esperas, de veinticuatro a trece; Wq, de tres a más o menos uno coma seis; y la utilización, de cero coma ocho a cero coma sesenta y cuatro. A mí Lq me dio cero coma cincuenta y dos. El tiempo de atención bajó un tercio y la espera, casi a la mitad. Como T cambió, compará indicadores, no áreas en bruto. Lo calculé yo con la misma regla; revisalo con tu hoja.

### Ejercicio tres: formato parcial

Llegadas: cero, cinco, siete, ocho, dieciséis, diecisiete, dieciocho y veintidós. Duraciones: tres, dos, tres, tres, tres, dos, dos y dos. Inicios: cero, cinco, siete, diez, dieciséis, diecinueve, veintiuno y veintitrés. Esperas: cero, cero, cero, dos, cero, dos, tres y uno, que suman ocho. Las permanencias suman veintiocho.

T, veinticinco. Wq, un minuto; W, tres coma cinco. Utilización, cero coma ocho; ocioso, cinco minutos. Lambda, cero coma treinta y dos. Esperan cuatro de ocho. Cola máxima, dos. Lq, cero coma treinta y dos; L, uno coma doce. Little cierra. El visitante tres llega en el siete, justo cuando termina el dos, así que no espera. Lo calculé yo; revisalo con tu hoja.

La consigna e: el jefe dice que con el operador ocupado el ochenta por ciento, el puesto está bien dimensionado. Tu respuesta: la utilización sola no alcanza. La mitad de los visitantes esperó, hubo dos en cola, y las esperas aparecen cuando llegan varios juntos: es la variabilidad. El argumento más fuerte está en el propio práctico: los tres ejercicios tienen utilización cero coma ocho, y Wq da dos, tres y un minuto. Sumá que una sola corrida con ocho visitantes es poca evidencia, y que si un minuto de espera es aceptable depende de un criterio de servicio que el enunciado no da.

## Preguntas tipo multiple choice

Pregunta uno. ¿Qué es correcto sobre Wq y Lq? Opción a: los dos son promedios en el tiempo. Opción b: Wq es un promedio sobre los clientes, en minutos, y Lq un promedio en el tiempo, en clientes. Opción c: Lq se obtiene promediando el largo de la cola en algunos instantes. Opción d: miden lo mismo con distinta unidad. La correcta es la b. La tramposa es la c: el apunte la descarta porque no pondera cuánto duró cada valor.

Pregunta dos. La utilización del servidor es: opción a, un promedio por entidad, como Wq; opción b, un promedio en el tiempo, como Lq y L; opción c, la suma de duraciones dividida por la cantidad de clientes; opción d, la proporción de clientes que no esperaron. La correcta es la b: mira cuánto tiempo estuvo ocupado el servidor a lo largo de la corrida. La tramposa es la a, porque se arma con la duración de cada cliente.

Pregunta tres. La Ley de Little: opción a, solo vale con un servidor; opción b, requiere llegadas exponenciales; opción c, vale para cualquier sistema estable, sin suponer distribución, disciplina ni cantidad de servidores; opción d, solo vale con FIFO. La correcta es la c. Las otras le agregan a la ley un supuesto que no tiene.

Pregunta cuatro. Según el apunte, comprobar Little en un modelo sirve para: opción a, validarlo contra el sistema real; opción b, verificar que está bien construido; opción c, estimar la distribución de llegadas; opción d, elegir la disciplina. La correcta es la b. La tramposa es la a: verificar no es validar.

Pregunta cinco. Un alumno calcula Lq dividiendo la suma de esperas por T y después comprueba que es igual a lambda por Wq. Opción a: es una verificación válida y más rápida. Opción b: la igualdad se cumple siempre por álgebra y no comprueba nada. Opción c: Little no se va a cumplir. Opción d: Lq da distinto que por área. La correcta es la b, la advertencia metodológica. La tramposa es la a: el número está bien, pero la comprobación es circular.

Pregunta seis. Sobre las disciplinas, ¿cuál es correcta? Opción a: LIFO aumenta la espera media. Opción b: la prioridad reduce siempre la espera media global. Opción c: primero el trabajo más corto reduce la espera media, pero puede postergar indefinidamente a los largos. Opción d: cambiar la disciplina reduce el trabajo del servidor. La correcta es la c. La a y la b son las trampas del apunte: LIFO no cambia la media, y la prioridad puede empeorarla.

Pregunta siete. Con los mismos servidores, una cola única frente a una fila por servidor: opción a, es peor porque el cliente no elige; opción b, suele ser mejor porque nunca queda un servidor ocioso con gente esperando en otra fila; opción c, es mejor porque atiende más rápido; opción d, da igual. La correcta es la b. La tramposa es la c: conclusión bien, motivo mal.

Pregunta ocho. Un recurso tiene, en promedio, capacidad suficiente para la demanda. Según el apunte: opción a, no se forma cola, porque la capacidad media alcanza; opción b, se forma cola igual, porque las llegadas y los servicios no están sincronizados; opción c, solo se forma cola si el servidor está al cien por ciento; opción d, que haya cola depende solo de la disciplina. La correcta es la b: la causa de las colas es la variabilidad. La tramposa es la a, que es justo el malentendido que el apunte desarma.

Pregunta nueve. Para modelar el patrón de llegadas hay que definir: opción a, el instante de llegada de cada cliente; opción b, la distribución del tiempo entre llegadas; opción c, la capacidad de la cola; opción d, la cantidad de servidores. La correcta es la b, que es la conexión con el eje tres. La tramposa es la a: lo que se modela es el tiempo entre llegadas, no el instante.

Pregunta diez. En un modelo con prioridad, la prioridad es expropiativa cuando: opción a, el cliente prioritario interrumpe el servicio en curso; opción b, el prioritario espera a que termine el servicio actual y pasa adelante en la cola; opción c, se atiende primero el trabajo más corto; opción d, da lo mismo, porque las dos variantes dan iguales resultados. La correcta es la a. La tramposa es la b, que es la no expropiativa. Y la d es falsa: el apunte dice que son sistemas distintos y dan resultados distintos.

Pregunta once. La cantidad de clientes en cola, Q de t: opción a, sube con cada llegada; opción b, sube cuando llega alguien que tiene que esperar y baja cuando uno pasa a ser atendido; opción c, baja cuando un cliente se va del sistema; opción d, es un número fijo para toda la corrida. La correcta es la b. Las tramposas son la a y la c: si el servidor está libre, el que llega no pasa por la fila, y la fila baja cuando alguien pasa al servidor, no cuando se va. La d tampoco: el apunte dice que la cola no es un número, sino una función escalonada que cambia a lo largo de la corrida.

## Lo que puede entrar en desarrollo

Si tuviera que apostar, van en este orden.

Primero, promediar por entidad contra promediar en el tiempo: Wq y W sobre los clientes, en minutos; Lq, L y la utilización a lo largo del tiempo, en clientes; por qué no sirve muestrear instantes; y que en el sistema están los que esperan más el que se atiende.

Segundo, la Ley de Little: qué relaciona; de dónde sale; su generalidad; su uso como primera técnica de verificación; y la advertencia de los dos caminos independientes.

Tercero, por qué un recurso con utilización razonable puede tener colas, que es la consigna e del ejercicio tres con otro nombre: la variabilidad como causa; el dato del práctico, misma utilización con Wq de dos, tres y un minuto; y qué mirar en cambio.

Cuarto, las decisiones de diseño baratas: cola única contra filas separadas, con su motivo, y la disciplina, que no cambia el trabajo pero sí quién espera.

## Lo mínimo que te tenés que llevar

Uno: las colas aparecen por la variabilidad, aunque la capacidad media alcance; por eso se simula.

Dos: en la tabla, instante no es duración. Cada cliente empieza en el mayor valor entre su llegada y el fin del anterior, y ante un empate va primero el fin de servicio.

Tres: en la tabla, Wq y W se dividen por la cantidad de clientes; Lq, L, la utilización y lambda se dividen por T, que es cuando se va el último.

Cuatro: en la tabla, L es Lq más la utilización.

Cinco: Little, que en la tabla comprobás con L igual a lambda por W, vale para cualquier sistema estable y verifica de verdad solo con dos caminos independientes.

Seis: la cola única le gana a varias filas con los mismos servidores, y la utilización sola no dice si un sistema está bien dimensionado.

Eso es el eje cinco. Mañana, en la tabla, despacio y con la regla del máximo. Suerte.
