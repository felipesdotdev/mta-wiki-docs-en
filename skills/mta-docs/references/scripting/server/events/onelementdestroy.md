---
doc_id: "mta-wiki:4228"
title: "OnElementDestroy"
source_title: "OnElementDestroy"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementDestroy"
revision_id: 59467
language: "en"
categories: ["Server_Events"]
---

# OnElementDestroy

This event is triggered when an element gets destroyed by [destroyElement](mta://scripting/shared/functions/destroyelement.md) or when the creator resource is stopping. It is also triggered when a parent element of this element is destroyed.

## Parameters

No parameters.

## Source

The source of this event is the element that is being destroyed.

## Example

This example sends a message to the vehicle occupants when it's being destroyed.

```
addEventHandler("onElementDestroy", getRootElement(), function ()
  if getElementType(source) == "vehicle" then
    local nPassengers = getVehicleMaxPassengers(source)
    for i=0,nPassengers-1 do
      local occupant = getVehicleOccupant(source, i)
      if occupant then
        outputChatBox("The vehicle that you were in has been destroyed by the script", occupant)
      end
    end
  end
end)
```

This example outputs a message every time an element is destroyed saying which resource created the element

```
function getSourceResourceOfElementDestruction()
	-- Players aren't destroyed by any resource
	if (getElementType(source) == "player") then
		outputChatBox("Player "..getPlayerName(source).." destroyed")
		return true
	end
	
	local sourceResourceRoot = getElementParent(getElementParent(source)) -- Get the resource root element of the element
	-- Now to get the resource from the resource root element
	local theResource = false
	for ind, res in pairs(getResources()) do -- Loop all resources
		if (getResourceRootElement(res) == sourceResourceRoot) then -- Compare each resources root element to what we've got
			theResource = res -- We've found the source
			break -- End the loop
		end
	end
	if (theResource) then -- Did we find it?
		local resourceName = getResourceName(theResource) -- Get the resources name
		outputChatBox(resourceName.." destroyed a "..getElementType(source)) -- Output the resource name along with element type
	end
end
addEventHandler("onElementDestroy", root, getSourceResourceOfElementDestruction) -- All elements
```

This example only works in builds above 1.3.4-5937 and will tell you if a script is causing bugs with other scripts if it's deleting elements from other scripts because element IDs are being re-used and some scripts don't dereference an element after destroying it.

```
function checkForNaughtyScriptsThatDeleteRandomElements()
	-- Ignore players
	if (getElementType(source) == "player") then
		return true
	end
	
	-- Get the resource that created the element
	local sourceResourceRoot = getElementParent(getElementParent(source))
	local theResource = false
	for ind, res in pairs(getResources()) do
		if (getResourceRootElement(res) == sourceResourceRoot) then
			theResource = res
			break
		end
	end
	
	-- Output info if the destroying resource isn't the same as the creator resource
	if (theResource and theResource ~= sourceResource) then
		local destroyerResource = tostring(getResourceName(theResource))
		local creatorResource = tostring(getResourceName(sourceResource))
		outputDebugString(destroyerResource.." destroyed a "..getElementType(source).." made by "..creatorResource)
	end
end
addEventHandler("onElementDestroy", root, checkForNaughtyScriptsThatDeleteRandomElements)
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- onElementDestroy

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
