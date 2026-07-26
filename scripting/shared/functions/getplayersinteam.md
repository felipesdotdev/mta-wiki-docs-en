---
doc_id: "mta-wiki:1769"
title: "GetPlayersInTeam"
source_title: "GetPlayersInTeam"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayersInTeam"
revision_id: 40702
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:21.704731+00:00"
---

# GetPlayersInTeam

This function retrieves all the players of the specified team.

## Syntax

```
table getPlayersInTeam ( team theTeam )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):getPlayers(...)*

**Variable**: *.players*

### Arguments

- **theTeam:** The team you wish to retrieve all the players from.

### Returns

Returns a [table](mta://reference/misc/table.md) of all the players in the team, or an empty one if there are none else false if invalid arguments are passed.

## Example

Click to collapse [-]
Server

Find and kill all the players in the specified team (for example 'killTeam Red').

```
function killTeamFunction ( thePlayer, command, teamName )
	-- Find and kill all the players in the team that was specified with the console command
	local theTeam = getTeamFromName ( teamName )
	if ( theTeam ) then
		local players = getPlayersInTeam ( theTeam )
		-- Loop through the player table
		for playerKey, playerValue in ipairs ( players ) do
			-- kill the player
			killPlayer ( playerValue )
		end
	end
end

addCommandHandler ( "killTeam", killTeamFunction )
```

Click to collapse [-]
Client

This example will show all players in a team when a player types the 'showTeam TeamName' command.

```
function showTeamFunction ( command, teamName )
        -- Find and show all the players in the team that was specified with the console command
        local theTeam = getTeamFromName ( teamName )
        if ( theTeam ) then
                local players = getPlayersInTeam ( theTeam ) 
                -- Loop through the player table
                for playerKey, playerValue in ipairs ( players ) do
                        outputChatBox ( getPlayerName(playerValue) )
                end
        end
end

addCommandHandler ( "showTeam", showTeamFunction )
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
