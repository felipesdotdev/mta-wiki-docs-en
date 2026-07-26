---
doc_id: "mta-wiki:14583"
title: "DgsMenuRemoveItem"
source_title: "DgsMenuRemoveItem"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuRemoveItem"
revision_id: 82220
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:04.705079+00:00"
---

# DgsMenuRemoveItem

This function removes an item from a DGS menu element.

## Syntax

```
bool dgsMenuRemoveItem ( element menu, int uniqueID )
```

### Required Arguments

- **menu:** The DGS menu element from which to remove the item

- **uniqueID:** The unique ID of the menu item to remove (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Returns

Returns *true* if the item was successfully removed, *false* if the item with the specified uniqueID was not found.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Option 1", "command1")
local item2 = dgsMenuAddItem(menu, "Option 2", "command2")
local item3 = dgsMenuAddItem(menu, "Option 3", "command3")

-- Remove the second item
local removeItem = dgsMenuRemoveItem(menu, item2)

-- Show the menu (item2 will not be visible)
dgsMenuShow(menu)
```

## See Also

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuAddSeparator](mta://scripting/client/functions/dgsmenuaddseparator.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [dgsMenuGetItemText](mta://scripting/client/functions/dgsmenugetitemtext.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsMenuGetItemCommand](mta://scripting/client/functions/dgsmenugetitemcommand.md)

- [dgsMenuSetItemCommand](mta://scripting/client/functions/dgsmenusetitemcommand.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
