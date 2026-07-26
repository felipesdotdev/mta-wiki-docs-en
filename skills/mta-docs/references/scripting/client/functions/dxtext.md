---
doc_id: "mta-wiki:13851"
title: "DxText"
source_title: "DxText"
source_url: "https://wiki.multitheftauto.com/wiki/DxText"
revision_id: 75953
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxText

This function draws a dxText but it will make it relative.

## Syntax

```
bool dxDrawText ( string text, float leftX, float topY [, float rightX = leftX, float bottomY = topY, int color = white, float scaleXY = 1.0 [, float scaleY = 1.0 ],
                  mixed font = "default", string alignX = "left", string alignY = "top", bool clip = false, bool wordBreak = false,
                  bool postGUI = false, bool colorCoded = false, bool subPixelPositioning = false,
                  float fRotation = 0.0, float fRotationCenterX = 0.0, float fRotationCenterY = 0.0, float fLineSpacing = 0.0] )
```

### Required Arguments

- **text:** the text to draw

- **leftX:** the absolute X coordinate of the top left corner of the text

- **topY:** the absolute Y coordinate of the top left corner of the text

### Optional Arguments

- **rightX:** the absolute X coordinate of the right side of the text bounding box. Used for text aligning, clipping and word breaking.

- **bottomY:** the absolute Y coordinate of the bottom side of the text bounding box. Used for text aligning, clipping and word breaking.

- **color:** the color of the text, a value produced by [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **scale:** the size of the text.**scale:** can (optionally) be specified as two floats. i.e. **scaleX, scaleY**

- **font:** Either a custom [DX font](https://wiki.multitheftauto.com/index.php?search=DX%20font) element or the name of a built-in DX font: **Note: Some fonts are incompatible with certain languages such as Arabic.**

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

- **alignX:** horizontal alignment of the text within the bounding box. Can be **"left"**, **"center"** or **"right"**.

- **alignY:** vertical alignment of the text within the bounding box. Can be **"top"**, **"center"** or **"bottom"**.

- **clip:** if set to *true*, the parts of the text that don't fit within the bounding box will be cut off.

- **wordBreak:** if set to *true*, the text will wrap to a new line whenever it reaches the right side of the bounding box. If *false*, the text will always be completely on one line.

- **postGUI:** A bool representing whether the text should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes. **Note: clip and wordBreak are forced false if this is set.**

- **subPixelPositioning:** A bool representing whether the text can be positioned sub-pixel-ly. Looks nicer for moving/scaling animations.

- **fRotation:** Rotation****

- **fRotationCenterX:** Rotation Origin X****

- **fRotationCenterY:** Rotation Origin Y****

- **fLineSpacing:** Distance in pixels between the lines of text, this can be a negative number, works only when **colorCoded** is set to true**

### Returns

Returns *true* if successful, *false* otherwise.

## Resource

[RDX](https://wiki.multitheftauto.com/wiki/Resource:RDX)

## Example

Click to collapse [-]
Client

```
loadstring(exports.rdx:import())()

function drawStuff()
	dxText("Hello this is Mr3b", 468, 279, 898, 307, tocolor(0, 0, 0, 254), 1.00, "default", "center", "center", false, false, false, false, false)
end
addEventHandler("onClientRender", root, drawStuff)
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

- [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md)

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
