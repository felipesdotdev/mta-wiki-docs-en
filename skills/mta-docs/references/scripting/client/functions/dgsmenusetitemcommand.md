---
doc_id: "mta-wiki:14572"
title: "DgsMenuSetItemCommand"
source_title: "DgsMenuSetItemCommand"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuSetItemCommand"
revision_id: 82209
language: "en"
categories: ["Client_functions"]
---

# DgsMenuSetItemCommand

This function changes the command identifier of an existing menu item. The command is used to identify the item when it's selected.

## Syntax

```
bool dgsMenuSetItemCommand ( element menu, int uniqueID, string command )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

- **command:** The new command identifier for this item

### Returns

Returns *true* if the command was set successfully, *false* otherwise.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with some items
local menu = dgsCreateMenu(200, 200, 150, 120, false)
local item1 = dgsMenuAddItem(menu, "Save", "save")
local item2 = dgsMenuAddItem(menu, "Load", "load")
local item3 = dgsMenuAddItem(menu, "Toggle", "mode_normal")

-- Show the menu
dgsMenuShow(menu)

-- Change the toggle item command based on current state
local isAdvancedMode = false

function toggleMode()
    isAdvancedMode = not isAdvancedMode

    if isAdvancedMode then
        dgsMenuSetItemCommand(menu, item3, "mode_advanced")
        dgsMenuSetItemText(menu, item3, "Advanced Mode")
        outputChatBox("Switched to advanced mode")
    else
        dgsMenuSetItemCommand(menu, item3, "mode_normal")
        dgsMenuSetItemText(menu, item3, "Normal Mode")
        outputChatBox("Switched to normal mode")
    end
end

-- Handle menu selections
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end

    local command = dgsMenuGetItemCommand(source, uniqueID)
    if command == "save" then
        outputChatBox("Saving...")
    elseif command == "load" then
        outputChatBox("Loading...")
    elseif command == "mode_normal" or command == "mode_advanced" then
        toggleMode()
    end
end, false)
```

## Notes

| [[{{{image}}}\|link=\|]] | Note: The menu automatically resizes when item commands are changed |
| --- | --- |
|  |  |

## See Also

- [dgsMenuGetItemCommand](mta://scripting/client/functions/dgsmenugetitemcommand.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
