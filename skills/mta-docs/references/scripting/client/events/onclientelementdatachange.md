---
doc_id: "mta-wiki:2600"
title: "OnClientElementDataChange"
source_title: "OnClientElementDataChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementDataChange"
revision_id: 59655
language: "en"
categories: ["Client_events"]
---

# OnClientElementDataChange

This event is triggered *after* an element's [data](mta://reference/misc/element-data--975d1ea3.md) entry is changed. Such changes can be made on the client or the server using [setElementData](mta://scripting/shared/functions/setelementdata.md).

## Parameters

```
string theKey, var oldValue, var newValue
```

- **theKey**: The name of the element data entry that has changed.

- **oldValue**: The old value of this entry before it changed. See [element data](mta://reference/misc/element-data--975d1ea3.md) for a list of possible datatypes.

- **newValue**: the new value of this entry after it changed. This will be equivalent to [getElementData](mta://scripting/shared/functions/getelementdata.md)(source, theKey).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) whose [element data](mta://reference/misc/element-data--975d1ea3.md) changed.

## Example

This example tells the client whenever a player's "score" element data is changed.

```
function scoreChangeTracker(theKey, oldValue, newValue)
    if (getElementType(source) == "player") and (theKey == "score") then
        outputChatBox(getPlayerName(source).."'s new score is "..newValue.."!")
    end
end
addEventHandler("onClientElementDataChange", root, scoreChangeTracker)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- onClientElementDataChange

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

- [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md)

- [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md)

- [onClientElementStreamIn](mta://scripting/client/events/onclientelementstreamin.md)

- [onClientElementStreamOut](mta://scripting/client/events/onclientelementstreamout.md)

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
