---
doc_id: "mta-wiki:11997"
title: "PhysicsAddChildShape"
source_title: "PhysicsAddShape"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsAddShape"
revision_id: 65122
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.356798+00:00"
---

# PhysicsAddChildShape

Adds child shape to already existing, compound shape. Limit: 8196 child shapes.

## Syntax

```
boolean physicsAddChildShape(physics-shape compoundShape, physics-shape childShape [, float offsetX, float offsetY, float offsetZ [, float offsetRotationX, float  offsetRotationY, float offsetRotationZ] ] )
```

### Required Arguments

- **compoundShape:** Must be compound shape

- **childShape:** Can not be compound shape

- **offsetXYZ:** Offset position of center

- **rotationXYZ:** Offset rotationof center

### Returns

True, if shape got added. False otherwise.

## Example

Creates something that reminds chain

```
local compound = physicsCreateShape(physics, "compound")
local capsule = physicsCreateShape(physics, "capsule", 0.2,1.5)
physicsAddChildShape(compound, capsule)
physicsAddChildShape(compound, capsule, 0,1,0.5, 45,0,0)
physicsAddChildShape(compound, capsule, 0,1,0.5, 45,0,0)
physicsAddChildShape(compound, capsule, 0,-1,0.5, -45,0,0)
physicsAddChildShape(compound, capsule, 0,-0.8,1.5, 120,0,0)
physicsAddChildShape(compound, capsule, 0,0.8,1.5, -120,0,0)

function createChainLink(x,y,z,rx,ry,rz)
  local link = physicsCreateRigidBody(physics,compound)
  physicsSetProperties(link, "position", x,y,z)
  physicsSetProperties(link, "rotation", rx,ry,rz)
end

function createChain()
  for i=1,2 do
    createChainLink(0,0,5 + i,0,0,0)
    createChainLink(0,0,6 + i,0,0,90)
  end
end
createChain()
```

## See Also

- [physicsCreateWorld](mta://scripting/client/functions/physicscreateworld.md)

- [physicsDestroy](mta://scripting/client/functions/physicsdestroy.md)

- [physicsCreateShape](mta://scripting/client/functions/physicscreateshape.md)

- [physicsCreateShapeFromModel](mta://scripting/client/functions/physicscreateshapefrommodel.md)

- [physicsCreateRigidBody](mta://scripting/client/functions/physicscreaterigidbody.md)

- [physicsCreateStaticCollision](mta://scripting/client/functions/physicscreatestaticcollision.md)

- [physicsCreateConstraint](mta://scripting/client/functions/physicscreateconstraint.md)

- physicsAddChildShape

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
