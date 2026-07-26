---
doc_id: "mta-wiki:1705"
title: "SetTeamName"
source_title: "SetTeamName"
source_url: "https://wiki.multitheftauto.com/wiki/SetTeamName"
revision_id: 80438
language: "en"
categories: ["Server_functions"]
---

# SetTeamName

This function is used to set a team's name.

## Syntax

```
bool setTeamName ( team theTeam, string newName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](https://wiki.multitheftauto.com/index.php?search=team):setName(...)*

**Variable**: *.name*

**Counterpart**: *[getTeamName](mta://scripting/shared/functions/getteamname.md)*

### Required Arguments

- **theTeam:** The [team](https://wiki.multitheftauto.com/index.php?search=team) you want to change the name of.

- **newName:** A string representing the name you want the team to be called.

### Returns

Returns *true* if the team was valid and the name was changed, *false* otherwise.

## Example

This example gets the current team of a player, then changes its name.

```
function changeMyTeamName ( source, key, newName )
    playerteam = getPlayerTeam ( source )            -- get the player's team
    if ( playerteam ) then                           -- if he was on a team
        oldName = getTeamName ( playerteam )         -- get the teams current name
        setTeamName ( playerteam, newName )          -- change the teams name to blue
        outputChatBox ( "Changed " .. getPlayerName ( source ) .. "'s team name from " .. oldName .. " to " .. newName )
    end
end
addCommandHandler ( "changeteamname", changeMyTeamName )
```

## See Also

- [createTeam](mta://scripting/server/functions/createteam.md)

- [setTeamColor](mta://scripting/server/functions/setteamcolor.md)

- [setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)

- setTeamName
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
