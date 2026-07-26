---
doc_id: "mta-wiki:1818"
title: "OnElementDataChange"
source_title: "OnElementDataChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementDataChange"
revision_id: 82492
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.027540+00:00"
---

# OnElementDataChange

This event is triggered *after* an element's [data](mta://reference/misc/element-data--975d1ea3.md) entry is changed. Such changes can be made on the client or the server using [setElementData](mta://scripting/shared/functions/setelementdata.md).

| [[{{{image}}}\|link=\|]] | Note: These predefined variables are special in this event: client : The client global variable is set to the client that called setElementData , or nil if it was called on the server. sourceResource : The resource which changed the element data - nil , if client synced data, resource element otherwise. |
| --- | --- |
|  |  |

## Parameters

```
string theKey, var oldValue, var newValue
```

- **theKey**: The name of the element data entry that has changed.

- **oldValue**: The old value of this entry before it changed. See [element data](mta://reference/misc/element-data--975d1ea3.md) for a list of possible datatypes.

- **newValue**: the new value of this entry after it changed. This will be equivalent to [getElementData](mta://scripting/shared/functions/getelementdata.md)(source, theKey).

## Cancelling

This event cannot be cancelled using [cancelEvent](mta://scripting/shared/functions/cancelevent.md). To reverse the effect, use [setElementData](mta://scripting/shared/functions/setelementdata.md) with the old value. See Example.

ADDED/UPDATED IN VERSION 1.7.0 [r25731](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25731):

This event can be cancelled using [cancelEvent](mta://scripting/shared/functions/cancelevent.md). If a client sent the cancelled change to the server, the server will send the client the server's version of the element data.

## Source

The source of this event is the [element](mta://reference/misc/element.md) whose element data changed.

## Example

Click to collapse [-]
Server

This example outputs a message to players when any of their element data values is changed.

```
function outputChange(theKey, oldValue, newValue)
    if (getElementType(source) == "player") then -- check if the element is a player
        outputChatBox("Your element data '" .. tostring(theKey) .. "' has changed from '" .. tostring(oldValue) .. "' to '" .. tostring(newValue) .. "'", source) -- output the change for the affected player
    end
end
addEventHandler("onElementDataChange", root, outputChange)
```

Click to collapse [-]
Server

This example checks and possibly reverses an element's data change.

```
function checkChange(theKey, oldValue)
    -- The client can only set 'special_thing' on its own player
    if (theKey== "special_thing") and (client ~= source) then
        outputChatBox("Illegal setting of " .. tostring(theKey) .. "' by '" .. tostring(getPlayerName(client)))
        setElementData(source, theKey, oldValue) -- Set back the original value
    end
end
addEventHandler("onElementDataChange", root, checkChange)
```

This example blocks all element data changes from clients. In MTA 1.7+ only.

```
function checkChange(theKey, oldValue, newValue)
    if (client) then -- if there's a client variable, it means it came from a player.
        cancelEvent()
    end
end
addEventHandler("onElementDataChange", root, checkChange)
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- onElementDataChange

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
