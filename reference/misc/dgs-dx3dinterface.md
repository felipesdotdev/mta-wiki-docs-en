---
doc_id: "mta-wiki:10197"
title: "Dgs-dx3dinterface"
source_title: "Dgs-dx3dinterface"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dx3dinterface"
revision_id: 64590
language: "en"
categories: []
generated_at: "2026-07-26T16:11:21.602865+00:00"
---

# Dgs-dx3dinterface

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dx3dinterface that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### fadeDistance

The distance of which 3D Interface starts to fading.

```
dgsSetProperty(interface,"fadeDistance",fadeDistance)
```

- **fadeDistance:** A float of the fade distance.

### faceRelativeTo

This property is used to adjust the relativity of property "faceTo".

```
dgsSetProperty(interface,"faceRelativeTo",faceRelativeTo)
```

- **faceRelativeTo:** A string of the relative options:

- **self:** Default state, relative to 3D Interface itself, faceTo = selfPosition+faceTo

- **world:** Default state, relative to the world, faceTo = absoluteWorldPosition

### faceTo

A table stores x,y,z coordinate that dx 3d interface faces towards in the world.

```
dgsSetProperty(interface,"faceTo",{faceTowardsX,faceTowardsY,faceTowardsZ})
```

- **faceTowardsX:** The x coordinate of the destination dx 3d interface faces towards.

- **faceTowardsY:** The y coordinate of the destination dx 3d interface faces towards.

- **faceTowardsZ:** The z coordinate of the destination dx 3d interface faces towards.

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the dx 3d interface.

```
dgsSetProperty(interface,"color",color)
```

- **color:**  An integer of the color of the dx 3d interface.

### maxDistance

The maximum visible distance in the world.

```
dgsSetProperty(interface,"maxDistance",maxDistance)
```

- **maxDistance:** A float of the distance.

### renderTarget_parent

This property stores a render target of the dx 3d interface.

```
dgsSetProperty(interface,"renderTarget_parent",renderTarget)
```

- **renderTarget:** A render target that is used to render the child dgs elements of the dx 3d interface.

### resolution

The resolution (pixels) of the render target.

```
dgsSetProperty(interface,"resolution",{width,height})
```

- **width:** The width of the render target in pixels.

- **height:** The height of the render target in pixels.

### size

The size is relative to the world.

```
dgsSetProperty(interface,"size",{width,height})
```

- **width:** A float of the width of the dx 3d interface relative to the world.

- **height:** A float of the height of the dx 3d interface relative to the world.

### position

A table stores x,y,z coordinate of the dx 3d interface in the world.

```
dgsSetProperty(interface,"position",{x,y,z})
```

- **x:** The x coordinate of the destination.

- **y:** The y coordinate of the destination.

- **z:** The z coordinate of the destination.

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- dgs-dx3dinterface

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
