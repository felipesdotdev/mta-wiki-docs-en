---
doc_id: "mta-wiki:4588"
title: "OnPedWasted"
source_title: "OnPedWasted"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedWasted"
revision_id: 82054
language: "en"
categories: ["Server_Events", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:24.295116+00:00"
---

# OnPedWasted

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

This event is triggered when a ped is killed or dies. It is not triggered for players.

## Parameters

```
int totalAmmo, element killer, int killerWeapon, int bodypart, bool stealth, int animGroup, int animID
```

- **totalAmmo**: an [int](mta://reference/misc/int.md) representing the total ammo the victim had when he died.

- **killer**: an [element](mta://reference/misc/element.md) representing the [player](mta://reference/misc/player.md), [ped](mta://reference/misc/ped.md) or [vehicle](mta://reference/misc/vehicle.md) who was the killer.  If there was no killer this is *false*.

- **killerWeapon**: an [int](mta://reference/misc/int.md) representing the [killer weapon](mta://reference/misc/weapons.md) or the [damage types](mta://reference/misc/damage-types.md).

- **bodypart**: an [int](mta://reference/misc/int.md) representing the bodypart ID the victim was hit on when he died.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **stealth**: a [boolean](mta://reference/misc/boolean.md) representing whether or not this was a stealth kill.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animGroup**: an [integer](mta://reference/misc/int.md) representing the ped's current animation group.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animID**: an [integer](mta://reference/misc/int.md) representing the ped's current animation ID.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](mta://reference/misc/ped.md) that died or got killed.

## Example

This example outputs to the console that the ped is now dead.

```
ped1 = createPed(112, 0, 0, 0) --Create our Ped
function died()
    outputConsole("Your Ped is dead now!")
end
addEventHandler("onPedWasted", ped1, died) --Add the Event when ped1 dies
```

## See Also

### Ped events

- [onPedDamage](mta://scripting/server/events/onpeddamage.md)

- [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md)

- [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md)

- onPedWasted

- [onPedWeaponSwitch](mta://scripting/server/events/onpedweaponswitch.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- [onPedWeaponReload](mta://scripting/server/events/onpedweaponreload.md)

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
