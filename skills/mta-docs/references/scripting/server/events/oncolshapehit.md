---
doc_id: "mta-wiki:1836"
title: "OnColShapeHit"
source_title: "OnColShapeHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnColShapeHit"
revision_id: 75903
language: "en"
categories: ["Server_Events"]
---

# OnColShapeHit

| [[{{{image}}}\|link=\|]] | Note: The hit won't be detected if the element that entered the colshape is a colshape. |
| --- | --- |
|  |  |

This event is triggered when a physical [element](mta://reference/misc/element.md) hits a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape).

## Parameters

```
element hitElement, bool matchingDimension
```

- **hitElement**: the [element](mta://reference/misc/element.md) that entered the colshape.

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) referring to whether the hit collision shape was in the same [dimension](mta://reference/misc/dimension.md) as the element.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) that got hit by a player or vehicle.

## Example

This example creates a hill area for a *King of the hill* gamemode.  When a player enters or leaves the area, it's announced in the chatbox.

```
-- create our hill area for our gamemode
local hillArea = createColRectangle ( -2171.0678710938, 678.17950439453, 15, 15 )

-- add hill_Enter as a handler for when a player enters the hill area
function hill_Enter ( thePlayer, matchingDimension )
        if getElementType ( thePlayer ) == "player" then --if the element that entered was player
                --let's get the name of the player
                local nameOfThePlayer = getPlayerName ( thePlayer )
	        --announce to everyone that the player entered the hill
	        outputChatBox ( nameOfThePlayer.." entered the zone!", root, 255, 255, 109 )
        end
end
addEventHandler ( "onColShapeHit", hillArea, hill_Enter )

-- add hill_Enter as a handler for when a player leaves the hill area
function hill_Exit ( thePlayer, matchingDimension )
        if getElementType ( thePlayer ) == "player" then --if the element that left was player
	        --check if the player is not dead
	        if isPlayerDead ( thePlayer ) ~= true then
                        --let's get the name of the player
                        local nameOfThePlayer = getPlayerName ( thePlayer )
	        	--if he was alive, announce to everyone that the player has left the hill
	        	outputChatBox ( nameOfThePlayer.." left the zone!", root, 255, 255, 109 )
	        end
        end
end
addEventHandler ( "onColShapeLeave", hillArea, hill_Exit )
```

## See Also

### Colshape events

- onColShapeHit

- [onColShapeLeave](mta://scripting/server/events/oncolshapeleave.md)

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
