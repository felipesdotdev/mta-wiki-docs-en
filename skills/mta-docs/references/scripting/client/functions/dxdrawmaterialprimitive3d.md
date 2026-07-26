---
doc_id: "mta-wiki:12449"
title: "DxDrawMaterialPrimitive3D"
source_title: "DxDrawMaterialPrimitive3D"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawMaterialPrimitive3D"
revision_id: 81253
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxDrawMaterialPrimitive3D

This function draws a 3D primitive shape with material applied to it in the 3D world - rendered for one frame. This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.
If image file is used, it should ideally have dimensions that are a power of two, to prevent possible blurring.
Power of two: 2px, 4px, 8px, 16px, 32px, 64px, 128px, 256px, 512px, 1024px...

|  | This page describes the current implementation. For older versions check legacy version |
| --- | --- |
|  |  |

## Syntax

```
bool dxDrawMaterialPrimitive3D ( primitiveType pType, mixed material, string stage, table vertex1 [, table vertex2, ...] )
```

### Required Arguments

- **pType:** Type of primitive to be drawn.

- **image:** Either a [material](https://wiki.multitheftauto.com/index.php?search=material) element or a [filepath](mta://reference/misc/filepath.md) of the image which is going to be drawn. (.dds images are also supported). Image files should ideally have dimensions that are a power of two, to prevent possible blurring. Use a texture created with [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md) to **speed up drawing**.

- **stage:** A string representing a stage at which the actual drawcall should happen:

- prefx - Primitives are rendered before the color correction. This stage makes primitives look natural to SA but colors could be distorted.

- postfx - Primitives are rendered after the color correction. This stage conveys a color from the function to a screen without distortions.

- postgui - Primitives are rendered after GUI. The primitives should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **vertices:** Tables representing each primitive vertex, required amount of them is determined by primitive type.

## Allowed types

 

Available primitive types.

More info on primitives may be found on [this MSDN site](https://msdn.microsoft.com/en-us/library/windows/desktop/bb147291.aspx)

- **pointlist:** Renders the vertices as a collection of isolated points.

- **linelist:** Renders the vertices as a list of isolated straight line segments.

- **linestrip:** Renders the vertices as a single polyline.

- **trianglelist:** Renders the specified vertices as a sequence of isolated triangles. Each group of three vertices defines a separate triangle.

- **trianglestrip:** Renders the vertices as a triangle strip.

- **trianglefan:** Renders the vertices as a triangle fan.

## Vertices format

- **posX:** An float representing the X position of the vertex in the GTA world.

- **posY:** An float representing the Y position of the vertex in the GTA world.

- **posZ:** An float representing the Z position of the vertex in the GTA world.

- **color (optional):** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB. If it's not specified, white color is used.

- **u:** An float representing  the relative X coordinate of the top left corner of the material which should be drawn from image

- **v:** An float representing  the relative Y coordinate of the top left corner of the material which should be drawn from image

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Remarks

When a 3D draw call is issued by any such material MTA function then the principle to [push it directly to the 3D adapter](https://github.com/multitheftauto/mtasa-blue/blob/16769b8d1c94e2b9fe6323dcba46d1305f87a190/Client/core/Graphics/CMaterialPrimitive3DBatcher.cpp#L42) does apply. To achieve this there is **no software-side 3D clipping mathematics** being performed. This way the vertex data is always being pushed to the vertex shader, leaving the entire freedom to the developer on how to interpret this vertex data in the shader. For example, even though this function does imply an use in 3D world space, the vertex coordinates could be translated directly into Direct3D 9 screen space instead, effectively discarding any multiplication with the camera projection matrix. The mathematical model for translation into valid Direct3D 9 screen-space coordinates is described [here](https://docs.microsoft.com/en-us/windows/win32/direct3d9/viewports-and-clipping). Let's assume that you are drawing the rectangle on a classic sheet of paper with a mathematical 2D X,Y coordinate system.

To transform the coordinates you first have to flip the Y coordinate using negation and then apply the Direct3D 9 screen-space rasterization cross-hair by using the screen dimensions (sw, sh). Since linear shapes are being preserved across linear translations, you can simplify each vertex-based figure into it's set of vertices for the purpose shown above. By using this function in such a way it can perform all the operations in the same quality such as the simpler [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md) function.

## Example

This example draws the picture with the file name 'test.png' on the ground of Grove Street and adds a /flip command to flip it. The 'test.png' file needs to be included in the [meta.xml](mta://reference/misc/meta-xml.md) in order for this example to work.

```
local picture = "test.png"
local worldRenderPositions = { -- create a table with all the world positions
    
    { 2483, -1663, 12.4, 0, 0 }, -- top left
    { 2493, -1663, 12.4, 1, 0 }, -- top right
    { 2483, -1673, 12.4, 0, 1 }, -- bottom left
    { 2493, -1673, 12.4, 1, 1 }, -- bottom right
    
    }
    
function renderPicture()
    dxDrawMaterialPrimitive3D( "trianglestrip", picture, false, unpack(worldRenderPositions) ) -- use unpack() to separate the points
end
addEventHandler( "onClientRender", root, renderPicture )

function flipPicture()
    for index, point in ipairs(worldRenderPositions) do
        if point[4] == 1 then
            point[4] = 0
        else
            point[4] = 1
        end
        if point[5] == 1 then
            point[5] = 0
        else
            point[5] = 1
        end
    end
end
addCommandHandler( "flip", flipPicture )
```

This function can be used to draw billboards in the game world. You have to [understand the mathematical models about the human vision](https://forum.mtasa.com/topic/133065-naruto-jutsus-help-me/?do=findComment&comment=1003073) to calculate the proper vertices.

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

- [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md)

- dxDrawMaterialPrimitive3D

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
