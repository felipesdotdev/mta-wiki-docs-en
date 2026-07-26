---
doc_id: "mta-wiki:1285"
title: "TextCreateDisplay"
source_title: "TextCreateDisplay"
source_url: "https://wiki.multitheftauto.com/wiki/TextCreateDisplay"
revision_id: 25226
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.789348+00:00"
---

# TextCreateDisplay

A [text display](mta://reference/misc/textdisplay.md) is like a canvas that can contain many [items of text](mta://reference/misc/textitem.md). Each display can be seen by multiple observers (players) and each player can see multiple displays.

## Syntax

```
textdisplay textCreateDisplay()
```

## Required Arguments

*This function has no arguments.*

## Example

```
function showTextDisplay ( player, command )
   local serverDisplay = textCreateDisplay()                             -- create a text display
   textDisplayAddObserver ( serverDisplay, player )                      -- make it visible to a player
   local serverText = textCreateTextItem ( "Hello world!", 0.5, 0.5 )    -- create a text item for the display
   textDisplayAddText ( serverDisplay, serverText )                      -- add it to the display so it is displayed
end
addCommandHandler( "showText", showTextDisplay )
```

## See Also

- textCreateDisplay

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

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
