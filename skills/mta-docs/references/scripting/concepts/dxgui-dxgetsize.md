---
doc_id: "mta-wiki:6630"
title: "DxGUI/dxGetSize"
source_title: "DxGUI/dxGetSize"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetSize"
revision_id: 32359
language: "en"
categories: ["Utility_templates"]
---

# DxGUI/dxGetSize

You can use this function to get dxElement size.

## Syntax

```
float w, float h  dxGetSize (element dxElement, [bool relative = false])
```

### Required Arguments

- **dxElement:** A dxGUI element.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **relative:** This is whether sizes and positioning are relative.  If this is *true*, script give relative w,h.

### Returns

- **w**: An element width

- **h**: An element height

## Example

This example gets window relative size.

```
local w,h = dxGetSize(dxWindow,true)
outputChatBox(w.." "..h)
```

## See Also

[Back to dxGUI page](https://wiki.multitheftauto.com/index.php?search=Back%20to%20dxGUI%20page)
