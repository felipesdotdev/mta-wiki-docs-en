---
doc_id: "mta-wiki:7432"
title: "DxGUI/dxMove"
source_title: "DxGUI/dxMove"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxMove"
revision_id: 38172
language: "en"
categories: []
generated_at: "2026-07-26T16:14:48.807038+00:00"
---

# DxGUI/dxMove

You can use this function to move dxGUI element.

## Syntax

```
dxMove (element dxElement, float xMove, float yMove)
```

### Required Arguments

- **dxElement:** A dxGUI element.

- **xMove:** Position X, where dxGUI element move.

- **yMove:** Position Y, where dxGUI element move.

### Returns

- **false** if *dxElement*, *xMove*, *yMove* are not set.

## Example

This example moves dxGUI window to (0;0).

Click to collapse [-]
Client

```
local x, y = guiGetScreenSize() --Getting screen size
addEventHandler("onClientResourceStart", resourceRoot, 
    function()
        --Create dxGUI window with name "wind":
        wind = dxCreateWindow(x/2, y/2, 50, 50, "Window", tocolor(255,255,255,255),"default-bold","Lighter Black")
    end)    
--Move dxGUI to (0;0) when player joining.
addEventHandler("onClientPlayerJoin", resourceRoot, function() dxMove(wind, 0, 0) end)
```

## See Also

[Back to dxGUI page](mta://scripting/concepts/dxgui.md)
