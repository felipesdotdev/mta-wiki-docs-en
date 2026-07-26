---
doc_id: "mta-wiki:2347"
title: "CountPlayersInTeam"
source_title: "CountPlayersInTeam"
source_url: "https://wiki.multitheftauto.com/wiki/CountPlayersInTeam"
revision_id: 82610
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CountPlayersInTeam

This function is for returning the number of players in the specified team.

## Syntax

```
int countPlayersInTeam ( team theTeam )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](https://wiki.multitheftauto.com/index.php?search=team):countPlayers(...)*

**Variable**: *.playerCount*

### Optional Arguments

- **theTeam:** The team you wish to retrieve the player count of.

### Returns

Returns an integer containing the number of players in the team, *false* if it could not be retrieved.

## Example

Click to collapse [-]
Example 1

This example adds a command in the console to find out how many players are on your team.

```
function outputTeamSize ( source, commandName )
	-- Get player's team
	local theTeam = getPlayerTeam ( source )
	-- If the player is in any team
	if theTeam then
		-- Tell the player how big his team is
		outputChatBox ( "Your team has " .. countPlayersInTeam ( theTeam ) .. " players.", source )
	else
		outputChatBox ( "You're not in a team.", source )
	end
end
addCommandHandler ( "teamsize", outputTeamSize )
```

Click to collapse [-]
Example 2

This example adds a command in the console to find out how many players are on your team, clientside

```
function outputTeamSize ( commandName )
	-- Get player's team
	local theTeam = getPlayerTeam ( getLocalPlayer() )
	-- If the player is in any team
	if team then
		-- Tell the player how big his team is
		outputChatBox ( "Your team has " .. countPlayersInTeam ( theTeam ) .. " players." )
	else
		outputChatBox ( "You're not in a team." )
	end
end
addCommandHandler ( "teamsize", outputTeamSize )
```

Click to collapse [-]
Example 3

This example balances a gamemode, to ensure equal number of players between the "grove" and "ballas" teams.  This could be triggered when a player joins the server, or for all players currently in the server when the gamemode starts.

```
function balanceTeams ( thePlayer )
	--get the team pointers from their names
	local groveTeam = getTeamFromName ( "grove" )
	local ballasTeam = getTeamFromName ( "ballas" )
	--count the number of players in each team, and store them
	local groveCount = countPlayersInTeam ( groveTeam )
	local ballasCount = countPlayersInTeam ( ballasTeam )
	if groveCount == ballasCount then --if the teams are equal
		setPlayerTeam ( thePlayer , groveTeam ) --place the player in grove
	elseif groveCount > ballasCount then --if there are more in grove
		setPlayerTeam ( thePlayer , ballasTeam ) --place him in ballas
	elseif groveCount < ballasCount then --if there are more in ballas
		setPlayerTeam ( thePlayer , groveTeam ) --place him in grove.
	end
end
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
