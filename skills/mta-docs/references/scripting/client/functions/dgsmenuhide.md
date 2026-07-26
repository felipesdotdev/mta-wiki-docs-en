---
doc_id: "mta-wiki:14570"
title: "DgsMenuHide"
source_title: "DgsMenuHide"
source_url: "https://wiki.multitheftauto.com/wiki/DgsMenuHide"
revision_id: 82206
language: "en"
categories: ["Client_functions"]
---

# DgsMenuHide

This function hides a DGS menu and cleans up any associated submenus.

## Syntax

```
bool dgsMenuHide ( element menu )
```

### Required Arguments

- **menu:** The DGS menu element to hide

### Returns

Returns *true* if the menu was hidden successfully, *false* otherwise.

## Examples

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a menu
local menu = dgsCreateMenu(200, 200, 150, 120, false)
dgsMenuAddItem(menu, "New File", "new")
dgsMenuAddItem(menu, "Open File", "open")
dgsMenuAddSeparator(menu)
dgsMenuAddItem(menu, "Exit", "exit")

-- Show the menu
dgsMenuShow(menu)

-- Handle menu selection
addEventHandler("onDgsMenuSelect", menu, function(subMenu, uniqueID)
    if uniqueID == -1 then return end

    local command = dgsMenuGetItemCommand(source, uniqueID)
    if command == "exit" then
        dgsMenuHide(source)
        outputChatBox("Menu closed!")
    else
        outputChatBox("Selected: " .. command)
    end
end, false)
```

## Notes

| [[{{{image}}}\|link=\|]] | Note: This function automatically cleans up submenus and removes focus from the menu |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Menus are automatically hidden when losing focus if autoHide property is enabled (default) |
| --- | --- |
|  |  |

## See Also

- [dgsMenuShow](mta://scripting/client/functions/dgsmenushow.md)

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [dgsMenuClean](https://wiki.multitheftauto.com/index.php?title=DgsMenuClean&action=edit&redlink=1)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).
