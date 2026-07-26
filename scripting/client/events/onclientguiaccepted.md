---
doc_id: "mta-wiki:2573"
title: "OnClientGUIAccepted"
source_title: "OnClientGUIAccepted"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIAccepted"
revision_id: 55059
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.516968+00:00"
---

# OnClientGUIAccepted

This event is triggered when enter is pressed on an editbox.

## Parameters

```
element editBox
```

- **editBox**: the [editbox](mta://scripting/concepts/element-gui-edit-field.md) which had focus.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the editbox which enter was pressed on.

## Example

This example creates an editbox and prints a message when enter is pressed.

```
editBox = guiCreateEdit ( 0.3, 0.1, 0.4, 0.1, "", true )
addEventHandler( "onClientGUIAccepted", editBox,
    function( theElement ) 
        outputChatBox( guiGetText( theElement ) )
    end
)
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

- onClientGUIAccepted

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

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
