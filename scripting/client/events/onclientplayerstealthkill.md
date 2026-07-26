---
doc_id: "mta-wiki:5189"
title: "OnClientPlayerStealthKill"
source_title: "OnClientPlayerStealthKill"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerStealthKill"
revision_id: 71981
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.824298+00:00"
---

# OnClientPlayerStealthKill

This event is triggered when the local player stealth kills another player.

## Parameters

```
element targetPlayer
```

- **targetPlayer**: The [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) that is being stealth killed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) that initiated the stealth kill. (Local player only)

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), then the stealth kill is aborted.

## Example

This example disables stealth kills.

```
function abortAllStealthKills(targetPlayer)
    cancelEvent()
end
addEventHandler("onClientPlayerStealthKill", localPlayer, abortAllStealthKills)
```

This example disables stealth kills on a specific Ped.

```
local myNPC = createPed(187, 1481.265, -1752.25, 15.446, 0)

function antiKnife(targetPlayer)
    if targetPlayer == myNPC then
        cancelEvent()
    end
end
addEventHandler("onClientPlayerStealthKill", localPlayer, antiKnife)
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

- onClientPlayerStealthKill

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
