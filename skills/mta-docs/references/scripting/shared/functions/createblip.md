---
doc_id: "mta-wiki:1450"
title: "CreateBlip"
source_title: "CreateBlip"
source_url: "https://wiki.multitheftauto.com/wiki/CreateBlip"
revision_id: 76951
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Changes_in_1.0"]
---

# CreateBlip

This function creates a [blip](https://wiki.multitheftauto.com/index.php?search=blip) [element](mta://reference/misc/element.md), which is displayed as an icon on the client's radar.

## Syntax

Click to collapse [-]
Server

```
blip createBlip ( float x, float y, float z [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0, element visibleTo = getRootElement( ) ] )
```

Click to collapse [-]
Client

```
blip createBlip ( float x, float y, float z [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0 ] )
```

 

example

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Blip](https://wiki.multitheftauto.com/index.php?search=Blip)(...)*

### Required Arguments

- **x:** The x position of the blip, in world coordinates.

- **y:** The y position of the blip, in world coordinates.

- **z:** The z position of the blip, in world coordinates.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **icon:** The icon that the radar blips should be. Default is 0. Valid values can be seen at [Radar Blips](mta://reference/misc/radar-blips.md)

- **size:** The size of the radar blip. Only applicable to the *Marker* icon. Default is 2. Maximum is 25.

- **r:** The amount of red in the blip's color (0–255). Only applicable to the *Marker* icon. Default is 255.

- **g:** The amount of green in the blip's color (0–255). Only applicable to the *Marker* icon. Default is 0.

- **b:** The amount of blue in the blip's color (0–255). Only applicable to the *Marker* icon. Default is 0.

- **a:** The amount of alpha in the blip's color (0–255). Only applicable to the *Marker* icon. Default is 255.

- **ordering:** This defines the blip's Z-level ordering (-32768–32767). Default is 0.

- **visibleDistance:** The maximum distance from the camera at which the blip is still visible (0–65535).

Click to collapse [-]
Server

- **visibleTo:** This defines which elements can see the blip. Defaults to visible to everyone. See [visibility](mta://reference/misc/visibility.md).

## Returns

Returns an [element](mta://reference/misc/element.md) of the [blip](https://wiki.multitheftauto.com/index.php?search=blip) if it was created successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

**Example 1:** This example creates a radar blip at a random player's position and makes it so that it is only visible to that player.

```
-- Pick a random player
local myPlayer = getRandomPlayer( )
-- Retrieve the player's position and store it in the variables x, y and z
local x, y, z = getElementPosition( myPlayer )
-- Create a radar blip at the player's position, with a 'cash' icon and only visible to the player
local myBlip = createBlip( x, y, z, 51, 0, 0, 0, 255, myPlayer )
```

**Example 2:** This example attaches a blip to a player. You can attach a blip to an element by just setting the blip's parent to that element.

```
-- Pick a random player
local myPlayer = getRandomPlayer( )
-- Create a radar blip in the middle of the map
local myBlip = createBlip( 0, 0, 0 )
-- Make the player the parent of the blip, so that the blip follows the player around
setElementParent( myBlip, myPlayer )
```

## See Also

- createBlip

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)
