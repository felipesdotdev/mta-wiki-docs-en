---
doc_id: "mta-wiki:5466"
title: "OnClientGUIFocus"
source_title: "OnClientGUIFocus"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIFocus"
revision_id: 82081
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.721205+00:00"
---

# OnClientGUIFocus

This event is triggered each time a GUI element gains input focus (mainly useful for windows, editboxes and memos but triggered for all GUI elements nevertheless).

| [[{{{image}}}\|link=\|]] | Note: When a widget in a window that didn't have focus before receives focus, onClientGUIFocus is triggered first for the window and then for the child widget. When the window already had focus, onClientGUIFocus is only triggered for the newly focused child widget. |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the GUI element which just gained input focus.

## Example

```
local window, editbox = nil, nil
addCommandHandler("example",
function()
	local screenWidth, screenHeight = guiGetScreenSize()
	local windowWidth, windowHeight = 263, 90
	local left = screenWidth/2 - windowWidth/2
	local top = screenHeight/2 - windowHeight/2
	window = guiCreateWindow(left, top, windowWidth, windowHeight, "Example Window", false)		
	editbox = guiCreateEdit(11, 41, 241, 22, "", false, window)
	addEventHandler("onClientGUIFocus", editbox, onClientGUIFocus_editbox, true) --true because for the example we want propagated events
	addEventHandler("onClientGUIBlur", editbox, onClientGUIBlur_editbox, true) --true because for the example we want propagated events
	showCursor(true)
end)

function onClientGUIFocus_editbox()
	if source == editbox then
		outputChatBox("Example editBox received input focus")
	elseif source == window then
		outputChatBox("Example window received input focus")
	end
end

function onClientGUIBlur_editbox()
	if source == editbox then
		outputChatBox("Example editBox lost input focus")
	elseif source == window then
		outputChatBox("Example window lost input focus")
	end
end
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- [onClientCursorMove](mta://scripting/client/events/onclientcursormove.md)

- [onClientDoubleClick](mta://scripting/client/events/onclientdoubleclick.md)

- [onClientKey](mta://scripting/client/events/onclientkey.md)

- [onClientPaste](mta://scripting/client/events/onclientpaste.md)

### GUI

- [onClientGUIAccepted](mta://scripting/client/events/onclientguiaccepted.md)

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md)

- [onClientGUIComboBoxAccepted](mta://scripting/client/events/onclientguicomboboxaccepted.md)

- [onClientGUIDoubleClick](mta://scripting/client/events/onclientguidoubleclick.md)

- onClientGUIFocus

- [onClientGUIMouseDown](mta://scripting/client/events/onclientguimousedown.md)

- [onClientGUIMouseUp](mta://scripting/client/events/onclientguimouseup.md)

- [onClientGUIMove](mta://scripting/client/events/onclientguimove.md)

- [onClientGUIScroll](mta://scripting/client/events/onclientguiscroll.md)

- [onClientGUISize](mta://scripting/client/events/onclientguisize.md)

- [onClientGUITabSwitched](mta://scripting/client/events/onclientguitabswitched.md)

- [onClientMouseEnter](mta://scripting/client/events/onclientmouseenter.md)

- [onClientMouseLeave](mta://scripting/client/events/onclientmouseleave.md)

- [onClientMouseMove](mta://scripting/client/events/onclientmousemove.md)

- [onClientMouseWheel](mta://scripting/client/events/onclientmousewheel.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
