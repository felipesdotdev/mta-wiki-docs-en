---
doc_id: "mta-wiki:1415"
title: "GetPlayerSkin"
source_title: "GetPlayerSkin"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerSkin"
revision_id: 44568
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.466065+00:00"
---

# GetPlayerSkin

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getElementModel instead. |  |

This function returns an integer containing the ID number of the specified player's skin.

## Syntax

```
int getPlayerSkin ( player thePlayer )
```

### Required Arguments

- **player**: The player whose skin ID you want to retrieve.

### Returns

Returns an [int](mta://reference/misc/int.md) indicating which skin the player has. See [Character Skins](mta://reference/misc/character-skins.md).

## Example

Click to collapse [-]
Server

**Example 1:** This example spawns a player and tells him his skin

```
-- Spawn a player 
if ( spawnPlayer ( myPlayer, 1000, 1000, 1000, 90, 650 ) ) then
	-- Tell the player what skin they've spawned with
	outputChatBox ( "Your skin ID is: " .. getPlayerSkin ( myPlayer ), myPlayer )
end
```

**Example 2:** This example adds a "skin" command in console, which tells the player his/her skin.

```
function checkSkin ( source, commandName )
	outputChatBox ( "Your skin ID is: " .. getPlayerSkin ( source ), source )
end
addCommandHandler ( "skin", checkSkin )
```

Click to collapse [-]
Client

This example adds a "skin" command in console, which tells the player his/her skin.

```
function checkSkin ( commandName )
	outputChatBox ( "Your skin ID is: " .. getPlayerSkin ( getLocalPlayer() ) )
end
addCommandHandler ( "skin", checkSkin )
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
