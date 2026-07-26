---
doc_id: "mta-wiki:14638"
title: "Astrath:createButton"
source_title: "Astrath:createButton"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateButton"
revision_id: 82549
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:23.924427+00:00"
---

# Astrath:createButton

DxButton:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based button element. Buttons can be attached to parent elements, support hover effects, custom colors, icons, fonts, and descriptions. Each button instance is automatically registered in the DX library.

**Parameters:**

- text (string) – The button label text. Defaults to "Button".

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the button.

- parent (element) – Parent DX element to attach this button to (optional).

- relative (boolean) – Position relative to parent (optional).

- color (table / tocolor) – Main background color (optional).

- font (string) – Font used for text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

- description (string) – Optional description text.

- isIcon (boolean) – If true, the button will display an icon instead of text.

- iconWidth, iconHeight (float) – Size of the icon relative to the button (optional).

**Returns:**

Returns the newly created DxButton element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the button and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the button. |
| Ath:setEnabled(boolean) | Enables or disables the button for interaction. |
| Ath:setText(string) | Sets the button text. |
| Ath:getText() | Returns the current button text. |
| Ath:setDescription(string) | Sets the button description. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main or hover color of the button. |

**Example:**

```
-- Create a button at position 200x300 with size 150x50
local myButton = DxButton:new("Click Me", 200, 300, 150, 50)

-- Show the button and enable hover effect
myButton:setVisible(true)
myButton:setHoverable(true)

-- Change text and color
myButton:setText("Press Me")
myButton:setColor(255, 0, 0, 255, "mainColor")
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – Page for label element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
