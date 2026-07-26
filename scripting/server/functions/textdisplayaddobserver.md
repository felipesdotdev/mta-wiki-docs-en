---
doc_id: "mta-wiki:1305"
title: "TextDisplayAddObserver"
source_title: "TextDisplayAddObserver"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayAddObserver"
revision_id: 40111
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.860072+00:00"
---

# TextDisplayAddObserver

This function adds a [player](mta://reference/misc/player.md) as an observer of a [textdisplay](mta://reference/misc/textdisplay.md). This allows the [player](mta://reference/misc/player.md) to see any [textitems](mta://reference/misc/textitem.md) that the [textdisplay](mta://reference/misc/textdisplay.md) contains.

## Syntax

```
void textDisplayAddObserver ( textdisplay display, player playerToAdd )
```

### Required Arguments

- **display**: The [textdisplay](mta://reference/misc/textdisplay.md) to add the [player](mta://reference/misc/player.md) to as an observer.

- **playerToAdd**: The [player](mta://reference/misc/player.md) that should observe the [textdisplay](mta://reference/misc/textdisplay.md).

## Example

```
function MyTestTextFunction ()
display = textCreateDisplay ()                 -- create a new display, store the reference in a variable called display
textDisplayAddObserver ( display, thePlayer )  -- add an observer to it
text = textCreateTextItem ( "Hello World", 0.5, 0.5, "medium", 255, 0, 0, 255, 2, "left", "top", 255) --red text of 24pt at the center of your screen
textDisplayAddText ( display, text )           -- Add the text item to the text display
end
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- textDisplayAddObserver

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

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
