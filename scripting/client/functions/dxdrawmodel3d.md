---
doc_id: "mta-wiki:14181"
title: "DxDrawModel3D"
source_title: "DxDrawModel3D"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawModel3D"
revision_id: 82586
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:46.291535+00:00"
---

# DxDrawModel3D

| [[{{{image}}}\|link=\|]] | Important Note: You can not use this function to draw vehicles and ped |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: This function doesn't obey any streaming limits, you can draw as many models as you want |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: You can not render model to render target. |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

This function draws a 3D model - rendered for **one** frame. Drawn models are indistinguishable from this one created by [createObject](mta://scripting/shared/functions/createobject.md) function. This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) or [onClientPreRender](mta://scripting/client/events/onclientprerender.md) in order to display continuously. Note that a model must be loaded at the time this function is called. A model can be loaded and unloaded with the help of [engineStreamingRequestModel](mta://scripting/client/functions/enginestreamingrequestmodel.md) and [engineStreamingReleaseModel](mta://scripting/client/functions/enginestreamingreleasemodel.md) functions.

## Syntax

```
bool dxDrawModel3D( int modelId, float positionX, float positionY, float positionZ, float rotationX, float rotationY, float rotationZ [, float scaleX = 1, float scaleY = 1, float scaleZ = 1, float lighting = 0 ])
```

 

Model during day

 

Model during night

### Required Arguments

- **modelId:** [object](mta://reference/misc/object.md) you want to draw, must be regular object, you can not draw vehicles and peds. See [Object IDs](mta://reference/misc/object-ids.md) for a list of model IDs.

- **positionX:** A floating point number representing the X coordinate on the map.

- **positionY:** A floating point number representing the Y coordinate on the map.

- **positionZ:** A floating point number representing the Z coordinate on the map.

- **rotationX:** A floating point number representing the rotation about the X axis in degrees.

- **rotationY:** A floating point number representing the rotation about the Y axis in degrees.

- **rotationZ:** A floating point number representing the rotation about the Z axis in degrees.

### Optional Arguments

- **scaleX**: a float containing the new scale on the X axis

- **scaleY**: a float containing the new scale on the Y axis

- **scaleZ**: a float containing the new scale on the Z axis

ADDED/UPDATED IN VERSION 1.6.0 [r22862](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22862):

- **lighting:** Lighting of model. Allowed range is [0, 1].

### Returns

Returns true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Simple example

This example draws a model

```
local modelId = 1337

local function drawMyModel()
    dxDrawModel3D(modelId, 0, 0, 4, 0, 0, 0)
end

local function startDraw()
    engineStreamingRequestModel(modelId, true, true)
    addEventHandler("onClientPreRender", root, drawMyModel)
end

local function stopDraw()
    engineStreamingReleaseModel(modelId, true)
    removeEventHandler("onClientPreRender", root, drawMyModel)
end
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

- dxDrawModel3D

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
