---
doc_id: "mta-wiki:14647"
title: "Astrath:createRadio"
source_title: "Astrath:createRadio"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateRadio"
revision_id: 82565
language: "en"
categories: ["Client_functions"]
---

# Astrath:createRadio

DxRadio:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based radio button element. Radio buttons are single-select controls grouped by a key, allowing only one selection per group. Each radio instance is automatically registered in the DX library.

**Parameters:**

- text (string) – Label text for the radio button (optional, default: "radiobutton").

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the radio button.

- parent (element) – Parent DX element to attach this radio button to (optional).

- relative (boolean) – Position relative to parent (optional).

- key (string) – Group key to identify radio button group (optional, default: "Default").

- font (string) – Font used for text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

**Returns:**

Returns the newly created DxRadio element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the radio element and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the radio button. |
| Ath:setEnabled(boolean) | Enables or disables the radio button for interaction. |
| Ath:setSelected() | Selects this radio button and deselects others in the same group. |
| Ath:getSelected() | Returns whether this radio button is selected. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets main, hover, or selected color of the radio button. |

**Example:**

```
local myRadio = DxRadio:new("Option 1", 100, 100, 150, 30)

myRadio:setVisible(true)
myRadio:setHoverable(true)
myRadio:setColor(200, 200, 200, 200, "mainColor")
myRadio:setColor(30, 30, 30, 255, "selectColor")
myRadio:setSelected()
myRadio:draw()
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – Page for label element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
