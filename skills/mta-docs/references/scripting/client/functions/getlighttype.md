---
doc_id: "mta-wiki:8234"
title: "GetLightType"
source_title: "GetLightType"
source_url: "https://wiki.multitheftauto.com/wiki/GetLightType"
revision_id: 50867
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0"]
---

# GetLightType

This function returns the type for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
int getLightType ( light theLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](https://wiki.multitheftauto.com/index.php?search=light):getType(...)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to retrieve the type of.

### Returns

Returns an [int](mta://reference/misc/int.md) containing the type of the specified light, *false* if invalid arguments were passed.

### Example

```
local light = createLight(1, 2, 3, 4)
outputChatBox("light type " .. getLightType(light))
```

## See also

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- getLightType

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
