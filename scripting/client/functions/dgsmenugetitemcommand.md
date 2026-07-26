---
doc_id: "mta-wiki:14573"
title: "DgsMenuGetItemCommand"
source_title: "DgsMenuGetItemCommand"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuGetItemCommand"
revision_id: 82210
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:04.663606+00:00"
---

# DgsMenuGetItemCommand

This function retrieves the command identifier of a menu item. The command is used to identify which action should be performed when the item is selected.

## Syntax

```
string dgsMenuGetItemCommand ( element menu, int uniqueID )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

### Returns

Returns the command string if successful, *false* if the item doesn't exist.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with different types of items
local menu = dgsCreateMenu(200, 200, 180, 150, false)
local fileItem = dgsMenuAddItem(menu, "File", "file")
    dgsMenuAddItem(menu, "New", "file_new", fileItem)
    dgsMenuAddItem(menu, "Open", "file_open", fileItem)
    dgsMenuAddItem(menu, "Save", "file_save", fileItem)
dgsMenuAddSeparator(menu)
dgsMenuAddItem(menu, "Exit", "exit")

-- Show the menu
dgsMenuShow(menu)

-- Handle menu selections by checking commands
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end
    
    -- Get the command of the selected item
    local command = dgsMenuGetItemCommand(source, uniqueID)
    
    -- Perform actions based on command
    if command == "file_new" then
        outputChatBox("Creating new file...")
    elseif command == "file_open" then
        outputChatBox("Opening file...")
    elseif command == "file_save" then
        outputChatBox("Saving file...")
    elseif command == "exit" then
        outputChatBox("Goodbye!")
        dgsMenuHide(source)
        return
    end
    
    -- Close menu after action
    dgsMenuHide(source)
end, false)
```

## See Also

- [dgsMenuSetItemCommand](mta://scripting/client/functions/dgsmenusetitemcommand.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [onDgsMenuSelect](mta://scripting/client/events/ondgsmenuselect.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
