---
doc_id: "mta-wiki:1703"
title: "GetTeamFromName"
source_title: "GetTeamFromName"
source_url: "https://wiki.multitheftauto.com/wiki/GetTeamFromName"
revision_id: 54899
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetTeamFromName

This function finds a [team](https://wiki.multitheftauto.com/index.php?search=team) element using the provided team name.

## Syntax

```
team getTeamFromName ( string teamName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Team.getFromName(...)*

### Required Arguments

- **teamName:** A string determining the name of the team you wish to find.

### Returns

Returns the [team](https://wiki.multitheftauto.com/index.php?search=team) element if it was found, *false* otherwise.

## Example

This example creates a team, and sets the player's team to it's partial name:

```
-- Creates a red team
createTeam("Red", 255, 0, 0)

function joinRedTeam (source)
	local redteam = getTeamFromName("Red")
	if (redteam) then -- If the team was successfully created
		-- Sets the player's team by getting the partial name of the red team.
		setPlayerTeam(client, readteam)
		outputChatBox("You are now in the 'Red' team", source)
	else
		outputChatBox("Sorry, we can't set your team. An error occurred!", source)
	end
end

--Add console command to join the team when 'joinTeam' is typed.
addCommandHandler("jointeam", joinRedTeam)
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- getTeamFromName

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
