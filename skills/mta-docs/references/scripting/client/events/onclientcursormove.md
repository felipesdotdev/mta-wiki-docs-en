---
doc_id: "mta-wiki:2586"
title: "OnClientCursorMove"
source_title: "OnClientCursorMove"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientCursorMove"
revision_id: 82061
language: "en"
categories: ["Client_events"]
---

# OnClientCursorMove

This event is called by the root element whenever the cursor is moved over the screen, by the player. It returns information about the world coordinates as well as the screen coordinates of where the player moved the cursor.

The difference between this event and [onClientMouseMove](mta://scripting/client/events/onclientmousemove.md), is that the latter is actually called by GUI elements. This is to prevent double calling of onClientCursorMove, as onClientCursorMove is always called.

## Parameters

```
float cursorX, float cursorY, int absoluteX, int absoluteY, float worldX, float worldY, float worldZ
```

- **cursorX:** the relative X coordinate of the mouse cursor. 0 = left side of the screen, 1 = right side.

- **cursorY:** the relative Y coordinate of the mouse cursor. 0 = top of the screen, 1 = bottom.

- **absoluteX:** the X coordinate of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y coordinate of the mouse cursor, in pixels, measured from the top of the screen.

- **worldX:** the 3D in-game world X coordinate that the cursor is pointing at.

- **worldY:** the 3D in-game world Y coordinate that the cursor is pointing at.

- **worldZ:** the 3D in-game world Z coordinate that the cursor is pointing at.

## Source

The source of this event is the root element.

## Example

This example creates a text label at the bottom of the screen which displays the mouse position in pixels.

```
addEventHandler( "onClientResourceStart", resourceRoot,
    function ( )
        textLabel = guiCreateLabel( 0, .9, 1, .1, "X: -;  Y: -", true );
        guiLabelSetHorizontalAlign( textLabel, "center" );
    end
);

addEventHandler( "onClientCursorMove", root,
    function ( _, _, x, y )
        guiSetText( textLabel, "X: " .. tostring( x ) .. ";  Y: ".. tostring( y ) )
    end
);
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- onClientCursorMove

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
