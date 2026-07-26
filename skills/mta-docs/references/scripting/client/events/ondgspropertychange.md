---
doc_id: "mta-wiki:14567"
title: "OnDgsPropertyChange"
source_title: "OnDgsPropertyChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnDgsPropertyChange"
revision_id: 82193
language: "en"
categories: ["Client_events"]
---

# OnDgsPropertyChange

This event is triggered when a monitored property of a dgs element changes via [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md). The property must be added to the listener using [dgsAddPropertyListener](mta://scripting/client/functions/dgsaddpropertylistener.md) for this event to fire.

| [[{{{image}}}\|link=\|]] | Note: This event only fires for properties that have been explicitly added as listeners using dgsAddPropertyListener |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: The event only triggers when using dgsSetProperty , not element-specific functions like dgsSetText |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: This event does NOT fire for user input changes (like typing in edit boxes). For monitoring user text input, use onDgsTextChange instead |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: The event will not fire if the new value is the same as the old value |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: This event is designed for programmatic property changes, not user interactions |
| --- | --- |
|  |  |

## Parameters

```
string propertyName, mixed newValue, mixed oldValue
```

- **propertyName:** the name of the property that changed

- **newValue:** the new value that was set

- **oldValue:** the previous value before the change

## Source

The source is the dgs element whose property was changed.

## Example

This example shows how to monitor window position changes:

```
DGS = exports.dgs
local window = DGS:dgsCreateWindow(200, 200, 400, 300, "Property Monitor", false)

-- Add listener for position changes
DGS:dgsAddPropertyListener(window, "absPos")

-- Handle property changes
function handlePropertyChange(propertyName, newValue, oldValue)
    if propertyName == "absPos" then
        outputChatBox("Window moved from " .. oldValue[1] .. "," .. oldValue[2] ..
                     " to " .. newValue[1] .. "," .. newValue[2])
    end
end
addEventHandler("onDgsPropertyChange", window, handlePropertyChange)

-- Test the listener
setTimer(function()
    DGS:dgsSetProperty(window, "absPos", {300, 250})
end, 2000, 1)
```

This example demonstrates onDgsPropertyChange with programmatic text updates:

```
DGS = exports.dgs
local window = DGS:dgsCreateWindow(300, 200, 320, 320, "Property Change Demo", false)
local nameEdit = DGS:dgsCreateEdit(20, 50, 280, 30, "", false, window)
local emailEdit = DGS:dgsCreateEdit(20, 100, 280, 30, "", false, window)
local submitBtn = DGS:dgsCreateButton(20, 150, 280, 40, "Submit (Disabled)", false, window)
local statusLabel = DGS:dgsCreateLabel(20, 200, 280, 40, "Click buttons to set text", false, window)
local setNameBtn = DGS:dgsCreateButton(20, 250, 135, 30, "Set Name", false, window)
local setEmailBtn = DGS:dgsCreateButton(165, 250, 135, 30, "Set Email", false, window)

DGS:dgsCreateLabel(20, 30, 100, 20, "Name:", false, window)
DGS:dgsCreateLabel(20, 80, 100, 20, "Email:", false, window)

-- Monitor text property changes
DGS:dgsAddPropertyListener(nameEdit, "text")
DGS:dgsAddPropertyListener(emailEdit, "text")

function validateForm()
    local name = DGS:dgsGetProperty(nameEdit, "text")
    local email = DGS:dgsGetProperty(emailEdit, "text")

    local isValid = (name and name ~= "" and email and email ~= "" and string.find(email, "@"))

    DGS:dgsSetProperty(submitBtn, "enabled", isValid)
    if isValid then
        DGS:dgsSetProperty(submitBtn, "text", "Submit (Ready!)")
        DGS:dgsSetProperty(statusLabel, "text", "Form is valid!")
        DGS:dgsSetProperty(statusLabel, "textColor", tocolor(0, 255, 0, 255))
    else
        DGS:dgsSetProperty(submitBtn, "text", "Submit (Disabled)")
        DGS:dgsSetProperty(statusLabel, "text", "Fill both fields")
        DGS:dgsSetProperty(statusLabel, "textColor", tocolor(255, 0, 0, 255))
    end
end

function handlePropertyChange(propertyName, newValue, oldValue)
    outputChatBox("Property '" .. propertyName .. "' changed to: " .. tostring(newValue))
    validateForm()
end

addEventHandler("onDgsPropertyChange", nameEdit, handlePropertyChange)
addEventHandler("onDgsPropertyChange", emailEdit, handlePropertyChange)

-- Button handlers to trigger property changes
addEventHandler("onDgsMouseClick", setNameBtn, function()
    DGS:dgsSetProperty(nameEdit, "text", "John Doe")
end)

addEventHandler("onDgsMouseClick", setEmailBtn, function()
    DGS:dgsSetProperty(emailEdit, "text", "john@example.com")
end)

validateForm()
```

This example shows onDgsPropertyChange with button properties:

```
DGS = exports.dgs
local button = DGS:dgsCreateButton(100, 100, 200, 50, "Click Me", false)

-- Monitor button properties
DGS:dgsAddPropertyListener(button, {"alpha", "enabled"})

function handleButtonChange(propertyName, newValue, oldValue)
    outputChatBox("Button property '" .. propertyName .. "' changed from " ..
                 tostring(oldValue) .. " to " .. tostring(newValue))
end
addEventHandler("onDgsPropertyChange", button, handleButtonChange)

-- Test the property changes
setTimer(function()
    DGS:dgsSetProperty(button, "alpha", 128)
    DGS:dgsSetProperty(button, "enabled", false)
end, 2000, 1)
```

This example shows monitoring multiple properties:

```
DGS = exports.dgs
local button = DGS:dgsCreateButton(100, 100, 200, 50, "Monitor Me", false)

-- Monitor multiple properties
DGS:dgsAddPropertyListener(button, {"text", "alpha", "visible"})

function handleButtonChange(propertyName, newValue, oldValue)
    outputChatBox("Property '" .. propertyName .. "' changed from " ..
                 tostring(oldValue) .. " to " .. tostring(newValue))
end
addEventHandler("onDgsPropertyChange", button, handleButtonChange)

-- Test changes
setTimer(function()
    DGS:dgsSetProperty(button, "text", "Changed!")
    DGS:dgsSetProperty(button, "alpha", 128)
end, 1000, 1)
```

| [[{{{image}}}\|link=\|]] | Tip: Use dgsRemovePropertyListener to stop monitoring properties when no longer needed |
| --- | --- |
|  |  |

**Author:** [Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab)

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

- onDgsPropertyChange

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

### DGS functions

- [dgsAddPropertyListener](mta://scripting/client/functions/dgsaddpropertylistener.md)

- [dgsRemovePropertyListener](https://wiki.multitheftauto.com/index.php?title=DgsRemovePropertyListener&action=edit&redlink=1)

- [dgsGetListenedProperties](https://wiki.multitheftauto.com/index.php?title=DgsGetListenedProperties&action=edit&redlink=1)

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

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
