---
doc_id: "mta-wiki:13849"
title: "Resource : RDX"
source_title: "Resource:Fixing"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AFixing"
revision_id: 75954
language: "en"
categories: ["Changes_in_1.6.0"]
generated_at: "2026-07-26T16:17:01.329689+00:00"
---

# Resource : RDX

Download

Github Source: [https://github.com/Mr3bOfficial/rdx](https://github.com/Mr3bOfficial/rdx)

### How to Use

First you need to add to the top of your code *loadstring(exports.rdx:import())()* then you have to change some codes as showing in examples

### Notes

1 - You need to change the resolution from *rdx/config/data.lua* to your resolution.  

2 - Do not change any thing in *rdx/server-side/update.lua* or *rdx/update.cfg*.  

3 - To update the resource you need to type */update-rdx*.

## Functions

- [dxText](mta://scripting/client/functions/dxdrawtext.md)

- [dxImage](mta://scripting/client/functions/dxdrawimage.md)

- [dxRectangle](mta://scripting/client/functions/dxdrawrectangle.md)

- [dxRoundedRectangle](mta://scripting/shared/functions/roundedrectangle.md)

- [dxIsInPosition](mta://scripting/shared/functions/ismouseinposition.md)

- [dxCircle](mta://scripting/client/functions/dxdrawcircle.md)

- [dxImageSection](mta://scripting/client/functions/dxdrawimagesection.md)

- [guiWindow](mta://scripting/client/functions/guicreatewindow.md)

- [guiButton](mta://scripting/client/functions/guicreatebutton.md)

- [guiMemo](mta://scripting/client/functions/guicreatememo.md)

- [guiLabel](mta://scripting/client/functions/guicreatelabel.md)

- [guiCheckBox](mta://scripting/client/functions/guicreatecheckbox.md)

- [guiEdit](mta://scripting/client/functions/guicreateedit.md)

- [guiProgress](mta://scripting/client/functions/guicreateprogressbar.md)

- [guiRadioButton](mta://scripting/client/functions/guicreateradiobutton.md)

- [guiGridList](mta://scripting/client/functions/guicreategridlist.md)

- [guiTabPanel](mta://scripting/client/functions/guicreatetabpanel.md)

- [guiTab](mta://scripting/client/functions/guicreatetab.md)

- [guiImage](mta://scripting/client/functions/guicreatestaticimage.md)

- [guiScrollBar](mta://scripting/client/functions/guicreatescrollbar.md)

- [guiScrollPane](mta://scripting/client/functions/guicreatescrollpane.md)

- [guiComboBox](mta://scripting/client/functions/guicreatecombobox.md)

## Example

Click to collapse [-]
Client

```
loadstring(exports.rdx:import())()

addEventHandler("onClientRender", root,
    function()
        dxRectangle(468, 279, 430, 211, tocolor(255, 255, 255, 255), false)
        dxText("Hello this is Mr3b", 468, 279, 898, 307, tocolor(0, 0, 0, 254), 1.00, "default", "center", "center", false, false, false, false, false)
        dxImage(622, 338, 123, 92, ":guieditor/images/examples/mtalogo.png", 0, 0, 0, tocolor(255, 255, 255, 255), false)
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

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
