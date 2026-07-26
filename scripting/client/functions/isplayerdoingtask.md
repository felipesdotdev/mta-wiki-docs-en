---
doc_id: "mta-wiki:2309"
title: "IsPlayerDoingTask"
source_title: "IsPlayerDoingTask"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerDoingTask"
revision_id: 49337
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:59.183805+00:00"
---

# IsPlayerDoingTask

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use isPedDoingTask instead. |  |

This function checks if the specified player is carrying out a certain [task](mta://reference/misc/list-of-player-tasks.md).

## Syntax

```
bool isPlayerDoingTask ( player thePlayer, string taskName )
```

### Required Arguments

- **thePlayer**: A [player](mta://reference/misc/player.md) object referencing the specified player.

- **taskName**: A string containing the name of the [task](mta://reference/misc/list-of-player-tasks.md) you're checking for.

### Returns

Returns *true* if the player is currently doing the task, *false* otherwise.

## Example

This example checks if the player who entered the 'doingdriveby' command is doing a drive-by (clientside).

```
function amIDoingADriveby ()
  if ( isPlayerDoingTask ( getLocalPlayer(), "TASK_SIMPLE_GANG_DRIVEBY" ) ) then
    outputChatBox ( getPlayerName ( getLocalPlayer() ) .. " is doing a driveby!!!" )
  else
    outputChatBox ( getPlayerName ( getLocalPlayer() ) .. " is not doing a driveby" )
  end
end
addCommandHandler ( "doingdriveby", amIDoingADriveby )
```

## See Also

- [getLocalPlayer](mta://scripting/client/functions/getlocalplayer.md)

- [getPlayerMapBoundingBox](mta://scripting/client/functions/getplayermapboundingbox.md)

- [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [isPlayerMapVisible](mta://scripting/client/functions/isplayermapvisible.md)

- [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22751](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22751):

- [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

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
