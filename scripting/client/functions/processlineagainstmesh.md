---
doc_id: "mta-wiki:14141"
title: "ProcessLineAgainstMesh"
source_title: "ProcessLineAgainstMesh"
source_url: "https://wiki.multitheftauto.com/wiki/ProcessLineAgainstMesh"
revision_id: 82805
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:30.257736+00:00"
---

# ProcessLineAgainstMesh

ADDED/UPDATED IN VERSION 1.6.0 [r22219](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22219):

Does a raycast against an element's renderable mesh model directly 

Does a raycast against an element's renderable mesh model [not the collision model!].
The same functionality is already present in [processLineOfSight](mta://scripting/client/functions/processlineofsight.md), but the latter is a little buggy due to the fact that the collision model is always simplified, and not exactly the same as the mesh, which leads to situations where no hit is detected, even though the visible mesh is hittable [or vice versa].
Also, when one is interested in a specific element the overhead is a lot smaller [as we can skip all the collision detection done by the before-mentioned function].

## Syntax

Single line for convenience.

```
bool, float, float, string, string, float, float, float processLineAgainstMesh(element toTest, float startX, float startY, float startZ, float endX, float endY, float endZ)
```

Return values labelled for ease of reference.

```
bool               -- hit 
float float        -- texU, texV
string             -- textureName
string             -- frameName
float float float  -- worldX, worldY, worldZ
                  processLineAgainstMesh(element toTest, 
                                         float startX, float startY, float startZ, 
                                         float endX, float endY, float endZ)
```

### Required Arguments

- **toProcess:** The element to process the line against

- **startX, startY, startZ:** The start [origin] of the line

- **endX, endY, endZ:** The end of the line

### Returns

- **hit:** *true* if there is a collision with the given element's mesh, *false* otherwise [in which case all other values are nil]

- **texU, texV:** the U, V coordinates on the hit geometry's texture

- **textureName:** name of the hit geometry's texture

- **frameName:** hit frame's name

- **worldX, worldY, worldZ:** collision position in world space

## Example

This example prints the name of the texture hit by the player's crosshair on any vehicle in the world. It uses processLineAgainstMesh to check for collisions between a line from the camera to a point in front of it and the meshes of vehicles.

```
addEventHandler("onClientRender", root,
    function()
        local camX, camY, camZ, targetX, targetY, targetZ = getCameraMatrix()
        local dirX = targetX - camX
        local dirY = targetY - camY
        local dirZ = targetZ - camZ

        local endX = camX + dirX * 100
        local endY = camY + dirY * 100
        local endZ = camZ + dirZ * 100

        for _, vehicle in ipairs(getElementsByType("vehicle")) do
            local hit, _, _, textureName = processLineAgainstMesh(
                vehicle,
                camX, camY, camZ,
                endX, endY, endZ
            )

            if hit and textureName then
                print("Hit texture: " .. textureName)
                break
            end
        end
    end
)
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

- [getScreenFromWorldPosition](mta://scripting/client/functions/getscreenfromworldposition.md)

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

- processLineAgainstMesh

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
