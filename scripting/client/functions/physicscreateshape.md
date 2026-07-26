---
doc_id: "mta-wiki:11976"
title: "PhysicsCreateShape"
source_title: "PhysicsCreateShape"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsCreateShape"
revision_id: 65190
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.512378+00:00"
---

# PhysicsCreateShape

Creates physics shape used for static or dynamic collision detection

## Syntax

```
physics-shape physicsCreateShape(physics thePhysics, shape-type theShapeType, mixed)
         
physics-shape physicsCreateShape(physics thePhysics, "box", float size)
physics-shape physicsCreateShape(physics thePhysics, "box", float sizeX, sizeY, sizeZ)
physics-shape physicsCreateShape(physics thePhysics, "sphere", float radius)
physics-shape physicsCreateShape(physics thePhysics, "capsule", float radius, float height)
physics-shape physicsCreateShape(physics thePhysics, "cone", float radius, float height)
physics-shape physicsCreateShape(physics thePhysics, "cylinder", float radius, float height)
physics-shape physicsCreateShape(physics thePhysics, "heightfieldterrain", int sizeX, int sizeY [, table heightData ] )
physics-shape physicsCreateShape(physics thePhysics, "compound", int initialChildCapacity = 0)
physics-shape physicsCreateShape(physics thePhysics, "trianglemesh", vector3 vertexA, vector3 vertexB, vector3 vertexC, ...)
physics-shape physicsCreateShape(physics thePhysics, "convexhull", vector3 pointA, vector3 pointB, vector3, pointC, ...)
```

- **heightfieldterrain:** minimum size is 3x3, and maximum 8192x8192. By default terrain is flat, you can pass default height after size, each float represents height of next vertex.

- **trianglemesh:** each of three vectors creates single triangle, use n*3 vectors to create n triangles.

- **compound:** can contain up to 8192 child shapes.

- **convexhull:** require at least 3 points.

### Required Arguments

- **thePhysics:** physics world

- **theShapeType:** shape, availiable types "box", "sphere", "capsule", "cone", "cylinder", "heightfieldterrain", "compound", "trianglemesh", "convexhull",

### Returns

- **physics-shape** to use in future functions

## Example

```
local terrainData = {
  3,3,3,3,
  3,0,0,3,
  3,0,0,3,
  3,3,3,3,
}
local terrainShape = physicsCreateShape(physics, "heightfieldterrain", 4,4, terrainData)
local terrain = physicsCreateStaticCollision(terrainShape)
physicsSetProperties(terrain, "position", 0,0,5)
physicsSetProperties(terrain, "scale", 5,5,1) -- in terrain, sets mesh density, now mesh has size 20x20units, one vertex every 5 units
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](mta://scripting/client/functions/physicsdestroy.md)

- physicsCreateShape

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- [physicsCreateRigidBody](mta://scripting/client/functions/physicscreaterigidbody.md)

- [physicsCreateStaticCollision](mta://scripting/client/functions/physicscreatestaticcollision.md)

- [physicsCreateConstraint](mta://scripting/client/functions/physicscreateconstraint.md)

- [physicsAddChildShape](mta://scripting/client/functions/physicsaddchildshape.md)

- [physicsRemoveChildShape](mta://scripting/client/functions/physicsremovechildshape.md)

- [physicsGetChildShapes](mta://scripting/client/functions/physicsgetchildshapes.md)

- [physicsSetChildShapeOffsets](mta://scripting/client/functions/physicssetchildshapeoffsets.md)

- [physicsGetChildShapeOffsets](mta://scripting/client/functions/physicsgetchildshapeoffsets.md)

- [physicsGetShapes](mta://scripting/client/functions/physicsgetshapes.md)

- [physicsGetRigidBodies](mta://scripting/client/functions/physicsgetrigidbodies.md)

- [physicsGetStaticCollisions](mta://scripting/client/functions/physicsgetstaticcollisions.md)

- [physicsGetConstraints](mta://scripting/client/functions/physicsgetconstraints.md)

- [physicsSetProperties](mta://scripting/client/functions/physicssetproperties.md)

- [physicsGetProperties](https://wiki.multitheftauto.com/index.php?title=PhysicsGetProperties&action=edit&redlink=1)

- [physicsDrawDebug](mta://scripting/client/functions/physicsdrawdebug.md)

- [physicsSetDebugMode](mta://scripting/client/functions/physicssetdebugmode.md)

- [physicsBuildCollisionFromGTA](mta://scripting/client/functions/physicsbuildcollisionfromgta.md)

- [physicsApplyVelocity](mta://scripting/client/functions/physicsapplyvelocity.md)

- [physicsApplyVelocityForce](mta://scripting/client/functions/physicsapplyvelocityforce.md)

- [physicsApplyAngularVelocity](mta://scripting/client/functions/physicsapplyangularvelocity.md)

- [physicsApplyAngularVelocityForce](mta://scripting/client/functions/physicsapplyangularvelocityforce.md)

- [physicsApplyDamping](mta://scripting/client/functions/physicsapplydamping.md)

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
