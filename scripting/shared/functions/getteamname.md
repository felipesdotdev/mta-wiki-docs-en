---
doc_id: "mta-wiki:1704"
title: "GetTeamName"
source_title: "GetTeamName"
source_url: "https://wiki.multitheftauto.com/wiki/GetTeamName"
revision_id: 63287
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:26.024051+00:00"
---

# GetTeamName

This function gets the team name of a team object.

## Syntax

```
string getTeamName ( team theTeam )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):getName(...)*

**Variable**: *.name*

**Counterpart**: *[setTeamName](mta://scripting/server/functions/setteamname.md)*

### Required Arguments

- **theTeam:** The team you want to retrieve the name of.

### Returns

Returns a string representing the team's name if the team object was valid, *false* otherwise.

## Example

This example gets the current team of a player, then prints its name to the chatbox.

```
function whatTeamAmIOn (source)
    -- Get the player's team (source is the player who entered the command)
    local playerTeam = getPlayerTeam(source)
  
    if (playerTeam) then -- if he was on a team
        outputChatBox(getPlayerName(source).." is on team: "..getTeamName(playerTeam))
    else
        outputChatBox(getPlayerName(source).. " isn't on a team")
    end
end

-- Add console command to find your team when 'whatTeamAmIOn' is typed.
addCommandHandler("whatTeamAmIOn", whatTeamAmIOn)
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- getTeamName
