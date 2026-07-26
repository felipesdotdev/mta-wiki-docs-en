---
doc_id: "mta-wiki:1695"
title: "Element/Team"
source_title: "Team"
source_url: "https://wiki.multitheftauto.com/wiki/Team"
revision_id: 80479
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:16:57.619502+00:00"
---

# Element/Team

The team class represents player teams. Players on the same team can use team features such as teamchat or friendly fire.

A common misconception is that players would be child elements of team elements. This is wrong. Being part of a team is merely a relational connection rather than a change in element hierarchy. To perform logic on all the players of a team you have to use the [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md) function.

The element type of this class is: **"team"**.

**NOTE:** It is likely that the colorR/G/B values will be changed to the more standard color="#RRGGBB" before the final release.

## XML syntax

```
<team name="" colorR="" colorG="" colorB="" friendlyfire=""/>
```

### Required Attributes

- **name**: A name of the team

### Optional Attributes

- **colorR**: The red component of the team's color

- **colorG**: The green component of the team's color

- **colorB**: The blue component of the team's color

- **friendlyfire**: Should friendly fire be allowed (true/false)

## Related scripting functions

- [createTeam](mta://scripting/server/functions/createteam.md)

- [setTeamColor](mta://scripting/server/functions/setteamcolor.md)

- [setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)

- [setTeamName](mta://scripting/server/functions/setteamname.md)
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
