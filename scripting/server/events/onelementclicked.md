---
doc_id: "mta-wiki:2337"
title: "OnElementClicked"
source_title: "OnElementClicked"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementClicked"
revision_id: 59463
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:23.972448+00:00"
---

# OnElementClicked

This event is triggered when an element is clicked on by the client. These events can only trigger when the client has its cursor enabled. It triggers for all three mousebuttons in both their up and down states.

## Parameters

```
string mouseButton, string buttonState, player playerWhoClicked, float clickPosX, float clickPosY, float clickPosZ
```

- **mouseButton**: a [string](mta://reference/misc/string.md) representing the mouse button that was clicked. This might be *left*, *middle* or *right*.

- **buttonState**: a [string](mta://reference/misc/string.md) representing what state the button clicked is in. This might be *up* or *down*.

- **playerWhoClicked**: the [player](mta://reference/misc/player.md) that clicked on the [element](mta://reference/misc/element.md).

- **clickPosX**: the X position in the world the [player](mta://reference/misc/player.md) clicked at.

- **clickPosY**: the Y position in the world the [player](mta://reference/misc/player.md) clicked at.

- **clickPosZ**: the Z position in the world the [player](mta://reference/misc/player.md) clicked at.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that got clicked by the player.

## Examples

This example prints type of the element you clicked to chatbox when you click it.

```
function elementClicked( theButton, theState, thePlayer )
    if theButton == "left" and theState == "down" then -- if left mouse button was pressed down
        outputChatBox( "You clicked " .. getElementType( source ), thePlayer ) -- print the element type to players chatbox
    end
end
addEventHandler( "onElementClicked", root, elementClicked ) -- add a handler function for the event
```

This example check if the clicked element is a vehicle. If is, then repairs it.

```
function repairClickedVehicle( button, state, player ) -- Add the function
    if button == "left" and state == "down" then
        if getElementType( source ) == "vehicle" then -- If the clicked element is a vehicle...
            local x, y, z = getElementPosition( player )
            local x1, y1, z1 = getElementPosition( source ) 
            local distance = getDistanceBetweenPoints3D( x, y, z, x1, y1, z1 ) -- Some distance calculations
            if distance < 4 then -- Check if the player is near the vehicle
                if getElementHealth( source ) < 1000 then
                    fixVehicle( source )
                    outputChatBox( "You have repaired a "..getVehicleNameFromModel( getElementModel( source ) ), player, 0, 255, 0 )
                else
                    outputChatBox( "Vehicle is not damaged!", player, 255, 0, 0 )
                end
            end
        end
    end
end
addEventHandler( "onElementClicked", root, repairClickedVehicle ) -- Add the event handler
```

## See Also

### Element events

- onElementClicked

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
