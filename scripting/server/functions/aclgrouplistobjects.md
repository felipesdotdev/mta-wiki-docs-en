---
doc_id: "mta-wiki:3416"
title: "AclGroupListObjects"
source_title: "AclGroupListObjects"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupListObjects"
revision_id: 78259
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:40.601059+00:00"
---

# AclGroupListObjects

This function returns a table over all the objects that exist in a given ACL group. These are objects like players and resources.

## Syntax

```
table aclGroupListObjects ( aclgroup theGroup )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):listObjects(...)*

**Variable**: *.objects*

### Required Arguments

- **theGroup:** The ACL group to get the objects from

### Returns

Returns a table of strings in the given ACL group. This table might be empty. Returns *false* or *nil* if theGroup is invalid or it fails for some other reason.

## Examples

This example outputs a list of Objects if the ACL Group is given

Click to collapse [-]
Example 1: Server

```
addCommandHandler("aclObjectList",function(player,command,aclGroup)
	if aclGroup == '' then
		outputChatBox("Please add the aclGroup you want the list of.", player)
		outputChatBox("Syntax: /aclObjectList aclGroup", player)
		return
	end
	local objects = aclGroupListObjects(aclGetGroup(aclGroup))
	for k,v in ipairs(objects) do
		outputChatBox("ACL LIST: "..aclGroup.." #"..k.." Object: "..v,player)
	end
end)
```

This example outputs through the command "getAdminAccounts" all accounts added to the "Admin" group.

Click to collapse [-]
Example 2: Server

```
function outputAdminGroupAccounts(player)
	local admins = {} -- creates the table in which will be added the accounts of "Admin" group
	local group = aclGetGroup("Admin")
	-- should return the "aclgroup" if the "Admin" group be found in ACL
	if not group then return end
	for _, object in ipairs(aclGroupListObjects(group) or {}) do
		local objType = gettok( object, 1, string.byte('.') )
		-- objType: gets the object type only, which can be either "user" or "resource"
		if objType == "user" then -- checks if it's a player account
			local _name = gettok( object, 2, string.byte('.') ) -- ignores "user." by separating that from the account name
			table.insert( admins, _name ) -- adds the account name to the "admins" table
		end
	end
    for i, name in ipairs(admins) do -- loop through the table "admins"
        outputChatBox(tostring(i).." : "..tostring(name), player, 140, 220, 140)
        -- output will look like this: "1 : John"
    end
end
addCommandHandler("getAdminAccounts", outputAdminGroupAccounts)
-- adds the command "getAdminAccounts" and attaches it to the function "outputAdminGroupAccounts"
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

- aclGroupListObjects

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
