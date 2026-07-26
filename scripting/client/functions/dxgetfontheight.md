---
doc_id: "mta-wiki:3851"
title: "DxGetFontHeight"
source_title: "DxGetFontHeight"
source_url: "https://wiki.multitheftauto.com/wiki/DxGetFontHeight"
revision_id: 60948
language: "en"
categories: ["Client_functions", "Changes_in_1.4.1", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:48.959672+00:00"
---

# DxGetFontHeight

This function retrieves the theoretical height of a certain piece of text, if it were to be drawn using [dxDrawText](mta://scripting/client/functions/dxdrawtext.md).

| [[{{{image}}}\|link=\|]] | Note: The returned height will be in logical units which are 1.75 times the actual pixel height. |
| --- | --- |
|  |  |

## Syntax

```
int dxGetFontHeight ( [float scale=1, mixed font="default"] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This syntax requires you to ignore the font argument above*

**Method**: *[font](mta://reference/misc/element-dx-font.md):getHeight(...)*

### Required Arguments

*None*

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **scale:** The size of the text.

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

### Returns

Returns an integer of the height of the text.

## Example

The following example will draw two lines of text one above the other.

Click to collapse [-]
Client

```
screenWidth, screenHeight = guiGetScreenSize() -- Get the screen resolution
scale = 2  -- The scale of both texts

-- We add an event handler to keep drawing the text 
addEventHandler("onClientRender",root,function()

   -- Draw the first text 400 pixels from the top and left of the screen
   dxDrawText("Hello!", 400, 400, screenWidth,screenHeight,tocolor(255,255,255,255),scale,"pricedown")

   -- Draw the second text above the first one.
   -- The variable "offset" will return the height of the first text, so we can position the second text above the first one. 
   -- If we changed the scale, the second text would still be above the first one, since we calculated the height of the font. 
   offset = dxGetFontHeight(scale,"pricedown")
   dxDrawText("Hello!", 400, 400 - offset, screenWidth, screenHeight,tocolor(255,255,255,255),scale,"pricedown")
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

- dxGetFontHeight

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
