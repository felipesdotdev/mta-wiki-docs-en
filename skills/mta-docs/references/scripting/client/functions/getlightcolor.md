---
doc_id: "mta-wiki:8236"
title: "GetLightColor"
source_title: "GetLightColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetLightColor"
revision_id: 50869
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0"]
---

# GetLightColor

This function returns the color for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
int, int, int getLightColor ( light theLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](https://wiki.multitheftauto.com/index.php?search=light):getColor(...)*

**Variable**: *.color*

**Counterpart**: *[setLightColor](mta://scripting/client/functions/setlightcolor.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to retrieve the color of.

### Returns

Returns three [ints](mta://reference/misc/int.md) corresponding to the amount of red, green and blue (respectively) of the light, *false* if invalid arguments were passed.

### Example

```
local light = createLight(0, 0, 0, 4)
local red, green, blue = getLightColor(light)
outputChatBox(" light color is " .. red .. ", " .. green .. ", " .. blue)
```

## See also

- [createLight](mta://scripting/client/functions/createlight.md)

- getLightColor

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
