---
doc_id: "mta-wiki:14271"
title: "CreateBuilding"
source_title: "CreateBuilding"
source_url: "https://wiki.multitheftauto.com/wiki/CreateBuilding"
revision_id: 82376
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0", "Utility_templates"]
---

# CreateBuilding

ADDED/UPDATED IN VERSION 1.6.0 [r22410](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22410):

Creates a [building](https://wiki.multitheftauto.com/index.php?search=building) [element](mta://reference/misc/element.md) at a given position & interior with a certain rotation. 

| [[{{{image}}}\|link=\|]] | Note: Some objects / buildings in interior 13 show in all interiors. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Unlike createObject , this function does not have an isLowLOD argument. When using setLowLODElement , the system will automatically define the building as a LOD. |
| --- | --- |
|  |  |

## Important info about [Buildings](https://wiki.multitheftauto.com/index.php?search=Buildings)

- There is a distinction in GTA: San Andreas between static and dynamic models (these use a separate streaming system). Examples of buildings include building models, roads, and terrain. Objects created as [Buildings](https://wiki.multitheftauto.com/index.php?search=Buildings) can contain **glass** and **shadows**, unlike those created as [Objects](https://wiki.multitheftauto.com/index.php?search=Objects) (which are missing these features).

- Buildings can be created with dynamic object model IDs, but they won't have any physical interaction. For example, [object ID 1502 (Gen_doorINT04)](https://dev.prineside.com/en/gtasa_samp_model_id/model/1502-Gen_doorINT04/) is a door that can only be opened if created with [createObject](mta://scripting/shared/functions/createobject.md).

- Using buildings for mapping is more optimized than using objects. Gains in FPS can be noticed in areas where a lot of objects were replaced with buildings of this new system.

- Buildings can only be created inside regular GTA:SA Map Boundaries (X between -3000 and 3000; Y between -3000 and 3000). Use [createObject](mta://scripting/shared/functions/createobject.md) to spawn objects outside these normal limits. **This limitation is probably going to stop existing in the near future.**

- Created buildings can have **LOD models**. The procedure is as follows: spawn the LOD building using createBuilding, then use [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md) to associate it with the non-LOD building element you created beforehand. LOD model distance changed with [engineSetModelLODDistance](mta://scripting/client/functions/enginesetmodelloddistance.md) works for buildings.

- Buildings cannot appear in certain a [dimension](mta://reference/misc/dimension.md), and not show in others. Function [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) returns false on any building. A building is created in a specific [interior world](mta://reference/misc/interior.md) (such as 0, the main world), like the default GTA:SA landscape objects. All **buildings appear in EVERY DIMENSION**.

## Syntax

```
building createBuilding ( int modelId, float x, float y, float z [, float rx, float ry, float rz, int interior = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Building](https://wiki.multitheftauto.com/index.php?search=Building)(...)*

### Required Arguments

- **modelId:** A whole integer specifying the GTA:SA object model ID. See [Object IDs](mta://reference/misc/object-ids.md) for a list of model IDs.

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rx:** A floating point number representing the rotation about the X axis in degrees.

- **ry:** A floating point number representing the rotation about the Y axis in degrees.

- **rz:** A floating point number representing the rotation about the Z axis in degrees.

- **interior:** The interior you want to set the building to. Valid values are 0 to 255.

### Returns

- Returns the [building](https://wiki.multitheftauto.com/index.php?search=building) element if the creation was successful, throws an error otherwise.

## Example

Click to collapse [-]
How to automatically perform object/building creation

This example shows you how to automatically create an object or building element according to certain parameters.

**This script onlys works CLIENTSIDE due to createBuilding and [engineGetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginegetmodelphysicalpropertiesgroup.md).**

```
-- Creates an 'object' or 'building' element based on certain parameters or one of the functions fails
-- This function will throw an error when unexpected arguments are used
-- TODO: Add LOD support
function createObjectOrBuilding(modelID, x, y, z, rx, ry, rz, interior, dimension)
    -- Validate the arguments passed
    assert(type(modelID)=="number", "invalid modelID passed: " .. tostring(modelID))
    assert(type(x)=="number" and type(y)== "number" and type(z)=="number", "invalid position passed: " .. tostring(x) .. ", " .. tostring(y) .. ", " .. tostring(z))
    if not rx then rx = 0 end
    if not ry then ry = 0 end
    if not rz then rz = 0 end
    assert(type(rx)=="number" and type(ry)== "number" and type(rz)=="number", "invalid rotation passed: " .. tostring(rx) .. ", " .. tostring(ry) .. ", " .. tostring(rz))
    if not interior then interior = 0 end
    if not dimension then dimension = 0 end
    assert(type(interior)=="number" and interior >= 0 and interior <= 255, "invalid interior (must be 0-255) passed: " .. tostring(interior))
    assert(type(dimension)=="number" and dimension >= -1 and dimension <= 65535, "invalid dimension passed (must be -1 65535): " .. tostring(dimension))

    -- Dynamic object models will always have a physical properties group different than -1.
    local isNonDynamic = engineGetModelPhysicalPropertiesGroup(modelID) == -1
    -- Buildings can't be affected by dimension
    local isNormalDimension = dimension == 0
    -- Buildings can't be placed outside regular map boundaries
    local isInsideMapLimits = x >= -3000 and x <= 3000 and y >= -3000 and y <= 3000

    local obj, bld
    if isNonDynamic and isNormalDimension and isInsideMapLimits then
        bld = createBuilding(modelID, x, y, z, rx, ry, rz, interior)
        assert(bld, ("Failed to create building with model ID %d at %f, %f, %f in interior %d"):format(modelID, x, y, z, interior))
    else
        obj = createObject(modelID, x, y, z, rx, ry, rz, false)
        assert(obj, ("Failed to create object with model ID %d at %f, %f, %f"):format(modelID, x, y, z))
        setElementInterior(obj, interior)
        setElementDimension(obj, dimension)
    end
    return obj or bld
end

-- Test this create object/building function
addCommandHandler("testobject", function()
    -- This would be your object's model ID
    local modelID = 3556
    -- This would be your object's position coordinates
    local x, y, z = 0, 0, 69
    -- This would be your object's rotation coordinates
    local rx, ry, rz = 0, 0, 90
    -- This would be your object's interior ID
    local interior = 0
    -- This would be your object's dimension ID
    local dimension = 0

    -- We use pcall to catch any errors that may be thrown
    local success, element = pcall(createObjectOrBuilding, modelID, x, y, z, rx, ry, rz, interior, dimension)
    if not success then
        outputDebugString(("Failed to create object or building: %s"):format(tostring(element)), 4, 255, 25, 25)
        return
    end

    -- OPTIONAL: Then you can apply additional properties, like so:
    if getElementType(element) == "object" then
        setObjectScale(element, 1.69)
        setObjectBreakable(element, false)
        setElementAlpha(element, 230)
    end
    setElementCollisionsEnabled(element, true)
    setElementFrozen(element, false)
end)
```

Click to collapse [-]
Simple example

This example creates a building when the resource starts:

```
function loadMap()
   -- create a *building* at a specified position with a specified rotation
   createBuilding(4550, 1985, -2544, 94, 0,0,0) -- Maze Bank Tower in LS airport
end
addEventHandler("onClientResourceStart", resourceRoot, loadMap, false)
```

## See Also

### Building functions

ADDED/UPDATED IN VERSION 1.6.0 [r22410](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22410):

- createBuilding

### Object functions

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

### Client world functions

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
