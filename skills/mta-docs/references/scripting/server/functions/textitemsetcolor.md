---
doc_id: "mta-wiki:1588"
title: "TextItemSetColor"
source_title: "TextItemSetColor"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemSetColor"
revision_id: 78447
language: "en"
categories: ["Server_functions"]
---

# TextItemSetColor

This function sets the color of a text item.

## Syntax

```
bool textItemSetColor ( textitem theTextItem, int r, int g, int b, int a )
```

### Required Arguments

- **theTextItem:** The textitem you wish to set the color of.

- **red:** The amount of red in the text item's color (0 - 255).

- **green:** The amount of green in the text item's color (0 - 255).

- **blue:** The amount of blue in the text item's color (0 - 255).

- **alpha:** The amount of alpha in the text item's color (0 - 255). Alpha decides transparency where 255 is opaque and 0 is transparent.

### Returns

Returns *true* if the color was successfully set, *false* otherwise.

## Example

This example gets the color of a textitem named 'theTextItem' and if it is green, changes it to blue.

```
r,g,b,a = textItemGetColor ( theTextItem )           -- get the text color and store it in the variables 'r', 'g', 'b' and 'a'
if ( r == 0 ) and ( g == 255 ) and ( b == 0 ) then   -- if the color is green
    textItemSetColor ( theTextItem, 0, 0, 255, 255 ) -- set it to blue
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

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- textItemSetColor

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
