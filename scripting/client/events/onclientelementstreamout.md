---
doc_id: "mta-wiki:3855"
title: "OnClientElementStreamOut"
source_title: "OnClientElementStreamOut"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementStreamOut"
revision_id: 82050
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.446665+00:00"
---

# OnClientElementStreamOut

This event is triggered whenever a physical element is streamed out. This is triggered for all elements that are streamable, such as players, peds, vehicles, objects and markers when the local player is leaving the element. When this event is triggered, that element is no longer physical and is now virtualized by MTA.

| [[{{{image}}}\|link=\|]] | Note: Be aware that this event triggers for local player (as itself being the element that got streamed out) when said local player dies and respawns, as this is the removal & recreation of entity local ped. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This event is not triggered for elements that are streamed-in at the point of a destroyElement call. Use the onClientElementDestroy event in combination with the isElementStreamedIn function to handle such a case. |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that streamed out.

## Example

This example shows you how to tell player that another player was streamed out and the distance between them and said player

```
addEventHandler( "onClientElementStreamOut", root, 
    function ()
        if getElementType(source) == "player" then
            local x, y, z = getElementPosition(localPlayer)
            local xh, xy, xz = getElementPosition(source)
            local distance = getDistanceBetweenPoints3D(x, y, z, xh, xy, xz )
            outputChatBox( "A player has just streamed out. Distance to the player: " .. tostring(distance) .."." )
        end
    end
)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

- [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md)

- [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md)

- [onClientElementStreamIn](mta://scripting/client/events/onclientelementstreamin.md)

- onClientElementStreamOut

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
