---
doc_id: "mta-wiki:14574"
title: "DgsMenuSetItemText"
source_title: "DgsMenuSetItemText"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuSetItemText"
revision_id: 82207
language: "en"
categories: ["Client_functions"]
---

# DgsMenuSetItemText

This function changes the displayed text of an existing menu item.

## Syntax

```
bool dgsMenuSetItemText ( element menu, int uniqueID, string text )
```

### Required Arguments

- **menu:** The DGS menu element containing the item

- **uniqueID:** The unique ID of the menu item (returned by [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md))

- **text:** The new text to display for this menu item

### Returns

Returns *true* if the text was set successfully, *false* otherwise.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu with a toggle option
local menu = dgsCreateMenu(200, 200, 160, 120, false)
dgsMenuAddItem(menu, "Start Game", "start")
local soundItem = dgsMenuAddItem(menu, "Sound: ON", "toggle_sound")
dgsMenuAddItem(menu, "Exit", "exit")

-- Show the menu
dgsMenuShow(menu)

-- Track sound state
local soundEnabled = true

-- Handle menu selections
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end

    local command = dgsMenuGetItemCommand(source, uniqueID)
    if command == "start" then
        outputChatBox("Starting game...")
    elseif command == "toggle_sound" then
        -- Toggle sound state and update menu text
        soundEnabled = not soundEnabled
        if soundEnabled then
            dgsMenuSetItemText(source, soundItem, "Sound: ON")
            outputChatBox("Sound enabled")
        else
            dgsMenuSetItemText(source, soundItem, "Sound: OFF")
            outputChatBox("Sound disabled")
        end
        return -- Don't hide menu for toggle
    elseif command == "exit" then
        dgsMenuHide(source)
        return
    end

    dgsMenuHide(source)
end, false)
```

## See Also

- [dgsMenuGetItemText](mta://scripting/client/functions/dgsmenugetitemtext.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemCommand](mta://scripting/client/functions/dgsmenusetitemcommand.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
