---
doc_id: "mta-wiki:1584"
title: "TextItemSetScale"
source_title: "TextItemSetScale"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemSetScale"
revision_id: 78443
language: "en"
categories: ["Server_functions"]
---

# TextItemSetScale

This function allows the setting of the scale of a text item.

## Syntax

```
bool textItemSetScale ( textitem theTextitem, float scale )
```

### Required Arguments

- **theTextitem:** The text item you wish to set the scale of.

- **scale:** A floating point value indicating the scale of the text you wish to set to. 1.0 is around 12pt.

### Returns

Returns *true* if the scale was successfully set, *false* otherwise.

## Example

This example retrieves the scale of the *theTextitem* text item, and if it is too small it enlarges it so it is more visible.

```
local scale = textItemGetScale ( theTextItem )  --get the scale of theTextitem and define it as 'scale'
if (scale < 0.5) then --if the scale is smaller than 0.5
	textItemSetScale ( theTextItem, 1.0 ) --then restore it to default size, 1.0.
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

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- textItemSetScale

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
