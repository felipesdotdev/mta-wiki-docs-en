---
doc_id: "mta-wiki:8467"
title: "SetSearchLightStartRadius"
source_title: "SetSearchLightStartRadius"
source_url: "https://wiki.multitheftauto.com/wiki/SetSearchLightStartRadius"
revision_id: 62384
language: "en"
categories: ["Client_functions"]
---

# SetSearchLightStartRadius

This function sets the start radius of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
bool setSearchLightStartRadius ( searchlight theSearchlight, float startRadius )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):setStartRadius(...)*

**Variable**: *.startRadius*

**Counterpart**: *[getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)*

### Required Arguments

- **theSearchLight**: the searchlight to modify the property of.

- **startRadius**: the radius of the searchlight's light cone in its beginning.

### Returns

If every argument is correct, this function returns *true*. If not, it will return *false* plus an error message.

## Example

This example creates a skywalker light on top of Los Santos' skyscraper and turns it on/off every second by setting it's ending radius and starting radius to 0.

```
skywalkerLight = createSearchLight (1544, -1353.5, 330, 1528, -1347, 360, 0.2, 3, false)

setTimer (function ()	
	if not off then
		setSearchLightStartRadius (skywalkerLight, 0)
		setSearchLightEndRadius (skywalkerLight, 0)
		off = true
	else
		setSearchLightStartRadius (skywalkerLight, 0.2)
		setSearchLightEndRadius (skywalkerLight, 3)
		off = false
	end
end, 1000, 0)
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

- setSearchLightStartRadius
