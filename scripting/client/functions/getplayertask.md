---
doc_id: "mta-wiki:2308"
title: "GetPlayerTask"
source_title: "GetPlayerTask"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerTask"
revision_id: 40321
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.605923+00:00"
---

# GetPlayerTask

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedTask instead. |  |

This function is used to get the name of the current task of a certain type for a player.

## Syntax

```
string getPlayerTask ( player thePlayer, string priority, int taskType, [int index = 0] )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose task you want to retrieve.

- **priority**: A string determining which set of tasks you want to retrieve it from. This must be either "primary" or "secondary".

- **taskType**: An integer value representing the task type (or slot) you want to get the task from. Types can be:

- **PRIMARY TASKS**

- **0:** TASK_PHYSICAL_RESPONSE

- **1:** TASK_EVENT_RESPONSE_TEMP

- **2:** TASK_EVENT_RESPONSE_NONTEMP

- **3:** TASK_PRIMARY

- **4:** TASK_DEFAULT

- **SECONDARY TASKS**

- **0:** TASK_SECONDARY_ATTACK

- **1:** TASK_SECONDARY_DUCK

- **2:** TASK_SECONDARY_SAY

- **3:** TASK_SECONDARY_FACIAL_COMPLEX

- **4:** TASK_SECONDARY_PARTIAL_ANIM

- **5:** TASK_SECONDARY_IK

### Optional Arguments

- **index**: An integer value representing how many sub tasks to go through. -1 to get the simplest task, 0 to get the most complex task.

### Returns

Returns a string containing the name of a task. See [list of player tasks](mta://reference/misc/list-of-player-tasks.md) for valid strings. Returns *false* if invalid arguments are specified or if there is no task of the type or index specified.

## Example

Click to collapse [-]
Client

This example prints the name of a player's task to the chat when they use the "task" command in the console.

```
function myTask ( commandName, priority, taskType )
    task = getPlayerTask ( source, priority, tonumber(taskType) )
    taskName = "none"
    if ( task ) then
        taskName = task
    end
    outputChatBox ( getPlayerName( source ) .. "'s " .. priority .. "(" .. taskType .. ") task is: " .. taskName )
end    
addCommandHandler ( "task", myTask )
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
