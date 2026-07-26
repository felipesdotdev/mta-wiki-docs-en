---
doc_id: "mta-wiki:12675"
title: "OnClientResourceFileDownload"
source_title: "OnClientResourceFileDownload"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientResourceFileDownload"
revision_id: 81288
language: "en"
categories: ["Client_events"]
---

# OnClientResourceFileDownload

This event is triggered every time a [resource](mta://reference/misc/resource.md) file download is queued, finished or has failed.

|  | Warning: This event is NOT related to downloadFile and onClientFileDownloadComplete ! |
| --- | --- |
|  |  |

## Parameters

```
resource fileResource, string fileName, int fileSize, string state
```

- **fileResource:** [Resource](mta://reference/misc/resource.md) the file belongs to.

- **fileName:** Relative [resource](mta://reference/misc/resource.md) file path.

- **fileSize:** Size of the file in bytes.

- **state:** Possible values: `"queued"` or `"finished"` or `"failed"`.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the resource's root element.

## Example

This example will output the file's resource name/file name/size/state when downloading:

```
function writeMsg (fileResource, fileName, fileSize, state)
    local resourceName = getResourceName( fileResource )
    outputChatBox ( "Resource name: " .. resourceName .. ", file name: " .. fileName .. ", size: " .. fileSize .. ", state: " .. state)
end

addEventHandler ("onClientResourceFileDownload", root, writeMsg)
```

## See Also

### Client resource events

- onClientResourceFileDownload

- [onClientResourceStart](mta://scripting/client/events/onclientresourcestart.md)

- [onClientResourceStop](mta://scripting/client/events/onclientresourcestop.md)

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
