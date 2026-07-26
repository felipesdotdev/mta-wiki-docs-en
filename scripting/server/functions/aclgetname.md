---
doc_id: "mta-wiki:3341"
title: "AclGetName"
source_title: "AclGetName"
source_url: "https://wiki.multitheftauto.com/wiki/AclGetName"
revision_id: 69164
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:38.603242+00:00"
---

# AclGetName

Get the name of given ACL.

## Syntax

```
string aclGetName ( acl theAcl )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[acl](mta://reference/misc/acl.md):getName(...)*

**Variable**: *.name*

### Required Arguments

- **theACL:** The ACL to get the name of

### Returns

Returns the name of the given ACL as a string if successful. Returns *false*/*nil* if unsuccessful, ie the ACL is invalid.

## Example

This example adds a command *listacls* which prints out a name list of all ACLs to the console.

```
function printOutAllACLs ( thePlayer )
    -- get a table over all the ACLs
    local allACLs = aclList()
    -- if the table is empty (there are no ACLs)
    if #allACLs == 0 then
        -- print out a message to console and exit function
        return outputConsole ( "There are no ACLs!", thePlayer )
    else
        -- print out a list of the names
        outputConsole ( "List of all ACLs:", thePlayer )
        for key, singleACL in ipairs ( allACLs ) do
            local ACLName = aclGetName ( singleACL )
            outputConsole ( "- " .. tostring ( ACLName ), thePlayer )
        end
   end
end
addCommandHandler ( "listacls", printOutAllACLs )
```

## See Also

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclDestroyGroup](mta://scripting/server/functions/acldestroygroup.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- [aclGetGroup](mta://scripting/server/functions/aclgetgroup.md)

- aclGetName

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
