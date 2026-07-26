---
doc_id: "mta-wiki:1572"
title: "SetRadarAreaFlashing"
source_title: "SetRadarAreaFlashing"
source_url: "https://wiki.multitheftauto.com/wiki/SetRadarAreaFlashing"
revision_id: 67708
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:44.227054+00:00"
---

# SetRadarAreaFlashing

This function makes an existing radar area flash in transparency.

## Syntax

```
bool setRadarAreaFlashing ( radararea theRadarArea, bool flash )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](mta://reference/misc/radararea.md):setFlashing(...)*

**Variable**: *.flashing*

**Counterpart**: *[isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)*

### Required Arguments

- **theRadarArea:** the [radararea](mta://reference/misc/radararea.md) element we want to change flashing state of.

- **flash:** a bool indicating whether the radar area should flash (*true* to flash, *false* to not flash).

### Returns

Returns *true* if the new flash state was successfully set, *false* if the radar area doesn't exist or invalid arguments were passed.

## Example

**Example 1:** This example checks to see whether an existing radar area (*someArea*) is flashing, and forces it to flash if it isn't:

```
local isFlashing = isRadarAreaFlashing ( someArea )
if isFlashing then                                           -- if the area is already flashing...
    outputChatBox ( "The radar area is already flashing." )
else                                                         -- if it isn't...
    setRadarAreaFlashing ( someArea, true )                  -- make the area flash
end
```

**Example 2:** This example creates a radar area for the *King of the Hill* script, and a colsquare. When the player enters the radar area flashes, it stops flashing when a player leaves.

```
-- create our hill area for our gamemode
local hillArea = createColSquare ( -2171.0678710938, 678.17950439453, 0, 15, 15 )
local hillRadar = createRadarArea ( -2183.5678710938, 705.67950439453, 40, -40, 0, 255, 0, 175 )

-- add hill_Enter as a handler for when a player enters the hill area
function hill_Enter ( thePlayer, matchingDimension )
    -- announce to everyone that the player entered the hill
    outputChatBox( getPlayerName(thePlayer) .. " entered the zone!", root, 255, 255, 109 )
    setRadarAreaFlashing ( hillRadar, true )
end
addEventHandler ( "onColShapeHit", hillArea, hill_Enter )

-- add hill_Enter as a handler for when a player leaves the hill area
function hill_Exit ( thePlayer, matchingDimension )
    -- check if the player is not dead
    if isPlayerDead ( thePlayer ) ~= true then
        -- if he was alive, announce to everyone that the player has left the hill
        outputChatBox ( getPlayerName(thePlayer) .. " left the zone!", root, 255, 255, 109 )
        setRadarAreaFlashing ( hillRadar, false )
    end
end
addEventHandler ( "onColShapeLeave", hillArea, hill_Exit )
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- setRadarAreaFlashing

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)
