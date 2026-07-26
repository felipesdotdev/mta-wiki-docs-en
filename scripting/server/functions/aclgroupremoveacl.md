---
doc_id: "mta-wiki:3351"
title: "AclGroupRemoveACL"
source_title: "AclGroupRemoveACL"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupRemoveACL"
revision_id: 68736
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.812457+00:00"
---

# AclGroupRemoveACL

This function removes the given ACL from the given ACL group.

| [[{{{image}}}\|link=\|]] | Note: The resource that's using this function needs the right to remove an acl. |
| --- | --- |
|  |  |

## Syntax

```
bool aclGroupRemoveACL ( aclgroup theGroup, acl theACL )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):removeACL(...)*

### Required Arguments

- **theGroup:** The group to remove the given ACL from

- **theACL:** The ACL to remove from the given group

### Returns

Returns *true* if the ACL was successfully removed from the ACL group, *false*/*nil* if it could not be removed for some reason, ie. either of the elements were invalid.

## Example

This example outputs to the console if the Admin acl was removed from the Moderator ACL Group. (TESTED!)

```
addEventHandler("onResourceStart",resourceRoot,function()
	if(aclGroupRemoveACL(aclGetGroup("Moderator"),aclGet("Admin")))then
		aclSave()
		outputConsole("The Admin acl was removed from the Moderator group.")-- If it was successfully removed
	else
		outputConsole("Unsuccessful... Admin might have been removed from the Moderator group before.")-- if it was removed before or didn't existed
	end
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

- aclGroupRemoveACL

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
