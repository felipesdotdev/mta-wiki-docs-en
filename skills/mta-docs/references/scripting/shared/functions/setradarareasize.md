---
doc_id: "mta-wiki:1615"
title: "SetRadarAreaSize"
source_title: "SetRadarAreaSize"
source_url: "https://wiki.multitheftauto.com/wiki/SetRadarAreaSize"
revision_id: 43077
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetRadarAreaSize

This function changes the size of an existing [radar area](https://wiki.multitheftauto.com/index.php?search=radar%20area).

## Syntax

```
bool setRadarAreaSize ( radararea theRadararea, float x, float y )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](https://wiki.multitheftauto.com/index.php?search=radararea):setSize(...)*

### Required Arguments

- **theRadararea:** the [radararea](https://wiki.multitheftauto.com/index.php?search=radararea) element whose size is to be changed.

- **x:** the x length of the radar area.

- **y:** the y length of the radar area.

### Returns

Returns *true* if the size was set successfully, *false* if invalid arguments are passed.

## Example

**Example 1:** This example decreases the size of a team's radar area whenever a player from that team dies:

```
-- assume that team elements exist and that each player belongs to one of them
-- assume that radararea elements exist and that each is a child of one of the teams
function playerWasted ( killer, killerweapon, bodypart )
    local victimteam = getPlayerTeam ( source )                 -- get the team of the victim
    local killerteam = getPlayerTeam ( killer )                 -- get the team of the killer
    if ( killer and killerteam ~= victimteam ) then             -- if there is a killer and he is from an opposing team
        local victimarea = getElementChild ( victimteam, 0 )    -- get the radararea belonging to the victim's team
        local x, y = getRadarAreaSize ( victimarea )            -- get the size of the radar area
        x = x - 5
        y = y - 5
        setRadarAreaSize ( victimarea, x, y )                   -- set a new (smaller) size for the victim's radar area
    end
end
addEventHandler ( "onPlayerWasted", root, playerWasted )
```

**Example 2:** This example creates a radar area and resets its size right away:

```
aRadarArea = createRadarArea ( 1024, 1024, 30, 140, 255, 255, 0, 85 )
flag = setRadarAreaSize ( aRadarArea, 50, 90 )
if ( flag ) then
    outputChatBox ( "Radar area size set successfully!" )
else
    outputChatBox ( "Failed to set radar area size." )
end
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- setRadarAreaSize
