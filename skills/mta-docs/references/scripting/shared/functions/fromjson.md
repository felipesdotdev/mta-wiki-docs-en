---
doc_id: "mta-wiki:3453"
title: "FromJSON"
source_title: "FromJSON"
source_url: "https://wiki.multitheftauto.com/wiki/FromJSON"
revision_id: 82829
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FromJSON

This function parses a [JSON](mta://reference/misc/json.md) formatted string and unpacks the values into Lua variables. You can use [toJSON](mta://scripting/shared/functions/tojson.md) to encode variables into a JSON string that can be read by this function.

| [[{{{image}}}\|link=\|]] | Important Note: When parsing a JSON array, fromJSON unpacks the elements as multiple separate values. To mimic standard JSON parsing behavior and store these elements together in a single Lua table, you must wrap the function call in a table constructor {}. If your JSON string was generated directly by toJSON , you do not need to wrap it. local jsonString = '["Apple", "Orange"]' local fruitsTable = { fromJSON(jsonString) } |
| --- | --- |
|  |  |

## Syntax

```
var... fromJSON ( string json )
```

### Required Arguments

- **json:** A JSON formatted string.

### Returns

Returns the parsed JSON data as multiple values or a single table depending on the input JSON structure:

- Returns **multiple separate values** (unpacked) if the root element of the JSON is an **array**

- Returns a **table** if the root element of the JSON is an **object**

- Returns [nil](mta://reference/misc/nil.md) if the JSON string is invalid or malformed.

## Examples

### Example 1: Assigning to multiple variables

This example shows how fromJSON extracts values from a JSON array directly into separate Lua variables.

```
local jsonArray = '["Desert Eagle", 24]'

local name, ammo = fromJSON(jsonArray)

print(name, ammo) --> Output: Desert Eagle  24
```

### Example 2: Wrapping the call inside a table

This example shows how to capture all values of a JSON array in a single Lua table.

```
local jsonArray = '["Apple", "Orange", "Banana"]'

-- Put the fromJSON call inside of a table directly to capture all the values of the JSON array
local fruits = {fromJSON(jsonArray)}

if fruits[1] then -- Make sure the JSON was parsed correctly
    for i=1, #fruits do
        print(fruits[i])
    end
    --[[ Output:
    Apple
    Orange
    Banana
    ]]
end
```

### Example 3: Parsing a JSON object

```
local jsonObject = '{"playerName": "Alex", "score": 2500}'

local playerStats = fromJSON(jsonObject)

if playerStats then
    print(playerStats.playerName) --> Output: Alex
    print(playerStats.score)      --> Output: 2500
end
```

### Example 4: Parsing a nested JSON object

```
local jsonString = '{"vehicle": "Infernus", "upgrades": {"nos": true, "paintjob": 2}}'

local vehicleInfo = fromJSON(jsonString)

if vehicleInfo then
    print(vehicleInfo.vehicle)           --> Output: Infernus
    print(vehicleInfo.upgrades.nos)      --> Output: true
    print(vehicleInfo.upgrades.paintjob) --> Output: 2
end
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
