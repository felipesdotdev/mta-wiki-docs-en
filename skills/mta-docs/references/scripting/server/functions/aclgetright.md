---
doc_id: "mta-wiki:3342"
title: "AclGetRight"
source_title: "AclGetRight"
source_url: "https://wiki.multitheftauto.com/wiki/AclGetRight"
revision_id: 69168
language: "en"
categories: ["Server_functions"]
---

# AclGetRight

This function returns whether the access for the given right is set to true or false in the ACL.

## Syntax

```
bool aclGetRight ( acl theAcl, string rightName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):getRight(...)*

**Counterpart**: *[aclSetRight](mta://scripting/server/functions/aclsetright.md)*

### Required Arguments

- **theAcl:** The ACL to get the right from

- **rightName:** The right name to return the access value of.

### Returns

Returns *true* or *false* if the ACL gives access or not to the given function. Returns *nil* if it failed for some reason, e.g. an invalid ACL was specified or the right specified does not exist in the ACL.

## Example

This example lets players check if an ACL group has access to something or not.

```
--theACL examples: Admin, Default, Moderator
--theRight examples: command.debugscript, function.banPlayer

function aclRightCheck(player, command, theACL, theRight)
	if (theACL and theRight) then -- Make sure atleast two arguments were entered.
		local theACL = aclGet(theACL) -- If theACL exists then convert it into an ACL pointer from a string.
		if (theACL) then -- If the ACL was found.
			local theReturn = aclGetRight(theACL, theRight) -- Will return true if it was found in the ACL.
			outputChatBox("The ACL right was found and returned: "..tostring(theReturn), player, 0, 255, 0)
		else
			outputChatBox("The ACL you entered was not found to exist in the ACL file.", player, 255, 0, 0) -- When the ACL was not found.
		end
	else
		outputChatBox("You need to enter an ACL, and a right name.", player, 255, 0, 0) -- When 2 arguements weren't entered.
	end
end
addCommandHandler("aclgetright", aclRightCheck) -- When a player does the aclgetright command it calls aclRightCheck function above.
-- Example of use: /aclgetright Admin command.debugscript (this should return true)
-- Example of use: /aclgetright Default command.debugscript (this should return false)
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclDestroyGroup](mta://scripting/server/functions/acldestroygroup.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- [aclGetGroup](mta://scripting/server/functions/aclgetgroup.md)

- [aclGetName](mta://scripting/server/functions/aclgetname.md)

- aclGetRight

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

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
