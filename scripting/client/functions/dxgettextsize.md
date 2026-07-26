---
doc_id: "mta-wiki:12274"
title: "DxGetTextSize"
source_title: "DxGetTextSize"
source_url: "https://wiki.multitheftauto.com/wiki/DxGetTextSize"
revision_id: 81236
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:49.657305+00:00"
---

# DxGetTextSize

This function retrieves the theoretical width and height (in pixels) of a certain piece of text, if it were to be drawn using [dxDrawText](mta://scripting/client/functions/dxdrawtext.md).

**NOTE:** This function already takes the client's screen resolution into account.

## Syntax

```
float, float dxGetTextSize ( string text [, float width = 0, float scaleXY = 1.0 [, float scaleY = 1.0 ], mixed font = "default", bool wordBreak = false, bool colorCoded = false] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This syntax requires you to ignore the font argument above*

**Method**: *[font](mta://reference/misc/element-dx-font.md):getSize(...)*

### Required Arguments

- **text:** A string representing the text for which you wish to retrieve with width for.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **width:** The width of the text. Use with *wordBreak = true*.

- **scaleX:** The scale of the text. Scale can also be inputted as a [Vector2](mta://reference/misc/vector2.md).

- **scaleY:** The scale of the text.

- **font:** Either a custom [DX font](mta://reference/misc/dx-font.md) element or the name of a built-in dx font:

- **"default":**  Tahoma

- **"default-bold":** Tahoma Bold

- **"clear":** Verdana

- **"arial":** Arial

- **"sans":** Microsoft Sans Serif

- **"pricedown":** Pricedown (GTA's theme text)

- **"bankgothic":** Bank Gothic Medium

- **"diploma":** Diploma Regular

- **"beckett":** Beckett Regular

- **"unifont":** Unifont

- **wordBreak:** If set to *true*, the text will wrap to a new line whenever it reaches the right side of the bounding box. If *false*, the text will always be completely on one line.

- **colorCoded:** Should we exclude color codes from the width? False will include the hex in the length.

### Returns

Returns two floats representing the width and height of the text in pixels.

## Example

This example draws a text with black background at the bottom right corner of the screen.

```
local screenWidth, screenHeight = guiGetScreenSize()

local message = "Incredibly huuuuuuuge message"
local messageOffset = 32
local messagePadding = 16
local messageWidth = 256

function renderMessage()
    local textWidth, textHeight = dxGetTextSize(message, messageWidth, 2, "default", true)
    local x = screenWidth - textWidth - messageOffset
    local y = screenHeight - textHeight - messageOffset
    dxDrawRectangle(x - messagePadding, y - messagePadding, textWidth + messagePadding * 2, textHeight + messagePadding * 2, 0x80000000) -- draw background
    dxDrawText(message, x, y, x + textWidth, y + textHeight, 0xFFFFFFFF, 2, "default", "left", "top", false, true)
end
addEventHandler("onClientRender", root, renderMessage)
```

 
Example

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

- dxGetTextSize

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
