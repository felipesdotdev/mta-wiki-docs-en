---
doc_id: "mta-wiki:10007"
title: "OnDgsMouseLeave"
source_title: "OnClientDgsDxMouseLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientDgsDxMouseLeave"
revision_id: 76201
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.036716+00:00"
---

# OnDgsMouseLeave

This event is fired when the user moves the mouse away from a DGS element.

## Parameters

```
int absoluteX, int absoluteY, element enteredGUI
```

- **absoluteX**:  the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY**:  the Y position of the mouse cursor, in pixels, measured from the top of the screen.

- **enteredGUI**: is the DGS element that was switched from, or nil if it doesn't exist

## Source

The [source](mta://reference/misc/event-system.md) of this event is the DGS element that the mouse was moved away from.

## Example

This example shows a message when you move the mouse away from a DGS element.

```
addEventHandler("onDgsMouseLeave", root, function(aX, aY)
    outputChatBox("You're no longer pointing at a DGS element at (" .. tostring(aX) .. ", " .. tostring(aY) .. ")")
end)
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

- [onDgsMouseClick](mta://scripting/client/events/ondgsmouseclick.md)

- [onDgsMouseClickDown](mta://scripting/client/events/ondgsmouseclickdown.md)

- [onDgsMouseClickUp](mta://scripting/client/events/ondgsmouseclickup.md)

- [onDgsMouseDrag](https://wiki.multitheftauto.com/index.php?title=OnDgsMouseDrag&action=edit&redlink=1)

- [onDgsMouseDoubleClick](mta://scripting/client/events/ondgsmousedoubleclick.md)

- [onDgsMouseDoubleClickDown](mta://scripting/client/events/ondgsmousedoubleclickdown.md)

- [onDgsMouseDoubleClickUp](mta://scripting/client/events/ondgsmousedoubleclickup.md)

- [onDgsMouseDown](mta://scripting/client/events/ondgsmousedown.md)

- [onDgsMouseHover](mta://scripting/client/events/ondgsmousehover.md)

- [onDgsMouseEnter](mta://scripting/client/events/ondgsmouseenter.md)

- onDgsMouseLeave

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
