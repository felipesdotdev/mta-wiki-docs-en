---
doc_id: "mta-wiki:13784"
title: "Dgs3DImageDetachFromElement"
source_title: "Dgs3DImageDetachFromElement"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs3DImageDetachFromElement"
revision_id: 75340
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:11:25.157816+00:00"
---

# Dgs3DImageDetachFromElement

This function detaches attached 3DImageElement from another element.

## Syntax

```
bool dgs3DImageDetachFromElement ( element the3DImageElement, [ element theAttachToElement ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):3DImageDetachFromElement(...)*

**Counterpart**: *[3DImageAttachToElement](https://wiki.multitheftauto.com/index.php?title=3DImageAttachToElement&action=edit&redlink=1)*

### Required Arguments

- **the3DImageElement:** The element to be detached (the "child")

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **theAttachToElement:** The element you wish to detach from, will detach from the attached element if this isn't specified.

### Returns

Returns *true* if the detaching was successful, *false* otherwise.

## Example

**Example 1:** This example attaches a marker to a vehicle, and detaches it when it blows up:

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

- [dgs3DImageAttachToElement](mta://scripting/client/functions/dgs3dimageattachtoelement.md)

- [dgs3DImageIsAttached](mta://scripting/client/functions/dgs3dimageisattached.md)

- dgs3DImageDetachFromElement

- [dgs3DImageSetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageSetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageGetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetNativeSize](mta://scripting/client/functions/dgs3dimagegetnativesize.md)

- [dgs3DImageSetUVPosition](mta://scripting/client/functions/dgs3dimagesetuvposition.md)

- [dgs3DImageGetUVPosition](mta://scripting/client/functions/dgs3dimagegetuvposition.md)

- [dgs3DImageSetUVSize](mta://scripting/client/functions/dgs3dimagesetuvsize.md)

- [dgs3DImageGetUVSize](mta://scripting/client/functions/dgs3dimagegetuvsize.md)
