---
doc_id: "mta-wiki:2558"
title: "OnClientPlayerDamage"
source_title: "OnClientPlayerDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerDamage"
revision_id: 74507
language: "en"
categories: ["Client_events", "Changes_in_1.0"]
---

# OnClientPlayerDamage

This event is triggered whenever a player is damaged.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for players that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element attacker, int damage_causing, int bodypart [, float loss ]
```

- **attacker**: A [player](https://wiki.multitheftauto.com/index.php?search=player) [element](mta://reference/misc/element.md) representing the attacker or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) [element](mta://reference/misc/element.md) (when being run over or falling off a bike).

- **damage_causing**: An [int](mta://reference/misc/int.md) representing the cause of damage, either a [attacker weapon](mta://reference/misc/weapons.md), or some other [types of damage](mta://reference/misc/damage-types.md).

- **bodypart**: An integer representing the bodypart the player was damaged.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **loss**: A float representing the percentage of health the player lost.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) that got damaged. (Streamed in players only)

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), then any damaging effects to the local player will cease.

## Example

This example prevents any damage from the minigun.

```
function stopMinigunDamage(attacker, weapon, bodypart)
	if (weapon == 38) then --if the weapon used was the minigun
		cancelEvent() --cancel the event
	end
end
addEventHandler("onClientPlayerDamage", localPlayer, stopMinigunDamage)
```

## See Also

### Client player events

- [onClientPlayerChangeNick](mta://scripting/client/events/onclientplayerchangenick.md)

- [onClientPlayerChoke](mta://scripting/client/events/onclientplayerchoke.md)

- onClientPlayerDamage

- [onClientPlayerHeliKilled](mta://scripting/client/events/onclientplayerhelikilled.md)

- [onClientPlayerHitByWaterCannon](mta://scripting/client/events/onclientplayerhitbywatercannon.md)

- [onClientPlayerJoin](mta://scripting/client/events/onclientplayerjoin.md)

- [onClientPlayerPickupHit](mta://scripting/client/events/onclientplayerpickuphit.md)

- [onClientPlayerPickupLeave](mta://scripting/client/events/onclientplayerpickupleave.md)

- [onClientPlayerQuit](mta://scripting/client/events/onclientplayerquit.md)

- [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md)

- [onClientPlayerSpawn](mta://scripting/client/events/onclientplayerspawn.md)

- [onClientPlayerStealthKill](mta://scripting/client/events/onclientplayerstealthkill.md)

- [onClientPlayerStuntFinish](mta://scripting/client/events/onclientplayerstuntfinish.md)

- [onClientPlayerStuntStart](mta://scripting/client/events/onclientplayerstuntstart.md)

- [onClientPlayerTarget](mta://scripting/client/events/onclientplayertarget.md)

- [onClientPlayerVehicleEnter](mta://scripting/client/events/onclientplayervehicleenter.md)

- [onClientPlayerVehicleExit](mta://scripting/client/events/onclientplayervehicleexit.md)

- [onClientPlayerVoicePause](mta://scripting/client/events/onclientplayervoicepause.md)

- [onClientPlayerVoiceResumed](mta://scripting/client/events/onclientplayervoiceresumed.md)

- [onClientPlayerVoiceStart](mta://scripting/client/events/onclientplayervoicestart.md)

- [onClientPlayerVoiceStop](mta://scripting/client/events/onclientplayervoicestop.md)

- [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md)

- [onClientPlayerWeaponFire](mta://scripting/client/events/onclientplayerweaponfire.md)

- [onClientPlayerWeaponSwitch](mta://scripting/client/events/onclientplayerweaponswitch.md)

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
