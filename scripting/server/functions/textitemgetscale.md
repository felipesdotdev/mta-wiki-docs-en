---
doc_id: "mta-wiki:1585"
title: "TextItemGetScale"
source_title: "TextItemGetScale"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemGetScale"
revision_id: 78444
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:58.007917+00:00"
---

# TextItemGetScale

This function allows retrieval of the scale or size of a text item.

## Syntax

```
float textItemGetScale ( textitem theTextitem )
```

### Required Arguments

- **theTextitem:** The text item you wish to retrieve the scale of

### Returns

Returns a floating point of the scale of the text. 1.0 is around 12pt.

## Example

This example retrieves the scale of the 'theTextItem' text item, and if it is too small it enlarges it so it is more visible.

```
scale = textItemGetScale ( theTextitem )  -- get the scale of theTextItem and store it in the 'scale' variable
if scale < 0.5 then                       -- if the scale is smaller than 0.5
    textItemSetScale ( theTextItem, 1.0 ) -- then restore it to default size, 1.0.
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

- textItemGetScale

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
