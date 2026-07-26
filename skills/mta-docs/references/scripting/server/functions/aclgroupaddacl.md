---
doc_id: "mta-wiki:3350"
title: "AclGroupAddACL"
source_title: "AclGroupAddACL"
source_url: "https://wiki.multitheftauto.com/wiki/AclGroupAddACL"
revision_id: 69170
language: "en"
categories: ["Server_functions"]
---

# AclGroupAddACL

This function adds the given ACL to the given ACL group. This makes the resources and players in the given ACL group have access to what's specified in the given ACL. The rights for something in the different ACL's in a group are OR-ed together, which means if one ACL gives access to something, this ACL group will have access to that.

## Syntax

```
bool aclGroupAddACL ( aclgroup theGroup, acl theACL )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[aclgroup](mta://reference/misc/aclgroup.md):addACL(...)*

### Required Arguments

- **theGroup:** The group to add the ACL to

- **theACL:** The ACL to add to the group

### Returns

Returns *true* if the ACL could be successfully added to the ACL group, *false*/*nil* if either of the elements are invalid, the ACL is already in that group or if something else goes wrong.

## Example

This example adds a command *addAclGroup* with which you can easily add new access control lists to specified acl Groups.

```
function addAclGroup ( thePlayer, commandName, aclName )
if(aclName) then
    acl = aclCreate ( aclName )
else
    acl = aclCreate("myName")
end
aclGroup = aclGetGroup("Admin")
aclGroupAddACL(aclGroup,acl) -- now all Admins have the rights of acl, too
aclSave () 
addCommandHandler ( "addAclGroup", addAclGroup)
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

- aclGroupAddACL

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
