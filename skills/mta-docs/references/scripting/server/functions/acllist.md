---
doc_id: "mta-wiki:3340"
title: "AclList"
source_title: "AclList"
source_url: "https://wiki.multitheftauto.com/wiki/AclList"
revision_id: 68738
language: "en"
categories: ["Server_functions"]
---

# AclList

This function returns a list of all the ACLs.

## Syntax

```
table aclList ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the ACL class.*

**Method**: *[ACL](https://wiki.multitheftauto.com/index.php?search=ACL).list(...)*

### Returns

Returns a table of all the ACLs. This table can be empty if no ACLs exist. It can also return *false*/*nil* if it failed for some reason.

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

- aclList

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclReload](mta://scripting/server/functions/aclreload.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
