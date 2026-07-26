---
doc_id: "mta-wiki:6389"
title: "ES/Sistema de eventos"
source_title: "Evento"
source_url: "https://wiki.multitheftauto.com/wiki/Evento"
revision_id: 42286
language: "en"
categories: ["Translated/Scripting_Concepts"]
generated_at: "2026-07-26T16:10:42.212934+00:00"
---

# ES/Sistema de eventos

El sistema de eventos se encuentra en el núcleo del scripting de MTA. Los eventos funcionan en conjunto con el árbol de elementos. Los eventos son provocados cuando algo sucede - un jugador entra a un marcador, un elemento es cliqueado, etc. Cada evento tiene un elemento de origen, que es el que realiza la acción.

## Controladores de eventos

Para usar el sistema de eventos, se une o liga el controlador de eventos a los elementos en el árbol de elementos usando [addEventHandler](https://wiki.multitheftauto.com/wiki/ES/addEventHandler). Cuando se hace esto, las funciones serán activadas para todos los eventos que fueron provocados en ese elemento, sus padres e hijos. Por si mismo, un controlador de eventos ligado al elemento *raíz* será provocado cuando ocurra un evento para cualquier elemento. Como consecuencia se debe usar generalmente un controlador específico, cuando se pueda. Si solo se desea ver cuando el jugador entra a un marcador específico, solo se une el controlador de evento a dicho marcador.

Cada controlador de evento tiene dos variables 'ocultas':

- **source**: Este es el elemento que origina el evento.

- **this**: Este el elemento al cual se le provoca (p.ej. el que uniste con addEventHandler).

La variable *source* es la mas importante para la mayoría de los controladores. Casi siempre se querrá hacer referencia a esta variable para decir que elemento provoco el evento. La variable *this* tiene algunos usos para asegurarse de que el evento fue emitido por el elemento al que el controlador se unió.

Es *importante* notar que los eventos siguen la jerarquía de elementos. Inicialmente, todos los elementos provocan al elemento de *origen* (o *source* element), seguido de todos los elementos padres e hijos. Esto implica ciertas cosas:

- Un evento provocado sobre el elemento raíz se provocará en cada elemento dentro del árbol de elementos. Esto debe ser evitado cuando sea posible.

- Todos los eventos en cualquier parte dentro del árbol de elementos serán provocado sobre el elemento raíz. Esto significa que simplemente  se atrapa cada evento de un tipo provocando a un controlador hacia el elemento raíz. Esto solo se debe realizar si verdaderamente se quiere cada evento de ese tipo, de otra forma se une al lugar más específico en el árbol de elementos.

- Puedes unir un controlador de eventos al elementeo raíz de un resource para obtener todos los eventos provocados por los elementos que el resource contiene.

- Puedes crear elementos 'falsos' o 'dummy' para captar eventos de un grupo de elementos hijos.

- Puedes usar elementos falsos especificándolos dentro de un archivo .map (p.ej. <flag>) y crear representaciones 'reales' para ellos (p.ej. objectos) y hacer que sean elementos hijos reales de un elemento falso. Los controladores de eventos pueden entonces ser unidos al elemento falso y recibiran todos los eventos de los elementos reales. Esto es útil para cuando un resource maneja la representación del elemento (creando los objetos, por ejemplo), mientras otro desea controlar eventos especiales. Esto podría ser un resource de mapa que quiera controlar una bandera siendo capturada de alguna manera - el resource de mapa (generalmente) no sería consistente de la forma en que la bandera es representada. Esto no importa ya que este pordría solo unir los controladores a su elemento bandera falso mientras el otro resource de modo de juego puede controlar la representacion.

La función unida a un evento es llamada y pasada con un montón de argumentos. Estos argumentos son específicos del evento. Cada evento tiene parámetros específicos, por ejemplo [onClientGUIClick](https://wiki.multitheftauto.com/index.php?title=ES/onClientGUIClick&action=edit&redlink=1) tiene 4 parámetros, que son:

```
string botón, string estado, int xAbsoluto, int yAbsoluto
```

La función unida a este evento pasará estos parametros como argumentos. Debes recordar que cada evento tiene diferentes parámetros.

## Eventos incorporados

MTA tiene un número de eventos incorporados, los cuales se encuentran en [Client Scripting Events](mta://scripting/concepts/client-scripting-events.md) y [Scripting Events](mta://scripting/concepts/scripting-events.md).

## Eventos personalizados

Puedes crear tus propioas eventos que puedan ser provocados a travez de cualquier resource. Esta es una manéra importánte de comunicarse con otros resources y permitirles enlazarlos a tu código. Para agregar tus propios eventos, solo debes llamar la función [addEvent](https://wiki.multitheftauto.com/wiki/ES/addEvent). Luego puedes usar la función [triggerEvent](https://wiki.multitheftauto.com/index.php?title=ES/triggerEvent&action=edit&redlink=1) para provocar el evento en cualquier momento que quieras - incluso usando un timer, o basado en un evento general.

Por ejemplo, puedes hacer un modo de juego de Captura la Bandera y quieres provocar un evento cuando un jugador capture la bandera. Podrías haces esto uniendo un controlador de eventos al evento estándar de MTA [triggerEvent](https://wiki.multitheftauto.com/index.php?title=ES/onMarkerHit&action=edit&redlink=1) y verificar que el jugador que entró al marcador tiene la bandera. Si es así, entonces puedes provocar tu evento más específico *onFlagCaptured* y otros resources podrían controlarlo como ellos lo deseen.

## Cancelación

Los eventos pueden ser cancelados con [triggerEvent](https://wiki.multitheftauto.com/wiki/ES/cancelEvent). Esto puede tener una veriedad de consecuencias, pero en general significa que el servidor no realizará ninguna acción que debería hacer. Por ejemplo, cancelar el evento [onPickupUse](https://wiki.multitheftauto.com/index.php?title=ES/onPickupUse&action=edit&redlink=1) podría prevenir que un jugador se le de lo que intenta tomar de un pickup, cancelar el evento [onVehicleStartEnter](https://wiki.multitheftauto.com/index.php?title=ES/onVehicleStartEnter&action=edit&redlink=1) pordría prevenir que el jugador entre a un vehículo. Puedes comprobar si el evento actualmente activo ha sido cancelado usando [wasEventCanceled](https://wiki.multitheftauto.com/index.php?title=ES/wasEventCanceled&action=edit&redlink=1). Es importante notar que cancelar el evento *no* previene que otros controladores de evento sean provocados.
