---
doc_id: "mta-wiki:1589"
title: "TextItemGetColor"
source_title: "TextItemGetColor"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemGetColor"
revision_id: 78448
language: "en"
categories: ["Server_functions"]
---

# TextItemGetColor

This function allows you to retrieve the color of a text item.

## Syntax

```
int int int int textItemGetColor ( textitem theTextItem )
```

### Required Arguments

- **theTextItem:** The text item you wish to retrieve the color of.

### Returns

Returns four integers in RGBA format, with a maximum value of 255 for each. The values are, in order, *red*, *green*, *blue*, and *alpha*. Alpha decides transparency where 255 is opaque and 0 is transparent. *false* is returned if the text item is invalid.

## Example

This example gets the color of a text item named 'theTextItem' and if it is green, changes it to blue.

```
local r,g,b,a = textItemGetColor ( theTextItem )           -- get the text color and store it in the variables 'r','g','b' and 'a'
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

- textItemGetColor

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
