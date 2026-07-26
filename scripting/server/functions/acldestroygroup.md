---
doc_id: "mta-wiki:3346"
title: "AclDestroyGroup"
source_title: "AclDestroyGroup"
source_url: "https://wiki.multitheftauto.com/wiki/AclDestroyGroup"
revision_id: 69155
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.706385+00:00"
---

# AclDestroyGroup

This function destroys the given ACL group. The destroyed ACL group will no longer be valid.

## Syntax

```
bool aclDestroyGroup ( aclgroup aclGroup )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):destroy(...)*

### Required Arguments

- **aclGroup:** The [aclgroup](mta://reference/misc/aclgroup.md) element to destroy

### Returns

Returns *true* if the ACL group was successfully deleted, *false* if it could not be deleted for some reason (ie. invalid argument).

## Example

This example allows admins to remove an ACL group they specify.

```
function removeACLGroup ( source, command, groupName )
-- Check if they're an admin...
	if ( isObjectInACLGroup ( "user." .. getAccountName ( getPlayerAccount ( source )), aclGetGroup ( "Admin" ) ) ) then
		if ( groupName ) then -- Check if they specified the group name
			local group = aclGetGroup ( groupName ) -- Return any groups matching the name
				if ( group ) then -- If any were returned then...
					aclDestroyGroup ( group ) -- Destroy that group
				else
					-- Tell them if no groups with that name were found...
					outputChatBox ( "No group with that name was found.", source, 255, 0, 0 )
				end
	
		else -- If they didn't specify the group
			outputChatBox ( "Please specify the group name.", source, 255, 0, 0 ) -- Tell them that they must
		end
	else -- If they're not an admin....
		outputChatBox ( "You must be an admin to use this command", source, 255, 0, 0 ) -- Tell them it's restricted
	end
end
addCommandHandler ( "removeACL", removeACLGroup ) -- Make it happen when somebody types "/removeACL"
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- aclDestroyGroup

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

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
