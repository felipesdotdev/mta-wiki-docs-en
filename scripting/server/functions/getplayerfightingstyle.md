---
doc_id: "mta-wiki:2619"
title: "GetPlayerFightingStyle"
source_title: "GetPlayerFightingStyle"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerFightingStyle"
revision_id: 44597
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:19.274843+00:00"
---

# GetPlayerFightingStyle

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedFightingStyle instead. |  |

This allows you to retrieve what fighting style a player is currently using.

## Syntax

```
int getPlayerFightingStyle ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The player whose current fighting style ID you wish to retrieve

### Returns

Returns the player's current fighting style as an integer ID, *false* if it fails to retrieve a value.

**Fighting Styles:**

| Fighting Style | ID |
| --- | --- |
| STYLE_STANDARD | 4 |
| STYLE_BOXING | 5 |
| STYLE_KUNG_FU | 6 |
| STYLE_KNEE_HEAD | 7 |
| STYLE_GRAB_KICK | 15 |
| STYLE_ELBOWS | 16 |

## Example

This will allow any player to check what fighting style they are currently using, by typing the 'getfightingstyle' command.

```
function getPlayerFightStyle ( thePlayer, commandName )
	local playerstyle = getPlayerFightingStyle ( thePlayer )   -- store the fighting style in a variable
	outputChatBox ( tostring(playerstyle), thePlayer )         -- output it to the player
end
addCommandHandler ( "getfightingstyle", getPlayerFightStyle )
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
