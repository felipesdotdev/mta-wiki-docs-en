---
doc_id: "mta-wiki:8237"
title: "GetLightDirection"
source_title: "GetLightDirection"
source_url: "https://wiki.multitheftauto.com/wiki/GetLightDirection"
revision_id: 49405
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0"]
generated_at: "2026-07-26T16:15:15.085488+00:00"
---

# GetLightDirection

This function returns the direction for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
float, float, float getLightDirection ( light theLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](mta://reference/misc/light.md):getDirection(...)*

**Variable**: *.direction*

**Counterpart**: *[setLightDirection](mta://scripting/client/functions/setlightdirection.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to retrieve the direction of.

### Returns

Returns three [ints](mta://reference/misc/int.md) corresponding to the x, y and z coordinates (respectively) of the light direction, *false* if invalid arguments were passed.

### Example

```
function lightDirection ()
	local light = createLight(0, 1, 0, 4)
	local lx, ly, lz = getLightDirection(light)
	outputChatBox("light direction: " .. lx .. ", " .. ly .. ", " .. lz)
end
addCommandHandler("lightDirection", lightDirection)
```

## See also

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- getLightDirection

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
