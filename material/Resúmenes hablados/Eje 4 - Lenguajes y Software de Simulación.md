# Eje 4. Lenguajes y software de simulación

Vamos con el eje cuatro. Este audio dura unos veinticuatro minutos. Del eje entra solo la teoría, casi toda en multiple choice, así que vamos a lo preguntable y a las trampas. Ojo, el profe sacó de la evaluación los lenguajes clásicos y lo que aportó cada uno, los lenguajes de hoy como bibliotecas sobre lenguajes de propósito general, el panorama de herramientas y los dos complementos, el de la evolución de los lenguajes y el software y el de los criterios para elegir una herramienta. Eso no lo estudies: ya lo saqué de este resumen. Son cuatro ideas centrales. Una, el eje agrega el motor de tiempo: el reloj avanza al siguiente evento y todo simulador repite el mismo ciclo. Dos, hay dos visiones del mundo, eventos y procesos, y por debajo los procesos corren sobre un motor de eventos. Tres, cada herramienta tiene su paradigma, y el paradigma se elige al modelar, no al elegir el software. Cuatro, verificar no es validar.

## Dónde está parado este eje

De las diez etapas del estudio de simulación del eje uno, la cuarta, desarrollo del modelo de simulación, es traducir el modelo conceptual en un modelo computarizado. De eso trata este eje.

El eje dos te dio la aleatoriedad; el eje tres, las transformaciones y Monte Carlo, que es estático. El eje cuatro agrega la tercera pieza, el motor de tiempo.

Y una frase del apunte: todo lo que no se traduce no existe en el modelo. Si el cajero se toma un descanso y no se codificó, el simulador describe un sistema que no es el tuyo.

**Lo importante.** Eje dos, aleatoriedad. Eje tres, transformación. Eje cuatro, tiempo.

**Ojo, trampa.** Que Monte Carlo ya es una simulación dinámica: falso, es estática. Que el eje cuatro aporta la aleatoriedad: falso, eso es del eje dos.

## Los componentes de un modelo ejecutable

Casi todo modelo de eventos discretos usa las mismas piezas. El ejemplo es una caja de minimercado.

La entidad es el objeto que circula y sobre el que ocurren las cosas; se crea, se mueve y se destruye. Acá, cada cliente. El atributo es un dato propio de cada entidad: su hora de llegada, su prioridad. El recurso es el medio limitado que las entidades se disputan: el cajero, que puede estar libre, ocupado, en falla o fuera de turno. La cola es donde esperan las entidades que no pueden avanzar, con una disciplina que decide a quién le toca. Acá es FIFO: el primero que llega es el primero que se atiende.

La variable de estado es un dato global que describe al sistema en un instante: cuántos hay en la fila, si el cajero está ocupado. El evento es un suceso instantáneo que cambia el estado: una llegada, un fin de atención. El reloj de simulación guarda el tiempo simulado actual, que no tiene nada que ver con el tiempo real de ejecución: un año de una planta se puede simular en cuarenta segundos.

La lista de eventos futuros es la agenda, ordenada por tiempo, de los eventos ya programados que todavía no ocurrieron. Es la estructura central del simulador. Los acumuladores estadísticos son sumas y contadores que se actualizan durante la corrida. Y la réplica es una corrida completa del modelo; como es estocástico, una sola no alcanza.

**Lo importante.** Reconocer cada componente por su definición, sobre todo evento, reloj, lista de eventos futuros y réplica.

**Ojo, trampa.** Atributo contra variable de estado: el atributo es de cada entidad, la variable de estado es global. La cantidad de gente en la fila no es un atributo. Cola contra lista de eventos futuros: en la cola esperan entidades, en la lista esperan eventos, y la estructura central es la lista. Y el evento es instantáneo: la atención no es un evento; la llegada y el fin de atención, sí.

## El motor de tiempo

### Dos maneras de mover el reloj

Con incrementos fijos de tiempo, el reloj avanza siempre el mismo paso y en cada paso revisa si pasó algo. Se usa en sistemas continuos, donde el estado cambia permanentemente y se integran ecuaciones paso a paso. Es lo del eje ocho.

Con avance al siguiente evento, el reloj salta directo al próximo evento programado, porque entre evento y evento, por definición, no cambia nada. Es el mecanismo dominante en eventos discretos: en la caja, recalcular el estado segundo a segundo durante ocho horas no tendría sentido.

**Lo importante.** Incremento fijo va con continuo; siguiente evento va con discreto. La razón es la eficiencia. Eso sí, tomalo como la asociación típica, no como una definición: en el eje siete vas a ver que los modelos de agentes suelen avanzar por pasos fijos sin ser continuos, y el apunte pone esa confusión como trampa.

**Ojo, trampa.** Que te crucen los pares, o que te digan que entre dos eventos el estado cambia de a poco.

### El ciclo de ejecución

Todo simulador de eventos discretos, sin importar marca ni lenguaje, repite seis pasos. Uno, inicialización: reloj y acumuladores en cero, estado inicial, y se programan los primeros eventos, típicamente la primera llegada. Dos, selección del próximo evento: el de menor tiempo en la lista de eventos futuros, que se saca de la lista. Tres, avance del reloj hasta ese instante. Cuatro, ejecución de la rutina del evento: cambia el estado, se mueven entidades y se programan los eventos que se desprenden. Cinco, actualización de estadísticas. Seis, control de fin: si se cumplió la condición de corte, se emite el reporte; si no, se vuelve al paso dos. El corte puede ser el tiempo final, una cantidad de entidades procesadas o la lista de eventos vacía.

Y la regla de desempate. Si dos eventos coinciden en el mismo instante, hace falta una regla explícita, porque el resultado puede cambiar. La convención más habitual, y la que usa la cátedra, es procesar primero los fines de servicio y después las llegadas. Así el recurso se libera antes de que el cliente nuevo pregunte si está libre.

**Lo importante.** El orden de los pasos, que se elige el evento de menor tiempo, y la regla de desempate.

**Ojo, trampa.** Que inviertan los pasos dos y tres: primero se elige el evento, después se mueve el reloj. Que el próximo evento sea el primero que se programó: es el de menor tiempo. Y en el empate, que primero van las llegadas o que el orden no importa.

**Si te toca de desarrollo.** Justificá el siguiente evento frente al incremento fijo. Recorré los seis pasos, con la lista de eventos futuros como estructura central. Cerrá con las condiciones de corte y el desempate.

## Lenguajes de simulación

En los años cincuenta todo se programaba en lenguajes de propósito general, como FORTRAN, ALGOL y más tarde C, y en cada proyecto el analista reescribía la agenda, el reloj, las colas y las estadísticas.

De ahí nace el lenguaje de simulación: un lenguaje cuyas construcciones básicas corresponden directamente a los conceptos del modelado, como entidades, recursos, colas, eventos y avance del reloj. El motor viene incorporado; no lo escribe el usuario. El modelo queda más corto y con menos errores. El precio es cierta pérdida de libertad.

**Lo importante.** La definición y su frase clave: el motor viene incorporado.

**Ojo, trampa.** Que en un lenguaje de simulación el usuario programa la agenda: falso. Que da más libertad que un lenguaje de propósito general: es al revés.

## Las visiones del mundo

Según el apunte, este es el punto realmente conceptual del eje: el mismo sistema se puede describir de dos maneras, que dieron origen a dos familias de lenguajes. Se llaman visiones del mundo.

### Orientación a eventos

El modelo se organiza alrededor de los eventos: una rutina por tipo de evento, que dice qué cambia y qué eventos nuevos se programan. En el minimercado, la rutina de llegada primero programa la próxima llegada; después, si el cajero está libre, lo ocupa y programa el fin de atención, y si no, el cliente va a la fila. La de fin de atención libera al cajero o toma al siguiente de la fila.

El cliente no es protagonista: el modelo es una colección de reacciones del sistema. Es insuperable para entender un simulador por dentro, pero con veinte tipos de eventos entrelazados se vuelve difícil de seguir.

### Orientación a procesos

El modelo se organiza alrededor del ciclo de vida de la entidad. Escribís la historia del cliente: llega, toma el cajero, espera si está ocupado, se hace atender, lo libera y se va. Se lee como el enunciado. No aparecen el reloj, la agenda ni la fila: la fila surge sola, porque varios procesos quedan suspendidos en tomar el cajero.

Las instrucciones clave son las que suspenden el proceso. Demorar lo duerme un tiempo conocido. Tomar lo duerme un tiempo desconocido, hasta que el recurso esté disponible.

### Las dos visiones, comparadas

En eventos, el protagonista es el sistema, que reacciona. El reloj y la agenda son explícitos: los programa el modelador. Fortaleza, control total y máxima eficiencia; debilidad, difícil de seguir en modelos grandes. Ejemplos: SIMSCRIPT y los modelos escritos a mano en C, Java o Python.

En procesos, el protagonista es la entidad, que actúa. El reloj y la agenda son implícitos: los resuelve el lenguaje. Fortaleza, legibilidad y rapidez de construcción; debilidad, menos control fino en casos muy particulares. Ejemplos: GPSS, SIMULA, SimPy y casi todos los simuladores visuales.

Y lo que el apunte marca como lo más importante: las visiones no compiten, describen el mismo sistema desde distinta altura. Por debajo, un lenguaje de procesos se ejecuta con un motor de eventos: demorar cuatro es, para el motor, programar el evento reanudar este proceso en reloj más cuatro. Procesos es una interfaz más cómoda sobre el mismo motor.

### La tercera visión: objetos

La orientación a objetos no reemplaza a las otras dos, las envuelve: cada máquina u operario es un objeto con sus datos, su estado y su comportamiento, que se comunica con los demás.

Y el dato que más se pregunta: la programación orientada a objetos nació dentro de la simulación. SIMULA, de mediados de los sesenta, introdujo clase, objeto y herencia, que después pasaron a C más más, Java y Python. Por eso hoy, al arrastrar un procesador en un simulador visual, instanciás un objeto que ya trae su cola, su recurso y sus estadísticos.

**Lo importante.** Eventos: el sistema reacciona, reloj explícito. Procesos: la entidad actúa, reloj implícito. Procesos corre sobre un motor de eventos, y objetos envuelve a las dos.

**Ojo, trampa.** La más probable de todo el eje: que procesos usa un motor distinto o que las visiones son excluyentes. Falso. También que te crucen las características, como reloj explícito en procesos, o que te crucen demorar y tomar. Y que la simulación tomó los objetos de C más más o de Java: fue al revés.

**Si te toca de desarrollo.** Definí visión del mundo. Explicá eventos con sus rutinas y procesos con la historia del cliente, con demorar y tomar. Compará protagonista, reloj, fortaleza y debilidad. Cerrá con el motor de eventos por debajo y los objetos envolviendo a ambas.

## Software de simulación

### Cuatro familias de herramientas

Se diferencian por cuánto trabajo hace el analista y cuánto viene resuelto.

Lenguaje de propósito general, como Python o Java: hay que construir todo. Flexibilidad máxima, tiempo de desarrollo muy alto. Biblioteca de simulación, como SimPy: aporta el motor y vos escribís la lógica en código. Flexibilidad alta, desarrollo alto. Lenguaje de simulación, como GPSS o SIMSCRIPT: sus primitivas ya son conceptos de simulación. Flexibilidad media alta, desarrollo medio. Simulador visual: trae motor, objetos, animación y reportes, y armás el modelo arrastrando y parametrizando. Flexibilidad media, desarrollo bajo.

No hay opción universalmente mejor. Flexibilidad y velocidad de desarrollo son inversas: cuanto más resuelto viene, más rápido modelás y menos podés salirte del molde. Y como los simuladores visuales traen lenguajes internos, la frontera entre la tercera y la cuarta familia es porosa.

**Lo importante.** El orden de las cuatro familias y la relación inversa entre flexibilidad y velocidad.

**Ojo, trampa.** «El simulador visual siempre es la mejor opción»: no hay opción universalmente mejor. «Los simuladores visuales no permiten programar»: falso. Y no cruces los niveles: la biblioteca tiene flexibilidad alta; el lenguaje de simulación, media alta.

### No todo el software simula lo mismo

El apunte marca como error frecuente pedirle a una herramienta lo que su paradigma no puede representar.

Eventos discretos: entidades individuales que compiten por recursos; el estado cambia en instantes puntuales. Responde cuánto se espera o dónde está el cuello de botella. Eje cinco y trabajo integrador.

Dinámica de sistemas, o simulación continua: niveles y flujos con bucles de realimentación y ecuaciones integradas paso a paso. No hay individuos. Responde cómo evoluciona una población o un stock. Eje ocho.

Basada en agentes: individuos autónomos con reglas propias, y el comportamiento global emerge de sus interacciones. Responde cómo se difunde una epidemia o una conducta. Eje siete.

Multimétodo o híbrido: combina los anteriores. En la materia solo se menciona.

La advertencia: elegir el paradigma es una decisión de modelado, no de software. Se toma al formular el modelo conceptual, y si no corresponde al problema, ninguna herramienta lo arregla.

**Lo importante.** Cada paradigma se define por cómo representa el sistema, y se elige al modelar.

**Ojo, trampa.** Dinámica de sistemas con individuos, o agentes con un comportamiento global programado en lugar de emergente. Y sobre todo, que el paradigma se elige según el software disponible.

**Si te toca de desarrollo.** Definí los tres paradigmas principales con una pregunta típica de cada uno. Nombrá el híbrido. Cerrá con que la elección es de modelado: si el paradigma no corresponde al problema, ninguna herramienta lo arregla.

### Qué resuelve el software y qué sigue siendo tuyo

El software resuelve la agenda de eventos y el reloj, los generadores pseudoaleatorios del eje dos, la generación de variables del eje tres, las colas y recursos, las estadísticas, la animación y los reportes, y las réplicas y experimentos.

Sigue siendo tuyo formular el problema; analizar los datos de entrada para decidir qué distribución representa a las llegadas, que es del eje seis; el modelo conceptual; la verificación; la validación; y el diseño de experimentos. Cuando configurás una llegada exponencial, la herramienta usa un generador congruencial y un método de transformación: los ejes dos y tres sirven para juzgar si está bien usada.

**Lo importante.** La herramienta automatiza lo mecánico; lo conceptual es del analista.

**Ojo, trampa.** Que el software elige la distribución de entrada, verifica o valida. Genera la distribución que vos elegiste, pero no la elige.

## Implementación y verificación

### Verificación

Una vez armado el modelo en la herramienta, con objetos como fuente, cola, procesador o sumidero, hay que verificarlo. Verificar es comprobar que el modelo implementado hace lo que quisimos: que la traducción del conceptual al computacional fue correcta. Es puramente interna y ninguna herramienta la hace sola.

Las técnicas son siete. Correr con valores determinísticos, reemplazando las distribuciones por constantes para predecir el resultado a mano. Revisar la traza de eventos. Mirar la animación. Probar valores extremos, como un recurso de capacidad cero. Verificar la conservación de entidades: las creadas tienen que igualar a las que salieron más las que quedaron. Contrastar con un caso de solución conocida, como uno de teoría de colas. Y la revisión por otra persona.

La advertencia: la animación es ayuda, no prueba. Lo que se ve bien no está necesariamente bien.

**Lo importante.** Es interna, no la hace la herramienta y tiene técnicas concretas.

**Ojo, trampa.** Que la animación prueba que el modelo es correcto, o que el simulador verifica solo: falso. Y correr con valores determinísticos no es lo mismo que fijar la semilla.

### Verificar no es validar

El apunte dice que se confunden permanentemente.

Verificación pregunta si construimos bien el modelo. Compara el implementado contra el conceptual, y es interna, lógica y de programación. Ejemplo: la regla de prioridad quedó al revés en el código.

Validación pregunta si construimos el modelo correcto. Compara el modelo contra el sistema real, y es externa, estadística y de criterio experto. Ejemplo: el modelo asume llegadas parejas y en la realidad hay un pico al mediodía.

Un modelo puede estar perfectamente verificado y ser completamente inválido. La validación se ve en el eje seis.

**Lo importante.** Construir bien el modelo es verificar. Construir el modelo correcto es validar.

**Ojo, trampa.** Te cruzan los ejemplos: la prioridad invertida es de verificación, el pico del mediodía es de validación. Y la frase «si está verificado, es válido» es falsa.

**Si te toca de desarrollo.** Definí cada una con su pregunta, qué compara y su naturaleza. Dá un ejemplo de falla de cada una. Nombrá técnicas de verificación. Cerrá con que verificado no implica válido.

### Semillas, réplicas y reproducibilidad

Como el modelo es estocástico, cada corrida da un resultado distinto. Eso pide tres cuidados.

Fijar la semilla para reproducir exactamente una corrida, al depurar o para que otro obtenga los mismos números: lo que no se puede reproducir no se puede discutir. Correr varias réplicas con semillas distintas para estimar un indicador: una sola corrida no dice casi nada. Y usar corrientes separadas para cada fuente de aleatoriedad, que permite comparar escenarios con la misma suerte: es la técnica de números aleatorios comunes, de reducción de varianza, del eje seis.

**Lo importante.** Semilla fija para reproducir, semillas distintas para estimar, corrientes separadas para comparar.

**Ojo, trampa.** Réplicas con la misma semilla para estimar: repetirías la misma corrida. Y los números aleatorios comunes son para comparar escenarios.

**Si te toca de desarrollo.** Explicá por qué un modelo estocástico obliga a cuidar la aleatoriedad. Desarrollá los tres cuidados con su propósito: reproducir, estimar y comparar. Cerrá con que la reproducibilidad permite auditar las conclusiones.

## Preguntas tipo multiple choice

Pregunta uno. ¿Qué mecanismo de avance del tiempo domina en eventos discretos? Opciones: incrementos fijos, siguiente evento, sincronizado con el tiempo real, o el que elija el usuario. La correcta es siguiente evento, porque entre eventos no cambia nada. El distractor tramposo es incrementos fijos: existe, pero es para continuos.

Pregunta dos. En el ciclo, después de inicializar, ¿qué se hace? Opciones: avanzar el reloj un paso fijo, seleccionar el evento de menor tiempo, actualizar estadísticas, o ejecutar el primer evento programado. La correcta es seleccionar el de menor tiempo. Tramposas: el paso fijo, que mezcla mecanismos, y el primero programado.

Pregunta tres. Un fin de servicio y una llegada coinciden. Opciones: primero la llegada, primero el fin de servicio, el orden es indiferente, o se sortea. La correcta es primero el fin de servicio. La tramposa es que el orden es indiferente: el apunte dice que el resultado puede cambiar.

Pregunta cuatro. ¿Cuál es un atributo en el minimercado? Opciones: la cantidad de clientes en fila, la hora de llegada de un cliente, el estado del cajero, o el reloj. La correcta es la hora de llegada, dato propio de cada entidad. El distractor son la cantidad en fila y el estado del cajero, que son variables de estado.

Pregunta cinco. Sobre las visiones del mundo, ¿cuál es verdadera? Opciones: procesos usa un motor distinto; las visiones son excluyentes; un lenguaje de procesos se ejecuta con un motor de eventos; o en eventos el reloj es implícito. La correcta es la tercera. La primera es la trampa más fuerte, y la última cruza características.

Pregunta seis. En procesos, ¿qué instrucción suspende por un tiempo desconocido hasta que el recurso esté libre? Opciones: demorar, tomar, liberar o programar. La correcta es tomar. El distractor es demorar, que suspende un tiempo conocido.

Pregunta siete. ¿Dónde nació la programación orientada a objetos? Opciones: C más más, Java, SIMULA o GPSS. La correcta es SIMULA. La trampa es creer que la simulación tomó los objetos de los lenguajes generales: fue al revés, de SIMULA pasaron a C más más y a Java.

Pregunta ocho. ¿Qué familia tiene flexibilidad alta y desarrollo alto? Opciones: lenguaje de propósito general, biblioteca de simulación, lenguaje de simulación o simulador visual. La correcta es la biblioteca. El lenguaje general tiene flexibilidad máxima, y el de simulación, media alta: es fácil cruzarlos.

Pregunta nueve. ¿Cuándo se elige el paradigma? Opciones: al elegir el software, tras la primera corrida, al formular el modelo conceptual, o lo decide la herramienta. La correcta es al formular el modelo conceptual. La trampa es al elegir el software.

Pregunta diez. ¿Qué resuelve el software? Opciones: elegir la distribución de las llegadas, validar el modelo, administrar la agenda y el reloj, o verificar el modelo. La correcta es la agenda y el reloj. La más tramposa es elegir la distribución: el software la genera, pero no la elige.

Pregunta once. Quedó invertida una regla de prioridad en el código. ¿Qué problema es? Opciones: validación, verificación, reproducibilidad o paradigma. La correcta es verificación: el implementado no coincide con el conceptual. La tramposa es validación, que compara contra el sistema real.

Pregunta doce. Para estimar un indicador conviene: una corrida con semilla fija, varias réplicas con la misma semilla, varias réplicas con semillas distintas, o usar constantes. La correcta es réplicas con semillas distintas. La tramposa es la misma semilla, que repite la misma corrida; las constantes son para verificar.

## Lo que puede entrar en desarrollo

Las visiones del mundo. Definilas como dos descripciones del mismo sistema. Explicá eventos con rutinas y procesos con la historia de la entidad. Compará protagonista, reloj, fortaleza y debilidad, con ejemplos. Cerrá con el motor de eventos por debajo y los objetos de SIMULA envolviendo a ambas.

El motor de tiempo. Presentá los dos mecanismos y justificá el siguiente evento por eficiencia. Recorré los seis pasos, destacando la lista de eventos futuros. Cerrá con las condiciones de corte y el desempate.

Verificación y validación. Definí cada una con su pregunta, qué compara y su naturaleza. Dá un ejemplo de falla de cada tipo y algunas técnicas de verificación. Cerrá con que verificado no implica válido.

El software de simulación. Presentá las cuatro familias y la relación inversa entre flexibilidad y velocidad. Explicá que el paradigma se elige al modelar. Cerrá separando lo que resuelve el software de lo que sigue siendo del analista.

## Lo mínimo que te tenés que llevar

El eje cuatro agrega el motor de tiempo: en eventos discretos el reloj salta al siguiente evento, y el tiempo simulado no tiene nada que ver con el real.

El ciclo tiene seis pasos, se elige el evento de menor tiempo y, ante un empate, primero van los fines de servicio.

En eventos el sistema reacciona; en procesos la entidad actúa. Por debajo, procesos corre sobre un motor de eventos.

La orientación a objetos envuelve a las dos visiones, y nació dentro de la simulación, con SIMULA.

Flexibilidad y velocidad son inversas, y el paradigma se elige al modelar.

Verificar es construir bien el modelo; validar es construir el modelo correcto. La animación ayuda, pero no prueba.

Semilla fija para reproducir, semillas distintas para estimar y corrientes separadas para comparar.
