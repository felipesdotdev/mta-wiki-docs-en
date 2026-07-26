---
doc_id: "mta-wiki:3336"
title: "AclSave"
source_title: "AclSave"
source_url: "https://wiki.multitheftauto.com/wiki/AclSave"
revision_id: 68742
language: "en"
categories: ["Server_functions"]
---

# AclSave

The ACL XML file is automatically saved whenever the ACL is modified, but the automatic save can be delayed by up to 10 seconds for performance reasons. Calling this function will force an immediate save.

## Syntax

```
bool aclSave ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the ACL class.*

**Method**: *[ACL](https://wiki.multitheftauto.com/index.php?search=ACL).save(...)*

### Returns

Returns *true* if the ACL was successfully changed, *false* or *nil* if it could not be saved for some reason, ie. file in use.

## Example

This example saves the ACL when somebody types "/save-acl".

```
function saveACL ( thePlayer, command ) -- Function header. Also where thePlayer is defined.
	local saved = aclSave() -- Save the ACL
		if ( saved ) then -- If it was successfully saved then...
			outputChatBox ( "ACL was successfully saved.", thePlayer, 255, 0, 0 ) -- Output it saved
		else -- If it wasn't saved for whatever reason then...
			outputChatBox ( "An unexpected error occured.", thePlayer, 255, 0, 0 ) -- Output it didn't save
		end
end
addCommandHandler ( "save-acl", saveACL ) -- Make it trigger for "/save-acl".
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

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- aclSave

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
