---
doc_id: "mta-wiki:5683"
title: "DxUpdateScreenSource"
source_title: "DxUpdateScreenSource"
source_url: "https://wiki.multitheftauto.com/wiki/DxUpdateScreenSource"
revision_id: 71071
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:51.602031+00:00"
---

# DxUpdateScreenSource

This function updates the contents of a screen source [texture](mta://reference/misc/texture.md) with the screen output from GTA

## Syntax

```
bool dxUpdateScreenSource ( element screenSource [, bool resampleNow = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxScreenSource](mta://scripting/client/functions/dxscreensource.md):update(...)*

### Required Arguments

- **screenSource:** The screen source element whose pixels we want to fill with the screen capture

### Optional Arguments

- **resampleNow:** A bool to indicate if the screen should be captured immediately. The default is *false* which means the screen from the end of the previous frame is used (better for performance and consistency). Use *true* for layering fullscreen effects.

### Returns

Returns *true* if the screen was successfully captured, *false* otherwise.

## Example

This example will update the screen capture when F7 is pressed

```
addEventHandler("onClientResourceStart", resourceRoot,
    function()
        myScreenSource = dxCreateScreenSource( 500, 500)    -- Create a screen source texture which is 500 x 500 pixels
    end
)

bindKey( "F7", "down", 
    function()
        if myScreenSource then
            dxUpdateScreenSource( myScreenSource )          -- Capture the screen
        end
    end
)

addEventHandler( "onClientRender", root,
    function()
        if myScreenSource then
            dxDrawImage ( 0, 0, 300, 300, myScreenSource )  -- Draw the result in top left corner
        end
    end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.03795 | Added resample argument |
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

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- dxUpdateScreenSource
