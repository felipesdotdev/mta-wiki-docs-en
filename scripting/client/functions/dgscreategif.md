---
doc_id: "mta-wiki:14618"
title: "DgsCreateGIF"
source_title: "DgsCreateGIF"
source_url: "https://wiki.multitheftauto.com/wiki/DgsCreateGIF"
revision_id: 82411
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:12:17.055444+00:00"
---

# DgsCreateGIF

This function creates a GIF interface plugin.

## Syntax

```
element dgsCreateGIF( string pathOrRaw )
```

### Required Arguments

- **pathOrRaw:** A string representing the path to your GIF file, or the raw GIF data

### Returns

Returns a dgs-dxgif element (DGS Plugin Type)[ dgs-dxgif (Element Type) ] if succeed, *false* otherwise

## Example

```
DGS = exports.dgs --get exported functions from dgs

local gif = DGS:dgsCreateGIF("test.gif")
DGS:dgsGIFPlay(gif,1)  --Play GIF with Speed 1x
image = DGS:dgsCreateImage(500,500,200,200,gif,false)
```

## See Also

- dgsCreateGIF

- [dgsGIFGetSize](mta://scripting/client/functions/dgsgifgetsize.md)

- [dgsGIFGetImageCount](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetImageCount&action=edit&redlink=1)

- [dgsGIFGetImages](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetImages&action=edit&redlink=1)

- [dgsGIFPlay](https://wiki.multitheftauto.com/index.php?title=DgsGIFPlay&action=edit&redlink=1)

- [dgsGIFStop](https://wiki.multitheftauto.com/index.php?title=DgsGIFStop&action=edit&redlink=1)

- [dgsGIFSetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetSpeed&action=edit&redlink=1)

- [dgsGIFGetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetSpeed&action=edit&redlink=1)

- [dgsGIFGetPlaying](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetPlaying&action=edit&redlink=1)

- [dgsGIFSetLooped](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetLooped&action=edit&redlink=1)

- [dgsGIFGetLooped](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetLooped&action=edit&redlink=1)

- [dgsGIFSetFrameID](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetFrameID&action=edit&redlink=1)

- [dgsGIFGetFrameID](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetFrameID&action=edit&redlink=1)
