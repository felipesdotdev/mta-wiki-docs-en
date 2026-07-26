---
doc_id: "mta-wiki:3451"
title: "HasObjectPermissionTo"
source_title: "HasObjectPermissionTo"
source_url: "https://wiki.multitheftauto.com/wiki/HasObjectPermissionTo"
revision_id: 82417
language: "en"
categories: ["Server_functions", "Changes_in_1.7.0", "Utility_templates"]
---

# HasObjectPermissionTo

This function returns whether or not the given object has access to perform the given action.

| [[{{{image}}}\|link=\|]] | Note: Only certain action names work. This function seems to return nil and output a bad argument error when checking if an object has rights for an action which doesn't start with function. , command. or resource. keywords. |
| --- | --- |
|  |  |

Scripts frequently wish to limit access to features to particular users. The naive way to do this would be to check if the player who is attempting to perform an action is in a particular group (usually the Admin group). The main issue with doing this is that the Admin group is not guaranteed to exist. It also doesn't give the server admin any flexibility. He might want to allow his 'moderators' access to the function you're limiting access to, or he may want it disabled entirely.

This is where using the ACL properly comes in, and luckily this is very easy. It all comes down to using this function. This, somewhat confusingly named function lets you check if an ACL object (a player or a resource) has a particular ACL right. In this case, we just care about players.

So, first of all, think of a name for your 'right'. Let's say we want a private area only certain people can go in, we'll call our right accessPrivateArea. Then, all you need to do is add one 'if' statement to your code:

```
if hasObjectPermissionTo ( player, "resource.YourResourceName.accessPrivateArea", false ) then
-- Whatever you want to happen if they're allowed in
else
-- Whatever you want to happen if they aren't
end
```

Notice that we've named the *right* using *resource.YourResourceName.accessPrivateArea* - this is just for neatness, so that the admin knows what resource the right belongs to. It's strongly advised you follow this convention. The *false* argument specifies the 'defaultPermission', false indicating that if the user hasn't had the right allowed or dissallowed (i.e. the admin hasn't added it to the config), that it should default to being not allowed.

The only downside of using this method is that the admin has to modify his config. The upsides are that the admin has much more control and your script will work for any server, however the admin has configured it.

## Syntax

ADDED/UPDATED IN VERSION 1.7.0 [r25445](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25445):

**defaultPermission** argument now defaults to **false**. If third argument is **nil**/**false** (or not specified), then action (unless explicitly allowed in **ACL**) won't be processed due to missing rights. May affect the normal operation of existing scripts.

```
bool hasObjectPermissionTo ( string / element theObject, string theAction [, bool defaultPermission = true/false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is also a static function underneath the ACL class.*

**Method**: *[ACL](https://wiki.multitheftauto.com/index.php?search=ACL).hasObjectPermissionTo(...)*

### Required Arguments

- **theObject:** The object to test if has permission to. This can be a client element (ie. a player), a resource or a string in the form "user.<name>" or "resource.<name>".

- **theAction:** The action to test if the given object has access to. Ie. "function.kickPlayer".

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **defaultPermission:** The default permission if none is specified in either of the groups the given object is a member of. If this is left to true, the given object will have permissions to perform the action unless the opposite is explicitly specified in the [ACL](https://wiki.multitheftauto.com/index.php?search=ACL). If false, the action will be denied by default unless explicitly approved by the [Access Control List](mta://tutorials/access-control-list.md).

### Returns

Returns *true* if the given object has permission to perform the given action, *false* otherwise. Returns *nil* if the function failed because of bad arguments.

## Example

This example kicks a player if the user using it has access to the kickPlayer function.

```
-- Kick command
function onKickCommandHandler ( playerSource, commandName, playerToKick, stringReason )
    -- Does the calling user have permission to kick the player? Default
    -- to false for safety reasons. We do this so any user can't use us to
    -- kick players.
    if ( hasObjectPermissionTo ( playerSource, "function.kickPlayer", false ) ) then

        -- Do we have permission to kick the player? We do this so we can fail
        -- nicely if this resource doesn't have access to call that function.
        if ( hasObjectPermissionTo ( resource, "function.kickPlayer", true ) ) then
            -- Kick him
            kickPlayer ( playerToKick, playerSource, stringReason )
        else
            -- Resource doesn't have any permissions, sorry
            outputChatBox ( "kick: The admin resource is not able to kick players. Please give this resource access to 'function.kickPlayer' in the ACL to use this function.", playerSource )
        end
    else
        -- User doesn't have any permissions
        outputChatBox ( "kick: You don't have permissions to use this command.", playerSource )
    end
end
addCommandHandler ( "kick", onKickCommandHandler )
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

- hasObjectPermissionTo

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)
