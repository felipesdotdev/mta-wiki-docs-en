---
doc_id: "mta-wiki:10175"
title: "DGS General Basic Properties"
source_title: "DGS General Basic Properties"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_General_Basic_Properties"
revision_id: 79488
language: "en"
categories: []
---

# DGS General Basic Properties

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the general properties of all dgs elements that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alpha

Require a number ranges from 0 to 1. This is equivalent to [dgsSetAlpha](mta://scripting/client/functions/dgssetalpha.md)/[dgsGetAlpha](mta://scripting/client/functions/dgsgetalpha.md).

```
dgsSetProperty(dgsElement,"alpha",alpha = 1)
```

- **alpha:** The visibility/transparency of the DGS element. Ranges from 0 (fully transparent) to 1 (fully opaque). Default value is 0.80.

### clickCoolDown

This property is used to limit the click frequency to a specific dgs element.

```
dgsSetProperty(dgsElement,"clickCoolDown",clickCoolDown = false)
```

- **clickCoolDown:** A number indicates how long you want to limit the click (ms). Set to *false* to disable this.

### changeOrder

Require a bool indicates whether the layer will be changed when being brought to front ( or clicked ).

```
dgsSetProperty(dgsElement,"changeOrder",changeOrder = true)
```

- **changeOrder:** A bool indicates whether the layer will be changed when being brought to front ( or clicked ).

### debugTrace

This property stores the "debug tracing data" includes in which lua **file** and **line** the specific dgs element created (Only available using **loadstring(exports.dgs:dgsImportFunction())()**.

```
dgsSetProperty(dgsElement,"debugTrace",debugTrace)
```

- **debugTrace:** A table stores creation data. Structure is as follows:

```
{
	file=filePath,
	line=lineNum,
	fncName=functionName,
}
```

### enabled

Requires a bool value. This is equivalent to [dgsSetEnabled](mta://scripting/client/functions/dgssetenabled.md)/[dgsGetEnabled](mta://scripting/client/functions/dgsgetenabled.md).

```
dgsSetProperty(dgsElement,"enabled",enabled)
```

- **enabled:** The state.

### enableFullEnterLeaveCheck

Requires a bool value. This determines if target dgs element will have full check of mouse enter/leave. And you should use [onDgsElementEnter](mta://scripting/client/events/ondgselemententer.md)/[onDgsElementLeave](mta://scripting/client/events/ondgselementleave.md) instead of [onDgsMouseEnter](mta://scripting/client/events/ondgsmouseenter.md)/[onDgsMouseLeave](mta://scripting/client/events/ondgsmouseleave.md).

```
dgsSetProperty(dgsElement,"enableFullEnterLeaveCheck",enableFullEnterLeaveCheck)
```

- **enableFullEnterLeaveCheck:** The state.

### functionRunBefore

Requires a bool value. Set whether the function runs before rendering or after rendering (see property **functions**).

```
dgsSetProperty(dgsElement,"functionRunBefore",functionRunBefore)
```

- **functionRunBefore:** Set to true, and the function will run before rendering. Set to false, and the function will run after rendering.

### functions

Requires a string at the 3rd argument. This property runs a function while rendering.

**Predefine Variable**

- **self:** The DGS Element itself.

See example in [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

```
dgsSetProperty(dgsElement,"functions",fncString,arg1,arg2,...)
```

- **fncString:** The string of function to be loaded.

- **arg1:** argument 1

- **arg2:** argument 2

- **...:** other arguments

### childOutsideHit

Requires a bool value. Set whether children elements are clickable when they are outside of their parent element.

```
dgsSetProperty(dgsElement,"childOutsideHit",childOutsideHit = false)
```

- **childOutsideHit:** If set to true, the dgsElement's child elements are clickable even though they are not inside the bounding box of dgsElement.

### ignoreParentTitle

Requires a bool value. Set whether to ignore the title of dgs-dxwindow.

```
dgsSetProperty(dgsElement,"ignoreParentTitle",ignoreParentTitle = false)
```

- **ignoreParentTitle:** Set to true to ignore the title of dgs-dxwindow if its parent is a dgs-dxwindow . Set to false to disable it, which means the y position of dgsElement in dgs-dxwindow will start to be calculated under the title.

### mouseButtons

This property defines the specific mouse buttons that can be used to click on the element.
Syntax:

```
dgsSetProperty(dgsElement, "mouseButtons", {bool left, bool right, bool middle})
```

- **left**: Set this true to enable clicking with the left mouse button. Set it to false to disable clicking with the left mouse button.

- **right**: Set this to true to enable clicking with the right mouse button. Set it to false to disable clicking with the right mouse button.

- **middle**: Set this value to true to enable clicking with the middle mouse button. Set it to false to disable clicking with the middle mouse button.

### outline

The border line of the bounding box of dgs element.

```
dgsSetProperty(dgsElement,"outline",{side,width,color,left,right,top,bottom})
```

- **side** : A string indicates which side the outline will attach to. The available values are as follows:

- **in**

- **center**

- **out**

- **width**: The width of the outline.

- **color**: The color of the outline, which can be transformed by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **left**: Set **true** to show outline in the left, and **false** to hide it. (Default is **true** if not set)

- **right**: Set **true** to show the outline in the right, and **false** to hide it. (Default is **true** if not set)

- **top**: Set **true** to show the outline at the top, and **false** to hide it. (Default is **true** if not set)

- **bottom**: Set **true** to show the outline at the bottom, and **false** to hide it. (Default is **true** if not set)

### renderEventCall

Requires a bool value. Set whether [onDgsElementRender](mta://scripting/client/events/ondgselementrender.md) is triggered when rendering. (Don't always enable this, or it will cause severely performance decrease)

```
dgsSetProperty(dgsElement,"renderEventCall",renderEventCall = false)
```

- **renderEventCall:** Set to true to enable, and false to disable.

### postGUI

Requires a bool value. Set whether the dgs element is post gui when render settings "postGUI" is *nil*(automatic).

```
dgsSetProperty(dgsElement,"postGUI",postGUI)
```

- **postGUI:** Set to true to enable post gui, or it wil under gui.

### visible

This property change the visibility of a dgs element. This is equivalent to [dgsSetVisible](mta://scripting/client/functions/dgssetvisible.md)/[dgsGetVisible](mta://scripting/client/functions/dgsgetvisible.md).

```
dgsSetProperty(dgsElement,"visible",visible)
```

- **visible:** A bool indicates whether the dgs element is visible or not.

## See Also

### General Properties

- DGS General Basic Properties

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- [dgs-dx3dimage](mta://reference/misc/dgs-dx3dimage.md)

- [dgs-dx3dtext](mta://reference/misc/dgs-dx3dtext.md)

- [dgs-dx3dline](mta://reference/misc/dgs-dx3dline.md)

- [dgs-dxbutton](mta://reference/misc/dgs-dxbutton.md)

- [dgs-dxcheckbox](mta://reference/misc/dgs-dxcheckbox.md)

- [dgs-dxcombobox](mta://reference/misc/dgs-dxcombobox.md)

- [dgs-dxdetectarea](mta://reference/misc/dgs-dxdetectarea.md)

- [dgs-dxedit](mta://reference/misc/dgs-dxedit.md)

- [dgs-dxgridlist](mta://reference/misc/dgs-dxgridlist.md)

- [dgs-dximage](mta://reference/misc/dgs-dximage.md)

- [dgs-dxlabel](mta://reference/misc/dgs-dxlabel.md)

- [dgs-dxline](mta://reference/misc/dgs-dxline.md)

- [dgs-dxmemo](mta://reference/misc/dgs-dxmemo.md)

- [dgs-dxprogressbar](mta://reference/misc/dgs-dxprogressbar.md)

- [dgs-dxradiobutton](mta://reference/misc/dgs-dxradiobutton.md)

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
