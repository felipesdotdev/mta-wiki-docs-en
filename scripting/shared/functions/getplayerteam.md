---
doc_id: "mta-wiki:1694"
title: "GetPlayerTeam"
source_title: "GetPlayerTeam"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerTeam"
revision_id: 56863
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.625804+00:00"
---

# GetPlayerTeam

This function gets the current [team](mta://reference/misc/team.md) a [player](mta://reference/misc/player.md) is on.

## Syntax

```
team getPlayerTeam ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getTeam(...)*

**Variable**: *.team*

**Counterpart**: *[setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)*

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose team you want to find out.

### Returns

Returns a *team* element representing the team the player is on, *false* if the player is not part of a team.

## Example

Click to collapse [-]
Server

This example finds the team a player is on, and then changes its name.

```
function teamName ( source, key, newTeamName )
    local playerTeam = getPlayerTeam ( source )          -- get the player's team
    if ( playerTeam ) then                               -- if he's on a team
        local oldTeamName = getTeamName ( playerTeam )   -- get the team's current name
        setTeamName ( playerTeam, newTeamName )          -- change its name
        outputChatBox ( "Changed " .. getPlayerName ( source ).."'s team name from " .. oldTeamName .. " to " .. newTeamName )
    else
        outputChatBox ( getPlayerName ( source ) .. " isn't on a team" )
    end
end
addCommandHandler ( "teamname", teamName )
```

## See Also

- getPlayerTeam

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
