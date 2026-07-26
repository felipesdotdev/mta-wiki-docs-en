---
doc_id: "mta-wiki:1699"
title: "CreateTeam"
source_title: "CreateTeam"
source_url: "https://wiki.multitheftauto.com/wiki/CreateTeam"
revision_id: 81693
language: "en"
categories: ["Server_functions"]
---

# CreateTeam

This function is for creating a new [team](https://wiki.multitheftauto.com/index.php?search=team), which can be used to group players. Players will not join the team until they are respawned.

## Syntax

```
team createTeam ( string teamName [, int colorR = 235, int colorG = 221, int colorB = 178 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Team.create(...)*

### Required Arguments

- **teamName:** A string representing the teams name.

### Optional Arguments

- **colorR:** An integer representing the red color value.

- **colorG:** An integer representing the green color value.

- **colorB:** An integer representing the blue color value.

### Returns

Returns a team element if it was successfully created, *false* if invalid arguments are passed or a team with that name already exists.

## Example

**Example 1:** This example creates a new team for a player, then adds him to it.

```
function gimmeATeam(source, commandName, teamName)
    local newTeam = createTeam(teamName) -- create a new team with the specified name
    if newTeam then -- if it was successfully created
        setPlayerTeam(source, newTeam) -- add the player to the new team
    end
end
addCommandHandler("giveteam", gimmeATeam)
```

**Example 2:** This example creates two teams, one for Admin and one for Freeroamers, when the resource this script is in is started.

```
function createTeamsOnStart()
    teamAdmmin = createTeam("Admin", 0, 255, 0) -- change the 3 numbers(0,255,0), the first number is ColourR, the second is ColourG, and the last one is ColourB
    teamFreeroamers = createTeam("Freeroamer", 200, 0, 100)
end
addEventHandler("onResourceStart", resourceRoot, createTeamsOnStart) -- we attach the function to this resource's root element
```

**Example 3:** This example creates a team for Admin and when an admin logs in, he will be set in the Admin team.

```
function createAdminTeamOnStart()
    AdminTeam = createTeam("Admin", 0, 255, 0) -- create a new team and name it 'Admin'
end
addEventHandler("onResourceStart", resourceRoot, createAdminTeamOnStart) -- add an event handler

function setAdminTeam()
    if isObjectInACLGroup("user." .. getAccountName(getPlayerAccount(source)), aclGetGroup("Admin")) then -- if he is admin
        setPlayerTeam(source, AdminTeam) -- set him to admin team
    end
end
addEventHandler("onPlayerLogin", root, setAdminTeam) -- add an event handler
```

## See Also

- createTeam

- [setTeamColor](mta://scripting/server/functions/setteamcolor.md)

- [setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)

- [setTeamName](mta://scripting/server/functions/setteamname.md)
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
