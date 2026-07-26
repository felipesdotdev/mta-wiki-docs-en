---
doc_id: "mta-wiki:1380"
title: "OnPlayerChat"
source_title: "OnPlayerChat"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerChat"
revision_id: 79288
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.599153+00:00"
---

# OnPlayerChat

This event is triggered when a player chats inside the chatbox.

## Parameters

```
string message, int messageType
```

- **message**: a [string](mta://reference/misc/string.md) representing the message typed into the chat.

- **messageType**: an [int](mta://reference/misc/int.md) value representing the message type:

- **0:** normal message

- **1:** action message (/me)

- **2:** team message

- **3:** private message

- **4:** internal message

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who sent the chatbox message.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the game's chat system won't deliver the posts. You may use [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) to send the messages then.
Cancelling this event also means the chat will not appear in the server console or logs. If you want chat logging, you will have to add a call to [outputServerLog](mta://scripting/server/functions/outputserverlog.md) - See the second example.

## Examples

Click to collapse [-]
Example 1

This example limits receiving of chat messages to area around the player who sent the message, also blocking action and team text.

```
local chatRadius = 20 -- define our chat radius

function onPlayerChatSendMessageToNearbyPlayers(messageText, messageType)
	local normalMessage = (messageType == 0) -- we will only send normal chat messages, action and team types will be ignored

	if (not normalMessage) then -- it's not normal message
		return false -- do not continue
	end

	local playerName = getPlayerName(source)
	local playerX, playerY, playerZ = getElementPosition(source) -- get position of player who sent the message
	local playerInterior = getElementInterior(source) -- get interior of same player
	local playerDimension = getElementDimension(source) -- dimension as well
	local nearbyPlayers = getElementsWithinRange(playerX, playerY, playerZ, chatRadius, "player", playerInterior, playerDimension) -- get nearby players within given radius
	local messageToOutput = playerName..": "..messageText

	outputChatBox(messageToOutput, nearbyPlayers, 255, 255, 255, true) -- output message to them
	cancelEvent() -- block the original message by cancelling this event
end
addEventHandler("onPlayerChat", root, onPlayerChatSendMessageToNearbyPlayers)
```

Click to collapse [-]
Example 2

This example implements colored player names in chat.

```
--This function is executed when a player joins, it sets the player's name-tag color to a random color.

local function playerJoin()
	local red, green, blue = math.random (50, 255), math.random (50, 255), math.random (50, 255)
        setPlayerNametagColor(source, red, green, blue)
end
addEventHandler ("onPlayerJoin", root, playerJoin)

--This function is executed when a player says something in chat, it outputs the player's message, with their nick colored to match their name tag color.

local function playerChat(message, messageType)
	if messageType == 0 then --Global (main) chat
                cancelEvent()
                local red, green, blue = getPlayerNametagColor(source)
		outputChatBox(getPlayerName(source)..": #FFFFFF"..message, root, red, green, blue, true )
		outputServerLog("CHAT: "..getPlayerName(source)..": "..message) -- Because we cancelled the onPlayerChat event, we need to log chat manually.
	end
end
addEventHandler("onPlayerChat", root, playerChat)
```

Click to collapse [-]
Example 3

This is a script that kills any player that says 'kill'.

```
function onChat(message, messageType)
    if string.find(message, 'kill') then  -- Searches for the string 'kill' in the message sent
        killPed ( source, source ) -- Kills that player that typed the string 'kill'
    end
end
addEventHandler("onPlayerChat", root, onChat)
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

- onPlayerChat

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
