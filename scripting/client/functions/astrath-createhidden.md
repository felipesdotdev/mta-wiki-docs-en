---
doc_id: "mta-wiki:14643"
title: "Astrath:createHidden"
source_title: "Astrath:createHidden"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateHidden"
revision_id: 82558
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:24.022586+00:00"
---

# Astrath:createHidden

DxHidden:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a hidden DX element. Hidden elements are not drawn and can be used as containers or invisible parents for other DX elements. They can store position and size information and manage child elements.

**Parameters:**

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the hidden element.

- parent (element) – Parent DX element to attach this hidden element to (optional).

- relative (boolean) – Position relative to parent (optional).

**Returns:**

Returns the newly created DxHidden element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the hidden element and all its child elements. |
| Ath:setVisible(boolean) | Sets the visibility state of the hidden element (mostly for management, as hidden elements are not drawn). |
| Ath:setEnabled(boolean) | Enables or disables the element for internal logic or child interaction. |

**Example:**

```
-- Create a hidden element at position 100x100 with size 200x200
local hidden = DxHidden:new(100, 100, 200, 200)

-- Set it invisible (default, but can be toggled)
hidden:setVisible(false)

-- Enable it for internal logic
hidden:setEnabled(true)

-- Use as parent for other DX elements
local btn = DxButton:new("Click Me", 10, 10, 100, 40, hidden)
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Example of visible container element

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Example of child element
