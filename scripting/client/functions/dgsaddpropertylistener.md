---
doc_id: "mta-wiki:14569"
title: "DgsAddPropertyListener"
source_title: "DgsAddPropertyListener"
source_url: "https://wiki.multitheftauto.com/wiki/DgsAddPropertyListener"
revision_id: 82197
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:11:44.505733+00:00"
---

# DgsAddPropertyListener

This function enables monitoring of property changes on DGS elements. When a property that has been added to the listener list changes via [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md), it triggers the [onDgsPropertyChange](#Events) event.

| [[{{{image}}}\|link=\|]] | Note: Property listeners only trigger when using dgsSetProperty , not when using specific setter functions |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: The onDgsPropertyChange event is only triggered for properties that have been explicitly added to the listener |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: Property listeners persist until explicitly removed using dgsRemovePropertyListener or the element is destroyed |
| --- | --- |
|  |  |

## Syntax

```
bool dgsAddPropertyListener ( element dgsElement, string/table propertyNames )
bool dgsAddPropertyListener ( table dgsElements, string/table propertyNames )
```

### Required Arguments

- **dgsElement:** A DGS element or table of DGS elements to monitor.

- **propertyNames:** A property name (string) or table of property names to listen for changes.

### Returns

Returns *true* if the property listener was added successfully, *false* otherwise.

## Examples

### Example 1: Basic Property Monitoring

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a DGS window
local window = dgsCreateWindow(200, 200, 400, 300, "Property Monitor Demo", false)

-- Add listener for position changes
dgsAddPropertyListener(window, "absPos")

-- Set up event handler
addEventHandler("onDgsPropertyChange", window, function(propertyName, newValue, oldValue)
if propertyName == "absPos" then
outputChatBox("Window moved from " .. tostring(oldValue[1]) .. "," .. tostring(oldValue[2]) ..
" to " .. tostring(newValue[1]) .. "," .. tostring(newValue[2]))
end
end)

-- Test the listener
setTimer(function()
dgsSetProperty(window, "absPos", {300, 250})
end, 2000, 1)
```

### Example 2: Multiple Property Monitoring

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a DGS button
local button = dgsCreateButton(50, 50, 200, 100, "Monitor Me", false)

-- Monitor multiple properties
dgsAddPropertyListener(button, {"text", "color", "size"})

-- Handle property changes
addEventHandler("onDgsPropertyChange", button, function(propertyName, newValue, oldValue)
outputChatBox("Property '" .. propertyName .. "' changed!")

    if propertyName == "text" then
        outputChatBox("Text changed from '" .. tostring(oldValue) .. "' to '" .. tostring(newValue) .. "'")
    elseif propertyName == "color" then
        outputChatBox("Color changed")
    elseif propertyName == "size" then
        outputChatBox("Size changed to " .. tostring(newValue[1]) .. "x" .. tostring(newValue[2]))
    end

end)

-- Test the listeners
setTimer(function()
dgsSetProperty(button, "text", "Changed Text!")
end, 1000, 1)

setTimer(function()
dgsSetProperty(button, "color", {tocolor(255, 0, 0, 255), tocolor(200, 0, 0, 255), tocolor(150, 0, 0, 255)})
end, 2000, 1)
```

### Example 3: Monitoring Multiple Elements

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create multiple elements
local elements = {}
elements[1] = dgsCreateButton(100, 100, 150, 50, "Button 1", false)
elements[2] = dgsCreateButton(100, 200, 150, 50, "Button 2", false)
elements[3] = dgsCreateButton(100, 300, 150, 50, "Button 3", false)

-- Add property listeners to all elements at once
dgsAddPropertyListener(elements, "visible")

-- Handle visibility changes for all elements
for i, element in ipairs(elements) do
addEventHandler("onDgsPropertyChange", element, function(propertyName, newValue, oldValue)
if propertyName == "visible" then
local elementName = "Element " .. i
outputChatBox(elementName .. " visibility changed to " .. tostring(newValue))
end
end)
end

-- Test visibility changes
setTimer(function()
for i, element in ipairs(elements) do
dgsSetProperty(element, "visible", math.random() > 0.5)
end
end, 3000, 1)
```

### Example 4: Real-time Position Tracking

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions

-- Create a movable window
local trackingWindow = dgsCreateWindow(100, 100, 250, 200, "Position Tracker", false)
local positionLabel = dgsCreateLabel(10, 30, 230, 20, "Position: 100, 100", false, trackingWindow)
local sizeLabel = dgsCreateLabel(10, 60, 230, 20, "Size: 250 x 200", false, trackingWindow)

-- Monitor position and size changes
dgsAddPropertyListener(trackingWindow, {"absPos", "absSize"})

-- Update labels when properties change
addEventHandler("onDgsPropertyChange", trackingWindow, function(propertyName, newValue, oldValue)
if propertyName == "absPos" then
dgsSetProperty(positionLabel, "text", "Position: " .. newValue[1] .. ", " .. newValue[2])
elseif propertyName == "absSize" then
dgsSetProperty(sizeLabel, "text", "Size: " .. newValue[1] .. " x " .. newValue[2])
end
end)

-- Make window movable and resizable for testing
dgsSetProperty(trackingWindow, "movable", true)
dgsSetProperty(trackingWindow, "sizable", true)
```

## Author

[Mohab](https://wiki.multitheftauto.com/wiki/User:Mohab).

## See Also

- [dgsGetPosition](mta://scripting/client/functions/dgsgetposition.md)

- [dgsSetPosition](mta://scripting/client/functions/dgssetposition.md)

- [dgsSetParent](mta://scripting/client/functions/dgssetparent.md)

- [dgsGetParent](mta://scripting/client/functions/dgsgetparent.md)

- [dgsGetChild](mta://scripting/client/functions/dgsgetchild.md)

- [dgsGetChildren](mta://scripting/client/functions/dgsgetchildren.md)

- [dgsGetSize](mta://scripting/client/functions/dgsgetsize.md)

- [dgsSetSize](mta://scripting/client/functions/dgssetsize.md)

- [dgsGetType](mta://scripting/client/functions/dgsgettype.md)

- [dgsSetLayer](mta://scripting/client/functions/dgssetlayer.md)

- [dgsGetLayer](mta://scripting/client/functions/dgsgetlayer.md)

- [dgsSetCurrentLayerIndex](mta://scripting/client/functions/dgssetcurrentlayerindex.md)

- [dgsGetCurrentLayerIndex](mta://scripting/client/functions/dgsgetcurrentlayerindex.md)

- [dgsGetLayerElements](mta://scripting/client/functions/dgsgetlayerelements.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsSetPropertyInherit](mta://scripting/client/functions/dgssetpropertyinherit.md)

- [dgsGetProperties](mta://scripting/client/functions/dgsgetproperties.md)

- [dgsSetProperties](mta://scripting/client/functions/dgssetproperties.md)

- [dgsGetVisible](mta://scripting/client/functions/dgsgetvisible.md)

- [dgsSetVisible](mta://scripting/client/functions/dgssetvisible.md)

- [dgsGetEnabled](mta://scripting/client/functions/dgsgetenabled.md)

- [dgsSetEnabled](mta://scripting/client/functions/dgssetenabled.md)

- [dgsGetPositionAlignment](mta://scripting/client/functions/dgsgetpositionalignment.md)

- [dgsSetPositionAlignment](mta://scripting/client/functions/dgssetpositionalignment.md)

- [dgsGetAlpha](mta://scripting/client/functions/dgsgetalpha.md)

- [dgsSetAlpha](mta://scripting/client/functions/dgssetalpha.md)

- [dgsGetFont](mta://scripting/client/functions/dgsgetfont.md)

- [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)

- [dgsGetText](mta://scripting/client/functions/dgsgettext.md)

- [dgsSetText](mta://scripting/client/functions/dgssettext.md)

- [dgsGetPostGUI](mta://scripting/client/functions/dgsgetpostgui.md)

- [dgsSetPostGUI](mta://scripting/client/functions/dgssetpostgui.md)

- [dgsGetInputEnabled](mta://scripting/client/functions/dgsgetinputenabled.md)

- [dgsSetInputEnabled](mta://scripting/client/functions/dgssetinputenabled.md)

- [dgsGetInputMode](mta://scripting/client/functions/dgsgetinputmode.md)

- [dgsSetInputMode](mta://scripting/client/functions/dgssetinputmode.md)

- [dgsAttachToAutoDestroy](mta://scripting/client/functions/dgsattachtoautodestroy.md)

- [dgsDetachFromAutoDestroy](mta://scripting/client/functions/dgsdetachfromautodestroy.md)

- [dgsFocus](mta://scripting/client/functions/dgsfocus.md)

- [dgsBlur](mta://scripting/client/functions/dgsblur.md)

- [dgsCreateFont](mta://scripting/client/functions/dgscreatefont.md)

- [dgsBringToFront](mta://scripting/client/functions/dgsbringtofront.md)

- [dgsMoveToBack](mta://scripting/client/functions/dgsmovetoback.md)

- [dgsGetScreenSize](mta://scripting/client/functions/dgsgetscreensize.md)

- [dgsGetCursorPosition](mta://scripting/client/functions/dgsgetcursorposition.md)

- [dgsGetMouseEnterGUI](mta://scripting/client/functions/dgsgetmouseentergui.md)

- [dgsGetMouseLeaveGUI](mta://scripting/client/functions/dgsgetmouseleavegui.md)

- [dgsIsMouseWithinGUI](mta://scripting/client/functions/dgsismousewithingui.md)

- [dgsSetSystemFont](mta://scripting/client/functions/dgssetsystemfont.md)

- [dgsGetSystemFont](mta://scripting/client/functions/dgsgetsystemfont.md)

- [dgsGetElementsInLayer](mta://scripting/client/functions/dgsgetelementsinlayer.md)

- [dgsGetElementsFromResource](mta://scripting/client/functions/dgsgetelementsfromresource.md)

- [dgsGetFocusedGUI](mta://scripting/client/functions/dgsgetfocusedgui.md)

- [dgsImportFunction](mta://scripting/client/functions/dgsimportfunction.md)

- [dgsImportOOPClass](mta://scripting/client/functions/dgsimportoopclass.md)

- [dgsG2DLoadHooker](mta://scripting/client/functions/dgsg2dloadhooker.md)

- [dgsSetRenderSetting](mta://scripting/client/functions/dgssetrendersetting.md)

- [dgsGetRenderSetting](mta://scripting/client/functions/dgsgetrendersetting.md)

- [dgsSimulateClick](mta://scripting/client/functions/dgssimulateclick.md)

- [dgsGetRootElement](mta://scripting/client/functions/dgsgetrootelement.md)

- [dgsAddMoveHandler](mta://scripting/client/functions/dgsaddmovehandler.md)

- [dgsRemoveMoveHandler](mta://scripting/client/functions/dgsremovemovehandler.md)

- [dgsIsMoveHandled](mta://scripting/client/functions/dgsismovehandled.md)

- [dgsAddSizeHandler](mta://scripting/client/functions/dgsaddsizehandler.md)

- [dgsRemoveSizeHandler](mta://scripting/client/functions/dgsremovesizehandler.md)

- [dgsIsSizeHandled](mta://scripting/client/functions/dgsissizehandled.md)

- [dgsAttachElements](mta://scripting/client/functions/dgsattachelements.md)

- [dgsDetachElements](mta://scripting/client/functions/dgsdetachelements.md)

- [dgsElementIsAttached](mta://scripting/client/functions/dgselementisattached.md)

- dgsAddPropertyListener

- [dgsRemovePropertyListener](https://wiki.multitheftauto.com/index.php?title=DgsRemovePropertyListener&action=edit&redlink=1)

- [dgsGetListenedProperties](https://wiki.multitheftauto.com/index.php?title=DgsGetListenedProperties&action=edit&redlink=1)

- [dgsSetMultiClickInterval](mta://scripting/client/functions/dgssetmulticlickinterval.md)

- [dgsGetMultiClickInterval](mta://scripting/client/functions/dgsgetmulticlickinterval.md)

- [dgsSetMouseStayDelay](mta://scripting/client/functions/dgssetmousestaydelay.md)

- [dgsGetMouseStayDelay](mta://scripting/client/functions/dgsgetmousestaydelay.md)

- [dgsCenterElement](mta://scripting/client/functions/dgscenterelement.md)

- [dgsSetElementKeeperEnabled](mta://scripting/client/functions/dgssetelementkeeperenabled.md)

- [dgsGetElementKeeperEnabled](mta://scripting/client/functions/dgsgetelementkeeperenabled.md)

- [dgsSetClickingSound](mta://scripting/client/functions/dgssetclickingsound.md)

- [dgsGetClickingSound](mta://scripting/client/functions/dgsgetclickingsound.md)

- [dgsSetClickingSoundVolume](mta://scripting/client/functions/dgssetclickingsoundvolume.md)

- [dgsGetClickingSoundVolume](mta://scripting/client/functions/dgsgetclickingsoundvolume.md)
