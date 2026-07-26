---
doc_id: "mta-wiki:4234"
title: "SetGarageOpen"
source_title: "SetGarageOpen"
source_url: "https://wiki.multitheftauto.com/wiki/SetGarageOpen"
revision_id: 79947
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:40.788748+00:00"
---

# SetGarageOpen

This function opens or closes the specified garage door in the world.

| [[{{{image}}}\|link=\|]] | Note: setGarageOpen does not work with ID 32 (Pay 'n' Spray near Royal Casino). This garage has been disabled by Rockstar Games due to floor collision issues (see TheJizzy's video "BETA Leftovers and Glitches" at 12:12 timestamp). You can remove the door by using removeWorldModel and recreating it for later with moveObject . |
| --- | --- |
|  |  |

## Syntax

```
bool setGarageOpen ( int garageID, bool open )
```

### Required Arguments

- **garageID:** The [garage ID](mta://reference/misc/garage.md) that represents the garage door being opened or closed.

- **isOpen:** A boolean indicating whether or not to open the door.

### Returns

Returns *true* if successful, *false* if an invalid garage id was given.

## Example

Click to collapse [-]
Server

This example opens a garage door when a player enters a collision shape near it, and closes it when they leave:

```
local GARAGE_ID = 25

-- create a collision shape and attach event handlers to it when the resource starts
addEventHandler("onResourceStart", resourceRoot, function (resource)
	local garageCube = createColCuboid(1337, 194, 28, 6, 10, 4)
	addEventHandler("onColShapeHit", garageCube, onGarageCubeHit)
	addEventHandler("onColShapeLeave", garageCube, onGarageCubeLeave)
end)

-- open the door when someone enters the garage's collision shape
function onGarageCubeHit(hitElement, matchingDimension)
	if getElementType(hitElement) ~= "player" then
		return
	end
	-- check to make sure the door is closed
	-- open if they are closed
	setGarageOpen(GARAGE_ID, not isGarageOpen(GARAGE_ID))
end

-- close the door when someone leaves the garage's collision shape
function onGarageCubeLeave(leaveElement, matchingDimension)
	if getElementType(leaveElement) ~= "player" then
		return
	end
	-- check to make sure the door is open
	-- close if they are opened
	setGarageOpen(GARAGE_ID, not isGarageOpen(GARAGE_ID))
end
```

Click to collapse [-]
Server

This example opens each garage door when a player enters a collision shape near it, and closes it when they leave:

```
local garages = {
	{ 1643.43, -1520.3, 14.3438, },
	{ 1877.41, -2096.51, 14.0391, },
    { 1843.37, -1856.32, 13.875, },
    { 1798.69, -2146.73, 14, },
    { 1698.91, -2088.74, 14.1406, },
    { 2741.07, -2004.78, 14.875, },
    { 2644.86, -2039.23, 14.0391, },
    { 2071.48, -1831.42, 14.5625, },
    { 2505.52, -1690.99, 14.3281, },
    { 1041.35, -1025.93, 32.6719, },
    { 1024.98, -1029.35, 33.1953, },
    { 488.28, -1734.7, 12.3906, },
    { 322.4141, -1769.0312, 5.25, },
    { 1353.48, -626.63, 109.82, },
    { -2716.35, 217.48, 5.3828, },
    { -2730.47, 72.32, 5.3516, },
    { -2454.12, -123.06, 26.9844, },
    { -1935.86, 239.53, 35.3516, },
    { -1904.53, 277.9, 42.9531, },
    { -2102.93, -16.05, 36.4844, },
    { -2026.91, 129.41, 30.4531, },
    { -2038.93, 178.81, 29.9375, },
    { -2162.03, 654.66, 53.375, },
    { -1786.81, 1209.42, 25.8359, },
    { -2105.2, 896.93, 77.4453, },
    { -2425.73, 1027.99, 52.2812, },
    { -2696.01, 821.45, 50.8516, },
    { 1586.26, 1222.7, 19.75, },
    { 2609.52, 1438.37, 11.5938, },
    { 2386.66, 1043.6, 11.5938, },
    { 2449.55, 698.08, 11.6797, },
    { 1968.74, 2162.49, 12.0938, },
    { 1408.64, 1902.69, 11.6797, },
    { 1278.7, 2529.81, 11.3203, },
    { 929.55, 2012.06, 11.6797, },
    { -1420.55, 2591.16, 57.7422, },
    { -100, 1111.41, 21.6406, },
    { -360.77, 1194.26, 20.5938, },
    { 429.98, 2546.52, 17.3516, },
    { -389.59, 2227.91, 42.9219, },
    { 397.48, 2476.63, 19.5156, },
    { 412.12, 2476.63, 19.5156, },
    { -2113.04, -2460.62, 30.9141, },
    { 720.02, -462.52, 16.8594, },
    { 2231.24, 168.73, 27.7734, },
    { 786.01, -492.87, 17.632, },
}

local function createGarageColShape(x, y, z, ID)
    local col = createColSphere(x, y, z, 7)
    
    addEventHandler("onColShapeHit", col, function(hitElement, matchingDimension)
        if getElementType(hitElement) ~= "player" then
            return
        end
        setGarageOpen(ID, not isGarageOpen(ID))
    end)
    
    addEventHandler("onColShapeLeave", col, function(leaveElement, matchingDimension)
        if getElementType(hitElement) ~= "player" then
            return
        end
        setGarageOpen(ID, not isGarageOpen(ID))
    end)
end

addEventHandler("onResourceStart", resourceRoot, function(res)
    for ID, pos in ipairs(garages) do
        createGarageColShape(pos[1], pos[2], pos[3], ID)
    end
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

- setGarageOpen

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
