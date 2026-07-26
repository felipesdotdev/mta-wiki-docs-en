---
doc_id: "mta-wiki:1591"
title: "TextItemGetPriority"
source_title: "TextItemGetPriority"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemGetPriority"
revision_id: 78450
language: "en"
categories: ["Server_functions", "Needs_Example"]
generated_at: "2026-07-26T16:16:57.990831+00:00"
---

# TextItemGetPriority

|  | Script Example Missing Function TextItemGetPriority needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function retrieves the priority of a text item.  Priority defines the rate at whihc a text item is updated

## Syntax

```
int textItemGetPriority ( textitem textitemToCheck )
```

### Required Arguments

- **textitemToCheck:** The text item you wish to retrieve the priority of.

### Returns

Returns a integer of the priority of a text item, 0 = low, 1 = medium, 2 = high.

## Example

This page does not have an example.

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

- textItemGetPriority

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
