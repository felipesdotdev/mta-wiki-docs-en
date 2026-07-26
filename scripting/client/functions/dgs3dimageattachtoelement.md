---
doc_id: "mta-wiki:13783"
title: "Dgs3DImageAttachToElement"
source_title: "Dgs3DImageAttachToElement"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs3DImageAttachToElement"
revision_id: 75342
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:11:25.141464+00:00"
---

# Dgs3DImageAttachToElement

This function attaches 3D Image element to another element, so that the first one follows the second whenever it moves.

If an attempt is made to attach two elements that are already attached the opposite way (eg the3DImage becomes theAttachToElement and vice versa), the 1st attachment order is automatically detached in favor of the 2nd attachment order. Also, the3DImage  cannot be attached to two separate elements at one time. For example, two the3DImage can be attached to one single car, but you can attach car to the3DImage , If you attempt to do this it won't work .

This is not compatible with all elements.  The following elements are compatible:

- [Peds](mta://reference/misc/ped.md)

- [Players](mta://reference/misc/player.md)

- [Blips](mta://reference/misc/blip.md)

- [Vehicles](mta://reference/misc/vehicle.md)

- [Objects](mta://reference/misc/object.md)

- [Markers](mta://reference/misc/marker.md)

- [Pickups](mta://reference/misc/pickup.md)

- [Sounds](mta://reference/misc/sound.md)

- [Colshapes](mta://reference/misc/colshape.md)

- [Weapons](mta://scripting/client/functions/createweapon.md)

- [Cameras](mta://scripting/client/functions/camera.md)

## Syntax

```
bool dgs3DImageAttachToElement ( dgsElement the3DImageElement, element theAttachToElement, [ float xPosOffset = 0, float yPosOffset = 0, float zPosOffset = 0, float xRotOffset = 0, float yRotOffset = 0, float zRotOffset = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):3DImageAttachToElement(...)*

**Counterpart**: *[3DImageDetachFromElement](https://wiki.multitheftauto.com/index.php?title=3DImageDetachFromElement&action=edit&redlink=1)*

### Required Arguments

- **the3DImageElement:** The 3D Image element to be attached.

- **theAttachToElement:** The element to attach the first to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **xPosOffset:** The x offset, if you want the elements to be a certain distance from one another (default 0).

- **yPosOffset:** The y offset (default 0).

- **zPosOffset:** The z offset (default 0).

- **xRotOffset:** The x rotation offset (default 0).

- **yRotOffset:** The y rotation offset (default 0).

- **zRotOffset:** The z rotation offset (default 0).

### Returns

Returns *true* if the attaching process was successful, *false* otherwise.

## Example

Click to collapse [-]
client

**Example 1:** This example attaches a mic icon to any player who start voice chat:

```
dgs = exports.dgs

if isVoiceEnabled() then
	local micPNG = dxCreateTexture('assests/mic.png');
	local icons = {};
	addEventHandler('onClientPlayerVoiceStart',root,
		function()
			print('[Voice-System]: '..getPlayerName(source)..' started talking.')
			local x,y,z = getElementPosition(source);
			if ((source ~= localPlayer and isElementOnScreen(source)) or (localPlayer == source)) and not isElement(icons[source]) then
				icons[source] = dgs:dgsCreate3DImage(x,y,z+1.5,micPNG,tocolor(255,255,255,255),4,4,20);
				dgs:dgs3DImageAttachToElement( icons[source],localPlayer,0,0,1.5)
			end 
		end
	)
	addEventHandler('onClientPlayerVoiceStop',root,
		function() 
			print('[Voice-System]: '..getPlayerName(source)..' Stoped talking.')
			if isElement(icons[source]) then
				dgs:dgs3DImageDettachFromElement( icons[source],localPlayer);
				destroyElement(icons[source]);
				icons[source] = nil;
			end
		end
	)
end
```

## See Also

- [dgsCreate3DImage](mta://scripting/client/functions/dgscreate3dimage.md)

- [dgs3DImageSetSize](mta://scripting/client/functions/dgs3dimagesetsize.md)

- [dgs3DImageGetSize](mta://scripting/client/functions/dgs3dimagegetsize.md)

- [dgs3DImageSetImage](mta://scripting/client/functions/dgs3dimagesetimage.md)

- [dgs3DImageGetImage](mta://scripting/client/functions/dgs3dimagegetimage.md)

- dgs3DImageAttachToElement

- [dgs3DImageIsAttached](mta://scripting/client/functions/dgs3dimageisattached.md)

- [dgs3DImageDetachFromElement](mta://scripting/shared/functions/dgs3dimagedetachfromelement.md)

- [dgs3DImageSetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageSetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageGetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetNativeSize](mta://scripting/client/functions/dgs3dimagegetnativesize.md)

- [dgs3DImageSetUVPosition](mta://scripting/client/functions/dgs3dimagesetuvposition.md)

- [dgs3DImageGetUVPosition](mta://scripting/client/functions/dgs3dimagegetuvposition.md)

- [dgs3DImageSetUVSize](mta://scripting/client/functions/dgs3dimagesetuvsize.md)

- [dgs3DImageGetUVSize](mta://scripting/client/functions/dgs3dimagegetuvsize.md)
