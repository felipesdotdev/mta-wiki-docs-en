---
doc_id: "mta-wiki:12655"
title: "Resource : OnElementSpawn"
source_title: "Resource:OnElementSpawn"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AOnElementSpawn"
revision_id: 73065
language: "en"
categories: []
generated_at: "2026-07-26T16:17:13.437759+00:00"
---

# Resource : OnElementSpawn

This Serverside Script adds the function: onElementSpawn.

**Download can be found at the** [MTA community page](https://community.multitheftauto.com/index.php?p=resources&s=details&id=18375)**.**

## Source

The source of this event is the element that spawned.

## Code

Click to collapse [-]
Clientside Script

```
addEventHandler("onClientElementStreamIn", root, function()
	if getElementType(source) == "vehicle" then
		triggerServerEvent("onElementSpawnCheck", localPlayer, source)
	end
end)
```

Click to collapse [-]
Serverside Script

```
addEvent("onElementSpawn", true)

function onElementSpawnCheck(element)
	triggerEvent("onElementSpawn", element)
end
addEvent("onElementSpawnCheck", true)
addEventHandler("onElementSpawnCheck", root, onElementSpawnCheck)
```

## Example Code

Click to collapse [-]
Serverside Example

```
local Vehicle = createVehicle(411, 100, 100, 100)

addEventHandler("onElementSpawn", root, function()
	if getElementType(source) == "vehicle" then
		setElementPosition(source, 0, 0, 3)
	end
end)
```

**Author: David13Systems**

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

- [onElementStartSync](mta://scripting/server/events/onelementstartsync.md)

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
