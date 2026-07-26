---
doc_id: "mta-wiki:14312"
title: "Legacy/DxDrawLine3D"
source_title: "Legacy/DxDrawLine3D"
source_url: "https://wiki.multitheftauto.com/wiki/Legacy/DxDrawLine3D"
revision_id: 79449
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:04.159581+00:00"
---

# Legacy/DxDrawLine3D

This function draws a 3D line between two points in the 3D world - rendered for **one** frame.  This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.

| [[{{{image}}}\|link=\|]] | Note: This page only contains legacy implementations. For current implementation check dxDrawLine3D |
| --- | --- |
|  |  |

BEFORE VERSION 1.5.9 [r22465](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22465):

## Syntax

```
bool dxDrawLine3D ( float startX, float startY, float startZ, float endX, float endY, float endZ [, int color = 0xFFFFFFFF, float width = 1.0, bool postGUI = false ] )
```

### Required Arguments

- **startX:** The start X position of the 3D line, representing a coordinate in the GTA world.

- **startY:** The start Y position of the 3D line, representing a coordinate in the GTA world.

- **startZ:** The start Z position of the 3D line, representing a coordinate in the GTA world.

- **endX:** The end X position of the 3D line, representing a coordinate in the GTA world.

- **endY:** The end Y position of the 3D line, representing a coordinate in the GTA world.

- **endZ:** The end Z position of the 3D line, representing a coordinate in the GTA world.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **color:** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB.

- **width:** The width/thickness of the line

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

This is a small example of creating 3D Line / "Rope" between vehicle and player.

```
function makeLineAppear()
	testVehicle = createVehicle ( 411, 0, 0, 5 ) -- Create our test vehicle.
	addEventHandler("onClientRender", root, createLine)        -- onClientRender keeps the 3D Line visible.
end
function createLine ( )
	x1, y1, z1 = getElementPosition ( testVehicle )                       -- Get test vehicles position.
	x2, y2, z2 = getElementPosition ( localPlayer )                  -- Get local players position.
	dxDrawLine3D ( x1, y1, z1, x2, y2, z2, tocolor ( 0, 255, 0, 230 ), 2) -- Create 3D Line between test vehicle and local player.
end
addCommandHandler("line", makeLineAppear)
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
