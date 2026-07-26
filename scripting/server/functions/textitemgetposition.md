---
doc_id: "mta-wiki:1587"
title: "TextItemGetPosition"
source_title: "TextItemGetPosition"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemGetPosition"
revision_id: 78446
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.974781+00:00"
---

# TextItemGetPosition

This function allows retrieval of the position of a text item.

## Syntax

```
float float textItemGetPosition ( textitem theTextItem )
```

### Required Arguments

- **theTextItem:** The textitem you wish to retrieve the position of

### Returns

Returns two floats of the *x* and *y* position on the screen, where the maximum value is 1.0.

## Example

This example creates a text item 'myTextItem' only if the text item 'otherTextItem' is not in the same position, to prevent overlap.  If it is in the same position, then it moves it down.

```
function MyTestTextFunction ()
myDisplay = textCreateDisplay ( )                   -- create a text display
textDisplayAddObserver ( myDisplay, myPlayer )      -- make it visible to the player
x,y = textItemGetPosition ( otherTextItem )         -- get the position of 'otherTextItem'
if ( x == 0.5 ) and ( y == 0.5 ) then               -- if the x and y of the text item are in the middle
    textItemSetPosition ( otherTextItem, 0.5, 0.6 ) -- move otherTextItem down
end 
myTextItem = textCreateTextItem ( "Hello world!", 0.5, 0.5 ) -- create a new textitem in the middle saying "Hello world"
textDisplayAddText ( myDisplay, myTextItem )                 -- and add it to the text display
end
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

- [textDisplayRemoveText](mta://scripting/server/functions/textdisplayremovetext.md)

- [textItemGetColor](mta://scripting/server/functions/textitemgetcolor.md)

- textItemGetPosition

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
