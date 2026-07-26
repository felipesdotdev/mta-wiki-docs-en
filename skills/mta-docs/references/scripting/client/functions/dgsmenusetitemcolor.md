---
doc_id: "mta-wiki:14578"
title: "DgsMenuSetItemColor"
source_title: "DgsMenuSetItemColor"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuSetItemColor"
revision_id: 82214
language: "en"
categories: ["Client_functions"]
---

# DgsMenuSetItemColor

This function sets the color of a specific menu item. You can set both the normal and hover colors for the item.

## Syntax

```
bool dgsMenuSetItemColor ( element menu, int uniqueID, int r, int g, int b [, int a ] )
bool dgsMenuSetItemColor ( element menu, int uniqueID, int color )
bool dgsMenuSetItemColor ( element menu, int uniqueID, table colors )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Optional Arguments

- **r:** The red component (0-255)

- **g:** The green component (0-255)

- **b:** The blue component (0-255)

- **a:** The alpha component (0-255). If not specified, 255 is used

- **color:** A single color value (created with [tocolor](mta://scripting/shared/functions/tocolor.md))

- **colors:** A table containing two color values: {normalColor, hoverColor}. If only one color is provided, it will be used for both states

### Returns

Returns *true* if the color was set successfully, *false* otherwise.

## Examples

### Example 1: Using RGB Values

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Red Item", "red")
local item2 = dgsMenuAddItem(menu, "Blue Item", "blue")
local item3 = dgsMenuAddItem(menu, "Green Item", "green")

-- Set different colors for each item using RGB values
dgsMenuSetItemColor(menu, item1, 255, 0, 0)        -- Red
dgsMenuSetItemColor(menu, item2, 0, 0, 255, 200)   -- Blue with alpha
dgsMenuSetItemColor(menu, item3, 0, 255, 0)        -- Green

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

### Example 2: Using Color Values

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Yellow Item", "yellow")
local item2 = dgsMenuAddItem(menu, "Purple Item", "purple")
local item3 = dgsMenuAddItem(menu, "Orange Item", "orange")

-- Set colors using tocolor function
dgsMenuSetItemColor(menu, item1, tocolor(255, 255, 0))     -- Yellow
dgsMenuSetItemColor(menu, item2, tocolor(128, 0, 128))     -- Purple
dgsMenuSetItemColor(menu, item3, tocolor(255, 165, 0))     -- Orange

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

### Example 3: Using Color Tables (Normal and Hover States)

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Custom Colors", "custom")
local item2 = dgsMenuAddItem(menu, "Another Item", "another")

-- Set different colors for normal and hover states
local normalColor = tocolor(100, 100, 100)    -- Gray when normal
local hoverColor = tocolor(255, 255, 255)     -- White when hovering
dgsMenuSetItemColor(menu, item1, {normalColor, hoverColor})

-- You can also use the same color for both states
local singleColor = tocolor(255, 100, 100)    -- Light red
dgsMenuSetItemColor(menu, item2, {singleColor})  -- Will use the same color for both states

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

- [dgsMenuGetItemColor](mta://scripting/client/functions/dgsmenugetitemcolor.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsMenuSetItemTextSize](mta://scripting/client/functions/dgsmenusetitemtextsize.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
