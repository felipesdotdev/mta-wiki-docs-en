---
doc_id: "mta-wiki:2379"
title: "Element/Object"
source_title: "Element/Object"
source_url: "https://wiki.multitheftauto.com/wiki/Element/Object"
revision_id: 80972
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:14:54.000732+00:00"
---

# Element/Object

The object class represents dynamic and static 3D models placed in the GTA world.

The element type of this class is **"object"**.

## Important info about [Objects](mta://reference/misc/object.md)

- Objects only represent models **created by a script**, they do not represent objects that are part of GTA's default landscape (these belong to the "building pool").

- There is a distinction in GTA: San Andreas between static and dynamic models. The alternative [createBuilding](mta://scripting/shared/functions/createbuilding.md) function allows you to create objects that are non-dynamic, utilizing the GTA Building pool, which makes better use of memory.

- The [createObject](mta://scripting/shared/functions/createobject.md) function can also create non-dynamic objects, but for optimization reasons **it is recommended to spawn [Buildings](mta://development/building.md) when creating static objects that don't rely on the [Dimension](mta://reference/misc/dimension.md) system** (buildings don't use the same MTA object-streaming system).

## Object Models

[List of Object Model IDs](mta://reference/misc/object-ids.md)

## XML syntax

```
<object model="" posX="" posY="" posZ="" rotX="" rotY="" rotZ="" interior="" dimension="" scale="" collisions="" alpha="" frozen="" />
```

### Required Attributes

- **model**: The ID of the object being created.

- **posX**: A float representing the X position of the object.

- **posY**: A float representing the Y position of the object.

- **posZ**: A float representing the Z position of the object.

### Optional Attributes

- **rotX**: A float representing the X rotation of the object in degrees.

- **rotY**: A float representing the Y rotation of the object in degrees.

- **rotZ**: A float representing the Z rotation of the object in degrees.

- **interior**: The interior world the object is in.

- **dimension**: The object's dimension number.

- **scale**: The object's scale.

- **collisions**: Enable/Disable object collisions.

- **alpha**: Changes the object alpha.

- **frozen**: Sets whether the object should be frozen (also known as static)

## Related scripting functions

**Client**

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)
