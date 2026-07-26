---
doc_id: "mta-wiki:1636"
title: "TextDisplayRemoveObserver"
source_title: "TextDisplayRemoveObserver"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayRemoveObserver"
revision_id: 27195
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.929398+00:00"
---

# TextDisplayRemoveObserver

This function removes a [player](mta://reference/misc/player.md) observer of a [textdisplay](mta://reference/misc/textdisplay.md). This stops the [player](mta://reference/misc/player.md) from being able to see [textitems](mta://reference/misc/textitem.md) that the [textdisplay](mta://reference/misc/textdisplay.md) contains.

## Syntax

```
bool textDisplayRemoveObserver ( textdisplay display, player playerToRemove )
```

### Required Arguments

- **display**: The [textdisplay](mta://reference/misc/textdisplay.md) to remove the [player](mta://reference/misc/player.md) from as an observer.

- **playerToRemove**: The [player](mta://reference/misc/player.md) that should be removed from the [textdisplay](mta://reference/misc/textdisplay.md).

## Example

This example creates a new display and a "Hello World" text item for a player.  It then removes it from his screen 5 seconds later

```
display = textCreateDisplay ( ) --create the display
textDisplayAddObserver ( display, thePlayer ) --add an observer
newtextitem = textCreateTextItem ( "Hello World", 0.5, 0.5, "low", 255, 0, 0, 0, 1.0 ) --create our "Hello World" text item
textDisplayAddText ( display, newtextitem ) --add this to the display
setTimer ( textDisplayRemoveObserver, 5000,1, display, thePlayer ) --set a timer to remove this 5 seconds later.
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

- textDisplayRemoveObserver

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
