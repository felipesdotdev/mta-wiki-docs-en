---
doc_id: "mta-wiki:3293"
title: "OnClientGUIClick"
source_title: "OnClientGUIClicked"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIClicked"
revision_id: 82747
language: "en"
categories: ["Client_events", "Changes_in_1.7.0"]
generated_at: "2026-07-26T16:16:18.634066+00:00"
---

# OnClientGUIClick

This event happens when any gui-element clicked.

| [[{{{image}}}\|link=\|]] | Note: The player who clicked the gui-element is always the localPlayer . |
| --- | --- |
|  |  |

## Parameters

```
string button, string state, int absoluteX, int absoluteY
```

- **button:** the name of the button which will be clicked, it can be *left*, *right*, *middle*.

- **state:** the state of the mouse button, will be *down* if the mouse button was pushed, or *up* if it was released.

ADDED/UPDATED IN VERSION 1.7.0 [r26369](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=26369):

**down** state is now supported as well.  
To use this feature, you must also set **<min_mta_version>** to at least **1.7.0-7.26369** in **meta.xml**.  
Please note that before this version only the **up** state worked. 

- **absoluteX:** the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y position of the mouse cursor, in pixels, measured from the top of the screen.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the GUI element that was clicked.

| [[{{{image}}}\|link=\|]] | Note: If the GUI Element attached to this event has a parent element, this event will be triggered once the parent element of the attached element is clicked too. You can set the parameter propagate to false in the call to addEventHandler to prevent this. |
| --- | --- |
|  |  |

## Example

This example creates an edit box alongside an "Output!" button. When the button is clicked with the left mouse button, it will output the message in the edit box into the chat box.

```
-- When client's resource starts, create the GUI
function initGUI( )
    -- Create our button
    btnOutput = guiCreateButton( 0.7, 0.1, 0.2, 0.1, "Output!", true )

    -- And attach our button to the outputEditBox function
    addEventHandler ( "onClientGUIClick", btnOutput, outputEditBox, false )

    -- Create an edit box and define it as "editBox".
    editBox = guiCreateEdit( 0.3, 0.1, 0.4, 0.1, "Type your message here!", true )
    guiEditSetMaxLength ( editBox, 128 ) -- The max chatbox text length is 128, so force this
end
addEventHandler( "onClientResourceStart", resourceRoot, initGUI )

-- Setup our function to output the message to the chatbox
function outputEditBox ( button )
    if button == "left" then
        local text = guiGetText ( editBox )-- Get the text from the edit box
        outputChatBox ( text ) -- Output that text
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

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- onClientGUIClick

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
