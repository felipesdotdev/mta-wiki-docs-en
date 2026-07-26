---
doc_id: "mta-wiki:3343"
title: "AclSetRight"
source_title: "AclSetRight"
source_url: "https://wiki.multitheftauto.com/wiki/AclSetRight"
revision_id: 76238
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.647266+00:00"
---

# AclSetRight

This functions changes or adds the given right in the given ACL. The access can be *true* or *false* and specifies whether the ACL gives access to the right or not.

## Syntax

```
bool aclSetRight ( acl theAcl, string rightName, bool hasAccess )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):setRight(...)*

**Counterpart**: *[aclGetRight](mta://scripting/server/functions/aclgetright.md)*

### Required Arguments

- **theAcl:** The ACL to change the right of

- **rightName:** The right to add/change the access property of. It **must** be prefixed with "**function.**" or "**command.**" or "**general.**" or "**resource.**"

- **hasAccess:** Whether the access should be set to true or false

### Returns

Returns *true* if the access was successfully changed, *false* or *nil* if it failed for some reason, ie. invalid ACL or the rightname is invalid.

## Example

This example adds a command *setaclright* with which you can easily add new rights to specified access control lists.

```
function setACLRight ( thePlayer, commandName, aclName, rightName, access )
    local ourACL = aclGet ( aclName )
    -- if there is no previous ACL with this name, we need to create one
    if not ourACL then
        ourACL = aclCreate ( aclName )
    end

    -- turn the boolean string to lower case
    access = string.lower ( access )
    -- access has to be either true or false (booleans)
    if not (access == "true" or access == "false") then
        -- print out error message to debug window
        return outputDebugString ( "Invalid access; true and false are only accepted", 1 )
    end

    -- change the access to boolean
    if access == "true" then
        access = true
    else 
        access = false
    end

    -- and finally let's set the right
    aclSetRight ( ourACL, rightName, access )
    -- don't forget to save the ACL after it has been modified
    aclSave ()
end
addCommandHandler ( "setaclright", setACLRight )
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

- aclSetRight

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
