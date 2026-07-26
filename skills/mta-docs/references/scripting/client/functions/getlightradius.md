---
doc_id: "mta-wiki:8235"
title: "GetLightRadius"
source_title: "GetLightRadius"
source_url: "https://wiki.multitheftauto.com/wiki/GetLightRadius"
revision_id: 50868
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0"]
---

# GetLightRadius

This function returns the radius for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
float getLightRadius ( light theLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](https://wiki.multitheftauto.com/index.php?search=light):getRadius(...)*

**Variable**: *.radius*

**Counterpart**: *[setLightRadius](mta://scripting/client/functions/setlightradius.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to retrieve the radius of.

### Returns

Returns a [float](mta://reference/misc/float.md) containing the radius of the specified light, *false* if invalid arguments were passed.

### Example

```
local light = createLight(0, 0, 0, 4)
outputChatBox("light radius: " .. getLightRadius(light))
```

## See also

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- getLightRadius

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
