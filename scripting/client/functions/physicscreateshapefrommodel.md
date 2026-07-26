---
doc_id: "mta-wiki:12003"
title: "PhysicsCreateShapeFromModel"
source_title: "PhysicsCreateShapeFromModel"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsCreateShapeFromModel"
revision_id: 65196
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.529192+00:00"
---

# PhysicsCreateShapeFromModel

Creates shape from model in specific physics world. Model must be streamed in ( orignal gtasa models counts as stream in )

## Syntax

```
physics-shape physicsCreateShapeFromModel(physics thePhysics, int model)
```

### Required Arguments

- **thePhysics:** Physics world.

- **model:** object model.

### Returns

- **shape** compound shape made of triangle mesh, boxes and spheres.

## Example

Spawns hay, tree, barn, hay stack and fence as rigid body near by 0,0,0 coords

```
function createRigidBodyFromModel(model, x, y, z)
  local shape = physicsCreateShapeFromModel(physics, model)
  if(shape)then
    local rigid = physicsCreateRigidBody(shape)
    physicsSetProperties(rigid, "position",  x, y, z)
  end
end

createRigidBodyFromModel(3276, 0,0,10)
createRigidBodyFromModel(672, 20,0,10)
createRigidBodyFromModel(12918, -20,0,10)
createRigidBodyFromModel(3374, 0,20,10)
createRigidBodyFromModel(12919, 0,-30,10)
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](mta://scripting/client/functions/physicsdestroy.md)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- physicsCreateShapeFromModel

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
