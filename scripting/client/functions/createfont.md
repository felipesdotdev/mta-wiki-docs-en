---
doc_id: "mta-wiki:5687"
title: "DxCreateFont"
source_title: "CreateFont"
source_url: "https://wiki.multitheftauto.com/wiki/CreateFont"
revision_id: 78780
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:11:28.346787+00:00"
---

# DxCreateFont

| [[{{{image}}}\|link=\|]] | Note: The size can't be less than 5 or more than 150. Use this function after onClientResourceStart, otherwise some characters may be displayed incorrectly. |
| --- | --- |
|  |  |

This function creates a [DX font](mta://reference/misc/dx-font.md) element that can be used in [dxDrawText](mta://scripting/client/functions/dxdrawtext.md). Successful font creation is not guaranteed, and may fail due to hardware or memory limitations.

To see if creation is likely to fail, use [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md). (When **VideoMemoryFreeForMTA** is zero, failure *is* guaranteed.)

##### It is highly recommended that [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md) is used when writing and testing scripts using dxCreateFont.

## Syntax

```
element dxCreateFont ( string filepath[, int size=9, bool bold=false, string quality="proof" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxFont](mta://reference/misc/dx-font.md)(...)*

### Required Arguments

- **filepath:** the name of the file containing the font

### Optional Arguments

- **size:** size of the font

- **bold:** flag to indicate if the font should be bold

- **quality:** the font quality

- "default": not the actual default

- "draft"

- "proof": the default

- "nonantialiased"

- "antialiased"

- "cleartype"

- "cleartype_natural"

### Returns

Returns a [DX font](mta://reference/misc/dx-font.md) element if successful, *false* if invalid arguments were passed to the function, or there is insufficient resources available.

**You should always check to see if this function has returned false.**

## Example

```
local font = dxCreateFont('myfont.ttf', 20, false, 'proof') or 'default' -- fallback to default

addEventHandler('onClientRender', root, function()
    dxDrawText('Example Text', 100, 350, 300, 350, tocolor(255, 255, 0), 1, font)
end)
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- dxCreateFont

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

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
