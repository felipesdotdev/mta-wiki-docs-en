---
doc_id: "mta-wiki:6737"
title: "OnClientGUIComboBoxAccepted"
source_title: "OnClientGUIComboBoxAccepted"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIComboBoxAccepted"
revision_id: 82022
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.657287+00:00"
---

# OnClientGUIComboBoxAccepted

This event is called when a [combobox](mta://scripting/concepts/element-gui-combobox.md) gets accepted.

## Parameters

```
element theElement
```

- **theElement:** the [combobox](mta://scripting/concepts/element-gui-combobox.md) that got accepted.

## Source

The source of this event is the GUI combo box that was accepted.

## Example

This example will set the memo text to the selected combobox item text.

```
Combo = guiCreateComboBox ( 0.20, 0.03, 0.25, 0.30, "Example", true )
Memo = guiCreateMemo( 10, 50, 500, 150, "", false)
addEventHandler ( "onClientGUIComboBoxAccepted", guiRoot,
    function ( comboBox )
        if ( comboBox == Combo ) then
            local item = guiComboBoxGetSelected ( Combo )
            local text = tostring ( guiComboBoxGetItemText ( Combo , item ) )
            if ( text ~= "" ) then
                 guiSetText ( Memo , text )
            end
        end
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

- [onClientGUIAccepted](mta://scripting/client/events/onclientguiaccepted.md)

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md)

- onClientGUIComboBoxAccepted

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
