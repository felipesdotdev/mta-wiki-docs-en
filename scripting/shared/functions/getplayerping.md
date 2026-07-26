---
doc_id: "mta-wiki:1318"
title: "GetPlayerPing"
source_title: "GetPlayerPing"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerPing"
revision_id: 72064
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.248083+00:00"
---

# GetPlayerPing

This function returns the ping of a specified [player](mta://reference/misc/player.md). The ping is the number of milliseconds that data takes to travel from the player's client to the server or vice versa. If a player is using a VPN their ping will still be returned correctly.

## Syntax

```
int getPlayerPing ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getPing(...)*

**Variable**: *.ping*

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose ping you want to determine.

### Returns

Returns the ping as an [int](mta://reference/misc/int.md), or *false* if the player is invalid.

## Example

Click to collapse [-]
Server

This example checks every players ping every 5 seconds and if it's over 500 they get kicked.

```
function kickPing() -- Creates a function called kickPing
	for i, player in ipairs(getElementsByType("player")) do -- Loop every player
		if (getPlayerPing(player) >= 500) then -- If their ping is over 500
			kickPlayer(player, "Ping over 500!") -- Kick them
		end
	end
end
setTimer(kickPing, 5000, 0) -- Every 5 seconds, the kickPing function is called.
```

Click to collapse [-]
Client

This example checks the ping of every player entering the 'ping' command and warns him if it's over 100.

```
function checkPing()
        local ping = getPlayerPing(localPlayer)  -- get the ping from the source element (the player who joined)
        if (ping > 100) then                          -- if it's higher than 100...
                outputChatBox("Your ping is pretty high! Please try to lower it if possible.") -- output a message to the player
        end
end
addCommandHandler("ping", checkPing)
```

## See Also

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

- getPlayerPing

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
