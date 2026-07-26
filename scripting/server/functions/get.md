---
doc_id: "mta-wiki:3256"
title: "Get"
source_title: "Get"
source_url: "https://wiki.multitheftauto.com/wiki/Get"
revision_id: 63949
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:06.067043+00:00"
---

# Get

This function gets a setting's value, or a group of settings' values, from the [settings registry](mta://reference/misc/settings-system.md).

| [[{{{image}}}\|link=\|]] | Note: Your settings cannot have a period (.) in them. This character is reserved. Read below for more details. |
| --- | --- |
|  |  |

## Syntax

```
var get ( string settingName )
```

## Optional Arguments

**settingName:** The name of the setting you want to get. See [setting names](mta://reference/misc/settings-system.md) for information on settings names.

### Returns

Returns the value of the setting if a single setting was specified and found, or a *table* (in associative-array form) containing:

- the list of global setting name/value pairs if "." is passed as a setting name,

- the list of resource settings if a resource name followed by a "." is passed,

- the list of the script's resource settings if an empty string is passed.

It returns *false* if the specified setting or settings group doesn't exist, or if the settings group you are trying to retrieve doesn't have any public or protected settings.

## Example

Example returns a value from the settings registry with the name "respawnTime".

```
function getMySetting()
    if get ( "respawnTime" ) then
        return get ( "respawnTime" )
    end
    return false
end
```

Or easier:

```
mySetting=get("respawnTime") or false
```

## See Also

- get

- [set](mta://scripting/server/functions/set.md)
