---
doc_id: "mta-wiki:1867"
title: "SetTeamColor"
source_title: "SetTeamColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetTeamColor"
revision_id: 80436
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:45.432342+00:00"
---

# SetTeamColor

This function is for setting the color of a specified team. This color is shown, for example, in the team players' nametags.

## Syntax

```
bool setTeamColor ( team theTeam, int colorR, int colorG, int colorB )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[team](mta://reference/misc/team.md):setColor(...)*

### Required Arguments

- **theTeam:** The [team](mta://reference/misc/team.md) you want to change the color of.

- **colorR:** An integer representing the red color value, from 0 to 255.

- **colorG:** An integer representing the green color value, from 0 to 255.

- **colorB:** An integer representing the blue color value, from 0 to 255.

### Returns

Returns *true* if the team is valid and the color is different, otherwise *false*.

## Example

This example creates a new team then changes its name and color.

```
team = createTeam ( "RedTeam", 255, 0, 0 ) -- create the team
if ( team ) then                           -- if the team was created (a team with that name didn't already exist)
    setTeamName ( team, "BlueTeam" )       -- change the name
    setTeamColor ( team, 0, 0, 255 )       -- change the color to suit its new name
end
```

## See Also

- [createTeam](mta://scripting/server/functions/createteam.md)

- setTeamColor

- [setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)

- [setTeamName](mta://scripting/server/functions/setteamname.md)
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
