---
doc_id: "mta-wiki:5679"
title: "DxCreateRenderTarget"
source_title: "DxCreateRenderTarget"
source_url: "https://wiki.multitheftauto.com/wiki/DxCreateRenderTarget"
revision_id: 81685
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxCreateRenderTarget

This function creates a render target element, which is a special type of [texture](https://wiki.multitheftauto.com/index.php?search=texture) that can be drawn on with the dx functions. Successful render target creation is not guaranteed, and may fail due to hardware or memory limitations.

To see if creation is likely to fail, use [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md). (When **VideoMemoryFreeForMTA** is zero, failure *is* guaranteed.)

| [[{{{image}}}\|link=\|]] | Tip: Use dxSetBlendMode to get better quality |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: It is highly recommended that dxSetTestMode is used when writing and testing scripts using dxCreateRenderTarget. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Render targets are usually cleared when the player minimizes MTA (i.e. alt-tab). See onClientRestore for details on when to restore any fixed content. |
| --- | --- |
|  |  |

## Syntax

```
element dxCreateRenderTarget ( int width, int height [, bool withAlpha = false ] )
```

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21938](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21938))

```
element dxCreateRenderTarget ( int width, int height, surface-format surfaceFormat )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxRenderTarget](https://wiki.multitheftauto.com/index.php?search=DxRenderTarget)(...)*

### Required Arguments

- **width :** The width of the texture in pixels.

- **height :** The height of the texture in pixels.

- **withAlpha:** The render target will be created with an alpha channel. 'false' will turn images' alpha channels to black color

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21938](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21938))

- **surfaceFormat :** A string containing the surface format. See [Surface formats](mta://reference/misc/surface-format.md). Default format without alpha is "x8r8g8b8", default with alpha is "a8r8g8b8".

### Returns

Returns a [texture](https://wiki.multitheftauto.com/index.php?search=texture) element if successful, *false* if the system is unable to create a render target.

**You should always check to see if this function has returned false.**

## Explanation

What is a render target?

A render target is like a blank canvas. You can draw on the render target as many times as you like - and even clear it.

If your dxDraw* calls are static (meaning the appearance doesn't change), or only update periodically, then a render target can be useful not only for cleaner code - but for performance reasons too. Instead of making possibly hundreds of dxDraw* calls every frame, you can simply make those calls on a single frame and draw directly to the render target, then use a **single** dxDrawImage call every frame afterwards to display the render target.

Render targets can also be used to create and display the same thing multiple times, as shown in the example below.

## Example

```
local myRenderTarget

addEventHandler("onClientResourceStart", resourceRoot,
    function()
        myRenderTarget = dxCreateRenderTarget(250, 100, true)       -- Create a render target

        if (myRenderTarget) then 
            updateRenderTarget()     -- Our function to draw to the render target (see below)
        end
    end
)

addEventHandler( "onClientRender", root,
    function()
        if myRenderTarget then
            -- Draw the render target lots of times in different positions on the screen
            dxDrawImage(350, 50, 250, 100, myRenderTarget)
            dxDrawImage(450, 380, 250, 100, myRenderTarget)
            dxDrawImage(550, 250, 250, 100, myRenderTarget)
            dxDrawImage(650, 70, 250, 100, myRenderTarget)
        end
    end
)

function updateRenderTarget()
    dxSetRenderTarget(myRenderTarget, true)
    dxSetBlendMode("modulate_add")  -- Set 'modulate_add' when drawing stuff on the render target

    dxDrawText("Hello " .. getTickCount(), 10, 10, 0, 0, tocolor(255, 255, 255, 255), 2, "clear")        -- Draw a message
    dxDrawRectangle(10, 50, 40, 40, tocolor(math.random(255), math.random(255), math.random(255)))       -- Draw a square with random color

    -- ... etc, imagine you have a lot of dxDraw* calls to make, this is where render targets come in handy!

    dxSetBlendMode("blend")  -- Restore default blending
    dxSetRenderTarget()      -- Restore default render target
end

-- We can even update the render target on the fly, by binding it to a key
bindKey("r", "down", updateRenderTarget)
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- dxCreateRenderTarget

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
