---
doc_id: "mta-wiki:14576"
title: "DgsMenuSetItemTextSize"
source_title: "DgsMenuSetItemTextSize"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuSetItemTextSize"
revision_id: 82212
language: "en"
categories: ["Client_functions"]
---

# DgsMenuSetItemTextSize

This function sets the text size of a specific menu item.

## Syntax

```
bool dgsMenuSetItemTextSize ( element menu, int uniqueID, float textSizeX [, float textSizeY ] )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

- **textSizeX:** The horizontal scale of the text

### Optional Arguments

- **textSizeY:** The vertical scale of the text. If not specified, textSizeX is used for both dimensions

### Returns

Returns *true* if the text size was set successfully, *false* otherwise.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with different text sizes
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Normal Size", "normal")
local item2 = dgsMenuAddItem(menu, "Large Text", "large")
local item3 = dgsMenuAddItem(menu, "Small Text", "small")

-- Set different text sizes for each item
dgsMenuSetItemTextSize(menu, item1, 1.0)        -- Normal size
dgsMenuSetItemTextSize(menu, item2, 1.5)        -- Large text
dgsMenuSetItemTextSize(menu, item3, 0.8, 0.8)   -- Small text

-- Show the menu
dgsMenuShow(menu)

-- Handle menu selections
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end
    
    local command = dgsMenuGetItemCommand(source, uniqueID)
    outputChatBox("Selected: " .. command)
    dgsMenuHide(source)
end, false)
```

## See Also

- [dgsMenuGetItemTextSize](mta://scripting/client/functions/dgsmenugetitemtextsize.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
