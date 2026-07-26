---
doc_id: "mta-wiki:1379"
title: "SetPlayerArmor"
source_title: "SetPlayerArmor"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerArmor"
revision_id: 40562
language: "en"
categories: ["Deprecated", "Server_functions"]
generated_at: "2026-07-26T16:16:43.612839+00:00"
---

# SetPlayerArmor

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedArmor instead. |  |

This function allows you to set the armor value of a [player](mta://reference/misc/player.md).

## Syntax

```
bool setPlayerArmor ( player thePlayer, float playerArmor )
```

### Required Arguments

- **thePlayer**: the [player](mta://reference/misc/player.md) whose armor you want to modify.

- **playerArmor**: the amount of armor you want to set on the player. Valid values are from 0 to 100.

### Returns

Returns *true* if the armor was changed succesfully. Returns *false* if an invalid player is specified, or the armor value specified is out of acceptable range.

## Example

Click to collapse [-]
Server

This example removes the armor of a player.

```
function givePlayerArmor ( player, command )
	setPlayerArmor ( player, 100 ) --Set player's armor to 100 when he types the command 'addarmor'
end
addCommandHandler ( "addarmor", givePlayerArmor )

function removePlayerArmor ( player, command )
	setPlayerArmor ( player, 0 ) --Set player's armor to 0 when he types the command 'removearmor'
end
addCommandHandler ( "removearmor", removePlayerArmor )
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
