---
doc_id: "mta-wiki:2781"
title: "IsInsideRadarArea"
source_title: "IsInsideRadarArea"
source_url: "https://wiki.multitheftauto.com/wiki/IsInsideRadarArea"
revision_id: 73889
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:56.086729+00:00"
---

# IsInsideRadarArea

This function checks if a 2D position is inside a [radar area](mta://reference/misc/radararea.md) or not.

## Syntax

```
bool isInsideRadarArea ( radararea theArea, float posX, float posY )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](mta://reference/misc/radararea.md):isInside(...)*

### Required Arguments

- **theArea:** The [radar area](mta://reference/misc/radararea.md) you're checking the position against.

- **posX:** The X coordinate of the position you're checking.

- **posY:** The Y coordinate of the position you're checking.

### Returns

Returns *true* if the position is inside the radar area, *false* if it isn't or if any parameters are invalid.

## Example

This function checks if an element is within a radar area.

```
function isElementInsideRadarArea ( theElement, theArea )
	-- get the x, y coordinates from getElementPosition (z gets silently discarded)
	local posX, posY = getElementPosition( theElement )
	-- call isInsideRadarArea with those coordinates and return its result
	return isInsideRadarArea ( theArea, posX, posY )
end
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- isInsideRadarArea

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)
