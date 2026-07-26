---
doc_id: "mta-wiki:8238"
title: "SetLightRadius"
source_title: "SetLightRadius"
source_url: "https://wiki.multitheftauto.com/wiki/SetLightRadius"
revision_id: 69000
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0"]
generated_at: "2026-07-26T16:16:41.233895+00:00"
---

# SetLightRadius

This function sets the radius for a [light](mta://reference/misc/element-light.md) element.

## Syntax

```
bool setLightRadius ( light theLight, float radius )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[light](mta://reference/misc/light.md):setRadius(...)*

**Variable**: *.radius*

**Counterpart**: *[getLightRadius](mta://scripting/client/functions/getlightradius.md)*

### Required Arguments

- **theLight:** The [light](mta://reference/misc/element-light.md) that you wish to set the radius of.

### Returns

Returns *true* if the function was successful, *false* otherwise.

### Example

```
local light = createLight(0, 2, 3, 4)
addCommandHandler("setradiusoflight",
	function(cmd, radius)
		if radius then
			if tonumber(radius) > 0 then
				setLightRadius(light, tonumber(radius))
			else
				outputChatBox("Radius must be greater than 0.")
			end
		else
			outputChatBox("You must specify a radius.")
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

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- setLightRadius
