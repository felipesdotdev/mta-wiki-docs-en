---
doc_id: "mta-wiki:2331"
title: "ShowCursor"
source_title: "ShowCursor"
source_url: "https://wiki.multitheftauto.com/wiki/ShowCursor"
revision_id: 82009
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
---

# ShowCursor

This function is used to show or hide a [player](https://wiki.multitheftauto.com/index.php?search=player)'s cursor.

| [[{{{image}}}\|link=\|]] | Note: Regardless of the cursor state you set using this function, the cursor will always be visible while the menu, the chatbox input line or the console are active, or if another resource has called this function. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Be aware of that if showCursor enbaled by a resource you can't disabled it from a different ressource showCursor(false) will not works, in order to make it works, disable it from the original resource that enabled it or use export |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool showCursor ( player thePlayer, bool show, [ bool toggleControls = true ] )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you want to show or hide the cursor of.

- **show:** A boolean value determining whether to show (*true*) or hide (*false*) the cursor.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **toggleControls:** A boolean value determining whether to disable controls whilst the cursor is showing.  *true* implies controls are disabled, *false* implies controls remain enabled.

Click to collapse [-]
Client

```
bool showCursor ( bool show, [ bool toggleControls = true ]  )
```

### Required Arguments

- **show:** A boolean value determining whether to show (*true*) or hide (*false*) the cursor.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **toggleControls:** A boolean value determining whether to disable controls whilst the cursor is showing.  *true* implies controls are disabled, *false* implies controls remain enabled.

### Returns

Returns *true* if the player's cursor was shown or hidden successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

This example shows the cursor for a player named "Dave", then outputs a message if it was shown successfully.

```
local thePlayer = getPlayerFromName ( "Dave" )              -- get the player named Dave
if thePlayer then                                           -- if we got him
    showCursor ( thePlayer, true )                          -- make his cursor show
    if isCursorShowing ( thePlayer ) then                   -- did it show?
        outputChatBox ( "Cursor is now showing for Dave." ) -- print a message to the chat box
    end
end
```

Click to collapse [-]
Client

This example shows the cursor all the time

```
showCursor ( true ) -- Shows cursor
showCursor ( false ) -- Doesnt Show Cursor
```

## See Also

- [isCursorShowing](mta://scripting/shared/functions/iscursorshowing.md)

- showCursor
