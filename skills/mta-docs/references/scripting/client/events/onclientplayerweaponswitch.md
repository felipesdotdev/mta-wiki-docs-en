---
doc_id: "mta-wiki:2686"
title: "OnClientPlayerWeaponSwitch"
source_title: "OnClientPlayerWeaponSwitch"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerWeaponSwitch"
revision_id: 69541
language: "en"
categories: ["Client_events"]
---

# OnClientPlayerWeaponSwitch

This event is triggered whenever the local player's equipped **[weapon slot](https://wiki.multitheftauto.com/index.php?search=weapon%20slot)** changes. This means giveWeapon and takeWeapon will trigger this event if the equipped slot is forced to change.

## Parameters

```
int previousWeaponSlot, int currentWeaponSlot
```

- **previousWeaponSlot**: An integer representing the previous [weapon slot](https://wiki.multitheftauto.com/index.php?search=weapon%20slot) the player had before he switched.

- **currentWeaponSlot**: An integer representing the new [weapon slot](https://wiki.multitheftauto.com/index.php?search=weapon%20slot) the player has after he switched.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) who switched their weapon (Local player only)

## Cancel effect

If this event is canceled, then the weapon will not be switched.

## Example

This example disables the use of aiming for the minigun.

```
function disableMinigunOnSwitch(prevSlot, curSlot)
	if getPedWeapon(localPlayer, curSlot) == 38 then --if the switched weapon is the minigun
		toggleControl("aim_weapon", false) --disable the aim button
	else --if it isnt the minigun
		toggleControl("aim_weapon", true) --renable the aim button
	end
end
addEventHandler("onClientPlayerWeaponSwitch", localPlayer, disableMinigunOnSwitch)
```

## See Also

### Client player events

- [onClientPlayerChangeNick](mta://scripting/client/events/onclientplayerchangenick.md)

- [onClientPlayerChoke](mta://scripting/client/events/onclientplayerchoke.md)

- [onClientPlayerDamage](mta://scripting/client/events/onclientplayerdamage.md)

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

- onClientPlayerWeaponSwitch

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
