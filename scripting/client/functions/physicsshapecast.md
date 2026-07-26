---
doc_id: "mta-wiki:12004"
title: "PhysicsShapeCast"
source_title: "PhysicsShapeCast"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsShapeCast"
revision_id: 65143
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.919645+00:00"
---

# PhysicsShapeCast

Tests collision ( like ray cast ) between two position having shape you provided.
Remember to let world update before cast, just wait one frame.

## Syntax

```
table physicsShapeCast(physics-shape theShape, float startX, float startY, float startZ, float endX, float endY, float endZ [ , float startRotationX, float startRotationY, float startRotationZ, float endRotationX, float endRotationY, float endRotationZ ] )
```

### Required Arguments

- **theShape:** Primitive shape, supported shapes: "box", "sphere", "cone", "cylinder"

- **startXYZ:** start position.

- **endXYZ:** end position.

- **startRotationXYZ:** start rotation, by default 0,0,0.

- **endRotationXYZ:** end rotation, by default 0,0,0.

### Returns

table with content:

- **hit** boolean - indicate does hit occurs.

- **shapeposition** {x,y,z} - position of shape in moment of contact.

- **shaperotation** {x,y,z} - rotation of shape in moment of contact.

- **hitpoint** {x,y,z} - contact point.

- **hitnormal** {x,y,z} - contact normal vector.

- **shape** physics-shape - contact shape.

- **staticcollision** physics-shape - contact static collision, can be false.

- **rigidbody** physics-rigid-body - contact rigid body, can be false.

## Example

Creates giant random tetris

```
local function dropShapeAtPosition(shape, x,y,z)
  local result = physicsShapeCast(shape, x,y,z + 1000, x,y,z - 1000)
  if(result.hit)then
    local collision = physicsCreateStaticCollision(physics, shape)
    physicsSetProperties(collision, "position", result.shapeposition[1], result.shapeposition[2], result.shapeposition[3])
    physicsSetProperties(collision, "rotation", result.shaperotation[1], result.shaperotation[2], result.shaperotation[3])
  end
end

function tetris()
  setTimer(function()
      local box = physicsCreateShape(physics, "box", math.random() * 5 + 1, math.random() * 5 + 1, math.random() * 2 + 1)
      dropShapeAtPosition(box, math.random(60),math.random(60),0)
  end,0,1000)
end
tetris()
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

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

- physicsShapeCast

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
