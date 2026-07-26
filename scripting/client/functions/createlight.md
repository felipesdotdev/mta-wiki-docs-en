---
doc_id: "mta-wiki:8233"
title: "CreateLight"
source_title: "CreateLight"
source_url: "https://wiki.multitheftauto.com/wiki/CreateLight"
revision_id: 79919
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0", "Utility_templates"]
generated_at: "2026-07-26T16:12:06.727084+00:00"
---

# CreateLight

This function creates a 3D [light](mta://reference/misc/element-light.md) in the world.

| [[{{{image}}}\|link=\|]] | Note: The direction of the light only has any effect if the light type is spot light . One light will only apply illumination effects to peds , players , wheels and number plates (like a emergency vehicle siren light does). Two or more lights will apply illumination effects to everything (excluding objects) that is in range of, at least, two of them. |
| --- | --- |
|  |  |

## Syntax

```
light createLight ( int lightType, float posX, float posY, float posZ [, float radius = 3, int r = 255, int g = 0, int b = 0, float dirX = 0, float dirY = 0, float dirZ = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Light](mta://reference/misc/light.md)(...)*

### Required Arguments

- **lightType:** An integer representing the type of light to create.

- **0**: Point light, which illuminates surroundings evenly across the light radius.

- **1**: Spot light, which illuminates the direction of the light defined by *dirX*, *dirY* and *dirZ*.

- **2**: Dark light, which darkens its surrounding elements to full black.

- **posX:** A floating point number representing the X coordinate on the map.

- **posY:** A floating point number representing the Y coordinate on the map.

- **posZ:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **radius:** A floating point number representing the radius of the light.

- **r:** An integer number representing the amount of red to use in the colouring of the light (0 - 255).

- **g:** An integer number representing the amount of green to use in the colouring of the light (0 - 255).

- **b:** An integer number representing the amount of blue to use in the colouring of the light (0 - 255).

- **dirX:** A floating point number representing the light direction's X coordinate on the map.

- **dirY:** A floating point number representing the light direction's Y coordinate on the map.

- **dirZ:** A floating point number representing the light direction's Z coordinate on the map.

### Returns

Returns the [light](mta://reference/misc/element-light.md) element if creation was successful, *false* otherwise.

## Example

This example will make every player to look completely black without using shaders. It will also dark vehicles he uses too.

```
local lightRadius = 2 * getElementRadius(localPlayer) -- Every standard player model has the same radius, so save it for quicker access
local lights = { [localPlayer] = createLight(2, 0, 0, 0, lightRadius) } -- Initialize our light table with the one that the local player will use for the effect

local function addPlayerDarkLight()
    -- Create a new dark light for that player
    lights[source] = createLight(2, 0, 0, 0, lightRadius)
end
addEventHandler("onClientPlayerJoin", root, addPlayerDarkLight)

local function removePlayerDarkLight()
    -- Destroy the light of that player and remove references
    destroyElement(lights[source])
    lights[source] = nil
end
addEventHandler("onClientPlayerQuit", root, removePlayerDarkLight)

-- Make the dark light assigned to each player to move with his center, so we achieve the desired effect
local function updateLightPositions()
    for player, light in pairs(lights) do
        if isElementStreamedIn(player) then
           setElementPosition(light, getPedBonePosition(player, 2))
        end
    end
end
addEventHandler("onClientPreRender", root, updateLightPositions)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.0-3.0152 | Addendum to r7048 (Applied source patch #8737 (PointLight Creation) by Lex128.) |
| --- | --- |

## See Also

- createLight

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)
