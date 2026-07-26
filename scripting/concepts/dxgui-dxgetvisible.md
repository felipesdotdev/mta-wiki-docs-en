---
doc_id: "mta-wiki:6631"
title: "DxGUI/dxGetVisible"
source_title: "DxGUI/dxGetVisible"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetVisible"
revision_id: 32360
language: "en"
categories: []
generated_at: "2026-07-26T16:14:48.793802+00:00"
---

# DxGUI/dxGetVisible

You can use this function to get dxElement visiblity.

## Syntax

```
dxElement  dxGetVisible (element dxElement)
```

### Required Arguments

- **dxElement:** A dxGUI element.

### Returns

- **visiblity**: dxGUI visiblity

## Example

This example gets window visiblity.

```
local visiblity = dxGetVisible(dxWindow)
outputChatBox( tostring(visiblity) )
```

## See Also

[Back to dxGUI page](mta://scripting/concepts/dxgui.md)
