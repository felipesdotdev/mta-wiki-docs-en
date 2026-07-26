---
doc_id: "mta-wiki:12032"
title: "PhysicsGetElementType"
source_title: "PhysicsGetElementType"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsGetElementType"
revision_id: 65212
language: "en"
categories: ["Client_functions"]
---

# PhysicsGetElementType

Returns type of physics-element

## Syntax

```
string physicsGetElementType(physics-element thePhysicsElement)
```

### Required Arguments

- **thePhysicsElement:** physics element: shape, constraint, rigid body, static collision

### Returns

Name of physics element, "shape", "rigidbody", "staticcollision", "constraint"

## Example

```
local shape = physicsCreateShape(physics, "box", 1)
local rb = physicsCreateRigidBody(shape)
local col = physicsCreateStaticCollision(shape)
local const = physicsCreateConstraint("pointtopoint", rb, 0,0,0)
iprint("shape: ",physicsGetElementType(shape)) -- shape
iprint("rigidbody: ",physicsGetElementType(rb)) -- rigidbody
iprint("staticcollision: ",physicsGetElementType(col)) -- staticcollision
iprint("constraint: ",physicsGetElementType(const)) -- constraint
iprint("invalid: ",physicsGetElementType(physics)) -- false
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

- [physicsApplyVelocity](mta://scripting/client/functions/physicsapplyvelocity.md)

- [physicsApplyVelocityForce](mta://scripting/client/functions/physicsapplyvelocityforce.md)

- [physicsApplyAngularVelocity](mta://scripting/client/functions/physicsapplyangularvelocity.md)

- [physicsApplyAngularVelocityForce](mta://scripting/client/functions/physicsapplyangularvelocityforce.md)

- [physicsApplyDamping](mta://scripting/client/functions/physicsapplydamping.md)

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- physicsGetElementType

- [physicsIsElement](mta://scripting/client/functions/physicsiselement.md)
