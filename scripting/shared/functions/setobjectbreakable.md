---
doc_id: "mta-wiki:6215"
title: "SetObjectBreakable"
source_title: "SetObjectBreakable"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectBreakable"
revision_id: 81113
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:41.647874+00:00"
---

# SetObjectBreakable

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

Added also as a server-side function. Previously only available as a client-side function. 

This function sets an object to be breakable/unbreakable.

## Syntax

```
bool setObjectBreakable ( object theObject, bool breakable )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):setBreakable(...)*

**Variable**: *.breakable*

**Counterpart**: *[isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)*

### Required Arguments

- **object** the [object](mta://reference/misc/object.md) that's being set.

- **breakable** a boolean whether the object is breakable (true) or unbreakable (false).

### Returns

- *true* if the object is now breakable.

- *false* if it can't or if invalid arguments are passed.

## Example

This example creates an object when the resource starts and sets it to be breakable.

```
function toggleObjectVulnerability()
	local object = createObject(1337, 5540.6654, 1020.55122, 1240.545)
	if isObjectBreakable(object) then
		setObjectBreakable(object, false)
		outputChatBox("The object is now not breakable.")
	else
		setObjectBreakable(object, true)
		outputChatBox("The object is now breakable.")
	end
end
addEventHandler("onClientResourceStart", resourceRoot, toggleObjectVulnerability)
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

- setObjectBreakable

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)
