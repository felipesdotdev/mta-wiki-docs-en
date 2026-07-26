---
doc_id: "mta-wiki:4874"
title: "OnClientPreRender"
source_title: "OnClientWorld"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientWorld"
revision_id: 82089
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.723905+00:00"
---

# OnClientPreRender

This event is triggered every time before GTA renders a new frame.

| [[\|link=\|]] | Warning: This event and onClientRender will trigger whatever function it is attached to with every frame. Depending on the server's maximum FPS and what your computer might handle - you might end up triggering the function 30-60 times per second . As a result, this event may cause severe lag and/or even crashes if not used cautiously. |
| --- | --- |
|  |  |

## Parameters

```
float timeSlice
```

- **timeSlice:** The interval between this frame and the previous one in milliseconds (delta time).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](mta://reference/misc/root-element.md).

## Example

This example makes the camera follow the player in a GTA2-like way.

```
function updateCamera ()
	local x, y, z = getElementPosition ( localPlayer )
	setCameraMatrix ( x, y, z + 50, x, y, z )
end
addEventHandler ( "onClientPreRender", root, updateCamera )
```

## See Also

### [Game Processing Order](mta://reference/misc/game-processing-order.md)

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md)

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- onClientPreRender

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md)

- [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md)

- [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
