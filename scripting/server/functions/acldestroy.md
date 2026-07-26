---
doc_id: "mta-wiki:3338"
title: "AclDestroy"
source_title: "AclDestroy"
source_url: "https://wiki.multitheftauto.com/wiki/AclDestroy"
revision_id: 69152
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.543570+00:00"
---

# AclDestroy

This function destroys the ACL passed. The destroyed ACL will no longer be valid.

## Syntax

```
bool aclDestroy ( acl theACL )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):destroy(...)*

### Required Arguments

- **theACL:** The ACL to destroy

### Returns

Returns *true* if successfully destroyed and *false* if it could not be deleted (ie. it's not valid).

## Example

This example shows you a command to delete an ACL:

```
function deleteSomeACL ( thePlayer, cmdname, theACL )
    if aclGet ( theACL ) then --Check if the specified ACL exists
        --If it does
        local deleted = aclDestroy ( theACL ) --Try to delete the ACL
        if deleted then --If the ACL has been deleted
            --We will give the player a succes-message
            outputChatBox ( "ACL " ..theACL.. " Succesfully removed!", thePlayer )
        else --If there was something wrong while deleting
            --We send the player an error message
            outputChatBox ( "Error while removing ACL " ..theACL.. "!", thePlayer )
        end
    else --If the ACL doesn't exists
        outputChatBox ( "Error: Invalid ACL Name specified, or the ACL doesn't exist.", thePlayer )
    end
end
addCommandHandler ( "deleteACL", deleteSomeACL ) --Add the commandhandler
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- aclDestroy

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
