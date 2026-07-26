---
doc_id: "mta-wiki:6039"
title: "DxSetShaderTransform"
source_title: "DxSetShaderTransform"
source_url: "https://wiki.multitheftauto.com/wiki/DxSetShaderTransform"
revision_id: 81051
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
---

# DxSetShaderTransform

This function applies a 3D transformation to a [shader](https://wiki.multitheftauto.com/index.php?search=shader) element when it is drawn with [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md).

## Syntax

```
bool dxSetShaderTransform ( element theShader,
                            float rotationX, float rotationY, float rotationZ,
                          [ float rotationCenterOffsetX = 0, float rotationCenterOffsetY = 0, float rotationCenterOffsetZ = 0,
                            bool bRotationCenterOffsetOriginIsScreen = false,
                            float perspectiveCenterOffsetX = 0, float perspectiveCenterOffsetY = 0,
                            bool bPerspectiveCenterOffsetOriginIsScreen = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[shader](https://wiki.multitheftauto.com/index.php?search=shader):setTransform(...)*

### Required Arguments

- **theShader:** The shader element whose transformation is to be changed

- **rotationX:** Rotation angle in degrees around the X axis (Left,right). This will make the shader rotate along its width.

- **rotationY:** Rotation angle in degrees around the Y axis (Up,down). This will make the shader rotate along its height.

- **rotationZ:** Rotation angle in degrees around the Z axis (In,out). This will make the shader rotate in a similar way to the rotation argument in [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md).

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rotationCenterOffsetX :** The center of rotation offset X position in screen relative units.

- **rotationCenterOffsetY :** The center of rotation offset Y position in screen relative units.

- **rotationCenterOffsetZ :** The center of rotation offset Z position in screen relative units.

- **bRotationCenterOffsetOriginIsScreen :** Set to [true](mta://reference/misc/boolean.md) if the center of rotation origin should be the center of the screen rather than the center of the image.

- **perspectiveCenterOffsetX :** The center of perspective offset X position in screen relative units.

- **perspectiveCenterOffsetY :** The center of perspective offset Y position in screen relative units.

- **bPerspectiveCenterOffsetOriginIsScreen :** Set to [true](mta://reference/misc/boolean.md) if the center of perspective origin should be the center of the screen rather than the center of the image.

To convert screen relative units into screen pixel coordinates, *multiply* by the screen size. Conversely, to convert screen pixel coordinates to screen relative units, ***divide*** by the screen size.

### Returns

Returns *true* if the shader element's transform was successfully changed, *false* otherwise.

## Example

```
local shader
local texture
local angle = 0 -- Initialize angle for rotation
local radius = 50 -- Reduced radius for the circular motion
local centerX, centerY -- Center of the screen

function startShaderExample()
    -- Create a shader
    shader = dxCreateShader("texture.fx")
    
    -- Load a texture
    texture = dxCreateTexture("myTexture.png")
    
    -- Apply the texture to the shader
    dxSetShaderValue(shader, "gTexture", texture)
    
    -- Get the center of the screen
    local screenWidth, screenHeight = guiGetScreenSize()
    centerX = screenWidth / 2
    centerY = screenHeight / 2
    
    -- Start rendering the shader
    addEventHandler("onClientRender", root, renderShader)
end
addEventHandler("onClientResourceStart", resourceRoot, startShaderExample)

function renderShader()
    -- Increment the angle to create rotation over time
    angle = angle + 0.02
    if angle > 2 * math.pi then
        angle = 0
    end

    -- Calculate the position based on a smaller circular path
    local positionX = centerX + math.cos(angle) * radius
    local positionY = centerY + math.sin(angle) * radius

    -- Apply transformation: translation along a smaller circular path and rotation
    dxSetShaderTransform(shader, positionX, positionY, 0, 0, 0, angle)
    
    -- Draw a rectangle with the shader applied, following the circular path
    dxDrawImage(positionX - 128, positionY - 128, 256, 256, shader)
end

function stopShaderExample()
    if shader then
        destroyElement(shader)
        shader = nil
    end
    if texture then
        destroyElement(texture)
        texture = nil
    end
    removeEventHandler("onClientRender", root, renderShader)
end
addEventHandler("onClientResourceStop", resourceRoot, stopShaderExample)
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

- [dxIsAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxisaspectratioadjustmentenabled.md)

- [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

- [dxSetBlendMode](mta://scripting/client/functions/dxsetblendmode.md)

- [dxSetPixelColor](mta://scripting/client/functions/dxsetpixelcolor.md)

- [dxSetRenderTarget](mta://scripting/client/functions/dxsetrendertarget.md)

- [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md)

- [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

- dxSetShaderTransform

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
