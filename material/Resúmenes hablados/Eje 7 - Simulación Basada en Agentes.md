# Eje 7. Simulación basada en agentes

Bueno, vamos con el eje siete, simulación basada en agentes. Esto te lleva unos veintitrés minutos de escucha. De este eje entra solo la teoría, casi todo en multiple choice y quizás alguna pregunta de desarrollo. El práctico de NetLogo no entra; lo nombro solo cuando ayuda. Además, el profe sacó del parcial la sección del modelo trazado a mano, es decir, todo el ejercicio de Schelling con su grilla, su tick y sus números, y todas las fórmulas de cálculo: se evalúan los conceptos. Así que eso no lo estudies. Las cuatro ideas centrales son estas: qué es un agente y qué no es; que el tiempo y el orden de activación son parte de la especificación del modelo; qué es emergencia y cómo se reconoce, con el test rápido, el criterio completo y los tres casos; y cuándo conviene usar agentes, con la equifinalidad como su crítica más seria.

## Para ubicarte

En el eje cuatro viste cuatro paradigmas: eventos discretos, dinámica de sistemas, agentes y multimétodo. Los ejes cinco y seis fueron de eventos discretos; este es el segundo paradigma.

El apunte arranca con el supermercado. Con eventos discretos respondés bien cuántas cajas hacen falta. Pero si los clientes miran las otras filas, se cambian o abandonan según su propia tolerancia, lo que importa ya no es el flujo del proceso sino lo que decide cada uno. La lógica pasó de la estructura del sistema a los individuos.

**Ojo, trampa.** El apunte no dice que eventos discretos no pueda modelar eso: dice que se puede, pero cuesta.

## Qué es un agente

### La definición

Un agente es una entidad individual identificable, con estado propio, situada en un entorno, que ejecuta reglas de comportamiento y puede percibir y afectar al entorno o a otros agentes con cierto grado de autonomía.

Individual quiere decir que no es un promedio ni un agregado. Situado quiere decir que vive en una grilla, un espacio o una red, y ese entorno define quiénes son sus vecinos. Y autonomía, que nadie le dice paso a paso qué hacer.

### Lo obligatorio y lo opcional

Esta es de las preguntas más probables. El núcleo son cuatro propiedades: identidad, estado propio, autonomía y situación en un entorno. Muy frecuentes, pero no obligatorias: reactividad, que es responder a lo que percibe, e interacción, que es influir sobre otros o intercambiar información. La heterogeneidad es frecuente, no obligatoria. Y hay tres opcionales: proactividad, que es actuar según objetivos propios; aprendizaje; y capacidad social compleja, como negociar o cooperar.

Para acordarte del núcleo, pensá en cuatro preguntas: quién es, qué tiene, dónde está y si se maneja solo.

**Lo importante.** Un modelo perfectamente válido puede no tener ninguna de las otras seis propiedades. Según el apunte, muchos malentendidos vienen de exigirle a todo agente cosas que solo tienen algunos.

**Ojo, trampa.** Tres suenan obligatorias y no lo son. La interacción es muy frecuente, no núcleo. La heterogeneidad parece la esencia del paradigma, pero es frecuente, no obligatoria. Y el aprendizaje es opcional.

### Cuatro cosas que un agente no es

No es necesariamente una persona: puede ser un vehículo, un router, una empresa, una célula o un proceso.

No es inteligencia artificial. Los modelos más famosos usan agentes con una regla de dos líneas. Un agente puede ser deliberadamente tonto, y si de reglas triviales sale un comportamiento colectivo complejo, el hallazgo es más fuerte, no más débil.

No es lo mismo que un objeto de programación. Se implementa como objeto, pero lo que lo define es su papel en el modelo: un individuo activo que decide por sí mismo.

Y no es una persona animada en pantalla. Lo que importa es si decide por sí mismo o si recorre un camino que le marca el proceso.

**Ojo, trampa.** Si una opción dice que reglas simples dan un hallazgo menos valioso, es falsa. Y un cliente que camina por la pantalla siguiendo la ruta del proceso no es un agente, aunque se vea como persona.

## La ficha del modelo: los ocho componentes

El modelo conceptual de un modelo de agentes son ocho preguntas, y si las respondés, está especificado. El apunte lo llama la ficha del modelo: agentes, estado, entorno, vecindad, reglas, interacción, tiempo y activación, y salidas.

En el Schelling del práctico, por ejemplo, el entorno es una grilla toroidal, la vecindad son las ocho celdas de alrededor, la interacción es indirecta, a través del espacio, porque los agentes no se comunican, y el tiempo avanza por ticks, con los insatisfechos mudándose de a uno en orden aleatorio.

**Lo importante.** La ficha es una versión reducida del protocolo ODD. Y el componente que más se olvida es el séptimo, tiempo y activación: se da por sentado que el tiempo simplemente avanza, y no es así.

### Cómo avanza el tiempo

Como en el eje cinco usaste siempre avance al siguiente evento, es fácil creer que eventos discretos usa siguiente evento y agentes usa incrementos fijos.

**Ojo, trampa.** Esa idea es falsa, y el apunte la plantea justamente para desarmarla. Es cierto que la mayoría de los modelos de agentes avanzan por pasos fijos, llamados ticks, y que la mayoría de los de eventos discretos van al siguiente evento. Pero es una tendencia, no una definición. Hay modelos de agentes que agendan eventos futuros, y plataformas de agentes construidas sobre un motor de eventos discretos.

**Lo importante.** Lo que define a la simulación basada en agentes no es cómo avanza el reloj, sino cómo se representa el sistema: individuos explícitos, con estado propio, reglas locales e interacción. El mecanismo temporal es una decisión de implementación posterior.

### El orden de activación

Imaginá un modelo de contagio. En este tick, A contagia a B. ¿Puede B contagiar a C en el mismo tick? Depende de una decisión explícita.

En el esquema sincrónico, todos calculan su nuevo estado con el estado del tick anterior, y después se actualizan todos juntos. B se enferma al final del tick y contagia a C recién en el siguiente.

En el asincrónico, o secuencial, los agentes actúan de a uno y cada uno ve los cambios de los anteriores. Si B actúa después de A, puede contagiar a C en el mismo tick. Y aparece una segunda decisión: en qué orden actúan, siempre el mismo o al azar en cada tick.

**Lo importante.** No es un detalle de programación: es parte de la especificación y puede cambiar los resultados. Si dos personas implementan el mismo modelo conceptual, una sincrónica y otra secuencial, obtienen resultados distintos sin que ninguna haya cometido un error. La diferencia está en un supuesto que nunca se escribió. Por eso el apunte lo conecta con la verificación de los ejes cuatro y seis, y dice que la fila siete de la ficha no se puede dejar en blanco.

**Ojo, trampa.** Te pueden dar vuelta los esquemas: contagiar en el mismo tick solo es posible en el asincrónico, y solo si B actúa después de A. Y si una opción atribuye la diferencia de resultados a un error de implementación, es falsa.

## Emergencia

Es el concepto central de la unidad y la razón más fuerte para usar el paradigma. Emergencia es la aparición de una regularidad o estructura a nivel global que no fue programada como regla global, sino que resulta de la interacción repetida de reglas locales. El modelador programa cómo actúa cada individuo; no programa «formen una bandada».

### El test rápido y el criterio completo

El test rápido: ¿existe en el modelo una instrucción que ordene directamente el patrón que observo? Si es que sí, no hay emergencia, hay una regla global disfrazada. Si es que no y el patrón aparece igual, tenés un candidato.

El criterio completo: un patrón es emergente cuando aparece a nivel global sin una regla global que lo imponga y puede explicarse como resultado acumulado de reglas e interacciones locales. La evidencia se refuerza si, al modificar o eliminar una regla local, el patrón cambia o desaparece. Esa es la parte operativa.

### Los tres casos

Caso uno, no es emergencia. Una instrucción manda, en el tick cincuenta, a todos los agentes del tipo A hacia la izquierda, y aparece segregación perfecta. Lo ordenó una regla global: el test rápido lo descarta.

Caso dos, todavía no alcanza. Al inicializar al azar, por casualidad quedan siete azules juntos en un rincón. Nadie lo ordenó, así que pasa el test rápido, pero no es emergencia: lo produjo el sorteo inicial, no la dinámica. Un patrón emergente tiene que aparecer con las corridas, no venir dado.

Caso tres, sí es emergencia. Cada pájaro aplica tres reglas mirando a sus vecinos cercanos: no chocarse, apuntar hacia donde apuntan ellos y no quedarse solo. Aparece una bandada coordinada, sin líder. Pasa el test rápido, y si desactivás la regla de alineación la bandada se deshace: cumple el criterio completo.

**Ojo, trampa.** El caso dos es el tramposo. Que nadie lo haya ordenado no alcanza: el test rápido te da un candidato, no una confirmación. Y no es una regla global disfrazada; eso es el caso uno.

### Las dos exageraciones

La primera es tratar la emergencia como algo misterioso o inexplicable; en modelos simples se puede analizar perfectamente. La segunda es convertirla en requisito, creer que si un modelo no muestra emergencia no es de agentes. No hay acuerdo en la literatura sobre eso. Como dice el apunte, es una razón poderosa para usar el paradigma, no un carnet de pertenencia.

**Si te toca de desarrollo.** Dá la definición. Explicá el test rápido y el criterio completo, remarcando que sacar una regla y ver caer el patrón refuerza la evidencia. Aplicalo a los tres casos. Y cerrá con las dos exageraciones: no es misteriosa y no es requisito.

## Cuándo conviene usar agentes y cuándo no

### Frente a eventos discretos

En eventos discretos la entidad recorre un flujo definido en el modelo, la lógica está en la estructura del proceso y la pregunta típica es de espera, utilización y capacidad. En agentes, la entidad ejecuta su propio comportamiento, la lógica está en las reglas locales del individuo, la heterogeneidad suele ser central, la vecindad o la red son explícitas, y la pregunta típica es de difusión, interacción, adaptación, de cómo lo micro produce lo macro.

**Ojo, trampa.** El apunte advierte que esto es una guía de modelado, no una frontera informática. Una entidad de eventos discretos puede llevar atributos, rutearse según condiciones y disparar eventos; y un agente puede tener una regla trivial.

**Lo importante.** La diferencia más defendible es dónde se ubica la lógica: en el flujo del sistema, o en el individuo que dice «mi estado es X, percibo Y, por eso hago Z».

Un mismo sistema, como el supermercado o una red de datos, admite las dos miradas, y ninguna es más correcta. Eventos discretos pregunta cuánto; agentes pregunta qué pasa si los individuos se comportan distinto entre sí.

### Frente a dinámica de sistemas

Dinámica de sistemas, el eje ocho, trabaja con niveles agregados, flujos y bucles de realimentación. Agentes trabaja con individuos explícitos, observa al individuo y al agregado a la vez, y es más costoso. En una epidemia, dinámica de sistemas usa susceptibles, infectados y recuperados con tasas promedio; con agentes, cada persona tiene sus contactos, y la curva aparece de los contagios individuales.

**Ojo, trampa.** Ninguno es más realista por definición. Si la pregunta se responde con promedios, dinámica de sistemas es mejor, porque es más barato y tiene menos supuestos.

### Señales a favor y en contra

A favor de agentes: importa la heterogeneidad; importa quién interactúa con quién; hay decisiones locales con información parcial; hay adaptación o aprendizaje; se quiere explicar un patrón macro desde reglas micro; o una política actúa sobre subgrupos distintos.

En contra: la pregunta es de capacidad o colas y eventos discretos la resuelve; dinámica de sistemas responde lo mismo con menos supuestos; no hay evidencia para justificar las reglas individuales; se representan miles de individuos solo para mirar un promedio; o el detalle micro no cambia la decisión.

**Si te toca de desarrollo.** Ubicá la diferencia de fondo con eventos discretos, que es dónde está la lógica. Marcá el contraste con dinámica de sistemas, individuos contra agregados. Mostrá un mismo sistema mirado de dos formas, como la epidemia. Nombrá algunas señales a favor y en contra. Y cerrá con que ninguno es más realista por definición: decide la pregunta.

### El costo oculto: la equifinalidad

Un modelo de agentes obliga a inventar reglas de comportamiento, mucho más difíciles de medir que un tiempo de servicio. Y un modelo puede reproducir perfectamente los datos con reglas equivocadas. Eso es la equifinalidad, y el apunte la llama la crítica metodológica más seria al paradigma.

**Ojo, trampa.** Si una opción dice que, como el modelo reproduce bien los datos, sus reglas quedan validadas, esa es la trampa. Y no te guíes por el nombre: no habla de agentes que terminan en el mismo estado.

## Áreas de aplicación

Lo que hace apropiado al paradigma no es el dominio, sino que la pregunta dependa de la interacción y de las diferencias entre individuos. Cerca de la carrera: redes de computadoras, sistemas distribuidos, ciberseguridad y usuarios de una plataforma.

**Ojo, trampa.** «La epidemiología se modela siempre con agentes» es falso: no decide el dominio, decide la pregunta.

## Anexos: historia, herramientas y ODD

### Historia y herramientas

Tres hitos: Schelling en 1971, a mano; Reynolds y las bandadas de los boids en 1987; y NetLogo, de Wilensky, en 1999.

La elección del paradigma es previa a la elección de la herramienta. NetLogo es el entorno de agentes más usado en enseñanza, libre y gratuito. Su vocabulario mínimo: turtle, un agente móvil; patch, una celda fija, que también tiene estado y puede ejecutar reglas; link, una conexión entre agentes; observer, el nivel global que crea agentes y mide; y tick, un paso de tiempo.

FlexSim también hace agentes: desde 2020 incluye Agent System. Pero su propia documentación aclara que se relaciona estrechamente, aunque no exactamente, con el modelado basado en agentes de la literatura. Y AnyLogic es multimétodo real, con los tres paradigmas en un mismo modelo.

**Ojo, trampa.** «FlexSim es solo de eventos discretos» es falso: ningún software pertenece para siempre a un solo paradigma. Pero tampoco hacés agentes en FlexSim por poner personas que caminan: hay que construir el comportamiento desde el individuo.

### El protocolo ODD

ODD viene de Overview, Design concepts, Details. Nació en ecología porque los modelos publicados se describían tan incompletos que era imposible reproducirlos, y su versión vigente es de 2020. Tiene siete elementos en tres bloques. Overview: propósito; entidades, variables de estado y escalas; y visión general del proceso y programación, que es qué pasa en cada paso y en qué orden actúan los agentes. Design concepts: los conceptos de diseño, como emergencia, adaptación, aprendizaje, percepción, interacción, estocasticidad y observación. Details: inicialización, datos de entrada y submodelos.

**Lo importante.** Los tres elementos de Overview son, esencialmente, las ocho filas de la ficha. Lo que agrega el ODD es el bloque de conceptos de diseño, que obliga a declarar cosas que de otro modo quedan implícitas.

**Ojo, trampa.** ODD documenta, no valida. Un modelo puede estar impecablemente descripto y ser un mal modelo; el protocolo sirve para que otro lo reproduzca y lo discuta. Y no mezcles los números: la ficha tiene ocho componentes; el ODD, siete elementos en tres bloques.

## Preguntas tipo multiple choice

Pregunta uno. ¿Cuál pertenece al núcleo obligatorio de un agente? Opciones: aprendizaje, heterogeneidad, autonomía o proactividad. La correcta es autonomía: el núcleo es identidad, estado propio, autonomía y situación en un entorno. El distractor tramposo es heterogeneidad, que parece esencial pero es frecuente, no obligatoria.

Pregunta dos. ¿Qué afirmación sobre los agentes es correcta? Opciones: que tiene que representar a una persona; que necesita algo de inteligencia artificial; que puede tener una sola regla trivial y el modelo seguir siendo valioso; o que toda entidad que se mueve en pantalla es un agente. La correcta es la tercera: con reglas triviales, el hallazgo es más fuerte. El distractor tramposo es el de inteligencia artificial.

Pregunta tres. ¿Qué define a la simulación basada en agentes? Opciones: avanzar por incrementos fijos; programarse en NetLogo; representar el sistema con individuos explícitos, con estado propio, reglas locales e interacción; o producir siempre emergencia. La correcta es la tercera. El distractor tramposo es incrementos fijos, que es una tendencia, no una definición.

Pregunta cuatro. A contagia a B en el tick actual. Con activación sincrónica, ¿cuándo puede B contagiar a C? Opciones: en el mismo tick; en el tick siguiente; según el orden aleatorio; o nunca. La correcta es en el tick siguiente, porque todos calculan con el estado anterior y se actualizan juntos. El distractor tramposo es en el mismo tick, que corresponde al asincrónico cuando B actúa después de A.

Pregunta cinco. Dos personas implementan el mismo modelo conceptual, una con activación sincrónica y otra secuencial, y obtienen resultados distintos. ¿Por qué? Opciones: una cometió un error de programación; es ruido que se arregla con más réplicas; hay un supuesto que no se escribió, el de tiempo y activación; o el modelo no es válido. La correcta es la tercera. El distractor tramposo es el error de programación: el apunte aclara que ninguna se equivocó.

Pregunta seis. Al inicializar al azar, quedan siete azules juntos en un rincón, sin que nadie lo ordene. ¿Es emergencia? Opciones: sí, porque no hay regla global; no, porque es una regla global disfrazada; no, porque lo produjo el sorteo inicial y no la dinámica; o sí, pero débil. La correcta es la tercera. El distractor tramposo es la primera: pasar el test rápido solo te da un candidato.

Pregunta siete. ¿Qué refuerza la evidencia de que un patrón es emergente? Opciones: que sea sorprendente; que no se pueda explicar desde las reglas; que al modificar o eliminar una regla local el patrón cambie o desaparezca; o que aparezca desde el primer tick. La correcta es la tercera. El distractor tramposo es la segunda, que es la exageración de la emergencia misteriosa.

Pregunta ocho. Un modelo hecho con agentes no muestra ningún patrón emergente. ¿Qué se puede decir? Opciones: que no es un modelo de agentes; que en realidad es de eventos discretos; que puede ser un modelo de agentes correctamente construido; o que está mal verificado. La correcta es la tercera: la emergencia no es un carnet de pertenencia. El distractor tramposo es la primera.

Pregunta nueve. ¿Qué es la equifinalidad? Opciones: que distintos paradigmas dan el mismo resultado; que un modelo puede reproducir perfectamente los datos con reglas equivocadas; que todos los agentes terminan en el mismo estado; o que el modelo converge siempre al mismo equilibrio. La correcta es la segunda, la crítica metodológica más seria al paradigma. Los distractores tramposos son la tercera y la cuarta, que se cuelgan del nombre.

Pregunta diez. ¿Cuál es la diferencia más defendible entre eventos discretos y agentes? Opciones: que en eventos discretos las entidades no tienen atributos; que en eventos discretos no se rutea según condiciones; dónde se ubica la lógica, en el flujo del sistema o en el individuo; o que usan software distinto. La correcta es la tercera. Las dos primeras son la trampa: una entidad de eventos discretos puede tener atributos y rutearse según condiciones.

Pregunta once. Si la pregunta sobre una epidemia se responde bien con promedios, ¿qué conviene? Opciones: agentes, porque es más realista; agentes, porque representa a cada persona; dinámica de sistemas, porque es más barato y tiene menos supuestos; o da lo mismo. La correcta es la tercera. El distractor tramposo es la primera: ningún paradigma es más realista por definición.

Pregunta doce. Sobre el protocolo ODD, ¿qué es correcto? Opciones: que valida el modelo; que garantiza que el modelo es bueno; que documenta el modelo para que otro pueda reproducirlo y discutirlo; o que tiene ocho componentes. La correcta es la tercera: documenta, no valida. El distractor tramposo es la cuarta: ocho son las filas de la ficha, y el ODD tiene siete elementos.

## Lo que puede entrar en desarrollo

Primer tema: qué es un agente. Empezá con la definición completa. Separá el núcleo de cuatro de las propiedades frecuentes y opcionales. Seguí con las cuatro cosas que un agente no es, con un ejemplo cada una. Y cerrá con que lo define su papel: un individuo que decide por sí mismo.

Segundo tema: la emergencia. Definí emergencia y el criterio para reconocerla: el test rápido y el criterio completo, remarcando que sacar una regla local y ver caer el patrón refuerza la evidencia. Aplicalo a los tres casos, con la bandada como el caso que sí es emergencia. Y cerrá con las dos exageraciones: no es misteriosa y no es requisito.

Tercer tema: el tiempo y la activación. Desarmá la idea de que agentes es igual a incrementos fijos y decí qué define realmente al paradigma. Explicá el esquema sincrónico y el asincrónico con el ejemplo del contagio, y la segunda decisión del asincrónico: en qué orden actúan. Mostrá que esa elección puede cambiar el resultado: dos implementaciones del mismo modelo conceptual dan resultados distintos sin que ninguna tenga un error. Y cerrá con que es parte de la especificación y por eso la fila siete de la ficha no se deja en blanco.

Cuarto tema: los límites del paradigma. Explicá el costo oculto de inventar reglas difíciles de medir. Definí equifinalidad: reproducir los datos no prueba que las reglas sean correctas. Nombrá algunas señales en contra. Y cerrá con el ODD, que documenta, no valida.

## Lo mínimo que te tenés que llevar

El núcleo de un agente es identidad, estado propio, autonomía y situación en un entorno. Interacción y heterogeneidad no son obligatorias.

Un agente no es necesariamente una persona, ni inteligencia artificial, ni un objeto de programación, ni una animación que camina.

Lo que define al paradigma es cómo representa el sistema, no cómo avanza el reloj.

El orden de activación es parte de la especificación y puede cambiar los resultados. La fila de tiempo y activación nunca va en blanco.

Emergencia es un patrón global sin regla global, explicable por reglas locales. No es misteriosa ni es requisito.

Ningún paradigma es más realista por definición, y reproducir los datos no prueba que las reglas sean las correctas.
