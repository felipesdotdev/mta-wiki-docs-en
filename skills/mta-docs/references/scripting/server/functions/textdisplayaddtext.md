---
doc_id: "mta-wiki:1304"
title: "TextDisplayAddText"
source_title: "TextDisplayAddText"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayAddText"
revision_id: 10854
language: "en"
categories: ["Server_functions"]
---

# TextDisplayAddText

This function adds a [textitem](mta://reference/misc/textitem.md) to a [textdisplay](mta://reference/misc/textdisplay.md). This allows any observers of the [textdisplay](mta://reference/misc/textdisplay.md) to see the [textitem](mta://reference/misc/textitem.md).

## Syntax

```
void textDisplayAddText ( textdisplay displayToAddTo, textitem itemToAdd )
```

### Required Arguments

- **displayToAddTo**: The [textdisplay](mta://reference/misc/textdisplay.md) to add the [textitem](mta://reference/misc/textitem.md) to.

- **itemToAdd**: The [textitem](mta://reference/misc/textitem.md) to add to the display.

## Example

```
-- Create a text display.
myTextDisplay = textCreateDisplay ()
-- Add a player as an observer, i.e. this player will see all text items that are on this display
textDisplayAddObserver ( myTextDisplay, aPlayer )
-- Create a new text item with the text 'Hello World' and a priority of 'low' and colored red.
myTextItem = textCreateTextItem ( "Hello World", 0.5, 0.5, "low", 255, 0, 0, 0, 1.0 )
-- Add the newly created text item to the display
textDisplayAddText ( myTextDisplay, myTextItem )
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- textDisplayAddText

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- [textDisplayIsObserver](mta://scripting/server/functions/textdisplayisobserver.md)

- [textDisplayRemoveObserver](mta://scripting/server/functions/textdisplayremoveobserver.md)

- [textDisplayRemoveText](mta://scripting/server/functions/textdisplayremovetext.md)

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
