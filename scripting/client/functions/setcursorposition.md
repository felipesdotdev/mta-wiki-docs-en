---
doc_id: "mta-wiki:4309"
title: "SetCursorPosition"
source_title: "SetCursorPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetCursorPosition"
revision_id: 81003
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:39.198427+00:00"
---

# SetCursorPosition

This function sets the current position of the mouse cursor.

## Syntax

```
bool setCursorPosition ( int cursorX, int cursorY )
```

### Required Arguments

- **cursorX:** Position over the X axis

- **cursorY:** Position over the Y axis

### Returns

Returns *true* if the position has been successfully set, *false* otherwise.

## Example

This example sets your cursor position to the center of your screen after using the command *cursorpos*.

```
function centerCursorFunction()
    local showing = isCursorShowing ()
    if showing then -- if the cursor is showing
        local screenX, screenY = guiGetScreenSize () --get the screen size in pixels
        setCursorPosition (screenX/2, screenY/2) --set the cursor position to the center of the screen
    else
        outputChatBox( "Your cursor is not showing." )
    end
end
addCommandHandler( "cursorpos", centerCursorFunction )
```

## See Also

- [getCursorAlpha](mta://scripting/client/functions/getcursoralpha.md)

- [getCursorPosition](mta://scripting/client/functions/getcursorposition.md)

- [setCursorAlpha](mta://scripting/client/functions/setcursoralpha.md)

- setCursorPosition
  

- **Shared**

- [isCursorShowing](mta://scripting/shared/functions/iscursorshowing.md)

- [showCursor](mta://scripting/shared/functions/showcursor.md)
