---
doc_id: "mta-wiki:5145"
title: "DxDrawImageSection"
source_title: "DxDrawImageSection"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawImageSection"
revision_id: 78834
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxDrawImageSection

Differing from [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md), this function only draws a part of an image on the screen for a single frame. In order for the image to stay visible continuously, you need to call this function with the same parameters on each frame update (see [onClientRender](mta://scripting/client/events/onclientrender.md)).

Image files should ideally have dimensions that are a power of two, to prevent possible blurring.  

**Power of two: 2px, 4px, 8px, 16px, 32px, 64px, 128px, 256px, 512px, 1024px...**

| [[{{{image}}}\|link=\|]] | Tip: Use a texture created with dxCreateTexture to speed up drawing . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: To help prevent edge artifacts when drawing textures, set textureEdge to "clamp" when calling dxCreateTexture |
| --- | --- |
|  |  |

## Syntax

```
bool dxDrawImageSection ( float posX, float posY, float width, float height,
                          float u, float v, float usize, float vsize, mixed image,
                        [ float rotation = 0, float rotationCenterOffsetX = 0, float rotationCenterOffsetY = 0,
                          int color = white, bool postGUI = false ] )
```

### Required Arguments

 

An example of how dxDrawImageSection function works in practice.

- **posX:** the absolute X coordinate of the top left corner of the image

- **posY:** the absolute Y coordinate of the top left corner of the image

- **width:** the absolute width of the image

- **height:** the absolute height of the image

- **u:** the absolute X coordinate of the top left corner of the section which should be drawn from image

- **v:** the absolute Y coordinate of the top left corner of the section which should be drawn from image

- **usize:** the absolute width of the image section

- **vsize:** the absolute height of the image section

- **image:** Either a [material](https://wiki.multitheftauto.com/index.php?search=material) element or a [filepath](mta://reference/misc/filepath.md) of the image which is going to be drawn. (.dds images are also supported). Image files should ideally have dimensions that are a power of two, to prevent possible blurring. Use a texture created with [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md) to **speed up drawing**.

### Optional Arguments

- **rotation:** the rotation, in degrees for the image.

- **rotationCenterOffsetX:** the absolute X offset from the image center for which to rotate the image from.

- **rotationCenterOffsetY:** the absolute Y offset from the image center for which to rotate the image from.

- **color:** the color of the image, a value produced by [tocolor](mta://scripting/shared/functions/tocolor.md) or hexadecimal number in format: 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **postgui :** A bool representing whether the image should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Client

**Example 1**
The example draws a section of an image. (You can use [this](https://i.imgur.com/rMaiEpp.png) image to test.)

```
addEventHandler("onClientRender", root, function()
    local sectionStartX, sectionStartY = 202, 65
    local sectionWidth, sectionHeight  = 150, 150

    dxDrawImageSection(500, 500, 256, 256, sectionStartX, sectionStartY, sectionWidth, sectionHeight, "example.jpg")
end)
```

**Example 2**
The example draws a section of an image. (You can use [this](http://i1325.photobucket.com/albums/u630/Tourmalinelisa2/128x128.jpg) image to test.)

```
addEventHandler('onClientRender', root, function()
  dxDrawImageSection(400, 200, 64, 64, 0, 0, 64, 64, 'img.jpg') -- Draw a certain section
  dxDrawImage(400, 300, 128, 128, 'img.jpg') -- Draw the whole image to be able to identify the difference
end)
```

**Example 3**
This Example draws you a section that cut image from start point 0 to 100

```
local myimg = dxCreateTexture("myimage.png") -- Make This Image as texture 
addEventHandler('onClientRender', root, function()
dxDrawImageSection(400,200,100,100,0,0,100,100,myimg) -- draw image section that clip part of image from start of image to 100 as width and height 
-- By Ahmeed - Farees
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

- dxDrawImageSection

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
