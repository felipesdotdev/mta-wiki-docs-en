---
doc_id: "mta-wiki:2330"
title: "IsCursorShowing"
source_title: "IsCursorShowing"
source_url: "https://wiki.multitheftauto.com/wiki/IsCursorShowing"
revision_id: 82128
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:54.144416+00:00"
---

# IsCursorShowing

This function determines the state of a player's cursor.

| [[{{{image}}}\|link=\|]] | Note: This function only handles the cursor state set by the showCursor function, ignoring it if the console, chatbox, or menu is open. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: If you use this function on the server-side, keep in mind that it only detects the showCursor function executed on the server-side and does not detect the function executed on the client-side. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool isCursorShowing ( player playerElement )
```

### Required Arguments

- **playerElement:** The [player](mta://reference/misc/player.md) from whom we want to retrieve the cursor state.

Click to collapse [-]
Client

```
bool isCursorShowing ( )
```

On the client-side, this function doesn't require any arguments because it gets the cursor state of the [localPlayer](mta://scripting/client/functions/localplayer.md).

### Returns

Returns *true* if the player's cursor is visible, and *false* if it is not.

## Example

Click to collapse [-]
Server (Simple)

This example creates a function to set the state of the player's cursor using the [showCursor](mta://scripting/shared/functions/showcursor.md) function.

```
function toggleCursor(playerElement)
    if playerElement and isElement(playerElement) then -- Check whether the given element exists
        local cursorState = isCursorShowing(playerElement) -- Retrieve the state of the player's cursor
        local cursorStateOpposite = not cursorState -- The logical opposite of the cursor state

        showCursor(playerElement, cursorStateOpposite) -- Setting the new cursor state
    end
end
```

Click to collapse [-]
Server (Complex)

This example creates a function that gets the state of the player's cursor and outputs it to the chatbox using the [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) function.

```
function outputCursor(playerElement)
    if playerElement and isElement(playerElement) then -- Check whether the given element exists
        local cursorState = isCursorShowing(playerElement) -- Retrieve the state of the player's cursor
        local cursorStateText = cursorState and "visible" or "hidden" -- Calculate the context from the boolean variable.

        outputChatBox("Your cursor is " .. cursorStateText .. ".", playerElement) -- Output the text in the chatbox according to the cursor state.
    end
end
```

Click to collapse [-]
Client (Simple)

This example creates a function to set the state of the player's cursor using the [showCursor](mta://scripting/shared/functions/showcursor.md) function.

```
function toggleCursor()
    local cursorState = isCursorShowing() -- Retrieve the state of the player's cursor
    local cursorStateOpposite = not cursorState -- The logical opposite of the cursor state

    showCursor(cursorStateOpposite) -- Setting the new cursor state
end
```

If you are already advanced in scripting, using this code is recommended, as it is much more compact:

```
function toggleCursor()
    showCursor(not isCursorShowing())
end
```

Click to collapse [-]
Client (Complex)

This example creates a function that allows the player to change the state of the cursor using the [showCursor](mta://scripting/shared/functions/showcursor.md) and [bindKey](mta://scripting/shared/functions/bindkey.md) functions.

```
function toggleCursor()
    local cursorState = isCursorShowing() -- Retrieve the state of the player's cursor
    local cursorStateOpposite = not cursorState -- The logical opposite of the cursor state

    showCursor(cursorStateOpposite) -- Setting the new cursor state
end

bindKey("m", "down", toggleCursor) -- Assigning our toggleCursor function to the 'm' key press.
```

If you are already advanced in scripting, using this code is recommended, as it is much more compact:

```
bindKey("m", "down",
    function()
        showCursor(not isCursorShowing())
    end
)
```

## See Also

- isCursorShowing

- [showCursor](mta://scripting/shared/functions/showcursor.md)
