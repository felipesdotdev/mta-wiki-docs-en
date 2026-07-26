---
doc_id: "mta-wiki:14639"
title: "Astrath:createCheckBox"
source_title: "Astrath:createCheckBox"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateCheckBox"
revision_id: 82551
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:23.939196+00:00"
---

# Astrath:createCheckBox

DxCheckbox:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based checkbox element. Checkboxes can be attached to parent elements, support hover effects, custom colors, and selection state. Each checkbox instance is automatically registered in the DX library.

**Parameters:**

- text (string) – The label text of the checkbox. Defaults to "radio".

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the checkbox.

- parent (element) – Parent DX element to attach this checkbox to (optional).

- relative (boolean) – Position relative to parent (optional).

- font (string) – Font used for text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

**Returns:**

Returns the newly created DxCheckbox element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the checkbox and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the checkbox. |
| Ath:setEnabled(boolean) | Enables or disables the checkbox for interaction. |
| Ath:isSelected() | Returns whether the checkbox is currently selected. |
| Ath:setSelected(boolean) | Sets the checkbox selection state. |
| Ath:getSelected() | Returns the current selection state. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main, hover, or select color of the checkbox. |

**Example:**

```
-- Create a checkbox at position 300x400 with size 20x20
local myCheckbox = DxCheckbox:new("Accept Terms", 300, 400, 20, 20)

-- Show the checkbox and enable hover effect
myCheckbox:setVisible(true)
myCheckbox:setHoverable(true)

-- Set selection state
myCheckbox:setSelected(true)

-- Change colors
myCheckbox:setColor(255, 255, 255, 255, "mainColor")
myCheckbox:setColor(0, 255, 0, 200, "hoverColor")
myCheckbox:setColor(0, 200, 0, 255, "selectColor")
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Page for button element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
