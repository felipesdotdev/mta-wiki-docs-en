---
doc_id: "mta-wiki:4654"
title: "OnClientGUIMouseDown"
source_title: "OnClientGUIMouseDown"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIMouseDown"
revision_id: 76382
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.744006+00:00"
---

# OnClientGUIMouseDown

This event is fired when the user clicks certain mouse button on a GUI element.

## Parameters

```
string button, int absoluteX, int absoluteY
```

- **button:** the name of the mouse button that the GUI element was clicked with, can be *left*, *right*, or *middle*.

- **absoluteX:** the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y position of the mouse cursor, in pixels, measured from the top of the screen.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the GUI element that was clicked.

## Example

This example show how to add very basic *click'n'drag* feature for GUI elements (only for those which parent element is gui-root)

```
addEventHandler( "onClientGUIMouseDown", root,
    function ( btn, x, y )
        if btn == "left" then
            clickedElement = source; -- store the clicked element in a global variable
            local elementPos = { guiGetPosition( source, false ) };
            offsetPos = { x - elementPos[ 1 ], y - elementPos[ 2 ] }; -- get the offset position
        end
    end
);

addEventHandler( "onClientGUIMouseUp", root,
    function ( btn, x, y )
        if btn == "left" then
            clickedElement = nil;
        end
    end
);

addEventHandler( "onClientCursorMove", root,
    function ( _, _, x, y )
        if clickedElement then
            guiSetPosition( clickedElement, x - offsetPos[ 1 ], y - offsetPos[ 2 ], false );
        end
    end
);
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

- onClientGUIMouseDown

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
