---
doc_id: "mta-wiki:7076"
title: "GetCursorAlpha"
source_title: "GetCursorAlpha"
source_url: "https://wiki.multitheftauto.com/wiki/GetCursorAlpha"
revision_id: 81180
language: "en"
categories: ["Client_functions"]
---

# GetCursorAlpha

This function is used to get the client's cursor alpha (transparency).

## Syntax

```
int getCursorAlpha ( )
```

 

example of cursor alpha

### Returns

Returns a [int](mta://reference/misc/int.md) between 0 and 255, where 255 is fully opaque and 0 is fully transparent.

## Example

```
-- Simple command to test the getCursorAlpha function
addCommandHandler( "cursorAlpha", 
    function ()
        if ( isCursorShowing ( ) ) then
            outputChatBox( "The cursor alpha: "..getCursorAlpha( ) )
        else
            outputChatBox( "The cursor is not showing!" )
        end
    end
)
```

## See Also

- getCursorAlpha

- [getCursorPosition](mta://scripting/client/functions/getcursorposition.md)

- [setCursorAlpha](mta://scripting/client/functions/setcursoralpha.md)

- [setCursorPosition](mta://scripting/client/functions/setcursorposition.md)
  

- **Shared**

- [isCursorShowing](mta://scripting/shared/functions/iscursorshowing.md)

- [showCursor](mta://scripting/shared/functions/showcursor.md)
