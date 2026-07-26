---
doc_id: "mta-wiki:2501"
title: "ProcessLineOfSight"
source_title: "ProcessLineOfSight"
source_url: "https://wiki.multitheftauto.com/wiki/ProcessLineOfSight"
revision_id: 79555
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:30.335700+00:00"
---

# ProcessLineOfSight

This function casts a ray between two points in the world, and tells you information about the point that was hit, if any. The two positions **must** be within the local player's draw distance as the collision data is not loaded outside this area, and the call will just fail as if the ray didn't hit.

This function is relatively expensive to call, so over use of this in scripts may have a detrimental effect on performance.

This function is useful for checking for collisions and for editor-style scripts. If you wish to find what element is positioned at a particular point on the screen, use this function combined with [getWorldFromScreenPosition](mta://scripting/client/functions/getworldfromscreenposition.md). If you wish to just know if something is hit, and don't care about what or where was hit, use [isLineOfSightClear](mta://scripting/client/functions/islineofsightclear.md).

| [[{{{image}}}\|link=\|]] | Note: Due to a bug, shootThroughStuff argument does currently check for seeThroughStuff! |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Due to a bug, seeThroughStuff argument has no effect. It mistakenly checks for "shootThrough" surfaces and will always behave as if the argument is set to FALSE (It will never hit). |
| --- | --- |
|  |  |

## Syntax

Return values labelled for ease of reference.

```
bool               -- hit
float float float  -- hitX, hitY, hitZ
element            -- hitElement
float float float  -- normalX, normalY, normalZ
int                -- material
float              -- lighting
int                -- piece
int                -- worldModelID
float float float  -- worldModelPositionX,Y,Z
float float float  -- worldModelRotationX,Y,Z
int                -- worldLODModelID
float float        -- uvX, uvY
string             -- textureName,
string             -- frameName,
float float float  -- modelHitX, modelHitY, modelHitZ
                  processLineOfSight ( float startX, float startY, float startZ, 
                                       float endX, float endY, float endZ, 
                                       [ bool checkBuildings = true, 
                                       bool checkVehicles = true, 
                                       bool checkPlayers = true, 
                                       bool checkObjects = true, 
                                       bool checkDummies = true, 
                                       bool seeThroughStuff = false, 
                                       bool ignoreSomeObjectsForCamera = false, 
                                       bool shootThroughStuff = false, 
                                       element ignoredElement = nil,
                                       bool includeWorldModelInformation = false,
                                       bool bIncludeCarTyres = false,
                                       bool bIncludeExtraMateriaInfo = false ] )
```

### Required Arguments

- **startX:** The start *x* position

- **startY:** The start *y* position

- **startZ:** The start *z* position

- **endX:** The end *x* position

- **endY:** The end *y* position

- **endZ:** The end *z* position

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **checkBuildings:** Allow the line of sight to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkVehicles:** Allow the line of sight to be blocked by [vehicles](mta://reference/misc/vehicle.md).

- **checkPlayers:** Allow the line of sight to be blocked by [players](mta://reference/misc/player.md).

- **checkObjects:** Allow the line of sight to be blocked by [objects](mta://reference/misc/object.md).

- **checkDummies:** Allow the line of sight to be blocked by GTA's internal dummies.  These are not used in the current MTA version so this argument can be set to *false*.

- **seeThroughStuff:** Allow the line of sight **pass through** collision materials that have this flag enabled (By default material IDs 52, 55 and 66 which are some fences that you can shoot throug but still walk on them).

- **ignoreSomeObjectsForCamera:** Allow the line of sight to **pass through** objects that have (K) property enabled in "object.dat" data file. (i.e. Most dynamic objects like boxes or barrels)

- **shootThroughStuff:** Allow the line of sight to **pass through** collision materials that have this flag enabled (By default material IDs 28, 29, 31, 32, 33, 74, 75, 76, 77, 78, 79, 96, 97, 98, 99, 100 which are exclusively sand / beach or underwater objects).

- **ignoredElement:** Allow the line of sight to **pass through** a certain specified element. This is usually set to the object you are tracing from so it does not interfere with the results.

- **includeWorldModelInformation :** Include the results of hitting a world model.

- **bIncludeCarTyres :** Includes car tyre hits.

ADDED/UPDATED IN VERSION 1.6.0 [r22173](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22173):

- **bIncludeExtraMateriaInfo:** Include the material info like UV coords, textureName, frameName and exact position hit on the model.

### Returns

- **hit:** *true* if there is a collision, *false* otherwise

The other values are only filled if there is a collision, they contain *nil* otherwise

- **hitX, hitY, hitZ:** collision position

- **hitElement:** the MTA element hit if any, *nil* otherwise

- **normalX, normalY, normalZ:** the normal of the surface hit

- **material:** an integer representing the [GTASA material ID](mta://reference/misc/material-ids.md) of the surface hit when applicable (world, objects)

- **lighting:** a float between 0 (fully dark) and 1 (bright) representing the amount of light that the hit building surface will transfer to peds or vehicles that are in contact with it. The value can be affected by the game time of day, usually with a lower (darker) value being returned during the night.

- **piece:** an integer representing the part of the element hit if hitElement is a vehicle or a ped/player, *0* otherwise.

- For a ped/player, piece represents the body part hit:

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- For vehicles, piece represents the vehicle part hit:

- **0:** Frame

- **2:** Trunk

- **3:** Hood

- **4:** Rear

- **5:** Front left door

- **6:** Front right door

- **7:** Rear left door

- **8:** Rear right door

- **13:** Front Left tyre

- **14:** Front Right tyre

- **15:** Back Left tyre

- **16:** Back Right tyre

(Other potential IDs haven't been documented yet and might depend on vehicle model)

- **worldModelID:** If includeWorldModelInformation was set to *true* and a world model was hit, this will contain the model ID.

- **worldModelPositionX,Y,Z:** If worldModelID is set, this will contain the world model position.

- **worldModelRotationX,Y,Z:** If worldModelID is set, this will contain the world model rotation.

- **worldLODModelID:** If worldModelID is set, this will contain the LOD model ID if applicable.

- **uvX, uvY:** If bIncludeExtraMateriaInfo is set, it contains the texture UV positions of the hit triangle of the hit entity.

- **textureName:** Same as above, but contains the texture name.

- **frameName:** Same as above, but contains the frame name. (This, for example in case of cars this is (but not limited to) a [Vehicle Components](mta://reference/misc/vehicle-components.md))

- **modelHitX, modelHitY, modelHitZ:** Same as above, but contains the exact position hit on the model itself (It is much more precise than the `hitX, hitY, hitZ` returned above, as those are only processed against the much more simpler collision mesh, while these are obtained from processing the visual mesh itself (the DFF))

## Examples

This example shows how you can tell what position and element the camera is looking at, up to 50 units away.

```
local w, h = guiGetScreenSize ()
local tx, ty, tz = getWorldFromScreenPosition ( w/2, h/2, 50 )
local px, py, pz = getCameraMatrix()
hit, x, y, z, elementHit = processLineOfSight ( px, py, pz, tx, ty, tz )
if hit then
    outputChatBox ( "Looking at " .. x .. ", " .. y .. ", " ..  z )
    if elementHit then
        outputChatBox ( "Hit element " .. getElementType(elementHit) )
    end
end
```

This example shows how you can get the surface type a vehicle is on. This is useful if you want to do a script to dirt cars over time. Please note that this function doesn't count if the vehicle is streamed in or not, so expect this function to fail or return incorrect values on unloaded vehicles.

```
function getSurfaceVehicleIsOn(vehicle)
    if isElement(vehicle) and (isVehicleOnGround(vehicle) or isElementInWater(vehicle)) then -- Is an element and is touching any surface?
        local cx, cy, cz = getElementPosition(vehicle) -- Get the position of the vehicle
        local gz = getGroundPosition(cx, cy, cz) - 0.001 -- Get the Z position of the ground the vehicle is on (-0.001 because of processLineOfSight)
        local hit, _, _, _, _, _, _, _, surface = processLineOfSight(cx, cy, cz, cx, cy, gz) -- This will get the material of the thing the car is standing on
        if hit then
            return surface -- If everything is correct, stop executing this function and return the surface type
        end
    end
    return false -- If something isn't correct, return false
end
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04273 | bIncludeCarTyres argument added |
| --- | --- |

| 1.3.0-9.04273 | worldModelID return value fixed |
| --- | --- |

| 1.3.0-9.04405 | lighting return value fixed |
| --- | --- |

| 1.6.0-9.22173 | bIncludeExtraMateriaInfo argument added |
| --- | --- |

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

- [processLineAgainstMesh](mta://scripting/client/functions/processlineagainstmesh.md)

- processLineOfSight

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
