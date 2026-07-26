---
doc_id: "mta-wiki:14123"
title: "GetColorFilter"
source_title: "GetColorFilter"
source_url: "https://wiki.multitheftauto.com/wiki/GetColorFilter"
revision_id: 82138
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:08.726934+00:00"
---

# GetColorFilter

This function is used to get the values of color filtering.

| [[{{{image}}}\|link=\|]] | Tip: Normally the game is adding these colors to a screen to simulate weather effects. Sometimes it can be important to disable these effects. You can get rid of the effects by calling setColorFilter with zero values. |
| --- | --- |
|  |  |

## Syntax

```
int, int, int, int, int, int, int, int getColorFilter ( bool isOriginal )
```

### Required Arguments

- **isOriginal:** A bool indicates if the return values of color filter are GTASA original or changed by [setColorFilter](mta://scripting/client/functions/setcolorfilter.md). If this is set to *false*, the return values would be the color filter that is currently being used.

### Returns

Returns 8 *[integers](mta://reference/misc/integer.md)*, of which the first 4 indicate the color (R,G,B,A) of color filter A, and the last 4 indicate the color (R,G,B,A) of  color filter B.

## Examples

This example corrects color of dxDrawMaterialLine3D. But this method has some limit.

```
local testRT = dxCreateRenderTarget(32,32,true)

x,y,z = 0, 0, 4
size = 4
addEventHandler("onClientRender", root, function()
	dxSetRenderTarget(testRT,true)
	dxDrawRectangle(0,0,32,32,tocolor(255,255,255,255))
	dxSetRenderTarget()

	local aR,aG,aB,aA,bR,bG,bB,bA = getColorFilter(false)							--Get current color filter
	local cR,cG,cB = 127/255+(aR*aA+bR*bA)/65535*0.5, 127/255+(aG*aA+bG*bA)/65535*0.5, 127/255+(aB*aA+bB*bA)/65535*0.5	--Calculate the result color of color filter
	dxDrawMaterialLine3D(x+size, y+size, z-0.95, x-size, y-size, z-0.95,false, testRT, size*2,tocolor(127, 127, 127, 255))
	dxDrawMaterialLine3D(x+size+20, y+size, z-0.95, x-size+20, y-size, z-0.95,false, testRT, size*2,tocolor(127/cR, 127/cG, 127/cB, 255))
end)
```

This example corrects color of dxDrawMaterialLine3D using shader

```
local shader = [[
float3 colorFilter = float3(1,1,1);
texture sourceTexture;

sampler2D SamplerTex = sampler_state{
    Texture = sourceTexture;
    MipFilter = Linear;
    MinFilter = Linear;
    MagFilter = Linear;
    AddressU = Mirror;
    AddressV = Mirror;
};

float4 colorFilterRemover(float4 color:COLOR0, float2 UV:TEXCOORD0) : COLOR0{
	color *= tex2D(SamplerTex, UV);
	color.rgb /= colorFilter;
	return color;
}

technique cFilterRemover{
	pass P0{
		PixelShader = compile ps_2_0 colorFilterRemover();
	}
}
]]

local cFilterRemover = dxCreateShader(shader)
local testRT = dxCreateRenderTarget(32,32,true)
dxSetShaderValue(cFilterRemover,"sourceTexture",testRT)

x,y,z = 0, 0, 4
size = 4
addEventHandler("onClientRender", root, function()
	dxSetRenderTarget(testRT,true)
	dxDrawRectangle(0,0,32,32,tocolor(255,255,255,255))
	dxSetRenderTarget()

	local aR,aG,aB,aA,bR,bG,bB,bA = getColorFilter(false)							--Get current color filter
	local cR,cG,cB = 127+(aR*aA+bR*bA)/255*0.5, 127+(aG*aA+bG*bA)/255*0.5, 127+(aB*aA+bB*bA)/255*0.5	--Calculate the result color of color filter
	dxSetShaderValue(cFilterRemover,"colorFilter",cR/255,cG/255,cB/255)					--Apply to the color filter remover shader
	dxDrawMaterialLine3D(x+size, y+size, z-0.95, x-size, y-size, z-0.95,false, cFilterRemover, size*2,tocolor(127, 127, 127, 255))
	dxDrawMaterialLine3D(x+size+20, y+size, z-0.95, x-size+20, y-size, z-0.95,false, testRT, size*2,tocolor(127, 127, 127, 255))
end)
```

## See Also

- [areTrafficLightsLocked](mta://scripting/shared/functions/aretrafficlightslocked.md)

- [getAircraftMaxHeight](mta://scripting/shared/functions/getaircraftmaxheight.md)

- [getAircraftMaxVelocity](mta://scripting/shared/functions/getaircraftmaxvelocity.md)

- [getCloudsEnabled](mta://scripting/shared/functions/getcloudsenabled.md)

- [getFarClipDistance](mta://scripting/shared/functions/getfarclipdistance.md)

- [getFogDistance](mta://scripting/shared/functions/getfogdistance.md)

- [getGameSpeed](mta://scripting/shared/functions/getgamespeed.md)

- [getGravity](mta://scripting/shared/functions/getgravity.md)

- [getHeatHaze](mta://scripting/shared/functions/getheathaze.md)

- [getInteriorSoundsEnabled](mta://scripting/shared/functions/getinteriorsoundsenabled.md)

- [getJetpackMaxHeight](mta://scripting/shared/functions/getjetpackmaxheight.md)

- [getMinuteDuration](mta://scripting/shared/functions/getminuteduration.md)

- [getMoonSize](mta://scripting/shared/functions/getmoonsize.md)

- [getOcclusionsEnabled](mta://scripting/shared/functions/getocclusionsenabled.md)

- [getRainLevel](mta://scripting/shared/functions/getrainlevel.md)

- [getSunColor](mta://scripting/shared/functions/getsuncolor.md)

- [getSunSize](mta://scripting/shared/functions/getsunsize.md)

- [getTime](mta://scripting/shared/functions/gettime.md)

- [getTrafficLightState](mta://scripting/shared/functions/gettrafficlightstate.md)

- [getWeather](mta://scripting/shared/functions/getweather.md)

- [getWindVelocity](mta://scripting/shared/functions/getwindvelocity.md)

- [getSkyGradient](mta://scripting/shared/functions/getskygradient.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

- [isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md)

- [getZoneName](mta://scripting/shared/functions/getzonename.md)

- [isGarageOpen](mta://scripting/shared/functions/isgarageopen.md)

- [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md)

- [resetFarClipDistance](mta://scripting/shared/functions/resetfarclipdistance.md)

- [resetFogDistance](mta://scripting/shared/functions/resetfogdistance.md)

- [resetHeatHaze](mta://scripting/shared/functions/resetheathaze.md)

- [resetMoonSize](mta://scripting/shared/functions/resetmoonsize.md)

- [resetRainLevel](mta://scripting/shared/functions/resetrainlevel.md)

- [resetSkyGradient](mta://scripting/shared/functions/resetskygradient.md)

- [resetSunColor](mta://scripting/shared/functions/resetsuncolor.md)

- [resetSunSize](mta://scripting/shared/functions/resetsunsize.md)

- [resetWindVelocity](mta://scripting/shared/functions/resetwindvelocity.md)

- [restoreAllWorldModels](mta://scripting/shared/functions/restoreallworldmodels.md)

- [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md)

- [setAircraftMaxHeight](mta://scripting/shared/functions/setaircraftmaxheight.md)

- [setAircraftMaxVelocity](mta://scripting/shared/functions/setaircraftmaxvelocity.md)

- [setCloudsEnabled](mta://scripting/shared/functions/setcloudsenabled.md)

- [setFarClipDistance](mta://scripting/shared/functions/setfarclipdistance.md)

- [setFogDistance](mta://scripting/shared/functions/setfogdistance.md)

- [setGameSpeed](mta://scripting/shared/functions/setgamespeed.md)

- [setGarageOpen](mta://scripting/shared/functions/setgarageopen.md)

- [setGravity](mta://scripting/shared/functions/setgravity.md)

- [setHeatHaze](mta://scripting/shared/functions/setheathaze.md)

- [setInteriorSoundsEnabled](mta://scripting/shared/functions/setinteriorsoundsenabled.md)

- [setMinuteDuration](mta://scripting/shared/functions/setminuteduration.md)

- [setMoonSize](mta://scripting/shared/functions/setmoonsize.md)

- [setOcclusionsEnabled](mta://scripting/shared/functions/setocclusionsenabled.md)

- [setRainLevel](mta://scripting/shared/functions/setrainlevel.md)

- [setSkyGradient](mta://scripting/shared/functions/setskygradient.md)

- [setSunColor](mta://scripting/shared/functions/setsuncolor.md)

- [setSunSize](mta://scripting/shared/functions/setsunsize.md)

- [setTime](mta://scripting/shared/functions/settime.md)

- [setTrafficLightState](mta://scripting/shared/functions/settrafficlightstate.md)

- [setTrafficLightsLocked](mta://scripting/shared/functions/settrafficlightslocked.md)

- [setWeather](mta://scripting/shared/functions/setweather.md)

- [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md)

- [setWindVelocity](mta://scripting/shared/functions/setwindvelocity.md)

- [setJetpackMaxHeight](mta://scripting/shared/functions/setjetpackmaxheight.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

- [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [resetWorldProperties](mta://scripting/shared/functions/resetworldproperties.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909):

- [removeGameWorld](mta://scripting/client/functions/removegameworld.md)

- [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md)
