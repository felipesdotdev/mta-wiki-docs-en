---
doc_id: "mta-wiki:14581"
title: "DgsMenuAddSeparator"
source_title: "DgsMenuAddSeparator"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuAddSeparator"
revision_id: 82221
language: "en"
categories: ["Client_functions"]
---

# DgsMenuAddSeparator

This function adds a separator to a DGS menu. A separator is a visual divider that can be used to organize menu items into logical groups. It can be displayed as a horizontal line or as text.

 
A thin horizontal line used to visually divide sections of a DGS Menu

 
DGS Text Seperator

## Syntax

```
int uniqueID, int position dgsMenuAddSeparator ( element menu [, string text, int parentItemID, int position ] )
```

### Required Arguments

- **menu:** The DGS menu element to add the separator to

### Optional Arguments

- **text:** The text to display for the separator. If not specified or *nil*, a horizontal line will be drawn instead

- **parentItemID:** The unique ID of the parent item. If not specified, the separator will be added to the root menu

- **position:** The position where the separator should be inserted. If not specified, it will be added at the end

### Returns

Returns the unique ID of the separator and its position if successful, *false* otherwise.

## Examples

### Example 1: Basic Separator (Line)

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with items and separators
local menu = dgsCreateMenu(200, 200, 200, 150, false)

-- Add some menu items
local item1 = dgsMenuAddItem(menu, "New File", "file.new")
local item2 = dgsMenuAddItem(menu, "Open File", "file.open")

-- Add a separator line
dgsMenuAddSeparator(menu)

-- Add more items after the separator
local item3 = dgsMenuAddItem(menu, "Save", "file.save")
local item4 = dgsMenuAddItem(menu, "Save As", "file.saveas")

-- Add another separator
dgsMenuAddSeparator(menu)

-- Add exit item
local item5 = dgsMenuAddItem(menu, "Exit", "file.exit")

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

### Example 2: Text Separator

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with text separators (wider menu for better text visibility)
local menu = dgsCreateMenu(200, 200, 300, 250, false)

-- Add file operations
local item1 = dgsMenuAddItem(menu, "New", "file.new")
local item2 = dgsMenuAddItem(menu, "Open", "file.open")
local item3 = dgsMenuAddItem(menu, "Save", "file.save")

-- Add a text separator
dgsMenuAddSeparator(menu, "--- Edit Operations ---")

-- Add edit operations
local item4 = dgsMenuAddItem(menu, "Copy", "edit.copy")
local item5 = dgsMenuAddItem(menu, "Paste", "edit.paste")
local item6 = dgsMenuAddItem(menu, "Cut", "edit.cut")

-- Add another text separator
dgsMenuAddSeparator(menu, "--- View Options ---")

-- Add view operations
local item7 = dgsMenuAddItem(menu, "Zoom In", "view.zoomin")
local item8 = dgsMenuAddItem(menu, "Zoom Out", "view.zoomout")

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

### Example 3: Separator with Position and Parent Item

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with nested items and separators
local menu = dgsCreateMenu(200, 200, 200, 200, false)

-- Add main menu items
local fileItem = dgsMenuAddItem(menu, "File", "file")
local editItem = dgsMenuAddItem(menu, "Edit", "edit")

-- Add items to the File submenu
local newItem = dgsMenuAddItem(menu, "New", "file.new", fileItem)
local openItem = dgsMenuAddItem(menu, "Open", "file.open", fileItem)

-- Add a separator in the File submenu at position 3
local separatorID = dgsMenuAddSeparator(menu, nil, fileItem, 3)

-- Add more items to the File submenu
local saveItem = dgsMenuAddItem(menu, "Save", "file.save", fileItem)
local exitItem = dgsMenuAddItem(menu, "Exit", "file.exit", fileItem)

-- Add another separator with text in the File submenu
dgsMenuAddSeparator(menu, "Recent Files", fileItem)

-- Add recent file items
local recent1 = dgsMenuAddItem(menu, "document1.txt", "file.recent1", fileItem)
local recent2 = dgsMenuAddItem(menu, "document2.txt", "file.recent2", fileItem)

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

### Example 4: Context Menu with Separators

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a context menu that appears on right-click
local contextMenu = dgsCreateMenu(200, 200, 180, 150, false)

-- Add context menu items
local cutItem = dgsMenuAddItem(contextMenu, "Cut", "cut")
local copyItem = dgsMenuAddItem(contextMenu, "Copy", "copy")
local pasteItem = dgsMenuAddItem(contextMenu, "Paste", "paste")

-- Add separator
dgsMenuAddSeparator(contextMenu)

-- Add more options
local selectAllItem = dgsMenuAddItem(contextMenu, "Select All", "selectall")

-- Add separator with text
dgsMenuAddSeparator(contextMenu, "Properties")

-- Add properties item
local propertiesItem = dgsMenuAddItem(contextMenu, "Item Properties", "properties")

-- Create a button that shows the context menu
local button = dgsCreateButton(400, 400, 200, 50, "Right Click Me", false)

addEventHandler("onDgsMouseClickUp", button, function(mouseButton)
    if mouseButton == "right" then
        local x, y = dgsGetCursorPosition()
        dgsMenuShow(contextMenu, x, y)
    end
end)

-- Handle context menu selections
addEventHandler("onDgsMenuSelect", contextMenu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end
    
    local command = dgsMenuGetItemCommand(source, uniqueID)
    outputChatBox("Context action: " .. command)
    dgsMenuHide(source)
end, false)
```

## See Also

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuRemoveItem](mta://scripting/client/functions/dgsmenuremoveitem.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [dgsMenuShow](mta://scripting/client/functions/dgsmenushow.md)

- [dgsMenuHide](mta://scripting/client/functions/dgsmenuhide.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
