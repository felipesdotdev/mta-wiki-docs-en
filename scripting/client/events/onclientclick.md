---
doc_id: "mta-wiki:2578"
title: "OnClientClick"
source_title: "OnClientClick"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientClick"
revision_id: 81958
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:17.177438+00:00"
---

# OnClientClick

This event triggers whenever the user clicks his mouse.  This is linked to the GTA world, as oppose to GUI for which [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md) is to be used.  This event allows detection of click positions of the 3D world.

| [[{{{image}}}\|link=\|]] | Note: This event only triggers if the cursor is visible by showCursor |
| --- | --- |
|  |  |

## Parameters

```
string button, string state, int absoluteX, int absoluteY, float worldX, float worldY, float worldZ, element clickedWorld
```

- **button**:  This refers the button used to click on the mouse, can be *left*, *right*, or *middle*.

- **state**: This can be used to tell if the user released or pressed the mouse button, where *up* is passed if the button is released, and *down* is passed if the button is pushed.

- **absoluteX**: This refers to the 2D *x coordinate* the user clicked on his screen, and is an *absolute* position in pixels.

- **absoluteY**: This refers to the 2D *y coordinate* the user clicked on his screen, and is an *absolute* position in pixels.

- **worldX**: This represents the 3D *x coordinate* the player clicked on the screen, and is relative to the GTA world.

- **worldY**: This represents the 3D *y coordinate* the player clicked on the screen, and is relative to the GTA world.

- **worldZ**: This represents the 3D *z coordinate* the player clicked on the screen, and is relative to the GTA world.

- **clickedWorld**: This represents any physical [entity](mta://reference/misc/entity.md) elements that were clicked. If the player clicked on no MTA element, it's set to false.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](mta://reference/misc/root-element.md).

## Example

This example creates a label when an element is clicked, the label displays in the position of the element telling you what kind of element you have clicked.  It hides after 5 seconds.

```
local myLabel = guiCreateLabel  ( 0, 0, 1, 1, "", true )

function addLabelOnClick ( button, state, absoluteX, absoluteY, worldX, worldY, worldZ, clickedElement )
        --if an element was clicked on screen
        if ( clickedElement ) then
                --retreive the element type
                local elementType = getElementType ( clickedElement )
                --change the label text to that element type
                guiSetText ( myLabel, elementType )
                --and place it in the position of where the element is
                guiSetPosition ( myLabel, absoluteX, absoluteY, false )
                --hide the text by passing an empty string 5 seconds later
                setTimer ( guiSetText, 5000, 1, myLabel, "" )
        end
end
addEventHandler ( "onClientClick", root, addLabelOnClick )
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- onClientClick

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
