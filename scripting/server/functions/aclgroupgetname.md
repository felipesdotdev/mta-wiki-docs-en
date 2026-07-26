---
doc_id: "mta-wiki:3349"
title: "AclGroupGetName"
source_title: "AclGroupGetName"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupGetName"
revision_id: 68810
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.768226+00:00"
---

# AclGroupGetName

This function is used to get the name of the given ACL group.

## Syntax

```
string aclGroupGetName ( aclgroup aclGroup )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):getName(...)*

**Variable**: *.name*

### Required Arguments

- **aclGroup:** The ACL group to get the name of

### Returns

Returns the name of the given ACL group as a string if successful, otherwise *false* or *nil* if the aclGroup is invalid or it fails for some other reason.

## Example

This example outputs to the console that "Admin's are ready to watch :)".

```
addEventHandler("onResourceStart", resourceRoot, function()
	outputConsole(aclGroupGetName(aclGetGroup("Admin")).."'s are ready to watch :)",root)
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

- aclGroupGetName

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

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
