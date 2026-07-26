---
doc_id: "mta-wiki:8463"
title: "Element/Searchlight"
source_title: "Searchlight"
source_url: "https://wiki.multitheftauto.com/wiki/Searchlight"
revision_id: 70671
language: "en"
categories: ["Changes_in_1.5.2", "Utility_templates", "Element_Types"]
generated_at: "2026-07-26T16:16:36.466367+00:00"
---

# Element/Searchlight

The searchlight class represents special spotlights in the GTA world. They are different to common spotlights because their visual effects.

The element type of this class is **"searchlight"**.

| [[{{{image}}}\|link=\|]] | Note: The XML syntax is not implemented yet, but is a representation of what it would be if implemented. |
| --- | --- |
|  |  |

## XML syntax

```
<searchlight startX="" startY="" startZ="" endX="" endY="" endZ="" startRadius="" endRadius="" renderSpot="" />
```

### Required Attributes

- **startX**: the X coordinate where the searchlight light cone will start.

- **startY**: the Y coordinate where the searchlight light cone will start.

- **startZ**: the Z coordinate where the searchlight light cone will start.

- **endX**: the X coordinate of the direction where the searchlight will point to.

- **endY**: the Y coordinate of the direction where the searchlight will point to.

- **endZ**: the Z coordinate of the direction where the searchlight will point to.

- **startRadius**: the radius of the searchlight's light cone in its beginning.

- **endRadius**: the radius of the searchlight's light cone in its end.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **renderSpot**: if *true*, the searchlight will lighten the surface where it ends.

## Related scripting functions

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
