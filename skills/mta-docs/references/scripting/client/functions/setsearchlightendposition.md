---
doc_id: "mta-wiki:8466"
title: "SetSearchLightEndPosition"
source_title: "SetSearchLightEndPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetSearchLightEndPosition"
revision_id: 82069
language: "en"
categories: ["Client_functions"]
---

# SetSearchLightEndPosition

This function sets the end position of a [searchlight](https://wiki.multitheftauto.com/index.php?search=searchlight) element.

## Syntax

```
bool setSearchLightEndPosition ( searchlight theSearchLight, float endX, float endY, float endZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):setEndPosition(...)*

**Variable**: *.endPosition*

**Counterpart**: *[getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)*

### Required Arguments

- **theSearchLight**: the searchlight to modify the property of.

- **endX**: the X coordinate where the searchlight light cone will end.

- **endY**: the Y coordinate where the searchlight light cone will end.

- **endZ**: the Z coordinate where the searchlight light cone will end.

### Returns

If every argument is correct, this function returns *true*. If not, it will return *false* plus an error message.

## Example

This example creates a searchlight that originates in the camera position and targets to the front of it.

```
local searchLight = createSearchLight(0, 0, 0, 0, 0, 0, 0, 10)

if searchLight then
    local function updateSearchLight()
        -- Get camera position and look at point
        local sx, sy, sz, ex, ey, ez = getCameraMatrix()
        -- Set searchlight's start position to the camera position, and end position to the look at point
        setSearchLightStartPosition(searchLight, sx, sy, sz)
        setSearchLightEndPosition(searchLight, ex, ey, ez)
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

- setSearchLightEndPosition

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
