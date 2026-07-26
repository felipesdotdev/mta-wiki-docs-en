---
doc_id: "mta-wiki:3352"
title: "AclGroupAddObject"
source_title: "AclGroupAddObject"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupAddObject"
revision_id: 76952
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.834377+00:00"
---

# AclGroupAddObject

This function adds an object to the given ACL group. An object can be a player's account, specified as:

```
user.<accountname>
```

Or a resource, specified as:

```
resource.<resourcename>
```

Objects are specified as strings. The ACL groups work for the user accounts and the resources that are specified in them.

## Syntax

```
bool aclGroupAddObject ( aclgroup theGroup, string theObjectName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):addObject(...)*

### Required Arguments

- **theGroup:** The group to add the object name string too.

- **theObjectName:** The object string to add to the given ACL.

### Returns

Returns *true* if the object was successfully added to the ACL, *false* if it already existed in the list.

## Example

This example makes every player able to use a command named "giveAccountAdminRights" that will add a specific accountname as an ACL object to the "Admin" group.

```
function giveAdminRights (playerSource, commandName, accountName) --add the function giveAdminRights and specify its arguments
	if accountName then --if there was an accountName entered then
		aclGroupAddObject (aclGetGroup("Admin"), "user."..accountName) --add an ACL object using the form "user.[accountName]" to the ACL group "Admin"
		outputChatBox ("Account '"..accountName.."' succesfully added to the admin group", playerSource) --output a notification to the player who entered the command that the acocunt was successfully added
	else --else output an error message and the correct syntax of the command to the player who entered it
		outputChatBox ("No account name specified.", playerSource)
		outputChatBox ("Correct syntax: /giveAccountAdminRights [accountName]", playerSource)
	end
end

addCommandHandler ("giveAccountAdminRights", giveAdminRights) --add a command "giveAccountAdminRights" and attch the function "giveAdminRights" to it
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

- aclGroupAddObject

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
