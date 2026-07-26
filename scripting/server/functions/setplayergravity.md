---
doc_id: "mta-wiki:2624"
title: "SetPlayerGravity"
source_title: "SetPlayerGravity"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerGravity"
revision_id: 48928
language: "en"
categories: ["Deprecated", "Server_functions"]
generated_at: "2026-07-26T16:16:43.728888+00:00"
---

# SetPlayerGravity

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedGravity instead. |  |

## Description

This function sets the gravity level of a player.

## Syntax

```
setPlayerGravity ( player thePlayer, float level )
```

### Required Arguments

- **thePlayer**: The player whose gravity to change.

- **level**: The level of gravity ( default is **0.008** )

## Example

Click to collapse [-]
Server

This example allows the user to type a command to change their gravity:

```
function consoleSetPlayerGravity ( thePlayer, commandName, level )
	if ( thePlayer and level ) then
		local success = setPedGravity ( thePlayer, tonumber ( level ) )  -- Sets the gravity
		if (not success) then --Check if setPlayerGravity was false (not successful)
			outputConsole( "Failed to set player gravity", thePlayer )  -- If success is false, meaning gravity could not be set, this message will show
		end
	end
end
addCommandHandler ( "setplayergravity", consoleSetPlayerGravity )
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
