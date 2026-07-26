---
doc_id: "mta-wiki:5851"
title: "Changes in 1.2"
source_title: "Changes in 1.2"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.2"
revision_id: 42210
language: "en"
categories: ["Changelog", "Changes_in_1.2"]
---

# Changes in 1.2

| MTA:SA Releases | Changelog Pages |
| --- | --- |
| 1.0 | 1.0.0 • 1.0.1 • 1.0.2 • 1.0.3 • 1.0.4 |
| 1.1 | 1.1.0 • 1.1.1 |
| 1.2 | 1.2.0 |
| 1.3 | 1.3.0 • 1.3.1 • 1.3.2 • 1.3.3 • 1.3.4 • 1.3.5 |
| 1.4 | 1.4.0 • 1.4.1 |
| 1.5 | 1.5.0 • 1.5.1 • 1.5.2 • 1.5.3 • 1.5.4 • 1.5.5 • 1.5.6 • 1.5.7 • 1.5.8 • 1.5.9 |
| 1.6 | 1.6.0 |
| 1.7 | 1.7.0 |

## Main Additions

- Major bandwidth usage reductions

- Ability to replace ped models

- Ability to replace weapon models

- Threaded database access functions

- Custom weapon stats

- Synced and controllable vehicle variants

- Improved bullet accuracy synchronization

## Client

### New Functions

- Added [createSWATRope](mta://scripting/client/functions/createswatrope.md)

- Added [toJSON](mta://scripting/shared/functions/tojson.md)

- Added [fromJSON](mta://scripting/shared/functions/fromjson.md)

- Added [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- Added [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- Added [getVehicleVariant](mta://scripting/shared/functions/getvehiclevariant.md)

- Added [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- Added [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- Added [isElementLowLOD‎](mta://scripting/shared/functions/iselementlowlod.md)

- Added [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- Added [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

- Added [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

### New Events

- None yet

### Changes

- Major reduction in download when playing

- Ability to replace ped models

- Ability to replace weapon models

- Added anisotropic filtering option

- Added grass toggle option

- Fixed long vehicles controlled by remote clients sometimes shake weirdly

- New client command 'serial' to get ones serial

- Added 'showcol' command to see colshapes if [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md) is set

- New map image in F11

- Added opacity keys to radar map and reduced its memory usage

- Improved bullet accuracy synchronization

## Server

### New Functions

- Added [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- Added [deleteResource](mta://scripting/server/functions/deleteresource.md)

- Added [renameResource](mta://scripting/server/functions/renameresource.md)

- Added [dbExec](mta://scripting/server/functions/dbexec.md)

- Added [dbQuery](mta://scripting/server/functions/dbquery.md)

- Added [dbPoll](mta://scripting/server/functions/dbpoll.md)

- Added [dbConnect](mta://scripting/server/functions/dbconnect.md)

- Added [dbFree](mta://scripting/server/functions/dbfree.md)

- Added [getVehicleVariant](mta://scripting/shared/functions/getvehiclevariant.md)

- Added [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- Added [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- Added [setVehicleVariant](mta://scripting/shared/functions/setvehiclevariant.md)

- Added [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

- Added [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- Added [isElementLowLOD‎](mta://scripting/shared/functions/iselementlowlod.md)

- Added [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- Added [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

- Added [getResourceACLRequests](mta://scripting/server/functions/getresourceaclrequests.md)

- Added [updateResourceACLRequest](mta://scripting/server/functions/updateresourceaclrequest.md)

### New Events

- Added [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- Added [onElementModelChanged](https://wiki.multitheftauto.com/index.php?search=onElementModelChanged)

### Changes

- Major reduction in bandwidth upload usage

- Updated [createResource](mta://scripting/server/functions/createresource.md) and Fixed [copyResource](mta://scripting/server/functions/copyresource.md)

- Added basic backup of some server files

- Added option to log database queries to a file

- Added reconnect option to [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- Synchronized vehicle variants

- Various optimizations and stability improvements

- Added glitch "highcloserangedamage" to enable/disable extreme close range damage to the glitch functions.

- Added 'enablesd' server option for competitive gamemodes

- Various resource optimizations

- Threaded pure sync to reduce lag in busy servers

- Upgraded Raknet and sqlite

## Resources

- Scoreboard updated to use dxscoreboard resource

- Parachute and scoreboard have been optimized

- Added fastrope resource

## Editor

- None yet
