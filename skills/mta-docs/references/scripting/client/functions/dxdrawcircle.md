---
doc_id: "mta-wiki:7344"
title: "DxDrawCircle"
source_title: "DxDrawCircle"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawCircle"
revision_id: 73127
language: "en"
categories: ["Client_functions", "Changes_in_1.5.5", "Utility_templates", "Changes_in_1.6.0"]
---

# DxDrawCircle

This function draws a circle shape on the screen - rendered for **one** frame.  This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to be display continuously.

## Syntax

```
bool dxDrawCircle ( float posX, float posY, float radius [, float startAngle = 0.0, float stopAngle = 360.0, int theColor = white,
                    int theCenterColor = theColor, int segments = 32, int ratio = 1, bool postGUI = false ] )
```

### Required Arguments

 

An example of how dxDrawCircle function works in practice.

- **posX**: An integer representing the **absolute** X position of the circle center, represented by pixels on the screen.

- **posY**: An integer representing the **absolute** Y position of the circle center, represented by pixels on the screen.

- **radius**: An integer representing the radius scale of the circle that is being drawn.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **startAngle**: An integer representing the angle of the first point of the circle.

- **stopAngle**: An integer representing the angle of the last point of the circle.

- **theColor**: An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **theCenterColor**: An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **segments**: An integer ranging from 3-1024 representing how many triangles are used to form the circle, more segments = smoother circle. Note: using lots of segments may cause lag.

- **ratio**: Ratio between width and height, e.g: 2 would mean that the width of the circle is 2 times the height.

- **postGUI**: A bool representing whether the circle should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

### Returns

Returns *true* if the creation of the 2D circle was successful, *false* otherwise.

## Remarks

By documentation this function does perform a **triangle approximation of the cicle**. This is important for when there is no shader support on the end-user hardware. If there is shader support then you can instead use shaders with euler-based math (sin/cos/asin) to create a smoother circle. The performance does scale much better than increasing the segment count of this function because drawing using shader would take up only one draw-call. Take look at [this post](https://forum.mtasa.com/topic/133045-dxdrawcircle-chart/?do=findComment&comment=1002953) for more details.

The above remark is about drawing circles on modern end-user hardware with angle-interval support, as necessary by example for pie-charts. **Drawing full circles** is easier because the math can be simplified to a euler distance calculation from the texcoord (0.5, 0.5) to the currently drawing pixel. Then the HLSL clip function can be used to not render any pixels outside of the circle. Read more about it in [this post](https://forum.mtasa.com/topic/133453-round-render-target/#comment-1004102).

## Example

This function draws a rectangle with rounded corners.

```
function dxDrawRoundedRectangle(x, y, rx, ry, color, radius)
    rx = rx - radius * 2
    ry = ry - radius * 2
    x = x + radius
    y = y + radius

    if (rx >= 0) and (ry >= 0) then
        dxDrawRectangle(x, y, rx, ry, color)
        dxDrawRectangle(x, y - radius, rx, radius, color)
        dxDrawRectangle(x, y + ry, rx, radius, color)
        dxDrawRectangle(x - radius, y, radius, ry, color)
        dxDrawRectangle(x + rx, y, radius, ry, color)

        dxDrawCircle(x, y, radius, 180, 270, color, color, 7)
        dxDrawCircle(x + rx, y, radius, 270, 360, color, color, 7)
        dxDrawCircle(x + rx, y + ry, radius, 0, 90, color, color, 7)
        dxDrawCircle(x, y + ry, radius, 90, 180, color, color, 7)
    end
end
dxDrawRoundedRectangle(350, 50, 100, 100, tocolor(0, 255, 0, 255), 20)
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md)

- [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md)

- dxDrawCircle

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
