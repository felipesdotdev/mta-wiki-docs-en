---
doc_id: "mta-wiki:3957"
title: "SetObjectStatic"
source_title: "SetObjectStatic"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectStatic"
revision_id: 49171
language: "en"
categories: ["Client_functions", "Deprecated"]
---

# SetObjectStatic

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setElementFrozen instead. |  |

Makes an object static or non-static. Static objects are rock solid in one place, unaffected by gravity and pushing. Nonstatic objects can fall, be pushed around etc.

**Note1:** Not all objects that are static by default can be made nonstatic.

**Note2:** Dynamic objects with a "destroyed" state are still destroyable. Use [isElementOnScreen](mta://scripting/client/functions/iselementonscreen.md) to detect, destroy, and recreate these objects.

## Syntax

```
bool setObjectStatic ( object theObject, bool toggle )
```

### Required Arguments

- **theObject:** the object whose behaviour you want to change.

- **toggle:** *true* makes the object static, *false* makes it nonstatic.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

## See Also

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
