---
doc_id: "mta-wiki:2353"
title: "GetTeamFriendlyFire"
source_title: "GetTeamFriendlyFire"
source_url: "https://wiki.multitheftauto.com/wiki/GetTeamFriendlyFire"
revision_id: 40703
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:25.872193+00:00"
---

# GetTeamFriendlyFire

This function tells you if friendly fire is turned on for the specified team.

## Syntax

```
bool getTeamFriendlyFire ( team theTeam )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):getFriendlyFire(...)*

**Variable**: *.friendlyFire*

**Counterpart**: *[setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)*

### Required Arguments

- **theTeam:** The team object that will be checked

### Returns

Returns *true* if friendly fire is on for the specified team, *false* if it is turned off or if invalid arguments are specified.

## Example

This example makes a command that checks if friendly fire is on for each team, and toggles it on if it isn't.

```
function setFriendlyFireOn ( )
	-- For each team,	
	for index, theTeam in ipairs ( getElementsByType("team") ) do
	        -- if friendly fire is off,
	        if ( getTeamFriendlyFire ( theTeam ) == false ) then
	                -- switch it on.
	                setTeamFriendlyFire ( theTeam, true )
	        end
	end
end
-- Add console command 'setFF'
addCommandHandler ( "setFF", setFriendlyFireOn )
```

## See Also

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- getTeamFriendlyFire

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
