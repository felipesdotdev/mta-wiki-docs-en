---
doc_id: "mta-wiki:4554"
title: "OnClientPedDamage"
source_title: "OnClientPedDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedDamage"
revision_id: 81992
language: "en"
categories: ["Client_events"]
---

# OnClientPedDamage

This event is triggered whenever a [ped](https://wiki.multitheftauto.com/index.php?search=ped) is damaged.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for peds that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element attacker, int weapon, int bodypart [, float loss ]
```

- **attacker**: A [player](https://wiki.multitheftauto.com/index.php?search=player) [element](mta://reference/misc/element.md) representing the attacker or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) [element](mta://reference/misc/element.md) (when a ped falls of a bike).

- **weapon**: An integer representing the [weapon ID](mta://reference/misc/weapons.md) the attacker used

- **bodypart**: An integer representing the bodypart the ped was damaged

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **loss**: A float representing the percentage of health the ped lost.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that got damaged

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), then any damaging effects to the ped will cease.

## Example

This example cancels any damage done to peds

```
function cancelPedDamage()
	cancelEvent() -- cancel any damage done to peds
end
addEventHandler("onClientPedDamage", root, cancelPedDamage)
```

## See Also

### Client ped events

- onClientPedDamage

- [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- [onClientPedHitByWaterCannon](mta://scripting/client/events/onclientpedhitbywatercannon.md)

- [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md)

- [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md)

- [onClientPedWasted](mta://scripting/client/events/onclientpedwasted.md)

- [onClientPedWeaponFire](mta://scripting/client/events/onclientpedweaponfire.md)

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
