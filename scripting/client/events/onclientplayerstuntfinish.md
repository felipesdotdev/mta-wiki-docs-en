---
doc_id: "mta-wiki:3437"
title: "OnClientPlayerStuntFinish"
source_title: "OnClientPlayerStuntFinish"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerStuntFinish"
revision_id: 72069
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.845613+00:00"
---

# OnClientPlayerStuntFinish

This event is triggered whenever the local player finishes a vehicle stunt.

## Parameters

```
string stuntType, int stuntTime, float stuntDistance
```

- **stuntType**: the type of stunt the player just performed. Valid types are:

- 2wheeler

- wheelie

- stoppie

- **stuntTime**: the number of miliseconds the stunt lasted.

- **stuntDistance**: the distance traveled while doing the stunt.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the local [player](mta://reference/misc/player.md).

## Example

This is a simple stunt script which tells player what stunt he/she started and finished, time the stunt taken to perform and distance travelled while stunting.

```
function onClientPlayerStuntStart(stuntType)
    outputChatBox("You started stunt: "..stuntType)
end
addEventHandler("onClientPlayerStuntStart", localPlayer, onClientPlayerStuntStart)

function onClientPlayerStuntFinish(stuntType, stuntTime, stuntDistance)
    outputChatBox("You finished stunt: "..stuntType..", time: "..stuntTime..", distance: "..stuntDistance)
end
addEventHandler("onClientPlayerStuntFinish", localPlayer, onClientPlayerStuntFinish)
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

- onClientPlayerStuntFinish

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
