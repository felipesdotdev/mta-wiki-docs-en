---
doc_id: "mta-wiki:8239"
title: "SetLightColor"
source_title: "SetLightColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetLightColor"
revision_id: 50871
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:41.204873+00:00"
---

# SetLightColor

This function sets the color for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
bool setLightColor ( light theLight, float r, float g, float b )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](mta://reference/misc/light.md):setColor(...)*

**Variable**: *.color*

**Counterpart**: *[getLightColor](mta://scripting/client/functions/getlightcolor.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to set the color of.

### Returns

Returns *true* if the function was successful, *false* otherwise.

### Example

```
local light = createLight(1, 2, 3, 4)
addCommandHandler("setcoloroflight",
	function(cmd, r, g, b)
		if r and g and b then
			setLightColor(light, tonumber(r), tonumber(g), tonumber(b))
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

- setLightColor

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
