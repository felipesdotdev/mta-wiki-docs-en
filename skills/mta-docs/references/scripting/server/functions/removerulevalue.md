---
doc_id: "mta-wiki:2725"
title: "RemoveRuleValue"
source_title: "RemoveRuleValue"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveRuleValue"
revision_id: 80627
language: "en"
categories: ["Server_functions"]
---

# RemoveRuleValue

This function removes a set rule value that can be viewed by server browsers.

## Syntax

```
bool removeRuleValue ( string key )
```

### Required Arguments

- **key:** The name of the rule you wish to remove

### Returns

Returns *true* if the rule value was removed, *false* if it failed.

## Example

This example shows how you could **unset/remove a rule** that shows that your script is running on the server.

```
removeRuleValue ( "myScriptRunning" )
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- removeRuleValue

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
