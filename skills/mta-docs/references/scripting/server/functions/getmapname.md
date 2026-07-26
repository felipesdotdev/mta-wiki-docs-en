---
doc_id: "mta-wiki:3447"
title: "GetMapName"
source_title: "GetMapName"
source_url: "https://wiki.multitheftauto.com/wiki/GetMapName"
revision_id: 18298
language: "en"
categories: ["Server_functions"]
---

# GetMapName

This function retrieves the current mapname as set by [setMapName](mta://scripting/server/functions/setmapname.md).

## Syntax

```
string getMapName ()
```

### Returns

Returns the mapname as a string. If no mapname is set it returns *nil*.

## Example

This example adds a *checkmap* command with which you can check what map you are currently playing.

```
function checkMap ( thePlayer )
    local mapName = getMapName() -- get the maps name
	if mapName and mapName ~= "None" then -- if map name was set and it isn't "None" (default map name)
        outputChatBox( "You're playing map called \"" .. mapName .. "\"", thePlayer ) -- print out the map name
    else -- there was no name so tell that to player
        outputChatBox( "You're playing an unnamed map.", thePlayer ) -- print out the message
    end
end
addCommandHandler ( "checkmap", checkMap )
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- getMapName

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
