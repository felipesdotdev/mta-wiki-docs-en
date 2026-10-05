---
doc_id: "mta-wiki:14688"
title: "SetSearchLightColor"
source_title: "SetSearchLightColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetSearchLightColor"
revision_id: 82894
language: "en"
categories: ["Client_functions"]
---

# SetSearchLightColor

This function sets the color of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```lua
nil setSearchLightColor ( searchlight theSearchLight, int color )
```

### Required Arguments

- **theSearchLight**: the searchlight to set the color of.

- **color**: the color to apply, created using [tocolor](mta://scripting/shared/functions/tocolor.md).

| [[{{{image}}}\|link=\|]] | Note: The alpha component is stored, but does not affect the searchlight's appearance. |
| --- | --- |
|  |  |

### Returns

This function does not return any values. Invalid arguments raise an error.

## Example

This example creates an orange searchlight above the player.

```lua
addCommandHandler("orangelight", function()
    local x, y, z = getElementPosition(localPlayer)
    local searchLight = createSearchLight(x, y, z + 10, x, y, z, 0, 5)

    if not searchLight then
        return
    end

    setSearchLightColor(searchLight, tocolor(255, 128, 0))
    outputChatBox("Created an orange searchlight.")

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

- setSearchLightColor

- [getSearchLightColor](mta://scripting/client/functions/getsearchlightcolor.md)
