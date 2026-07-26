---
doc_id: "mta-wiki:12315"
title: "DgsBlurBoxSetLevel"
source_title: "DgsBlurBoxSetLevel"
source_url: "https://wiki.multitheftauto.com/wiki/DgsBlurBoxSetLevel"
revision_id: 66436
language: "en"
categories: ["Client_functions"]
---

# DgsBlurBoxSetLevel

This function sets blur box level.

## Syntax

```
bool dgsBlurBoxSetLevel( element blurBox, int level )
```

### Required Arguments

- **blurBox:** A dgs blur box element.

- **level:** A int of the blur box level.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This example change blur box level every 1 second.

```
DGS = exports.dgs --get exported functions from dgs

local blurbox = DGS:dgsCreateBlurBox(600,500)
local window = DGS:dgsCreateImage(200,200,600,500,blurbox,false)
blurLevel = 0
setTimer(function()
    blurLevel = blurLevel + 1
    outputChatBox("Blur box level is now "..blurLevel)
end, 1000, 0)

addEventHandler("onClientRender", root, function()
    DGS:dgsBlurBoxSetLevel(blurbox,blurLevel)
    if blurLevel >= 15 then
        blurLevel = 0
    end
end)
```
