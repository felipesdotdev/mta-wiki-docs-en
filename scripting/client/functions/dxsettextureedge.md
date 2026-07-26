---
doc_id: "mta-wiki:7574"
title: "DxSetTextureEdge"
source_title: "DxSetTextureEdge"
source_url: "https://wiki.multitheftauto.com/wiki/DxSetTextureEdge"
revision_id: 45969
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:51.454454+00:00"
---

# DxSetTextureEdge

This functions allows you to change the edge handling after creating the texture.

## Syntax

```
bool dxSetTextureEdge ( texture theTexture, string textureEdge [, int border-color] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[texture](mta://reference/misc/texture.md):setEdge(...)*

### Required Arguments

- **theTexture:** The affected texture

- **textureEdge:** The texture edge mode. Available modes are **wrap, mirror, clamp, border, mirror-once**

### Optional Arguments

- **border-color:** If textureEdge is set to border, you are able to define a border color here

## Example

The following example draws the image above ingame.

Click to collapse [-]
Client

```
local renderTarget1 = dxCreateScreenSource(300, 300)
dxSetTextureEdge(renderTarget1, "wrap")
local renderTarget2 = dxCreateScreenSource(300, 300)
dxSetTextureEdge(renderTarget2, "mirror")
local renderTarget3 = dxCreateScreenSource(300, 300)
dxSetTextureEdge(renderTarget3, "clamp")
local renderTarget4 = dxCreateScreenSource(300, 300)
dxSetTextureEdge(renderTarget4, "border", tocolor(255, 0, 0))

addEventHandler("onClientRender", root,
	function()
		-- Update the screen sources
		dxUpdateScreenSource(renderTarget1)
		dxUpdateScreenSource(renderTarget2)
		dxUpdateScreenSource(renderTarget3)
		dxUpdateScreenSource(renderTarget4)
	
		-- Draw screen sources in different modes
		dxDrawImageSection(20, 200, 300, 300, -50, 0, 100, 100, renderTarget1)
		dxDrawImageSection(350, 200, 300, 300, -50, 0, 100, 100, renderTarget2)
		dxDrawImageSection(680, 200, 300, 300, -50, 0, 100, 100, renderTarget3)
		dxDrawImageSection(1010, 200, 300, 300, -50, 0, 100, 100, renderTarget4)
	end
)
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

- dxSetTextureEdge

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
