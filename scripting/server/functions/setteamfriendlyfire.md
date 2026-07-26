---
doc_id: "mta-wiki:2354"
title: "SetTeamFriendlyFire"
source_title: "SetTeamFriendlyFire"
source_url: "https://wiki.multitheftauto.com/wiki/SetTeamFriendlyFire"
revision_id: 80437
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:45.444760+00:00"
---

# SetTeamFriendlyFire

This function sets the friendly fire value for the specified team.

## Syntax

```
bool setTeamFriendlyFire ( team theTeam , bool friendlyFire )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):setFriendlyFire(...)*

**Variable**: *.friendlyFire*

**Counterpart**: *[getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)*

### Required Arguments

- **theTeam:** The  [team](mta://reference/misc/team.md) that will have friendly fire set

- **friendlyFire:** A boolean denoting whether the players from the same team can kill each other (*true*) or whether the players can't kill each other (*false*).

### Returns

Returns *true* if the friendly fire value is set for the specified team, *false* if the friendly fire value can't be set for the specified team or if invalid arguments are specified.

## Example

This example checks if friendly fire is on for every team, and toggles it on if it isn't.

```
-- get a table with all teams
local allTeams = getElementsByType ( "team" )
-- for every team,
for index, theTeam in ipairs(allTeams) do
	-- if friendly fire is off,
	if ( getTeamFriendlyFire ( theTeam ) == false ) then
		-- switch it on
		setTeamFriendlyFire ( theTeam, true )
	end
end
```

## See Also

- [createTeam](mta://scripting/server/functions/createteam.md)

- [setTeamColor](mta://scripting/server/functions/setteamcolor.md)

- setTeamFriendlyFire

- [setTeamName](mta://scripting/server/functions/setteamname.md)
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
