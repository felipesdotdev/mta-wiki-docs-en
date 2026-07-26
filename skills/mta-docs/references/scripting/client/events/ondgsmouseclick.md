---
doc_id: "mta-wiki:9416"
title: "OnDgsMouseClick"
source_title: "OnDgsMouseClick"
source_url: "https://wiki.multitheftauto.com/wiki/OnDgsMouseClick"
revision_id: 69028
language: "en"
categories: ["Client_events"]
---

# OnDgsMouseClick

This event happens when any dgs-element clicked

| [[{{{image}}}\|link=\|]] | Note: The player who clicked the dgs-element is always the localPlayer . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: If you want to ask why everything is triggered... See the forth parameter of addEventHandler |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This event will not trigger when onDgsMousePreClick is cancelled. |
| --- | --- |
|  |  |

## Parameters

```
string button, string state, int absoluteX, int absoluteY, bool isCoolingDown
```

- **button:** the name of the button which will be clicked , it can be *left*, *right*, *middle*

- **state:** the state of the mouse button, will be *down* if the mouse button was pushed, or *up* if it was released.  **Please note currently both *up* and *down* state are supported, which is different from *onClientGUIClick*.** For only *up* or *down*, see [onDgsMouseClickUp](mta://scripting/client/events/ondgsmouseclickup.md)/[onDgsMouseClickDown](mta://scripting/client/events/ondgsmouseclickdown.md)

- **absoluteX:** the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y position of the mouse cursor, in pixels, measured from the top of the screen.

- **isCoolingDown:** A bool indicates whether this dgs element is cooling down. See [Property:clickCoolDown](mta://reference/misc/dgs-general-basic-properties.md)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the DGS element that was clicked.

## Example

This example creates an edit box alongside an "Output!" button. When the button is clicked with the left mouse button, it will output the message in the edit box into the chat box.

```
DGS = exports.dgs
-- When client's resource starts, create the GUI
function initGUI( )
    -- Create our button
    btnOutput = DGS:dgsCreateButton( 0.7, 0.1, 0.2, 0.1, "Output!", true )

    -- And attach our button to the outputEditBox function
    addEventHandler ( "onDgsMouseClick", btnOutput, outputEditBox )

    -- Create an edit box and define it as "editBox".
    editBox = DGS:dgsCreateEdit( 0.3, 0.1, 0.4, 0.1, "Type your message here!", true )
end
addEventHandler( "onClientResourceStart", getResourceRootElement( getThisResource( ) ), initGUI )

-- Setup our function to output the message to the chatbox
function outputEditBox ( button, state )
    if button == "left" and state == "down" then
        local text = DGS:dgsGetText( editBox )-- Get the text from the edit box
        outputChatBox ( text ) -- Output that text
    end
end
```

### Clear Example

```
DGS = exports.dgs

btnOutput = DGS:dgsCreateButton( 0.7, 0.1, 0.2, 0.1, "Output!", true )

function outputEditBox ( button, state )
    if button == "left" and state == "down" then
        outputChatBox ( "Hey bro, you clicked me, your state is "..state )
    end
end
addEventHandler ( "onDgsMouseClick", btnOutput, outputEditBox )
```

## See Also

### DGS events

## General

- [onDgsBlur](mta://scripting/client/events/ondgsblur.md)

- [onDgsCreate](mta://scripting/client/events/ondgscreate.md)

- [onDgsCursorTypeChange](mta://scripting/client/events/ondgscursortypechange.md)

- [onDgsCursorStateChange](https://wiki.multitheftauto.com/index.php?title=OnDgsCursorStateChange&action=edit&redlink=1)

- [onDgsDestroy](mta://scripting/client/events/ondgsdestroy.md)

- [onDgsElementRender](mta://scripting/client/events/ondgselementrender.md)

- [onDgsElementMove](mta://scripting/client/events/ondgselementmove.md)

- [onDgsElementSize](mta://scripting/client/events/ondgselementsize.md)

- [onDgsElementEnter](mta://scripting/client/events/ondgselemententer.md)

- [onDgsElementLeave](mta://scripting/client/events/ondgselementleave.md)

- [onDgsFocus](mta://scripting/client/events/ondgsfocus.md)

- [onDgsKey](mta://scripting/client/events/ondgskey.md)

- [onDgsPositionChange](mta://scripting/client/events/ondgspositionchange.md)

- [onDgsPreRender](mta://scripting/client/events/ondgsprerender.md)

- [onDgsRender](mta://scripting/client/events/ondgsrender.md)

- [onDgsElementScroll](mta://scripting/client/events/ondgselementscroll.md)

- [onDgsSizeChange](mta://scripting/client/events/ondgssizechange.md)

- [onDgsTextChange](mta://scripting/client/events/ondgstextchange.md)

- [onDgsWindowClose](mta://scripting/client/events/ondgswindowclose.md)

- [onDgsPropertyChange](mta://scripting/client/events/ondgspropertychange.md)

## Check Box

- [onDgsCheckBoxChange](mta://scripting/client/events/ondgscheckboxchange.md)

## Combo Box

- [onDgsComboBoxStateChange](mta://scripting/client/events/ondgscomboboxstatechange.md)

- [onDgsComboBoxSelect](mta://scripting/client/events/ondgscomboboxselect.md)

## Drag'N Drop

- [onDgsDrag](https://wiki.multitheftauto.com/index.php?title=OnDgsDrag&action=edit&redlink=1)

- [onDgsDrop](https://wiki.multitheftauto.com/index.php?title=OnDgsDrop&action=edit&redlink=1)

## Edit

- [onDgsEditPreSwitch](mta://scripting/client/events/ondgseditpreswitch.md)

- [onDgsEditSwitched](mta://scripting/client/events/ondgseditswitched.md)

- [onDgsEditAccepted](mta://scripting/client/events/ondgseditaccepted.md)

## Grid List

- [onDgsGridListItemDoubleClick](mta://scripting/client/events/ondgsgridlistitemdoubleclick.md)

- [onDgsGridListSelect](mta://scripting/client/events/ondgsgridlistselect.md)

- [onDgsGridListHover](mta://scripting/client/events/ondgsgridlisthover.md)

## Menu

- [onDgsMenuHover](mta://scripting/client/events/ondgsmenuhover.md)

- [onDgsMenuSelect](mta://scripting/client/events/ondgsmenuselect.md)

## Selector

- [onDgsSelectorSelect](mta://scripting/client/events/ondgsselectorselect.md)

## Mouse

- [onDgsMousePreClick](mta://scripting/client/events/ondgsmousepreclick.md)

- onDgsMouseClick

- [onDgsMouseClickDown](mta://scripting/client/events/ondgsmouseclickdown.md)

- [onDgsMouseClickUp](mta://scripting/client/events/ondgsmouseclickup.md)

- [onDgsMouseDrag](https://wiki.multitheftauto.com/index.php?title=OnDgsMouseDrag&action=edit&redlink=1)

- [onDgsMouseDoubleClick](mta://scripting/client/events/ondgsmousedoubleclick.md)

- [onDgsMouseDoubleClickDown](mta://scripting/client/events/ondgsmousedoubleclickdown.md)

- [onDgsMouseDoubleClickUp](mta://scripting/client/events/ondgsmousedoubleclickup.md)

- [onDgsMouseDown](mta://scripting/client/events/ondgsmousedown.md)

- [onDgsMouseHover](mta://scripting/client/events/ondgsmousehover.md)

- [onDgsMouseEnter](mta://scripting/client/events/ondgsmouseenter.md)

- [onDgsMouseLeave](mta://scripting/client/events/ondgsmouseleave.md)

- [onDgsMouseMultiClick](mta://scripting/client/events/ondgsmousemulticlick.md)

- [onDgsMouseMove](mta://scripting/client/events/ondgsmousemove.md)

- [onDgsMouseStay](mta://scripting/client/events/ondgsmousestay.md)

- [onDgsMouseUp](mta://scripting/client/events/ondgsmouseup.md)

- [onDgsMouseWheel](mta://scripting/client/events/ondgsmousewheel.md)

## Radio Button

- [onDgsRadioButtonChange](mta://scripting/client/events/ondgsradiobuttonchange.md)

## Switch Button

- [onDgsSwitchButtonStateChange](mta://scripting/client/events/ondgsswitchbuttonstatechange.md)

## Tab

- [onDgsTabPanelTabSelect](mta://scripting/client/events/ondgstabpaneltabselect.md)

- [onDgsTabSelect](mta://scripting/client/events/ondgstabselect.md)

## Animation

- [onDgsStopMoving](mta://scripting/client/events/ondgsstopmoving.md)

- [onDgsStopSizing](mta://scripting/client/events/ondgsstopsizing.md)

- [onDgsStopAlphaing](mta://scripting/client/events/ondgsstopalphaing.md)

- [onDgsStopAniming](mta://scripting/client/events/ondgsstopaniming.md)

## Plugin

### Media

- [onDgsMediaPlay](mta://scripting/client/events/ondgsmediaplay.md)

- [onDgsMediaPause](mta://scripting/client/events/ondgsmediapause.md)

- [onDgsMediaStop](mta://scripting/client/events/ondgsmediastop.md)

- [onDgsMediaLoaded](https://wiki.multitheftauto.com/index.php?title=OnDgsMediaLoaded&action=edit&redlink=1)

- [onDgsMediaTimeUpdate](https://wiki.multitheftauto.com/index.php?title=OnDgsMediaTimeUpdate&action=edit&redlink=1)

- [onDgsMediaBrowserReturn](https://wiki.multitheftauto.com/index.php?title=OnDgsMediaBrowserReturn&action=edit&redlink=1)

### Color Picker

- [onDgsColorPickerChange](mta://scripting/client/events/ondgscolorpickerchange.md)

- [onDgsColorPickerComponentSelectorChange](mta://scripting/client/events/ondgscolorpickercomponentselectorchange.md)

### QRCode

- [onDgsQRCodeLoad](mta://scripting/client/events/ondgsqrcodeload.md)

### Remote Image

- [onDgsRemoteImageLoad](mta://scripting/client/events/ondgsremoteimageload.md)

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
