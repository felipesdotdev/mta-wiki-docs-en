---
doc_id: "mta-wiki:4556"
title: "OnClientPedWeaponFire"
source_title: "OnClientPedWeaponFire"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedWeaponFire"
revision_id: 82060
language: "en"
categories: ["Client_events"]
---

# OnClientPedWeaponFire

This event is called when ped shoots a weapon.  This does not trigger for projectiles based, or melee weapons.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for peds that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
int weapon, int ammo, int ammoInClip, float hitX, float hitY, float hitZ, element hitElement
```

- **weapon**:  an [int](mta://reference/misc/int.md) representing [weapon](mta://reference/misc/weapons.md) used for making a shot.

- **ammo**: an [int](mta://reference/misc/int.md) ammount of ammo left for this weapon type.

- **ammoInClip**: an [int](mta://reference/misc/int.md) ammount of ammo left for this weapon type in clip.

- **hitX**: [float](mta://reference/misc/float.md) world X coordinate representing the hit point.

- **hitY**: [float](mta://reference/misc/float.md) world Y coordinate representing the hit point.

- **hitZ**: [float](mta://reference/misc/float.md) world Z coordinate representing the hit point.

- **hitElement**: an [element](mta://reference/misc/element.md) which was hit by a shot.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) who fired the weapon.

## Example

```
addEventHandler("onClientPedWeaponFire", root,
     function(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement)
          if isElement(hitElement) and getElementType(hitElement) == "player" then
               outputChatBox("You hit " .. getPlayerName(hitElement), 0, 255, 0)
          end
     end
)
```

## See Also

### Client ped events

- [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md)

- [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- [onClientPedHitByWaterCannon](mta://scripting/client/events/onclientpedhitbywatercannon.md)

- [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md)

- [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md)

- [onClientPedWasted](mta://scripting/client/events/onclientpedwasted.md)

- onClientPedWeaponFire

- [onClientPedStep](mta://scripting/client/events/onclientpedstep.md)

- [onClientPedChoke](mta://scripting/client/events/onclientpedchoke.md)

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
