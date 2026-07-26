---
doc_id: "mta-wiki:11981"
title: "PhysicsRayCast"
source_title: "PhysicsRayCast"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsRayCast"
revision_id: 65087
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.827483+00:00"
---

# PhysicsRayCast

Perform ray cast between two positions.

## Syntax

```
raycast-result physicsRayCast(physics thePhysics, raycast-type theType, float startX, float startY, float startZ, float endX, float endY, float endZ, bool filterBackfaces = false )
```

### Required Arguments

- **physics:** The physics world.

- **raycast-type:** Type of raycasting, see [Physics raycast type](mta://reference/misc/physics-raycast-type.md)

- **startXYZ:** Start position.

- **endXYZ:** End position.

- **filterBackfaces :** Detect hit of backfaces. TODO, tests needed

### Returns

- **raycast-result** raycast result, see [Physics raycast type](mta://reference/misc/physics-raycast-type.md)

## Example

```
result = physicsRayCast(physics, "default", 0,0,10, 0,0,0)
if result.hit then
  if result.rigidbody ~= false then
    print("Rigid body has been hit")
  elseif result.staticcollision ~= false then
    print("Static collision has been hit")
  end
end
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

- [physicsApplyDamping](mta://scripting/client/functions/physicsapplydamping.md)

- physicsRayCast

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
