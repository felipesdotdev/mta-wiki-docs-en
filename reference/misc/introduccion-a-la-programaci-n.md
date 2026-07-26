---
doc_id: "mta-wiki:5516"
title: "ES/Introducción a Lua"
source_title: "Introduccion a la Programación"
source_url: "https://wiki.multitheftauto.com/wiki/Introduccion_a_la_Programaci%C3%B3n"
revision_id: 39269
language: "en"
categories: []
generated_at: "2026-07-26T16:10:28.171342+00:00"
---

# ES/Introducción a Lua

Los llamados "resources" son fundamentales en MTA. Básicamente consisten en una carpeta o archivo ZIP que contiene una colección archivos, además de un archivo **meta.xml** que define qué archivos pertenecen al resource, algunas configuraciones, y otras cosas. Como los programas en un sistema operativo, los resources pueden ser iniciados, detenidos, y reiniciados, y varios pueden funcionar al mismo tiempo.

Todo lo que es la programación ocurre dentro de los resources. Lo que éste haga define si se trata de un modo de juego, un mapa, un script sencillo, u otra cosa. MTA, por defecto, trae ciertos resources que puedes usar opcionalmente en tus modos de juego.

**Lo primero que debes tener en cuenta al iniciarte en la programacion en LUA, es conseguir un editor que funcione para ello. Esto hace mucho más facil tu trabajo, permitiéndote corregir el sintaxis de las matemáticas, por ejemplo. El equipo de MTA recomienda [Notepad++](http://notepad-plus.sourceforge.net/uk/site.htm) y [LuaEdit](http://luaedit.sourceforge.net/).**

**También en cuanto a Tutoriales, puedes guiarte de estos: [Scripteando Cosas Básicas](http://forum.mtasa.com/viewtopic.php?f=145&t=70852) .**

## Creando un script funcional

Primero, aprenderemos a hacer un script que permita al jugador caminar libremente por la ciudad. Esto lo explicaremos paso a paso.

### Estructura de un script y ubicación del mismo

Dirijámonos a la carpeta raíz de tu servidor para MTA (por defecto es *C:\Archivos de Programa\Multi Theft Auto\server*). Después vamos a la siguiente ubicación:

\server\mods\deathmatch\resources\

Verás muchos archivos ZIP. Como mencioné antes, estos ZIP son los resources, que vienen por defecto con MTA. Para crear tu propio resource, añade una carpeta a esta ubicación, y dale un nombre. Recomiendo que, al ser tu primer script, sigas las instrucciones al pie de la letra, y a esta carpeta la llames "myserver".

Ahora, entremos a la ubicación:

\resources\myserver\

### Identificando tu resource

Como mencioné antes, todo resource tiene un archivo que define el tipo, los archivos, y las configuraciones del resource, es el *meta.xml*. Siempre debe estar dentro de cada resource, de otra forma éste no funciona. Así que creemos un archivo de texto, y llamémoslo "meta.xml" (sin las comillas). Luego abrámoslo con el Bloc de Notas, o con Microsoft Wordpad.

Una vez dentro de este archivo, agregaremos el siguiente código:

```
<meta>
     <info author="TuNombre" type="gamemode" name="Mi Servidor" description="Mi primer servidor de MTA DM" />
     <script src="script.lua" />
</meta>
```

En la etiqueta *<info />* hay un campo "type". Éste indica el tipo de resource, que siendo "gamemode" en este caso, define que es un modo de juego. Nótese que cuando es otro tipo de resource, el valor "type" cambia. Pero eso lo veremos luego. Por ahora, un modo de juego es lo que necesitas para comenzar un servidor.

La etiqueta *<script />* indica el script que tendrá nuestro modo de juego. A continuación, cómo crearlo.

### Creando un script simple

Nótese que en la etiqueta *<script />*, el archivo Lua no está en otro directorio, como por ejemplo *myserver\script.lua*. Esto es porque el archivo LUA del que hablamos será creado en el mismo lugar en el que el archivo *meta.xml*. Bueno, ahora creamos en "myserver", otro archivo de texto, y lo llamamos "script.lua". Abrámoslo y agreguemos estas líneas:

```
function manejadorDeInicio()
	local x = 1959.55
	local y = -1714.46
	local z = 10
	spawnPlayer(source, x, y, z)
	fadeCamera(source, true)
	setCameraTarget(source, source)
	outputChatBox("Bienvenido a Mi Servidor", source)
end
addEventHandler("onPlayerJoin", getRootElement(), manejadorDeInicio)
```

Este script inicia a tu jugador en las coordenadas "x", "y" y "z" (spawnPlayer) cuando entras al servidor. OJO: ¡La función *fadeCamera* siempre debe ser usada cuando inicias al jugador, de otra forma, la pantalla quedará en negro!. Lo mismo pasa con la función *setCameraTarget*; si no la usas, el jugador no podrá verse a sí mismo, si no que mirará al cielo infinito.

La variable **source** indica qué fue lo que ocasionó al evento. Como el evento *onPlayerJoin* significa *alIniciarJugador*, lógico que lo que ocasione a este evento sea el jugador. Así, evitaremos iniciar a cualquier jugador.

Ahora, dirigiéndonos a [addEventHandler](mta://scripting/shared/functions/addeventhandler.md), podrás ver que posee 3 cosas: *onPlayerJoin* (el nombre del evento), *getRootElement()* (que indica por qué o quién será iniciado el evento, ya que *getRootElement()* significa "todo"), y *joinHandler*, que es el nombre de la función a ejecutar cuando el evento sea activado.

Con esto, deberías poder comenzar a jugar. Pero faltan algunos detalles... ¡Sigamos!

### Corriendo el script

Para que tu servidor local sea iniciado, debes ir a la carpeta raíz de tu servidor (recuerda cuando fuimos a los resources, 2 puestos encima). Una vez que lo inicies, aparecerá una consola con una serie de datos; recuerda el número del puerto, porque lo necesitarás para jugar. Cuando aparezca un mensaje que diga "Server started and is ready to accept connections!", sabrás que ya está listo.

Pero antes de jugar, debes iniciar el modo de juego. Escribe "gamemode myserver" en la consola del servidor, y presiona Enter. El servidor emitirá algunos mensajes, e iniciará tu modo de juego, y si algún error surge, nos lo dirá. Bueno, ahora es tiempo de probar el modo de juego. Inicia MTA, y en el menú principal escoge "Quick Connect". Apareceren 3 campos. En el primero, escribe "localhost", en el segundo, el número del puerto de tu servidor, y en el tercero, nada, después de todo es la contraseña,y tú no pusiste ninguna. Si todo funciona bien, deberías poder comenzar a jugar en Los Santos.

A continuación, te enseñaremos a crear un comando que permita crear un vehículo a tu lado. Si quieres, puedes saltarte este paso y seguir la programación avanzada con [Map Manager](mta://mapping/map-manager.md), que continúa este tutorial. También puedes revisar [Introducción a la Programación del GUI](mta://scripting/concepts/introduction-to-scripting-gui.md), en el que te enseñaremos a diseñar la Interfaz Gráfica de Usuario (GUI en inglés, por *Graphical User Interface*).

## Creando un Comando

Volvamos a *script.lua*. Como dije hace un momento, crearemos un comando que permita crear un vehículo a tu lado. Primero, necesitaremos crear una función a la que llamar, y un manejador de comandos que cree el comando buscado.

```
-- Aquí creamos la función que llama el manejador, con los argumentos "elJugador", "nombreDelComando", "modeloDeVehiculo":
function crearVehículoParaJugador(elJugador, nombreDelComando, modeloDeVehículo)
   -- Crear el vehículo y otros.
end

-- Aquí creamos el manejador de comandos:
addCommandHandler("crearvehiculo", crearVehículoParaJugador)
```

**Nota:** *Los nombres de las funciones tienen enlaces que te llevan a la **documentación** de ellas.*

#### Acerca de los manejadores de comandos

El primer argumento de *addCommandHandler* es el nombre del comando que el jugador podrá ingresar, y el segundo es la función que ejecutará en el momento de ingreso del comando (en este caso *crearVehiculoParaJugador*).

Si tienes alguna experiencia con la programación en C o algún lenguaje parecido, sabrás que las funciones se ejecutan de la forma:

```
nombreDeFunción(argumento1, argumento2, argumento3, ..)
```

```
nombreDeFunción(elJugador, nombreDelComando, argumento3, ..)
```

Fijémonos bien en esto. Vemos que *argumento1* es *elJugador* y *argumento2* es *nombreDelComando*. *elJugador* representa al jugador que haya ingresado el comando, por lo que de la forma que lo llames, esta variable será el jugador. *nombreDelComando* es simplemente el nombre del comando (sin la barra "/"), no hay ningún misterio en ello, por lo que si el jugador escribió "/crearvehiculo" entonces esta variable sería "crearvehiculo". Por último, *argumento3* representa una variable más, que estudiaremos más adelante. Nunca olvides que los 2 primeros argumentos son obligatorios y están predefinidos (y debes tenerlos en el orden que se indican), pero puedes llamarlos como sea.

*addCommandHandler* permite llamar fácilmente a funciones como *crearVehículoParaJugador*, de forma interna.

Por ejemplo: Alguien entra el comando "/crearvehiculo 468". El servidor creará el vehículo 468, es decir, la moto Sánchez. Dentro del código, *addCommandHandler* llama a la función *crearVehículoParaJugador* como si hubiera sido escrito así:

```
crearVehículoParaJugador(elJugador,"crearvehiculo","468") -- Recuerda que "elJugador" es el elemento jugador que entró el comando.
```

Como podemos ver, esto prevée ciertos argumentos que ya hemos mencionado. Pero el más importante es "468", que es el "argumento3" del que hablábamos más arriba. Éste se refiere al modelo del vehículo. Recuerda que siempre debes definir los primeros 2 parámetros ("elJugador" y "nombreDelComando"), porque de otra forma el comando no funcionará.

**Nota:** *Tienes que poner el manejador de comandos DEBAJO de la función a llamar por el comando. ¡El orden de las ejecuciones es fundamental!*

#### Escribiendo la función

Para llenar la función que hemos creado, primero hay que plantearse qué se debe hacer:

- Conseguir la posición del jugador, así sabremos dónde crear el vehículo (queremos que aparezca al lado del jugador).

- Calcular la posición donde crearemos el vehículo (no queremos que aparezca en el jugador).

- Crear el vehículo.

- Revisar si fue creado. Si no, mostrar alguna advertencia o algún mensaje de error.

Para conseguir estos objetivos, debemos usar ciertas funciones, las cuales se pueden ver visitando la [Lista de Funciones de Servidor](mta://scripting/concepts/scripting-functions.md). Primero, una función para conseguir la posición del jugador. Si visitaste la [Lista de Clases de MTA](https://wiki.multitheftauto.com/wiki/ES/Clases_MTA), sabrás que un jugador es un elemento, lo que nos lleva a buscar una **Función de Elemento**, la cual es *[getElementPosition](mta://scripting/shared/functions/getelementposition.md)*. Haciendo click en ella, visitarás la documentación de ella, que contiene una descripción, el sintaxis (los argumentos necesarios en la función), y, generalmente, un ejemplo de cómo usarla.

Para la función [getElementPosition](mta://scripting/shared/functions/getelementposition.md), el sintaxis sería:

```
float, float, float getElementPosition ( elemento elElemento )
```

Los 3 *float* que aparecen, son los valores que regresa la función. Estos valores, en español, se llaman **Número de punto flotante**, y son números que pueden o no, poseer decimales (véase la [Lista de tipos de valores](https://wiki.multitheftauto.com/wiki/ES/Tipos_de_Valores)). Como "x", "y" y "z" son coordenadas, por defecto siempre serán números de punto flotante. Ahora, fijándonos en los paréntesis, notaremos que sólo aparece "elElemento" como argumento de la función. Pues, aplicando la función a un jugador, tendríamos algo como esto:

```
function crearVehículoParaJugador(elJugador, nombreDelComando, modeloDeVehículo)
	--[[Aquí conseguiremos la posición del jugador, y la almacenaremos en 3 valores: "x", "y" y "z". Nota: "local" significa que las variables indicadas sólo pueden ser usadas en la función actual.]]--
	local x,y,z = getElementPosition(elJugador)
end
```

Ahora, para crear el vehículo al lado del jugador, debemos modificar alguna coordenada, en este caso, "x".

```
function crearVehículoParaJugador(elJugador, nombreDelComando, modeloDeVehículo)
	local x,y,z = getElementPosition(elJugador)
	x = x + 5 --Agregamos 5 a la posición "X" (¡esto no altera la posición del jugador!)
end
```

Nuevamente, necesitamos otra función para crear el vehículo. Buscándola en la [Lista de Funciones de Servidor](mta://scripting/concepts/scripting-functions.md), la encontraremos. Ya que hablamos de vehículo, vamos a la subcategoría tal, en la que encontramos [createVehicle](mta://scripting/shared/functions/createvehicle.md). En esta función, el valor que regresa la función consta de 1 solo argumento (esto es lo más común en las funciones), y es el vehículo creado, o un valor "boolean" ("lógico" en inglés) de tipo "false", si el vehículo no fue creado.

```
function crearVehículoParaJugador(elJugador, nombreDelComando, modeloDeVehículo)
	local x,y,z = getElementPosition(elJugador)
	x = x + 5
	local vehículoCreado = createVehicle(tonumber(modeloDeVehículo),x,y,z)
end
```

Nótese que usamos "tonumber(modeloDeVehículo)" en vez de usar directamente "modeloDeVehículo". Esto es porque cuando entramos un comando, todos los argumentos salen en forma de "string" ("arreglo" en inglés), que es un tipo de valor textual. Por ello, no puede ser usado como número, y la función "tonumber()" nos permite dejarlo como un número.

Bueno, tenemos todo lo necesario para que nuestro script funcione, pero eso no indica que esté listo. Ya tenemos la función para conseguir la posición del jugador, modificarla, y crear el vehículo. Pero nos falta el mensaje. La función para esto se llama *outputChatBox*. Como dije antes, si el vehículo no fue creado, entonces regresa un valor "false". Así que creamos nuestra primera condición, en la que si el valor regresado es falso, entonces aparece un mensaje.

Veamos cómo luce el script final:

```
function crearVehículoParaJugador(elJugador, nombreDelComando, modeloDeVehículo)
	local x,y,z = getElementPosition(elJugador)
	x = x + 5
	local vehículoCreado = createVehicle(tonumber(modeloDeVehículo),x,y,z)
	if (vehículoCreado == false) then --"if" es la condición, siempre debe ir acompañado de la condición y un "then".
		outputChatBox("Error al crear vehículo.",elJugador) --Crea un mensaje de error simple en el chat.
	end
end
addCommandHandler("crearvehiculo", crearVehículoParaJugador) --Y aquí creamos el manejador de comandos.
```

Nada mal, ¿no? Ya te hemos introducido en la creación de 2 scripts sencillos. Si quieres más programación avanzada, entonces visita el [Mánager de Mapas](https://wiki.multitheftauto.com/index.php?title=Map_Manager&action=edit&redlink=1).

## Lo que necesitas saber

Ya has leído un poco sobre resources, manejadores de comandos y funciones de búsqueda en la documentación (en el primer párrafo), pero aún queda mucho por aprender. En esta sección te daremos una vista rápida sobre esto, y si se puede, enlazar a otras páginas útiles.

### Scripts de cliente y servidor

Quizás ya has notado los términos Server (o Servidor) y Client (o Cliente) en algún lado, mayormente en conjunción con las funciones. MTA no sólo soporta scripts que funcionan en el servidor y prevén comandos (como el que escribimos arriba) u otras características; también scripts que corren en el cliente (MTA en sí, el software que usas para conectarte a los servidores). Esto se debe a que algunas funciones tienen que estar del lado cliente (como el GUI; Graphical User Interface, Interfaz de Usuario Gráfica), si bien funcionan mejor o porque no se pueden hacer en el servidor.

La mayoría de los scripts que harás (modos de juego y/o mapas) probablemente serán de tipo servidor, como el que escribimos en la primera sección. Si tratas de hacer funcionar algo que no se puede hacer en el servidor, probablemente tendrá que ser de cliente. para un script de cliente, por ejemplo, podrías crear un archivo de Lua ordinario (como *client.lua*) y especificarlo en el archivo meta.xml, así:

```
<script src="client.lua" type="client" />
```

El atributo *type* por defecto es 'server' (servidor), por lo que no es necesario escribirlo cuando se trata de scripts de servidor. Si quieres, puedes leer más sobre [scripts de cliente](https://wiki.multitheftauto.com/wiki/ES/Scripts_de_Cliente).

### Resources más complejos

La seccion previa es de como poner scripts de modo clientside, pero hay cosas mas posibles. Como se menciona al principio de este texto, los resources pueden hacer casi cualquier cosa. Su proposito es definido de porque hacen. Veamos unos resources teoricamente, por ver los archivos que tienen, el*meta.xml* y que podrian hacer:

#### Primer Ejemplo - Un script util

```
/admin_commands
	/meta.xml
	/commands.lua
	/client.lua
```

```
<meta>
	<info author="AlexD" description="Comandos de Admin" />
	<script src="commands.lua" />
	<script src="client.lua" type="client" />
</meta>
```

- El *commands.lua* tiene comandos de administrador, como banear a un jugador, mutearlo o cualquier cosa que pueda usar un administrador

- El *client.lua* tiene el GUI para poder ejecutar los comandos sencillamente.

Este ejemplo estaria corriendo todo el tiempo (talvez auto-empezado cuando el servidor empieza) Y es util durante toda la experiencia en el juego y tambien no interfiere con el Juego en general, al menos que un administrador decide de ejecutar algun acto, por supuesto.

#### Segundo Ejemplo - Un modo de Juego

```
/counterstrike
	/meta.xml
	/counterstrike.lua
	/buymenu.lua
```

```
<meta>
	<info author="AlexD" description="Recreacion de CounterStrike" type="gamemode" />
	<script src="counterstrike.lua" />
	<script src="buymenu.lua" type="client" />
</meta>
```

- El *counterstrike.lua* contiene lo similar a las siguientes caracteristicas:

- Dejar que los jugadores elijan su equipo y aparezcan en el

- Darles armas, objectivos e instrucciones (talvez leer de un Mapa, vease mas adelante)

- Definir las reglas del juego, ejemplo: cuando la partida acabe, que pasa cuando un jugador muere

- .. y talvez algo mas

- El *buymenu.lua* es un script Clientside y crea un menu para comprar armas

Este ejemplo puede ser llamado modo de juego, porque no solo interviene con el juego en general, pero actualmente define las reglas de el. El atributo *type* indica que este ejemplo sirve con el  [Map manager](mta://mapping/map-manager.md), si otro resource que fue escrito por el Equipo QA para gestionar modos de juego y carga de mapas. Es altamente recomendado que tu base tus modos de juego en las tecnicas que proporciona.

Esto tambien significa que el modo de juego no cargara sin el mapa. Los modos de juego tienen que ser tan genericos posibles. Un ejemplo de un mapa  es mostrado en el siguiente ejemplo.

#### Tercer ejemplo - Un mapa

```
/cs-airport
	/meta.xml
	/airport.map
	/airport.lua
```

```
<meta>
	<info author="Someguy" description="Counterstrike airport map" type="map" gamemodes="counterstrike" />
	<map src="airport.map" />
	<script src="airport.lua" />
</meta>
```

- El *airport.map* es un archivo XML que proporciona información sobre el mapa para el modo de juego, estos pueden incluir:

- Donde deben spawnear los jugadores, con que armas, que equipos hay

- Cuales son los objetivos

- Clima, tiempo, tiempo limite

- Proporcionar vehículos

- El *airport.lua* puede contener funciones del mapa específicas, que pueden incluir:

- Apertura de alguna puerta / hacer que algo explote cuando suceda algo específico

- Crear o mover algunos objetos personalizados, o manipular los objetos que se crean a través del archivo de mapa.

- .. cualquier cosa mapa-específicas que se pueda imaginar

Como puede ver, el atributo *type* cambió a 'map', diciéndole al [Map manager](mta://mapping/map-manager.md)  que este recurso es un mapa, mientras que el atributo *gamemodes* indica para que tipos de juego o gamemode este mapa es válido, en este caso el modo de juego en el ejemplo anterior. Lo que puede venir como una sorpresa es que también hay script en el recurso de mapa. Por supuesto, esto no es necesario en un mapa, pero abre un amplio abanico de posibilidades para los creadores de mapas para crear su propio mundo dentro de las reglas del modo de juego que para el que crean.

El archivo *airport.map* debe tener un aspecto similar a este:

```
<map mode="deathmatch" version="1.0">
	<terrorists>
		<spawnpoint posX="2332.23" posY="-12232.33" posZ="4.42223" skins="23-40" />
	</terrorists>
	<counterterrorists>
		<spawnpoint posX="2334.23443" posY="-12300.233" posZ="10.2344" skins="40-50" />
	</counterterrorists>

	<bomb posX="23342.23" posY="" posZ="" />
	
	<vehicle posX="" posY="" posZ="" model="602" />	
	<vehicle posX="" posY="" posZ="" model="603" />	
</map>
```

Cuando se inicia un modo de juego con un mapa, los resources del mapa se inicia automáticamente por el mapmanager y la información que contiene puede ser leída por el recursos del modo de juego. Cuando el mapa cambia, el recurso de mapa actual se detiene y se inicia el siguiente recurso de mapa. Para una explicación más detallada y ejemplos de cómo se utilizan los recursos del mapa en el main script, por favor visite la pagina [Writing Gamemodes](mta://mapping/writing-gamemodes.md).

### Eventos

Los eventos son la manera en la cual MTA le informa a los scripts cuando las cosas estan ocurriendo. Por ejemplo cuando un jugador muere, el evento [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md) es llamado. De manera de realizar cualquier accion cuando un jugador muere, tienes que prepararlo tu mismo, de manera similar a como cuando añades un command handler en[el primer capitulo](#Writing_the_script).

Este ejemplo mostrara un mensaje con el nombre del jugador que murió.

```
function playerDied(totalAmmo, killer, killerWeapon, bodypart)
	outputChatBox(getPlayerName(source).." died!")
end
addEventHandler("onPlayerWasted",getRootElement(),playerDied)
```

Instead of showing what arguments are needed, the documentation page for Events shows what parameters are passed to the handler function, similiar to the way a [command handler](#About_command_handlers) does, just that it is different from event to event. Another important point is the *source* variable, that exists in handler functions. It doesn't have to be added to the parameter list of the function, but it still exists. It has a different value from event to event, for player events (as in the example above) it is the player element. As another example, you can take a look at the basic spawning player script in the first section to get an idea how *source* is used.

## ¿Y ahora qué?

Deberías ya estar familiarizado con los aspectos básicos de los scripts de MTA, así como con la documentación. La [Página Principal](https://wiki.multitheftauto.com/wiki/ES/Pagina_Principal) te provee de enlaces con mayor información, así como tutoriales y Referencias que permiten una vista más profunda a los temas que te interesan.

Recomendamos que leas el tutorial de [debug](mta://scripting/concepts/debugging.md) (encuentro de errores). Es necesaria una buena habilidad con el "debug" cuando haces scripts. ¡Suerte en MTA!

## Traductores

- Benxamix2/The Kid

- AlexD

- Rockero
