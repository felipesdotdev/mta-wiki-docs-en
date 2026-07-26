---
doc_id: "mta-wiki:5467"
title: "OnClientGUIBlur"
source_title: "OnClientGUIBlur"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIBlur"
revision_id: 82078
language: "en"
categories: ["Client_events"]
---

# OnClientGUIBlur

This event is triggered each time a GUI element looses input focus (mainly useful for windows, editboxes and memos but triggered for all GUI elements nevertheless).

| [[{{{image}}}\|link=\|]] | Note: When the focus is transfered from one GUI element to an other, it is guaranteed that onClientGUIBlur on the element that lost focus is triggered before onClientGUIFocus on the element that just gained focus |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: When the focus of a full window is lost (transfered to an other window or lost), onClientGUIBlur is only triggered for the window itself even if one of its widgets had focus too. It's important in this case to use the 4th parameter of addEventHandler if you are only registered for the events of a child widget (cf. Example) |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: When a window is hidden with guiSetVisible , it (or its child widget having focus) keeps focus internally until an other window gains focus or the chatbox is used |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the GUI element which just lost input focus.

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

- onClientGUIBlur

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md)

- [onClientGUIComboBoxAccepted](mta://scripting/client/events/onclientguicomboboxaccepted.md)

- [onClientGUIDoubleClick](mta://scripting/client/events/onclientguidoubleclick.md)

- [onClientGUIFocus](mta://scripting/client/events/onclientguifocus.md)

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
