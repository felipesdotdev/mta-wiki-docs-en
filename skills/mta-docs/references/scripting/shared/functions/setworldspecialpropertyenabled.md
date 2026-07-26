---
doc_id: "mta-wiki:4348"
title: "SetWorldSpecialPropertyEnabled"
source_title: "SetWorldSpecialPropertyEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/SetWorldSpecialPropertyEnabled"
revision_id: 82581
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0", "Changes_in_1.5.5", "Changes_in_1.5.9"]
---

# SetWorldSpecialPropertyEnabled

ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

Added also as a server-side function. Previously only available as a client-side function. 

Enables or disables a special world property.

| [[{{{image}}}\|link=\|]] | Note: It's recommended to use server-side function with appropriate minclientversion for properties like " underworldwarp ", " burnflippedcars ", " extendedwatercannons ", " flyingcomponents ", " vehicle_engine_autostart " to avoid possible data desynchronization. |
| --- | --- |
|  |  |

## Syntax

```
bool setWorldSpecialPropertyEnabled ( string propname, bool enable )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Counterpart**: *[isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md)*

 
A photo demonstrating *randomfoliage* enabled and disabled.

 
A photo demonstrating *roadsignstext* enabled and disabled.

 
A photo demonstrating *extendedwatercannons* enabled and disabled.

### Required Arguments

- **propname:** the name of the property to set. Possible values are:

- **hovercars** - equivalent of the JBGVNB cheat, and allows cars to drive on water. (default: false)

- **aircars** - equivalent of the RIPAZHA cheat, and allows cars to fly. (default: false)

- **extrabunny** - equivalent of the CJPHONEHOME or JHJOECW cheat, and allows you to bunny hop on bicycles much higher. (default: false)

- **extrajump** - equivalent of the KANGAROO cheat, and allows you to jump on foot much higher. (default: false)

- **randomfoliage** - toggle randomly generated foliage on the GTA:SA map (default: true)

- **snipermoon** - toggle the GTA:SA easter egg, which increases the size of the moon every time you shoot it with a sniper rifle (default: false)

- **extraairresistance** - toggle the vehicle speed limit on cross-country roads (default: true)

- **underworldwarp** - toggle warp of peds and vehicles when fall under map (default: true)

- **vehiclesunglare** - toggle the vehicle sun glare effect (default: false)

- **coronaztest** - disable big sun lensflare effect (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r21919](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21919):

 **watercreatures** - toggle randomly generated underwater creatures (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

 **burnflippedcars** - toggle the vehicle to burn when upside down (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22199](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22199):

 **fireballdestruct** - toggle the aircraft model destruction on explosion ([preview](https://wiki.multitheftauto.com/images/1/1f/FireballDestruct.jpg)) (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

 **roadsignstext** - toggle the drawing of text on road signs. (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22485](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22485):

 **extendedwatercannons** - Increases the default limit of water cannons used at the same time from 3 to 30. (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22596](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22596):

 **tunnelweatherblend** - toggle the weather blending effect when the player is in the tunnel. (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r22815](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22815):

 **ignorefirestate** - Allows aiming when the player is on fire and entering burning vehicles. (default: false)

- ADDED/UPDATED IN VERSION 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909):

 **flyingcomponents** - This property determines whether the detached components such as doors, bumpers, etc., should respawn after a vehicle is recreated (change model or variant) or streamed in. (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r23223](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23223):

 **vehicleburnexplosions** - This property toggles creation of additional explosions ([type 2 - rocket](mta://reference/misc/explosion-types.md)) when plane or helicopter is burning. (default: true)

- ADDED/UPDATED IN VERSION 1.6.0 [r23237](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23237):

 **vehicle_engine_autostart** - This property toggles automatic vehicle engine state behavior. (default: true)  
If you set it to *false* then vehicle engine will not start on driver enter and will not stop on driver exit. To control the engine you need to use [setVehicleEngineState](mta://scripting/shared/functions/setvehicleenginestate.md). Helicopter rotors will spin only if the engine is on (with or without driver inside).  
This flag also affects bikes

- **enable:** whether or not to enable the property.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This code allows you to enable/disable certain property using **true** or **false**.

```
local worldSpecialProperties = {
	["hovercars"] = false,
	["aircars"] = false,
	["extrabunny"] = false,
	["extrajump"] = false,
	["randomfoliage"] = true,
	["snipermoon"] = false,
	["extraairresistance"] = true,
	["underworldwarp"] = true,
	["vehiclesunglare"] = false,
	["coronaztest"] = true,
	["watercreatures"] = true,
	["burnflippedcars"] = true,
	["fireballdestruct"] = true,
	["roadsignstext"] = true,
	["extendedwatercannons"] = true,
	["tunnelweatherblend"] = true,
	["ignorefirestate"] = false,
	["flyingcomponents"] = true,
	["vehicleburnexplosions"] = true,
	["vehicle_engine_autostart"] = true,
}

local function toggleWorldSpecialProperties()
	for propertyName, propertyState in pairs(worldSpecialProperties) do
		setWorldSpecialPropertyEnabled(propertyName, propertyState)
	end
end
addEventHandler("onClientResourceStart", resourceRoot, toggleWorldSpecialProperties)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-3.12286 | Added "underworldwarp" property |
| --- | --- |

| 1.5.9-1.21125 | Added "vehiclesunglare" property |
| --- | --- |

| 1.5.9-9.21313 | Added "coronaztest" property |
| --- | --- |

| 1.6.0-9.21919 | Added "watercreatures" property |
| --- | --- |

| 1.6.0-9.22195 | Added "burnflippedcars" property |
| --- | --- |

| 1.6.0-9.22199 | Added "fireballdestruct" property |
| --- | --- |

| 1.6.0-9.22430 | Added "roadsignstext" property |
| --- | --- |

| 1.6.0-9.22485 | Added "extenedwatercannons" property |
| --- | --- |

| 1.6.0-9.22596 | Added "tunnelweatherblend" property |
| --- | --- |

| 1.6.0-9.22815 | Added "ignorefirestate" property |
| --- | --- |

| 1.6.0-9.22909 | Added "flyingcomponents" property |
| --- | --- |

| 1.6.0-9.23223 | Added "vehicleburnexplosions" property |
| --- | --- |

| 1.6.0-9.23237 | Added "vehicle_engine_autostart" property |
| --- | --- |

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

- setWorldSpecialPropertyEnabled

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [resetWorldProperties](mta://scripting/shared/functions/resetworldproperties.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909):

- [removeGameWorld](mta://scripting/client/functions/removegameworld.md)

- [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md)
