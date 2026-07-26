---
doc_id: "mta-wiki:6087"
title: "DxSetBlendMode"
source_title: "DxSetBlendMode"
source_url: "https://wiki.multitheftauto.com/wiki/DxSetBlendMode"
revision_id: 81100
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:51.184898+00:00"
---

# DxSetBlendMode

This function sets the current blend mode for the dxDraw functions. Changing the blend mode can increase the quality when drawing text or certain other images to a render target. As a general guide use **modulate_add** when drawing text to a render target, and **add** when drawing the render target to the screen. Don't forget to restore the default **blend** at the end - See the example below.

## Syntax

```
bool dxSetBlendMode ( string blendMode )
```

### Required Arguments

- **blendMode :** The blend mode to use which can be one of:

- **blend:** The source textures are alpha blended to the screen/render target. This is the default mode for drawing and gives the results we all know and love.

- **add:** The source textures are added to the screen/render target.

- **modulate_add:** The source textures are multiplied by the alpha and then added to the screen/render target.

- **overwrite :** The source textures are overwritten. This can be useful for clearing render targets.

## Returns

Returns true if successful, or *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Client

This example shows how to use **modulate_add** and **add** to avoid quality problems when using a render target:

```
local myRenderTarget = dxCreateRenderTarget(500, 500, true)

--
-- Function to draw text to our render target texture when the 'r' key is pressed
--
function updateRenderTarget()
    dxSetRenderTarget(myRenderTarget, true)
    dxSetBlendMode("modulate_add")  -- Set 'modulate_add' when drawing stuff on the render target

    dxDrawText("Testing "..getTickCount(), 0, 0, 0, 0, tocolor(255, 255, 255, 255), 2, "clear")

    dxSetBlendMode("blend")         -- Restore default blending
    dxSetRenderTarget()             -- Restore default render target
end
bindKey("r", "down", updateRenderTarget )

--
-- Display render target contents
--
addEventHandler("onClientRender", root,
    function()
        dxSetBlendMode("add")       -- Set 'add' when drawing the render target on the screen
        dxDrawImage(100, 200, 500, 500, myRenderTarget, -10)
        dxSetBlendMode("blend")     -- Restore default blending
    end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04425 | Added overwrite |
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

- dxSetBlendMode

- [dxSetPixelColor](mta://scripting/client/functions/dxsetpixelcolor.md)

- [dxSetRenderTarget](mta://scripting/client/functions/dxsetrendertarget.md)

- [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md)

- [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

- [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md)

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
