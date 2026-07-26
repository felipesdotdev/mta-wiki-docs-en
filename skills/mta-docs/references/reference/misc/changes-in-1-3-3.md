---
doc_id: "mta-wiki:7206"
title: "Changes in 1.3.3"
source_title: "Changes in 1.3.3"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.3"
revision_id: 58988
language: "en"
categories: ["Changes_in_1.3"]
---

# Changes in 1.3.3

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

| [[{{{image}}}\|link=\|]] | Note: TODO, still not done -- X86dev 08:11, 3 July 2013 (UTC) |
| --- | --- |
|  |  |

## Main Additions / Changes

- Anti-cheat updates

- Optimized streamer to work better with complex maps

- Smoothed fonts when scaling chat box

- Added option to scale HUD elements correctly for widescreen

- Added option to disable OS and graphic driver 'tweaks', as they can interfere with MTA

- Better compatibility with NVidia Optimus laptops

- Improved server performance

- Updated our Audio Library to the latest version to improve some of our sound functions specifically beat detection and prevent crashes caused by calling getSoundMetaTags

### Client

#### New Functions

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md)

- [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

#### New Events

- [onClientSoundStarted](mta://scripting/client/events/onclientsoundstarted.md)

- [onClientSoundStopped](mta://scripting/client/events/onclientsoundstopped.md)

#### Changes / Bug Fixes

- Optimized streamer to work better with complex maps

- Smoothed fonts when scaling chat box

- Added option to scale HUD elements correctly for widescreen

- This might cause your UI elements to scale incorrectly if they are based on the SA HUD positions this can be fixed with [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

- Added option to disable OS and graphic driver 'tweaks', as they can interfere with MTA

- Better compatibility with NVidia Optimus laptops

- Fixed GUI window remaining when you disconnect while starting local server

- Fixed GUI labels sometimes blocking input

- Fixed a crash on disconnect

- Fixed [setVehicleLandingGearDown](mta://scripting/shared/functions/setvehiclelandinggeardown.md) not working sometimes

- Added reassuring animation during periods of no input response

- Fixed stability errors (random texture swapping/assertions) after alt+tab

- Fixed some texture replace errors

### Server

#### New Functions

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md)

- [getPlayerACInfo](mta://scripting/server/functions/getplayeracinfo.md)

#### New Events

- *None yet*

#### Changes / Bug Fixes

- Fixed incorrect server side vehicle engine state when driver warped in

- Fixed [onPlayerQuit](mta://scripting/server/events/onplayerquit.md) event not being triggered on shutdown

- Fixed serverside [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)()

- Improved server performance

- by caching player weapon range

- by reducing the amount of redundant data sent to the network thread

- Added CSimPedTaskPacket for better hit anim sync

- Fixed an issue with weapon ammo getting out of sync

- Sped up server scripts by optimizing ACL checks

- Fixed some desyncs in unoccupied vehicle sync (engine, derailed, in-water state)

- Fixed Get/SetMatrix rotation order for streamed out objects

- Fixed Linux compile issues

- Fixed crash in ReApplyMoveAnims

- Fixed [setElementPosition](mta://scripting/shared/functions/setelementposition.md) for players vehicle causing freeze for few seconds

- Fixed [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md) sometimes returning 0 while player is aiming on Slot 8

- Fixed [onPlayerDamage](mta://scripting/server/events/onplayerdamage.md) having wrong parameters if source on vehicle

- Fixed [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md) on a sandking (495) crashing the server immediately

- Fixed [onPlayerQuit](mta://scripting/server/events/onplayerquit.md) not calling on shutdown

- Fixed [setJetpackWeaponEnabled](mta://scripting/server/functions/setjetpackweaponenabled.md)() not working disabling jetpack weapons

- Sped up server scripts slightly

- Miscellaneous server optimizations

### Resources

- [**voice**] Fixed voice icon not disappearing for other players after the speaking have been stopped (ccw)

- [**acpanel**] Added acpanel

- [**admin**] Fixed 'Set Team' button

### Editor

- *None yet*

## Extra information

*More detailed information available on [Bug tracker Changelog](http://bugs.multitheftauto.com/changelog_page.php) and Google Code repositories:*

- MTA:SA: from  [r5357](http://code.google.com/p/mtasa-blue/source/list?num=25&start=5359) and [above](http://code.google.com/p/mtasa-blue/source/list)

- Resources: from [r930](http://code.google.com/p/mtasa-resources/source/list?num=25&start=930) and [above](http://code.google.com/p/mtasa-resources/source/list)
