---
doc_id: "mta-wiki:6160"
title: "DxDrawMaterialSectionLine3D"
source_title: "DxDrawMaterialSectionLine3D"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawMaterialSectionLine3D"
revision_id: 81106
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:46.254658+00:00"
---

# DxDrawMaterialSectionLine3D

This function draws a textured 3D line between two points in the 3D world - rendered for one frame.  This should be used in conjunction with [onClientPreRender](mta://scripting/client/events/onclientprerender.md) in order to display continuously.

The 3D line with a large width value effectively becomes a rectangle, so it it possible to construct basic shapes such as boxes with several large width lines and the appropriate values for 'faceToward'.

|  | This page describes the current implementation. For older versions check legacy version |
| --- | --- |
|  |  |

## Syntax

```
bool dxDrawMaterialSectionLine3D ( float startX, float startY, float startZ, float endX, float endY, float endZ,
                                   float u, float v, float usize, float vsize, [ bool flipUV = false, ] element material, float width,
                                 [ int color = white, [ bool stage = "postfx", ] float faceTowardX, float faceTowardY, float faceTowardZ ] )
```

### Required Arguments

- **startX/Y/Z:** The start position of the 3D line, representing a coordinate in the GTA world.

- **endX/Y/Z:** The end position of the 3D line, representing a coordinate in the GTA world.

- **u:** the absolute X coordinate of the top left corner of the section

- **v:** the absolute Y coordinate of the top left corner of the section

- **usize:** the absolute width of the section

- **vsize:** the absolute height of the section

- **material:** A [material](mta://reference/misc/material.md) to draw the line with.

- **width:** The width/thickness of the line in GTA world units. (This is 1/75th of the width used in dxDrawLine3D)

## Optional Arguments

- **flipUV**: A bool representing whether a UV orientation should be flipped.

- **color:** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB.

- **stage:** A string representing a stage at which the actual drawcall should happen:

- prefx - Lines are rendered before the color correction. This stage makes lines look natural to SA but colors could be distorted.

- postfx - Lines are rendered after the color correction. This stage conveys a color from the function to a screen without distortions.

- postgui - Lines are rendered after GUI. The line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **faceTowardX/Y/Z:** The direction the front of the line should face towards. If this is not set, the front of the line always faces toward the camera.

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

This example draws corona like effects near the player

```
coronaTexture = dxCreateTexture("corona.png")
red = tocolor(255,0,0)
green = tocolor(0,255,0)
blue = tocolor(0,0,255)

addEventHandler("onClientPreRender",root,
    function()
        local x,y,z = getElementPosition(localPlayer)

        dxSetBlendMode("add")   -- Add blend mode looks best for corona effects
        drawCorona( x+2, y+2, z+1, 1, red )
        drawCorona( x+1, y+3, z+2, 1, green )
        drawCorona( x-1, y+2, z+3, 1, blue )
        dxSetBlendMode("blend") -- Restore default
    end
)

-- Draw the corona texture
function drawCorona( x, y, z, size, color )
    dxDrawMaterialSectionLine3D ( x, y, z+size,
                                  x, y, z-size,
                                  0,0,1,1, coronaTexture, size, color)
end
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

- [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

- [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md)

- [dxDrawMaterialPrimitive3D](mta://scripting/client/functions/dxdrawmaterialprimitive3d.md)

- dxDrawMaterialSectionLine3D

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
