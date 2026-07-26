---
doc_id: "mta-wiki:3415"
title: "AclGroupListACL"
source_title: "AclGroupListACL"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupListACL"
revision_id: 68734
language: "en"
categories: ["Server_functions"]
---

# AclGroupListACL

This function returns a table over all the ACL's that exist in a given ACL group.

## Syntax

```
table aclGroupListACL ( aclgroup theGroup )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):listACL(...)*

**Variable**: *.aclList*

### Required Arguments

- **theGroup:** The ACL group to get the ACL elements from

### Returns

Returns a table of the ACL elements in the given ACL group. This table might be empty. Returns *false* or *nil* if theGroup is invalid or it fails for some other reason.

## Example

This example outputs the list of ACL's if the aclGroup name is given. (TESTED!)

```
addCommandHandler("aclList",function(player,command,aclGroup)
	if(aclGroup~="")then
		tables = aclGroupListACL(aclGetGroup(aclGroup))
		count = 0
		for list,nam in pairs(tables) do
			outputChatBox("ACL LIST: "..aclGroup.."Line: "..tostring(count).." ACL: "..aclGetName(nam)..".",player)
			count = count + 1
		end
	else
		outputChatBox("Please add the aclGroup you want the list of.",player)
		outputChatBox("Syntax: /aclList aclGroup",player)
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

- aclGroupListACL

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
