---
doc_id: "mta-wiki:2739"
title: "Gamemode CTVC"
source_title: "Gamemode CTVC"
source_url: "https://wiki.multitheftauto.com/wiki/Gamemode_CTVC"
revision_id: 9176
language: "en"
categories: []
generated_at: "2026-07-26T16:15:05.251419+00:00"
---

# Gamemode CTVC

CTVC (**C**apture **t**he **V**ehicle **C**lassic) is a gamemode similiar to CTF (Capture the Flag), with the difference that you have to steal and capture vehicles instead of flags.

# Game Description

- Try to steal the enemy vehicle and get it to your own base (marker)

- You can only capture when your own team's vehicle is safe at your base

- When the team vehicle is left with no driver or is destroyed, it returns to the base automatically

## Points

- Capture (driver): 7 points

- Destroy your own vehicle when its stolen: 5 points

- Kill an enemy player: 1 point

- Kill yourself: -1 point

- Kill a player of your own team: -1 point

# Map Elements

## Ctv Settings

```
<ctvSettings timeLimit="{int=300}" time="{string=12:00}" description="{string}" author="{string}" weather="{int=0}" />
```

#### Required Attributes

(none)

#### Optional Attributes

- **timelimit:** How long will one round take

- **time:** The time that is set at the start of the map

- **description:** What is this map about

- **author:** Who made this map

- **weather:** The weather that is set at the start of the map

## Teams

```
<team name="{string}" color="{string}">
  // more elements required here (see below)
</team>
```

#### Required Attributes

- **name:** The name of the team (usual values would be Red and Blue)

- **color:** RGB-Color, seperated by comma (e.g. "255,0,0" for red)

#### Optional Attributes

(none)

### Base

```
<base posX="{float}" posY="{float}" posZ="{float}" />
```

#### Required Attributes

- **posX,posY,posZ:** The position of the team's base (where they capture the enemy vehicle)

#### Optional Attributes

(none)

### Spawnarea

```
<spawnarea posX="(float)" posY="(float)" posZ="(float)" sizeX="(int=2)" sizeY="(int=2)" skins="{int,int=0}"
	weapons="{int,int;int,int=''}" radius="{int=2}" shape="{string=circle}" />
```

A spawnarea is a rectangle or circle in which players are spawned randomly. It is defined by one point and two size values or the radius. There can be more than one spawnarea in one team, from which one will be chosen randomly on spawn.

#### Required Attributes

- **posX, posY, posZ:** position

#### Optional Attributes

- **skins:** list of skins of which one is randomly chosen, seperated by comma, range of skins seperated by hyphen (e.g. 10,14,20-24 would be 10,14,20,21,22,23,24)

- **weapons:** weapon1,ammo1;weapon2,ammo2;weapon3,ammo3..

- **shape**

- **"circle": (default)** a circle

- **"rectangle":** a rectangle

- **sizeX, sizeY:** if shape="rectangle", the maximum number that will be added to the X or Y coordinate

- **radius:** if shape="circle", radius of the circle

### Teamvehicle

```
<teamvehicle model="536" posX="2496.6750" posY="-1656.5686" posZ="13.1526"
	rotX="0" rotY="0" rotZ="143.7" plate="FARTVAN" colors="ran,0,0,0" />
```

#### Required Attributes

- **posX,posY,posZ:** The position of the vehicle

- **model:** The model id of the vehicle

#### Optional Attributes

*may be implemented soon*
