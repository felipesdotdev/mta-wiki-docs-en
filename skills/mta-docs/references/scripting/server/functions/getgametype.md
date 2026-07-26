---
doc_id: "mta-wiki:3446"
title: "GetGameType"
source_title: "GetGameType"
source_url: "https://wiki.multitheftauto.com/wiki/GetGameType"
revision_id: 18297
language: "en"
categories: ["Server_functions"]
---

# GetGameType

This function retrieves the current gametype as set by [setGameType](mta://scripting/server/functions/setgametype.md). The game type is displayed in the server browser next to the server's name.

## Syntax

```
string getGameType ()
```

### Returns

Returns the gametype as a string. If no gametype is set it returns *nil*.

## Example

This example sends a message to player when he joins, if the current game type is Race.

```
function playerJoinHandler( )
   if getGameType() == "Race" then
      outputChatBox( "Ready... Get set... GO!!", source )
   end
end
addEventHandler( "onPlayerJoin", getRootElement(), playerJoinHandler )
```

## See Also

- getGameType

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
