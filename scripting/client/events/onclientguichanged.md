---
doc_id: "mta-wiki:2572"
title: "OnClientGUIChanged"
source_title: "OnClientGUIChanged"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIChanged"
revision_id: 67070
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.569464+00:00"
---

# OnClientGUIChanged

This event is fired when a [memo](mta://scripting/concepts/element-gui-memo.md) or an [editbox](mta://scripting/concepts/element-gui-edit-field.md) has changed (either by the user or by [guiSetText](mta://scripting/client/functions/guisettext.md)).

## Parameters

```
element theElement
```

- **theElement**: The GUI [element](mta://reference/misc/element.md) which was changed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the element which was changed.

## Example

This example creates an editbox and prints a message when it has changed

```
editBox = guiCreateEdit(0.3,0.1,0.4,0.1,"",true)
addEventHandler("onClientGUIChanged", editBox, function(element) 
   outputChatBox("The box now reads: " .. guiGetText(element))
end)
```

Or

```
editBox = guiCreateEdit(0.3,0.1,0.4,0.1,"",true)
addEventHandler("onClientGUIChanged", editBox, function() 
   outputChatBox("The box now reads: " .. guiGetText(source))
end)
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

- onClientGUIChanged

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
