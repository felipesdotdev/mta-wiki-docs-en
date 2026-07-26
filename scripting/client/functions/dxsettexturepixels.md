---
doc_id: "mta-wiki:6065"
title: "DxSetTexturePixels"
source_title: "DxSetTexturePixels"
source_url: "https://wiki.multitheftauto.com/wiki/DxSetTexturePixels"
revision_id: 81058
language: "en"
categories: ["Client_functions", "Needs_Example", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:51.492012+00:00"
---

# DxSetTexturePixels

|  | Script Example Missing Function DxSetTexturePixels needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function sets the [pixels](mta://reference/misc/texture-pixels.md) of a [texture](mta://reference/misc/texture.md) element. It can be used with a standard texture, render target or screen source. Only '**plain'** format pixels please.

| [[{{{image}}}\|link=\|]] | Note: This function is slow and not something you want to be doing once a frame. It is very slow when setting pixels to a render target or screen source. And is very slow indeed if the texture format is not "argb" . |
| --- | --- |
|  |  |

## Syntax

```
bool dxSetTexturePixels ( [ int surfaceIndex = 0, ] element texture, string pixels [, int x = 0, int y = 0, int width = 0, int height = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[texture](mta://reference/misc/texture.md):setPixels(...)*

### Required Arguments

- **texture :** The texture element to set the pixels of

- **pixels :** The '**plain'** format pixels to use

### Optional Arguments

- **surfaceIndex:** Desired slice to set if the texture is a volume texture, or desired face to set if the texture is a cube map. (Cube map faces: 0=+X 1=-X 2=+Y 3=-Y 4=+Z 5=-Z)

By default the pixels are set starting at the top left corner of the texture. To set a different region, define a rectangular area using all four of these optional arguments:

- **x:** Rectangle left position

- **y:** Rectangle top position

- **width:** Rectangle width

- **height :** Rectangle height

## Returns

Returns a string if successful, *false* if invalid arguments were passed to the function.

## Example

```
TODO
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04021 | Added surfaceIndex argument |
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

- dxSetTexturePixels

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
