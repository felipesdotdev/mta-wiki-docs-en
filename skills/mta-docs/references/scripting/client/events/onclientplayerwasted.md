---
doc_id: "mta-wiki:2560"
title: "OnClientPlayerWasted"
source_title: "OnClientPlayerWasted"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerWasted"
revision_id: 82047
language: "en"
categories: ["Client_events", "Changes_in_1.6.0"]
---

# OnClientPlayerWasted

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

This event is triggered whenever a player, including those remote, dies.

## Parameters

```
element killer, int weapon, int bodypart, bool stealth, int animGroup, int animID
```

- **killer**: A [player](https://wiki.multitheftauto.com/index.php?search=player), [ped](https://wiki.multitheftauto.com/index.php?search=ped) or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) [element](mta://reference/misc/element.md) representing the killer.

- **weapon**: An [integer](mta://reference/misc/int.md) representing the [killer weapon](mta://reference/misc/weapons.md) or the [damage types](mta://reference/misc/damage-types.md).

- **bodypart**: An [integer](mta://reference/misc/int.md) representing the bodypart the player was damaged.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **stealth**: A [boolean](mta://reference/misc/boolean.md) representing whether or not this was a stealth kill.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animGroup**: an [integer](mta://reference/misc/int.md) representing the player's current animation group.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animID**: an [integer](mta://reference/misc/int.md) representing the player's current animation ID.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) that died.

## Example

This example outputs a mocking message when the local player dies.

```
local messages = {
	"Better luck next time",
	"Don't think you're so cool now, do you?",
	"Nice one, pal",
	"Your opinion is void"
}

-- add an event for the local player only
addEventHandler("onClientPlayerWasted", localPlayer, function(killer, weapon, bodyPart)
	local randomMessage = messages[math.random(#messages)] -- get a random message from the table
	outputChatBox(randomMessage, 255, 0, 0) -- output the message
end)
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

- onClientPlayerWasted

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
