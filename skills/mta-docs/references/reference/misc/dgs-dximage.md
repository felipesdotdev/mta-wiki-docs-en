---
doc_id: "mta-wiki:10032"
title: "Dgs-dximage"
source_title: "Dgs-dximage"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dximage"
revision_id: 71432
language: "en"
categories: []
---

# Dgs-dximage

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dximage that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### image

This is equivalent to [dgsImageSetImage](mta://scripting/client/functions/dgsimagesetimage.md)/[dgsImageGetImage](mta://scripting/client/functions/dgsimagegetimage.md).

```
dgsSetProperty(image,"image",texture)
```

- **texture** : A material element (texture/shader/screen source/render target) of the image.

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the image.

```
dgsSetProperty(image,"color",color)
```

- **color** : An integer of the color of the image.

### rotationCenter

The rotation center of the image. *Learn More [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)*.

```
dgsSetProperty(image,"rotationCenter",{xOffset,yOffset,relative})
```

- **xOffset** : The X offset from the image center for which to rotate the image from, which determined by **relative**.

- **yOffset** : The Y offset from the image center for which to rotate the image from, which determined by **relative**.

- **relative** : A bool indicates whether the offsets are relative to the size of dgs-dximgage.

### rotation

The rotation of the image. *Learn More [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)*.

```
dgsSetProperty(image,"rotation",rotation)
```

- **rotation** : The rotation, in degrees for the image.

### shadow

The shadow image of the button.

```
dgsSetProperty(image,"shadow",{offsetX,offsetY,color})
```

- **offsetX** : A float of the 2D X offset of the shadow image of the button.

- **offsetY** : A float of the 2D Y offset of the shadow image of the button.

- **color** : An integer of the color of the shadow image of the button.

### UVSize

The uv size of image section [dgsImageSetUVSize](mta://scripting/client/functions/dgsimagesetuvsize.md)/[dgsImageGetUVSize](mta://scripting/client/functions/dgsimagegetuvsize.md). *Learn More [dxDrawImageSection](mta://scripting/client/functions/dxdrawimagesection.md)*.

```
dgsSetProperty(image,"UVSize",{USize,VSize,relative})
```

- **USize** : The width of the U size of image.

- **VSize** : The height of the V size of image.

- **relative** :This determines whether UV size is relative. If this is true, then UV size floats must be between 0 and 1, representing UV sizes relative to the pixels of the texture loaded.

### UVPos

The uv position image section [dgsImageSetUVPosition](mta://scripting/client/functions/dgsimagesetuvposition.md)/[dgsImageGetUVPosition](mta://scripting/client/functions/dgsimagegetuvposition.md). *Learn More [dxDrawImageSection](mta://scripting/client/functions/dxdrawimagesection.md)*.

```
dgsSetProperty(image,"UVPos",{UPos,VPos,relative})
```

- **UPos** : the X coordinate of the top left corner of the section which should be drawn from image.

- **VPos** : the Y coordinate of the top left corner of the section which should be drawn from image.

- **relative** :This determines whether UV position is relative. If this is true, then UV position floats must be between 0 and 1, representing UV positions relative to the pixels of the texture loaded.

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

- dgs-dximage

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
