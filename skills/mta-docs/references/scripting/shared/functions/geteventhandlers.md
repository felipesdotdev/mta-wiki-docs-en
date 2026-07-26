---
doc_id: "mta-wiki:7026"
title: "GetEventHandlers"
source_title: "GetEventHandlers"
source_url: "https://wiki.multitheftauto.com/wiki/GetEventHandlers"
revision_id: 82679
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4"]
---

# GetEventHandlers

This function gets the attached functions from the event and attached element from current lua script.

| [[{{{image}}}\|link=\|]] | Important Note: This function only checks the current script. |
| --- | --- |
|  |  |

## Syntax

```
table getEventHandlers ( string eventName, element attachedTo )
```

### Required Arguments

- **eventName:** The name of the event. For example ( "onPlayerWasted" ).

- **attachedTo:** The [element](mta://reference/misc/element.md) attached to.

### Returns

Returns table with attached functions, empty table otherwise.

### Example

Click to collapse [-]
Server

```
function isEventHandlerAdded( sEventName, pElementAttachedTo, func )
	if type( sEventName ) == 'string' and isElement( pElementAttachedTo ) and type( func ) == 'function' then
	    local aAttachedFunctions = getEventHandlers( sEventName, pElementAttachedTo )
		if type( aAttachedFunctions ) == 'table' and #aAttachedFunctions > 0 then
			for i, v in ipairs( aAttachedFunctions ) do
				if v == func then
					return true
				end
			end
		end
	end
	return false
end

function onPlayerWasted()
	outputChatBox( getPlayerName( source ) .. ' died.' )
end
addEventHandler( 'onPlayerWasted', root, onPlayerWasted )

addCommandHandler( 'removeOnPlayerWastedEvent', function()
    if isEventHandlerAdded( 'onPlayerWasted', root, onPlayerWasted ) then
        outputChatBox( 'onPlayerWasted succesfully removed!' )
        removeEventHandler( 'onPlayerWasted', root, onPlayerWasted )
    end
end)
```

Click to collapse [-]
Clientside example

This example removes all onClientMarkerHit event in current script.

```
local events = getEventHandlers ( "onClientMarkerHit", resourceRoot )
for i,v in ipairs(events) do 
    removeEventHandler ( "onClientMarkerHit", resourceRoot, v) 
end
```

## See also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- getEventHandlers

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
