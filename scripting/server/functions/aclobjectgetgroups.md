---
doc_id: "mta-wiki:14182"
title: "AclObjectGetGroups"
source_title: "AclObjectGetGroups"
source_url: "https://wiki.multitheftauto.com/wiki/AclObjectGetGroups"
revision_id: 78274
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:19.865017+00:00"
---

# AclObjectGetGroups

ADDED/UPDATED IN VERSION 1.6.0 [r22273](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22273):

This function returns a table of all groups the object is in.

## Syntax

```
table aclObjectGetGroups ( string object )
```

### Required Arguments

- **object:** The name of the ACL entry to get groups of

### Returns

Returns a table of all groups the object is in on success, false if something went wrong.

## Examples

This example outputs a list of all groups of the calling user

Click to collapse [-]

```
addCommandHandler("listGroups",function(player)
	local account = getPlayerAccount(player)
	if not account or isGuestAccount(account) then return end

	outputChatBox('Groups:', player)
	local groups = aclObjectGetGroups('user.'..getAccountName(account)) 

	for _,v in ipairs(groups) do
		outputChatBox('* '..aclGroupGetName(v))
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

- [aclGroupRemoveACL](mta://scripting/server/functions/aclgroupremoveacl.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22273](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22273):

- aclObjectGetGroups

- [aclGroupRemoveObject](mta://scripting/server/functions/aclgroupremoveobject.md)

- [aclList](mta://scripting/server/functions/acllist.md)

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclReload](mta://scripting/server/functions/aclreload.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
