---
doc_id: "mta-wiki:8470"
title: "GetSearchLightEndPosition"
source_title: "GetSearchLightEndPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetSearchLightEndPosition"
revision_id: 73247
language: "en"
categories: ["Client_functions"]
---

# GetSearchLightEndPosition

This function gets the end position of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
float float float getSearchLightEndPosition ( searchlight theSearchLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):getEndPosition(...)*

**Variable**: *.endPosition*

**Counterpart**: *[setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)*

### Required Arguments

- **theSearchLight**: the searchlight to get the position where the searchlight's light cone ends.

### Returns

If the specified searchlight element is valid, this function will return three *float*, which are the three coordinates of searchlight's end position. If not, it will return *false* plus an error message.

## Example

```
local helmetLantern

local function updateHelmetLantern()
    local helmetPos, playerMatrix = Vector3(getPedBonePosition(localPlayer, 6)), getElementMatrix(localPlayer)
    local targetPos = Vector3(playerMatrix[4][1] + playerMatrix[2][1] * 3, playerMatrix[4][2] + playerMatrix[2][2] * 3, playerMatrix[4][3] + playerMatrix[2][3] * 3)
    -- If the searchlight we use for the effect doesn't exist, create it
    -- If it is already created, then simply update its start and end positions
    if not helmetLantern then
        helmetLantern = createSearchLight(helmetPos, targetPos, 0, 15)
		local a , b = getSearchLightEndPosition(helmetLantern)
		outputChatBox(a .." "..b)
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

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- getSearchLightEndPosition

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
