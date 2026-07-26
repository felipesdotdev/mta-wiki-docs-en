---
doc_id: "mta-wiki:14575"
title: "DgsMenuGetItemText"
source_title: "DgsMenuGetItemText"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuGetItemText"
revision_id: 82211
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:04.672111+00:00"
---

# DgsMenuGetItemText

This function retrieves the displayed text of a menu item.

## Syntax

```
string dgsMenuGetItemText ( element menu, int uniqueID )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Returns

Returns the text string if successful, *false* if the item doesn't exist.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with some items
local menu = dgsCreateMenu(200, 200, 150, 100, false)
local item1 = dgsMenuAddItem(menu, "New Game", "new")
local item2 = dgsMenuAddItem(menu, "Load Game", "load")
local item3 = dgsMenuAddItem(menu, "Exit", "exit")

-- Show the menu
dgsMenuShow(menu)

-- Get and display the text of menu items
local text1 = dgsMenuGetItemText(menu, item1)
local text2 = dgsMenuGetItemText(menu, item2)
local text3 = dgsMenuGetItemText(menu, item3)

outputChatBox("Menu items: " .. text1 .. ", " .. text2 .. ", " .. text3)
-- Output: "Menu items: New Game, Load Game, Exit"
```

## See Also

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuGetItemCommand](mta://scripting/client/functions/dgsmenugetitemcommand.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
