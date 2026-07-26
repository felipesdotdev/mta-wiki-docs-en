---
doc_id: "mta-wiki:14641"
title: "Astrath:createEditBox"
source_title: "Astrath:createEditBox"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateEditBox"
revision_id: 82554
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:23.979987+00:00"
---

# Astrath:createEditBox

DxEdit:new / Astrath:createEditBox

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based edit box element. Edit boxes allow text input with options for read-only mode, numeric-only input, hover effects, and color customization. Each edit box instance is automatically registered in the DX library.

**Parameters:**

- text (string) – Initial text for the edit box (optional).

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the edit box.

- parent (element) – Parent DX element to attach this edit box to (optional).

- relative (boolean) – Position relative to parent (optional).

- font (string) – Font used for the text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

- placeholder (string) – Placeholder text when the edit box is empty (optional).

**Returns:**

Returns the newly created DxEdit element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the edit box and all its child elements. |
| Ath:clear() | Clears all text and resets the cursor. |
| Ath:setVisible(boolean) | Shows or hides the edit box. |
| Ath:setEnabled(boolean) | Enables or disables the edit box for interaction. |
| Ath:setReadOnly(boolean) | Enables or disables read-only mode. |
| Ath:setNumericOnly(boolean) | Enables numeric-only input. |
| Ath:getReadOnly() | Returns whether the edit box is in read-only mode. |
| Ath:setText(string) | Sets the text of the edit box. |
| Ath:getText() | Returns the current text of the edit box. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main background or hover color of the edit box. |

**Example:**

```
-- Create an edit box at position 400x200 with size 200x25
local myEdit = DxEdit:new("", 400, 200, 200, 25)

-- Set placeholder text
myEdit.placeholder = "Enter your name..."

-- Enable numeric only
myEdit:setNumericOnly(true)

-- Show edit box and enable hover
myEdit:setVisible(true)
myEdit:setHoverable(true)

-- Set background color to light grey
myEdit:setColor(200, 200, 200, 255, "mainColor")
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Page for button element reference

- [DxCheckbox:new](https://wiki.multitheftauto.com/index.php?title=DxCheckbox:new&action=edit&redlink=1) – Page for checkbox element reference

- [DxCombobox:new](https://wiki.multitheftauto.com/index.php?title=DxCombobox:new&action=edit&redlink=1) – Page for combobox element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
