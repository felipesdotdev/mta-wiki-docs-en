---
doc_id: "mta-wiki:12676"
title: "OnClientTransferBoxProgressChange"
source_title: "OnClientTransferBoxProgressChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientTransferBoxProgressChange"
revision_id: 81289
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.465831+00:00"
---

# OnClientTransferBoxProgressChange

This event is triggered every time the [resource](mta://reference/misc/resource.md) file downloader (aka. transfer box) updates the download progress.

## Parameters

```
float downloadedSizeTotal, float downloadTotalBytes
```

- **downloadedSizeTotal:** The total progress in bytes.

- **downloadTotalBytes:** The total size of the download in bytes.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Example

This example will show the percentage of the download progress, whenever a resource is started:

```
addEventHandler ("onClientTransferBoxProgressChange", root, function (downloadedSize, totalSize)
    local percentage = math.min ((downloadedSize / totalSize) * 100, 100)

    print (percentage .. "%")
end)
```

**NOTE**: The code must be in a separated resource. It will be responsible to be watching other resources.

## See Also

### Client other events

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

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- onClientTransferBoxProgressChange

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
