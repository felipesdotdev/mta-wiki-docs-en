---
doc_id: "mta-wiki:5760"
title: "OnClientHUDRender"
source_title: "OnClientHUDRender"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientHUDRender"
revision_id: 31623
language: "en"
categories: ["Client_events"]
---

# OnClientHUDRender

This event is triggered before GTA renders the HUD. This is particularly useful if you want to use [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md) to capture the screen onto a texture without capturing the HUD, or to alter HUD textures using [shaders](mta://reference/misc/element-shader.md) before they are drawn onto the screen.

## Parameters

*None*

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](https://wiki.multitheftauto.com/index.php?search=root%20element).

## Example

```
local render_count = 0

addEventHandler("onClientHUDRender", root, function()
	render_count = render_count + 1
end)

addEventHandler("onClientRender", root, function()
	render_count = render_count - 1
end)

addCommandHandler("getLossFrames", function()
	outputChatBox("Loss: "..render_count)
	outputDebugString("Loss: "..render_count, 3, 255, 0, 0)
end)
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

- onClientHUDRender

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
