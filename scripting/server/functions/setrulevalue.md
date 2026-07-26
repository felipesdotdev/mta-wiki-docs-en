---
doc_id: "mta-wiki:1817"
title: "SetRuleValue"
source_title: "SetRuleValue"
source_url: "https://wiki.multitheftauto.com/wiki/SetRuleValue"
revision_id: 80626
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:44.468875+00:00"
---

# SetRuleValue

This function sets a rule value that can be viewed by server browsers.

## Syntax

```
bool setRuleValue ( string key, string value )
```

### Required Arguments

- **key:** The name of the rule **(MAX 200 characters)**

- **value:** The value you wish to set for the rule **(MAX 200 characters)**

### Returns

Returns *true* if the rule value was set, *false* if invalid arguments were specified.

## Example

This example shows how you could set a rule that shows that your script is running on the server.

```
setRuleValue ( "myScriptRunning", "yes" )
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- setRuleValue
