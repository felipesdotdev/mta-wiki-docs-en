---
doc_id: "mta-wiki:1286"
title: "TextDestroyDisplay"
source_title: "TextDestroyDisplay"
source_url: "https://wiki.multitheftauto.com/wiki/TextDestroyDisplay"
revision_id: 13438
language: "en"
categories: ["Server_functions"]
---

# TextDestroyDisplay

This function destroys a text display and will unlink all the [textitems](mta://reference/misc/textitem.md) on it. This does not stop the textitems existing, but anyone who was observing the textitems through this display will stop seeing them.

## Syntax

```
bool textDestroyDisplay ( textdisplay display )
```

### Required Arguments

- **display:** This is the [textdisplay](mta://reference/misc/textdisplay.md) that you wish to have destroyed.

## Example

This example creates a display then destroys it again straight away.

```
myDisplay = textCreateDisplay ()
textDestroyDisplay ( myDisplay )
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- textDestroyDisplay

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

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
