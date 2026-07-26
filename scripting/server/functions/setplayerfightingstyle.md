---
doc_id: "mta-wiki:2503"
title: "SetPlayerFightingStyle"
source_title: "SetPlayerFightingStyle"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerFightingStyle"
revision_id: 49087
language: "en"
categories: ["Deprecated", "Server_functions"]
generated_at: "2026-07-26T16:16:43.712694+00:00"
---

# SetPlayerFightingStyle

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedFightingStyle instead. |  |

Changes a player's fighting style, most only change the 'special attack' which is done using the Aim and Enter keys.

**Fighting Styles:**

| Fighting Style | ID |
| --- | --- |
| STYLE_STANDARD | 4 |
| STYLE_BOXING | 5 |
| STYLE_KUNG_FU | 6 |
| STYLE_KNEE_HEAD | 7 |
| STYLE_GRAB_KICK | 15 |
| STYLE_ELBOWS | 16 |

## Syntax

```
setPlayerFightingStyle ( player thePlayer, int style )
```

### Required Arguments

- **thePlayer:** Tells the function to give the fighting style to a player

- **style:** A whole integer specifying the style of fighting you want to give to the player

## Example

Click to collapse [-]
Server

This example sets the player's fighting style to the desired style when he types "setstyle" followed by a number from 4 to 16 in console.

```
function consoleSetFightingStyle ( thePlayer, commandName, id )
	if ( thePlayer and id ) then                                                 -- If player and ID are specified
		local status = setPlayerFightingStyle ( thePlayer, tonumber(id) )    -- set the fighting style
		if ( not status ) then                                               -- if that failed
			outputConsole ( "Failed to set fighting style.", thePlayer ) -- show a message
		end
	end
end
addCommandHandler ( "setstyle",  consoleSetFightingStyle )
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
