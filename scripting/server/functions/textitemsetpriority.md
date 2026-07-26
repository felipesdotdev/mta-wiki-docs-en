---
doc_id: "mta-wiki:1590"
title: "TextItemSetPriority"
source_title: "TextItemSetPriority"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemSetPriority"
revision_id: 78449
language: "en"
categories: ["Server_functions", "Needs_Example"]
generated_at: "2026-07-26T16:16:58.068241+00:00"
---

# TextItemSetPriority

|  | Script Example Missing Function TextItemSetPriority needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function sets the priority for a text item.  Priority is the importance of sending updated text to the client. The system is implemented as 3 queues, with the *high* queue being emptied before the *medium* queue is processed, and with one update sent per server frame. Hence, if you set all your text items to *medium* priority it has the same effect as if you set them all to *high* or *low*.

## Syntax

```
void textItemSetPriority ( textitem theTextItem, string priority )
```

### Required Arguments

- **theTextItem:** The text item you wish to set priority to.

- **priority:** The priority you wish to set to the item, which can be *"high"*, *"medium"*, or *"low"* respective of their priority.

## Example

This page does not have an example

```
--add an example here
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

- textItemSetPriority

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
