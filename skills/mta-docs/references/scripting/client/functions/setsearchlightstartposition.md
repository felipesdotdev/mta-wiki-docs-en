---
doc_id: "mta-wiki:8465"
title: "SetSearchLightStartPosition"
source_title: "SetSearchLightStartPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetSearchLightStartPosition"
revision_id: 62383
language: "en"
categories: ["Client_functions"]
---

# SetSearchLightStartPosition

This function sets the start position of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
bool setSearchLightStartPosition ( searchlight theSearchLight, float startX, float startY, float startZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):setStartPosition(...)*

**Variable**: *.startPosition*

**Counterpart**: *[getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)*

### Required Arguments

- **theSearchLight**: the searchlight to modify the property of.

- **startX**: the X coordinate where the searchlight light cone will start.

- **startY**: the Y coordinate where the searchlight light cone will start.

- **startZ**: the Z coordinate where the searchlight light cone will start.

### Returns

If every argument is correct, this function returns *true*. If not, it will return *false* plus an error message.

## Example

This example creates a searchlight that originates in the camera position and targets the center of the map.

```
local searchLight = createSearchLight(0, 0, 0, 0, 0, 0, 0, 10)

if searchLight then
    local function updateSearchLight()
        -- Set its start position to the camera position
        setSearchLightStartPosition(searchLight, getCameraMatrix())
    end
    addEventHandler("onClientPreRender", root, updateSearchLight)
end
```

## See also

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- setSearchLightStartPosition

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
