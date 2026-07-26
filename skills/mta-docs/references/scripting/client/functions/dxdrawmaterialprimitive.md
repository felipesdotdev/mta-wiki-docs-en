---
doc_id: "mta-wiki:10764"
title: "DxDrawMaterialPrimitive"
source_title: "DxDrawMaterialPrimitive"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawMaterialPrimitive"
revision_id: 80081
language: "en"
categories: ["Client_functions", "Changes_in_1.5.6", "Changes_in_1.6.0"]
---

# DxDrawMaterialPrimitive

This function draws a 2D primitive shape with material applied to it across the screen - rendered for one frame. This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.
If image file is used, it should ideally have dimensions that are a power of two, to prevent possible blurring.
Power of two: 2px, 4px, 8px, 16px, 32px, 64px, 128px, 256px, 512px, 1024px...

## Syntax

```
bool dxDrawMaterialPrimitive ( primitiveType pType, mixed material, bool postGUI, table vertex1 [, table vertex2, ...] )
```

### Required Arguments

- **pType:** Type of primitive to be drawn.

- **image:** Either a [material](https://wiki.multitheftauto.com/index.php?search=material) element or a [filepath](mta://reference/misc/filepath.md) of the image which is going to be drawn. (.dds images are also supported). Image files should ideally have dimensions that are a power of two, to prevent possible blurring. Use a texture created with [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md) to **speed up drawing**.

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **vertices:** Tables representing each primitive vertex, required amount of them is determined by primitive type.

## Allowed types

 

Available primitive types.

More info on primitives may be found on [this MSDN site](https://msdn.microsoft.com/en-us/library/windows/desktop/bb147291(v=vs.85).aspx)

- **pointlist:** Renders the vertices as a collection of isolated points.

- **linelist:** Renders the vertices as a list of isolated straight line segments.

- **linestrip:** Renders the vertices as a single polyline.

- **trianglelist:** Renders the specified vertices as a sequence of isolated triangles. Each group of three vertices defines a separate triangle.

- **trianglestrip:** Renders the vertices as a triangle strip.

- **trianglefan:** Renders the vertices as a triangle fan.

## Vertices format

- **posX:** An float representing the absolute X position of the vertex, represented by pixels on the screen.

- **posY:** An float representing the absolute Y position of the vertex, represented by pixels on the screen.

- **color (optional):** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue). If it's not specified, white color is used.

- **u:** An float representing  the relative X coordinate of the top left corner of the material which should be drawn from image

- **v:** An float representing  the relative Y coordinate of the top left corner of the material which should be drawn from image

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

```
-- Load the texture
local texture = dxCreateTexture("myTexture.png")

-- Function to render a textured triangle
function renderPrimitive()
    if texture then
        -- Draw the primitive using the "trianglelist" type
        -- 3 vertices, each with 4 numbers: {x, y, u, v}
        dxDrawMaterialPrimitive("trianglelist", texture, false, {100, 100, 0, 0}, {300, 100, 1, 0}, {200, 300, 0.5, 1})
    end
end

-- Add an event handler to render the primitive every frame
addEventHandler("onClientRender", root, renderPrimitive)
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md)

- [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md)

- [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md)

- [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)

- [dxDrawImageSection](mta://scripting/client/functions/dxdrawimagesection.md)

- [dxDrawLine](mta://scripting/client/functions/dxdrawline.md)

- [dxDrawLine3D](mta://scripting/client/functions/dxdrawline3d.md)

- [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

- dxDrawMaterialPrimitive

- [dxDrawMaterialPrimitive3D](mta://scripting/client/functions/dxdrawmaterialprimitive3d.md)

- [dxDrawMaterialSectionLine3D](mta://scripting/client/functions/dxdrawmaterialsectionline3d.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22271](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22271):

- [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md)

- [dxDrawPrimitive](mta://scripting/client/functions/dxdrawprimitive.md)

- [dxDrawPrimitive3D](mta://scripting/client/functions/dxdrawprimitive3d.md)

- [dxDrawRectangle](mta://scripting/client/functions/dxdrawrectangle.md)

- [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)

- [dxDrawWiredSphere](mta://scripting/client/functions/dxdrawwiredsphere.md)

- [dxGetBlendMode](mta://scripting/client/functions/dxgetblendmode.md)

- [dxGetFontHeight](mta://scripting/client/functions/dxgetfontheight.md)

- [dxGetMaterialSize](mta://scripting/client/functions/dxgetmaterialsize.md)

- [dxGetPixelColor](mta://scripting/client/functions/dxgetpixelcolor.md)

- [dxGetPixelsSize](mta://scripting/client/functions/dxgetpixelssize.md)

- [dxGetPixelsFormat](mta://scripting/client/functions/dxgetpixelsformat.md)

- [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md)

- [dxGetTextSize](mta://scripting/client/functions/dxgettextsize.md)

- [dxGetTextWidth](mta://scripting/client/functions/dxgettextwidth.md)

- [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md)

- [dxIsAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxisaspectratioadjustmentenabled.md)

- [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

- [dxSetBlendMode](mta://scripting/client/functions/dxsetblendmode.md)

- [dxSetPixelColor](mta://scripting/client/functions/dxsetpixelcolor.md)

- [dxSetRenderTarget](mta://scripting/client/functions/dxsetrendertarget.md)

- [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md)

- [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

- [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md)

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
