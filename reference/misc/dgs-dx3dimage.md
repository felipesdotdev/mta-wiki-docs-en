---
doc_id: "mta-wiki:12698"
title: "Dgs-dx3dimage"
source_title: "Dgs-dx3dimage"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dx3dimage"
revision_id: 73129
language: "en"
categories: []
generated_at: "2026-07-26T16:11:21.550961+00:00"
---

# Dgs-dx3dimage

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dx3dimage that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### canBeBlocked

This property determines what can block the 3d image, see [isLineOfSightClear](mta://scripting/client/functions/islineofsightclear.md).

```
dgsSetProperty(image3D,"canBeBlocked",canBeBlocked)
```

- **canBeBlocked:**  A table or bool that determines what can block the 3d image, available options are as follows:

- **true:** Everything can block the 3d image.

- **false:** Nothing can block the 3d image.

- *table* has following keys:

- **checkBuildings:** Allow the line of sight to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkVehicles:** Allow the line of sight to be blocked by [vehicles](mta://reference/misc/vehicle.md).

- **checkPeds:** Allow the line of sight to be blocked by peds, i.e. [players](mta://reference/misc/player.md).

- **checkObjects:** Allow the line of sight to be blocked by [objects](mta://reference/misc/object.md).

- **checkDummies:** Allow the line of sight to be blocked by GTA's internal dummies.  These are not used in the current MTA version so this argument can be set to *false*.

- **seeThroughStuff:** Allow the line of sight to **pass through** collision materials that have this flag enabled (By default material IDs 52, 55 and 66 which are some fences). This flag originally allows some objects to be walked on but you can shoot throug them.

- **ignoreSomeObjectsForCamera:** Allow the line of sight to **pass through** objects that have (K) property enabled in "object.dat" data file. (i.e. Most dynamic objects like boxes or barrels)

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the 3d image.

```
dgsSetProperty(image3D,"color",color)
```

- **color:**  An integer of the color of the 3d image.

### dimension

The dimension of 3d image. Players can't see the 3d image in different dimensions.

```
dgsSetProperty(image3D,"dimension",dimension)
```

- **dimension:**  An integer of the dimension of 3d image.

### fadeDistance

The distance of which 3D image starts to fading.

```
dgsSetProperty(image3D,"fadeDistance",fadeDistance)
```

- **fadeDistance:** A float of the fade distance.

### fixImageSize

This property keeps the image size on screen rather than let the image size change with distance.

```
dgsSetProperty(image3D,"fixImageSize",fixImageSize)
```

- **fixImageSize:** A bool of whether fix the image size.

### image

This property stores the image of 3d image.

```
dgsSetProperty(image3D,"image",image)
```

- **image:** An texture element such as texture, render target, screen source, shader and so on. Or texture path. Or nil (color only).

### imageSize

The scale of the image of the 3d image.

```
dgsSetProperty(image3D,"imageSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X size of the image of the 3d image ( Width in pixels on screen at the distance of 50 unit in game ).

- **scaleY** : A float of the 2D Y size of the image of the 3d image ( Height in pixels on screen at the distance of 50 unit in game ).

### interior

The interior of 3d image. Players can't see the 3d image in different interiors.

```
dgsSetProperty(image3D,"interior",interior)
```

- **interior:**  An integer of the interior of 3d image.

### isBlocked

This property indicates whether the 3d image is blocked or not, which is only recommended to read.

```
dgsSetProperty(image3D,"isBlocked",isBlocked)
```

- **isBlocked:**  A bool value indicates whether the 3d image is blocked.

### isOnScreen

This property indicates whether the 3d image is on screen or not, which is only recommended to read.

```
dgsSetProperty(image3D,"isOnScreen",isOnScreen)
```

- **isOnScreen:** A bool value indicates whether the 3d image is on screen.

### maxDistance

The maximum visible distance in the world.

```
dgsSetProperty(image3D,"maxDistance",maxDistance)
```

- **maxDistance:** A float of the distance.

### position

A table stores x,y,z coordinate of the 3d image in the world.

```
dgsSetProperty(image3D,"position",{x,y,z})
```

- **x:** The x coordinate of the destination.

- **y:** The y coordinate of the destination.

- **z:** The z coordinate of the destination.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- dgs-dx3dimage

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
