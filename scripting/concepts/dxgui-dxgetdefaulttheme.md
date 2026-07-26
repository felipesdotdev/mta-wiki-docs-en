---
doc_id: "mta-wiki:6496"
title: "DxGUI/dxGetDefaultTheme"
source_title: "DxGUI/dxGetDefaultTheme"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxGetDefaultTheme"
revision_id: 31213
language: "en"
categories: []
generated_at: "2026-07-26T16:14:48.749871+00:00"
---

# DxGUI/dxGetDefaultTheme

You can use this function to get default theme.

## Syntax

```
dxTheme dxGetDefaultTheme ( )
```

### Returns

Returns a dxTheme if it was successfully got which then can use other methods, false otherwise.

## Example

This example create a window based on an orange theme.And create a button based on default theme.

```
local orange = dxGetTheme("Orange")
dxCreateWindow(....,orange)
local default = dxGetDefaultTheme()
dxCreateButton(....,default)
```

## See Also

[Back to dxGUI page](mta://scripting/concepts/dxgui.md)
