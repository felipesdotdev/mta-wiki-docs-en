---
doc_id: "mta-wiki:12008"
title: "PhysicsApplyVelocity"
source_title: "PhysicsApplyVelocity"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsApplyVelocity"
revision_id: 65150
language: "en"
categories: ["Client_functions"]
---

# PhysicsApplyVelocity

Applies velocity to rigid body

## Syntax

```
bool physicsApplyVelocity( physics-rigid-body theRigidBody, float velocityX, float velocityY, float velocityZ [, float relativeX, float relativeY, float relativeZ ] )
```

### Required Arguments

- **theRigidBody:** rigid body you want to apply velocity

- **velocityXYZ:** velocity you wants to apply

- **relativeXYZ:** relative position, default: 0,0,0

### Returns

True if velocity got applied, false otherwise.

## Example

Doing box flip

```
local box = physicsCreateShape(physics, "box", 1)
local function spawnTestBox(x,y,z)
  local boxrb = physicsCreateRigidBody(box)
  physicsSetProperties(boxrb, "position", x,y,z)
  return boxrb;
end

local notATable = spawnTestBox(0,0,5)
setTimer(function()
  physicsApplyVelocity(notATable , 0,0,10, 0,1,0)
end,500,1) -- let box land on the ground.
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

- physicsApplyVelocity

- [physicsApplyVelocityForce](mta://scripting/client/functions/physicsapplyvelocityforce.md)

- [physicsApplyAngularVelocity](mta://scripting/client/functions/physicsapplyangularvelocity.md)

- [physicsApplyAngularVelocityForce](mta://scripting/client/functions/physicsapplyangularvelocityforce.md)

- [physicsApplyDamping](mta://scripting/client/functions/physicsapplydamping.md)

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
