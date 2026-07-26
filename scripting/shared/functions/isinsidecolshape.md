---
doc_id: "mta-wiki:10261"
title: "IsInsideColShape"
source_title: "IsInsideColShape"
source_url: "https://wiki.multitheftauto.com/wiki/IsInsideColShape"
revision_id: 59767
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:15:56.075058+00:00"
---

# IsInsideColShape

This function checks if a 3D position is inside a colshape or not.

## Syntax

```
bool isInsideColShape ( colshape theShape, float posX, float posY, float posZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):isInside(...)*

### Required Arguments

- **theShape:** The colshape you're checking the position against.

- **posX:** The X coordinate of the position you're checking.

- **posY:** The Y coordinate of the position you're checking.

- **posZ:** The Z coordinate of the position you're checking.

### Returns

Returns *true* if the position is inside the colshape, *false* if it isn't or if any parameters are invalid.

## Example

This function checks if an element is within a colshape.

```
function isElementInsideColShape( theElement, theColShape )
    return isInsideColShape( theColShape, getElementPosition( theElement ) )
end
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- isInsideColShape

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)
