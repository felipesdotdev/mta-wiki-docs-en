---
doc_id: "mta-wiki:14579"
title: "DgsMenuGetItemColor"
source_title: "DgsMenuGetItemColor"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuGetItemColor"
revision_id: 82224
language: "en"
categories: ["Client_functions"]
---

# DgsMenuGetItemColor

This function gets the color of a specific menu item. You can retrieve the colors either as separate RGBA components or as color values.

## Syntax 1

```
int r, int g, int b, int a, int hr, int hg, int hb, int ha dgsMenuGetItemColor ( element menu, int uniqueID )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Optional Arguments

- **notSplitColor:** If set to *true*, returns the color values as they are stored (two color values). If *false* or not specified, returns 8 separate RGBA components

### Returns

When **notSplitColor** is *false* or not specified:
Returns 8 integers representing the RGBA components: normal red, normal green, normal blue, normal alpha, hover red, hover green, hover blue, hover alpha. Returns *false* if the operation failed.

## Syntax2

```
int normalColor, int hoverColor dgsMenuGetItemColor ( element menu, int uniqueID, bool notSplitColor )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Optional Arguments

- **notSplitColor:** If set to *true*, returns the color values as they are stored (two color values). If *false* or not specified, returns 8 separate RGBA components

### Returns

When **notSplitColor** is *true*:
Returns two color values: normalColor, hoverColor. Returns *false* if the operation failed.

## Examples

### Example 1: Getting RGBA Components

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Red Item", "red")
local item2 = dgsMenuAddItem(menu, "Custom Item", "custom")

-- Set colors for the items
dgsMenuSetItemColor(menu, item1, 255, 0, 0, 200)  -- Red with alpha
local normalColor = tocolor(100, 150, 200)
local hoverColor = tocolor(200, 255, 100)
dgsMenuSetItemColor(menu, item2, {normalColor, hoverColor})

-- Get the colors as RGBA components
local r, g, b, a, hr, hg, hb, ha = dgsMenuGetItemColor(menu, item1)
if r then
    outputChatBox("Item 1 - Normal: R=" .. r .. " G=" .. g .. " B=" .. b .. " A=" .. a)
    outputChatBox("Item 1 - Hover: R=" .. hr .. " G=" .. hg .. " B=" .. hb .. " A=" .. ha)
end

local r2, g2, b2, a2, hr2, hg2, hb2, ha2 = dgsMenuGetItemColor(menu, item2)
if r2 then
    outputChatBox("Item 2 - Normal: R=" .. r2 .. " G=" .. g2 .. " B=" .. b2 .. " A=" .. a2)
    outputChatBox("Item 2 - Hover: R=" .. hr2 .. " G=" .. hg2 .. " B=" .. hb2 .. " A=" .. ha2)
end

-- Show the menu
dgsMenuShow(menu)
```

### Example 2: Getting Color Values

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Blue Item", "blue")
local item2 = dgsMenuAddItem(menu, "Yellow Item", "yellow")

-- Set colors for the items
dgsMenuSetItemColor(menu, item1, tocolor(0, 0, 255))  -- Blue for both states
local normalYellow = tocolor(255, 255, 0)
local hoverYellow = tocolor(255, 255, 150)
dgsMenuSetItemColor(menu, item2, {normalYellow, hoverYellow})

-- Get the colors as color values
local normalColor1, hoverColor1 = dgsMenuGetItemColor(menu, item1, true)
if normalColor1 then
    outputChatBox("Item 1 - Normal Color: " .. normalColor1)
    outputChatBox("Item 1 - Hover Color: " .. hoverColor1)
end

local normalColor2, hoverColor2 = dgsMenuGetItemColor(menu, item2, true)
if normalColor2 then
    outputChatBox("Item 2 - Normal Color: " .. normalColor2)
    outputChatBox("Item 2 - Hover Color: " .. hoverColor2)
end

-- Show the menu
dgsMenuShow(menu)
```

### Example 3: Color Inspection and Modification

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items
local menu = dgsCreateMenu(200, 200, 200, 150, false)
local item1 = dgsMenuAddItem(menu, "Inspectable Item", "inspect")

-- Set initial color
dgsMenuSetItemColor(menu, item1, 128, 128, 128, 255)  -- Gray

-- Function to inspect and modify colors
function inspectAndModifyColor(menu, uniqueID)
    -- Get current colors as RGBA components
    local r, g, b, a, hr, hg, hb, ha = dgsMenuGetItemColor(menu, uniqueID)
    
    if r then
        outputChatBox("Current colors:")
        outputChatBox("Normal - R:" .. r .. " G:" .. g .. " B:" .. b .. " A:" .. a)
        outputChatBox("Hover - R:" .. hr .. " G:" .. hg .. " B:" .. hb .. " A:" .. ha)
        
        -- Modify the colors (make them brighter)
        local newR = math.min(255, r + 50)
        local newG = math.min(255, g + 50)
        local newB = math.min(255, b + 50)
        
        -- Set the new colors
        dgsMenuSetItemColor(menu, uniqueID, newR, newG, newB, a)
        outputChatBox("Colors have been brightened!")
    else
        outputChatBox("Failed to get item colors")
    end
end

-- Show the menu
dgsMenuShow(menu)

-- Inspect and modify colors after 3 seconds
setTimer(inspectAndModifyColor, 3000, 1, menu, item1)
```

## See Also

- [dgsMenuSetItemColor](mta://scripting/client/functions/dgsmenusetitemcolor.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuGetItemText](mta://scripting/client/functions/dgsmenugetitemtext.md)

- [dgsMenuGetItemTextSize](mta://scripting/client/functions/dgsmenugetitemtextsize.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
