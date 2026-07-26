---
doc_id: "mta-wiki:11729"
title: "OnDgsMouseUp"
source_title: "OnDgsMouseUp"
source_url: "https://wiki.multitheftauto.com/wiki/OnDgsMouseUp"
revision_id: 69031
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:22.959558+00:00"
---

# OnDgsMouseUp

This event is fired when the user releases his mouse button when on top of a DGS element.

| [[{{{image}}}\|link=\|]] | Note: This event will not trigger when onDgsMousePreClick is cancelled. |
| --- | --- |
|  |  |

## Parameters

```
string button, int absoluteX, int absoluteY
```

- **button:** the name of the mouse button that was released on a DGS element, can be *left*, *right*, or *middle*.

- **absoluteX:** the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y position of the mouse cursor, in pixels, measured from the top of the screen.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the DGS element on top of which the mouse button was released.

## Example

This example show how to add very basic *click'n'drag* feature for DGS elements (only for those which parent element is dgs-root)

```
DGS = exports.dgs
addEventHandler( "onDgsMouseDown", getRootElement( ),
    function ( btn, x, y )
        if btn == "left" then
            clickedElement = source; -- store the clicked element in a global variable
            local elementPos = { DGS:dgsGetPosition( source, false ) };
            offsetPos = { x - elementPos[ 1 ], y - elementPos[ 2 ] }; -- get the offset position
        end
    end
);

addEventHandler( "onDgsMouseUp", getRootElement( ),
    function ( btn, x, y )
        if btn == "left" then
            clickedElement = nil;
        end
    end
);

addEventHandler( "onDgsMouseMove", getRootElement( ),
    function ( x, y )
        if clickedElement then
            DGS:dgsSetPosition( clickedElement, x - offsetPos[ 1 ], y - offsetPos[ 2 ], false );
        end
    end
);
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

- [onDgsMouseLeave](mta://scripting/client/events/ondgsmouseleave.md)

- [onDgsMouseMultiClick](mta://scripting/client/events/ondgsmousemulticlick.md)

- [onDgsMouseMove](mta://scripting/client/events/ondgsmousemove.md)

- [onDgsMouseStay](mta://scripting/client/events/ondgsmousestay.md)

- onDgsMouseUp

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
