---
doc_id: "mta-wiki:12089"
title: "TDX"
source_title: "TDX"
source_url: "https://wiki.multitheftauto.com/wiki/TDX"
revision_id: 65875
language: "en"
categories: []
generated_at: "2026-07-26T16:16:54.806680+00:00"
---

# TDX

Total DX Library (TDX) is a DX GUI library for MTA:SA which aims to replicate all of the features offered by CEGUI - but instead is built upon the existing dxDraw* functions provided by MTA.

**Author:** LopSided

**GitHub:** [https://github.com/Lpsd/total-dx-lib](https://github.com/Lpsd/total-dx-lib)

## Getting Started

It's really simple to implement Total DX Library into your resource/project. Download the [latest release](https://github.com/Lpsd/total-dx-lib/releases) from GitHub and drop the **dxlib** folder from the .zip into your server's **resources** folder.

Start the **dxlib** resource and ensure it loads correctly (you should see some output in debugscript).

Next you'll need to import the library into your resource, using the code below. We recommend you put this code inside an **onClientResourceStart** event for each resource.

```
loadstring(exports.dxlib:dxLoadFunctions())()
```

Once the library has been imported, there's no need to use any more exports! You can use all the features documented here as though they were part of MTA itself.

**Note**: Every TDX GUI element created will be hosted within the parent **dxlib** resource. Upon restarting the **dxlib** resource any previous GUI will be destroyed (meaning user interaction/input will be lost!) - be careful.

### Example Usage

At the core, TDX is object-oriented, which is great for complex GUI systems. However, procedural style is also supported!

**OOP (Object-Oriented) Example:**

```
local window = DxWindow:new(300, 300, 300, 300, "Color Picker")
local input = DxInput:new(0, 50, 200, 35, "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
input:setParent(window)
input:setCentered(true)
```

**Procedural Example:**

```
local window = dxCreateWindow(300, 300, 300, 300, "Color Picker")
local input = dxCreateInput(0, 50, 200, 35, "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
dxSetParent(input, window)
dxSetCentered(input, true)
```

### Classes

Below you can find a list of currently supported classes - **DxClass (dx-type)**

- DxBlank (dx-blank)

- DxButton (dx-button)

- DxCheckbox(dx-checkbox)

- DxCircle (dx-circle)

- DxColorPicker (dx-colorpicker)

- DxImage (dx-image)

- DxInput (dx-input)

- DxRadioButton (dx-radiobutton)

- DxRing (dx-ring)

- DxSlider (dx-slider)

- DxText (dx-text)

- DxWindow (dx-window)

All of these classes inherit the base class, DxElement, which provides many of the available methods for each class.

# **Functions**

- [dxAddClickFunction](mta://reference/misc/dxaddclickfunction.md)

- [dxAddRenderFunction](mta://scripting/client/functions/dxaddrenderfunction.md)

- [dxApplyMask](mta://scripting/client/functions/dxapplymask.md)

- [dxBringToFront](mta://scripting/client/functions/dxbringtofront.md)

- [dxDestroy](mta://scripting/client/functions/dxdestroy.md)

- [dxGetAlpha](mta://scripting/client/functions/dxgetalpha.md)

- [dxGetBounds](mta://scripting/client/functions/dxgetbounds.md)

- [dxGetChildren](https://wiki.multitheftauto.com/index.php?title=DxGetChildren&action=edit&redlink=1)

- [dxGetChildrenByType](https://wiki.multitheftauto.com/index.php?title=DxGetChildrenByType&action=edit&redlink=1)

- [dxGetColor](https://wiki.multitheftauto.com/index.php?title=DxGetColor&action=edit&redlink=1)

- [dxGetGlobalProperty](https://wiki.multitheftauto.com/index.php?title=DxGetGlobalProperty&action=edit&redlink=1)

- [dxGetHoverColor](https://wiki.multitheftauto.com/index.php?title=DxGetHoverColor&action=edit&redlink=1)

- [dxGetIndex](https://wiki.multitheftauto.com/index.php?title=DxGetIndex&action=edit&redlink=1)

- [dxGetInheritedBounds](https://wiki.multitheftauto.com/index.php?title=DxGetInheritedBounds&action=edit&redlink=1)

- [dxGetInheritedChildren](https://wiki.multitheftauto.com/index.php?title=DxGetInheritedChildren&action=edit&redlink=1)

- [dxGetInheritedChildrenByType](https://wiki.multitheftauto.com/index.php?title=DxGetInheritedChildrenByType&action=edit&redlink=1)

- [dxGetInheritedParents](https://wiki.multitheftauto.com/index.php?title=DxGetInheritedParents&action=edit&redlink=1)

- [dxGetMaskTexture](https://wiki.multitheftauto.com/index.php?title=DxGetMaskTexture&action=edit&redlink=1)

- [dxGetNonRootElements](https://wiki.multitheftauto.com/index.php?title=DxGetNonRootElements&action=edit&redlink=1)

- [dxGetObstructingElement](https://wiki.multitheftauto.com/index.php?title=DxGetObstructingElement&action=edit&redlink=1)

- [dxGetParent](https://wiki.multitheftauto.com/index.php?title=DxGetParent&action=edit&redlink=1)

- [dxGetPosition](https://wiki.multitheftauto.com/index.php?title=DxGetPosition&action=edit&redlink=1)

- [dxGetProperty](https://wiki.multitheftauto.com/index.php?title=DxGetProperty&action=edit&redlink=1)

- [dxGetRootElement](https://wiki.multitheftauto.com/index.php?title=DxGetRootElement&action=edit&redlink=1)

- [dxGetRootElements](https://wiki.multitheftauto.com/index.php?title=DxGetRootElements&action=edit&redlink=1)

- [dxGetSize](https://wiki.multitheftauto.com/index.php?title=DxGetSize&action=edit&redlink=1)

- [dxGetText](https://wiki.multitheftauto.com/index.php?title=DxGetText&action=edit&redlink=1)

- [dxGetTextColor](https://wiki.multitheftauto.com/index.php?title=DxGetTextColor&action=edit&redlink=1)

- [dxGetTexture](https://wiki.multitheftauto.com/index.php?title=DxGetTexture&action=edit&redlink=1)

- [dxGetTopLevelChildren](https://wiki.multitheftauto.com/index.php?title=DxGetTopLevelChildren&action=edit&redlink=1)

- [dxGetVisible](https://wiki.multitheftauto.com/index.php?title=DxGetVisible&action=edit&redlink=1)

- [dxIsChild](https://wiki.multitheftauto.com/index.php?title=DxIsChild&action=edit&redlink=1)

- [dxIsFront](https://wiki.multitheftauto.com/index.php?title=DxIsFront&action=edit&redlink=1)

- [dxIsInheritedChild](https://wiki.multitheftauto.com/index.php?title=DxIsInheritedChild&action=edit&redlink=1)

- [dxIsObstructed](https://wiki.multitheftauto.com/index.php?title=DxIsObstructed&action=edit&redlink=1)

- [dxIsObstructedByElement](https://wiki.multitheftauto.com/index.php?title=DxIsObstructedByElement&action=edit&redlink=1)

- [dxIsParent](https://wiki.multitheftauto.com/index.php?title=DxIsParent&action=edit&redlink=1)

- [dxIsRootElement](https://wiki.multitheftauto.com/index.php?title=DxIsRootElement&action=edit&redlink=1)

- [dxRemoveClickFunction](https://wiki.multitheftauto.com/index.php?title=DxRemoveClickFunction&action=edit&redlink=1)

- [dxRemoveRenderFunction](https://wiki.multitheftauto.com/index.php?title=DxRemoveRenderFunction&action=edit&redlink=1)

- [dxSendToBack](https://wiki.multitheftauto.com/index.php?title=DxSendToBack&action=edit&redlink=1)

- [dxSetAlpha](https://wiki.multitheftauto.com/index.php?title=DxSetAlpha&action=edit&redlink=1)

- [dxSetCentered](https://wiki.multitheftauto.com/index.php?title=DxSetCentered&action=edit&redlink=1)

- [dxSetColor](https://wiki.multitheftauto.com/index.php?title=DxSetColor&action=edit&redlink=1)

- [dxSetDragArea](https://wiki.multitheftauto.com/index.php?title=DxSetDragArea&action=edit&redlink=1)

- [dxSetGlobalProperty](https://wiki.multitheftauto.com/index.php?title=DxSetGlobalProperty&action=edit&redlink=1)

- [dxSetHoverColor](https://wiki.multitheftauto.com/index.php?title=DxSetHoverColor&action=edit&redlink=1)

- [dxSetIndex](https://wiki.multitheftauto.com/index.php?title=DxSetIndex&action=edit&redlink=1)

- [dxSetMaskEnabled](https://wiki.multitheftauto.com/index.php?title=DxSetMaskEnabled&action=edit&redlink=1)

- [dxSetParent](https://wiki.multitheftauto.com/index.php?title=DxSetParent&action=edit&redlink=1)

- [dxSetPosition](https://wiki.multitheftauto.com/index.php?title=DxSetPosition&action=edit&redlink=1)

- [dxSetProperty](https://wiki.multitheftauto.com/index.php?title=DxSetProperty&action=edit&redlink=1)

- [dxSetSize](https://wiki.multitheftauto.com/index.php?title=DxSetSize&action=edit&redlink=1)

- [dxSetText](https://wiki.multitheftauto.com/index.php?title=DxSetText&action=edit&redlink=1)

- [dxSetTextColor](https://wiki.multitheftauto.com/index.php?title=DxSetTextColor&action=edit&redlink=1)

- [dxSetVisible](https://wiki.multitheftauto.com/index.php?title=DxSetVisible&action=edit&redlink=1)

- [isMouseOverDxElement](https://wiki.multitheftauto.com/index.php?title=IsMouseOverDxElement&action=edit&redlink=1)

### Button

[Template:TDX button functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_button_functions&action=edit&redlink=1)

### Checkbox

[Template:TDX checkbox functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_checkbox_functions&action=edit&redlink=1)

### Circle

[Template:TDX circle functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_circle_functions&action=edit&redlink=1)

### Color Picker

[Template:TDX colorpicker functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_colorpicker_functions&action=edit&redlink=1)

### Image

[Template:TDX image functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_image_functions&action=edit&redlink=1)

### Input

[Template:TDX input functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_input_functions&action=edit&redlink=1)

### Radio Button

[Template:TDX radiobutton functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_radiobutton_functions&action=edit&redlink=1)

### Ring

[Template:TDX ring functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_ring_functions&action=edit&redlink=1)

### Slider

[Template:TDX slider functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_slider_functions&action=edit&redlink=1)

### Text

[Template:TDX text functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_text_functions&action=edit&redlink=1)

### Window

[Template:TDX window functions](https://wiki.multitheftauto.com/index.php?title=Template:TDX_window_functions&action=edit&redlink=1)

# **Events**

- coming soon
