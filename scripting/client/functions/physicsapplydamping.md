---
doc_id: "mta-wiki:12012"
title: "PhysicsApplyDamping"
source_title: "PhysicsApplyDamping"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsApplyDamping"
revision_id: 65155
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.414528+00:00"
---

# PhysicsApplyDamping

Slows down rigid body

## Syntax

```
bool physicsApplyDamping( physics-rigid-body theRigidBody, float dumping)
```

### Required Arguments

- **theRigidBody:** rigid body you want to apply velocity

- **dumping:** how much rigid body must slow down, if negative value, effect will inverted, make it speed up

### Returns

True if angular velocity got applied, false otherwise.

## Example

After threee seconds make box rapidly slow down falling

```
local box = physicsCreateShape(physics, "box", 1)
local boxrb = physicsCreateRigidBody(box)
physicsSetProperties(boxrb, "position", 0,0,100)

setTimer(function()
  physicsApplyDamping(boxrb, 10000)
end,3000,1)
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

- physicsApplyDamping

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
