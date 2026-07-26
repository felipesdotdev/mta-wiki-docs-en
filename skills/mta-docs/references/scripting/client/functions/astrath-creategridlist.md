---
doc_id: "mta-wiki:14642"
title: "Astrath:createGridList"
source_title: "Astrath:createGridList"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateGridList"
revision_id: 82557
language: "en"
categories: ["Client_functions"]
---

# Astrath:createGridList

DxEdit:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based gridlist element. Gridlists display rows and columns of data, support scrolling, hover effects, row selection, and customizable colors and fonts. Each gridlist instance is automatically registered in the DX library.

**Parameters:**

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the gridlist.

- parent (element) – Parent DX element to attach this gridlist to (optional).

- relative (boolean) – Position relative to parent (optional).

- columnSize (table / number / 'auto') – Width of columns, can be 'auto' to divide evenly.

- font (string) – Font used for text (optional, default: "default-bold").

- fontSize (float) – Font size multiplier (optional, default: 1).

- color, headColor, hoverColor, activeColor (table / tocolor) – Main, header, hover, and active row colors (optional).

- scrollColor, scrollBGColor (table / tocolor) – Scrollbar colors (optional).

**Returns:**

Returns the newly created DxGridlist element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the gridlist and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the gridlist. |
| Ath:setEnabled(boolean) | Enables or disables the gridlist for interaction. |
| Ath:addColumn(title, textAlign, columnSize) | Adds a new column with optional alignment and width. |
| Ath:addRow(...) | Adds a new row with the given items. |
| Ath:clear() | Clears all rows from the gridlist. |
| Ath:setColumnTitle(idOrName, newTitle) | Changes the title of a column by ID or name. |
| Ath:setItemText(columnID, rowID, text) | Sets the text of a specific cell. |
| Ath:getItemText(columnID, rowID) | Returns the text of a specific cell. |
| Ath:getColumnCount() | Returns the total number of columns. |
| Ath:getRowCount() | Returns the total number of rows. |
| Ath:removeColumn(columnID) | Removes a column by its ID. |
| Ath:removeRow(rowID) | Removes a row by its ID. |
| Ath:getRowText(columnID, rowID) | Returns the text of a cell at a given row and column. |
| Ath:getSelectedRowID() | Returns the currently selected row ID. |
| Ath:getSelectedRowItem() | Returns all items in the currently selected row. |
| Ath:setSelectedRowID(id) | Sets the selected row by ID. |
| Ath:addChildDxElement(element) | Adds a child element to the gridlist. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets colors for main, hover, header, active, or scroll elements. |

**Example:**

```
-- Create a gridlist at position 200x150 with size 400x300
local myGrid = DxGridlist:new(200, 150, 400, 300)

-- Add columns
myGrid:addColumn("ID", "center", 0.1)
myGrid:addColumn("Name", "left", 0.45)
myGrid:addColumn("Score", "right", 0.45)

-- Add rows
myGrid:addRow(1, "Alice", 95)
myGrid:addRow(2, "Bob", 88)
myGrid:addRow(3, "Charlie", 76)

-- Set selected row
myGrid:setSelectedRowID(2)

-- Change main color
myGrid:setColor(50, 50, 50, 255, "mainColor")
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxButton:new](https://wiki.multitheftauto.com/index.php?title=DxButton:new&action=edit&redlink=1) – Page for button element reference

- [DxCombobox:new](https://wiki.multitheftauto.com/index.php?title=DxCombobox:new&action=edit&redlink=1) – Page for combobox element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
