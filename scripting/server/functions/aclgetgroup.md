---
doc_id: "mta-wiki:3347"
title: "AclGetGroup"
source_title: "AclGetGroup"
source_url: "https://wiki.multitheftauto.com/wiki/AclGetGroup"
revision_id: 69161
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.724999+00:00"
---

# AclGetGroup

This function is used to get the ACL group with the given name. If you need most of the groups you should consider using [aclGroupList](mta://scripting/server/functions/aclgrouplist.md) instead to get a table containing them all.

## Syntax

```
aclgroup aclGetGroup ( string groupName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the ACL Group class.*

**Method**: *[ACLGroup](mta://reference/misc/aclgroup.md).get(...)*

### Required Arguments

- **groupName:** The name to get the ACL group from

### Returns

Returns the ACL group if it could be found. Returns false/nil if it did not exist or failed for some reason.

## Example

**Example 1:** This example makes every player able to use a command named "giveAccountAdminRights" that will add a specific accountname as an ACL object to the "Admin" group.

```
function giveAdminRights (playerSource, commandName, accountName) --add the function giveAdminRights and specify its arguments
	if accountName then --if there was an accountName entered then
		aclGroupAddObject (aclGetGroup("Admin"), "user."..accountName)) --add an ACL object using the form "user.[accountName]" to the ACL group "Admin"
		outputChatBox ("Account '"..accountName.."' succesfully added to the admin group", playerSource) --output a notification to the player who entered the command that the acocunt was successfully added
	else --else output an error message and the correct syntax of the command to the player who entered it
		outputChatBox ("No account name specified.", playerSource)
		outputChatBox ("Correct syntax: /giveAccountAdminRights [accountName]", playerSource)
	end
end

addCommandHandler ("giveAccountAdminRights", giveAdminRights) --add a command "giveAccountAdminRights" and attch the function "giveAdminRights" to it
```

**Example 2:** This example displays a list of all the online admins in the chat box (assuming your administrator's group in your ACL is called 'admin'):

```
players = getElementsByType ( "player" )
admins = ""
for k,v in ipairs(players) do
   local accountname = ""
   if (isGuestAccount(getPlayerAccount(v)) == false) then
      accountname = getAccountName (getPlayerAccount(v))
      if isObjectInACLGroup ( "user." .. accountname, aclGetGroup ( "admin" ) ) then
         if (admins == "") then
            admins = getPlayerName(v)
         else
            admins = admins .. ", " .. getPlayerName(v)
         end
      end
   end
end
outputChatBox( "Online Admins:", getRootElement(), 255, 255, 0)
outputChatBox( " " .. tostring ( admins ), getRootElement(), 255, 255, 0)
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclDestroyGroup](mta://scripting/server/functions/acldestroygroup.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- aclGetGroup

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
