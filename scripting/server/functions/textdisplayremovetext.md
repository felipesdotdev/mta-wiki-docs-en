---
doc_id: "mta-wiki:1637"
title: "TextDisplayRemoveText"
source_title: "TextDisplayRemoveText"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayRemoveText"
revision_id: 48004
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.946095+00:00"
---

# TextDisplayRemoveText

This function removes a [textitem](mta://reference/misc/textitem.md) from a [textdisplay](mta://reference/misc/textdisplay.md). This stops any observers of the [textdisplay](mta://reference/misc/textdisplay.md) from being able to see the [textitem](mta://reference/misc/textitem.md).

## Syntax

```
void textDisplayRemoveText ( textdisplay displayToRemoveFrom, textitem itemToRemove )
```

### Required Arguments

- **displayToRemoveFrom**: The [textdisplay](mta://reference/misc/textdisplay.md) to remove the [textitem](mta://reference/misc/textitem.md) from.

- **itemToRemove**: The [textitem](mta://reference/misc/textitem.md) to remove from the display.

## Example

This example creates a text display and adds a "Hello World" text item to it.  It then removes that text item 5 seconds later.

```
-- Create a text display.
myTextDisplay = textCreateDisplay ( )
-- Add a player as an observer, i.e. this player will see everything added to this display
textDisplayAddObserver ( myTextDisplay, aPlayer )
-- Create a new text item with the text 'Hello World' and a priority of 'low' and colored red.
myTextItem = textCreateTextItem ( "Hello World", 0.5, 0.5, "low", 255, 0, 0, 0, 1.0 )
-- Add the newly created text item to the display
textDisplayAddText ( myTextDisplay, myTextItem )
-- Remove the text item from the display
setTimer ( textDisplayRemoveText, 5000, 1, myTestDispay, myTextItem )
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- [textDisplayIsObserver](mta://scripting/server/functions/textdisplayisobserver.md)

- [textDisplayRemoveObserver](mta://scripting/server/functions/textdisplayremoveobserver.md)

- textDisplayRemoveText

- [textItemGetColor](mta://scripting/server/functions/textitemgetcolor.md)

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
