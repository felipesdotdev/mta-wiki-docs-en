---
doc_id: "mta-wiki:14577"
title: "DgsMenuGetItemTextSize"
source_title: "DgsMenuGetItemTextSize"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuGetItemTextSize"
revision_id: 82213
language: "en"
categories: ["Client_functions"]
---

# DgsMenuGetItemTextSize

This function gets the text size of a specific menu item.

## Syntax

```
float, float dgsMenuGetItemTextSize ( element menu, int uniqueID )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Returns

Returns two floats representing the horizontal and vertical text scale factors, or *false* if the operation failed.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Normal Size", "normal")
local item2 = dgsMenuAddItem(menu, "Large Text", "large")

-- Set different text sizes
dgsMenuSetItemTextSize(menu, item1, 1.0)
dgsMenuSetItemTextSize(menu, item2, 1.5, 2.0)

-- Get and display the text sizes
local sizeX1, sizeY1 = dgsMenuGetItemTextSize(menu, item1)
local sizeX2, sizeY2 = dgsMenuGetItemTextSize(menu, item2)

outputChatBox("Item 1 text size: " .. sizeX1 .. "x" .. sizeY1)
outputChatBox("Item 2 text size: " .. sizeX2 .. "x" .. sizeY2)

-- Show the menu
dgsMenuShow(menu)
```

## See Also

- [dgsMenuSetItemTextSize](mta://scripting/client/functions/dgsmenusetitemtextsize.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
