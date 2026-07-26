---
doc_id: "mta-wiki:2748"
title: "GetPlayerGravity"
source_title: "GetPlayerGravity"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerGravity"
revision_id: 44599
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetPlayerGravity

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedGravity instead. |  |

This function returns a float that contains the current gravity for the specified [player](https://wiki.multitheftauto.com/index.php?search=player).

## Syntax

```
float getPlayerGravity ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose gravity you want to check

### Returns

Returns a [float](mta://reference/misc/float.md) indicating the player's gravity, or *false* if the player is invalid. Default value is 0.008.

## Example

This example outputs the gravity of the player who entered the 'showGravity' command.

```
function showGravity ( thePlayer )
	local gravity = getPlayerGravity ( thePlayer )
	outputChatBox ( "Your gravity: " .. tostring(gravity), thePlayer )
end
addCommandHandler ( "showGravity", showGravity )
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
