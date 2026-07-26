---
doc_id: "mta-wiki:4344"
title: "TextDisplayIsObserver"
source_title: "TextDisplayIsObserver"
source_url: "https://wiki.multitheftauto.com/wiki/TextDisplayIsObserver"
revision_id: 31092
language: "en"
categories: ["Server_functions"]
---

# TextDisplayIsObserver

This function checks if a player can see the specified [textdisplay](mta://reference/misc/textdisplay.md).

## Syntax

```
bool textDisplayIsObserver ( textdisplay display, player thePlayer )
```

### Required Arguments

- **display**: The [textdisplay](mta://reference/misc/textdisplay.md).

- **thePlayer**: The [player](https://wiki.multitheftauto.com/index.php?search=player).

### Returns

Return true if [textdisplay](mta://reference/misc/textdisplay.md) is showing, or false if not.

## Example

```
serverDisplay = textCreateDisplay()  -- create a text display
serverText = textCreateTextItem ( "Hello world!", 0.5, 0.5 ) -- create a text item for the display
textDisplayAddText ( serverDisplay, serverText )  -- add it to the display so it is displayed

function showTextDisplay ( player, command )
	local isObserver = textDisplayIsObserver ( serverDisplay , player ) -- check if he is already a observer in the server display
	if not isObserver then -- if he is not an observer
		textDisplayAddObserver ( serverDisplay, player ) -- make it visible to a player
	end
end
addCommandHandler( "showText", showTextDisplay )

function removeTextDisplay ( player , command )
	local isObserver = textDisplayIsObserver ( serverDisplay , player ) -- check if he is already a observer in the server display
	if isObserver then -- if he is an observer
		textDisplayRemoveObserver ( serverDisplay , player ) -- remove the player from display
	end
end
addCommandHandler( "removeText",removeTextDisplay)
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- textDisplayIsObserver

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
