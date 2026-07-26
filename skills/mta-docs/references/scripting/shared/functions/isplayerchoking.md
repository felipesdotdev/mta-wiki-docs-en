---
doc_id: "mta-wiki:3382"
title: "IsPlayerChoking"
source_title: "IsPlayerChoking"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerChoking"
revision_id: 40332
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# IsPlayerChoking

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use isPedChoking instead. |  |

This function checks if the specified [player](https://wiki.multitheftauto.com/index.php?search=player) is choking (coughing) or not.  This happens as a result of weapons that produce smoke - smoke grenades, fire extinguisher and the spray can.

## Syntax

```
bool isPlayerChoking ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](https://wiki.multitheftauto.com/index.php?search=player) you wish to check

### Returns

Returns *true* if the player is choking, *false* otherwise.

## Example

This example checks if a random player is choking or not, and if so displays a message in the chat box.

```
aPlayer = getRandomPlayer ( )
if ( isPlayerChoking ( aPlayer ) ) then
	outputChatBox ( getClientName ( aPlayer ) .. " is choking.  Keep away from those cigarettes!" )
end
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
