---
doc_id: "mta-wiki:6497"
title: "DxGUI/dxGetPosition"
source_title: "DxGUI/dxGetPosition"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetPosition"
revision_id: 31215
language: "en"
categories: ["Utility_templates"]
---

# DxGUI/dxGetPosition

You can use this function to get dxElement position.

## Syntax

```
float x, float y (float Title:x,float Title:y) dxGetPosition (element dxElement, [bool relative = false])
```

### Required Arguments

- **dxElement:** A dxGUI element.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **relative:** This is whether sizes and positioning are relative.  If this is *true*, they send relative x,y,(Title:x,Title:y) positions.

### Returns

- **x**: An element x position

- **y**: An element y position

- **Title:x**: An element titlebar x position.(It's for only dxWindows)

- **Title:y**: An element titlebar y position.(It's for only dxWindows)

## Example

This example gets window position and multiply with 2.

```
local x,y = dxGetPosition(ourWindow)
dxSetPosition(ourWindow,x*2,y*2)
```

## See Also

[Back to dxGUI page](https://wiki.multitheftauto.com/index.php?search=Back%20to%20dxGUI%20page)
