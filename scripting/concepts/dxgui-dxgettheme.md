---
doc_id: "mta-wiki:6495"
title: "DxGUI/dxGetTheme"
source_title: "DxGUI/dxGetTheme"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetTheme"
revision_id: 31212
language: "en"
categories: []
generated_at: "2026-07-26T16:14:48.786638+00:00"
---

# DxGUI/dxGetTheme

You can use this function to get theme by name.

## Syntax

```
dxTheme dxGetTheme ( themeName )
```

### Required Arguments

- **themeName:** A name of the theme in **themes.xml**

### Returns

Returns a dxTheme if it is exists, false otherwise.

## Example

This example creates a window based on orange theme.

```
local theme = dxGetTheme("Orange")
dxCreateWindow(....,theme)
```

## See Also

[Back to dxGUI page](mta://scripting/concepts/dxgui.md)
