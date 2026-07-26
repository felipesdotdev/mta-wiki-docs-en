---
doc_id: "mta-wiki:6159"
title: "DxDrawMaterialLine3D"
source_title: "DxDrawMaterialLine3D"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawMaterialLine3D"
revision_id: 81105
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
---

# DxDrawMaterialLine3D

This function draws a textured 3D line between two points in the 3D world - rendered for one frame.  This should be used in conjunction with [onClientPreRender](mta://scripting/client/events/onclientprerender.md) in order to display continuously.

The 3D line with a large width value effectively becomes a rectangle, so it it possible to construct basic shapes such as boxes with several large width lines and the appropriate values for 'faceToward'.

3D lines are drawn at a particular place in the [game processing order](mta://reference/misc/game-processing-order.md), so use [onClientPreRender](mta://scripting/client/events/onclientprerender.md) for drawing if you are attaching them to world elements.

|  | This page describes the current implementation. For older versions check legacy version |
| --- | --- |
|  |  |

## Syntax

```
bool dxDrawMaterialLine3D ( float startX, float startY, float startZ, float endX, float endY, float endZ, [ bool flipUV = false, ] element material, float width,
                          [ int color = white, [ string stage = "postfx", ] float faceTowardX, float faceTowardY, float faceTowardZ ] )
```

### Required Arguments

- **startX/Y/Z:** The start position of the 3D line, representing a coordinate in the GTA world.

- **endX/Y/Z:** The end position of the 3D line, representing a coordinate in the GTA world.

- **material:** A [material](https://wiki.multitheftauto.com/index.php?search=material) to draw the line with.

- **width:** The width/thickness of the line in GTA world units. (This is 1/75th of the width used in dxDrawLine3D)

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **flipUV**: A bool representing whether a UV orientation should be flipped.

- **color:** An [integer](mta://reference/misc/int.md) of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB.

- **stage:** A string representing a stage at which the actual drawcall should happen:

- prefx - Lines are rendered before the color correction. This stage makes lines look natural to SA but colors could be distorted.

- postfx - Lines are rendered after the color correction. This stage conveys a color from the function to a screen without distortions.

- postgui - Lines are rendered after GUI. The line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **faceTowardX/Y/Z:** The position the front of the line should face towards. If this is not set, the camera position is used, so the front of the line faces toward the camera.

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

Draws [an image](https://wiki.multitheftauto.com/wiki/File:DxDrawMaterialLine3D-example.png) in coordiantes -2422.68555, -608.78986, 132.56250:

```
local redcircle = dxCreateTexture("red.png")

x,y,z = -2422.68555, -608.78986, 132.56250

size = 1

addEventHandler("onClientRender", root, function()
    dxDrawMaterialLine3D(x+size, y+size, z-0.95, x-size, y-size, z-0.95, redcircle, size*2,tocolor(255, 255, 255, 255), false, x, y, z)
end)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-9.11998 | Added postGUI argument |
| --- | --- |

| 1.5.8-9.20862 | Added flipUV argument |
| --- | --- |

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

- dxDrawMaterialLine3D

- [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md)

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
