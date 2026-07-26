---
doc_id: "mta-wiki:3848"
title: "DxDrawRectangle"
source_title: "DxDrawRectangle"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawRectangle"
revision_id: 60126
language: "en"
categories: ["Client_functions", "Changes_in_1.4.0", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:46.820591+00:00"
---

# DxDrawRectangle

This function draws a 2D rectangle across the screen - rendered for **one** frame. This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.

## Syntax

```
bool dxDrawRectangle ( float startX, float startY, float width, float height [, int color = white, bool postGUI = false, bool subPixelPositioning = false ] )
```

### Required Arguments

- **startX:** An float representing the **absolute** origin X position of the rectangle, represented by pixels on the screen.

- **startY:** An float representing the **absolute** origin Y position of the rectangle, represented by pixels on the screen.

- **width:** An float representing the width of the rectangle, drawn in a *right* direction from the origin.

- **height:** An float representing the height of the rectangle, drawn in a *downwards* direction from the origin.

### Optional Arguments

- **color:** the hex color of the rectangle, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI.

ADDED/UPDATED IN VERSION 1.4.0 [r6931](http://code.google.com/p/mtasa-blue/source/detail?r=6931):

- **subPixelPositioning:** A bool representing whether the rectangle can be positioned sub-pixel-ly.

### Returns

Returns true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

Example of MOTD (message of the day), made using DxDrawText, -Line and -Rectangle.

```
local x,y = guiGetScreenSize()  -- Get players resolution.
local playerName = getPlayerName ( localPlayer )  -- Get players name.
local MOTDText = "Welcome to our server, this is a test MOTD script for MTA's Wiki."  -- Example of MOTD message.

function drawStuff()
	dxDrawRectangle ( x/3.8, y/3.8, x/2.02, y/2, tocolor ( 0, 0, 0, 150 ) ) -- Create our black transparent MOTD background Rectangle.
	dxDrawText ( "Welcome " .. playerName, x/3.5, y/3.6, x, y, tocolor ( 255, 255, 255, 255 ), 1, "bankgothic" ) -- Create Welcome title.
        dxDrawText ( "Welcome " .. playerName, x/3.48, y/3.58, x, y, tocolor ( 0, 0, 0, 255 ), 1, "bankgothic" ) -- Create Welcome title shadow.
	dxDrawLine ( x/3.6, y/3.3, x/1.35, y/3.3, tocolor ( 255, 255, 255, 255 ), 2 ) -- Create underline for title.
	dxDrawLine ( x/3.59, y/3.275, x/1.348, y/3.275, tocolor ( 0, 0, 0, 255 ), 2 ) -- Create underline shadow.
	dxDrawText ( MOTDText, x/3.6, y/3, x, y, tocolor ( 255, 255, 255, 255 ), 1, "clear" ) -- Create MOTD text.
end

addEventHandler("onClientRender", root, drawStuff)  -- Keep everything visible with onClientRender.
```

## Changelog

| Version | Description |
| --- | --- |

| 1.4.0-9.06931 | Added subPixelPositioning argument |
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

- [dxDrawMaterialSectionLine3D](mta://scripting/client/functions/dxdrawmaterialsectionline3d.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22271](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22271):

- [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md)

- [dxDrawPrimitive](mta://scripting/client/functions/dxdrawprimitive.md)

- [dxDrawPrimitive3D](mta://scripting/client/functions/dxdrawprimitive3d.md)

- dxDrawRectangle

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
