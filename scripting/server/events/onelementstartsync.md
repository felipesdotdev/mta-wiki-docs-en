---
doc_id: "mta-wiki:5276"
title: "OnElementStartSync"
source_title: "OnElementStartSync"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementStartSync"
revision_id: 61001
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.118545+00:00"
---

# OnElementStartSync

This event is triggered when an element becomes synced by a player.

## Parameters

```
player newSyncer
```

- **newSyncer**: a [player](mta://reference/misc/player.md) element representing the player who is now syncing the [element](mta://reference/misc/element.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that got synced by a player.

## Example

Click to collapse [-]
Server

This example matches the model of the element to the player, when an element receives a new syncer.

```
function elementStartSync( newSyncer )
    local strElementType = getElementType( source )
    local playerVehicle = getPedOccupiedVehicle( newSyncer )
    if ( strElementType == 'vehicle' ) then
        if ( not playerVehicle ) then return false end
        
        setElementModel( source, getElementModel(playerVehicle) )
    elseif ( strElementType == 'ped' ) then
        setElementModel( source, getElementModel(newSyncer) )
    end
end
addEventHandler ('onElementStartSync', root, elementStartSync)
```

This example will prevent vehicles from entering a certain area by destroying them upon entrance

```
local myColShape = createColCuboid(1000, -800, 900, 1000, 1000, 1000)

function checkSyncOfVehicles()
	if isElement(source) and getElementType (source) == "vehicle" and isElementWithinColShape(source, myColShape) then
		destroyElement (source)
	end
end
addEventHandler ("onElementStartSync", root, checkSyncOfVehicles)
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- [onElementDestroy](mta://scripting/server/events/onelementdestroy.md)

- [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md)

- [onElementInteriorChange](mta://scripting/server/events/onelementinteriorchange.md)

- [onElementModelChange](mta://scripting/server/events/onelementmodelchange.md)

- onElementStartSync

- [onElementStopSync](mta://scripting/server/events/onelementstopsync.md)

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
