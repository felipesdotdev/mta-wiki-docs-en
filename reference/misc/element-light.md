---
doc_id: "mta-wiki:8245"
title: "Element/Light"
source_title: "Element/Light"
source_url: "https://wiki.multitheftauto.com/wiki/Element/Light"
revision_id: 70663
language: "en"
categories: ["Changes_in_1.5.0", "Utility_templates", "Element_Types"]
generated_at: "2026-07-26T16:14:53.960572+00:00"
---

# Element/Light

The light class represents colored, 3D lights in the GTA world. There are a couple different types of lights, which are point lights, spot lights and dark lights.

The element type of this class is **"light"**.

| [[{{{image}}}\|link=\|]] | Note: The XML syntax is not implemented yet, but is a representation of what it would be if implemented. |
| --- | --- |
|  |  |

## XML syntax

```
<light posX="" posY="" posZ="" type="" radius="" color="" dirX="" dirY="" dirZ="" shadows="" />
```

### Required Attributes

- **lightType:** An integer representing the type of light to create.

- **0**: Point light, which illuminates surroundings evenly across the light radius.

- **1**: Spot light, which illuminates the direction of the light defined by *dirX*, *dirY* and *dirZ*.

- **2**: Dark light, which darkens its surrounding elements to full black.

- **posX:** A floating point number representing the X coordinate on the map.

- **posY:** A floating point number representing the Y coordinate on the map.

- **posZ:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **radius:** A floating point number representing the radius of the light.

- **color:** The color of the light in HTML style format #RRGGBB, defaults to black (invisible) if not specified.

- **dirX:** A floating point number representing the light direction's X coordinate on the map.

- **dirY:** A floating point number representing the light direction's Y coordinate on the map.

- **dirZ:** A floating point number representing the light direction's Z coordinate on the map.

- **shadows:** A boolean representing whether or not does the light cast shadows.

## Related scripting functions

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
