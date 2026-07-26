---
doc_id: "mta-wiki:12033"
title: "PhysicsIsElement"
source_title: "PhysicsIsElement"
source_url: "https://wiki.multitheftauto.com/wiki/PhysicsIsElement"
revision_id: 65214
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:28.810137+00:00"
---

# PhysicsIsElement

Returns whatever physics-element exists

## Syntax

```
bool physicsIsElement(physics-element thePhysicsElement)
```

### Required Arguments

- **thePhysicsElement:** physics element: shape, constraint, rigid body, static collision

### Returns

True if physics element exists

## Example

if shape got destroyed, static collisions, rigid body and its constraints will destroyed too, this example prove it.

```
local shape = physicsCreateShape(physics, "box", 1)
local rb = physicsCreateRigidBody(shape)
local col = physicsCreateStaticCollision(shape)
local const = physicsCreateConstraint("pointtopoint", rb, 0,0,0)
iprint("isElement before", physicsIsElement(shape), physicsIsElement(rb), physicsIsElement(col), physicsIsElement(const)) -- true, true, true, true
physicsDestroy(shape)
iprint("isElement after", physicsIsElement(shape), physicsIsElement(rb), physicsIsElement(col), physicsIsElement(const)) -- false, false, false ,false
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

- [physicsShapeCast](mta://scripting/client/functions/physicsshapecast.md)

- [physicsGetElementType](mta://scripting/client/functions/physicsgetelementtype.md)

- physicsIsElement
