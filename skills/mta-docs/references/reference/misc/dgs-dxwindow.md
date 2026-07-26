---
doc_id: "mta-wiki:10201"
title: "Dgs-dxwindow"
source_title: "Dgs-dxwindow"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxwindow"
revision_id: 74457
language: "en"
categories: []
---

# Dgs-dxwindow

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxwindow that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the title text of the window.

The functions as follows are based on this property.

[dgsWindowSetHorizontalAlign](mta://scripting/client/functions/dgswindowsethorizontalalign.md)/[dgsWindowGetHorizontalAlign](mta://scripting/client/functions/dgswindowgethorizontalalign.md)

[dgsWindowSetVerticalAlign](mta://scripting/client/functions/dgswindowsetverticalalign.md)/[dgsWindowGetVerticalAlign](mta://scripting/client/functions/dgswindowgetverticalalign.md)

```
dgsSetProperty(window,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the title text of the windowl. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the title text of the window. Can be "top", "center" or "bottom".

### borderSize

This property determines the border size in pixels which is used to resize the window.

```
dgsSetProperty(window,"borderSize",borderSize)
```

- **borderSize:** An integer of the size of the border of the window in pixels.

### closeButtonEnabled

This property determines whether the close button of window is enabled or not.

```
dgsSetProperty(window,"closeButtonEnabled",closeButtonEnabled)
```

- **closeButtonEnabled:** A bool of whether close button is enabled or not.

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background of the window.

```
dgsSetProperty(window,"color",color)
```

- **color:** An integer of the color of the background of the window.

### colorCoded

Whether the color code in the title text is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(window,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(window,"font",font)
```

- **font:** A [dx font element](mta://reference/misc/element-dx-font.md) of the title text font of the window.

### ignoreTitle

This property determines whether to ignore the window title when calculating window's child elements (useful for gui to dgs).

```
dgsSetProperty(window,"ignoreTitle",ignoreTitle)
```

- **ignoreTitle:** A bool of the state of whether to ignore the window title.

### image

The texture element(texture/render target/screen source/shader etc) of the background of the window.

```
dgsSetProperty(window,"image",image)
```

- **image:** A texture element of the background of the window.

### maxSize

This property determines the maximum width and height of the window that users can resize to.

```
dgsSetProperty(window,"maxSize",{maxWidth,maxHeight})
```

- **maxWidth:** An integer of the maximum width of the window.

- **maxHeight:** An integer of the maximum height of the window.

### minSize

This property determines the minimum width and height of the window that users can resize to.

```
dgsSetProperty(window,"minSize",{minWidth,minHeight})
```

- **minWidth:** An integer of the minimum width of the window.

- **minHeight:** An integer of the minimum height of the window.

### movable

This is equivalent to [dgsWindowSetMovable](mta://scripting/client/functions/dgswindowsetmovable.md), which allows you to specify whether or not a user can move a DGS window.

```
dgsSetProperty(window,"movable",movable)
```

- **movable:** A boolean value indicating whether user can move the window or not.

### sizable

This is equivalent to [dgsWindowSetSizable](mta://scripting/client/functions/dgswindowsetsizable.md), which allows you to specify whether or not a user can resize a DGS window.

```
dgsSetProperty(window,"sizable",sizable)
```

- **movable:** A boolean value indicating whether user can resize the window or not.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(window,"text",text)
```

- **text:** A string of the title text of the window.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the title text of the window.

```
dgsSetProperty(window,"textColor",textColor)
```

- **textColor:** An integer of the color of the title text of the window.

### textOffset

The offset of the title text of window.

```
dgsSetProperty(window,"textOffset",{offsetX,offsetY,relative})
```

- **offsetX** : A float of the 2D X offset relative to the position of the text of window, depends on **relative**.

- **offsetY** : A float of the 2D Y offset relative to the position of the text of window, depends on **relative**.

- **relative** : A bool of whether the offset is relative or absolute.

### textSize

The scale of the **title** *text* of the window. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(window,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the title text of the window.

- **scaleY:** A float of the 2D Y scale of the title text of the window.

### titleColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the **title** of the window when the window is **focused** ( For **blurred**, see [titleColorBlur](#titleColorBlur) ).

```
dgsSetProperty(window,"titleColor",titleColor)
```

- **titleColor:** An integer of the color of the title of the focused window.

### titleColorBlur

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the title of the window when the window is **blurred**.

```
dgsSetProperty(window,"titleColorBlur",titleColorBlur)
```

- **titleColorBlur:** An integer of the color of the title of the blurred window. Set to *nil* to disable blur color.

### titleHeight

This property determines the title size in pixels which is also used to move the window.

```
dgsSetProperty(window,"titleHeight",titleHeight)
```

- **titleHeight:** An integer of the size of the title of the window in pixels.

### titleImage

The texture element(texture/render target/screen source/shader etc) of the title background of the window.

```
dgsSetProperty(window,"titleImage",titleImage)
```

- **titleImage:** A texture element of the title background of the window.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

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

- dgs-dxwindow

### Extra Properties For DGS Plugins
