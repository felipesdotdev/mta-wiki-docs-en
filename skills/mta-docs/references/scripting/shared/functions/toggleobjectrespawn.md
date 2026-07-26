---
doc_id: "mta-wiki:7000"
title: "ToggleObjectRespawn"
source_title: "ToggleObjectRespawn"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleObjectRespawn"
revision_id: 80105
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2", "Changes_in_1.6.0"]
---

# ToggleObjectRespawn

This function is used to toggle if an object should respawn after it got destroyed

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

This function is now also available on the server side. 

| [[{{{image}}}\|link=\|]] | Note: The object will be respawned when it is streamed |
| --- | --- |
|  |  |

## Syntax

```
bool toggleObjectRespawn ( object theObject, bool respawn )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):toggleRespawn(...)*

### Required Arguments

- **theObject**: the object you want to toggle the respawn from

- **respawn**: a bool denoting whether we want to enable (*true*) or disable (*false*) respawning

### Returns

- *true* when the it was changed successfully.

- *false* otherwise.

## Example

This example adds command *tos* that toggles respawn of all the objects.

```
local respawn = false
addCommandHandler("tos",
	function ()
		for i, object in pairs(getElementsByType("object")) do
			toggleObjectRespawn(object, not respawn)
		end
		outputChatBox("Object respawning " .. (respawn and "disabled" or "enabled"))
		respawn = not respawn
	end)
```

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- toggleObjectRespawn

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)
