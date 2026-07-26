---
doc_id: "mta-wiki:14648"
title: "Astrath:createShape"
source_title: "Astrath:createShape"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateShape"
revision_id: 82566
language: "en"
categories: ["Client_functions"]
---

# Astrath:createShape

DxShape:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based shape element. Shapes can have custom colors, hover effects, and rounded corners. Each shape instance is automatically registered in the DX library.

**Parameters:**

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the shape.

- parent (element) – Parent DX element to attach this shape to (optional).

- relative (boolean) – Position relative to parent (optional).

- color (table / tocolor) – Main color of the shape (optional, default: grey).

**Returns:**

Returns the newly created DxShape element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the shape and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the shape. |
| Ath:setEnabled(boolean) | Enables or disables the shape for interaction. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets main or hover color of the shape. |

**Example:**

```
local myShape = DxShape:new(100, 100, 200, 150)
myShape:setVisible(true)
myShape:setHoverable(true)
myShape:setColor(150, 150, 150, 255, "mainColor")
myShape:draw()
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – Page for label element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
