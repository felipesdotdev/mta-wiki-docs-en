---
doc_id: "mta-wiki:7704"
title: "Acl"
source_title: "Acl"
source_url: "https://wiki.multitheftauto.com/wiki/Acl"
revision_id: 61526
language: "en"
categories: ["Scripting_Concepts"]
---

# Acl

**ACL** or **Access Control List** is a set of rights grouped together to create a list, they are defined in the [ACL.xml](mta://tutorials/access-control-list.md) file as <acl> nodes. These ACLs can then be added to certain [ACL Groups](mta://reference/misc/aclgroup.md) to grant or deny these groups specified permissions or acces to server scripting functions defined in the ACL.
Example of an ACL:

```
<acl name="Example">
        <right name="general.ModifyOtherObjects" access="true" />
        <right name="function.startResource" access="true" />
        <right name="function.stopResource" access="true" />
        <right name="function.shutdown" access="false" />
        <right name="command.shutdown" access="false" />
</acl>
```

This creates ACL called *Example* and gives resources access to start/stop resources and modify other resources but denies access to shutting down the server. Players that are in group using this ACL will be denied access to *shutdown* command.

## Related scripting functions

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- [aclGetName](mta://scripting/server/functions/aclgetname.md)

- [aclGetRight](mta://scripting/server/functions/aclgetright.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [aclList](mta://scripting/server/functions/acllist.md)

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)
