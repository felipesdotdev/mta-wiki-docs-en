---
doc_id: "mta-wiki:12208"
title: "Dgs-dxprogressbar"
source_title: "Dgs-dxprogressbar"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxprogressbar"
revision_id: 82392
language: "en"
categories: []
---

# Dgs-dxprogressbar

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxlabel that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### bgColor

This property determines the background color of the progress bar.

```
dgsSetProperty(progressbar,"bgColor",bgColor)
```

- **bgColor** : An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the background image of the progress bar.

```
dgsSetProperty(progressbar,"bgImage",bgImage)
```

- **bgImage** : A material element that serves as the background image of the progress bar (texture/shader/screen source/renderTarget).

### indicatorColor

This property determines the indicator color of the progress bar.

```
dgsSetProperty(progressbar,"indicatorColor",indicatorColor)
```

- **indicatorColor** : An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### indicatorImage

This property determines the indicator image of the progress bar.

```
dgsSetProperty(progressbar,"indicatorImage",indicatorImage)
```

- **indicatorImage** : A material element that serves as the indicator image of the progress bar (texture/shader/screen source/renderTarget).

### indicatorMode

This property determines the indicator mode of the progress bar. See [dgsProgressBarSetMode](mta://scripting/client/functions/dgsprogressbarsetmode.md)/[dgsProgressBarGetMode](mta://scripting/client/functions/dgsprogressbargetmode.md).

```
dgsSetProperty(progressbar,"indicatorMode",indicatorMode)
```

- **indicatorMode** : A bool indicates if indicator image uses clip mode or stretch mode. (false for stretch, true for clip)

### padding

This property determines the padding of the progress bar.

```
dgsSetProperty(progressbar,"padding",{paddingX,paddingY})
```

- **paddingX** : An integer of 2D x padding value.

- **paddingY** : An integer of 2D y padding value.

### progress

This property stores the progress value of progress bar.

```
dgsSetProperty(progressbar,"progress",progress)
```

- **progress** : A float of progress value.

### progressReverse

This property determines if the progress value is reversed.

```
dgsSetProperty(progressbar,"progressReverse",progressReverse)
```

- **progressReverse** : A bool indicates if the progress value is from 0 to 100 or 100 to 0.

### style

This property stores the style name of progress bar, to change the style use [dgsProgressBarSetStyle](mta://scripting/client/functions/dgsprogressbarsetstyle.md).

```
dgsSetProperty(progressbar,"style",style)
```

- **style** : A string of the style name.

## Style Properties

### >Style:normal-horizontal<

None

### >Style:normal-vertical<

None

### >Style:ring-round<

#### antiAliased

This style property determines the anti aliasing of the ring.

```
dgsSetProperty(progressbar,"antiAliased",antiAliased)
```

- **antiAliased:** A float of the anti aliasing of the ring.

#### bgProgress

This style property determines the progress of the background of the ring.

```
dgsSetProperty(progressbar,"bgProgress",bgProgress)
```

- **bgProgress:** A float of the progress of the background of the ring.

#### bgRadius

This style property determines the radius of the background of the ring.

```
dgsSetProperty(progressbar,"bgRadius",bgRadius)
```

- **bgRadius:** A float of the radius of the background of the ring.

#### bgRotation

This style property determines the rotation of the background of the ring.

```
dgsSetProperty(progressbar,"bgRotation",bgRotation)
```

- **bgRotation:** A float of the rotation of the background of the ring.

#### bgThickness

This style property determines the thickness of the background of the ring.

```
dgsSetProperty(progressbar,"bgThickness",bgThickness)
```

- **bgThickness:** A float of the thickness of the background of the ring.

#### elements

This style property stores the custom elements of the progress bar.

```
dgsSetProperty(progressbar,"elements",elements)
```

- **elements:** A table of elements. Built-in elements are as follows:

- **elements.circleShader:** A shader of ring-round style.

#### isClockwise

This style property determines whether the progress direction is clockwise or anti-clockwise .

```
dgsSetProperty(progressbar,"isClockwise",isClockwise)
```

- **isClockwise:** A bool of whether the progress direction is clockwise or anti-clockwise.

#### radius

This style property determines the radius of the ring.

```
dgsSetProperty(progressbar,"radius",radius)
```

- **radius:** A float of the radius of the ring.

#### rotation

This style property determines the rotation of the ring.

```
dgsSetProperty(progressbar,"rotation",rotation)
```

- **rotation:** A float of the rotation of the ring.

#### thickness

This style property determines the thickness of the ring.

```
dgsSetProperty(progressbar,"thickness",thickness)
```

- **radius:** A float of the thickness of the ring.

### >Style:ring-plain<

#### antiAliased

This style property determines the anti aliasing of the ring.

```
dgsSetProperty(progressbar,"antiAliased",antiAliased)
```

- **antiAliased:** A float of the anti aliasing of the ring.

#### bgProgress

This style property determines the progress of the background of the ring.

```
dgsSetProperty(progressbar,"bgProgress",bgProgress)
```

- **bgProgress:** A float of the progress of the background of the ring.

#### bgRadius

This style property determines the radius of the background of the ring.

```
dgsSetProperty(progressbar,"bgRadius",bgRadius)
```

- **bgRadius:** A float of the radius of the background of the ring.

#### bgRotation

This style property determines the rotation of the background of the ring.

```
dgsSetProperty(progressbar,"bgRotation",bgRotation)
```

- **bgRotation:** A float of the rotation of the background of the ring.

#### bgThickness

This style property determines the thickness of the background of the ring.

```
dgsSetProperty(progressbar,"bgThickness",bgThickness)
```

- **bgThickness:** A float of the thickness of the background of the ring.

#### elements

This style property stores the custom elements of the progress bar.

```
dgsSetProperty(progressbar,"elements",elements)
```

- **elements:** A table of elements. Built-in elements are as follows:

- **elements.circleShader:** A shader of ring-round style.

#### isClockwise

This style property determines whether the progress direction is clockwise or anti-clockwise.

```
dgsSetProperty(progressbar,"isClockwise",isClockwise)
```

- **isClockwise:** A bool of whether the progress direction is clockwise or anti-clockwise.

#### radius

This style property determines the radius of the ring.

```
dgsSetProperty(progressbar,"radius",radius)
```

- **radius:** A float of the radius of the ring.

#### rotation

This style property determines the rotation of the ring.

```
dgsSetProperty(progressbar,"rotation",rotation)
```

- **rotation:** A float of the rotation of the ring.

#### thickness

This style property determines the thickness of the ring.

```
dgsSetProperty(progressbar,"thickness",thickness)
```

- **thickness:** A float of the thickness of the ring.

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

- dgs-dxprogressbar

- [dgs-dxradiobutton](mta://reference/misc/dgs-dxradiobutton.md)

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
