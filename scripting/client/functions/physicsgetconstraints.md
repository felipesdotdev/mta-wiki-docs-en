---
doc_id: "mta-wiki:11990"
title: "PhysicsGetConstraints"
source_title: "PhysicsGetConstraints"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsGetConstraints"
revision_id: 65105
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.736182+00:00"
---

# PhysicsGetConstraints

Returns all constraints created in specific physics world.

## Syntax

```
table physicsGetConstraints(physics thePhysics)
```

### Required Arguments

- **physics:** The physics world.

### Returns

- **table of constraints:** {constraint, constraint, constraint, ...}

## Example

```
constraints = physicsGetConstraints(physics)
print("You have created ".. #constraints .." constraints so far!")
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

- physicsGetConstraints

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
