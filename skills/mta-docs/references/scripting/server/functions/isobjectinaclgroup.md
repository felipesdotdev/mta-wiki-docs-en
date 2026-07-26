---
doc_id: "mta-wiki:4448"
title: "IsObjectInACLGroup"
source_title: "IsObjectInACLGroup"
source_url: "https://wiki.multitheftauto.com/wiki/IsObjectInACLGroup"
revision_id: 79323
language: "en"
categories: ["Server_functions", "Changes_in_1.4.0"]
---

# IsObjectInACLGroup

| [[{{{image}}}\|link=\|]] | Important Note: You must NOT to use this function to limit features to users that belong to specific groups. Instead you MUST use hasObjectPermissionTo . Using this function forces the server owner to name their group a certain way, whereas using hasObjectPermissionTo allows the owner to give permission for whatever features you restrict to whatever groups they have set up in their ACL. |
| --- | --- |
|  |  |

This function is used to determine if an object is in a group.

## Syntax

```
bool isObjectInACLGroup ( string theObjectName, aclgroup theGroup )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](https://wiki.multitheftauto.com/index.php?search=aclgroup):doesContainObject(...)*

### Required Arguments

- **theObjectName:** the name of the object to check. Examples: "resource.ctf", "user.Jim".

- **theGroup:** the [ACL group](mta://reference/misc/aclgroup.md) pointer of the group from which the object should be found.

### Returns

Returns *true* if the object is in the specified group, *false* otherwise.

## Example

**Example 1:** This example adds a *jetpack* command that is only available to admins.  When entering the command, it will toggle the player's jetpack.

```
addCommandHandler ( "jetpack", function ( thePlayer )
    if doesPedHaveJetPack ( thePlayer ) then -- If the player have a jetpack already, remove it
        removePedJetPack ( thePlayer ) -- Remove the jetpack
        return -- And stop the function here
    end

    -- Otherwise, give him one if he has access

    local accName = getAccountName ( getPlayerAccount ( thePlayer ) ) -- get his account name
    if isObjectInACLGroup ("user."..accName, aclGetGroup ( "Admin" ) ) then -- Does he have access to Admin functions?
        if not doesPedHaveJetPack ( thePlayer ) then -- If the player doesn't have a jetpack give it.
            givePedJetPack ( thePlayer )  -- Give the jetpack
        end
    end
end)
```

**Example 2:** This example displays a list of all the online admins in the chat box (assuming your administrator's group in your ACL is called 'Admin'):

```
local admins = ""
local players = getElementsByType("player")
for k, v in ipairs(players) do
   if not isGuestAccount(getPlayerAccount(v)) then
      local accountName = getAccountName(getPlayerAccount(v))
      if isObjectInACLGroup("user." .. accountName, aclGetGroup("Admin")) then
         if admins == "" then
            admins = getPlayerName(v)
         else
            admins = admins .. ", " .. getPlayerName(v)
         end
      end
   end
end
outputChatBox("Online Admins:", getRootElement(), 255, 255, 0)
outputChatBox(" " .. admins, getRootElement(), 255, 255, 0)
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

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- isObjectInACLGroup
