---
doc_id: "mta-wiki:3452"
title: "ToJSON"
source_title: "ToJSON"
source_url: "https://wiki.multitheftauto.com/wiki/ToJSON"
revision_id: 81015
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Changes_in_1.5", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:16:58.404346+00:00"
---

# ToJSON

This function converts a **single** value (preferably a Lua table) into a [JSON](mta://reference/misc/json.md) encoded string. You can use this to store the data and then load it again using [fromJSON](mta://scripting/shared/functions/fromjson.md).

| [[{{{image}}}\|link=\|]] | Important Note: Due to technical limitations (partly of json-c) the stringified keys will be truncated to the first 255 characters |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: When using toJSON for submitting data using fetchRemote for example, make sure to use string.sub(data, 2, -2) to remove the brackets as many APIs will not understand the request |
| --- | --- |
|  |  |

## Syntax

```
string toJSON ( var value [, bool compact = false ][, string prettyType = "none" ] )
```

### Required Arguments

- **var:** An argument of any type. Arguments that are elements will be stored as element IDs that are liable to change between sessions. As such, do not save elements across sessions as you will get unpredictable results.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **compact:** a [boolean](mta://reference/misc/boolean.md) representing whether the string will contain whitespaces. To remove whitespaces from JSON string, use *true*. String will contain whitespaces per default.

- **prettyType:** a type [string](mta://reference/misc/string.md) from below:

- none

- spaces

- tabs

### Returns

Returns a JSON formatted string.

## Example

This example shows how you can encode an array. The string json should equal *"[ { "1": "dogs", "mouse": "food", "cat": "hungry", "birds": 4 } ]" after executed.*

```
local json = toJSON ( { "dogs", cat = "hungry", mouse = "food", birds = 4 } )
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
