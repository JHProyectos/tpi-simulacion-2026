# Eje 5. Simulación de sistemas discretos

Bueno, vamos con el eje cinco, el de colas. En el parcial te aparece dos veces: la teoría, mayormente en multiple choice y quizás con alguna pregunta de desarrollo, y la práctica, la tabla de simulación que hacés a mano con calculadora. Esto dura unos treinta y un minutos. Hay cuatro ideas centrales. Una: las colas se forman por la variabilidad, aunque la capacidad media alcance. Dos: en la tabla, cada cliente empieza en el mayor valor entre su llegada y el fin del anterior. Tres: los tiempos de espera se promedian sobre los clientes, y las cantidades en cola y la utilización se promedian en el tiempo. Cuatro: la Ley de Little une esas dos maneras de promediar y sirve para verificar. En cada tema te marco lo importante, la trampa y, si puede caer de desarrollo, cómo armar la respuesta.

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

## Notación de Kendall

Describe un sistema de colas en una línea, con seis campos separados por barras, en este orden: distribución del tiempo entre llegadas, distribución del tiempo de servicio, cantidad de servidores en paralelo, capacidad total del sistema contando cola y servicio, tamaño de la población y disciplina. En los dos primeros van letras: M, exponencial o markoviana; D, determinística, o sea constante; y G, general.

Casi siempre se escriben solo los tres primeros, y entonces se sobreentiende capacidad infinita, población infinita y FIFO.

Los ejemplos del apunte. M barra M barra uno: una caja con fila única sin límite. M barra M barra cinco: cinco cajeros con una sola fila. M barra M barra veinte barra treinta: un centro de llamadas con veinte operadores y treinta líneas; si las treinta están ocupadas, la llamada se pierde. M barra D barra uno: una máquina de ciclo fijo, servicio sin variabilidad. G barra G barra uno: el caso general, sin fórmula cerrada, que se resuelve simulando.

Para qué sirve: obliga a explicitar los supuestos antes de construir el modelo. El apunte la llama una herramienta de modelado disfrazada de notación.

**Lo importante.** El orden de los campos: llegadas, servicio, servidores, capacidad, población, disciplina. Y qué se supone cuando se escriben solo tres.

**Ojo, trampa.** La M es exponencial, no «media» ni «múltiple». El primer campo son las llegadas: en M barra D barra uno lo constante es el servicio. El cuarto campo es la capacidad del sistema, no el largo de la cola: en el centro de llamadas, con veinte atendiendo, quedan como mucho diez esperando. Si se omiten campos, se supone infinito, infinito y FIFO, no cero. Y el que se resuelve simulando por no tener fórmula cerrada es G barra G barra uno.

**Si te toca de desarrollo.** Decí que es la forma estándar de describir un sistema de colas. Nombrá los seis campos en orden, con sus valores. Explicá qué se supone al omitir los tres últimos. Leé un ejemplo. Y cerrá con que obliga a explicitar supuestos.

## Medidas de desempeño

Se agrupan según desde dónde mirás.

Desde el cliente se mide tiempo y se promedia sobre los clientes. Wq es el tiempo promedio de espera en cola: la suma de las esperas dividida por la cantidad de clientes. W es el tiempo promedio en el sistema: la suma de las permanencias, desde que cada uno llega hasta que se va, dividida por la cantidad de clientes. Y W es Wq más el tiempo promedio de servicio.

Desde el sistema se mide cantidad y se promedia en el tiempo. Lq es la cantidad promedio de clientes en cola, y L la cantidad promedio en el sistema. Cada una es el área bajo su curva dividida por el tiempo total simulado, que llamamos T.

Desde el recurso está la utilización, que el apunte escribe con la letra griega rho: tiempo ocupado dividido por T; con varios servidores se promedia entre todos. El tiempo ocioso es T menos el tiempo ocupado. Y en la misma tabla aparece lambda, la tasa de llegada: cantidad de clientes dividida por T.

Se suman la longitud máxima de cola, para dimensionar la sala de espera; la proporción de clientes que esperan; y, si la capacidad es limitada, los rechazados.

**Lo importante.** Cliente: tiempos divididos por la cantidad de clientes. Sistema y recurso: divididos por T.

**Ojo, trampa.** Lambda es clientes dividido tiempo, en clientes por minuto, no al revés. La longitud máxima es un pico; Lq es un promedio. Y la utilización ideal no es cien por ciento: el apunte dice que un recurso que nunca descansa está saturado.

## Dos maneras de promediar

El apunte lo marca como el concepto más importante del eje y el que más se confunde. Wq y Lq parecen los dos «el promedio de la cola», pero no son lo mismo.

Wq y W son promedios por entidad: cuánto esperó cada cliente, sumado y dividido por la cantidad de clientes. Da minutos. Lq, L y la utilización son promedios en el tiempo: el área bajo una curva dividida por T. Da clientes.

Por eso Lq no se obtiene promediando el largo de la cola en algunos instantes elegidos: le daría el mismo peso a dos clientes durante medio minuto que a uno durante ocho minutos. Cada valor tiene que pesar según cuánto duró.

Cómo se leen: Wq igual a un minuto quiere decir que un cliente cualquiera esperó, en promedio, un minuto. Lq igual a cero coma cuatro quiere decir que si mirás la cola en un momento al azar, encontrás en promedio cero coma cuatro personas. Lo primero le interesa al cliente; lo segundo, a quien dimensiona la sala de espera.

**Lo importante.** Dos preguntas, dos divisores: la cantidad de clientes o T. Y la utilización va con Lq y L.

**Ojo, trampa.** La trampa número uno del eje son los pares cruzados: «Lq es un promedio sobre los clientes», «Wq es un área dividida por T», «la utilización es un promedio por entidad». Todas falsas. También «Lq se obtiene promediando la cola en los instantes de llegada», que el apunte descarta. Y mirá las unidades: Lq en minutos o Wq en clientes es un error.

**Si te toca de desarrollo.** Decí que hay dos tipos de promedio y por qué se confunden. Explicá Wq y W, por entidad, en minutos. Explicá Lq, L y la utilización, como área bajo una función escalonada dividida por T, en clientes. Mostrá por qué no se muestrean instantes. Y cerrá con la lectura de cada uno.

## Las tres funciones escalonadas

B de t vale uno si el servidor está ocupado y cero si está libre; su área dividida por T da la utilización. Q de t cuenta los que esperan en la fila: sube cuando llega alguien que tiene que esperar y baja cuando uno pasa a ser atendido; su área dividida por T da Lq. N de t cuenta los que están en el sistema, o sea, los que esperan más el que se atiende; su área dividida por T da L.

En todo instante, N de t es Q de t más B de t. Como vale instante a instante, vale también para las áreas y los promedios: L es igual a Lq más la utilización. En el ejemplo del apunte las áreas son doce para B, seis para Q y dieciocho para N, con T igual a quince: L da cero coma cuatro más cero coma ocho, uno coma dos.

Esto ahorra trabajo, porque no hace falta dibujar N de t, y sirve de control: si medís las tres áreas y la suma no cierra, hay un error en algún gráfico.

**Lo importante.** L es Lq más la utilización, porque en el sistema están los que esperan más el que se atiende.

**Ojo, trampa.** «L es Lq más uno», como si siempre hubiera alguien en servicio; «L es Lq por la utilización»; «L es Lq más W», que suma una cantidad con un tiempo. Todas falsas. Y Q de t no sube con cada llegada, solo con las que esperan; y baja cuando alguien pasa al servidor, no cuando se va.

## Ley de Little

En el ejemplo, el área bajo Q dio seis, exactamente la suma de las esperas, y el área bajo N dio dieciocho, la suma de las permanencias. No es casualidad: si el sistema arranca y termina vacío, cada cliente aporta al área justo el tiempo que estuvo presente.

De ahí sale la Ley de Little: L es igual a lambda por W, y Lq es igual a lambda por Wq. La cantidad promedio en el sistema es la tasa de llegada por el tiempo promedio de permanencia. Y es muy general: no supone ninguna distribución, disciplina ni cantidad de servidores. Vale para cualquier sistema estable.

En el ejemplo, lambda es seis dividido quince, cero coma cuatro. Por Wq, que es uno, da cero coma cuatro; por W, que es tres, da uno coma dos. Igual que por áreas.

La advertencia metodológica: para que sea una verificación de verdad, los dos lados tienen que salir por caminos independientes, uno promediando esperas sobre los clientes y el otro sumando rectángulos bajo la curva. Si sacás Lq dividiendo la suma de esperas por T, la igualdad se cumple siempre por álgebra y no comprueba nada.

Y su valor: en el eje cuatro se dijo que verificar es comprobar que el modelo está bien construido. Little es la primera técnica concreta: si los indicadores no la cumplen, hay un error en el modelo o en la forma de recolectar los estadísticos.

**Lo importante.** Las dos relaciones, su generalidad y su uso para verificar.

**Ojo, trampa.** «Solo vale para M barra M barra uno», «requiere llegadas exponenciales», «solo con FIFO»: todo falso. Es verificación, no validación: no compara el modelo con el sistema real. Se multiplica, no se divide. Y la igualdad entre área y suma de esperas el apunte la explica para un sistema que arranca y termina vacío.

**Si te toca de desarrollo.** Enunciá las dos relaciones en palabras. Explicá de dónde salen: con el sistema vacío al principio y al final, el área es la suma de los tiempos de cada cliente. Remarcá su generalidad. Presentala como la primera técnica de verificación. Y cerrá con la advertencia de los caminos independientes.

## La práctica: la tabla paso a paso

Los tres ejercicios del práctico piden lo mismo, y el tres tiene el formato y el puntaje del ejercicio de colas del parcial. Va la receta.

### Antes de arrancar

Leé bien el enunciado: un dato es el instante de llegada y el otro es la duración de la atención, no el instante en que termina. El apunte dice que confundirlos es el error más frecuente y arruina toda la tabla.

### Paso uno: la tabla

Para cada cliente, en orden: inicio es el mayor valor entre su llegada y el fin del anterior. Fin es inicio más duración. Espera, su Wq, es inicio menos llegada. Permanencia, su W, es fin menos llegada. Después sumá duraciones, esperas y permanencias. Control rápido: la suma de permanencias es la suma de esperas más la de duraciones.

**Ojo, trampa.** El empate: si un cliente llega justo cuando termina el anterior, empieza en ese instante y su espera es cero. La convención de la cátedra, que viene del eje cuatro, es procesar primero el fin de servicio y después la llegada, así el recurso ya está libre. En la tabla sale solo por la regla del máximo; donde te puede pisar es al contar la cola.

### Paso dos: el horizonte

T es el instante en que se retira el último cliente, o sea, el fin del último servicio.

**Ojo, trampa.** No es la última llegada ni la suma de duraciones. En el ejercicio uno las dos dan veinte, pero T es veinticinco. Con veinte, la utilización te daría uno, y eso tiene que hacerte ruido.

### Paso tres: los indicadores

Wq: suma de esperas dividida por la cantidad de clientes. W: suma de permanencias dividida por la cantidad de clientes. Utilización: suma de duraciones dividida por T. Ocioso: T menos la suma de duraciones. Lambda: clientes dividido T. Proporción que espera: clientes con espera mayor que cero, dividido el total. Cola máxima: la mayor cantidad de gente esperando a la vez.

**Ojo, trampa.** El divisor. Wq y W van por clientes; la utilización, lambda, Lq y L, por T. En el ejercicio uno, si dividís el área de la cola por los ocho clientes en vez de por los veinticinco minutos, te da dos, que es justo Wq: ese número va a estar de distractor. Y el que llega justo cuando el otro termina no cuenta entre los que esperaron.

### Paso cuatro: gráficos y áreas

Tres gráficos sobre el mismo eje de tiempo: las llegadas como marcas, B de t como bloques entre cero y uno, y Q de t como escalones. Para el área de Q armás la tabla de tramos: cortás en cada llegada, inicio y fin, multiplicás cuántos había en cola por cuánto duró el tramo, y sumás. Lq es esa área dividida por T. La utilización sale del área de B. Y L es Lq más la utilización.

**Ojo, trampa.** El área de Q te va a coincidir con la suma de esperas, y es un buen control. Pero si te piden Lq por área y vos dividís la suma de esperas por T, no hiciste lo pedido y Little queda circular. Otra: el empate al contar la cola. En el ejercicio dos, en el minuto veintidós termina el cliente cinco, entra el seis y llega el ocho. Con el fin primero, la cola queda en dos. Si procesás primero la llegada, por un instante contás tres y la cola máxima te sale mal. Al área no le cambia nada; al máximo, sí.

### Paso cinco: verificar con Little

Comparás Lq por área contra lambda por Wq, y L contra lambda por W.

**Ojo, trampa.** Usá lambda como fracción. En el ejercicio dos es ocho treintavos; si lo redondeás a cero coma veintisiete y multiplicás por tres, te da cero coma ochenta y uno y parece que no cierra.

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

Pregunta dos. La utilización del servidor es: opción a, un promedio por entidad, como Wq; opción b, un promedio en el tiempo, como Lq y L; opción c, la suma de duraciones dividida por la cantidad de clientes; opción d, la proporción de clientes que no esperaron. La correcta es la b: área bajo B de t dividida por T. La tramposa es la a, porque se arma con la duración de cada cliente.

Pregunta tres. Con un servidor, Lq vale cero coma cuatro y la utilización cero coma ocho. L vale: opción a, cero coma treinta y dos; opción b, uno coma dos; opción c, uno coma cuatro; opción d, cero coma cuatro. La correcta es la b, Lq más la utilización. La a multiplica en vez de sumar, y la c suma uno, como si siempre hubiera alguien en servicio.

Pregunta cuatro. La Ley de Little: opción a, solo vale para M barra M barra uno; opción b, requiere llegadas exponenciales; opción c, vale para cualquier sistema estable, sin suponer distribución, disciplina ni cantidad de servidores; opción d, solo vale con FIFO. La correcta es la c. Las otras le agregan a la ley un supuesto que no tiene.

Pregunta cinco. Con lambda igual a cero coma cuatro clientes por minuto y W igual a tres minutos, L vale: opción a, siete coma cinco; opción b, uno coma dos; opción c, cero coma trece; opción d, tres coma cuatro. La correcta es la b, lambda por W. La a divide W por lambda, y la c divide lambda por W.

Pregunta seis. Según el apunte, comprobar Little en un modelo sirve para: opción a, validarlo contra el sistema real; opción b, verificar que está bien construido; opción c, estimar la distribución de llegadas; opción d, elegir la disciplina. La correcta es la b. La tramposa es la a: verificar no es validar.

Pregunta siete. Un alumno calcula Lq dividiendo la suma de esperas por T y después comprueba que es igual a lambda por Wq. Opción a: es una verificación válida y más rápida. Opción b: la igualdad se cumple siempre por álgebra y no comprueba nada. Opción c: Little no se va a cumplir. Opción d: Lq da distinto que por área. La correcta es la b, la advertencia metodológica. La tramposa es la a: el número está bien, pero la comprobación es circular.

Pregunta ocho. Un cliente llega en el minuto siete, justo cuando termina el anterior. Opción a: empieza en el siete y no espera, porque primero se procesa el fin de servicio. Opción b: queda en cola, porque primero se procesa la llegada. Opción c: empieza en el siete más la duración del anterior. Opción d: se decide al azar. La correcta es la a: regla del máximo y desempate del eje cuatro. La tramposa es la b, que además infla la cola máxima.

Pregunta nueve. M barra M barra uno, con tres campos, significa: opción a, llegadas y servicio exponenciales, un servidor, capacidad y población infinitas y FIFO; opción b, llegadas de media constante y un lugar en el sistema; opción c, múltiples llegadas y múltiples servicios; opción d, exponenciales, un servidor y capacidad uno. La correcta es la a. Las trampas: leer la M como media o múltiple, y tomar el uno como capacidad.

Pregunta diez. En M barra M barra veinte barra treinta, el treinta es: opción a, el largo máximo de la cola; opción b, la capacidad total del sistema, cola más servicio; opción c, la población; opción d, los servidores. La correcta es la b. La tramposa es la a: el cuarto campo incluye a los que están siendo atendidos.

Pregunta once. Sobre las disciplinas, ¿cuál es correcta? Opción a: LIFO aumenta la espera media. Opción b: la prioridad reduce siempre la espera media global. Opción c: primero el trabajo más corto reduce la espera media, pero puede postergar indefinidamente a los largos. Opción d: cambiar la disciplina reduce el trabajo del servidor. La correcta es la c. La a y la b son las trampas del apunte: LIFO no cambia la media, y la prioridad puede empeorarla.

Pregunta doce. Con los mismos servidores, una cola única frente a una fila por servidor: opción a, es peor porque el cliente no elige; opción b, suele ser mejor porque nunca queda un servidor ocioso con gente esperando en otra fila; opción c, es mejor porque atiende más rápido; opción d, da igual. La correcta es la b. La tramposa es la c: conclusión bien, motivo mal.

Pregunta trece. En el ejercicio uno, la última llegada es en el veinte, el último se va en el veinticinco, hay ocho clientes y el área bajo Q da dieciséis. Lq vale: opción a, dos; opción b, cero coma sesenta y cuatro; opción c, cero coma ocho; opción d, cero coma cincuenta. La correcta es la b. La a divide por los clientes y da justo Wq. La c toma como T la última llegada, y encima coincide con la utilización.

## Lo que puede entrar en desarrollo

Si tuviera que apostar, van en este orden.

Primero, promediar por entidad contra promediar en el tiempo: Wq y W sobre los clientes, en minutos; Lq, L y la utilización como área sobre T, en clientes; por qué no sirve muestrear instantes; y L igual a Lq más la utilización.

Segundo, la Ley de Little: las dos relaciones; de dónde salen; su generalidad; su uso como primera técnica de verificación; y la advertencia de los dos caminos independientes.

Tercero, por qué un recurso con utilización razonable puede tener colas, que es la consigna e del ejercicio tres con otro nombre: la variabilidad como causa; el dato del práctico, misma utilización con Wq de dos, tres y un minuto; y qué mirar en cambio.

Cuarto, la notación de Kendall: los seis campos en orden, los valores M, D y G, los supuestos al omitir los últimos tres, un ejemplo leído, y por qué es una herramienta de modelado.

Quinto, las decisiones de diseño baratas: cola única contra filas separadas, con su motivo, y la disciplina, que no cambia el trabajo pero sí quién espera.

## Lo mínimo que te tenés que llevar

Uno: las colas aparecen por la variabilidad, aunque la capacidad media alcance; por eso se simula.

Dos: en la tabla, instante no es duración. Cada cliente empieza en el mayor valor entre su llegada y el fin del anterior, y ante un empate va primero el fin de servicio.

Tres: Wq y W se dividen por la cantidad de clientes; Lq, L, la utilización y lambda se dividen por T, que es cuando se va el último.

Cuatro: L es Lq más la utilización.

Cinco: Little, L igual a lambda por W, vale para cualquier sistema estable y verifica de verdad solo con dos caminos independientes.

Seis: Kendall es llegadas, servicio, servidores, capacidad, población y disciplina; con tres campos, el resto es infinito, infinito y FIFO.

Siete: la cola única le gana a varias filas con los mismos servidores, y la utilización sola no dice si un sistema está bien dimensionado.

Eso es el eje cinco. Mañana, en la tabla, despacio y con la regla del máximo. Suerte.
