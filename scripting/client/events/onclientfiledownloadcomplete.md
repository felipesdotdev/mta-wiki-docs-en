---
doc_id: "mta-wiki:6116"
title: "OnClientFileDownloadComplete"
source_title: "OnClientFileDownloadComplete"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientFileDownloadComplete"
revision_id: 79348
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.489919+00:00"
---

# OnClientFileDownloadComplete

This event is triggered when a file has been downloaded after [downloadFile](mta://scripting/client/functions/downloadfile.md) has been successfully called.

## Parameters

```
string fileName, bool success, resource requestResource
```

- **fileName**: the file downloaded.

- **success**: whether successful or not.

ADDED/UPDATED IN VERSION 1.5.7-20468 :

- **requestResource**: the resource that called [downloadFile](mta://scripting/client/functions/downloadfile.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md) of the resource that downloaded file.

## Example

This example plays a sound if it was downloaded successfully

```
addEventHandler("onClientFileDownloadComplete", root, function(file, success)
    -- if the file relates to other resource
    if source ~= resourceRoot then
        return
    end

    -- if the file download failed
    if not success then
        outputChatBox(file..' failed to download')
        return
    end

    -- check if filename ends with .mp3
    if file:sub(-4) ~= '.mp3' then
        return
    end

    -- if so, play the sound
    playSound(file)
end)
```

## See Also

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- onClientFileDownloadComplete

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
