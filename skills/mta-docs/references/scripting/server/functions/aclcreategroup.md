---
doc_id: "mta-wiki:3345"
title: "AclCreateGroup"
source_title: "AclCreateGroup"
source_url: "https://wiki.multitheftauto.com/wiki/AclCreateGroup"
revision_id: 69149
language: "en"
categories: ["Server_functions"]
---

# AclCreateGroup

This function creates a group in the ACL. An ACL group can contain objects like players and resources. They specify who has access to the ACL's in this group.

## Syntax

```
aclgroup aclCreateGroup ( string groupName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ACLGroup](mta://reference/misc/aclgroup.md)(...)*

### Required Arguments

- **groupName:** The name of the group to create

### Returns

Returns the pointer to the created aclgroup if successful. Returns false if failed.

## Example

This example adds a command *addobjecttogroup* with which you can easily add new objects to specified access control list groups.

```
function addACLGroupObject ( thePlayer, commandName, groupName, objectName )
    local ourGroup = aclGetGroup ( groupName )
    -- if there is no previous group with this name, we need to create one
    if not ourGroup then
        ourGroup = aclCreateGroup ( groupName )
    end

    -- if object name wasn't given
    if not objectName then
        -- print out message to chatbox
        return outputChatBox ( "You need to specify the object!", thePlayer )
    end

    -- and finally let's add the object to it's group
    aclGroupAddObject ( ourGroup, objectName )
    -- don't forget to save the ACL after it has been modified
    aclSave ()
end
addCommandHandler ( "addobjecttogroup", addACLGroupObject )
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- aclCreateGroup

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

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
