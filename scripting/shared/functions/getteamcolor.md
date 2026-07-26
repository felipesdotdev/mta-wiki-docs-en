---
doc_id: "mta-wiki:1866"
title: "GetTeamColor"
source_title: "GetTeamColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetTeamColor"
revision_id: 40705
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:25.860878+00:00"
---

# GetTeamColor

This function retrieves the color of a team.

## Syntax

```
int, int, int getTeamColor ( team theTeam )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):getColor(...)*

### Required Arguments

- **theTeam:** The team you want to get the color of.

### Returns

Returns 3 integers representing the red, green, and blue color components of the team if it's valid, *false* otherwise.

## Example

Click to collapse [-]
Serverside example

This example defines a console command that outputs the player's team name and colors if he is on a team.

```
function teamInfo ( source )
    local r, g, b
    local playerTeam = getPlayerTeam( source )
  
    -- Make a string to print out the player's team information
    local text = getPlayerName ( source )

    if ( playerTeam ) then -- If the player is on a team (team is not false)
        -- Add the team name to the string
        text = text .. " is on " .. getTeamName ( playerTeam )
    
        -- Get the red, green, and blue values of the team's color
        r, g, b = getTeamColor ( playerTeam )
    
        -- Convert the colors to strings and add them to the string
        text = text .. " with team colors: " .. tostring(r) .. ", " .. tostring(g) .. ", " .. tostring(b)
    else                   -- if he's not on a team
        text = text .. " is not on a team."
    end

    -- Print the string with the player's team information
    outputChatBox ( text )
end

-- Add console command to print out your team information
addCommandHandler ( "teamInfo", teamInfo )
```

## See Also

- getTeamColor

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
