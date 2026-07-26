---
doc_id: "mta-wiki:8460"
title: "CreateSearchLight"
source_title: "CreateSearchLight"
source_url: "https://wiki.multitheftauto.com/wiki/CreateSearchLight"
revision_id: 47560
language: "en"
categories: ["Client_functions", "Changes_in_1.5.2", "Utility_templates"]
---

# CreateSearchLight

This function creates a [searchlight](mta://reference/misc/element-searchlight.md). A [searchlight](mta://reference/misc/element-searchlight.md) is a spotlight which looks like the one available in the Police Maverick.

| [[{{{image}}}\|link=\|]] | Tip: You should only use this function when you are sure that the searchlight will point upwards or downwards . Using them horizontally or almost horizontally will generate visual artifacts in the searchlight. |
| --- | --- |
|  |  |

## Syntax

```
searchlight createSearchLight ( float startX, float startY, float startZ, float endX, float endY, float endZ, float startRadius, float endRadius [, bool renderSpot = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[SearchLight](mta://reference/misc/element-searchlight.md)(...)*

### Required Arguments

- **startX**: the X coordinate where the searchlight light cone will start.

- **startY**: the Y coordinate where the searchlight light cone will start.

- **startZ**: the Z coordinate where the searchlight light cone will start.

- **endX**: the X coordinate of the direction where the searchlight will point to.

- **endY**: the Y coordinate of the direction where the searchlight will point to.

- **endZ**: the Z coordinate of the direction where the searchlight will point to.

- **startRadius**: the radius of the searchlight's light cone in its beginning.

- **endRadius**: the radius of the searchlight's light cone in its end.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **renderSpot**: if *true*, the searchlight will lighten the surface where it ends.

### Returns

If every argument is correct and the limit of 1000 searchlights has not been reached, this function returns a [searchlight element](mta://reference/misc/element-searchlight.md). Otherwise, it returns *false*.

## Example

This example allows players to wear a helmet lantern, which can be toggled on or off by pressing O or using */togglelantern*. It uses createSearchLight to create the illumination effect.

```
local helmetLantern

local function updateHelmetLantern()
    -- Calculate light properties
    local helmetPos, playerMatrix = Vector3(getPedBonePosition(localPlayer, 6)), getElementMatrix(localPlayer)
    local targetPos = Vector3(playerMatrix[4][1] + playerMatrix[2][1] * 3, playerMatrix[4][2] + playerMatrix[2][2] * 3, playerMatrix[4][3] + playerMatrix[2][3] * 3)
    -- If the searchlight we use for the effect doesn't exist, create it
    -- If it is already created, then simply update its start and end positions
    if not helmetLantern then
        helmetLantern = createSearchLight(helmetPos, targetPos, 0, 15)
    else
        setSearchLightStartPosition(helmetLantern, helmetPos)
        setSearchLightEndPosition(helmetLantern, targetPos)
    end
end

local function manageHelmetLantern()
    local helmetLanternOff = not helmetLantern
    playSoundFrontEnd(helmetLanternOff and 37 or 38)
    if helmetLanternOff then
        -- Let updateHelmetLantern take care of creating and updating the effect
        addEventHandler("onClientPreRender", root, updateHelmetLantern)
    else
        -- Stop updateHelmetLantern doing its job and clear variables
        removeEventHandler("onClientPreRender", root, updateHelmetLantern)
        destroyElement(helmetLantern)
        helmetLantern = nil
    end
end

-- Allow the player to turn the helmet lantern or on off by using /togglelantern or pressing O
addCommandHandler("togglelantern", manageHelmetLantern)
bindKey("o", "down", manageHelmetLantern)
```

## See also

- createSearchLight

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
