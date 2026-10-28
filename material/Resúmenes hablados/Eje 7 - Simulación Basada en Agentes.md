# Eje 7. Simulación basada en agentes

Bueno, vamos con el eje siete: simulación basada en agentes. Esto te lleva unos veintiocho minutos de escucha.

Primero, qué entra. De este eje entra solo la teoría, casi todo en multiple choice y quizás alguna pregunta de desarrollo. El práctico de NetLogo no entra; lo nombro solo cuando ayuda.

Y ahora, qué salió. El profe sacó del parcial la sección del modelo trazado a mano, es decir, todo el ejercicio de Schelling con su grilla, su tick y sus números. Y también todas las fórmulas de cálculo. Se evalúan los conceptos, así que eso no lo estudies.

¿Qué te tenés que llevar? Cuatro ideas. La primera: qué es un agente y qué no es. La segunda: que el tiempo y el orden de activación son parte de la especificación del modelo. La tercera: qué es emergencia y cómo se reconoce, con el test rápido, el criterio completo y los tres casos. Y la cuarta: cuándo conviene usar agentes, con la equifinalidad como su crítica más seria.

## Para ubicarte

En el eje cuatro viste cuatro paradigmas: eventos discretos, dinámica de sistemas, agentes y multimétodo. Los ejes cinco y seis fueron de eventos discretos. Este es el segundo paradigma.

El apunte arranca con el supermercado. Con eventos discretos respondés muy bien cuántas cajas hacen falta. Ahora cambiá la escena: los clientes miran las otras filas, algunos se cambian, otros abandonan, cada uno según su propia tolerancia. ¿Qué importa ahora? Ya no el flujo del proceso, sino lo que decide cada uno.

Pensalo así: antes mirabas el plano del local desde arriba; ahora te tenés que meter en la cabeza de cada cliente. La lógica pasó de la estructura del sistema a los individuos.

**Ojo, trampa.** El apunte no dice que eventos discretos no pueda modelar eso. Dice que se puede, pero cuesta.

## Qué es un agente

### La definición

Un agente es una entidad individual identificable, con estado propio, situada en un entorno, que ejecuta reglas de comportamiento y puede percibir y afectar al entorno o a otros agentes con cierto grado de autonomía.

Larga, ¿no? Desarmémosla en tres palabras.

Individual quiere decir que no es un promedio ni un agregado. Es uno, con nombre y apellido.

Situado quiere decir que vive en algún lado: una grilla, un espacio o una red. Y ese entorno es el que define quiénes son sus vecinos.

Y autonomía quiere decir que nadie le dice paso a paso qué hacer. Es como un conductor en el tránsito: nadie le maneja el volante, corre su propia lógica.

### Lo obligatorio y lo opcional

Esta es de las preguntas más probables.

El núcleo son cuatro propiedades: identidad, estado propio, autonomía y situación en un entorno. Para acordarte, pensá en cuatro preguntas: quién es, qué tiene, dónde está y si se maneja solo.

Después vienen dos muy frecuentes, pero no obligatorias. La reactividad, que es responder a lo que percibe. Y la interacción, que es influir sobre otros o intercambiar información.

Más afuera, la heterogeneidad: que los agentes puedan diferir entre sí. Frecuente, no obligatoria.

Y por último, tres opcionales. La proactividad, que es actuar según objetivos propios. El aprendizaje. Y la capacidad social compleja, como negociar o cooperar.

Abajo lo tenés dibujado en capas.

![Las propiedades de un agente en capas](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje7-agente.svg)

*Figura 1. El núcleo de cuatro en el centro y, hacia afuera, lo frecuente y lo opcional.*

**Lo importante.** Un modelo perfectamente válido puede no tener ninguna de las otras seis propiedades. Es como un auto: sin aire acondicionado ni radio, sigue siendo un auto. Según el apunte, muchos malentendidos vienen justamente de exigirle a todo agente cosas que solo tienen algunos.

**Ojo, trampa.** Hay tres que suenan obligatorias y no lo son. La primera, la interacción: es muy frecuente, pero no es núcleo. La segunda, la heterogeneidad, que parece la esencia del paradigma y sin embargo es frecuente, no obligatoria. Y la tercera, el aprendizaje, que es opcional.

### Cuatro cosas que un agente no es

Ahora al revés: cuatro errores.

El primero: un agente no es necesariamente una persona. Puede ser un vehículo, un router, una empresa, una célula o un proceso.

El segundo: no es inteligencia artificial. Los modelos más famosos usan agentes con una regla de dos líneas. Un agente puede ser deliberadamente tonto. ¿Y eso le quita valor? Al contrario. Si de reglas triviales sale un comportamiento colectivo complejo, el hallazgo es más fuerte, no más débil.

El tercero: no es lo mismo que un objeto de programación. Se implementa como objeto, sí. Pero lo que lo define es su papel en el modelo: un individuo activo que decide por sí mismo. Decir que un agente es un objeto es como decir que una novela es un archivo de texto: es cierto como implementación, pero no te dice qué es.

Y el cuarto: no es una persona animada en pantalla. Lo que importa es si decide por sí mismo o si recorre un camino que le marca el proceso. Pensá en un tren y en un peatón. El tren se mueve, pero va por las vías que le pusieron. El peatón elige por dónde ir. El agente es el peatón.

**Ojo, trampa.** Dos clásicas. Si una opción dice que reglas simples dan un hallazgo menos valioso, es falsa. Y un cliente que camina por la pantalla siguiendo la ruta del proceso no es un agente, aunque se vea como una persona.

## La ficha del modelo: los ocho componentes

¿Cómo se especifica un modelo de agentes? Con ocho preguntas. Si las respondés todas, el modelo está especificado. El apunte lo llama la ficha del modelo.

Las ocho filas son: agentes, estado, entorno, vecindad, reglas, interacción, tiempo y activación, y salidas. Pensala como un formulario: la fila que vos no completás, alguien la va a completar a su manera.

Un ejemplo, con el Schelling del práctico. El entorno es una grilla toroidal. La vecindad son las ocho celdas de alrededor. La interacción es indirecta, a través del espacio, porque los agentes no se comunican. Y el tiempo avanza por ticks, con los insatisfechos mudándose de a uno en orden aleatorio.

**Lo importante.** La ficha es una versión reducida del protocolo ODD. Y el componente que más se olvida es el séptimo, tiempo y activación. Se da por sentado que el tiempo simplemente avanza, y no es así.

### Cómo avanza el tiempo

Como en el eje cinco usaste siempre avance al siguiente evento, es fácil creer que eventos discretos usa siguiente evento y agentes usa incrementos fijos.

**Ojo, trampa.** Esa idea es falsa, y el apunte la plantea justamente para desarmarla. Es cierto que la mayoría de los modelos de agentes avanzan por pasos fijos, que se llaman ticks. Y es cierto que la mayoría de los de eventos discretos van al siguiente evento. Pero es una tendencia, no una definición. Hay modelos de agentes que agendan eventos futuros. Y hay plataformas de agentes construidas sobre un motor de eventos discretos.

Es como decir que el fútbol es lo que se juega los domingos: suele pasar, pero no lo define.

**Lo importante.** Entonces, ¿qué define a la simulación basada en agentes? No cómo avanza el reloj, sino cómo se representa el sistema: individuos explícitos, con estado propio, reglas locales e interacción. El mecanismo temporal es una decisión de implementación posterior.

### El orden de activación

Ahora viene lo más fino del eje. Imaginá un modelo de contagio. En este tick, A contagia a B. ¿Puede B contagiar a C en el mismo tick? Depende de una decisión que hay que tomar a propósito.

Primera opción, el esquema sincrónico. Todos calculan su nuevo estado mirando el estado del tick anterior, y después se actualizan todos juntos. Es como votar con sobre cerrado: todos votan mirando lo mismo, y los sobres se abren juntos. Resultado: B se enferma al final del tick, y contagia a C recién en el siguiente.

Segunda opción, el esquema asincrónico, o secuencial. Los agentes actúan de a uno, y cada uno ve los cambios de los anteriores. Es como votar a mano alzada, de a uno, viendo lo que votaron los de antes. Resultado: si B actúa después de A, se enferma y puede contagiar a C en el mismo tick.

Y el asincrónico trae una segunda decisión: en qué orden actúan. ¿Siempre el mismo, o al azar en cada tick?

Abajo tenés los dos esquemas lado a lado.

![El contagio con activación sincrónica y asincrónica](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje7-activacion.svg)

*Figura 2. En el sincrónico, C se contagia en el tick siguiente; en el asincrónico, puede contagiarse en el mismo.*

**Lo importante.** Esto no es un detalle de programación: es parte de la especificación, y puede cambiar los resultados. Dos personas implementan el mismo modelo conceptual, una sincrónica y otra secuencial. Obtienen resultados distintos, y ninguna cometió un error. ¿Dónde está la diferencia? En un supuesto que nunca se escribió.

Es como dos cocineros con la misma receta, que dice qué ingredientes van pero no en qué orden. Los dos la siguen bien, y les salen platos distintos.

Por eso el apunte lo conecta con la verificación de los ejes cuatro y seis, y dice que la fila siete de la ficha no se puede dejar en blanco.

**Ojo, trampa.** Dos cosas. Te pueden dar vuelta los esquemas: contagiar en el mismo tick solo es posible en el asincrónico, y solo si B actúa después de A. Y si una opción atribuye la diferencia de resultados a un error de implementación, es falsa.

## Emergencia

Llegamos al concepto central de la unidad, y a la razón más fuerte para usar el paradigma.

Emergencia es la aparición de una regularidad o estructura a nivel global que no fue programada como regla global, sino que resulta de la interacción repetida de reglas locales.

En criollo: el modelador programa cómo actúa cada individuo. No programa «formen una bandada». La bandada aparece sola.

Una imagen cotidiana: el caminito marcado en el pasto de una plaza. Nadie lo diseñó. Sale de que cada uno corta camino y pisa donde el pasto ya está gastado. El patrón está arriba; las decisiones, abajo.

### El test rápido y el criterio completo

¿Cómo sabés si algo es emergente? En dos pasos.

Primero, el test rápido: ¿existe en el modelo una instrucción que ordene directamente el patrón que observo? Si es que sí, no hay emergencia: hay una regla global disfrazada. Si es que no, y el patrón aparece igual, tenés un candidato. Ojo: candidato, todavía no confirmado.

Después, el criterio completo: un patrón es emergente cuando aparece a nivel global sin una regla global que lo imponga, y puede explicarse como resultado acumulado de reglas e interacciones locales.

Y la evidencia se refuerza si, al modificar o eliminar una regla local, el patrón cambia o desaparece. Esa es la parte operativa: sacás una pieza y mirás si se cae la estructura.

### Los tres casos

El caso uno no es emergencia. Una instrucción manda, en el tick cincuenta, a todos los agentes del tipo A hacia la izquierda, y aparece segregación perfecta. ¿Hay una instrucción que ordene el patrón? Sí. Lo ordenó una regla global, y el test rápido ya lo descarta.

El caso dos todavía no alcanza. Al inicializar al azar, por casualidad quedan siete azules juntos en un rincón. Nadie lo ordenó, así que pasa el test rápido. Pero no es emergencia: lo produjo el sorteo inicial, no la dinámica. Es como repartir las cartas y que te toquen tres ases: nadie lo ordenó, pero tampoco es una jugada; es el reparto. Un patrón emergente tiene que aparecer con las corridas, no venir dado.

Y el caso tres sí es emergencia. Cada pájaro aplica tres reglas mirando a sus vecinos cercanos: no chocarse, apuntar hacia donde apuntan ellos y no quedarse solo. Aparece una bandada coordinada, sin líder. Pasa el test rápido. Y si desactivás la regla de alineación, la bandada se deshace: cumple el criterio completo.

Abajo lo tenés dibujado, con los tres casos pasando por los filtros.

![Emergencia y los tres casos para reconocerla](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje7-emergencia.svg)

*Figura 3. La bandada sale de tres reglas locales. El caso uno cae en el test rápido, el dos en el criterio completo y el tres los pasa.*

**Ojo, trampa.** El caso dos es el tramposo. Que nadie lo haya ordenado no alcanza: el test rápido te da un candidato, no una confirmación. Y fijate que tampoco es una regla global disfrazada; eso es el caso uno.

### Las dos exageraciones

La primera exageración es tratarla como algo misterioso o inexplicable. No es magia. En modelos simples se puede analizar perfectamente por qué aparece el patrón.

La segunda es convertirla en requisito: creer que si un modelo no muestra emergencia, no es de agentes. No hay acuerdo en la literatura sobre eso. Como dice el apunte, es una razón poderosa para usar el paradigma, no un carnet de pertenencia.

**Si te toca de desarrollo.** Primero, dá la definición. Después, explicá el test rápido y el criterio completo, remarcando que sacar una regla y ver caer el patrón refuerza la evidencia. Aplicalo a los tres casos. Y por último, cerrá con las dos exageraciones: no es misteriosa y no es requisito.

## Cuándo conviene usar agentes y cuándo no

### Frente a eventos discretos

En eventos discretos, la entidad recorre un flujo definido en el modelo. La lógica está en la estructura del proceso. Y la pregunta típica es de espera, utilización y capacidad.

En agentes, la entidad ejecuta su propio comportamiento. La lógica está en las reglas locales del individuo. La heterogeneidad suele ser central, y la vecindad o la red son explícitas. Y la pregunta típica es de difusión, interacción y adaptación: de cómo lo micro produce lo macro.

**Ojo, trampa.** El apunte advierte que esto es una guía de modelado, no una frontera informática. Una entidad de eventos discretos puede llevar atributos, rutearse según condiciones y disparar eventos. Y un agente puede tener una regla trivial.

**Lo importante.** Entonces, ¿cuál es la diferencia más defendible? Dónde se ubica la lógica: en el flujo del sistema, o en el individuo que dice «mi estado es X, percibo Y, por eso hago Z».

Un mismo sistema, como el supermercado o una red de datos, admite las dos miradas, y ninguna es más correcta. Responden preguntas distintas. Eventos discretos pregunta cuánto. Agentes pregunta qué pasa si los individuos se comportan distinto entre sí.

### Frente a dinámica de sistemas

Dinámica de sistemas, que es el eje ocho, trabaja con niveles agregados, flujos y bucles de realimentación. Agentes trabaja con individuos explícitos, observa al individuo y al agregado a la vez, y es más costoso.

Si te sirve: dinámica de sistemas mira el bosque; agentes mira cada árbol y el bosque al mismo tiempo.

El ejemplo es una epidemia. Dinámica de sistemas usa susceptibles, infectados y recuperados, con tasas promedio. Con agentes, cada persona tiene sus contactos, y la curva aparece de los contagios individuales.

**Ojo, trampa.** Ninguno es más realista por definición. Si la pregunta se responde con promedios, dinámica de sistemas es mejor, porque es más barato y tiene menos supuestos.

Abajo tenés los tres paradigmas lado a lado.

![Dónde vive la lógica en cada paradigma](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje7-paradigmas.svg)

*Figura 4. La lógica vive en el flujo, en cada individuo o en los niveles agregados. Decide la pregunta.*

### Señales a favor y en contra

Primero, las señales a favor de agentes. Que importe la heterogeneidad. Que importe quién interactúa con quién. Que haya decisiones locales con información parcial, o adaptación o aprendizaje. Que se quiera explicar un patrón macro desde reglas micro. Y por último, que una política actúe sobre subgrupos distintos.

Después, las señales en contra. Que la pregunta sea de capacidad o de colas, y eventos discretos la resuelva. Que dinámica de sistemas responda lo mismo con menos supuestos. Que no haya evidencia para justificar las reglas individuales. Que se representen miles de individuos solo para mirar un promedio. Y por último, que el detalle micro no cambie la decisión.

**Si te toca de desarrollo.** Primero, ubicá la diferencia de fondo con eventos discretos, que es dónde está la lógica. Después marcá el contraste con dinámica de sistemas: individuos contra agregados. Mostrá un mismo sistema mirado de dos formas, como la epidemia. Nombrá algunas señales a favor y en contra. Y por último, cerrá con que ninguno es más realista por definición: decide la pregunta.

### El costo oculto: la equifinalidad

Ahora, la letra chica. Un modelo de agentes te obliga a inventar reglas de comportamiento, y esas reglas son mucho más difíciles de medir que un tiempo de servicio.

Y un modelo puede reproducir perfectamente los datos con reglas equivocadas. Eso es la equifinalidad, y el apunte la llama la crítica metodológica más seria al paradigma.

Es como el alumno que llega al resultado correcto con un procedimiento equivocado. El número da, pero el razonamiento está mal.

**Ojo, trampa.** Si una opción dice que, como el modelo reproduce bien los datos, sus reglas quedan validadas, esa es la trampa. Y no te guíes por el nombre: la equifinalidad no habla de agentes que terminan en el mismo estado.

## Áreas de aplicación

Lo que hace apropiado al paradigma no es el dominio, sino que la pregunta dependa de la interacción y de las diferencias entre individuos. Cerca de la carrera tenés cuatro: redes de computadoras, sistemas distribuidos, ciberseguridad y usuarios de una plataforma.

**Ojo, trampa.** «La epidemiología se modela siempre con agentes» es falso. No decide el dominio, decide la pregunta.

## Anexos: historia, herramientas y ODD

### Historia y herramientas

Tres hitos, en orden. Primero, Schelling en 1971, a mano. Después, Reynolds y las bandadas de los boids en 1987. Y por último, NetLogo, de Wilensky, en 1999.

La elección del paradigma es previa a la elección de la herramienta.

NetLogo es el entorno de agentes más usado en enseñanza, libre y gratuito. Su vocabulario mínimo son cinco palabras. Turtle es un agente móvil. Patch es una celda fija, que también tiene estado y puede ejecutar reglas. Link es una conexión entre agentes. Observer es el nivel global, el que crea agentes y mide. Y tick es un paso de tiempo.

FlexSim también hace agentes: desde 2020 incluye Agent System. Pero su propia documentación aclara que se relaciona estrechamente, aunque no exactamente, con el modelado basado en agentes de la literatura. Y AnyLogic es multimétodo real, con los tres paradigmas en un mismo modelo.

**Ojo, trampa.** «FlexSim es solo de eventos discretos» es falso: ningún software pertenece para siempre a un solo paradigma. Pero tampoco hacés agentes en FlexSim por poner personas que caminan. Acordate del tren y el peatón: hay que construir el comportamiento desde el individuo.

### El protocolo ODD

ODD viene de Overview, Design concepts, Details. Nació en ecología, por un problema concreto: los modelos publicados se describían tan incompletos que era imposible reproducirlos. Su versión vigente es de 2020.

Tiene siete elementos, en tres bloques. Primero, Overview, con tres: el propósito; las entidades, variables de estado y escalas; y la visión general del proceso y programación, que es qué pasa en cada paso y en qué orden actúan los agentes. Después, Design concepts: los conceptos de diseño, como emergencia, adaptación, aprendizaje, percepción, interacción, estocasticidad y observación. Y por último, Details, con tres: inicialización, datos de entrada y submodelos.

**Lo importante.** Los tres elementos de Overview son, esencialmente, las ocho filas de la ficha. Lo que agrega el ODD es el bloque de conceptos de diseño, que obliga a declarar cosas que de otro modo quedan implícitas.

**Ojo, trampa.** ODD documenta, no valida. Un modelo puede estar impecablemente descripto y ser un mal modelo. Es como una receta bien escrita: cualquiera la puede repetir, pero eso no garantiza que el plato salga rico. El protocolo sirve para que otro lo reproduzca y lo discuta. Y no mezcles los números: la ficha tiene ocho componentes; el ODD, siete elementos en tres bloques.

## Preguntas tipo multiple choice

Pregunta uno. ¿Cuál pertenece al núcleo obligatorio de un agente? Opciones: aprendizaje, heterogeneidad, autonomía o proactividad.

La correcta es autonomía, porque el núcleo es identidad, estado propio, autonomía y situación en un entorno. ¿Y la que te quiere hacer pisar el palito? Heterogeneidad: parece esencial, pero es frecuente, no obligatoria.

Pregunta dos. ¿Qué afirmación sobre los agentes es correcta? Las opciones: que tiene que representar a una persona; que necesita algo de inteligencia artificial; que puede tener una sola regla trivial y el modelo seguir siendo valioso; o que toda entidad que se mueve en pantalla es un agente.

Va la tercera: con reglas triviales, el hallazgo es más fuerte. La tramposa es la de inteligencia artificial.

Pregunta tres. ¿Qué define a la simulación basada en agentes? Opciones: avanzar por incrementos fijos; programarse en NetLogo; representar el sistema con individuos explícitos, con estado propio, reglas locales e interacción; o producir siempre emergencia.

Es la tercera. La tramposa es incrementos fijos, que es una tendencia, no una definición.

Pregunta cuatro. A contagia a B en el tick actual. Con activación sincrónica, ¿cuándo puede B contagiar a C? Opciones: en el mismo tick; en el tick siguiente; según el orden aleatorio; o nunca.

La correcta es en el tick siguiente, porque todos calculan con el estado anterior y se actualizan juntos: es el sobre cerrado. La tramposa es en el mismo tick, que corresponde al asincrónico cuando B actúa después de A.

Pregunta cinco. Dos personas implementan el mismo modelo conceptual, una con activación sincrónica y otra secuencial, y obtienen resultados distintos. ¿Por qué? Opciones: una cometió un error de programación; es ruido que se arregla con más réplicas; hay un supuesto que no se escribió, el de tiempo y activación; o el modelo no es válido.

Va la tercera. La tramposa es el error de programación: el apunte aclara que ninguna se equivocó.

Pregunta seis. Al inicializar al azar quedan siete azules juntos en un rincón, sin que nadie lo ordene. ¿Es emergencia? Opciones: sí, porque no hay regla global; no, porque es una regla global disfrazada; no, porque lo produjo el sorteo inicial y no la dinámica; o sí, pero débil.

Es la tercera: son los tres ases del reparto. La tramposa es la primera, porque pasar el test rápido solo te da un candidato.

Pregunta siete. ¿Qué refuerza la evidencia de que un patrón es emergente? Opciones: que sea sorprendente; que no se pueda explicar desde las reglas; que al modificar o eliminar una regla local el patrón cambie o desaparezca; o que aparezca desde el primer tick.

La correcta es la tercera. La tramposa es la segunda, que es la exageración de la emergencia misteriosa.

Pregunta ocho. Un modelo hecho con agentes no muestra ningún patrón emergente. ¿Qué se puede decir? Opciones: que no es un modelo de agentes; que en realidad es de eventos discretos; que puede ser un modelo de agentes correctamente construido; o que está mal verificado.

Va la tercera: la emergencia no es un carnet de pertenencia. La tramposa es la primera.

Pregunta nueve. ¿Qué es la equifinalidad? Opciones: que distintos paradigmas dan el mismo resultado; que un modelo puede reproducir perfectamente los datos con reglas equivocadas; que todos los agentes terminan en el mismo estado; o que el modelo converge siempre al mismo equilibrio.

La correcta es la segunda, la crítica metodológica más seria al paradigma. ¿Las tramposas? La tercera y la cuarta, que se cuelgan del nombre.

Pregunta diez. ¿Cuál es la diferencia más defendible entre eventos discretos y agentes? Opciones: que en eventos discretos las entidades no tienen atributos; que en eventos discretos no se rutea según condiciones; dónde se ubica la lógica, en el flujo del sistema o en el individuo; o que usan software distinto.

Es la tercera. Y acá la trampa son las dos primeras, porque una entidad de eventos discretos puede tener atributos y rutearse según condiciones.

Pregunta once. Si la pregunta sobre una epidemia se responde bien con promedios, ¿qué conviene? Opciones: agentes, porque es más realista; agentes, porque representa a cada persona; dinámica de sistemas, porque es más barato y tiene menos supuestos; o da lo mismo.

Va la tercera. La tramposa es la primera: ningún paradigma es más realista por definición.

Pregunta doce. Sobre el protocolo ODD, ¿qué es correcto? Opciones: que valida el modelo; que garantiza que el modelo es bueno; que lo documenta para que otro pueda reproducirlo y discutirlo; o que tiene ocho componentes.

La correcta es la tercera: documenta, no valida. La tramposa es la cuarta, porque ocho son las filas de la ficha, y el ODD tiene siete elementos.

## Lo que puede entrar en desarrollo

Primer tema: qué es un agente. Empezá con la definición completa. Después separá el núcleo de cuatro de las propiedades frecuentes y opcionales. Seguí con las cuatro cosas que un agente no es, con un ejemplo cada una. Y cerrá con que lo define su papel: un individuo que decide por sí mismo.

Segundo tema: la emergencia. Primero, definí emergencia y el criterio para reconocerla: el test rápido y el criterio completo, remarcando que sacar una regla local y ver caer el patrón refuerza la evidencia. Después aplicalo a los tres casos, con la bandada como el que sí es emergencia. Y por último, las dos exageraciones: no es misteriosa y no es requisito.

Tercer tema: el tiempo y la activación. Arrancá desarmando la idea de que agentes es igual a incrementos fijos, y decí qué define realmente al paradigma. Después explicá el esquema sincrónico y el asincrónico con el ejemplo del contagio, y la segunda decisión del asincrónico: en qué orden actúan. Mostrá que esa elección puede cambiar el resultado: dos implementaciones del mismo modelo conceptual dan resultados distintos sin que ninguna tenga un error. Y cerrá con que es parte de la especificación, y que por eso la fila siete de la ficha no se deja en blanco.

Cuarto tema: los límites del paradigma. Primero, el costo oculto de inventar reglas difíciles de medir. Después, la equifinalidad: reproducir los datos no prueba que las reglas sean correctas. Nombrá algunas señales en contra. Y por último, el ODD, que documenta, no valida.

## Lo mínimo que te tenés que llevar

El núcleo de un agente es identidad, estado propio, autonomía y situación en un entorno. Interacción y heterogeneidad no son obligatorias.

Un agente no es necesariamente una persona, ni inteligencia artificial, ni un objeto de programación, ni una animación que camina.

Lo que define al paradigma es cómo representa el sistema, no cómo avanza el reloj.

El orden de activación es parte de la especificación y puede cambiar los resultados. La fila de tiempo y activación nunca va en blanco.

Emergencia es un patrón global sin regla global, explicable por reglas locales. No es misteriosa ni es requisito.

Ningún paradigma es más realista por definición, y reproducir los datos no prueba que las reglas sean las correctas.
