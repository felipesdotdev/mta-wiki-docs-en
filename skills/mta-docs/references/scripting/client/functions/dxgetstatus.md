---
doc_id: "mta-wiki:5812"
title: "DxGetStatus"
source_title: "DxGetStatus"
source_url: "https://wiki.multitheftauto.com/wiki/DxGetStatus"
revision_id: 76812
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# DxGetStatus

This function gets information about various internal datum.

## Syntax

```
table dxGetStatus ( )
```

### Returns

Returns a table with the following entries:

- **TestMode:** The current dx test mode. See [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md).

- **VideoCardName:** The name of the graphics card.

- **VideoCardRAM:** The installed memory in MB of the graphics card.

- **VideoCardPSVersion:** The maximum pixel shader version of the graphics card.

- **VideoCardMaxAnisotropy:** The maximum anisotropic filtering available. (0-4 which respectively mean: off, 2x, 4x, 8x, 16x)

- **VideoCardNumRenderTargets:** The maximum number of simultaneous render targets a shader can use.

- **VideoMemoryFreeForMTA:** The amount of memory in MB available for MTA to use. **When this gets to zero, [guiCreateFont](mta://scripting/client/functions/guicreatefont.md), [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md) and [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md) will fail.**

- **VideoMemoryUsedByFonts:** The amount of graphic memory in MB used by custom fonts.

- **VideoMemoryUsedByTextures:** The amount of graphic memory in MB used by textures.

- **VideoMemoryUsedByRenderTargets:** The amount of graphic memory in MB used by render targets.

- **SettingWindowed:** The windowed setting. (true/false)

- **SettingFullScreenStyle:** Display style when in full screen mode. (0-2 which respectively mean: Standard, Borderless window, Borderless keep res)

- **SettingFXQuality:** The FX Quality. (0-3)

- **SettingDrawDistance:** The draw distance setting. (0-100)

- **SettingVolumetricShadows:** The volumetric shadows setting. (true/false)

- **SettingStreamingVideoMemoryForGTA:** The usable graphics memory setting. (64-256)

- **SettingAnisotropicFiltering:** The anisotropic filtering setting. (0-4 which respectively mean: off, 2x, 4x, 8x, 16x)

- **SettingAntiAliasing:** The anti-aliasing setting. (0-3 which respectively mean: off, 1x, 2x, 3x)

- **SettingHeatHaze:** The heat haze setting. (true/false)

- **SettingGrassEffect:** The grass effect setting. (true/false)

- **Setting32BitColor:** The color depth of the screen. (false is 16bit, true is 32bit)

- **SettingHUDMatchAspectRatio:** The hud match aspect ratio setting. (true/false)

- **SettingAspectRatio:** The aspect ratio setting. ("auto", "4:3", "16:10", "16:9")

- **SettingFOV:** The FOV setting.

- **SettingHighDetailVehicles:** High detail vehicles setting. (true/false)

- **SettingHighDetailPeds:** High detail peds setting. (true/false)

- **SettingCoronaReflections:** Corona rain reflections setting. (true/false)

- **SettingDynamicPedShadows:** Dynamic ped shadows setting. (true/false)

- **AllowScreenUpload:** The allows screen uploads setting. (true/false)

- **DepthBufferFormat:** The format of the shader readable depth buffer, or 'unknown' if not available.

- **TotalPhysicalMemory:** The amount of total physical memory in MB.

- **UsingDepthBuffer:** *true* if the depth buffer is used, *false* otherwise.

- **SettingDebugMode:** Selected option in Settings -> Advanced tab -> Debug setting ("Default", "#6734 Graphics", "#6732 D3D", "#0000 Log timing", "#0000 Joystick", "#0000 Lua trace", "#0000 Resize always", "#0000 Resize never")

## Example

```
addCommandHandler("getinfo",
	function ()
		local info = dxGetStatus ()
		for k, v in pairs (info) do
			outputChatBox (k .. " : " .. tostring (v))
		end
	end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04715 | Added DepthBufferFormat argument |
| --- | --- |

| 1.3.0-9.04811 | Added VideoCardMaxAnisotropy, SettingAnisotropicFiltering, SettingAntiAliasing, SettingHeatHaze, SettingGrassEffect and Setting32BitColor arguments |
| --- | --- |

| 1.3.4-9.05731 | Added SettingHUDMatchAspectRatio and SettingAspectRatio |
| --- | --- |

| 1.4.1-9.07181 | Added SettingFOV |
| --- | --- |

| 1.4.1-9.07310 | Added VideoCardNumRenderTargets |
| --- | --- |

| 1.5.2-9.07816 | Added UsingDepthBuffer |
| --- | --- |

| 1.5.3-9.11199 | Added SettingHighDetailVehicles |
| --- | --- |

| 1.5.5-9.11814 | Added SettingFullScreenStyle Fixed SettingWindowed |
| --- | --- |

| 1.5.8-9.20508 | Added SettingHighDetailPeds |
| --- | --- |

| 1.5.8-9.20901 | Added TotalPhysicalMemory |
| --- | --- |

| 1.6.0-9.21785 | Added SettingDebugMode |
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

- [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)

- [dxDrawWiredSphere](mta://scripting/client/functions/dxdrawwiredsphere.md)

- [dxGetBlendMode](mta://scripting/client/functions/dxgetblendmode.md)

- [dxGetFontHeight](mta://scripting/client/functions/dxgetfontheight.md)

- [dxGetMaterialSize](mta://scripting/client/functions/dxgetmaterialsize.md)

- [dxGetPixelColor](mta://scripting/client/functions/dxgetpixelcolor.md)

- [dxGetPixelsSize](mta://scripting/client/functions/dxgetpixelssize.md)

- [dxGetPixelsFormat](mta://scripting/client/functions/dxgetpixelsformat.md)

- dxGetStatus

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
