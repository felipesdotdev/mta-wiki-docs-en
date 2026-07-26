---
doc_id: "mta-wiki:3344"
title: "AclRemoveRight"
source_title: "AclRemoveRight"
source_url: "https://wiki.multitheftauto.com/wiki/AclRemoveRight"
revision_id: 68741
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.668446+00:00"
---

# AclRemoveRight

This function removes the given right (string) from the given ACL.

## Syntax

```
bool aclRemoveRight ( acl theAcl, string rightName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):removeRight(...)*

### Required Arguments

- **theAcl:** The ACL to remove the right from

- **rightName:** The ACL name to remove from the right from

### Returns

Returns *true* if the given right was successfully removed from the given ACL, *false* or *nil* if it could not be removed for some reason, ie. it didn't exist in the ACL.

## Example

This example removes an acl right on resource start.

```
addEventHandler("onResourceStart",resourceRoot,function()
   aclRemoveRight(aclGet("Admin"),"function.setServerPassword")
end)
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclDestroyGroup](mta://scripting/server/functions/acldestroygroup.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- [aclGetGroup](mta://scripting/server/functions/aclgetgroup.md)

- [aclGetName](mta://scripting/server/functions/aclgetname.md)

- [aclGetRight](mta://scripting/server/functions/aclgetright.md)

- [aclGroupAddACL](mta://scripting/server/functions/aclgroupaddacl.md)

- [aclGroupAddObject](mta://scripting/server/functions/aclgroupaddobject.md)

- [aclGroupGetName](mta://scripting/server/functions/aclgroupgetname.md)

- [aclGroupList](mta://scripting/server/functions/aclgrouplist.md)

- [aclGroupListACL](mta://scripting/server/functions/aclgrouplistacl.md)

- [aclGroupListObjects](mta://scripting/server/functions/aclgrouplistobjects.md)

- [aclGroupRemoveACL](mta://scripting/server/functions/aclgroupremoveacl.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22273](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22273):

- [aclObjectGetGroups](mta://scripting/server/functions/aclobjectgetgroups.md)

- [aclGroupRemoveObject](mta://scripting/server/functions/aclgroupremoveobject.md)

- [aclList](mta://scripting/server/functions/acllist.md)

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclReload](mta://scripting/server/functions/aclreload.md)

- aclRemoveRight

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
