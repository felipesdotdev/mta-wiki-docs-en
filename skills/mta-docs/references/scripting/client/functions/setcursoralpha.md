---
doc_id: "mta-wiki:7075"
title: "SetCursorAlpha"
source_title: "SetCursorAlpha"
source_url: "https://wiki.multitheftauto.com/wiki/SetCursorAlpha"
revision_id: 81179
language: "en"
categories: ["Client_functions"]
---

# SetCursorAlpha

This function is used to change alpha (transparency) from the client's cursor.

## Syntax

```
bool setCursorAlpha( int alpha )
```

 

example of cursor alpha

### Required Arguments

- **alpha**: The alpha value to set. Value can be 0-255, where 255 is fully opaque and 0 is fully transparent.

### Returns

Returns *true* if the new alpha value was set, or *false* otherwise.

## Example

```
-- Simple command to test the setCursorAlpha function
addCommandHandler( "cursorAlpha", 
    function ()
        -- Show the cursor if it is not showing or hide the cursor if it is
        showCursor( not isCursorShowing ( ) )
        -- Set the alpha to 100
        setCursorAlpha(100)
    end
)
```

## See Also

- [getCursorAlpha](mta://scripting/client/functions/getcursoralpha.md)

- [getCursorPosition](mta://scripting/client/functions/getcursorposition.md)

- setCursorAlpha

- [setCursorPosition](mta://scripting/client/functions/setcursorposition.md)
  

- **Shared**

- [isCursorShowing](mta://scripting/shared/functions/iscursorshowing.md)

- [showCursor](mta://scripting/shared/functions/showcursor.md)
