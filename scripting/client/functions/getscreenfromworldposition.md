---
doc_id: "mta-wiki:2693"
title: "GetScreenFromWorldPosition"
source_title: "GetScreenFromWorldPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetScreenFromWorldPosition"
revision_id: 76383
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.0", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:24.009599+00:00"
---

# GetScreenFromWorldPosition

This function gets the screen position of a point in the world. This is useful for attaching 2D gui elements to parts of the world (e.g. players) or detecting if a point is on the screen (though it does not check if it is actually visible, you should use [processLineOfSight](mta://scripting/client/functions/processlineofsight.md) for that).

## Syntax

```
float, float, float getScreenFromWorldPosition ( float x, float y, float z [, float edgeTolerance = 0.0, bool relative = true ] )
```

### Required Arguments

- **x:** A float value indicating the x position in the world.

- **y:** A float value indicating the y position in the world.

- **z:** A float value indicating the z position in the world.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **edgeTolerance:** A [float](mta://reference/misc/float.md) value indicating the distance the position can be off screen before the function returns false. Note: it's clamped down on both axies to the size of screen at the given axis*10

- **relative:** A [boolean](mta://reference/misc/boolean.md) value that indicates if edgeTolerance is in pixels [false], or relative to the screen size [true].

### Returns

Returns two *x*, *y* [floats](mta://reference/misc/float.md) indicating the screen position and [float](mta://reference/misc/float.md) distance between screen and given position if successful, *false* otherwise.

### Example

Click to collapse [-]
Client-side Script

This example add a '3d' text at coordinates 0, 0, 0 (center of map).

```
addEventHandler ( "onClientRender", root,
function ( )
	if ( getDistanceBetweenPoints3D ( 0, 0, 3, getElementPosition ( localPlayer ) ) ) < 50 then
		local coords = { getScreenFromWorldPosition ( 0, 0, 3 ) }
		if coords[1] and coords[2] then
			dxDrawText ( "Hello !", coords[1], coords[2], coords[1], coords[2], tocolor(255,255,255), 1, "default-bold" )
		end
	end
end )
```

## See Also

- [createSWATRope](mta://scripting/client/functions/createswatrope.md)

- [getBirdsEnabled](mta://scripting/client/functions/getbirdsenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22188](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22188):

- [getColorFilter](mta://scripting/client/functions/getcolorfilter.md)

- [getCoronaReflectionsEnabled](mta://scripting/client/functions/getcoronareflectionsenabled.md)

- [getGarageBoundingBox](mta://scripting/client/functions/getgarageboundingbox.md)

- [getGaragePosition](mta://scripting/client/functions/getgarageposition.md)

- [getGarageSize](mta://scripting/client/functions/getgaragesize.md)

- [getGroundPosition](mta://scripting/client/functions/getgroundposition.md)

- [getInteriorFurnitureEnabled](mta://scripting/client/functions/getinteriorfurnitureenabled.md)

- [getNearClipDistance](mta://scripting/client/functions/getnearclipdistance.md)

- [getPedsLODDistance](mta://scripting/client/functions/getpedsloddistance.md)

- [getRoofPosition](mta://scripting/client/functions/getroofposition.md)

- getScreenFromWorldPosition

- [getVehiclesLODDistance](mta://scripting/client/functions/getvehiclesloddistance.md)

- [getWorldFromScreenPosition](mta://scripting/client/functions/getworldfromscreenposition.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22592](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22592):

- [getWorldProperty](mta://scripting/client/functions/getworldproperty.md)

- [isAmbientSoundEnabled](mta://scripting/client/functions/isambientsoundenabled.md)

- [isLineOfSightClear](mta://scripting/client/functions/islineofsightclear.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22676](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22676):

- [isTimeFrozen](mta://scripting/client/functions/istimefrozen.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22721](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22721):

- [isVolumetricShadowsEnabled](mta://scripting/client/functions/isvolumetricshadowsenabled.md)

- [isWorldSoundEnabled](mta://scripting/client/functions/isworldsoundenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22219](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22219):

- [processLineAgainstMesh](mta://scripting/client/functions/processlineagainstmesh.md)

- [processLineOfSight](mta://scripting/client/functions/processlineofsight.md)

- [resetAmbientSounds](mta://scripting/client/functions/resetambientsounds.md)

- [resetBlurLevel](mta://scripting/client/functions/resetblurlevel.md)

- [resetColorFilter](mta://scripting/client/functions/resetcolorfilter.md)

- [resetCoronaReflectionsEnabled](mta://scripting/client/functions/resetcoronareflectionsenabled.md)

- [resetNearClipDistance](mta://scripting/client/functions/resetnearclipdistance.md)

- [resetPedsLODDistance](mta://scripting/client/functions/resetpedsloddistance.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22676](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22676):

- [resetTimeFrozen](mta://scripting/client/functions/resettimefrozen.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22721](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22721):

- [resetVolumetricShadows](mta://scripting/client/functions/resetvolumetricshadows.md)

- [resetVehiclesLODDistance](mta://scripting/client/functions/resetvehiclesloddistance.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22592](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22592):

- [resetWorldProperty](mta://scripting/client/functions/resetworldproperty.md)

- [resetWorldSounds](mta://scripting/client/functions/resetworldsounds.md)

- [setAmbientSoundEnabled](mta://scripting/client/functions/setambientsoundenabled.md)

- [setBirdsEnabled](mta://scripting/client/functions/setbirdsenabled.md)

- [setColorFilter](mta://scripting/client/functions/setcolorfilter.md)

- [setCoronaReflectionsEnabled](mta://scripting/client/functions/setcoronareflectionsenabled.md)

- [setInteriorFurnitureEnabled](mta://scripting/client/functions/setinteriorfurnitureenabled.md)

- [setNearClipDistance](mta://scripting/client/functions/setnearclipdistance.md)

- [setPedsLODDistance](mta://scripting/client/functions/setpedsloddistance.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22676](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22676):

- [setTimeFrozen](mta://scripting/client/functions/settimefrozen.md)

- [setVehiclesLODDistance](mta://scripting/client/functions/setvehiclesloddistance.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22592](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22592):

- [setWorldProperty](mta://scripting/client/functions/setworldproperty.md)

- [setWorldSoundEnabled](mta://scripting/client/functions/setworldsoundenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21902](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21902):

- [setGrainLevel](mta://scripting/client/functions/setgrainlevel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21902](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21902):

- [setGrainMultiplier](mta://scripting/client/functions/setgrainmultiplier.md)

- [testLineAgainstWater](mta://scripting/client/functions/testlineagainstwater.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22721](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22721):

- [setVolumetricShadowsEnabled](mta://scripting/client/functions/setvolumetricshadowsenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22837](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22837):

- [testSphereAgainstWorld](mta://scripting/client/functions/testsphereagainstworld.md)

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
