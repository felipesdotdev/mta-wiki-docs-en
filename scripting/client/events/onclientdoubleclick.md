---
doc_id: "mta-wiki:5435"
title: "OnClientDoubleClick"
source_title: "OnClientDoubleClick"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientDoubleClick"
revision_id: 55058
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.286144+00:00"
---

# OnClientDoubleClick

This event triggers whenever the user double-clicks his mouse.  This is linked to the GTA world, as appose to GUI for which [onClientGUIDoubleClick](mta://scripting/client/events/onclientguidoubleclick.md) is to be used.  This event allows detection of click positions of the 3D world.

## Parameters

```
string button, int absoluteX, int absoluteY, float worldX, float worldY, float worldZ, element clickedWorld
```

- **button**:  This refers the button used to click on the mouse, can be *left*, *right*, or *middle*.

- **absoluteX**: This refers to the 2D *x coordinate* the user clicked on his screen, and is an *absolute* position in pixels.

- **absoluteY**: This refers to the 2D *y coordinate* the user clicked on his screen, and is an *absolute* position in pixels.

- **worldX**: This represents the 3D *x coordinate* the player clicked on the screen, and is relative to the GTA world.

- **worldY**: This represents the 3D *y coordinate* the player clicked on the screen, and is relative to the GTA world.

- **worldZ**: This represents the 3D *z coordinate* the player clicked on the screen, and is relative to the GTA world.

- **clickedWorld**: This represents any physical [entity](mta://reference/misc/entity.md) elements that were clicked. If the player clicked on no MTA element, it's set to false.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](mta://reference/misc/root-element.md).

## Example

```
function onMyMouseDoubleClick (button, absoluteX, absoluteY, worldX, worldY,  worldZ, clickedWorld)
	if button == "left" then 
		playSoundFrontEnd(40)
	end
end
addEventHandler("onClientDoubleClick", root, onMyMouseDoubleClick)
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- [onClientCursorMove](mta://scripting/client/events/onclientcursormove.md)

- onClientDoubleClick

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
