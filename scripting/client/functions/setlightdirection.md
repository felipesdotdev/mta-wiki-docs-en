---
doc_id: "mta-wiki:8240"
title: "SetLightDirection"
source_title: "SetLightDirection"
source_url: "https://wiki.multitheftauto.com/wiki/SetLightDirection"
revision_id: 50872
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:41.216082+00:00"
---

# SetLightDirection

This function sets the direction for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
bool setLightDirection ( light theLight, float x, float y, float z )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](mta://reference/misc/light.md):setDirection(...)*

**Variable**: *.direction*

**Counterpart**: *[getLightDirection](mta://scripting/client/functions/getlightdirection.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to set the direction of.

### Returns

Returns *true* if the function was successful, *false* otherwise.

### Example

```
local light = createLight(0, 0, 0, 4)
addCommandHandler("setdirectionoflight",
	function(cmd, x, y, z)
		if x and y and z then
			setLightDirection(light, tonumber(x), tonumber(y), tonumber(z))
		end
	end
)
```

## See also

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- setLightDirection

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
