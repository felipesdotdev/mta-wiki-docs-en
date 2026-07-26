---
doc_id: "mta-wiki:4297"
title: "CreateFire"
source_title: "CreateFire"
source_url: "https://wiki.multitheftauto.com/wiki/CreateFire"
revision_id: 72021
language: "en"
categories: ["Client_functions"]
---

# CreateFire

Fire with default size (1.8)

Creates a patch of fire that will spread a bit and die out after a while. Because it's a client side only function, other players won't see it, so custom events or custom objects will be needed to make a fire visible to some players.

## Syntax

```
bool createFire ( float x, float y, float z [, float size = 1.8 ] )
```

### Required Arguments

- **x, y, z:** the coordinates when the initial patch of fire will be created.

### Optional Arguments

- **size:** a float value indicating the size of the initial patch of fire, this value also affects the duration of how long the fire remains.

### Returns

Returns *true* if successful, *false* if bad arguments were passed or the limit of active fires was reached. There can be a maximum of 60 active fires.

## Example

This example adds a /fire command, which creates a patch of fire in the position of the player that types it.

```
local function burn(commandName, theSize)
   if tonumber(theSize) then
        local x, y, z = getElementPosition(getLocalPlayer())
        createFire(x, y, z, tonumber(theSize))
        outputChatBox("Burn, buuuuurn >:]")
   else
        outputChatBox("Syntax: /fire <size>")
   end
end
addCommandHandler("fire", burn)
```

## See Also

- createFire

- [extinguishFire](mta://scripting/client/functions/extinguishfire.md)
