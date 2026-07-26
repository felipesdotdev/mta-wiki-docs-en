---
doc_id: "mta-wiki:3335"
title: "AclReload"
source_title: "AclReload"
source_url: "https://wiki.multitheftauto.com/wiki/AclReload"
revision_id: 68740
language: "en"
categories: ["Server_functions"]
---

# AclReload

This function reloads the ACL's and the ACL groups from the ACL XML file. All ACL and ACL group elements are invalid after a call to this and should not be used anymore.

## Syntax

```
bool aclReload ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the ACL class.*

**Method**: *[ACL](https://wiki.multitheftauto.com/index.php?search=ACL).reload(...)*

### Returns

Returns *true* if the XML was successfully reloaded from the file, *false* or *nil* if the XML was invalid, didn't exist or could not be loaded for some other reason.

## Example

This example allows an admin to reload the ACL by typing "/reloadACL".

```
function reloadACL ( source, command )
-- Check if they're an admin...
	if ( isObjectInACLGroup ( "user." .. getAccountName ( getPlayerAccount ( source )), aclGetGroup ( "Admin" ) ) ) then
		local reload = aclReload() -- Reload the ACL
			if ( reload ) then -- Check it was reloaded successfully
				outputChatBox ( "ACL was successfully reloaded.", source, 255, 0, 0 ) -- If so, output it
			else -- If not, output it (line below)
				outputChatBox ( "An unknown error occured. Please check the ACL file exists.", source, 255, 0, 0 )
			end
	else -- If they're not an admin, output it (below)
		outputChatBox ( "You must be an admin to use this command!", source, 255, 0, 0 )
	end
end
addCommandHandler ( "reloadACL", reloadACL )
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

- aclReload

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
