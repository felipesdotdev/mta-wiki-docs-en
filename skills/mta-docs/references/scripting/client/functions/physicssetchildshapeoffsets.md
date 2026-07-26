---
doc_id: "mta-wiki:12000"
title: "PhysicsSetChildShapeOffsets"
source_title: "PhysicsSetChildShapeOffsets"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsSetChildShapeOffsets"
revision_id: 65133
language: "en"
categories: ["Client_functions"]
---

# PhysicsSetChildShapeOffsets

Sets offset position and/or rotation of child shape.

Causes all rigids which uses this shape got activated.
Keeps last position/rotation if newly set position/rotation is equal 0

## Syntax

```
bool physicsSetChildShapeOffsets(physics-shape compoundShape, int index, float x, float y, float z [, float rx, float ry, float rz ] )
```

### Required Arguments

- **compoundShape:** Must be compound shape

- **index:** Index of child. Starts from 1.

- **xyz:** Offset position

- **rx, ry, rz:** Offset rotation

### Returns

Returns true if offset got changed, false otherwise

## Example

```
local compound = physicsCreateShape(physics, "compound")
local box = physicsCreateShape(physics, "box", 1)
physicsAddChildShape(compound, box,0,0,0,0,0,0)
physicsAddChildShape(compound, box,0,0,0,0,0,0)
physicsAddChildShape(compound, box,0,0,0,0,0,0)
local c = physicsCreateRigidBody(physics,compound)
physicsSetProperties(c, "position", 0,0,20)
addEventHandler("onClientPreRender", root, function()
  physicsSetChildShapeOffsets(compound,1, 0,2,math.cos(getTickCount()/500))
  physicsSetChildShapeOffsets(compound,3, 0,-2,math.cos(getTickCount()/500))
end)
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](https://wiki.multitheftauto.com/index.php?search=physicsDestroy)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- [physicsCreateRigidBody](mta://scripting/client/functions/physicscreaterigidbody.md)

- [physicsCreateStaticCollision](mta://scripting/client/functions/physicscreatestaticcollision.md)

- [physicsCreateConstraint](mta://scripting/client/functions/physicscreateconstraint.md)

- [physicsAddChildShape](mta://scripting/client/functions/physicsaddchildshape.md)

- [physicsRemoveChildShape](mta://scripting/client/functions/physicsremovechildshape.md)

- [physicsGetChildShapes](mta://scripting/client/functions/physicsgetchildshapes.md)

- physicsSetChildShapeOffsets

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
