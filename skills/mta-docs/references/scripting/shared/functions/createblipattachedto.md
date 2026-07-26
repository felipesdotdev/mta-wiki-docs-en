---
doc_id: "mta-wiki:1451"
title: "CreateBlipAttachedTo"
source_title: "CreateBlipAttachedTo"
source_url: "https://wiki.multitheftauto.com/wiki/CreateBlipAttachedTo"
revision_id: 69108
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Changes_in_1.0"]
---

# CreateBlipAttachedTo

This function creates a [blip](https://wiki.multitheftauto.com/index.php?search=blip) that is attached to an [element](mta://reference/misc/element.md). This blip is displayed as an icon on the client's radar and will 'follow' the element that it is attached to around.

## Syntax

Click to collapse [-]
Server

```
blip createBlipAttachedTo ( element elementToAttachTo [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0, element visibleTo = getRootElement( ) ] )
```

Click to collapse [-]
Client

```
blip createBlipAttachedTo ( element elementToAttachTo [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Blip](https://wiki.multitheftauto.com/index.php?search=Blip).createAttachedTo(...)*

### Required Arguments

- **elementToAttachTo:** The [element](mta://reference/misc/element.md) to attach the blip to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **icon:** The icon that the radar blips should be. Valid values can be seen at [Radar Blips](mta://reference/misc/radar-blips.md)

- **size:** The size of the radar blip. Only applicable to the *Marker* icon. Default value is 2. Maximum is 25.

- **r:** The amount of red in the blip's color (0 - 255). Only applicable to the *Marker* icon. Default is 255.

- **g:** The amount of green in the blip's color (0 - 255). Only applicable to the *Marker* icon. Default is 0.

- **b:** The amount of blue in the blip's color (0 - 255). Only applicable to the *Marker* icon. Default is 0.

- **a:** The amount of alpha in the blip's color (0 - 255). Only applicable to the *Marker* icon. Default is 255.

- **ordering:** This defines the blip's Z-level ordering (-32768 - 32767). Default is 0.

- **visibleDistance:** The maximum distance from the camera at which the blip is still visible (0-65535)

Click to collapse [-]
Server

- **visibleTo:** What elements can see the blip. Defaults to visible to everyone. See [visibility](mta://reference/misc/visibility.md).

### Returns

Returns a [blip](https://wiki.multitheftauto.com/index.php?search=blip) if the blip was created succesfully, or *false* otherwise.

## Example

Click to collapse [-]
Server

This example creates a radar blip attached to a random player, visible to everyone. The blip will follow the player around as they move. This could be used for manhunt, to emphasise a random player.

```
-- Pick a random player
function setupRandomRobber ()
	local myPlayer = getRandomPlayer ()
	-- Create a radar blip at the player's position, with a 'cash' icon and only visible to everyone (no 'visibleTo' parameter)
	local myBlip = createBlipAttachedTo ( myPlayer, 52 )
end
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- createBlipAttachedTo

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
