---
doc_id: "mta-wiki:1583"
title: "TextItemGetText"
source_title: "TextItemGetText"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemGetText"
revision_id: 78442
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:58.021076+00:00"
---

# TextItemGetText

This function returns the current text of the specified [textitem](mta://reference/misc/textitem.md).

## Syntax

```
string textItemGetText ( textitem theTextitem )
```

### Required Arguments

- **theTextitem:** A valid [textitem](mta://reference/misc/textitem.md).

### Returns

Returns a [string](mta://reference/misc/string.md) containing the text if the function was successful, *false* otherwise.

## Example

Increment a score display. In real scripts it's of course better to keep a global 'score' variable which can be incremented directly.

```
function givePoint ( thePlayer )
    local scoretextitem = scoretextitems[thePlayer]    -- find the score text item that belongs to this player
    local score = textItemGetText ( scoretextitem )    -- read the text (a score number)
    score = tostring(tonumber(score) + 1)              -- convert to number, add 1, convert to text
    textItemSetText ( scoretextitem, score )           -- put the new score on the text item
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

- textItemGetText

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
