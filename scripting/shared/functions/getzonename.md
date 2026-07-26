---
doc_id: "mta-wiki:2345"
title: "GetZoneName"
source_title: "GetZoneName"
source_url: "https://wiki.multitheftauto.com/wiki/GetZoneName"
revision_id: 75457
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:30.787994+00:00"
---

# GetZoneName

This function allows you to retrieve the zone name of a certain location.

## Syntax

```
string getZoneName ( float x, float y, float z, [bool citiesonly=false] )
```

### Required Arguments

- **x:** The X axis position

- **y:** The Y axis position

- **z:** The Z axis position

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **citiesonly**: An optional argument to choose if you want to return one of the following city names:

- Tierra Robada

- Bone County

- Las Venturas

- San Fierro

- Red County

- Whetstone

- Flint County

- Los Santos

### Returns

Returns the string of the zone name.

 

All GTA SA zones and cities

- **Whetstone**

- Angel Pine

- Flint County *

- Foster Valley

- Mount Chiliad

- Shady Cabin

- Shady Creeks

- **Flint County**

- Back o Beyond

- Beacon Hill

- Easter Bay Chemicals

- The Farm

- Flint Intersection

- Flint Range

- Leafy Hollow

- Los Santos Inlet

- **Los Santos**

- Commerce

- Conference Center

- Downtown Los Santos

- East Beach

- East Los Santos

- El Corona

- Ganton

- Glen Park

- Idlewood

- Jefferson

- Las Colinas

- Little Mexico

- Los Flores

- Los Santos International

- Marina

- Market

- Market Station

- Mulholland

- Mulholland Intersection

- Ocean Docks

- Pershing Square

- Playa del Seville

- Richman

- Rodeo

- Santa Maria Beach

- Temple

- Unity Station

- Verdant Bluffs

- Verona Beach

- Vinewood

- Willowfield

- **San Fierro**

- Avispa Country Club

- Battery Point

- Calton Heights

- Chinatown

- City Hall

- Cranberry Station

- Doherty

- Downtown

- Easter Basin

- Easter Bay Airport

- Easter Tunnel

- Esplanade East

- Esplanade North

- Financial

- Foster Valley

- Gant Bridge

- Garcia

- Garver Bridge

- Hashbury

- Juniper Hill

- Juniper Hollow

- Kincaid Bridge

- King's

- Missionary Hill

- Mount Chiliad

- Ocean Flats

- Palisades

- Paradiso

- Queens

- San Fierro Bay

- Santa Flora

- **Red County**

- Blueberry

- Blueberry Acres

- Dillimore

- Easter Bay Airport

- Easter Bay Chemicals

- Fallen Tree

- Fallow Bridge

- Fern Ridge

- Fisher's Lagoon

- Flint County *

- Flint Water

- Frederick Bridge

- Hampton Barns

- Hankypanky Point

- Hilltop Farm

- Las Venturas *

- Martin Bridge

- Montgomery

- Montgomery Intersection

- Mulholland

- North Rock

- Palomino Creek

- Richman

- San Andreas Sound

- San Fierro *

- The Mako Span

- The Panopticon

- **Tierra Robada**

- Aldea Malvada

- Arco del Oeste

- Bayside

- Bayside Marina

- Bayside Tunnel

- Bone County *

- El Quebrados

- Gant Bridge

- Garver Bridge

- Kincaid Bridge

- Las Barrancas

- Robada Intersection

- San Fierro Bay

- Sherman Reservoir

- The Sherman Dam

- Valle Ocultado

- **Bone County**

- 'The Big Ear'

- El Castillo del Diablo

- Fort Carson

- Green Palms

- Hunter Quarry

- Las Brujas

- Las Payasadas

- Lil' Probe Inn

- Octane Springs

- Regular Tom

- Restricted Area

- Verdant Meadows

- **Las Venturas**

- Blackfield

- Blackfield Chapel

- Blackfield Intersection

- Caligula's Palace

- Come-A-Lot

- Creek

- Greenglass College

- Harry Gold Parkway

- Julius Thruway East

- Julius Thruway North

- Julius Thruway South

- Julius Thruway West

- K.A.C.C. Military Fuels

- Las Venturas Airport

- Last Dime Motel

- Linden Side

- Linden Station

- LVA Freight Depot

- Old Venturas Strip

- Pilgrim

- Pilson Intersection

- Pirates in Men's Pants

- Prickle Pine

- Randolph Industrial Estate

- Redsands East

- Redsands West

- Roca Escalante

- Rockshore East

- Rockshore West

- Royal Casino

- Sobell Rail Yards

- Spinybed

- Starfish Casino

- The Camel's Toe

- The Clown's Pocket

- The Emerald Isle

- The Four Dragons Casino

- The High Roller

- The Pink Swan

- The Strip

- The Visage

- Whitewood Estates

- Yellow Bell Golf Course

- Yellow Bell Station

***** Not real zone, but it still can be found using getZoneName

## Example

Click to collapse [-]
Server

**Example 1:** This example returns the player's City & Zone.

```
function outputPlayerZone(thePlayer)
    -- get the player position
    x, y, z = getElementPosition(thePlayer)
    -- get the player zone
    zone = getZoneName(x, y, z)
    -- get the player city (citiesonly as true)
    city = getZoneName(x, y, z, true)
    -- output to local player's chatbox
    outputChatBox("City: ".. city .." / Zone: ".. zone, thePlayer)
end
addCommandHandler("getloc", outputPlayerZone)
```

**Example 2:** This example will tell you what zone a specified player is in when the "getloc" console command is used.

```
function scriptGetLoc ( source, command, playername ) --when getloc is called
  local thePlayer = getPlayerFromName ( playername ) --get the player from nickname
  if ( thePlayer ~= false ) then --if there is a player from the nickname
    local x, y, z = getElementPosition ( thePlayer )
    local location = getZoneName ( x, y, z )
	local city = getZoneName ( x, y, z, true )
    outputChatBox ( playername .. " is at " .. location .. " (" .. city .. ")", source ) --announce his zone
  else outputChatBox ( "Player does not exist" )
  end
end
addCommandHandler( "getloc", scriptGetLoc ) -- add a command "getloc" which initiates "scriptGetloc" function
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

- getZoneName

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
