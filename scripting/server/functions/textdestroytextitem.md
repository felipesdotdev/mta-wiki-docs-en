---
doc_id: "mta-wiki:1582"
title: "TextDestroyTextItem"
source_title: "TextDestroyTextItem"
source_url: "https://wiki.multitheftauto.com/wiki/TextDestroyTextItem"
revision_id: 10352
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.843654+00:00"
---

# TextDestroyTextItem

This function destroys a [textitem](mta://reference/misc/textitem.md) object.

## Syntax

```
void textDestroyTextItem ( textitem theTextitem )
```

### Required Arguments

- **theTextitem:** The text item you wish to destroy.

## Example

This example creates then destroys a [textitem](mta://reference/misc/textitem.md).

```
-- Create a new text item
text = textCreateTextItem ( "Hello, world!" )
-- Destroy it
textDestroyTextItem ( text )
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- textDestroyTextItem

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

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
