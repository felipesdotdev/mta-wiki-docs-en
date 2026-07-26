---
doc_id: "mta-wiki:13785"
title: "Dgs3DImageIsAttached"
source_title: "Dgs3DImageIsAttached"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs3DImageIsAttached"
revision_id: 76032
language: "en"
categories: ["Client_functions"]
---

# Dgs3DImageIsAttached

This functions checks whether or not 3DImage element is attached to another element.

## Syntax

```
bool dgs3DImageIsAttached( dgsElement element )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):isAttached(...)*

### Required Arguments

- **element:** The dgs 3d image element to check for attachment.

### Returns

Returns *true* if the specified element is attached to another element, *false* if it is not attached or *nil* if an improper argument was passed.

## Example

This example is making export function to check weather the player is talking or not:

```
dgs = exports.dgs

function isPlayerTalking(player)
	local player = player or localPlayer;
	return dgs:dgs3DImageIsAttached(icons[player]); -- this table inside another client file .
end
```

## See Also

- [dgsCreate3DImage](mta://scripting/client/functions/dgscreate3dimage.md)

- [dgs3DImageSetSize](mta://scripting/client/functions/dgs3dimagesetsize.md)

- [dgs3DImageGetSize](mta://scripting/client/functions/dgs3dimagegetsize.md)

- [dgs3DImageSetImage](mta://scripting/client/functions/dgs3dimagesetimage.md)

- [dgs3DImageGetImage](mta://scripting/client/functions/dgs3dimagegetimage.md)

- [dgs3DImageAttachToElement](mta://scripting/client/functions/dgs3dimageattachtoelement.md)

- dgs3DImageIsAttached

- [dgs3DImageDetachFromElement](mta://scripting/shared/functions/dgs3dimagedetachfromelement.md)

- [dgs3DImageSetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageSetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageGetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetNativeSize](mta://scripting/client/functions/dgs3dimagegetnativesize.md)

- [dgs3DImageSetUVPosition](mta://scripting/client/functions/dgs3dimagesetuvposition.md)

- [dgs3DImageGetUVPosition](mta://scripting/client/functions/dgs3dimagegetuvposition.md)

- [dgs3DImageSetUVSize](mta://scripting/client/functions/dgs3dimagesetuvsize.md)

- [dgs3DImageGetUVSize](mta://scripting/client/functions/dgs3dimagegetuvsize.md)
