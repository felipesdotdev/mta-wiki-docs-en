---
doc_id: "mta-wiki:12029"
title: "PhysicsCreateConstraint"
source_title: "PhysicsCreateConstraint"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsCreateConstraint"
revision_id: 65203
language: "en"
categories: ["Client_functions"]
---

# PhysicsCreateConstraint

Creates connection between rigid body and other rigid body or specified position.

## Syntax

```
physics-constraint physicsCreateConstraint(constraint-type theConstraintType [, disableCollisionsBetweenLinkedBodies = true], physics-rigid-body rigidBodyA [, physics-rigid-body rigidBodyB], mixed )
```

### Required Arguments

- **theConstraintType:** "pointtopoint", "hidge", "fixed", "slider", see [Physics constraints](https://wiki.multitheftauto.com/index.php?title=Physics_constraints&action=edit&redlink=1)

- **disableCollisionsBetweenLinkedBodies:** disable collision between two rigid bodies, useful when rigids are close to each other.

- **rigidBodyA:** first rigid body,

- **rigidBodyB:** second rigid body, optional, can be replaced with position in some cases.

- **mixed:** depends on constraint type

### Returns

- **physics** world used for simulation.

## Example

Spawns capsule and attach invisible line to the rigid body.

```
local capsule = physicsCreateShape(physics, "capsule", 0.5, 1.2)
local capsulerb = physicsCreateRigidBody(capsule );
physicsCreateConstraint("pointtopoint", capsulerb, 0,0,0)
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](https://wiki.multitheftauto.com/index.php?search=physicsDestroy)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- [physicsCreateRigidBody](mta://scripting/client/functions/physicscreaterigidbody.md)

- [physicsCreateStaticCollision](mta://scripting/client/functions/physicscreatestaticcollision.md)

- physicsCreateConstraint

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
