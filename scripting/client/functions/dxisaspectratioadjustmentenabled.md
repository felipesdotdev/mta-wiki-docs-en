---
doc_id: "mta-wiki:11880"
title: "DxIsAspectRatioAdjustmentEnabled"
source_title: "DxIsAspectRatioAdjustmentEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/DxIsAspectRatioAdjustmentEnabled"
revision_id: 81225
language: "en"
categories: ["Client_functions", "Changes_in_1.3.3", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:50.240286+00:00"
---

# DxIsAspectRatioAdjustmentEnabled

This function gets the current aspect ratio set by [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md).

## Syntax

```
bool, float dxIsAspectRatioAdjustmentEnabled ( )
```

### Returns

- **boolean:** returns **true** when enabled by [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md), **false** otherwise.

- **float:** aspect ratio set by [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

## Example

This example will draw the aspect ratio to screen if aspect ratio was enabled previously.

```
addEventHandler("onClientRender", root, function()
    dxSetAspectRatioAdjustmentEnabled(true)

    local enabled, ratio = dxIsAspectRatioAdjustmentEnabled()
	
    if(enabled) then
        dxDrawText("Aspect ratio is: " .. ratio, 250, 250)
    end
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

- dxIsAspectRatioAdjustmentEnabled

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
