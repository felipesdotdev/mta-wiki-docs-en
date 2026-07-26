---
doc_id: "mta-wiki:9616"
title: "Dgs-dxbutton"
source_title: "Dgs-dxbutton"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxbutton"
revision_id: 78566
language: "en"
categories: []
---

# Dgs-dxbutton

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxbutton that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the button.

```
dgsSetProperty(button,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the text within the button. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the text within the button. Can be "top", "center" or "bottom".

### clickOffset

The offset indicates that how much the text of the button will shift when it is clicked.

```
dgsSetProperty(button,"clickOffset",{offsetX,offsetY})
```

- **offsetX** : A float of the 2D X offset relative to the position of the button.

- **offsetY** : A float of the 2D Y offset relative to the position of the button.

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background of the button.

```
dgsSetProperty(button,"color",{normalColor,hoveringColor,clickedColor})
```

- **normalColor:** An integer of the color of the background of the button ( neither selected nor clicked by mouse ).

- **hoveringColor:** An integer of the color of the background of the button which is selected.

- **clickedColor:** An integer of the color of the background of the button which is clicked.

### disabledColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background of the button when disabled.

```
dgsSetProperty(button,"disabledColor",disabledColor)
```

- **disabledColor:** An integer of the color of the background of the button when disabled.

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(button,"colorCoded",colorCoded)
```

- **colorCoded** : Set to true to enable embedded #FFFFFF color codes.

### colorTransitionPeriod

This property sets the transition period among colors (normal, hovering, clicked).

```
dgsSetProperty(button,"colorTransitionPeriod",colorTransitionPeriod)
```

- **colorTransitionPeriod** : An integer indicates the transition time in miliseconds. ( Set to 0 to disable )

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(button,"font",font)
```

- **font** : A [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the button.

### iconAlignment

Alignment of the icon within the button.

```
dgsSetProperty(button,"iconAlignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the icon within the button. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the icon within the button. Can be "top", "center" or "bottom".

### iconColor

This property enables you to change the icon color (Work with **iconImage**).

```
dgsSetProperty(button,"iconColor",{normalColor,hoveringColor,clickedColor})
```

- **normalColor:** An integer of the color of the icon image of the button ( neither selected nor clicked by mouse ).

- **hoveringColor:** An integer of the color of the icon image of the button which is selected.

- **clickedColor:** An integer of the color of the icon image of the button which is clicked.

### iconImage

Require [texture/shader] that can be used as the icon image of button.

```
dgsSetProperty(button,"iconImage",{normalImage,hoveringImage,clickedImage})
```

- **normalImage:** A texture/shader element of the icon image of the button ( neither selected nor clicked by mouse ). ( You can pass a nil value to disable this option )

- **hoveringImage:** A texture/shader element of the  icon image of the button which is selected. ( You can pass a nil value to disable this option )

- **clickedImage:** A texture/shader element of the  icon image of the button which is clicked. ( You can pass a nil value to disable this option )

### iconOffset

This property enables you to change the offset of the icon from the text (Work with **iconImage**).

```
dgsSetProperty(button,"iconOffset",{iconOffsetX,iconOffsetY,relative})
```

- **iconOffsetX** : An integer of the 2D X offset in pixels to the position of the icon.

- **iconOffsetY** : An integer of the 2D Y offset in pixels to the position of the icon.

- **relative** : A bool of whether the iconOffset is relative to the height of text or absolute pixels.

### iconRelative

This property determines whether the icon is relative to the text or button.

```
dgsSetProperty(button,"iconRelative",iconRelative)
```

- **iconRelative:** A bool  determines whether the icon is relative to the text or button.

### iconShadow

The shadow icon image of the button.

```
dgsSetProperty(button,"iconShadow",{offsetX,offsetY,color})
```

- **offsetX** : A float of the 2D X offset of the shadow icon of the button.

- **offsetY** : A float of the 2D Y offset of the shadow icon of the button.

- **color** : An integer of the color of the shadow icon of the button.

### iconSize

This property enables you to change the icon size (Work with **iconImage**).

```
dgsSetProperty(button,"iconSize",{iconSizeX,iconSizeY,relative})
```

- **iconSizeX** : A number of the 2D X scale to the size of the icon image.

- **iconSizeY** : A number of the 2D Y scale to the size of the icon image.

- **relative** : A bool of whether the iconSize is relative to the height of text or absolute pixels.

### image

Require [texture/shader] that can be used as the background of button.

```
dgsSetProperty(button,"image",image)
```

- **image:** A texture/shader element of the background of the button

Or

```
dgsSetProperty(button,"image",{normalImage,hoveringImage,ClickedImage})
```

- **normalImage:** A texture/shader element of the background of the button ( neither selected nor clicked by mouse ). ( You can pass a nil value to disable this image option )

- **hoveringImage:** A texture/shader element of the background of the button which is selected. ( You can pass a nil value to disable this image option )

- **clickedImage:** A texture/shader element of the background of the button which is clicked. ( You can pass a nil value to disable this image option )

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(button,"text",text)
```

- **text** : A string of the text of the button.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the button.

```
dgsSetProperty(button,"textColor",textColor)
```

- **textColor** : An integer of the color of the text of the button.

### textOffset

The offset of the text on button.

```
dgsSetProperty(button,"textOffset",{offsetX,offsetY,relative})
```

- **offsetX** : A float of the 2D X offset relative to the position of the button, depends on **relative**.

- **offsetY** : A float of the 2D Y offset relative to the position of the button, depends on **relative**.

- **relative** : A bool of whether the offset is relative or absolute.

### textPadding

The text padding of the text on button.

```
dgsSetProperty(button,"textPadding",{offsetX,offsetY,relative})
```

- **textPaddingX** : A float of the 2D horizontal padding relative to the size of the button, depends on **relative**.

- **textPaddingY** : A float of the 2D vertical padding offset relative to the size of the button, depends on **relative**.

- **relative** : A bool of whether the padding is relative or absolute.

### textSize

The scale of the text of the button. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(button,"textSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X scale of the text of the button.

- **scaleY** : A float of the 2D Y scale of the text of the button.

### shadow

The shadow text of the button.

```
dgsSetProperty(button,"shadow",{offsetX,offsetY,color})
```

- **offsetX** : A float of the 2D X offset of the shadow text of the button.

- **offsetY** : A float of the 2D Y offset of the shadow text of the button.

- **color** : An integer of the color of the shadow text of the button.

### wordBreak

Whether the word-break is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(button,"wordBreak",wordBreak)
```

- **wordBreak** : If set to true, the text will wrap to a new line whenever it reaches the right side of the bounding box. If false, the text will always be completely on one line.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- [dgs-dx3dimage](mta://reference/misc/dgs-dx3dimage.md)

- [dgs-dx3dtext](mta://reference/misc/dgs-dx3dtext.md)

- [dgs-dx3dline](mta://reference/misc/dgs-dx3dline.md)

- dgs-dxbutton

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
