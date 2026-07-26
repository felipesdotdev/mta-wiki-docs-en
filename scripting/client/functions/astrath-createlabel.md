---
doc_id: "mta-wiki:14645"
title: "Astrath:createLabel"
source_title: "Astrath:createLabel"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateLabel"
revision_id: 82563
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:24.072126+00:00"
---

# Astrath:createLabel

DxLabel:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based label element. Labels display text, support parent-relative positioning, custom fonts, colors, alignment, and optional hover effects. Each label instance is automatically registered in the DX library.

**Parameters:**

- text (string) – Text to display in the label.

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the label.

- parent (element) – Parent DX element to attach this label to (optional).

- relative (boolean) – Position relative to parent (optional).

- font (string) – Font used for the text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

- horizontalAlign (string) – Horizontal alignment ("left", "center", "right", optional, default: "center").

- verticalAlign (string) – Vertical alignment ("top", "center", "bottom", optional, default: "center").

**Returns:**

Returns the newly created DxLabel element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the label element and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the label. |
| Ath:setEnabled(boolean) | Enables or disables the label for interaction. |
| Ath:setText(string) | Sets the label text. |
| Ath:getText() | Returns the current label text. |
| Ath:setFont(string) | Changes the label font. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main or hover text color. |
| Ath:setHorizontalAlign(string) | Sets horizontal alignment of the text. |
| Ath:setVerticalAlign(string) | Sets vertical alignment of the text. |

**Example:**

```
local myLabel = DxLabel:new("Hello World", 100, 100, 200, 50)

myLabel:setVisible(true)
myLabel:setHoverable(true)
myLabel:setText("Welcome")
myLabel:setColor(255, 200, 0, 255, "mainColor")
myLabel:setHorizontalAlign("center")
myLabel:setVerticalAlign("center")
myLabel:draw()
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Page for button element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
