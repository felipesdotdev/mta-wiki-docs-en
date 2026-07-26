---
doc_id: "mta-wiki:2555"
title: "OnClientPlayerQuit"
source_title: "OnClientPlayerQuit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerQuit"
revision_id: 41612
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.748634+00:00"
---

# OnClientPlayerQuit

This event is triggered when a **remote** player quits the game or leaves the server. It **will not** get triggered on the source player's client. (Use [onClientResourceStop](mta://scripting/client/events/onclientresourcestop.md) to save client side data when the local player quits.)

## Parameters

```
string reason
```

- **reason**: A string representing the reason why the player quit.

- "Unknown"

- "Quit"

- "Kicked"

- "Banned"

- "Bad Connection"

- "Timed out"

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) that quit the game.

## Example

This example prints a message in the chatbox when a remote player leaves the server.

```
function onQuitGame( reason )
    outputChatBox ( getPlayerName( source ).." has left the server ("..reason..")" )
end
addEventHandler( "onClientPlayerQuit", getRootElement(), onQuitGame )
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

- onClientPlayerQuit

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
