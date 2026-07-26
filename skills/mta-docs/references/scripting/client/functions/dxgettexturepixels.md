---
doc_id: "mta-wiki:6064"
title: "DxGetTexturePixels"
source_title: "DxGetTexturePixels"
source_url: "https://wiki.multitheftauto.com/wiki/DxGetTexturePixels"
revision_id: 81057
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxGetTexturePixels

This function fetches the [pixels](mta://reference/misc/texture-pixels.md) from a [texture](https://wiki.multitheftauto.com/index.php?search=texture) element. It can be used with a standard texture, render target or screen source.

| [[{{{image}}}\|link=\|]] | Important Note: If the user has not enabled screen uploading in the settings, the function will use a 32x32 empty texture as a basis. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function is slow and not something you want to be doing once a frame. It is slower when reading pixels from a render target or screen source. And is very slow indeed if the texture format is not 'argb' (unless the native ' dds' format is used with correct options). |
| --- | --- |
|  |  |

## Syntax

```
string dxGetTexturePixels ( [ int surfaceIndex = 0, ] element texture [, string pixelsFormat = "plain" [, string textureFormat = "unknown"] [, bool mipmaps = true] ] [, int x = 0, int y = 0, int width = 0, int height = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[texture](https://wiki.multitheftauto.com/index.php?search=texture):getPixels(...)*

### Required Arguments

- **texture :** The texture element to get the pixels from

### Optional Arguments

- **surfaceIndex:** Desired slice to get if the texture is a volume texture, or desired face to get if the texture is a cube map. (Cube map faces: 0=+X 1=-X 2=+Y 3=-Y 4=+Z 5=-Z)

ADDED/UPDATED IN VERSION 1.6.0 [r22185](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22185):

- **pixelsFormat:** "plain", "dds"

- **textureFormat:** A string representing the desired texture format for "**dds**" pixels, which can be one of:

- **"unknown"**: Determined automatically based on texture format (default).

- **"argb"**: ARGB uncompressed 32 bit color.

- **"dxt1"**: DXT1 compressed - Can take a fraction of a second longer to create (unless the texture is already in DXT1). Uses 8 times less video memory than ARGB and *can speed up drawing*. Quality not as good as ARGB. *It supports alpha blending, but it can only be on or off, that is: either 0 or 255.*

- **"dxt3"**: DXT3 compressed - Can take a fraction of a second longer to create (unless the texture is already in DXT3). Uses 4 times less video memory than ARGB and *can speed up drawing*. Quality slightly better than DXT1 and supports crisp alpha blending.

- **"dxt5"**: DXT5 compressed - Can take a fraction of a second longer to create (unless the texture is already in DXT5). Uses 4 times less video memory than ARGB and *can speed up drawing*. Quality slightly better than DXT1 and supports smooth alpha blending.

- **mipmaps:** True to create a mip-map chain for "**dds**" pixels so the texture looks good when drawn at various sizes.

By default the pixels from the whole texture is returned. To get only a portion of the texture, define a rectangular area using all four of these optional arguments:

- **x:** Rectangle left position

- **y:** Rectangle top position

- **width:** Rectangle width

- **height :** Rectangle height

## Returns

Returns pixels string if successful, *false* if invalid arguments were passed to the function.

## Example

```
local mtaLogo = dxCreateTexture("mta-logo.png")
outputChatBox("MTA logo pixels is: "..dxGetTexturePixels(mtaLogo))
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04021 | Added surfaceIndex argument |
| --- | --- |

| 1.6.0-9.22185 | Added dds pixels format |
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

- dxGetTexturePixels

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
