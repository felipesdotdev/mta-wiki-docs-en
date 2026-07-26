---
doc_id: "mta-wiki:7276"
title: "Changes in 1.3.5"
source_title: "Changes in 1.3.5"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.5"
revision_id: 58990
language: "en"
categories: ["Changes_in_1.3"]
---

# Changes in 1.3.5

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

## Main Additions / Changes

- Huge code cleaups / optimizations

- Improved performance browser

- Improved mathematical precision for client and syncing

- Bullet sync for sniper rifle

## Scripting

### Scripting: New functions

#### Client

- Added [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- Added [guiEditGetCaretIndex](mta://scripting/client/functions/guieditgetcaretindex.md)

- Added [guiMemoGetCaretIndex](mta://scripting/client/functions/guimemogetcaretindex.md)

- Added [getCamera](mta://scripting/client/functions/getcamera.md)

- Added [setInteriorFurnitureEnabled](mta://scripting/client/functions/setinteriorfurnitureenabled.md)

- Added [getInteriorFurnitureEnabled](mta://scripting/client/functions/getinteriorfurnitureenabled.md)

#### Server

- None yet

#### Shared (*Client & Server side*)

- Added [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- Added [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- Added [base64Encode](mta://scripting/shared/functions/base64encode.md)

- Added [base64Decode](mta://scripting/shared/functions/base64decode.md)

- Added [teaEncode](mta://scripting/shared/functions/teaencode.md)

- Added [teaDecode](mta://scripting/shared/functions/teadecode.md)

- Added [pregFind](https://wiki.multitheftauto.com/index.php?search=pregFind)

- Added [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- Added [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- Added [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- Added [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

### Scripting: New Events

#### Client

- Added [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

#### Server

- None yet

### Scripting: Changes, Bugfixes and Additions

- Added option to specify timeout length for [callRemote](mta://scripting/server/functions/callremote.md) and [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- Added error message parameter to [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md) in case of failure

- Added rotation parameter for [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)

- Added flags (1 ignorecase; 2 multiline; 4 dotall; 8 extented) to preg functions

- Added character option to preg option flags

- Added easier way to set weapon flags

- Added warning message for server scripts that might be causing a long freeze

- Fixed some weapon flags

- Fixed [isPedOnFire](mta://scripting/shared/functions/ispedonfire.md) not working correctly

- Fixed [onPlayerVoiceStart](mta://scripting/server/events/onplayervoicestart.md) re-triggering when cancelled

- Fixed double [dbPoll](mta://scripting/server/functions/dbpoll.md) freeze

- Fixed [setPedAimTarget](mta://scripting/client/functions/setpedaimtarget.md) returning true for local player

- Fixed [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md) sometimes returning a blank screen

- Fixed event handler *sourceResource* global variable

- Fixed [dxGetPixelsFormat](mta://scripting/client/functions/dxgetpixelsformat.md) not recognising some jpeg files

- Fixed [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md) not closing the file after creating font

- Fixed [onPedWasted](mta://scripting/server/events/onpedwasted.md) / [onClientPedWasted](mta://scripting/client/events/onclientpedwasted.md) always returning 63 (blown) as weapon

- Fixed [setPedStat](mta://scripting/shared/functions/setpedstat.md) being sometimes not synced to client

- Fixed [onClientSoundStopped](mta://scripting/client/events/onclientsoundstopped.md) sometimes being late

- Fixed [attachElements](mta://scripting/shared/functions/attachelements.md) with the camera not removing the camera target

- Fixed inability to bind num_enter key

- Fixed an inconsistence - Details: [r5852](https://code.google.com/p/mtasa-blue/source/detail?r=5852)

- Fixed Backspace key not working in NoCurses mode

- Fixed explosions created with [createExplosion](mta://scripting/shared/functions/createexplosion.md) passing through servers

- Fixed [isElementInWater](mta://scripting/shared/functions/iselementinwater.md) returning false with peds

- Fixed [guiScrollPaneSetHorizontalScrollPosition](mta://scripting/client/functions/guiscrollpanesethorizontalscrollposition.md) and [guiScrollPaneSetVerticalScrollPosition](mta://scripting/client/functions/guiscrollpanesetverticalscrollposition.md) not correctly using floating point numbers

- Disabled [destroyElement](mta://scripting/shared/functions/destroyelement.md) and [setElementParent](mta://scripting/shared/functions/setelementparent.md) for the camera element

- Updated Lua to 5.1.5-2

## Client

### Client: Additions

- Added online help option for timed out error codes

- Added more on-line help for in-game error messages

- Added virus help messages to the loader

- Added helpful messages for some crash types

- Added upgrade message to uninstaller

- Added disk space checks

### Client: Bugfixes & Changes

- Fixed an issue when client runs with reduced mathematical precision compared to the server

- Fixed problem with network floaters

- Fixed escape key issue

- Fixed ped Z position being sometimes out of sync

- Fixed timeout problem with some gta_sa.exe's

- Fixed exploding vehicle causing issue with player death

- Fixed some GUI crashes

- Fixed client Lua crash

- Fixed launch crash

- Fixed crash caused by a custom model restoring conflict somewhere

- Fixed a bug when throwing grenade could cause crash

- Fixed [onClientElementStreamOut](mta://scripting/client/events/onclientelementstreamout.md) crash

- Fixed graphics driver crash bug

- Fixed another graphics driver crash bug

- Fixed crash in loader

- Fixed crash caused by element attachment problem somewhere

- Fixed GUI skin change crash

- Fixed depth buffer access (while antialiasing on) messing up screen output

- Fixed getting wrong CJ clothes when spawning

- Fixed problems with unicode install paths

- Fixed problem of missing GTA language files

- Fixed an issue when several vehicle colours result into black ones

- Fixed damage proof boats still taking collision damage

- Fixed vehicle color desync caused by setting paintjob

- Fixed country rifle not inflicting damage without aiming

- Fixed crouch roll glitch

- Fixed a cursor alpha issue

- Fixed ped attached objects sliding when ped walks on slopes

- Fixed Intel clipping issues

- Fixed [engineLoadTXD](mta://scripting/client/functions/engineloadtxd.md) and [engineReplaceModel](mta://scripting/client/functions/enginereplacemodel.md) not properly closing invalid files

- Fixed progress spinner not showing when server is using [latency reduction](https://wiki.multitheftauto.com/index.php?search=latency%20reduction)

- Fixed network trouble message causing WSOD when server is using [latency reduction](https://wiki.multitheftauto.com/index.php?search=latency%20reduction)

- Fixed progress spinner not showing when processing downloaded client files

- Fixed Windows "Not responding" warning when client is busy

- Fixed a bug when player could not enter any vehicle after trying to enter a vehicle in water

- Fixed gta_sa.exe not generating correctly

- Fixed custom binds not saving properly

- Fixed a startup freeze

- Sped up [engineGetVisibleTextureNames](mta://scripting/client/functions/enginegetvisibletexturenames.md)

- Made glitches more compatible with [latency_reduction](https://wiki.multitheftauto.com/index.php?search=latency_reduction) mode

- Improved bad install path detection on client launch

- Improved client error messages

- Tweaked client launcher trouble detection

- Updated anti-virus detection

- Unicode support for file paths

## Server

### Server: Additions

- Added 2 special detections - Details: [mtaserver.conf -> enablesd](mta://scripting/concepts/anti-cheat-guide.md)

- Added option to enable optimized vehicle parts state sync - Details: [r6107](https://code.google.com/p/mtasa-blue/source/detail?r=6107)

- Added server option to log loadstring calls

- Added option to compact internal databases

- Added option to automatically update [minclientversion](https://wiki.multitheftauto.com/index.php?search=minclientversion) - Details: [minclientversion_auto_update](https://wiki.multitheftauto.com/index.php?search=minclientversion_auto_update)

- Added thread performance stats

- Added server stats for RPC packets

- Added server stats for usage of event and element data names

- Updated performance stats to include open file count

### Server: Bugfixes & Changes

- Fixed server stalls caused by open ports tester and master server announcer

- Fixed several server crashes

- Fixed [killPlayer](mta://scripting/server/functions/killplayer.md) crashing server

- Fixed a server exit crash

- Fixed server crash during shutdown

- Fixed server crash when calling [setControlState](mta://scripting/shared/functions/setcontrolstate.md) with a ped

- Fixed server --maxplayers command line argument not working as advertised

- Fixed includes failing when a resource changes

- Fixed bug when player could not walk sideways while aiming with [latency_reduction](https://wiki.multitheftauto.com/index.php?search=latency_reduction) enabled

- Fixed unnecessary syncing of attached marker positions

- Fixed synced health and armor values so the fractional part is more consistent

- Fixed vehicle wheel states not syncing properly

- Tided server account handling

- Tweaked server performance stats output

- Improved mtasa:// protocol typo handler

- Reduced memory usage for database query results

- Removed sqlite external dependency

## Resources

- [**admin**] Added some anticheat info

- [**admin**] Fixed problems with certain player names

- [**race**] Fixed rankingboard bug

- [**freeroam**] Fixed vehicle command issue

- [**fastrope**] Fixed being able to fall from super high and not get hurt

- [**parachute**] Optimized resource - Details: [r966](https://code.google.com/p/mtasa-resources/source/detail?r=966), [r979](https://code.google.com/p/mtasa-resources/source/detail?r=979), [r980](https://code.google.com/p/mtasa-resources/source/detail?r=980), [r982](https://code.google.com/p/mtasa-resources/source/detail?r=982)

- [**parachute**] Reduced server CPU and bandwidth usage

- [**parachute**] Fixed some parachute stuff not working

## Editor

- Added support for hardcoded [fileCopy](mta://scripting/shared/functions/filecopy.md) function

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and Google Code repositories:*

- MTA:SA: from  [r5799](https://code.google.com/p/mtasa-blue/source/list?num=25&start=5804) to [r6156](https://code.google.com/p/mtasa-blue/source/list?num=25&start=6157)

- Resources: [from r955 to r991](https://code.google.com/p/mtasa-resources/source/list)

- [MTASA 1.3.5 released](http://forum.mtasa.com/viewtopic.php?f=31&t=71767)

[fi:Uutta versiossa 1.3.5](https://wiki.multitheftauto.com/index.php?title=Fi:Uutta_versiossa_1.3.5&action=edit&redlink=1)
