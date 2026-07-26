---
doc_id: "mta-wiki:2348"
title: "Element/Collision shape"
source_title: "Colshape"
source_url: "https://wiki.multitheftauto.com/wiki/Colshape"
revision_id: 70588
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:10:34.887646+00:00"
---

# Element/Collision shape

The collision shape class represents invisible collision detection shapes that can be created in the GTA world. Collision shapes are typically used to detect physical entities moving through them and perform actions when they do.

The element type for this class is **colshape**.

## XML syntax

```
<colcube posX="1024.768" posY="1248.1024" posZ="800.600" width="100" height="100" depth="100"/>
<colsphere posX="1024.768" posY="1248.1024" posZ="800.600" radius="100"/>
<coltube posX="1024.768" posY="1248.1024" posZ="800.600" radius="30" height="15"/>
<colrectangle posX="1024.768" posY="1248.1024" posZ="800.600" width="100" depth="61.8"/>
<colcircle posX="1024.768" posY="1248.1024" posZ="800.600" radius="30"/>
```

### Required Attributes

- **posX**: A float representing the X position of the colshape.

- **posY**: A float representing the Y position of the colshape.

- **posZ**: A float representing the Z position of the colshape.

- **radius**: The radius of the colshape (spheres, tubes and circles only).

- **width**: The width of the colshape (rectangles and cubes only).

- **depth**: The depth of the colshape (rectangles and cubes only).

- **height**: The height of the colshape (cubes only).

### Optional Attributes

- **dimension**: The dimension the colshape is in

## Related scripting functions

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

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)
