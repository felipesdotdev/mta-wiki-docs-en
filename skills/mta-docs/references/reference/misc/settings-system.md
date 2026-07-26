---
doc_id: "mta-wiki:3260"
title: "Settings system"
source_title: "Settings system"
source_url: "https://wiki.multitheftauto.com/wiki/Settings_system"
revision_id: 80574
language: "en"
categories: ["Scripting_Concepts"]
---

# Settings system

The settings system allows you to store and retrieve settings for future use, or provide server administrators with an easy way to configure your resource without modifying any files.

Settings can be modified in two ways - either by scripts or by the server administrator using the console.

## Setting names

Settings have a fairly simple naming system that allows you to specify the *scope* and *access* they provide.

Names are in the format:

[*access*][*resourceName*].*settingName*

Access modifiers:

- *****: *public* and can be read and written by any resource.

- **#**: *protected* and can be read by any resource but only written by the resource they belong to.

- **@**: *private* and can only be read and written to by the resource they belong to.

- None specified: *private* if it is a local setting, *public* if it's a global setting.

The *resourceName* is optional. If it isn't specified, then the setting is *global*.

The *settingName* can be anything you want.

## Examples

```
<meta>
    <settings>
        <setting name="@PrivateEntry" value="MyPrivateValue" myCustomKey="myCustomValue"/>
        <setting name="#ProtectedEntry" value="MyProtectedValue" myCustomKey="myCustomValue"/>
        <setting name="*PublicEntry" value="MyPublicValue" myCustomKey="myCustomValue"/>
    </settings>
</meta>
```

```
-- Get current resource name;
-- resource is a predefined global variable holding handle to current resource
local resName = getResourceName(resource)

-- You don't need to provide resource name before the entry name
-- HOWEVER resource name is NECESSARY in order to get other values than "value" entry
local privateEntry = get(resName..'.PrivateEntry')
local protectedEntry = get(resName..'ProtectedEntry')
local publicEntry = get(resName..'PublicEntry')

iprint(privateEntry)    -- MyPrivateValue
iprint(protectedEntry)  -- MyProtectedValue
iprint(publicEntry)     -- MyPublicValue

iprint(get(resName..'.PublicEntry.myCustomKey'))    -- myCustomValue
```

## Scripting functions

There are two scripting functions in the setting system: [set](mta://scripting/server/functions/set.md) and [get](mta://scripting/server/functions/get.md).

## Console functions

There are two console functions in the settings system:

- [get](mta://scripting/server/functions/get.md)

- [set](mta://scripting/server/functions/set.md)
