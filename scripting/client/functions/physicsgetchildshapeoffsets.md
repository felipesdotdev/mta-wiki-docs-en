---
doc_id: "mta-wiki:11999"
title: "PhysicsGetChildShapeOffsets"
source_title: "PhysicsGetChildShapeOffsets"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsGetChildShapeOffsets"
revision_id: 65131
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.707708+00:00"
---

# PhysicsGetChildShapeOffsets

Returns offset position and rotation of child shape.
Sometimes return number is slightly different than input!

## Syntax

```
float float float float float float physicsGetChildShapeOffsets(physics-shape compoundShape, int index)
```

### Required Arguments

- **compoundShape:** Must be compound shape

- **index:** Index of child. Starts from 1.

### Returns

Returns offset position ( x,y,z ) and rotation (rx,ry,rz) of child shape. False otherwise

## Example

```
local compound = physicsCreateShape(physics, "compound")
local capsule = physicsCreateShape(physics, "capsule", 1, 1)
physicsAddChildShape(compound, capsule,1,2,3,4,5,6)
x,y,z,rx,ry,rz = physicsGetChildShapeOffsets(compound, 1)
outputChatBox("Offset of first shape: ".. string.format("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f", x,y,z,rx,ry,rz))
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](mta://scripting/client/functions/physicsdestroy.md)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- [physicsCreateRigidBody](mta://scripting/client/functions/physicscreaterigidbody.md)

- [physicsCreateStaticCollision](mta://scripting/client/functions/physicscreatestaticcollision.md)

- [physicsCreateConstraint](mta://scripting/client/functions/physicscreateconstraint.md)

- [physicsAddChildShape](mta://scripting/client/functions/physicsaddchildshape.md)

- [physicsRemoveChildShape](mta://scripting/client/functions/physicsremovechildshape.md)

- [physicsGetChildShapes](mta://scripting/client/functions/physicsgetchildshapes.md)

- [physicsSetChildShapeOffsets](mta://scripting/client/functions/physicssetchildshapeoffsets.md)

- physicsGetChildShapeOffsets

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
