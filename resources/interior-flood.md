---
doc_id: "mta-wiki:7322"
title: "Resource : Interior flood"
source_title: "Resource:Interior flood"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AInterior_flood"
revision_id: 37555
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:12.963564+00:00"
---

# Resource : Interior flood

The resource makes it possible to render water in interiors, where normaly wouldn't be visible. It draws a line material and applies a shader effect that mimicks the gta water effect.

## Overview

This resource provides few convenient exported functions.
Here you can download an example of how to use that: [Download!](http://www.solidfiles.com/d/73d0427849/)

## Exported functions

#### createWaterInInterior

Click to collapse [-]
Client

This function creates water.

```
bool exports.interior_flood:createWaterInInterior( int x1, int y1, float z1, int x2, int y2, float z2, int x3, int y3, float z3, int x4, int y4, float z4, int intID, [ int effectType = 0 ] )
```

### Required Arguments

- **x1, y1, z1:** position of bottom left (south-west) corner.

- **x2, y2, z2:** position of bottom right (south-east) corner.

- **x3, y3, z3:** position of top left (north-west) corner.

- **x4, y4, z4:** position of top right (north-east) corner.

- **intID:** interior in which the water is to be created.

### Optional Arguments

- **effectType:** effect type (0 - classic water, 1- watershine)

### Returns

Returns water element if successful, *false* otherwise.

#### createWaterInInteriorRadius

Click to collapse [-]
Client

This function creates water (using different data).

```
bool exports.interior_flood:createWaterInInteriorRadius( int x, int y, int z, float radius, int intID, [ int effectType = 0 ] )
```

### Required Arguments

- **x, y, z:** position of the top-central point.

- **radius:** define the radious of water box to be created.

- **intID:** interior in which the water is to be created.

### Optional Arguments

- **effectType:** effect type (0 - classic water, 1- watershine)

### Returns

Returns water element if successful, *false* otherwise.

#### destroyWaterInInterior

Click to collapse [-]
Client

This function destroys previously created water.

```
bool exports.interior_flood:destroyWaterInInterior( element )
```

### Required Arguments

- **element:** Previously created waterInInterior element.

### Returns

Returns 'true' if successful, *false* otherwise.

#### attachMaterialToWaterInInterior

Click to collapse [-]
Client

This function attaches water surface material to existing water in interior.

```
bool exports.interior_flood:attachMaterialToWaterInInterior( int x, int y,int z, float radius, int intID, [ int effectType = 0 ] )
```

### Required Arguments

- **x, y, z:** position of the top-central point. The 'z' position will be corrected by height of the existing water.

- **radius:** define the radious of the effect.

- **intID:** interior in which the water is to be created.

### Optional Arguments

- **effectType:** effect type (0 - classic water, 1- watershine)

### Returns

Returns water element if successful, *false* otherwise.

#### detachMaterialFromWaterInInterior

Click to collapse [-]
Client

This function destroys the surface material created with attachMaterialToWaterInInterior.

```
bool exports.interior_flood:detachMaterialFromWaterInInterior( element )
```

### Required Arguments

- **element:** Previously created waterSurface element.

### Returns

Returns 'true' if successful, *false* otherwise.

## Examples

```
exports.interior_flood:createWaterInInteriorRadius(-28.628,-83.787,1003.5,15,18,1)
```

This creates visible water in interior 18.

```
exports.interior_flood:createWaterInInterior(-290,-290,40,290,-290,40, -290, 290, 40, 290, 290, 40,0,1 )
```

This creates visible water in interior 0.

```
local someWater = exports.interior_flood:createWaterInInterior(-290,-290,40,290,-290,40, -290, 290, 40, 290, 290, 40,0,1 )
exports.interior_flood:destroyWaterInInterior(someWater)
```

This creates and destroys visible water in interior 0.

Of course when you want to use theese functions in your resources you have to include
the interior_flood resource in meta.

## See Also

[Resource Download](https://community.multitheftauto.com/index.php?p=resources&s=details&id=8234)
