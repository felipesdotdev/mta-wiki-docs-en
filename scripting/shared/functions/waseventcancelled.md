---
doc_id: "mta-wiki:3433"
title: "WasEventCancelled"
source_title: "WasEventCancelled"
source_url: "https://wiki.multitheftauto.com/wiki/WasEventCancelled"
revision_id: 75037
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:06.355369+00:00"
---

# WasEventCancelled

This function checks if the last completed event was cancelled. This is mainly useful for custom events created by scripts.

Events can be cancelled using [cancelEvent](mta://scripting/shared/functions/cancelevent.md), this indicates that the resource which triggered the event should do whatever it can to reverse any changes made by whatever caused the event. See [triggerEvent](mta://scripting/shared/functions/triggerevent.md) for a more detailed explanation of this.

## Syntax

```
bool wasEventCancelled ( )
```

### Returns

Returns *true* if the event was cancelled, *false* if it wasn't or doesn't exist.

## Example

This example implements a custom event *onFlagPickup* that would be triggered if an *onMarkerHit* event was triggered on a marker whose parent was a *flag* element. If the event isn't canceled then an element data value is set on the player.

```
addEvent ( "onFlagPickup", true )

function flagHitcheck ( thePlayer )
    parentElement = getElementParent ( source ) -- get the parent of the marker
    if ( getElementType ( parentElement ) == "flag" ) then -- if it was a flag element then
        triggerEvent ( "onFlagPickup", source, thePlayer ) -- trigger our onFlagPickup event
        
        if ( not wasEventCancelled() ) then -- if handlers for 'onFlagPickup' didn't cancel it then
            setElementData ( thePlayer, "hasFlag", true ) -- set that the player picked up the flag
        end
    end
end
addEventHandler ( "onMarkerHit", getRootElement(), flagHitCheck )
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- wasEventCancelled
