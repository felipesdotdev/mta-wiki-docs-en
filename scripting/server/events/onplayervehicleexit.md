---
doc_id: "mta-wiki:3460"
title: "OnPlayerVehicleExit"
source_title: "OnPlayerVehicleExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerVehicleExit"
revision_id: 68473
language: "en"
categories: ["Server_Events", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:16:25.784051+00:00"
---

# OnPlayerVehicleExit

This event is triggered when a [player](mta://reference/misc/player.md) leaves a vehicle, for whatever reason.

## Parameters

```
vehicle theVehicle, int seat, ped jacker, bool forcedByScript
```

- **theVehicle**: a [vehicle](mta://reference/misc/vehicle.md) element representing the vehicle in which the player exited from.

- **seat**: an [int](mta://reference/misc/int.md) representing the seat in which the player was before exiting.

- **jacker**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element representing who jacked the driver.

- **forcedByScript:** a [boolean](mta://reference/misc/boolean.md) representing whether the exit was forced using [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md) or by the player.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) that left the vehicle.

## Example

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function addHelmetOnEnter ( vehicle, seat, jacked )
  if ( getVehicleID ( vehicle ) == 522 ) then -- if its a nrg
    addPedClothes ( source, "moto", "moto", 16 ) -- add the helmet
  end
end
addEventHandler ( "onPlayerVehicleEnter", root, addHelmetOnEnter )

function removeHelmetOnExit ( vehicle, seat, jacked )
  if ( getVehicleID ( vehicle ) == 522 ) then -- if its a nrg
    removePedClothes ( source, 16 ) -- remove the helmet
  end
end
addEventHandler ( "onPlayerVehicleExit", root, removeHelmetOnExit )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.3-9.11247 | Added forcedByScript argument |
| --- | --- |

## See Also

### Player events

- [onPlayerACInfo](mta://scripting/server/events/onplayeracinfo.md)

- [onPlayerBan](mta://scripting/server/events/onplayerban.md)

- [onPlayerChangeNick](mta://scripting/server/events/onplayerchangenick.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22790](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22790))

- [onPlayerChangesWorldSpecialProperty](mta://scripting/server/events/onplayerchangesworldspecialproperty.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22790](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22790))

- [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md)

- [onPlayerChat](mta://scripting/server/events/onplayerchat.md)

- [onPlayerClick](mta://scripting/server/events/onplayerclick.md)

- [onPlayerCommand](mta://scripting/server/events/onplayercommand.md)

- [onPlayerConnect](mta://scripting/server/events/onplayerconnect.md)

- [onPlayerContact](mta://scripting/server/events/onplayercontact.md)

- [onPlayerDamage](mta://scripting/server/events/onplayerdamage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22293](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22293))

- [onPlayerDetonateSatchels](mta://scripting/server/events/onplayerdetonatesatchels.md)

- [onPlayerJoin](mta://scripting/server/events/onplayerjoin.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r20463](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20463))

- [onPlayerDiscordJoin](mta://scripting/server/events/onplayerdiscordjoin.md)

- [onPlayerLogin](mta://scripting/server/events/onplayerlogin.md)

- [onPlayerLogout](mta://scripting/server/events/onplayerlogout.md)

- [onPlayerMarkerHit](mta://scripting/server/events/onplayermarkerhit.md)

- [onPlayerMarkerLeave](mta://scripting/server/events/onplayermarkerleave.md)

- [onPlayerModInfo](mta://scripting/server/events/onplayermodinfo.md)

- [onPlayerMute](mta://scripting/server/events/onplayermute.md)

- [onPlayerNetworkStatus](mta://scripting/server/events/onplayernetworkstatus.md)

- [onPlayerPickupHit](mta://scripting/server/events/onplayerpickuphit.md)

- [onPlayerPickupLeave](mta://scripting/server/events/onplayerpickupleave.md)

- [onPlayerPickupUse](mta://scripting/server/events/onplayerpickupuse.md)

- [onPlayerPrivateMessage](mta://scripting/server/events/onplayerprivatemessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22293](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22293))

- [onPlayerProjectileCreation](mta://scripting/server/events/onplayerprojectilecreation.md)

- [onPlayerQuit](mta://scripting/server/events/onplayerquit.md)

- [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md)

- [onPlayerSpawn](mta://scripting/server/events/onplayerspawn.md)

- [onPlayerStealthKill](mta://scripting/server/events/onplayerstealthkill.md)

- [onPlayerTarget](mta://scripting/server/events/onplayertarget.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22447](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22447))

- [onPlayerTeamChange](mta://scripting/server/events/onplayerteamchange.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22313](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22313))

- [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22459](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22459))

- [onPlayerTriggerInvalidEvent](mta://scripting/server/events/onplayertriggerinvalidevent.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22930](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22930))

- [onPlayerTeleport](mta://scripting/server/events/onplayerteleport.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- [onPlayerWeaponReload](mta://scripting/server/events/onplayerweaponreload.md)

- [onPlayerUnmute](mta://scripting/server/events/onplayerunmute.md)

- [onPlayerVehicleEnter](mta://scripting/server/events/onplayervehicleenter.md)

- onPlayerVehicleExit

- [onPlayerVoiceStart](mta://scripting/server/events/onplayervoicestart.md)

- [onPlayerVoiceStop](mta://scripting/server/events/onplayervoicestop.md)

- [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md)

- [onPlayerWeaponFire](mta://scripting/server/events/onplayerweaponfire.md)

- [onPlayerWeaponSwitch](mta://scripting/server/events/onplayerweaponswitch.md)

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
