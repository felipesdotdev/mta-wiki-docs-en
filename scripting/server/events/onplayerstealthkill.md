---
doc_id: "mta-wiki:5188"
title: "OnPlayerStealthKill"
source_title: "OnPlayerStealthKill"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerStealthKill"
revision_id: 72073
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:25.481234+00:00"
---

# OnPlayerStealthKill

This event is triggered when a player stealth kills another player.

## Parameters

```
element targetPlayer
```

- **targetPlayer**: the [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) that is being stealth killed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) that initiated the stealth kill.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), then the stealth kill is aborted.

## Example

Click to collapse [-]
Server

```
function onStealthKill(targetPlayer)
     outputChatBox("Stealth kill!", source) -- Tell the player he/she has done a stealth kill.
     outputChatBox(getPlayerName(targetPlayer).." has been stealth-killed by "..getPlayerName(source)..".")
end
addEventHandler("onPlayerStealthKill", root, onStealthKill) -- Adds a handler for the stealth kill event.
```

Click to collapse [-]
Server

```
function onStealthKill(targetPlayer)
     cancelEvent(true, "No more stealth kills.") -- Aborts the stealth-kill.
end
addEventHandler("onPlayerStealthKill", root, onStealthKill) -- Adds a handler for the stealth kill event.
```

Click to collapse [-]
Server

This example will prevent the stealthkill animation of the attacker as it occurs, something which is tricky to achieve (hence this example is extra useful).
Note: you won't get this to work properly without timer and 'fake' animation. Lots of scripters have broken their backs over this.

```
local function preventStealthAnimation(thePlayer)
    setPedAnimation(thePlayer, "ped", "0", -1, true, true, true, true, 350)
end

function onPlayerStealthKill(targetPlayer)
    setTimer(preventStealthAnimation, 50, 1, source)
end
addEventHandler("onPlayerStealthKill", root, onPlayerStealthKill)
```

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

- onPlayerStealthKill

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

- [onPlayerVehicleExit](mta://scripting/server/events/onplayervehicleexit.md)

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
