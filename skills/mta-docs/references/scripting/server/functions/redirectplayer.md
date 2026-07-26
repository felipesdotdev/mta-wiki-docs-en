---
doc_id: "mta-wiki:4269"
title: "RedirectPlayer"
source_title: "RedirectPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/RedirectPlayer"
revision_id: 80398
language: "en"
categories: ["Server_functions", "Changes_in_1.2"]
---

# RedirectPlayer

This function redirects the player to a specified server.

| [[{{{image}}}\|link=\|]] | Note: A resource using this function needs ACL rights in order to work (function.redirectPlayer) |
| --- | --- |
|  |  |

## Syntax

```
bool redirectPlayer ( player thePlayer, string serverIP = "", int serverPort = 0 [, string serverPassword = "" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):redirect(...)*

### Required Arguments

- **thePlayer:** The player you want to redirect

- **serverIP:** The IP address (or domain name that resolves to the IP address) of the server you want to redirect the player to. **Use an empty string to reconnect to the same server.**

- **serverPort:** The game port of the server you want to redirect the player to, this is usually 22003. **Set to zero to use the same port as the current server.**

### Optional Arguments

- **serverPassword:** The password for the server if it's protected

### Returns

Returns *true* if the player was redirected successfully, *false* if bad arguments were passed.

## Example

This example auto-redirects all connecting players to another given servers' IP:port.

```
local ip_port = "123.123.1.2:1234"	-- enter IP and port in format: 192.168.1.1:22003
local password = "password_placeholder" -- If the server is passworded insert password here (if no password, it wont use the value)

function onConnectRedirect()
	redirectPlayer(source, gettok(ip_port,1,":"), tonumber(gettok(ip_port,2,":")), password)
end
addEventHandler ("onPlayerJoin", root, onConnectRedirect)
```

This example adds a "joinserver" command using the syntax, "/joinserver serverIP serverPort [serverPassword]".

```
function joinserverHandlerFunction (playerSource, commandName, serverIP, serverPort, serverPassword)
	if serverIP and serverPort then --if IP and Port were specified
		if serverPassword then --if also a password was specified
			redirectPlayer (playerSource, serverIP, tonumber(serverPort), serverPassword) --redirect the player
		else -- else if no password was specified
			redirectPlayer (playerSource, serverIP, tonumber(serverPort))  --redirect the player without using the serverPassword parameter
		end
	else -- if no IP or Port have been specified
		outputChatBox ("Error! Correct Syntax: /joinserver IP Port [Password]", playerSource) --output an Error message to the chatbox
	end
end

addCommandHandler ("joinserver", joinserverHandlerFunction)
```

This example adds a "rejoin" command like the inbuilt reconnect command.

```
function rejoinMe(thePlayer, theCommand)
    redirectPlayer(thePlayer)
end
addCommandHandler("rejoin", rejoinMe) -- Attach rejoin command to our function
```

## See Also

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md)

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- redirectPlayer

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
  

- **Shared**

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
