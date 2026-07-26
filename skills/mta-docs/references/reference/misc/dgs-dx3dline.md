---
doc_id: "mta-wiki:13633"
title: "Dgs-dx3dline"
source_title: "Dgs-dx3dline"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dx3dline"
revision_id: 74320
language: "en"
categories: []
---

# Dgs-dx3dline

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dx3dline that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the default color of the 3d line. If the color of item is not specified, this color will be used.

```
dgsSetProperty(line3D,"color",color)
```

- **color:** An integer of the color of the 3d line.

### dimension

The dimension of 3d line. Players can't see the 3d line in different dimensions.

```
dgsSetProperty(line3D,"dimension",dimension)
```

- **dimension:**  An integer of the dimension of 3d line.

### fadeDistance

The distance of which 3d line starts to fading.

```
dgsSetProperty(line3D,"fadeDistance",fadeDistance)
```

- **fadeDistance:** A float of the fade distance.

### interior

The interior of 3d line. Players can't see the 3d line in different interiors.

```
dgsSetProperty(line3D,"interior",interior)
```

- **interior:**  An integer of the interior of 3d line.

### maxDistance

The maximum visible distance in the world.

```
dgsSetProperty(line3D,"maxDistance",maxDistance)
```

- **maxDistance:** A float of the distance.

### position

A table stores x,y,z coordinate of the 3d line in the world.

```
dgsSetProperty(line3D,"position",{x,y,z})
```

- **x:** The x coordinate of the destination.

- **y:** The y coordinate of the destination.

- **z:** The z coordinate of the destination.

### rotation

A table stores rotation x,y,z coordinate of the 3d line in the world.

```
dgsSetProperty(line3D,"rotation",{rx,ry,rz})
```

- **rx:** The x coordinate of the rotation.

- **ry:** The y coordinate of the rotation.

- **rz:** The z coordinate of the rotation.

### lineData

A table stores the line data of 3d line

```
dgsSetProperty(line3D,"lineData",lineData)
```

- **lineData:** A table stores all line data.

**Data Structure**

```
--- If StartXYZ don't exist, will use last endXYZ or 0,0,0
{
	{ startX, startY,	startZ, endX, endY, endZ, width, color },
	{ startX, startY,	startZ, endX, endY, endZ, width, color },
	...
}
```

### lineWidth

An float of the default width of 3d line. If the width of item is not specified, this width will be used.

```
dgsSetProperty(line3D,"lineWidth",lineWidth)
```

- **lineWidth:** A float of the width.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- [dgs-dx3dimage](mta://reference/misc/dgs-dx3dimage.md)

- [dgs-dx3dtext](mta://reference/misc/dgs-dx3dtext.md)

- dgs-dx3dline

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
