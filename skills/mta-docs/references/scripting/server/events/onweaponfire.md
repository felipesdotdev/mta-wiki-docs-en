---
doc_id: "mta-wiki:6992"
title: "OnWeaponFire"
source_title: "OnWeaponFire"
source_url: "https://wiki.multitheftauto.com/wiki/OnWeaponFire"
revision_id: 81156
language: "en"
categories: ["Server_Events"]
---

# OnWeaponFire

This event is triggered when a custom weapon gets fired.

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the element that fired the weapon. If the server is the creator it returns *nil*.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the bullet(s) won't be synced with other players.

## Example

```
addEventHandler( "onWeaponFire", root,
    function ()
        if ( isElement( source ) ) and ( getElementType( source ) == "player" ) then
            outputChatBox( "You fired a weapon!", source, 0, 225, 0 )
        end
    end
)
```

## See Also

### Weapon events

- onWeaponFire

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
