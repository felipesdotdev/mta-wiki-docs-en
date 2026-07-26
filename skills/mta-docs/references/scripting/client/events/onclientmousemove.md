---
doc_id: "mta-wiki:3922"
title: "OnClientMouseMove"
source_title: "OnClientMouseMove"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientMouseMove"
revision_id: 55075
language: "en"
categories: ["Client_events"]
---

# OnClientMouseMove

This event is triggered each time the user moves the mouse on top of a GUI element.

## Parameters

```
int absoluteX, int absoluteY
```

- **absoluteX**:  the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY**:  the Y position of the mouse cursor, in pixels, measured from the top of the screen.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the GUI element on which the mouse was moved.

## Example

This example creates a text label at the bottom of the screen that tells player the position of mouse when moved on top of a "TEST WINDOW" (the gui element).

```
addEventHandler( "onClientResourceStart", getResourceRootElement( ),
    function ( )
        guiCreateWindow( 10, 200, 200, 150, "TEST WINDOW", false );
        textLabel = guiCreateLabel( 0, .9, 1, .1, "", true );
        guiLabelSetHorizontalAlign( textLabel, "center" );
    end
);

addEventHandler( "onClientMouseMove", getRootElement( ),
    function ( x, y )
        if source then
            if not guiGetVisible( textLabel ) then guiSetVisible( textLabel, true ) end
            guiSetText( textLabel, "X: " .. tostring( x ) .. ";  Y: ".. tostring( y ) )
        else
            guiSetVisible( textLabel, false );
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

- onClientMouseMove

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
