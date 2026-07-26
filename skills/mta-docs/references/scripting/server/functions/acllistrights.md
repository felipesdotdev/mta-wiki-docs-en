---
doc_id: "mta-wiki:3417"
title: "AclListRights"
source_title: "AclListRights"
source_url: "https://wiki.multitheftauto.com/wiki/AclListRights"
revision_id: 68739
language: "en"
categories: ["Server_functions"]
---

# AclListRights

This function returns a table of all the rights that a given ACL has.

## Syntax

```
table aclListRights ( acl theACL, string allowedType )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):listRights(...)*

### Required Arguments

- **theACL:** The ACL to get the rights from

- **allowedType:** The allowed right type. Possible values are *general*, *function*, *resource* and *command*

### Returns

Returns a table over the rights as strings in the given ACL. This table might be empty. Returns *false* or *nil* if theACL is invalid or it fails for some other reason.

## Example

This example outputs the rights of the given acl. (TESTED!)

```
addCommandHandler("aclRights",function(player,command,theAcl)
	if(theAcl~="")then
		rights = aclListRights(aclGet(theAcl))
		count = 0
		for acl,list in pairs(rights)do
			outputChatBox("ACL List: "..theAcl.." #"..tostring(count).." Right: "..list..".",player)
			count = count + 1
		end
	else
		outputChatBox("Please type in a acl that you want to retrieve the rights from.",player)
		outputChatBox("Please use this Syntax: /aclRights theACL ",player)
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

- [aclObjectGetGroups](mta://scripting/server/functions/aclobjectgetgroups.md)

- [aclGroupRemoveObject](mta://scripting/server/functions/aclgroupremoveobject.md)

- [aclList](mta://scripting/server/functions/acllist.md)

- aclListRights

- [aclReload](mta://scripting/server/functions/aclreload.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
