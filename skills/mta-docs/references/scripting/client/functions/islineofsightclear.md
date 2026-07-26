---
doc_id: "mta-wiki:2594"
title: "IsLineOfSightClear"
source_title: "IsLineOfSightClear"
source_url: "https://wiki.multitheftauto.com/wiki/IsLineOfSightClear"
revision_id: 66964
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
---

# IsLineOfSightClear

This function checks if there are obstacles between two points of the game world, optionally ignoring certain kinds of elements. Use [processLineOfSight](mta://scripting/client/functions/processlineofsight.md) if you want more information about what the ray hits.

| [[{{{image}}}\|link=\|]] | Note: This function does currently NOT support collisions with the "shootthrough" flag enabled. That means: isLineOfSightClear will never collide with such collisions and this can lead to unreliabilities. The "shootthrough" flag is used by many beach/sand/underwater objects. |
| --- | --- |
|  |  |

## Syntax

```
bool isLineOfSightClear ( float startX, float startY, float startZ, float endX, float endY, float endZ, [ bool checkBuildings = true, bool checkVehicles = true, bool checkPeds = true,
                          bool checkObjects = true, bool checkDummies = true, bool seeThroughStuff = false, bool ignoreSomeObjectsForCamera = false, element ignoredElement = nil ] )
```

### Required Arguments

- **startX:** The first point's world X coordinate.

- **startY:** The first point's world Y coordinate.

- **startZ:** The first point's world Z coordinate.

- **endX:** The second point's world X coordinate.

- **endY:** The second point's world Y coordinate.

- **endZ:** The second point's world Z coordinate.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **checkBuildings:** Allow the line of sight to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkVehicles:** Allow the line of sight to be blocked by [vehicles](https://wiki.multitheftauto.com/index.php?search=vehicles).

- **checkPeds:** Allow the line of sight to be blocked by peds, i.e. [players](https://wiki.multitheftauto.com/index.php?search=players).

- **checkObjects:** Allow the line of sight to be blocked by [objects](https://wiki.multitheftauto.com/index.php?search=objects).

- **checkDummies:** Allow the line of sight to be blocked by GTA's internal dummies.  These are not used in the current MTA version so this argument can be set to *false*.

- **seeThroughStuff:** Allow the line of sight to **pass through** collision materials that have this flag enabled (By default material IDs 52, 55 and 66 which are some fences). This flag originally allows some objects to be walked on but you can shoot throug them.

- **ignoreSomeObjectsForCamera:** Allow the line of sight to **pass through** objects that have (K) property enabled in "object.dat" data file. (i.e. Most dynamic objects like boxes or barrels)

- **ignoredElement:** Allow the line of sight to pass through a certain specified element.

### Returns

Returns *true* if the line between the specified points is clear, *false* if there's an obstacle or if invalid parameters are passed.

## Example

Click to expand [+]
Client

isLineOfSightClear is the economical way to cast a ray in the world. 
This example demonstrates how you can easily implement basic NPC behaviour such as jumping obstacles. A 3D line is drawn connecting the two points in the ray.

```
local t_Data = {}

local function updateNPC ()
    if (not isElement(t_Data.ped) or (getElementHealth(t_Data.ped) == 0)) then
        return toggleNPCFollower ()
    end
    
    local t_PlayerPos = {getElementPosition(localPlayer)}
    local t_PedPos = {getElementPosition(t_Data.ped)}
    
    local intDistance = getDistanceBetweenPoints3D (t_PedPos[1], t_PedPos[2], t_PedPos[3], unpack(t_PlayerPos))
    if (intDistance < 4) then
        setPedControlState (t_Data.ped, 'forwards', false)
        return true
    end
    
    -- Calculate the rotation between ped and player position
    local intPedRot = -math.deg (math.atan2(t_PlayerPos[1] - t_PedPos[1], t_PlayerPos[2] - t_PedPos[2]))
    if intPedRot < 0 then intPedRot = intPedRot + 360 end;
    
    setElementRotation (t_Data.ped, 0, 0, intPedRot, 'default', true)
    -- At this point we know that the ped needs to move it
    setPedControlState (t_Data.ped, 'forwards', true)
    
    local bPathClear = true
    local t_Matrix = getElementMatrix (t_Data.ped)
    
    -- Calculate a position 1m ahead of ped
    local int_RayX = t_Matrix[2][1] + t_Matrix[4][1]
    local int_RayY = t_Matrix[2][2] + t_Matrix[4][2]
    local int_RayZ = t_Matrix[2][3] + t_Matrix[4][3]
    
    -- We cast 10 rays 1m ahead of the ped
    for i = 1, 10 do
        local intSourceX, intSourceY, intSourceZ = t_PedPos[1], t_PedPos[2], t_PedPos[3]
        
        -- The target position height is identical to the center of the ped (1m above ground) 
        -- We lower this value by 0.5m to detect short obstacles
        local intTargetX, intTargetY, intTargetZ = int_RayX, int_RayY, int_RayZ - 0.5 + i*0.2
        
        bPathClear = isLineOfSightClear (intSourceX, intSourceY, intSourceZ, intTargetX, intTargetY, intTargetZ, true, true, false, true)
        dxDrawLine3D (intSourceX, intSourceY, intSourceZ, intTargetX, intTargetY, intTargetZ, bPathClear and tocolor(255,255,255,255) or tocolor(255,0,0,255))
        
        if (not bPathClear) then
            break
        end
    end
    
    if (not bPathClear) then
        setPedControlState (t_Data.ped, 'jump', true)
    else
        setPedControlState (t_Data.ped, 'jump', false)
    end
    
    if (intDistance > 15) then
        setPedControlState (t_Data.ped, 'sprint', true)
    else
        setPedControlState (t_Data.ped, 'sprint', false)
    end
end

function toggleNPCFollower ()
    if (t_Data.ped) then
        if (t_Data.updateNPCTimer) then
            if (isTimer(t_Data.updateNPCTimer)) then
                killTimer (t_Data.updateNPCTimer)
            end
        end
        if (isElement(t_Data.ped)) then
            destroyElement (t_Data.ped)
        end
        t_Data.ped = nil
        return true
    end

    local intX, intY, intZ = getElementPosition (localPlayer)
    local _, _, intRZ = getElementRotation (localPlayer)
    local t_Matrix = getElementMatrix (localPlayer)
    
    -- Calculate a position 4m behind local player
    local intPedX = -4 * t_Matrix[2][1] + t_Matrix[4][1]
    local intPedY = -4 * t_Matrix[2][2] + t_Matrix[4][2]
    local intPedZ = -4 * t_Matrix[2][3] + t_Matrix[4][3]
    
    t_Data.ped = createPed (0, intPedX, intPedY, intPedZ, intRZ)
    t_Data.updateNPCTimer = setTimer (updateNPC, 50, 0)
end
addCommandHandler ('npc', toggleNPCFollower)
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

- isLineOfSightClear

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
