---
doc_id: "mta-wiki:11891"
title: "EngineRestoreObjectGroupPhysicalProperties"
source_title: "EngineRestoreObjectGroupPhysicalProperties"
source_url: "https://wiki.multitheftauto.com/wiki/EngineRestoreObjectGroupPhysicalProperties"
revision_id: 81230
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
---

# EngineRestoreObjectGroupPhysicalProperties

This function restores all physical properties of given properties group.

## Syntax

```
bool engineRestoreObjectGroupPhysicalProperties ( int groupID )
```

### Required Arguments

- **groupID**: the id of physical properties group which you wish to restore.

### Returns

Returns **true** if everything went well, error is raised otherwise.

## Example

Click to collapse [-]
Client

```
function restorePhysicalGroup(_, group)
    engineRestoreObjectGroupPhysicalProperties(tonumber(group))
end
addCommandHandler ( "restorePhysicalGroup", restorePhysicalGroup )
--restorePhysicalGroup(120)
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

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)
