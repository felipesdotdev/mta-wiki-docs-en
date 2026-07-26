---
doc_id: "mta-wiki:2550"
title: "OnClientWeaponFire"
source_title: "OnClientWeaponFire"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientWeaponFire"
revision_id: 62456
language: "en"
categories: ["Client_events"]
---

# OnClientWeaponFire

This event triggers when a [custom weapon](mta://reference/misc/element-weapon.md) fires a shot.

| [[{{{image}}}\|link=\|]] | Note: This event is ONLY for custom weapons that were created with createWeapon , for regular weapons use onClientPlayerWeaponFire . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for custom weapons that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element hitElement, float posX,  float posY, float posZ, float normalX, float normalY, float normalZ, int materialType, float lighting, int pieceHit
```

- **hitElement:** the element that was hit

- **posX:** the position it will hit

- **posY:** the position it will hit

- **posZ:** the position it will hit

- **normalX:** the normal it hit ( see processLineOfSight )

- **normalY:** the normal it hit ( see processLineOfSight )

- **normalZ:** the normal it hit ( see processLineOfSight )

- **materialType:** the material type it hit ( see processLineOfSight )

- **lighting:** the lighting of the entity it hit ( see processLineOfSight )

- **pieceHit:** the piece of the entity it hit ( see processLineOfSight )

## Source

The [source](mta://reference/misc/event-system.md) of this event is the weapon that was fired.

## Cancel Effect

If this event was [canceled](mta://reference/misc/event-system.md), then the weapon will not fire.

## Example

This example prevents player damage from custom weapons.

```
function noDamageToPlayersFromCustomWeapons(target)
    if target == localPlayer then
        cancelEvent() -- If the weapon hit the player, cancel the shot
    end
end
addEventHandler("onClientWeaponFire", root, noDamageToPlayersFromCustomWeapons)
```

## See Also

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
