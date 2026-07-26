---
doc_id: "mta-wiki:3844"
title: "DxDrawLine"
source_title: "DxDrawLine"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawLine"
revision_id: 81883
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
---

# DxDrawLine

This function draws a 2D line across the screen - rendered for **one** frame.  This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.

## Syntax

```
bool dxDrawLine ( int startX, int startY, int endX, int endY, int color [, float width = 1.0, bool postGUI = false ] )
```

### Required Arguments

- **startX:** An integer representing the **absolute** start X position of the line, represented by pixels on the screen.

- **startY:** An integer representing the **absolute** start Y position of the line, represented by pixels on the screen.

- **endX:** An integer representing the **absolute** end X position of the line, represented by pixels on the screen.

- **endY:** An integer representing the **absolute** end Y position of the line, represented by pixels on the screen.

- **color:** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **width:** The width/thickness of the line

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

This example draws an 'X' across the screen.

```
local screenWidth, screenHeight = guiGetScreenSize() 
local lineColor = tocolor(255, 0, 0)
function drawLinesAcrossScreen()
	dxDrawLine(0, 0, screenWidth, screenHeight, lineColor)
	dxDrawLine(screenWidth, 0, 0, screenHeight, lineColor)
end
addEventHandler("onClientRender", root, drawLinesAcrossScreen)
```

This example draws a couple of circles

```
function drawCircle(x,y, radius, color)
    local numPoints = math.floor(math.pow(radius, 0.4) * 5)     -- Calculate number of points to make it look good
    local step = math.pi * 2 / numPoints
    local sx,sy
    for p=0,numPoints do
        local ex = math.cos(p * step) * radius
        local ey = math.sin(p * step) * radius
        if sx then
            dxDrawLine(x+sx, y+sy, x+ex, y+ey, color)
        end
        sx,sy = ex,ey
    end
end

addEventHandler("onClientRender", root, function()
    drawCircle(350, 350, 10, tocolor(255,0,255))
    drawCircle(350, 350, 50, tocolor(255,0,255))
end)
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

- dxDrawLine

- [dxDrawLine3D](mta://scripting/client/functions/dxdrawline3d.md)

- [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

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
