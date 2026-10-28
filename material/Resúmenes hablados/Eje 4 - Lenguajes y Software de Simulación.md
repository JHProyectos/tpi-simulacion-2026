# Eje 4. Lenguajes y software de simulación

Vamos con el eje cuatro. Este audio dura unos treinta minutos.

Arranco con una buena noticia: el profe recortó este eje. Sacó de la evaluación los lenguajes clásicos y lo que aportó cada uno, los lenguajes de hoy como bibliotecas sobre lenguajes de propósito general, el panorama de herramientas, y los dos complementos: el de la evolución de los lenguajes y el software, y el de los criterios para elegir una herramienta. Eso no lo estudies; ya lo saqué de este resumen.

Lo que entra es la teoría, casi toda en multiple choice. Así que vamos derecho a lo preguntable y a las trampas.

Son cuatro ideas centrales. La primera: el eje agrega el motor de tiempo. El reloj salta al siguiente evento, y todo simulador repite el mismo ciclo. La segunda: hay dos visiones del mundo, eventos y procesos, y por debajo los procesos corren sobre un motor de eventos. La tercera: cada herramienta tiene su paradigma, y el paradigma se elige al modelar, no al elegir el software. Y la cuarta, la que más se confunde: verificar no es validar.

## Dónde está parado este eje

¿Te acordás de las diez etapas del estudio de simulación, del eje uno? La cuarta es el desarrollo del modelo de simulación: traducir el modelo conceptual a un modelo computarizado. De eso trata este eje.

El eje dos te dio la aleatoriedad. El eje tres, las transformaciones y Monte Carlo, que es estático: no tiene tiempo. ¿Qué falta, entonces? Justamente el tiempo. Esa es la tercera pieza que agrega el eje cuatro: el motor de tiempo.

Y una frase del apunte: todo lo que no se traduce no existe en el modelo. Si el cajero se toma un descanso y nadie lo codificó, el simulador te da resultados prolijísimos de un sistema que no es el tuyo.

**Lo importante.** Eje dos, aleatoriedad. Eje tres, transformación. Eje cuatro, tiempo.

**Ojo, trampa.** Si te dicen que Monte Carlo ya es una simulación dinámica: falso, es estática. Y si te dicen que el eje cuatro aporta la aleatoriedad: también falso, eso es del eje dos.

## Los componentes de un modelo ejecutable

Casi todo modelo de eventos discretos usa las mismas piezas. El ejemplo es la caja de un minimercado, y vamos por grupos.

Primero, los protagonistas. La entidad es el objeto que circula y sobre el que ocurren las cosas: se crea, se mueve y se destruye. Acá, cada cliente. El atributo es un dato propio de cada entidad: su hora de llegada, su prioridad.

Segundo, lo que se disputan. El recurso es el medio limitado que las entidades necesitan: el cajero, que puede estar libre, ocupado, en falla o fuera de turno. La cola es donde esperan las que todavía no pueden avanzar, con una disciplina que decide a quién le toca. Acá es FIFO: el primero que llega es el primero que se atiende.

Tercero, cómo se describe el sistema. La variable de estado es un dato global que describe al sistema en un instante: cuántos hay en la fila, si el cajero está ocupado. Y el evento es un suceso instantáneo que cambia ese estado: una llegada, un fin de atención.

Cuarto, el tiempo. El reloj de simulación guarda el tiempo simulado actual, que no tiene nada que ver con el tiempo real de ejecución: un año de una planta se puede simular en cuarenta segundos. Y la lista de eventos futuros es la agenda, ordenada por tiempo, de los eventos ya programados que todavía no ocurrieron. Es la estructura central del simulador.

Y por último, los resultados. Los acumuladores estadísticos son sumas y contadores que se actualizan durante la corrida. La réplica es una corrida completa del modelo; como el modelo es estocástico, una sola no alcanza.

Abajo lo tenés dibujado.

![Componentes del modelo en la caja del minimercado](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje4-componentes.svg)

*Figura 1. La caja del minimercado con sus componentes: cliente y atributos, fila, cajero, eventos, variables de estado, reloj y lista de eventos futuros.*

**Lo importante.** Reconocer cada componente por su definición, sobre todo evento, reloj, lista de eventos futuros y réplica.

**Ojo, trampa.** Acá hay tres confusiones que el multiple choice adora, así que vamos una por una.

La primera: atributo contra variable de estado. Imaginate que cada cliente lleva una etiqueta colgada. Lo que dice esa etiqueta, su hora de llegada o su prioridad, es un atributo: es de él y viaja con él. La variable de estado, en cambio, no es de nadie en particular: es del sistema entero. ¿Cuánta gente hay en la fila? Eso no lo sabe ningún cliente por su cuenta; es una foto de todo el sistema. Así que si una opción te dice que la cantidad de gente en la fila es un atributo, ya sabés: es falsa.

La segunda: la cola contra la lista de eventos futuros. Se mezclan porque en las dos hay algo esperando. Pero en la cola esperan clientes, haciendo fila para pagar. En la lista de eventos futuros esperan cosas que todavía no pasaron: la próxima llegada, el próximo fin de atención. Y si te preguntan cuál es la estructura central del simulador, es la lista, no la cola.

Y la tercera, que es la más traicionera: el evento es instantáneo. Pasa en un momento y listo. Entonces, ¿la atención es un evento? No, porque la atención dura. Lo que sí son eventos son los instantes en que algo cambia: cuando llega el cliente y cuando termina de atenderse. Si te sirve, pensalo como un video: el evento es un fotograma, no la escena.

## El motor de tiempo

### Dos maneras de mover el reloj

La primera manera son los incrementos fijos de tiempo. El reloj avanza siempre el mismo paso y en cada paso revisa si pasó algo, como un sereno que hace la ronda cada media hora, pase algo o no. Se usa en sistemas continuos, donde el estado cambia todo el tiempo y se integran ecuaciones paso a paso. Es lo del eje ocho.

La segunda es el avance al siguiente evento. El reloj salta directo al próximo evento programado. ¿Por qué puede saltar? Porque entre evento y evento, por definición, no cambia nada. Es el mecanismo dominante en eventos discretos: en la caja, recalcular el estado segundo a segundo durante ocho horas no tendría sentido.

**Lo importante.** Incremento fijo va con continuo; siguiente evento va con discreto. ¿La razón? La eficiencia. Eso sí, tomalo como la asociación típica, no como una definición: en el eje siete vas a ver que los modelos de agentes suelen avanzar por pasos fijos sin ser continuos, y el apunte pone esa confusión como trampa.

**Ojo, trampa.** Que te crucen los pares. O que te digan que entre dos eventos el estado cambia de a poco: entre eventos no cambia nada.

### El ciclo de ejecución

Esto es de lo más preguntable del eje. Todo simulador de eventos discretos, sin importar marca ni lenguaje, repite seis pasos.

Primero, la inicialización: reloj y acumuladores en cero, estado inicial, y se programan los primeros eventos, típicamente la primera llegada.

Segundo, la selección del próximo evento: el de menor tiempo en la lista de eventos futuros, que se saca de la lista.

Tercero, el avance del reloj hasta ese instante.

Cuarto, la ejecución de la rutina del evento: cambia el estado, se mueven entidades y se programan los eventos que se desprenden.

Quinto, la actualización de estadísticas.

Y sexto, el control de fin. Si se cumplió la condición de corte, se emite el reporte; si no, se vuelve al paso dos. El corte puede ser el tiempo final, una cantidad de entidades procesadas o la lista de eventos vacía.

Pensalo como un secretario con su agenda: mira la próxima cita, adelanta el reloj y la atiende. Anota las citas nuevas que salen de ahí, toma nota de cómo le fue y, si no es hora de cerrar, vuelve a la agenda. Abajo lo tenés dibujado.

![Ciclo del motor de eventos alrededor de la lista de eventos futuros](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje4-motor-eventos.svg)

*Figura 2. El ciclo de ejecución: tras la inicialización, cinco pasos giran alrededor de la lista de eventos futuros hasta cumplir el corte.*

Y falta la regla de desempate, que el multiple choice adora. Si dos eventos caen en el mismo instante, hace falta una regla explícita, porque el resultado puede cambiar. La convención más habitual, y la que usa la cátedra, es procesar primero los fines de servicio y después las llegadas. Así el cajero se libera antes de que el cliente nuevo pregunte si está libre. Como en el ascensor: primero se baja, después se sube.

**Lo importante.** El orden de los pasos, que se elige el evento de menor tiempo, y la regla de desempate.

**Ojo, trampa.** Tres. La primera: que inviertan los pasos dos y tres. Primero se elige el evento y después se mueve el reloj; si no, ¿hasta dónde lo moverías? La segunda: que el próximo evento sea el primero que se programó. No, es el de menor tiempo: en la agenda manda la hora de la cita, no cuándo la anotaste. Y la tercera: en el empate, que primero van las llegadas o que el orden no importa.

**Si te toca de desarrollo.** Justificá el siguiente evento frente al incremento fijo. Recorré los seis pasos, con la lista de eventos futuros como estructura central. Y cerrá con las condiciones de corte y el desempate.

## Lenguajes de simulación

En los años cincuenta todo se programaba en lenguajes de propósito general, como FORTRAN, ALGOL y más tarde C. ¿El problema? En cada proyecto el analista reescribía la agenda, el reloj, las colas y las estadísticas.

De ahí nace el lenguaje de simulación: un lenguaje cuyas construcciones básicas corresponden directamente a los conceptos del modelado, como entidades, recursos, colas, eventos y avance del reloj. En vez de escribir «insertar un registro en una lista ordenada por tiempo», escribís «programar el fin de servicio dentro de cuatro minutos».

La frase clave: el motor viene incorporado; no lo escribe el usuario. ¿Qué ganás? Un modelo más corto y con menos errores. ¿Qué pagás? Cierta pérdida de libertad.

**Lo importante.** La definición y su frase clave: el motor viene incorporado.

**Ojo, trampa.** Que en un lenguaje de simulación el usuario programa la agenda: falso. Que da más libertad que un lenguaje de propósito general: es al revés.

## Las visiones del mundo

Prestá atención, porque según el apunte este es el punto realmente conceptual del eje: el mismo sistema se puede describir de dos maneras, que dieron origen a dos familias de lenguajes. Se llaman visiones del mundo.

### Orientación a eventos

El modelo se organiza alrededor de los eventos: una rutina por tipo de evento, que dice qué cambia y qué eventos nuevos se programan.

En el minimercado, la rutina de llegada primero programa la próxima llegada. Después, si el cajero está libre, lo ocupa y programa el fin de atención; si no, el cliente va a la fila. La de fin de atención libera al cajero o toma al siguiente de la fila.

¿Notaste algo? El cliente no es protagonista. El modelo es una colección de reacciones del sistema, como el manual de un empleado de guardia: si pasa esto, hacé aquello.

Es insuperable para entender un simulador por dentro. Pero con veinte tipos de eventos entrelazados, se vuelve difícil de seguir.

### Orientación a procesos

Acá el modelo se organiza alrededor del ciclo de vida de la entidad. Escribís la historia del cliente: llega, toma el cajero, espera si está ocupado, se hace atender, lo libera y se va. Se lee como el enunciado.

¿Y el reloj, la agenda y la fila? No aparecen. La fila surge sola, porque varios procesos quedan suspendidos en tomar el cajero.

Las instrucciones clave son las que suspenden el proceso. Demorar lo duerme un tiempo conocido, como una alarma: sabés cuándo te despertás. Tomar lo duerme un tiempo desconocido, hasta que el recurso esté disponible, como esperar que se libere el baño: sabés qué esperás, pero no cuánto.

### Las dos visiones, comparadas

Vamos punto por punto.

¿El protagonista? En eventos, el sistema, que reacciona. En procesos, la entidad, que actúa.

¿El reloj y la agenda? En eventos son explícitos: los programa el modelador. En procesos son implícitos: los resuelve el lenguaje.

¿La fortaleza? Eventos da control total y máxima eficiencia. Procesos, legibilidad y rapidez de construcción.

¿La debilidad? Eventos se vuelve difícil de seguir en modelos grandes. Procesos tiene menos control fino en casos muy particulares.

¿Ejemplos? De eventos, SIMSCRIPT y los modelos escritos a mano en C, Java o Python. De procesos, GPSS, SIMULA, SimPy y casi todos los simuladores visuales.

Y lo que el apunte marca como lo más importante: las visiones no compiten, describen el mismo sistema desde distinta altura. Por debajo, un lenguaje de procesos se ejecuta con un motor de eventos. Demorar cuatro es, para el motor, programar el evento reanudar este proceso en reloj más cuatro. Procesos es una interfaz más cómoda sobre el mismo motor. Como un auto automático: vos no hacés los cambios, pero la caja de cambios sigue ahí abajo.

### La tercera visión: objetos

La orientación a objetos no reemplaza a las otras dos: las envuelve. Cada máquina u operario es un objeto con sus datos, su estado y su comportamiento, que se comunica con los demás.

Y el dato que más se pregunta: la programación orientada a objetos nació dentro de la simulación. SIMULA, de mediados de los sesenta, introdujo clase, objeto y herencia, que después pasaron a C más más, Java y Python.

Por eso hoy, al arrastrar un procesador en un simulador visual, instanciás un objeto que ya trae su cola, su recurso y sus estadísticos. Abajo tenés las tres visiones en un solo dibujo.

![Las visiones del mundo sobre un mismo motor de eventos](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje4-visiones-mundo.svg)

*Figura 3. Eventos y procesos describen el mismo sistema sobre el mismo motor de eventos, y la orientación a objetos envuelve a las dos.*

**Lo importante.** Eventos: el sistema reacciona, reloj explícito. Procesos: la entidad actúa, reloj implícito. Procesos corre sobre un motor de eventos, y objetos envuelve a las dos.

**Ojo, trampa.** La más probable de todo el eje: que procesos usa un motor distinto, o que las visiones son excluyentes. Falso. Después, que te crucen las características, como reloj explícito en procesos, o que te crucen demorar y tomar. Y por último, que la simulación tomó los objetos de C más más o de Java: fue al revés.

**Si te toca de desarrollo.** Definí visión del mundo. Explicá eventos con sus rutinas y procesos con la historia del cliente, con demorar y tomar. Compará protagonista, reloj, fortaleza y debilidad. Y cerrá con el motor de eventos por debajo y los objetos envolviendo a ambas.

## Software de simulación

### Cuatro familias de herramientas

Hay cuatro caminos para implementar un modelo. Se diferencian por cuánto trabajo hace el analista y cuánto viene resuelto. Vamos de menos a más resuelto.

Primero, el lenguaje de propósito general, como Python o Java: hay que construir todo. Flexibilidad máxima, tiempo de desarrollo muy alto.

Segundo, la biblioteca de simulación, como SimPy: aporta el motor y vos escribís la lógica en código. Flexibilidad alta, desarrollo alto.

Tercero, el lenguaje de simulación, como GPSS o SIMSCRIPT: sus primitivas ya son conceptos de simulación. Flexibilidad media alta, desarrollo medio.

Y cuarto, el simulador visual: trae motor, objetos, animación y reportes, y armás el modelo arrastrando y parametrizando. Flexibilidad media, desarrollo bajo.

¿Cuál es la mejor? Ninguna en general. Flexibilidad y velocidad de desarrollo son inversas: cuanto más resuelto viene, más rápido modelás y menos podés salirte del molde. Como con la comida: cuanto más lista viene, más rápido comés, pero menos podés cambiar la receta.

Un matiz: como los simuladores visuales traen lenguajes internos, la frontera entre la tercera y la cuarta familia es porosa. Abajo tenés las cuatro en fila.

![Las cuatro familias de herramientas según flexibilidad y tiempo de desarrollo](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje4-familias-herramientas.svg)

*Figura 4. Las cuatro familias de herramientas: cuanto más resuelto viene, menos flexibilidad y menos tiempo de desarrollo.*

**Lo importante.** El orden de las cuatro familias y la relación inversa entre flexibilidad y velocidad.

**Ojo, trampa.** Que el simulador visual siempre es la mejor opción: no hay opción universalmente mejor. Que los simuladores visuales no permiten programar: falso. Y no cruces los niveles: la biblioteca tiene flexibilidad alta; el lenguaje de simulación, media alta.

### No todo el software simula lo mismo

El apunte marca como error frecuente pedirle a una herramienta lo que su paradigma no puede representar. Es como pedirle a una balanza la temperatura. Veamos los paradigmas.

Primero, eventos discretos: entidades individuales que compiten por recursos, y el estado cambia en instantes puntuales. Responde cuánto se espera o dónde está el cuello de botella. Eje cinco y trabajo integrador.

Segundo, dinámica de sistemas, o simulación continua: niveles y flujos con bucles de realimentación y ecuaciones integradas paso a paso. No hay individuos. Pensá en un tanque que se llena y se vacía: importa cuánta agua hay, no cada gota. Responde cómo evoluciona una población o un stock. Eje ocho.

Tercero, basada en agentes: individuos autónomos con reglas propias, y el comportamiento global emerge de sus interacciones. Como una bandada de pájaros: cada uno sigue sus reglas, y la forma de la bandada aparece sola. Responde cómo se difunde una epidemia o una conducta. Eje siete.

Y cuarto, multimétodo o híbrido: combina los anteriores. En la materia solo se menciona.

La advertencia: elegir el paradigma es una decisión de modelado, no de software. Se toma al formular el modelo conceptual, y si no corresponde al problema, ninguna herramienta lo arregla.

**Lo importante.** Cada paradigma se define por cómo representa el sistema, y se elige al modelar.

**Ojo, trampa.** Dinámica de sistemas con individuos, o agentes con un comportamiento global programado en lugar de emergente. Y sobre todo, que el paradigma se elige según el software disponible.

**Si te toca de desarrollo.** Definí los tres paradigmas principales con una pregunta típica de cada uno. Nombrá el híbrido. Y cerrá con que la elección es de modelado: si el paradigma no corresponde al problema, ninguna herramienta lo arregla.

### Qué resuelve el software y qué sigue siendo tuyo

El software resuelve lo mecánico. Primero, la agenda de eventos y el reloj. Después, los generadores pseudoaleatorios del eje dos y la generación de variables del eje tres. También las colas y recursos, las estadísticas, la animación y los reportes. Y por último, las réplicas y experimentos.

Lo tuyo es lo conceptual. Primero, formular el problema. Después, analizar los datos de entrada para decidir qué distribución representa a las llegadas, que es del eje seis. Y además, el modelo conceptual, la verificación, la validación y el diseño de experimentos.

Es como una calculadora: hace las cuentas perfecto, pero no sabe qué cuenta hacer.

Un puente con lo anterior: cuando configurás una llegada exponencial, la herramienta usa un generador congruencial y un método de transformación. Los ejes dos y tres sirven para juzgar si está bien usada.

**Lo importante.** La herramienta automatiza lo mecánico; lo conceptual es del analista.

**Ojo, trampa.** Que el software elige la distribución de entrada, verifica o valida. Genera la distribución que vos elegiste, pero no la elige.

## Implementación y verificación

### Verificación

Una vez armado el modelo en la herramienta, con objetos como fuente, cola, procesador o sumidero, hay que verificarlo.

Verificar es comprobar que el modelo implementado hace lo que quisimos: que la traducción del conceptual al computacional fue correcta. Como revisar una traducción contra el original. Es puramente interna y ninguna herramienta la hace sola.

Las técnicas son siete.

Primero, correr con valores determinísticos: reemplazás las distribuciones por constantes y predecís el resultado a mano.

Segundo, revisar la traza de eventos.

Tercero, mirar la animación.

Cuarto, probar valores extremos, como un recurso de capacidad cero.

Quinto, verificar la conservación de entidades: las creadas tienen que igualar a las que salieron más las que quedaron. Es un arqueo de caja: si no cierra, algo se perdió o se contó dos veces.

Sexto, contrastar con un caso de solución conocida, como uno de teoría de colas.

Y séptimo, la revisión por otra persona.

La advertencia: la animación es ayuda, no prueba. Lo que se ve bien no está necesariamente bien.

**Lo importante.** Es interna, no la hace la herramienta y tiene técnicas concretas.

**Ojo, trampa.** Que la animación prueba que el modelo es correcto, o que el simulador verifica solo: falso. Y correr con valores determinísticos no es lo mismo que fijar la semilla. Con la semilla fija sigue habiendo azar, solo que repetido; con constantes, no hay azar.

### Verificar no es validar

El apunte dice que se confunden permanentemente, así que vamos a fijarlo.

La verificación pregunta: ¿construimos bien el modelo? Compara el modelo implementado contra el conceptual, y es interna, lógica y de programación. Ejemplo de falla: la regla de prioridad quedó al revés en el código.

La validación pregunta: ¿construimos el modelo correcto? Compara el modelo contra el sistema real, y es externa, estadística y de criterio experto. Ejemplo de falla: el modelo asume llegadas parejas y en la realidad hay un pico al mediodía.

Pensalo con un mapa. Verificar es controlar que el mapa impreso sea igual al borrador. Validar es salir a la calle y ver si coincide con la ciudad. Por eso un modelo puede estar perfectamente verificado y ser completamente inválido. La validación se ve en el eje seis.

**Lo importante.** Construir bien el modelo es verificar. Construir el modelo correcto es validar.

**Ojo, trampa.** Te cruzan los ejemplos: la prioridad invertida es de verificación; el pico del mediodía, de validación. Y la frase «si está verificado, es válido» es falsa.

**Si te toca de desarrollo.** Definí cada una con su pregunta, qué compara y su naturaleza. Dá un ejemplo de falla de cada una. Nombrá técnicas de verificación. Y cerrá con que verificado no implica válido.

### Semillas, réplicas y reproducibilidad

Como el modelo es estocástico, cada corrida da un resultado distinto. Eso pide tres cuidados.

El primero: fijar la semilla para reproducir exactamente una corrida, al depurar o para que otro obtenga los mismos números. Lo que no se puede reproducir no se puede discutir.

El segundo: correr varias réplicas con semillas distintas para estimar un indicador. Una sola corrida no dice casi nada, como juzgar un restaurante por una sola visita.

Y el tercero: usar corrientes separadas para cada fuente de aleatoriedad, que permite comparar escenarios con la misma suerte. Es la técnica de números aleatorios comunes, de reducción de varianza, del eje seis. Como probar dos recorridos con el mismo tránsito: si uno gana, fue por el recorrido y no por la suerte.

**Lo importante.** Semilla fija para reproducir, semillas distintas para estimar, corrientes separadas para comparar.

**Ojo, trampa.** Réplicas con la misma semilla para estimar: repetirías la misma corrida. Y los números aleatorios comunes son para comparar escenarios.

**Si te toca de desarrollo.** Explicá por qué un modelo estocástico obliga a cuidar la aleatoriedad. Desarrollá los tres cuidados con su propósito: reproducir, estimar y comparar. Y cerrá con que la reproducibilidad permite auditar las conclusiones.

## Preguntas tipo multiple choice

A practicar: pensá cada respuesta antes de que te la diga.

Pregunta uno. ¿Qué mecanismo de avance del tiempo domina en eventos discretos? Opciones: incrementos fijos, siguiente evento, sincronizado con el tiempo real, o el que elija el usuario. La correcta es siguiente evento, porque entre eventos no cambia nada. ¿La tramposa? Incrementos fijos: existe, pero es para continuos.

Pregunta dos. En el ciclo, después de inicializar, ¿qué se hace? Opciones: avanzar el reloj un paso fijo, seleccionar el evento de menor tiempo, actualizar estadísticas, o ejecutar el primer evento programado. La correcta es seleccionar el de menor tiempo. Hay dos tramposas: el paso fijo, que mezcla mecanismos, y el primero programado.

Pregunta tres. Un fin de servicio y una llegada coinciden. Opciones: primero la llegada, primero el fin de servicio, el orden es indiferente, o se sortea. La correcta es primero el fin de servicio: primero se baja, después se sube. La tramposa es que el orden es indiferente, porque el apunte dice que el resultado puede cambiar.

Pregunta cuatro. ¿Cuál es un atributo en el minimercado? Opciones: la cantidad de clientes en fila, la hora de llegada de un cliente, el estado del cajero, o el reloj. La correcta es la hora de llegada: es de cada cliente, va en su etiqueta. Los distractores son la cantidad en fila y el estado del cajero, que son variables de estado: la foto del sistema.

Pregunta cinco. Sobre las visiones del mundo, ¿cuál es verdadera? Primera, procesos usa un motor distinto. Segunda, las visiones son excluyentes. Tercera, un lenguaje de procesos se ejecuta con un motor de eventos. Cuarta, en eventos el reloj es implícito. La correcta es la tercera. La primera es la trampa más fuerte, y la cuarta cruza características.

Pregunta seis. En procesos, ¿qué instrucción suspende por un tiempo desconocido hasta que el recurso esté libre? Opciones: demorar, tomar, liberar o programar. La correcta es tomar: la del baño. El distractor es demorar, que suspende un tiempo conocido: la alarma.

Pregunta siete. ¿Dónde nació la programación orientada a objetos? Opciones: C más más, Java, SIMULA o GPSS. La correcta es SIMULA. La trampa es creer que la simulación tomó los objetos de los lenguajes generales. Fue al revés: de SIMULA pasaron a C más más y a Java.

Pregunta ocho. ¿Qué familia tiene flexibilidad alta y desarrollo alto? Opciones: lenguaje de propósito general, biblioteca de simulación, lenguaje de simulación o simulador visual. La correcta es la biblioteca. ¿Dónde te agarran? En los vecinos: el lenguaje general tiene flexibilidad máxima, y el de simulación, media alta.

Pregunta nueve. ¿Cuándo se elige el paradigma? Opciones: al elegir el software, tras la primera corrida, al formular el modelo conceptual, o lo decide la herramienta. La correcta es al formular el modelo conceptual. La trampa es al elegir el software.

Pregunta diez. ¿Qué resuelve el software? Opciones: elegir la distribución de las llegadas, validar el modelo, administrar la agenda y el reloj, o verificar el modelo. La correcta es la agenda y el reloj. La más tramposa es elegir la distribución: el software la genera, pero no la elige. Acordate de la calculadora.

Pregunta once. Quedó invertida una regla de prioridad en el código. ¿Qué problema es? Opciones: validación, verificación, reproducibilidad o paradigma. La correcta es verificación: el implementado no coincide con el conceptual. La tramposa es validación, que compara contra el sistema real.

Pregunta doce. Para estimar un indicador, ¿qué conviene? Opciones: una corrida con semilla fija, varias réplicas con la misma semilla, varias réplicas con semillas distintas, o usar constantes. La correcta es réplicas con semillas distintas. La tramposa es la misma semilla, que repite la misma corrida. ¿Y las constantes? Esas son para verificar.

## Lo que puede entrar en desarrollo

Hay cuatro temas candidatos. Te dejo el recorrido de cada uno.

El primero, las visiones del mundo. Definilas como dos descripciones del mismo sistema. Explicá eventos con rutinas y procesos con la historia de la entidad. Compará protagonista, reloj, fortaleza y debilidad, con ejemplos. Y cerrá con el motor de eventos por debajo y los objetos de SIMULA envolviendo a ambas.

El segundo, el motor de tiempo. Presentá los dos mecanismos y justificá el siguiente evento por eficiencia. Recorré los seis pasos, destacando la lista de eventos futuros. Y cerrá con las condiciones de corte y el desempate.

El tercero, verificación y validación. Definí cada una con su pregunta, qué compara y su naturaleza. Dá un ejemplo de falla de cada tipo y algunas técnicas de verificación. Y cerrá con que verificado no implica válido.

Y el cuarto, el software de simulación. Presentá las cuatro familias y la relación inversa entre flexibilidad y velocidad. Explicá que el paradigma se elige al modelar. Y cerrá separando lo que resuelve el software de lo que sigue siendo del analista.

## Lo mínimo que te tenés que llevar

Si te quedás sin tiempo, quedate con esto.

El eje cuatro agrega el motor de tiempo. En eventos discretos el reloj salta al siguiente evento, y el tiempo simulado no tiene nada que ver con el real.

El ciclo tiene seis pasos. Se elige el evento de menor tiempo y, ante un empate, primero van los fines de servicio.

En eventos, el sistema reacciona. En procesos, la entidad actúa. Y por debajo, procesos corre sobre un motor de eventos.

La orientación a objetos envuelve a las dos visiones, y nació dentro de la simulación, con SIMULA.

Flexibilidad y velocidad son inversas, y el paradigma se elige al modelar.

Verificar es construir bien el modelo; validar es construir el modelo correcto. La animación ayuda, pero no prueba.

Y por último: semilla fija para reproducir, semillas distintas para estimar, y corrientes separadas para comparar.
