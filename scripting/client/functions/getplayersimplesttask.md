---
doc_id: "mta-wiki:2312"
title: "GetPlayerSimplestTask"
source_title: "GetPlayerSimplestTask"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerSimplestTask"
revision_id: 40317
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.451206+00:00"
---

# GetPlayerSimplestTask

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedSimplestTask instead. |  |

This function is used to get the name of a specified players current simplest [task](mta://reference/misc/task.md).  

**DP2 note:** Don't call this on players that have not spawned. This will crash the client.

## Syntax

```
string getPlayerSimplestTask ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose [task](mta://reference/misc/task.md) you want to retrieve.

### Returns

Returns a string representing the name of the player's simplest, active [task](mta://reference/misc/task.md).

## Example

This example prints the name of a players simplest task to the chat, when they use the "sTask" command.

```
function showSTask ()
  local thetask = getPlayerSimplestTask ( getLocalPlayer() )
  outputChatBox ( getPlayerName ( getLocalPlayer() ) .. "'s simplest task is: " .. thetask )
end
addCommandHandler ( "sTask", showSTask )
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
