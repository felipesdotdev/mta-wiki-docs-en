---
doc_id: "mta-wiki:11622"
title: "Dgs-dxscrollbar"
source_title: "Dgs-dxscrollbar"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxscrollbar"
revision_id: 80089
language: "en"
categories: []
generated_at: "2026-07-26T16:11:23.239486+00:00"
---

# Dgs-dxscrollbar

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxscrollbar that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### arrowWidth

This property adjusts the width of arrow ( take vertical scroll bar as a standard ).

```
dgsSetProperty(scrollbar,"arrowWidth",{arrowWidth,relative})
```

- **arrowWidth:** A number of the width of arrow, which is affected by **relative**.

- **relative:** A bool of whether the width is relative or not. If this is true, then length must be between 0 and 1.

### arrowColor

The arrow color of scroll bar, includes normal, hovering, click.

```
dgsSetProperty(scrollbar,"arrowColor",{arrowColorNormal,arrowColorHover,arrowColorClick})
```

- **arrowColorNormal:** An integer of the arrow color, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **arrowColorHover:** An integer of the arrow color when the mouse's cursor is hovering on it, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **arrowColorClick:** An integer of the arrow color when the arrow gets clicked, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### arrowImage

The arrow image of scroll bar.

```
dgsSetProperty(scrollbar,"arrowImage",arrowImage)
```

- **arrowImage:** A material element of the arrow image of scroll bar.

### cursorColor

The cursor color of scroll bar, includes normal, hovering, click.

```
dgsSetProperty(scrollbar,"cursorColor",{cursorColorNormal,cursorColorHover,cursorColorClick})
```

- **cursorColorNormal:** An integer of the cursor color, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **cursorColorHover:** An integer of the cursor color when the mouse's cursor is hovering on it, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **cursorColorClick:** An integer of the cursor color when the cursor gets clicked, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### cursorImage

The cursor image of scroll bar.

```
dgsSetProperty(scrollbar,"cursorImage",cursorImage)
```

- **cursorImage:** A material element of the cursor image of scroll bar.

### cursorWidth

This property adjusts the width of cursor ( take vertical scroll bar as a standard ).

```
dgsSetProperty(scrollbar,"cursorWidth",{cursorWidth,relative})
```

- **cursorWidth:** A number of the width of cursor, which is affected by **relative**.

- **relative:** A bool of whether the width is relative or not. If this is true, then length must be between 0 and 1.

### grades

This property stores the grades of scroll bar. *See [dgsScrollBarSetGrades](mta://scripting/client/functions/dgsscrollbarsetgrades.md)/[dgsScrollBarGetGrades](mta://scripting/client/functions/dgsscrollbargetgrades.md)*

```
dgsSetProperty(scrollbar,"grades",grades)
```

- **grades:** A number of the grades of scroll bar.

### currentGrade

This property stores the current grade of scroll bar if *grades* enabled.

```
dgsSetProperty(scrollbar,"currentGrade",currentGrade)
```

- **currentGrade:** A number of the current grade, ranges from 0 to *grades*.

### image

The image of scroll bar, includes arrow, cursor and trough.

```
dgsSetProperty(scrollbar,"image",{arrowImage,cursorImage,troughImage})
```

- **arrowImage:** A texture of the image of arrow.

- **cursorImage:** A texture of the image of cursor.

- **troughImage:** A texture of the image of trough.

### imageRotation

This property solves the problem of the rotation of the images.

```
dgsSetProperty(scrollbar,"imageRotation",{Horizontal,Vertical})
```

- **Horizontal:** A table includes arrowImageRotation,cursorImageRotation,troughImageRotation of horizontal scroll bar, by default:

```
{0,270,270}
```

- **Vertical:** A table includes arrowImageRotation,cursorImageRotation,troughImageRotation of vertical scroll bar, by default:

```
{270,0,0}
```

### cursorLength

This property determines whether the length of the cursor of scroll bar.

```
dgsSetProperty(scrollbar,"cursorLength",{cursorLength,relative})
```

- **cursorLength:** A number of the length of scroll bar, which is affected by **relative**.

- **relative:** A bool of whether the length is relative or not. If this is true, then length must be between 0 and 1.

### locked

This is equivalent to [dgsScrollBarSetLocked](mta://scripting/client/functions/dgsscrollbarsetlocked.md)/[dgsScrollBarGetLocked](mta://scripting/client/functions/dgsscrollbargetlocked.md).

```
dgsSetProperty(scrollbar,"locked",locked)
```

- **locked:** A bool of whether the scroll bar get locked or not.

### map

This property will map the value from 0~100 to mapMin~mapMax (Both get and set scroll position).

```
dgsSetProperty(scrollbar,"map",{mapMin,mapMax})
```

- **mapMin:** A number of the min value.

- **mapMax:** A number of the max value.

### multiplier

This property determines whether how much a scroll bar will scroll when you click the arrow or use mouse wheel.

This property is difficult to understand. Before use this property, do an experiment first.

```
dgsSetProperty(scrollbar,"multiplier",{multiplier,relative})
```

- **multiplier:** A number of the multiplier of scroll bar, which is affected by **relative**.

- **relative:** A bool of whether the multiplier is relative or not. If this is true, then multiplier must be between 0 and 1.

### scrollPosition

This is equivalent to [dgsScrollBarSetScrollPosition](mta://scripting/client/functions/dgsscrollbarsetscrollposition.md)/[dgsScrollBarGetScrollPosition](mta://scripting/client/functions/dgsscrollbargetscrollposition.md).

```
dgsSetProperty(scrollbar,"scrollPosition",scrollPosition)
```

- **scrollPosition:** An integer of the scroll poisition of the scroll bar. Ranges from 0 to 100.

### scrollArrow

This property indicates whether enable the scroll arrow or not. It is useful when making scroll bar act as slide or something else.

```
dgsSetProperty(scrollbar,"scrollArrow",scrollArrow)
```

- **scrollArrow:** A bool of whether enable the scroll arrow or not.

### troughClickAction

This property determines what will the scroll bar do when you click the trough.

```
dgsSetProperty(scrollbar,"troughClickAction",troughClickAction)
```

- **troughClickAction:** A string. Available values are as follows:

- **none:** No actions.

- **step:** Step up or down.

- **jump:** Make cursor of scroll bar jump to the current place you click.

### troughColor

The trough color of scroll bar.

```
dgsSetProperty(scrollbar,"troughColor",{troughColorPart1,troughColorPart2})
```

- **troughColorPart1:** An integer of the trough color on the left/top side of the cursor, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

- **troughColorPart2:** An integer of the trough color on the right/bottom side of the cursor, which can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### troughImageSectionMode

This property will toggle section mode or stretch mode.

```
dgsSetProperty(scrollbar,"troughImageSectionMode",troughImageSectionMode)
```

- **troughImageSectionMode:** A bool indicates whether to enable section mode of the image or keep stretch mode of the trough image.

### troughWidth

This property adjusts the width of trough ( take vertical scroll bar as a standard ).

```
dgsSetProperty(scrollbar,"troughWidth",{troughWidth,relative})
```

- **troughWidth:** A number of the width of arrow, which is affected by **relative**.

- **relative:** A bool of whether the width is relative or not. If this is true, then length must be between 0 and 1.

### troughImage

The trough image of scroll bar.

```
dgsSetProperty(scrollbar,"troughImage",troughImage)
```

- **troughImage:** A material element of the trough image of scroll bar.

### wheelReversed

This property determines whether the increasing/decreasing direction is reversed when using mouse wheel.

```
dgsSetProperty(scrollbar,"wheelReversed",wheelReversed)
```

- **wheelReversed:** A bool indicates whether the increasing/decreasing direction is reversed when using mouse wheel.

### isHorizontal

This property determines whether the scroll bar is horizontal or vertical.

```
dgsSetProperty(scrollbar,"isHorizontal",isHorizontal)
```

- **isHorizontal:** Available values are as follows:

- **false:** vertical

- **true:** horizontal

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

- dgs-dxscrollbar

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
