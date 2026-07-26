---
doc_id: "mta-wiki:3255"
title: "Set"
source_title: "Set"
source_url: "https://wiki.multitheftauto.com/wiki/Set"
revision_id: 67543
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:37.781220+00:00"
---

# Set

This function is used to save arbitrary data under a certain name on the [settings registry](mta://reference/misc/settings-system.md).

It's important to note that set *always* writes to the settings.xml file, even if [get](mta://scripting/server/functions/get.md) read the value from a resource's meta.xml. This means that the admin can specify settings in the settings.xml that override the resource's defaults, but that the defaults can still be retrieved if need be. As a general principle, resources should not be designed so that the admin is required to modify them, they should be 'black boxes'.

## Syntax

```
bool set ( string settingName, var value )
```

### Required Arguments

- **settingName:** The name of the setting you want to set. See [setting names](mta://reference/misc/settings-system.md) for information on settings names.

- **value:** The value to set the setting to. This can be any Lua data type, except for functions, most userdata (only [resources](mta://reference/misc/resource.md) can't be stored) and threads.

### Returns

Returns *true* if the setting has been set, *false* if you do not have access to the setting or invalid arguments were passed.

## Example

This example sets a specified setting with a Value. This is a *local* setting belonging to the resource that the code is run in.

```
function setAclRights(playerElement, commandName, acl, value, type)
   if not acl or not value then
      return outputChatBox("Syntax: /setacl <acl> <value>")
   end
   if set ( acl, value ) then
      outputChatBox("Acl "..acl.." value set to "..value)
      print(getPlayerName(playerElement).." has changed "..acl.." to "..value)
   else
      outputChatBox("Error happened while changing the Acl "..acl.." value to "..value)
      print(getPlayerName(playerElement).." tried to change "..acl.." to "..value)
   end
end
addCommandHandler("setacl", setAclRights)
```

## See Also

- [get](mta://scripting/server/functions/get.md)

- set
