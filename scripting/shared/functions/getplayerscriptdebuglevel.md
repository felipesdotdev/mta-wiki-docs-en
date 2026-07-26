---
doc_id: "mta-wiki:11913"
title: "GetPlayerScriptDebugLevel"
source_title: "GetPlayerScriptDebugLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerScriptDebugLevel"
revision_id: 81233
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:20.408916+00:00"
---

# GetPlayerScriptDebugLevel

This will allow you to retrieve the player current debug script level.

ADDED/UPDATED IN VERSION 1.6.0 [r22592](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22592):

This function has a client-sided variant, which can only retrieve the local player's script debug level.

## Syntax

Click to collapse [-]
Server

```
int getPlayerScriptDebugLevel( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getScriptDebugLevel(...)*

**Variable**: *.scriptDebugLevel*

**Counterpart**: *[setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)*

### Required Arguments

- **thePlayer:** The person whose debug script level you want

### Returns

Returns an *int* with the player debug script level, *false* if the player is invalid.

Click to collapse [-]
Client

```
int getPlayerScriptDebugLevel()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getScriptDebugLevel(...)*

**Variable**: *.scriptDebugLevel*

### Returns

Returns an *int* with the local player's debug script level.

## Example

Displays a message in the chat what is the player's debug level.

```
function showdebug (player)
    local level = getPlayerScriptDebugLevel( player )
    outputChatBox( "Your Script Debug Level: " .. level )
end
addCommandHandler ( "showdebug", showdebug )
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- getPlayerScriptDebugLevel

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
