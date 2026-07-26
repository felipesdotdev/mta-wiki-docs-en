---
doc_id: "mta-wiki:1702"
title: "RemovePlayerFromTeam"
source_title: "RemovePlayerFromTeam"
source_url: "https://wiki.multitheftauto.com/wiki/RemovePlayerFromTeam"
revision_id: 40344
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# RemovePlayerFromTeam

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPlayerTeam instead. |  |

This function is for removing a player from his current team.

## Syntax

```
bool removePlayerFromTeam ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The player you wish to remove from his team.

### Returns

Returns *true* if the player was on a team and was successfully removed it, *false* otherwise.

## Example

This example adds two new commands in console.  One to create a new team for a player, and another to remove the player from that team

```
function gimmeATeam ( source, key, teamName )
    local newTeam = createTeam ( teamName )  -- create a new team with the specified name
    if ( newTeam ) then                      -- if it was successfully created
        setPlayerTeam ( source, newTeam )  -- add the player to the new team
    end
end
addCommandHandler ( "gimmeateam", gimmeATeam )

function removeMyTeam ( source, key, teamName )
    local myTeam = getPlayerTeam ( source )--get his team
    if ( myTeam ) then --if he does have a team
        setPlayerTeam ( source, nil )      -- remove him from the team
        destroyElement ( myTeam ) --destroy his team
    end
end
addCommandHandler ( "removemyteam", removeMyTeam )
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
