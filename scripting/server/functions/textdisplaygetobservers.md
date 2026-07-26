---
doc_id: "mta-wiki:4641"
title: "TextDisplayGetObservers"
source_title: "TextDisplayGetObservers"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayGetObservers"
revision_id: 31093
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.896416+00:00"
---

# TextDisplayGetObservers

This function can be used to retrieve all the [players](mta://reference/misc/player.md)  currently observing a specified [textdisplay](mta://reference/misc/textdisplay.md).

## Syntax

```
table textDisplayGetObservers ( textdisplay theDisplay )
```

### Required Arguments

- **theDisplay**: The [textdisplay](mta://reference/misc/textdisplay.md) of which observers you want to get.

### Returns

Returns a [table](mta://reference/misc/table.md) of players that are observers of the display or *false* if invalid textdisplay is passed.

## Example

```
function removeAllObservers ( player , command )
	local tObservers = textDisplayGetObservers ( serverDisplay ) -- get a table of all observers in 'serverDisplay' text display
	if tObservers then -- if got the table
		for index,player in ipairs ( tObservers ) do -- loop the table
			textDisplayRemoveObserver ( serverDisplay , player ) -- remove the player from the text display
		end
	end
end
addCommandHandler("removeAllObservers",removeAllObservers)
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- textDisplayGetObservers

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
