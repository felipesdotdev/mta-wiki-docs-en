---
doc_id: "mta-wiki:3541"
title: "OnClientExplosion"
source_title: "OnClientExplosion"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientExplosion"
revision_id: 78763
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.468485+00:00"
---

# OnClientExplosion

This event is triggered every time an explosion is created on the current **clients scene** (inside the streamer).

## Parameters

```
float x, float y, float z, int theType
```

- **x:** X coordinate of where the explosion was created

- **y:** Y coordinate of where the explosion was created

- **z:** Z coordinate of where the explosion was created

- **theType:** the type of explosion created, see: [Explosion types](mta://reference/misc/explosion-types.md)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who created the explosion.
If the explosion is from a [vehicle](mta://reference/misc/vehicle.md) the source is the [player](mta://reference/misc/player.md) who syncs the vehicle.

### Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the explosion will not occur.

## Example

This example outputs the type of element that created the explosion into the chatbox.

```
function onClientExplosion(x, y, z, theType)
	outputChatBox("Explosion created by a "..getElementType(source))
end
addEventHandler("onClientExplosion", root, onClientExplosion)
```

## See Also

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- onClientExplosion

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md)

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

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
