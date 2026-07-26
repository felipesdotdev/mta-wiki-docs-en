---
doc_id: "mta-wiki:7106"
title: "SetObjectMass"
source_title: "SetObjectMass"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectMass"
revision_id: 42537
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
---

# SetObjectMass

This function sets the mass of a specified object. Changing the mass leads to a different movement behavior for especially dynamic objects.

## Syntax

```
bool setObjectMass ( object theObject, float mass )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):setMass(...)*

**Variable**: *.mass*

**Counterpart**: *[getObjectMass](mta://scripting/client/functions/getobjectmass.md)*

### Required Arguments

- **theObject:** the object whose mass will be set.

- **mass:** the new mass.

### Returns

- *true* if the new mass value has been.

- *false* otherwise.

## Example

This script basically creates an object then get's the mass and set's its mass 300 more than it's original mass, then tell the client the old and new mass of the object.

```
local object = createObject(1225,0,0,3)
local oldMass = getObjectMass(object)
local newMass = oldMass+300.0
setObjectMass(object,newMass)
outputChatBox("Object Old Mass: "..oldMass..", New Mass: "..newMass)
```

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

- setObjectMass

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)
