---
doc_id: "mta-wiki:14687"
title: "GetSearchLightColor"
source_title: "GetSearchLightColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetSearchLightColor"
revision_id: 82893
language: "en"
categories: ["Client_functions"]
---

# GetSearchLightColor

This function gets the color of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```lua
int int int int getSearchLightColor ( searchlight theSearchLight )
```

### Required Arguments

- **theSearchLight**: the searchlight to get the color of.

### Returns

Returns four integers representing the red, green, blue and alpha components of the searchlight's color, each ranging from 0 to 255. Invalid arguments raise an error.

The default color is red 200, green 200, blue 255 and alpha 0.

| [[{{{image}}}\|link=\|]] | Note: The alpha component is stored and returned, but does not affect the searchlight's appearance. |
| --- | --- |
|  |  |

## Example

This example creates a searchlight above the player and displays its default color.

```lua
addCommandHandler("getlightcolor", function()
    local x, y, z = getElementPosition(localPlayer)
    local searchLight = createSearchLight(x, y, z + 10, x, y, z, 0, 5)

    if not searchLight then
        return
    end

    local r, g, b, a = getSearchLightColor(searchLight)
    outputChatBox(("Searchlight color: R=%d, G=%d, B=%d, A=%d"):format(r, g, b, a))

    -- Remove the demonstration light after 10 seconds.
    setTimer(destroyElement, 10000, 1, searchLight)
end)
```

## See also

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)

ADDED/UPDATED IN VERSION 1.7.0 :

- [setSearchLightColor](mta://scripting/client/functions/setsearchlightcolor.md)

- getSearchLightColor
