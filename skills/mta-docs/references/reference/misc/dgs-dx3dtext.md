---
doc_id: "mta-wiki:11621"
title: "Dgs-dx3dtext"
source_title: "Dgs-dx3dtext"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dx3dtext"
revision_id: 73131
language: "en"
categories: []
---

# Dgs-dx3dtext

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dx3dtext that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the 3d text.

```
dgsSetProperty(text3D,"alignment",{alignX,alignY})
```

- **alignX** : Horizontal alignment of the text within the 3d text. Can be "left", "center" or "right".

- **alignY** : Vertical alignment of the text within the 3d text. Can be "top", "center" or "bottom".

### canBeBlocked

This property determines what can block the 3d text, see [isLineOfSightClear](mta://scripting/client/functions/islineofsightclear.md).

```
dgsSetProperty(text3D,"canBeBlocked",canBeBlocked)
```

- **canBeBlocked:**  A table or bool that determines what can block the 3d text, available options are as follows:

- **true:** Everything can block the 3d text.

- **false:** Nothing can block the 3d text.

- *table* has following keys:

- **checkBuildings:** Allow the line of sight to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkVehicles:** Allow the line of sight to be blocked by [vehicles](https://wiki.multitheftauto.com/index.php?search=vehicles).

- **checkPeds:** Allow the line of sight to be blocked by peds, i.e. [players](https://wiki.multitheftauto.com/index.php?search=players).

- **checkObjects:** Allow the line of sight to be blocked by [objects](https://wiki.multitheftauto.com/index.php?search=objects).

- **checkDummies:** Allow the line of sight to be blocked by GTA's internal dummies.  These are not used in the current MTA version so this argument can be set to *false*.

- **seeThroughStuff:** Allow the line of sight to **pass through** collision materials that have this flag enabled (By default material IDs 52, 55 and 66 which are some fences). This flag originally allows some objects to be walked on but you can shoot throug them.

- **ignoreSomeObjectsForCamera:** Allow the line of sight to **pass through** objects that have (K) property enabled in "object.dat" data file. (i.e. Most dynamic objects like boxes or barrels)

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the dx 3d text.

```
dgsSetProperty(text3D,"color",color)
```

- **color:**  An integer of the color of the dx 3d text.

### dimension

The dimension of dx 3d text. Players can't see the dx 3d text in different dimensions.

```
dgsSetProperty(text3D,"dimension",dimension)
```

- **dimension:**  An integer of the dimension of dx 3d text.

### fadeDistance

The distance of which 3D text starts to fading.

```
dgsSetProperty(text3D,"fadeDistance",fadeDistance)
```

- **fadeDistance:** A float of the fade distance.

### fixTextSize

This property keeps the text size on screen rather than let the text size change with distance.

```
dgsSetProperty(text3D,"fixTextSize",fixTextSize)
```

- **fixTextSize:** A bool of whether fix the text size.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(text3D,"font",font)
```

- **font** : A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the dx 3d text.

### interior

The interior of dx 3d text. Players can't see the dx 3d text in different interiors.

```
dgsSetProperty(text3D,"interior",interior)
```

- **interior:**  An integer of the interior of dx 3d text.

### isBlocked

This property indicates whether the 3d text is blocked or not, which is only recommended to read.

```
dgsSetProperty(text3D,"isBlocked",isBlocked)
```

- **isBlocked:**  A bool value indicates whether the 3d text is blocked.

### isOnScreen

This property indicates whether the 3d text is on screen or not, which is only recommended to read.

```
dgsSetProperty(text3D,"isOnScreen",isOnScreen)
```

- **isOnScreen:** A bool value indicates whether the 3d text is on screen.

### maxDistance

The maximum visible distance in the world.

```
dgsSetProperty(text3D,"maxDistance",maxDistance)
```

- **maxDistance:** A float of the distance.

### text

This property stores the text of 3d text.

```
dgsSetProperty(text3D,"text",text)
```

- **text** : A string of the text of 3d text

### textOffset

The offset of the 3d text.

```
dgsSetProperty(text3D,"textOffset",{offsetX,offsetY})
```

- **offsetX** : A float of the 2D X offset relative to the position of the 3d text.

- **offsetY** : A float of the 2D Y offset relative to the position of the 3d text.

### textSize

The scale of the text of the dx 3d text. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(text3D,"textSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X scale of the text of the dx 3d text.

- **scaleY** : A float of the 2D Y scale of the text of the dx 3d text.

### position

A table stores x,y,z coordinate of the dx 3d text in the world.

```
dgsSetProperty(text3D,"position",{x,y,z})
```

- **x:** The x coordinate of the destination.

- **y:** The y coordinate of the destination.

- **z:** The z coordinate of the destination.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- [dgs-dx3dimage](mta://reference/misc/dgs-dx3dimage.md)

- dgs-dx3dtext

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
