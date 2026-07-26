---
doc_id: "mta-wiki:14619"
title: "DgsGIFGetSize"
source_title: "DgsGIFGetSize"
source_url: "https://wiki.multitheftauto.com/wiki/DgsGIFGetSize"
revision_id: 82412
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:13:09.517941+00:00"
---

# DgsGIFGetSize

Returns the dimensions (width and height) of a GIF element created using [dgsCreateGIF](mta://scripting/client/functions/dgscreategif.md). The values correspond to the original size extracted from the GIF file during loading.

## Syntax

```
int int dgsGIFGetSize( element gif )
```

### Required Arguments

- **gif:** The **dgs-dxgif** type element you want to get the size of.

### Returns

Returns two integers corresponding to *width* and *height*

## Example

```
-- This script should be executed on the client-side

-- Import the DGS functions to use them from another resource
local DGS = exports.dgs

-- 1. Load the GIF from a file within your resource
local myAnimatedGif = DGS.dgsCreateGIF("files/loading.gif")

-- 2. Check if the GIF was loaded successfully before proceeding
if myAnimatedGif then
    -- 3. Use dgsGIFGetSize to get the width and height of the loaded GIF
    local width, height = DGS.dgsGIFGetSize(myAnimatedGif)

    -- 4. Display the dimensions in the chat to confirm the result
    outputChatBox(string.format("The loaded GIF has the dimensions: %d width by %d height.", width, height))

    -- 5. Practical example: Create a DGS image in the center of the screen
    --    using the 'width' and 'height' we just obtained so the size is perfect.
    local screenW, screenH = guiGetScreenSize()
    local posX = screenW / 2 - width / 2
    local posY = screenH / 2 - height / 2

    local gifImage = DGS.dgsCreateImage(posX, posY, width, height, myAnimatedGif, false)

    -- Start the GIF's animation
    DGS.dgsGIFPlay(myAnimatedGif)
else
    -- Inform the user if the GIF was not found or if an error occurred during loading
    outputChatBox("Error: Could not load the GIF file.", 255, 0, 0)
end
```

## See Also

- [dgsCreateGIF](mta://scripting/client/functions/dgscreategif.md)

- dgsGIFGetSize

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
