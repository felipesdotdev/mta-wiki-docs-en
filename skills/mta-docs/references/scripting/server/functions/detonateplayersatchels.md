---
doc_id: "mta-wiki:7434"
title: "DetonatePlayerSatchels"
source_title: "DetonatePlayerSatchels"
source_url: "https://wiki.multitheftauto.com/wiki/DetonatePlayerSatchels"
revision_id: 81187
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events"]
---

# DetonatePlayerSatchels

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function was introduced in 41342 and merged with detonateSatchels in 3af6a . |  |

This function detonates the thrown satchels of a player, as if they had fired the detonator. Please use [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md) instead.

## Syntax

```
bool detonatePlayerSatchels( player thePlayer )
```

### Required Arguments

- **thePlayer:** the player that should have their thrown satchels detonated.

### Returns

Returns *true* if a valid player element was passed, false otherwise.

## Example

This example will allow players to detonate their thrown satchels via the command /detonate

```
function cmdDetonateSatchels(plr)
	detonatePlayerSatchels(plr)
end
addCommandHandler("detonate", cmdDetonateSatchels)
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
