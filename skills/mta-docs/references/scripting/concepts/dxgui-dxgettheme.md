---
doc_id: "mta-wiki:6495"
title: "DxGUI/dxGetTheme"
source_title: "DxGUI/dxGetTheme"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetTheme"
revision_id: 31212
language: "en"
categories: []
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

[Back to dxGUI page](https://wiki.multitheftauto.com/index.php?search=Back%20to%20dxGUI%20page)
