---
doc_id: "mta-wiki:14571"
title: "DgsMenuAddItem"
source_title: "DgsMenuAddItem"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuAddItem"
revision_id: 82205
language: "en"
categories: ["Client_functions"]
---

# DgsMenuAddItem

This function adds a new item to a DGS menu. Each item can have text, a command identifier, and can optionally be a child of another item to create submenus.

## Syntax

```
int, int dgsMenuAddItem ( element menu, string text, string command [, int parentItemID, int position ] )
```

### Required Arguments

- **menu:** The DGS menu element to add the item to

- **text:** The text that will be displayed for this menu item

- **command:** A string identifier for this item (used to identify it when selected)

### Optional Arguments

- **parentItemID:** The unique ID of a parent item to create a submenu. If not specified, the item is added to the root menu

- **position:** The position where to insert the item. If not specified, the item is added at the end

### Returns

Returns the unique item ID and position if the item was added successfully, *false* otherwise.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu
local menu = dgsCreateMenu(200, 200, 180, 150, false)

-- Add root level items
local timeItem = dgsMenuAddItem(menu, "Time", "time")
local weatherItem = dgsMenuAddItem(menu, "Weather", "weather")
dgsMenuAddItem(menu, "Exit", "exit")

-- Add submenu items under "Time"
dgsMenuAddItem(menu, "Day", "set_day", timeItem)
dgsMenuAddItem(menu, "Night", "set_night", timeItem)

-- Add submenu items under "Weather"
dgsMenuAddItem(menu, "Clear", "clear_weather", weatherItem)
dgsMenuAddItem(menu, "Rain", "rain_weather", weatherItem)

-- Show the menu
dgsMenuShow(menu)

-- Handle menu selections
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end

    local command = dgsMenuGetItemCommand(source, uniqueID)
    if command == "set_day" then
        setTime(12, 0)
        outputChatBox("Time set to day")
    elseif command == "set_night" then
        setTime(0, 0)
        outputChatBox("Time set to night")
    elseif command == "clear_weather" then
        setWeather(0)
        outputChatBox("Weather set to clear")
    elseif command == "rain_weather" then
        setWeather(8)
        outputChatBox("Weather set to rain")
    elseif command == "exit" then
        dgsMenuHide(source)
        outputChatBox("Menu closed")
        return
    end

    -- Hide menu after most selections
    dgsMenuHide(source)
end, false)
```

## Notes

| [[{{{image}}}\|link=\|]] | Tip: Each item gets a unique ID that can be used with other menu functions like dgsMenuGetItemCommand |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Parent items automatically display a ">" indicator when they have child items |
| --- | --- |
|  |  |

## See Also

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [dgsMenuAddSeparator](mta://scripting/client/functions/dgsmenuaddseparator.md)

- [dgsMenuRemoveItem](mta://scripting/client/functions/dgsmenuremoveitem.md)

- [dgsMenuGetItemCommand](mta://scripting/client/functions/dgsmenugetitemcommand.md)

- [dgsMenuShow](mta://scripting/client/functions/dgsmenushow.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
