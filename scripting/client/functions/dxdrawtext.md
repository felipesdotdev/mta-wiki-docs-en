---
doc_id: "mta-wiki:3849"
title: "DxDrawText"
source_title: "DxDrawText"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawText"
revision_id: 82168
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0", "Changes_in_1.3.5", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:47.821255+00:00"
---

# DxDrawText

Draws a string of text on the screen for one frame. In order for the text to stay visible continuously, you need to call this function with the same parameters on each frame update (see [onClientRender](mta://scripting/client/events/onclientrender.md)).

## Syntax

```
bool dxDrawText ( string text, float leftX, float topY, [ float rightX = leftX, float bottomY = topY, int color = white, float textSize,
                  mixed font = "default", string alignX = "left", string alignY = "top", bool clip = false, bool wordBreak = false,
                  bool postGUI = false, bool colorCoded = false, bool subPixelPositioning = false,
                  float fRotation = 0.0, float fRotationCenterX = 0.0, float fRotationCenterY = 0.0, float fLineSpacing = 0.0 ] )
```

### Required Arguments

- **text:** the text to draw

- **leftX:** the absolute X coordinate of the top left corner of the text

- **topY:** the absolute Y coordinate of the top left corner of the text

### Optional Arguments

- **rightX:** the absolute X coordinate of the right side of the text bounding box. Used for text aligning, clipping and word breaking.

- **bottomY:** the absolute Y coordinate of the bottom side of the text bounding box. Used for text aligning, clipping and word breaking.

- **color:** the color of the text, a value produced by [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **textSize:** the size of the text scale.

- **font:** Either a custom [DX font](mta://reference/misc/dx-font.md) element or the name of a built-in DX font: **Note: Some fonts are incompatible with certain languages such as Arabic.**

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

## Remarks

The function is known to *optimize* certain drawing scenarios related to scaling and opacity (so called **text on raster optimisation**). You can find out more about it [here](https://forum.mtasa.com/topic/132881-scaling-dx-elements-for-all-resolution/?do=findComment&comment=1002485).

## Example

This example code will add the current zone name in the lower left corner of the players' screens.

```
local screenX, screenY = guiGetScreenSize() -- get the screen resolution (width and height)
local shadowColor = tocolor(0, 0, 0, 255) -- define shadow color outside render scope and use it afterwards (for performance reasons)
local textColor = tocolor(255, 255, 255, 255) -- define color outside render scope and use it afterwards (for performance reasons)

function renderPlayerZone()
    local playerX, playerY, playerZ = getElementPosition(localPlayer) -- get our player's coordinates
    local playerZoneName = getZoneName(playerX, playerY, playerZ) -- get name of the zone the player is in

    -- draw zone name text's shadow
    dxDrawText(playerZoneName, 44, screenY - 41, screenX, screenY, shadowColor, 1.02, "pricedown")
    -- draw zone name text
    dxDrawText(playerZoneName, 44, screenY - 43, screenX, screenY, textColor, 1, "pricedown")
end
addEventHandler("onClientRender", root, renderPlayerZone)
```

This example shows how to set both horizontal and vertical text size.

```
local screenX, screenY = guiGetScreenSize() -- get the screen resolution (width and height)
local textColor = tocolor(255, 255, 255, 255) -- define color outside render scope and use it afterwards (for performance reasons)

function renderGameTick()
    local tickNow = getTickCount()

    dxDrawText(tickNow, 44, screenY - 43, screenX, screenY, textColor, 1, 2, "pricedown")
end
addEventHandler("onClientRender", root, renderGameTick)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.03986 | Added colorCoded and subPixelPositioning arguments |
| --- | --- |

| 1.3.5-9.06054 | Added fRotation , fRotationCenterX and fRotationCenterY arguments |
| --- | --- |

| 1.5.8-9.20957 | Added fLineSpacing argument |
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

- dxDrawText

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
