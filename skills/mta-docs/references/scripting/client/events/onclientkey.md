---
doc_id: "mta-wiki:5624"
title: "OnClientKey"
source_title: "OnClientKey"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientKey"
revision_id: 81880
language: "en"
categories: ["Client_events"]
---

# OnClientKey

This event triggers whenever the user presses a button on their keyboard or mouse.
This event can also be used to see if the client scrolls their mouse wheel.

| [[{{{image}}}\|link=\|]] | Important Note: F8 key not triggered on this event! |
| --- | --- |
|  |  |

## Parameters

```
string button, bool pressOrRelease
```

- **button**:  This refers the button pressed. See [key names](mta://reference/misc/key-names.md) for a list of keys.

- **pressOrRelease**: This refers to whether they were pressing or releasing the key, *true* when pressing, *false* when releasing.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](https://wiki.multitheftauto.com/index.php?search=root%20element).

## Cancel effect

ADDED/UPDATED IN VERSION 1.4 :

If this event is [canceled](mta://reference/misc/event-system.md), then all GTA and MTA binds, bound to the canceled key, won't be triggered.

**Note 1:** The escape key can only be cancelled once. If a user presses the escape key twice in a row the main menu will still open.

**Note 2:** The event is only cancellable when the key is being pressed, not when being released.

## Example

This example will say in chatbox every time the user presses down a a key.

```
function playerPressedKey(button, press)
    if (press) then -- Only output when they press it down
        outputChatBox("You pressed the "..button.." key!")
    end
end
addEventHandler("onClientKey", root, playerPressedKey)
```

This example outputs if the client moves his mousewheel.

```
addEventHandler( "onClientKey", root, function(button,press) 
    -- Since mouse_wheel_up and mouse_wheel_down cant return a release, we dont have to check the press.
    if button == "mouse_wheel_up" or button == "mouse_wheel_down" then
        outputDebugString( button .. " moved." )
        return true
    end
    return false
end )
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- [onClientCursorMove](mta://scripting/client/events/onclientcursormove.md)

- [onClientDoubleClick](mta://scripting/client/events/onclientdoubleclick.md)

- onClientKey

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
