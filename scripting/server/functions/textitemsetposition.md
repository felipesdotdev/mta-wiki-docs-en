---
doc_id: "mta-wiki:1586"
title: "TextItemSetPosition"
source_title: "TextItemSetPosition"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemSetPosition"
revision_id: 78445
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:58.049235+00:00"
---

# TextItemSetPosition

This function allows the setting of the position of a text item.

## Syntax

```
bool textItemSetPosition ( textitem theTextItem, float x, float y )
```

### Required Arguments

- **theTextItem:** The text item that you want to move

- **x:** A floating point number between 0.0 and 1.0 indicating how far across the screen the text should be shown, as a percentage of the width, from the left hand side.

- **y:** A floating point number between 0.0 and 1.0 indicating how far down the screen the text should be shown, as a percentage of the height, from the top.

### Returns

Returns *true* if the position was successfully set, *false* otherwise.

## Example

This example creates a text item 'myTextItem' only if the text item 'otherTextItem' is not in the same position, to prevent overlap. If it is in the same position, then it moves it down.

```
myDisplay = textCreateDisplay ( )                    -- create a text display
textDisplayAddObserver ( myDisplay, myPlayer )      -- make it visible to the player
x,y = textItemGetPosition ( otherTextItem )         -- get the position of 'otherTextItem'
if ( x == 0.5 ) and ( y == 0.5 ) then               -- if the x and y of the text item are in the middle
    textItemSetPosition ( otherTextItem, 0.5, 0.6 ) -- move otherTextItem down
end 
myTextItem = textCreateTextItem ( "Hello world!", 0.5, 0.5 ) -- create a new text item in the middle saying "Hello world"
textDisplayAddText ( myDisplay, myTextItem )        -- and add it to the text display
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

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- textItemSetPosition

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
