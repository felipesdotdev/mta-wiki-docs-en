---
doc_id: "mta-wiki:4308"
title: "DxDrawImage"
source_title: "DxDrawImage"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawImage"
revision_id: 79916
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxDrawImage

An image drawn on the screen with the dxDrawImage function.

Draws an image on the screen for a single frame. In order for the image to stay visible continuously, you need to call this function with the same parameters on each frame update (see [onClientRender](mta://scripting/client/events/onclientrender.md)).  

Image files should ideally have dimensions that are a power of two, to prevent possible blurring.  

**Power of two: 2px, 4px, 8px, 16px, 32px, 64px, 128px, 256px, 512px, 1024px...**

| [[{{{image}}}\|link=\|]] | Important Note: Do not draw image from path. Use a texture created with dxCreateTexture instead to efficiently draw image . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: For further optimising your DX code, see dxCreateRenderTarget . You should use render target whenever possible, in order to dramatically reduce CPU usage caused by many dxDraw* calls. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: To help prevent edge artifacts when drawing textures, set textureEdge to "clamp" when calling dxCreateTexture . |
| --- | --- |
|  |  |

## Syntax

```
bool dxDrawImage ( float posX, float posY, float width, float height, mixed image,
                 [ float rotation = 0, float rotationCenterOffsetX = 0, float rotationCenterOffsetY = 0,
                   int color = tocolor(255,255,255,255), bool postGUI = false ] )
```

### Required Arguments

- **posX:** the absolute X coordinate of the top left corner of the image

- **posY:** the absolute Y coordinate of the top left corner of the image

- **width:** the absolute width of the image

- **height:** the absolute height of the image

- **image:** Either a [material](https://wiki.multitheftauto.com/index.php?search=material) element or a [filepath](mta://reference/misc/filepath.md) of the image which is going to be drawn. (.dds images are also supported). Image files should ideally have dimensions that are a power of two, to prevent possible blurring. Use a texture created with [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md) to **speed up drawing**.

### Optional Arguments

- **rotation:** the rotation, in degrees for the image.

- **rotationCenterOffsetX:** the absolute X offset from the image center for which to rotate the image from.

- **rotationCenterOffsetY:** the absolute Y offset from the image center for which to rotate the image from.

- **color:** Tints the image with a value produced by [tocolor](mta://scripting/shared/functions/tocolor.md) or hexadecimal number in format: 0xAARRGGBB (RR = red, GG = green, BB = blue, AA = alpha).

- **postGUI:** A bool representing whether the image should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Example of a pendulum swinging from the top of the screen, made using dxDrawImage.

```
local screenWidth, screenHeight = guiGetScreenSize()  -- Get screen resolution.
local arrowTexture = dxCreateTexture('arrow.png')

function renderDisplay ( )
	local seconds = getTickCount() / 1000
	local angle = math.sin(seconds) * 80
	-- This will draw the graphic file 'arrow.png' at the top middle of the screen
	-- using the size of 100 pixels wide, and 240 pixels high.
	-- The center of rotation is at the top of the image.
	dxDrawImage ( screenWidth/2 - 50, 0, 100, 240, arrowTexture, angle, 0, -120 )
end
addEventHandler("onClientRender", root, renderDisplay)  -- Keep everything visible with onClientRender.
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md)

- [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md)

- [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md)

- dxDrawImage

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
