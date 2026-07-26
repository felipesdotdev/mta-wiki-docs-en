---
doc_id: "mta-wiki:3353"
title: "AclGroupRemoveObject"
source_title: "AclGroupRemoveObject"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupRemoveObject"
revision_id: 78640
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.854183+00:00"
---

# AclGroupRemoveObject

This function removes the given object from the given ACL group. The object can be a resource or a player. See [aclGroupAddObject](mta://scripting/server/functions/aclgroupaddobject.md) for more details.

## Syntax

```
bool aclGroupRemoveObject ( aclgroup theGroup, string theObjectString )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):removeObject(...)*

### Required Arguments

- **theGroup:** The ACL group to remove the object string from

- **theObjectString:** The object to remove from the ACL group

### Returns

Returns *true* if the object existed in the ACL and could be removed, *false* if it could not be removed for some reason, ie. it did not exist in the given ACL group.

## Example

This example does...

```
function deladm (playerSource, commandName, accountName)
	if accountName then --Make the script able to detect if a user is given.
		aclGroupRemoveObject (aclGetGroup("Admin"), "user."..accountName) --Removing the admin.
		outputChatBox ("ACL: Account '"..accountName.."' succesfully removed as admin.", playerSource) -- Giving you a messsage.
		outputChatBox ("ACL: Someone have removed you as admin.", accountName) -- giving the poor removed guy a message.
	else --Make the Syntax display.
		outputChatBox ("ACL: No account name specified.", playerSource)
		outputChatBox ("ACL: Syntax: /deladmin [accountName]", playerSource)
	end
end
addCommandHandler ("deladmin", deladm)
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

- aclGroupRemoveObject

- [aclList](mta://scripting/server/functions/acllist.md)

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclReload](mta://scripting/server/functions/aclreload.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
