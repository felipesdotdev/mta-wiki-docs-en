---
doc_id: "mta-wiki:3339"
title: "AclGet"
source_title: "AclGet"
source_url: "https://wiki.multitheftauto.com/wiki/AclGet"
revision_id: 69158
language: "en"
categories: ["Server_functions"]
---

# AclGet

Get the ACL with the given name. If need to get most of the ACL's, you should consider using [aclList](mta://scripting/server/functions/acllist.md) to get a table of them all.

## Syntax

```
acl aclGet ( string aclName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the ACL class.*

**Method**: *[ACL](https://wiki.multitheftauto.com/index.php?search=ACL).get(...)*

### Required Arguments

- **aclName:** The name to get the ACL belonging to

### Returns

Returns the ACL with that name if it could be retrieved, *false*/*nil* if the ACL does not exist or it fails for some other reason.

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

- aclGet

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
