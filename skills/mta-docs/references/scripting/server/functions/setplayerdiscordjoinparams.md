---
doc_id: "mta-wiki:11579"
title: "SetPlayerDiscordJoinParams"
source_title: "SetPlayerDiscordJoinParams"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerDiscordJoinParams"
revision_id: 82579
language: "en"
categories: ["Server_functions"]
---

# SetPlayerDiscordJoinParams

| [[{{{image}}}\|link=\|]] | Important Note: This function was removed, read https://github.com/multitheftauto/mtasa-blue/pull/2499 for more information. |
| --- | --- |
|  |  |

Use empty string for **key** parameter to disable join/invite feature.

## Syntax

```
bool setPlayerDiscordJoinParams ( element thePlayer, string key, string partyId, int partyCurrentSize, int partyMaxSize )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setDiscordJoinParams(...)*

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose discord join parameters will be set on.

- **key:** The key which will be called upon invited users (or users who joined the game by clicking "Join") onPlayerJoin event. (Limited to 64 characters, must not contain space character)

- **partyId:** Changing the partyId is useful to make invites expire. (Limited to 64 characters, must not contain space character)

- **partyCurrentSize:** The current number of used capacity for other users to join. (Can't be more than partyMaxSize)

- **partyMaxSize:** The total capacity for users inside the party. (Can't be greater than server max players)

### Returns

Returns *true* if the value was set successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

```
function makeSomeParty ( playerSource, cmdName )
    setPlayerDiscordJoinParams(playerSource, "abcdefghijklmnopqrstuvwxyz", "abc123456", 1, 5)
end

addCommandHandler ( "makeParty", makeSomeParty )
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
