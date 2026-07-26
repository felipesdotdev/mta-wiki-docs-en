---
doc_id: "mta-wiki:12013"
title: "PhysicsCreateRigidBody"
source_title: "PhysicsCreateRigidBody"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsCreateRigidBody"
revision_id: 65157
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.495462+00:00"
---

# PhysicsCreateRigidBody

Creates rigid body from shape

## Syntax

```
physics-rigid-body physicsCreateRigidBody( physics-shape theShape [ , float mass, float localInertiaX, float localInertiaY, float localInertiaZ, float centerOfMassX, float centerOfMassY, float centerOfMassZ ])
```

### Required Arguments

- **theShape :** the shape of rigid body

- **mass:** mass of rigid body, by default 1, must be greater than 0

- **localInertiaXYZ:** local inertia

- **centerOfMassYYZ:** center of mass

### Returns

Rigid body, false otherwise.

## Example

Crushing 27 boxes

```
local box = physicsCreateShape(physics, "box", 1)
local sphere = physicsCreateShape(physics, "sphere", 3)
local function crush()
  for x = 1,3 do
    for y = 1,3 do
      for z = 1,3 do
        local boxrb = physicsCreateRigidBody(box)
        physicsSetProperties(boxrb, "position", x*2,y*2,3 + z * 2)
      end
    end
  end
    
  local sphereOfDoom = physicsCreateRigidBody(sphere, 10000)
  physicsSetProperties(sphereOfDoom, "position", 3,3,50)
end
crush()
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](mta://scripting/client/functions/physicsdestroy.md)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- physicsCreateRigidBody

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
