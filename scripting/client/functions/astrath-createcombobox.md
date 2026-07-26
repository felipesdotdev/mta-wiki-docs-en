---
doc_id: "mta-wiki:14640"
title: "Astrath:createComboBox"
source_title: "Astrath:createComboBox"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateComboBox"
revision_id: 82553
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:23.960844+00:00"
---

# Astrath:createComboBox

DxCombobox:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based combobox element. Comboboxes allow selecting from a list of items, support scrolling, hover effects, and color customization. Each combobox instance is automatically registered in the DX library.

**Parameters:**

- text (string) – The default text displayed on the combobox.

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the combobox.

- parent (element) – Parent DX element to attach this combobox to (optional).

- relative (boolean) – Position relative to parent (optional).

- desc (string) – Default placeholder text when no item is selected (optional).

- maxItems (number) – Maximum number of items displayed at once (optional, default: 10).

- color (table / tocolor) – Base color for bar, button, and body (optional).

- font (string) – Font used for text (optional, default: "default-bold").

- fontSize (float) – Font size multiplier (optional, default: 1).

- scrollColor, scrollBGColor (table / tocolor) – Scrollbar colors (optional).

**Returns:**

Returns the newly created DxCombobox element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the combobox and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the combobox. |
| Ath:setEnabled(boolean) | Enables or disables the combobox for interaction. |
| Ath:setText(string) | Sets the text displayed on the combobox. |
| Ath:addItem(string) | Adds a new item to the combobox list. |
| Ath:removeItem(number) | Removes an item from the list by its index. |
| Ath:clear() | Removes all items from the combobox. |
| Ath:setItemText(number, string) | Updates the text of an item at a given index. |
| Ath:getItemText(number) | Returns the text of an item by index. |
| Ath:setSelected(number) | Sets the selected item by index. |
| Ath:getSelected() | Returns the index of the currently selected item. |
| Ath:getItemCount() | Returns the total number of items in the combobox. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the color of bar, button, body, or hover. |

**Example:**

```
-- Create a combobox at position 400x200 with size 150x25
local myCombo = DxCombobox:new("Select Item", 400, 200, 150, 25)

-- Add items
myCombo:addItem("Option 1")
myCombo:addItem("Option 2")
myCombo:addItem("Option 3")

-- Show combobox and enable hover
myCombo:setVisible(true)
myCombo:setHoverable(true)

-- Select second item
myCombo:setSelected(2)

-- Change bar color
myCombo:setColor(255, 255, 255, 255, "barColor")
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Page for button element reference

- [DxCheckbox:new](https://wiki.multitheftauto.com/index.php?title=DxCheckbox:new&action=edit&redlink=1) – Page for checkbox element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
