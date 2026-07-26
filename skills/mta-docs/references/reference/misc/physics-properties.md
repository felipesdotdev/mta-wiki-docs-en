---
doc_id: "mta-wiki:11977"
title: "Physics properties"
source_title: "Physics properties"
source_url: "https://wiki.multitheftauto.com/wiki/Physics_properties"
revision_id: 65215
language: "en"
categories: []
---

# Physics properties

Physics properties

used in

- [physicsSetProperties](mta://scripting/client/functions/physicssetproperties.md)

- [physicsGetProperties](https://wiki.multitheftauto.com/index.php?title=PhysicsGetProperties&action=edit&redlink=1)

| Name | Support | Access | Parametrs | Description |
| --- | --- | --- | --- | --- |
| mass | rigid-body | set, get | float mass | Changes mass of rigid body. |
| position | rigid-body, static-collision | set, get | float x, float y, float z | Sets/gets position. |
| position | constraint | get | float x, float y, float z | Returns avarge position of two rigids. |
| rotation | rigid-body, static-collision | set, get | float rx, float ry, float rz | Sets/gets rotation. |
| velocity | rigid-body | set, get | float velocityX, float velocityY, float velocityZ | Sets/gets velocity. |
| angularvelocity | rigid-body | set, get | float velocityX, float velocityY, float velocityZ | Sets/gets angular velocity. |
| sleepingthresholds | rigid-body | set, get | float velocity, float angularVelocity | Sets how slow rigid body have to move, to go sleep. |
| simulationenabled | physics-world | set, get | bool enabled = true | Enable/disable simulation. |
| simulationsubsteps | physics-world | set, get | int subSteps = 10 | Between 1 and 256, sets how long and how precise collision detection should be. |
| restitution | rigid-body | set, get | float value | todo |
| scale | physics-shape, rigid-body, static-collision | set, get | float scaleX, float scaleY, float scaleZ | Sets/gets scale, if rigid of static collision as parametr, their shape scale got set/get. You can't scale per rigid/static collision |
| debugcolor | physics-shape, rigid-body, static-collision | set, get | color theColor / boolean false resets color | Changes debug color |
| filtermask | todo | set, get | todo | todo |
| filtergroup | todo | set, get | todo | todo |
| stiffness | todo | set, get | todo | todo |
| size | shape | set, get | float sizeX, float sizeY, float sizeZ | Changes size of "box" shape type. |
| radius | todo | set, get | todo | todo |
| height | todo | set, get | todo | todo |
| boundingbox | todo | get | todo | todo |
| boundingsphere | todo | get | todo | todo |
| gravity | physics-world | set, get | float gravityX, float gravityY, float gravityZ | Changes gravity of the simulation |
| usecontinuous | physics-world | set, get | bool bEnabled | False by default, enable detection of rigid body which happened between two simulation steps. Cause increased simulation time, prevents small shapes fly through thick surfaces |
| motionthreshold | todo | set, get | todo | todo |
| sweptsphereradius | todo | set, get | todo | todo |
| pivota | todo | set, get | todo | todo |
| pivotb | todo | set, get | todo | todo |
| lowerlinlimit | todo | set, get | todo | todo |
| upperlinlimit | todo | set, get | todo | todo |
| loweranglimit | todo | set, get | todo | todo |
| upperanglimit | todo | set, get | todo | todo |
| breakingimpulsethreshold | todo | set, get | todo | todo |
| appliedimpulse | todo | set, get | todo | todo |
| jointfeedback | todo | set, get | todo | todo |
| constraintbroken | todo | set, get | todo | todo |
| triggercollisionevents | physics-world | set, get | bool bEnabled = false | Cause physics world starts to trigger collision events. Don't enable if you don't use them. Can cause spam. |
| triggerconstraintevents | physics-world | set, get | bool bEnabled = false | Cause physics world starts to trigger constraints events. Don't enable if you don't use them. Can cause spam. |
| rigidbodya | todo | set, get | todo | todo |
| rigidbodyb | todo | set, get | todo | todo |
| sleep | todo | set, get | todo | todo |
| wantssleeping | todo | set, get | todo | todo |
| iscompound | todo | set, get | todo | todo |
| iscocave | todo | set, get | todo | todo |
| isconvex | todo | set, get | todo | todo |
| isconvex2d | todo | set, get | todo | todo |
| isinfinite | todo | set, get | todo | todo |
| isnonmoving | todo | set, get | todo | todo |
| ispolyhedral | todo | set, get | todo | todo |
| issoftbody | todo | set, get | todo | todo |
