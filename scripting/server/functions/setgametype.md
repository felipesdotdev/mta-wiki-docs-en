---
doc_id: "mta-wiki:1815"
title: "SetGameType"
source_title: "SetGameType"
source_url: "https://wiki.multitheftauto.com/wiki/SetGameType"
revision_id: 82143
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:40.760106+00:00"
---

# SetGameType

This function sets a string containing a name for the game type. This should be the game-mode that is active, for example "Capture The Flag" or "Deathmatch". This is then displayed in the server browser and external server browsers.

**It should be noted that [mapmanager](mta://mapping/mapmanager.md) handles this automatically for gamemodes that utilise the map/gamemode system.**

## Syntax

```
bool setGameType ( string gameType )
```

 

Gamemode column that shows a server's game type.

### Required Arguments

- **gameType:** A string containing a name for the game mode, or *false* to clear it. **(MAX 200 characters)**

### Returns

Returns *true* if the game type was set, *false* if an invalid argument was passed to the function.

## Examples

This example sets the game type to *Capture The Flag*.

```
setGameType ( "Capture The Flag" )
```

This example adds a command to change the game type.

```
function setNewGameType( source, commandName, newGameType )
    local oldGameType = getGameType() -- check old Game Type
    setGameType( newGameType ) -- set new Game Type
    outputChatBox( "Game Type " .. oldGameType .. " changed to " .. newGameType .. ".", getRootElement(), 255, 128, 0 )
end
addCommandHandler( "setgametype", setNewGameType )
```

## See Also

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- setGameType

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)
