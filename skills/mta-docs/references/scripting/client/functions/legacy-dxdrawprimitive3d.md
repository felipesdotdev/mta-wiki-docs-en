---
doc_id: "mta-wiki:14316"
title: "Legacy/dxDrawPrimitive3D"
source_title: "Legacy/dxDrawPrimitive3D"
source_url: "https://wiki.multitheftauto.com/wiki/Legacy/dxDrawPrimitive3D"
revision_id: 81362
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
---

# Legacy/dxDrawPrimitive3D

This function draws a 3D primitive in the 3D world - rendered for **one** frame.  This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.

| [[{{{image}}}\|link=\|]] | Note: This page only contains legacy implementations. For current implementation check dxDrawPrimitive3D |
| --- | --- |
|  |  |

BEFORE VERSION 1.5.9 [r22465](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22465):

## Syntax

```
bool dxDrawPrimitive3D ( string primitiveType, bool postGUI, table vertex1, table vertex2, table vertex3 [, table vertex4, ...] )
```

 

A four vertex primitive example using "trianglefan"

### Required Arguments

- **primitiveType:** The type of primitive to be drawn. This could be:

```
"pointlist"
   "linelist"
   "linestrip"
   "trianglefan"
   "trianglelist"
   "trianglestrip"
```

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **vertex1:** A table with the coordinates of the vertex plus its color.

- **vertex2:** A table with the coordinates of the vertex plus its color.

- **vertex3:** A table with the coordinates of the vertex plus its color.

The vertex should be passed like this:

```
{x, y, z, color}
```

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **vertexN:** A table with the coordinates of the vertex plus its color. You can add as much as you want.

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

This is a small example of creating 3D Primitive object with 4 vertex that will spawn on 'The Well Stacked Pizza Co.' in Idlewood.

```
local primitive = {
    {2087.8, -1804.2, 13.5, tocolor(255, 0, 0)}, 
    {2087.7, -1810.5, 13.5, tocolor(0, 255, 0)}, 
    {2092.7, -1813.6, 17.7, tocolor(0, 0, 255)},
    {2097.5, -1806.8, 16, tocolor(255, 255, 255)}
}

function draw()
    dxDrawPrimitive3D("trianglefan", false, unpack(primitive))
end
addEventHandler("onClientRender", root, draw)
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
