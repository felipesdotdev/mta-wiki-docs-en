---
doc_id: "mta-wiki:6535"
title: "Branches"
source_title: "Branches"
source_url: "https://wiki.multitheftauto.com/wiki/Branches"
revision_id: 79793
language: "en"
categories: ["Needs_Checking", "Development", "Archived"]
generated_at: "2026-07-26T16:11:38.716969+00:00"
---

# Branches

|  | This article needs checking. |
| --- | --- |
| Reason(s): This article is outdated |  |

## Weapon Creation

Weapon creation is a branch for creating weapon elements which can fire bullets and do not require ped/players assigned to them.

| Status | Merged - 1.3.1 |
| --- | --- |
| Branch | Weapon-Creation |
| Branch version | 1.4 |

### Functions

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

### General Notes

Created entities are for all intent and purpose objects so any object function will work on them like attachElements, setElementAlpha and such.

### Media

- [http://youtu.be/LN1nZZnzlms](http://youtu.be/LN1nZZnzlms)

## Custom Animations

Custom Animations is a branch for loading animations from .ifp files

| Status | Abandoned |
| --- | --- |
| Branch | Custom-Animations |
| Branch version | 1.4 |

### Functions

- [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md)

- [engineUnloadIFP](mta://scripting/client/functions/engineunloadifp.md)

### Media

- [http://youtu.be/D9YfVPiJniU](http://youtu.be/D9YfVPiJniU)

### General Notes

See [User:Cazomino05](https://wiki.multitheftauto.com/wiki/User:Cazomino05) for bugs.

## Custom Weapon Stats

Custom Weapon Stats is a branch to allow people to edit one of each weapon "properties" for each skill level
so, for example, an M4 at the Pro level can have 1000 damage and an M4 at a standard level can have 0.

| Status | Merged - 1.3.1 |
| --- | --- |
| Branch | Custom-Weapon-Stats |
| Branch version | 1.4 |

### Functions

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

### Media

- [http://youtu.be/M1dQWpDFq98](http://youtu.be/M1dQWpDFq98)

- [http://youtu.be/xfdEvpcuk7s](http://youtu.be/xfdEvpcuk7s)

- [http://youtu.be/eDU06fZiU9M](http://youtu.be/eDU06fZiU9M)

### General Notes

None.

## Analog Control States

The Analog Control States is a branch that is designed to allow proper setting and management of controls and therefore allows for the setting of controls to be between the range of 0 and 1 rather than true/false

This only works for certain properties such as left/right

| Status | Merged - 1.3.1 |
| --- | --- |
| Branch | Analog-Control-States |
| Branch version | 1.4 |

### Functions

- [setAnalogControlState](mta://scripting/client/functions/setanalogcontrolstate.md)

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

### Media

None.

### General Notes

None.

## Custom-Vehicle-Sirens

Custom Vehicle Sirens allows adding sirens to any individual vehicle in the game for instance to add an undercover sultan.

| Status | Merged - 1.3.1 |
| --- | --- |
| Branch | Custom-Vehicle-Sirens |
| Branch version | 1.4 |

### Functions

- [SetVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- [GetVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- [RemoveVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md)

- [GetVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- [AddVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

### Media

- [http://youtu.be/zjJdLCtKccA](http://youtu.be/zjJdLCtKccA)

- [http://youtu.be/ZJDrVf3qSm0](http://youtu.be/ZJDrVf3qSm0)

- [http://youtu.be/1J0_v85FioA](http://youtu.be/1J0_v85FioA)

- [http://youtu.be/X3zE6hZOx4c](http://youtu.be/X3zE6hZOx4c)

### General Notes

None.

## Custom-Train-Tracks

See the main page for this branch ([Custom Train Tracks](mta://reference/misc/custom-train-tracks.md)) for more information.
This branch makes it possible to make your own train tracks.

| Status | Work in progress |
| --- | --- |
| Branch | feature/custom-train-tracks |
| Branch version | 1.5.3 |

### Functions

- [createTrack](https://wiki.multitheftauto.com/index.php?title=CreateTrack&action=edit&redlink=1)

- [removeDefaultTrack](https://wiki.multitheftauto.com/index.php?title=RemoveDefaultTrack&action=edit&redlink=1)

- [resetDefaultTrack](https://wiki.multitheftauto.com/index.php?title=ResetDefaultTrack&action=edit&redlink=1)

- [setTrackLength](https://wiki.multitheftauto.com/index.php?title=SetTrackLength&action=edit&redlink=1)

- [getTrackLength](https://wiki.multitheftauto.com/index.php?title=GetTrackLength&action=edit&redlink=1)

### Media

- [MTA:SA Custom train tracks #1](https://www.youtube.com/watch?v=S_Q3Gk4jVr0&user=UCbl-5xYsT5KwnrfGdW9LYPQ)

## Awesomium

Possibility to create in-game browser.

| Status | Merged - 1.5 |
| --- | --- |
| Branch | Awesomium |
| Branch version | 1.5 |

### Functions

See [User:Jusonex](https://wiki.multitheftauto.com/wiki/User:Jusonex).

### Media

- [http://youtu.be/9w2qU6mZDh8](http://youtu.be/9w2qU6mZDh8)

- [http://youtu.be/qvqc1ScZSbM](http://youtu.be/qvqc1ScZSbM)

- [http://youtu.be/cyUw1F6uBig](http://youtu.be/cyUw1F6uBig)

### General notes

See [User:Jusonex](https://wiki.multitheftauto.com/wiki/User:Jusonex).
