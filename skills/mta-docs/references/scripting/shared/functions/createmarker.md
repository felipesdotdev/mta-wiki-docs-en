---
doc_id: "mta-wiki:1373"
title: "CreateMarker"
source_title: "CreateMarker"
source_url: "https://wiki.multitheftauto.com/wiki/CreateMarker"
revision_id: 79897
language: "en"
categories: ["Utility_templates", "Changes_in_1.6.0", "Server_functions", "Client_functions"]
---

# CreateMarker

| [[\|link=\|]] | Warning: When using type "arrow" markers, you may experience positioning issues. This is a known issue with how GTA creates these types of markers. It is recommended you keep the position at least 1 game unit above the ground to avoid issues. |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: "cylinder" marker type doesn't have the same size for collisions and visible textures. Note that the marker collisions are around 10-20% bigger than the visible texture. |
| --- | --- |
|  |  |

 

This image shows all the different marker types available using this function.

This function creates a marker. A marker is a 3D model in the world that can highlight a particular point or area, often used to instruct players where to go to perform actions such as entering buildings.

There are various limits that govern the maximum number of each type that can be visible at once. These are:

- Coronas: 32

- Checkpoints, Rings, Cylinders and Arrows combined: 32

You are able to create as many markers as you wish (memory and element limit permitting), but the player will only be able to see the nearest ones up to the limit.

## Syntax

Click to collapse [-]
Server

```
marker createMarker ( float x, float y, float z [, string theType = "checkpoint", float size = 4.0, int r = 0, int g = 0, int b = 255, int a = 255, element visibleTo = getRootElement( ), bool ignoreAlphaLimits = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Marker(...)*

### Required Arguments

- **x**: A floating point number representing the X coordinate on the map.

- **y**: A floating point number representing the Y coordinate on the map.

- **z**: A floating point number representing the Z coordinate on the map.

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **theType**: The visual type of the marker to be created. Possible values:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

- **size**: The diameter of the marker to be created, in meters.

- **r**: An integer number representing the amount of red to use in the colouring of the marker (0 - 255).

- **g**: An integer number representing the amount of green to use in the colouring of the marker (0 - 255).

- **b**: An integer number representing the amount of blue to use in the colouring of the marker (0 - 255).

- **a**: An integer number representing the amount of alpha to use in the colouring of the marker (0 - 255 where 0 is transparent and 255 is opaque).

- **visibleTo**: This defines which elements can see the marker. Defaults to visible to everyone. See [visibility](mta://reference/misc/visibility.md).

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **ignoreAlphaLimits**: This argument is only valid for **checkpoint** and **arrow** markers. It defines whether the alpha of these markers can be changed. If the argument is false, the marker has a constant alpha as before, i.e. checkpoint always 128 and arrow always 255. If the argument is true, alpha can be changed.

Click to collapse [-]
Client

```
marker createMarker ( float x, float y, float z [, string theType = "checkpoint", float size = 4.0, int r = 0, int g = 0, int b = 255, int a = 255, bool ignoreAlphaLimits  = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Marker(...)*

### Required Arguments

- **x**: A floating point number representing the X coordinate on the map.

- **y**: A floating point number representing the Y coordinate on the map.

- **z**: A floating point number representing the Z coordinate on the map.

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **theType**: The visual type of the marker to be created. Possible values:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

- **size**: The diameter of the marker to be created, in meters.

- **r**: An integer number representing the amount of red to use in the colouring of the marker (0 - 255).

- **g**: An integer number representing the amount of green to use in the colouring of the marker (0 - 255).

- **b**: An integer number representing the amount of blue to use in the colouring of the marker (0 - 255).

- **a**: An integer number representing the amount of alpha to use in the colouring of the marker (0 - 255 where 0 is transparent and 255 is opaque).

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **ignoreAlphaLimits**: This argument is only valid for **checkpoint** and **arrow** markers. It defines whether the alpha of these markers can be changed. If the argument is false, the marker has a constant alpha as before, i.e. checkpoint always 128 and arrow always 255. If the argument is true, alpha can be changed.

### Returns

Returns the [marker](https://wiki.multitheftauto.com/index.php?search=marker) element that was created, or *false* if the arguments are incorrect.

## Example

Click to collapse [-]
Example 1

This example creates a marker next to the player when they type 'createmarker':

```
-- this function is called whenever someone types 'createmarker' in the chat:
function chatCreateMarker ( thePlayer, commandName )
   if ( thePlayer ) then
      local x, y, z = getElementPosition ( thePlayer ) -- get the player's position
      -- create a cylindrical marker next to the player:
      local theMarker = createMarker ( x + 2, y + 2, z, "cylinder", 1.5, 255, 255, 0, 170 )
      if isElement ( theMarker ) then -- check if the marker was created successfully
         outputChatBox ( "Marker created successfully", thePlayer, 0, 255, 0 )
      else
         outputChatBox ( "Failed to create marker", thePlayer, 255, 0, 0 )
      end
   end
end
addCommandHandler ( "createmarker", chatCreateMarker )
```

## See Also

- createMarker

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)
