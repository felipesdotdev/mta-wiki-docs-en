---
doc_id: "mta-wiki:14298"
title: "OnPlayerTriggerInvalidEvent"
source_title: "OnPlayerTriggerInvalidEvent"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerTriggerInvalidEvent"
revision_id: 79398
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:25.669932+00:00"
---

# OnPlayerTriggerInvalidEvent

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22459](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22459))

This event is triggered whenever a player trigger invalid event on server-side.

It works for both non-added and non-remote events.

## Parameters

```
string eventName, bool isAdded, bool isRemote
```

- **eventName**: An [string](mta://reference/misc/string.md) representing event name.

- **isAdded**: An [bool](mta://reference/misc/bool.md) representing whether called event is added.

- **isRemote**: An [bool](mta://reference/misc/bool.md) representing whether called event is remote.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who triggered invalid event.

## Example

This example allows you to kick/ban player which triggered invalid event.

```
local invalidEventCheckPunishment = true -- should player be punished upon detection (make sure that resource which runs this code has admin rights)
local eventCheckPunishmentBan = true -- only relevant if invalidEventCheckPunishment is set to true; use true for ban or false for kick
local eventCheckPunishmentReason = "Triggered invalid event" -- only relevant if invalidEventCheckPunishment is set to true; reason which would be shown to punished player
local eventCheckPunishedBy = "Console" -- only relevant if invalidEventCheckPunishment is set to true; who was responsible for punishing, as well shown to punished player
local eventCheckBanByIP = false -- only relevant if invalidEventCheckPunishment and eventCheckPunishmentBan is set to true; banning by IP nowadays is not recommended (...)
local eventCheckBanByUsername = false -- community username - legacy thing, hence is set to false and should stay like that
local eventCheckBanBySerial = true -- only relevant if invalidEventCheckPunishment and eventCheckPunishmentBan is set to true; (...) if there is a player serial to use instead
local eventCheckBanTime = 0 -- only relevant if invalidEventCheckPunishment and eventCheckPunishmentBan is set to true; time in seconds, 0 for permanent
local eventCheckDebugMessageLevel = 4 -- this debug level allows to hide INFO: prefix, and use custom colors
local eventCheckDebugMessageRed = 255 -- debug message - red color
local eventCheckDebugMessageGreen = 127 -- debug message - green color
local eventCheckDebugMessageBlue = 0 -- debug message - blue color

function onPlayerTriggerInvalidEvent(eventName, isAdded, isRemote)
	local playerName = getPlayerName(source)
	local eventAdded = isAdded and "yes" or "no"
	local eventRemote = isRemote and "yes" or "no"
	local eventActionTaken = (not invalidEventCheckPunishment and "none") or (eventCheckPunishmentBan and "ban" or "kick")
	local eventLogText = "[Events]: "..playerName.." triggered invalid event '"..eventName.."' (event added: "..eventAdded..", event remote: "..eventRemote..", action taken: "..eventActionTaken..")"

	outputDebugString(eventLogText, eventCheckDebugMessageLevel, eventCheckDebugMessageRed, eventCheckDebugMessageGreen, eventCheckDebugMessageBlue)

	if (not invalidEventCheckPunishment) then
		return false
	end

	if (eventCheckPunishmentBan) then
		banPlayer(source, eventCheckBanByIP, eventCheckBanByUsername, eventCheckBanBySerial, eventCheckPunishedBy, eventCheckPunishmentReason, eventCheckBanTime)
	else
		kickPlayer(source, eventCheckPunishedBy, eventCheckPunishmentReason)
	end
end
addEventHandler("onPlayerTriggerInvalidEvent", root, onPlayerTriggerInvalidEvent)
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

- [onPlayerStealthKill](mta://scripting/server/events/onplayerstealthkill.md)

- [onPlayerTarget](mta://scripting/server/events/onplayertarget.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22447](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22447))

- [onPlayerTeamChange](mta://scripting/server/events/onplayerteamchange.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22313](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22313))

- [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22459](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22459))

- onPlayerTriggerInvalidEvent

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
