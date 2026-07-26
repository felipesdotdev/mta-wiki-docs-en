---
doc_id: "mta-wiki:2616"
title: "SetMapName"
source_title: "SetMapName"
source_url: "https://wiki.multitheftauto.com/wiki/SetMapName"
revision_id: 80629
language: "en"
categories: ["Server_functions"]
---

# SetMapName

This function is used to set a map name that will be visible in the server browser. In practice you should generally rely on the mapmanager to do this for you.

## Syntax

```
bool setMapName ( string mapName )
```

### Required Arguments

- **mapName:** The name you wish the server browser to show. **(MAX 200 characters)**

### Returns

Returns *true* if map name was set successfully, *false* otherwise.

## Example

This example sets the map name to *My amazing map!*.

```
setMapName("My amazing map!")
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- setMapName

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
