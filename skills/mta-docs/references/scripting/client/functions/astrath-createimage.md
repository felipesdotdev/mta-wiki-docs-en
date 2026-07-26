---
doc_id: "mta-wiki:14644"
title: "Astrath:createImage"
source_title: "Astrath:createImage"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateImage"
revision_id: 82562
language: "en"
categories: ["Client_functions"]
---

# Astrath:createImage

DxImage:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based image element. Images can be attached to parent elements, support transparency, custom styles, and optional parent-relative positioning. Each image instance is automatically registered in the DX library.

**Parameters:**

- path (string) – Path to the image file. Must exist.

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the image.

- parent (element) – Parent DX element to attach this image to (optional).

- relative (boolean) – Position relative to parent (optional).

**Returns:**

Returns the newly created DxImage element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the image element and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the image. |
| Ath:setEnabled(boolean) | Enables or disables the image for interaction. |
| Ath:setAlpha(number) | Sets the image transparency (0–255). |

**Example:**

```
local myImage = DxImage:new("images/logo.png", 100, 100, 200, 150)

myImage:setVisible(true)
myImage:setAlpha(200)
myImage:setPath("images/new_logo.png")
myImage:draw()
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – Page for label element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
