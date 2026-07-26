---
doc_id: "mta-wiki:14501"
title: "OnShutdown"
source_title: "OnShutdown"
source_url: "https://wiki.multitheftauto.com/wiki/OnShutdown"
revision_id: 81528
language: "en"
categories: ["Server_Events", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:26.375547+00:00"
---

# OnShutdown

ADDED/UPDATED IN VERSION 1.6.0 [r22837](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22837):

This event is triggered when the server is about to be stopped using the server console or the [shutdown](mta://scripting/server/functions/shutdown.md) function. 

| [[{{{image}}}\|link=\|]] | Note: There is no 100% guarantee that all the code and operations executed in this event will finish before the server is stopped. Therefore, avoid complex actions like triggers or exports, as there may not be enough time to complete the operations and execute the full code |
| --- | --- |
|  |  |

## Parameters

```
resource theResource, string reason
```

- **theResource:** The [resource](mta://reference/misc/resource.md) that stops the server using the [shutdown](mta://scripting/server/functions/shutdown.md) function. If the server is being stopped from the console, the **resource** is set to **nil**.

- **reason:** The reason for stopping the server (if provided).

## Source

The [source](mta://reference/misc/event-system.md) of this event is **root**.

## Cancel effect

This event cannot be canceled.

## Example

```
addEventHandler('onShutdown', root, function(resource, reason)
    outputServerLog("Server shutdown by resource: "..(resource and getResourceName(resource) or "Unknown").." Reason: "..reason)
end)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- [onExplosion](mta://scripting/server/events/onexplosion.md)

- [onSettingChange](mta://scripting/server/events/onsettingchange.md)

- [onUnban](mta://scripting/server/events/onunban.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22837](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22837):

- onShutdown

### Event functions

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
