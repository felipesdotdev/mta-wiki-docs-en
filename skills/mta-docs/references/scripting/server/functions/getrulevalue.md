---
doc_id: "mta-wiki:1816"
title: "GetRuleValue"
source_title: "GetRuleValue"
source_url: "https://wiki.multitheftauto.com/wiki/GetRuleValue"
revision_id: 51095
language: "en"
categories: ["Server_functions"]
---

# GetRuleValue

This function gets a rule value. A rule value is a string that can be viewed by server browsers and used for filtering the server list.

## Syntax

```
string getRuleValue ( string key )
```

### Required Arguments

- **key:** The name of the rule

### Returns

Returns a string containing the value set for the specified *key*, *false* if invalid arguments were specified.

## Example

This example shows how you can check if a rule is set.

```
if getRuleValue ( "myScriptRunning" ) then
    -- the value is set
end
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- getRuleValue

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
