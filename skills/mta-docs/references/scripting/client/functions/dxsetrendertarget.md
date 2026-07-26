---
doc_id: "mta-wiki:5682"
title: "DxSetRenderTarget"
source_title: "DxSetRenderTarget"
source_url: "https://wiki.multitheftauto.com/wiki/DxSetRenderTarget"
revision_id: 61717
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0-9.04431", "Changes_in_1.6.0"]
---

# DxSetRenderTarget

This function changes the drawing destination for the dx functions. It can be used to select a previously created render target, or if called with no arguments, restore drawing directly to the screen.

## Syntax

```
bool dxSetRenderTarget ( [ element renderTarget, bool clear = false ] )
```

If no arguments are supplied, the screen is restored as the drawing destination.

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[rendertarget](https://wiki.multitheftauto.com/index.php?search=rendertarget):setAsTarget(...)*

### Optional Arguments

- **renderTarget:** The render target element whose pixels we want to draw on.

- **clear:** If set to true, the render target will also be cleared.

### Returns

Returns *true* if the render target was successfully changed, *false* otherwise.

## Usage restrictions

- Items drawn with *postGUI* set to *true* will not appear on a custom render target.

- dxSetRenderTarget can be set at any time as long as <min_mta_version> in [meta.xml](mta://reference/misc/meta-xml.md) is set to at least 1.3.0-9.04431 e.g. **<min_mta_version client="1.3.0-9.04431" />**

## Example

```
addEventHandler("onClientResourceStart", resourceRoot,
    function()
        myRenderTarget = dxCreateRenderTarget( 80, 100 )  -- Create a render target texture which is 80 x 100 pixels
    end
)

addEventHandler( "onClientRender", root,
    function()
        if myRenderTarget then
            dxSetRenderTarget( myRenderTarget )  -- Select custom render target
            dxDrawText ( "Hello", 10, 20 )       -- The message 'Hello' will be drawn on myRenderTarget

            dxSetRenderTarget()                  -- Select default render target
            dxDrawText ( "Goodbye", 10, 20 )     -- The message 'Goodbye' will be drawn directly to the screen
        end
    end
)
```

This example shows how you can prepare render target contents at anytime (from client version 1.3.0-9.04431)

```
addEventHandler("onClientResourceStart", resourceRoot,
    function()
        myRenderTarget = dxCreateRenderTarget( 80, 100 )     -- Create a render target texture which is 80 x 100 pixels
        dxSetRenderTarget( myRenderTarget )                  -- Select custom render target for drawing
        dxDrawRectangle ( 2, 2, 60, 60, tocolor(255,255,0) ) -- Draw anything you like (to the render target)
        dxDrawText ( "Hello", 10, 20 )
        dxDrawText ( "This is", 10, 40 )
        dxDrawText ( "Amazing", 10, 60 )
        dxSetRenderTarget()                                  -- Unselect custom render target
    end
)

addEventHandler( "onClientRender", root,
    function()
        if myRenderTarget then
            dxDrawImage ( 100, 200, 80, 100, myRenderTarget )        -- Draw myRenderTarget content to the screen
        end
    end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04431 | Removed restrictions on when dxSetRenderTarget could be called |
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

- dxSetRenderTarget

- [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md)

- [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

- [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md)

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
