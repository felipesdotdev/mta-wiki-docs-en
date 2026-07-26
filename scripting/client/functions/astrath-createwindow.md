---
doc_id: "mta-wiki:14637"
title: "Astrath:createWindow"
source_title: "Astrath:createWindow"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateWindow"
revision_id: 82544
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:24.395155+00:00"
---

# Astrath:createWindow

DxWindow:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based window element. The window can contain child DX elements, supports customization of colors, fonts, header, and can be attached to a parent element. Each window instance is automatically registered in the DX library for rendering and management.

**Parameters:**

- title (string) – The title text displayed on the window. Defaults to "New window" if not provided.

- posX (float) – X position on screen.

- posY (float) – Y position on screen.

- width (float) – Width of the window.

- height (float) – Height of the window.

- color (table / tocolor) – Main background color in RGBA. Optional.

- parent (element) – Parent DX element to attach this window to. Optional.

- relative (boolean) – If true, position will be calculated relative to parent. Optional.

- header (boolean) – If true, the window will display a header. Optional.

- headerSize (float) – Relative size of the header. Defaults to 5% of height.

- headerColor (table / tocolor) – Header color in RGBA. Defaults to tocolor(91, 57, 219, 255).

- font (string) – Font used for title text. Defaults to "default-bold".

- fontsize (float) – Font size multiplier. Defaults to 1.

**Returns:**

Returns the newly created DX window element (DxWindow instance).

## Methods

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the window and all its child elements. |
| Ath:setTitle(title) | Sets a new title for the window. |
| Ath:setMovable(boolean) | Enables or disables window movement. |
| Ath:setVisible(boolean) | Shows or hides the window. |
| Ath:setEnabled(boolean) | Enables or disables window for interaction. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main or hover color of the window. |

**Example:**

```
-- Create a window at position 200x200 with size 300x200
local myWindow = DxWindow:new(
    "My Window", 200, 200, 300, 200, tocolor(50, 50, 50, 255), nil, false, true, 0.05, nil, "default-bold", 1
)

-- Show window and enable hover
myWindow:setVisible(true)
myWindow:setHoverable(true)
```

**See also:**

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – For creating buttons inside windows

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – For adding text labels

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to draw DX elements

- [Astrath](mta://reference/misc/astrath.md) – Main library page
