---
doc_id: "mta-wiki:1855"
title: "GetPlayerWantedLevel"
source_title: "GetPlayerWantedLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerWantedLevel"
revision_id: 43557
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.871766+00:00"
---

# GetPlayerWantedLevel

This function gets a player's current wanted level. The wanted level is indicated by the amount of stars a player has on the GTA HUD.

## Syntax

Click to collapse [-]
Server

```
int getPlayerWantedLevel ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getWantedLevel(...)*

**Variable**: *.wantedLevel*

**Counterpart**: *[setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)*

### Required Arguments

- **thePlayer:** The player whose wanted level you wish to get

Click to collapse [-]
Client

```
int getPlayerWantedLevel ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).getWantedLevel(...)*

**Counterpart**: *[setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)*

### Returns

Returns an *int* from 0 to 6 representing the player's wanted level, *false* if the player does not exist.

## Example

Click to collapse [-]
Example 1: Server

This example finds which players in the server have a wanted level:

```
local players = getElementsByType ( "player" ) -- get a table of all the players in the server
for theKey,thePlayer in ipairs(players) do -- use a generic for loop to step through each player
   local level = getPlayerWantedLevel ( thePlayer ) -- get the wanted level of the player
   if ( level > 0 ) then -- if the player has any stars, announce it in the chat:
      outputChatBox ( getPlayerName ( thePlayer ) .. " has a wanted level of " .. level .. "  stars!" )
   end 
end
```

Click to collapse [-]
Example 2: Client

This script output your wanted level when you type /wanted.

```
function outputWantedLevel ()
local wantedLvl = getPlayerWantedLevel ( )
   if wantedLvl == 0 then
      outputChatBox ( "You clean", 0, 255, 0)
   else
      outputChatBox ( "You have "..wantedLvl.." wanted stars!", 255, 0, 0)
   end
end
addCommandHandler ( "wanted", outputWantedLevel )
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

- getPlayerWantedLevel

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
