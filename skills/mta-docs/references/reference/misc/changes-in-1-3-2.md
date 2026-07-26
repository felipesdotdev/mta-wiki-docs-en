---
doc_id: "mta-wiki:6764"
title: "Changes in 1.3.2"
source_title: "Changes in 1.3.2"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.2"
revision_id: 52769
language: "en"
categories: ["Changes_in_1.3"]
---

# Changes in 1.3.2

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

### Client

#### New Functions

- Added [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

- Added [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md) (alias of [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md))

- Added [guiLabelGetColor](mta://scripting/client/functions/guilabelgetcolor.md)

- Added [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- Added [getPedOxygenLevel](mta://scripting/client/functions/getpedoxygenlevel.md)

- Added [setPedOxygenLevel](mta://scripting/client/functions/setpedoxygenlevel.md)

- Added [getVehicleComponentPosition](mta://scripting/client/functions/getvehiclecomponentposition.md)

- Added [getVehicleComponentRotation](mta://scripting/client/functions/getvehiclecomponentrotation.md)

- Added [getVehicleComponentVisible](mta://scripting/client/functions/getvehiclecomponentvisible.md)

- Added [resetVehicleComponentPosition](mta://scripting/client/functions/resetvehiclecomponentposition.md)

- Added [resetVehicleComponentRotation](mta://scripting/client/functions/resetvehiclecomponentrotation.md)

- Added [setVehicleComponentPosition](mta://scripting/client/functions/setvehiclecomponentposition.md)

- Added [setVehicleComponentRotation](mta://scripting/client/functions/setvehiclecomponentrotation.md)

- Added [setVehicleComponentVisible](mta://scripting/client/functions/setvehiclecomponentvisible.md)

- Added [getVehicleComponents](mta://scripting/client/functions/getvehiclecomponents.md)

- Added [engineGetModelLODDistance](mta://scripting/client/functions/enginegetmodelloddistance.md)

- Added [sha256](mta://scripting/shared/functions/sha256.md)

- Added [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- Added [guiGridListSetColumnTitle](mta://scripting/client/functions/guigridlistsetcolumntitle.md)

- Added [guiGridListGetColumnTitle](mta://scripting/client/functions/guigridlistgetcolumntitle.md)

- Added [guiGridListGetVerticalScrollPosition](mta://scripting/client/functions/guigridlistgetverticalscrollposition.md)

- Added [guiGridListSetVerticalScrollPosition](mta://scripting/client/functions/guigridlistsetverticalscrollposition.md)

- Added [guiGridListGetHorizontalScrollPosition](mta://scripting/client/functions/guigridlistgethorizontalscrollposition.md)

- Added [guiGridListSetHorizontalScrollPosition](mta://scripting/client/functions/guigridlistsethorizontalscrollposition.md)

- Added [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- Added [breakObject](mta://scripting/shared/functions/breakobject.md)

- Added [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- Added [isVehicleNitroRecharging](mta://scripting/client/functions/isvehiclenitrorecharging.md)

- Added [isVehicleNitroActivated](mta://scripting/client/functions/isvehiclenitroactivated.md)

- Added [getVehicleNitroCount](mta://scripting/client/functions/getvehiclenitrocount.md)

- Added [getVehicleNitroLevel](mta://scripting/client/functions/getvehiclenitrolevel.md)

- Added [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md)

- Added [setVehicleNitroCount](mta://scripting/client/functions/setvehiclenitrocount.md)

- Added [setVehicleNitroLevel](mta://scripting/client/functions/setvehiclenitrolevel.md)

- Added [setAircraftMaxVelocity](mta://scripting/shared/functions/setaircraftmaxvelocity.md)

- Added [getAircraftMaxVelocity](mta://scripting/shared/functions/getaircraftmaxvelocity.md)

- Added [getMoonSize](mta://scripting/shared/functions/getmoonsize.md)

- Added [setMoonSize](mta://scripting/shared/functions/setmoonsize.md)

- Added [resetMoonSize](mta://scripting/shared/functions/resetmoonsize.md)

- Added [guiStaticImageGetNativeSize](mta://scripting/client/functions/guistaticimagegetnativesize.md)

- Added [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- Added [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- Added [setCursorAlpha](mta://scripting/client/functions/setcursoralpha.md)

- Added [getCursorAlpha](mta://scripting/client/functions/getcursoralpha.md)

- Added [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- Added [bitAnd](mta://scripting/shared/functions/bitand.md)

- Added [bitNot](mta://scripting/shared/functions/bitnot.md)

- Added [bitOr](mta://scripting/shared/functions/bitor.md)

- Added [bitXor](mta://scripting/shared/functions/bitxor.md)

- Added [bitTest](mta://scripting/shared/functions/bittest.md)

- Added [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- Added [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- Added [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- Added [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- Added [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- Added [bitExtract](mta://scripting/shared/functions/bitextract.md)

- Added [bitReplace](mta://scripting/shared/functions/bitreplace.md)

- Added [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- Added [setSoundPan](mta://scripting/client/functions/setsoundpan.md)

- Added [getSoundPan](mta://scripting/client/functions/getsoundpan.md)

#### New Events

- Added [onClientVehicleNitroStateChange](mta://scripting/client/events/onclientvehiclenitrostatechange.md)

- Added [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md)

- Added [onClientObjectDamage](mta://scripting/client/events/onclientobjectdamage.md)

- Added [onClientWeaponFire](mta://scripting/client/events/onclientweaponfire.md)

- Added [onClientVehicleDrown](mta://scripting/client/events/onclientvehicledrown.md)

- Added [onClientPlayerVoicePause](mta://scripting/client/events/onclientplayervoicepause.md)

- Added [onClientPlayerVoiceResumed](mta://scripting/client/events/onclientplayervoiceresumed.md)

#### Changes / Bug Fixes

- Fixed [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md) killing players from falls

- Fixed textures disappearing and flickering at certain camera angles

- Fixed high CPU usage when minimized and not connected

- Integrated downgrader/patcher into the MTA installer

- More fixes for engineless NRG-500

- Fixed crashes on disconnect / reconnect

- Fixed crashes when using [setFarClipDistance](mta://scripting/shared/functions/setfarclipdistance.md)

- Fixed chinese characters in chat freezing the game

- Fixed FarClipDistance reseting each respawn

- Fixed [setFarClipDistance](mta://scripting/shared/functions/setfarclipdistance.md) messing with water drawing

- Added an interior argument (optional) to [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) and [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md)

- Fixed an issue when ped rotation while in air goes opposite direction by adding *conformPedAirRotation* argument to [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- Added work around to prevent server nitro adds cutting off recent client nitro adds

- Fixed blank lines in the client console sometimes

- Fixed launching issues with Steam

- Added heat haze setting

- Fixed crashes when getting combobox item text sometimes

- Made [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md) cancelable

- Fixed owning resource for client peds and water

- Fixed custom collisions preventing normal collisions of other models from loading correctly

- Fixed a bug when double-clicking on another server from server browser list while connecting to a server makes the game exit to desktop

- Fixed crash when destroying the source of [onClientColShapeHit](mta://scripting/client/events/onclientcolshapehit.md) event

- Fixed an error with [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- Conformed client console log date format to ISO 8601

- Fixed custom dx-fonts not working on Windows 8

- Prevented loading splash disappearing too early

- Fixed readable depth buffer not working with anti-aliasing

- Improved performance of readable depth buffer/AA fix - Details: [Depth buffer](mta://reference/misc/depthbuffer.md)

- Added more settings to [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md)

- Reduced chance of message boxes being obscured by other windows

- Fixed not working crouching with vehicle extrapolation

- Fixed startup issue with an exe version that someone gave support desk

- Fixed stuck voice problem

- Fixed [onClientPlayerVoiceStop](mta://scripting/client/events/onclientplayervoicestop.md) not working properly

- Fixed occasional invalid return value from [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- Added color coded argument to [dxGetTextWidth](mta://scripting/client/functions/dxgettextwidth.md)

- Main menu items 'Map Editor'/'Host Game' now will ask if player want to disconnect from current server

- Added proper axis support on controllers

- Fixed *hitElement* parameter working incorrectly with shotgun in [onClientPlayerWeaponFire](mta://scripting/client/events/onclientplayerweaponfire.md)

- Fixed and re-enabled [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- Added ped vertex [shader](https://wiki.multitheftauto.com/index.php?search=shader) support

- Fixed [engineGetModelTextureNames](mta://scripting/client/functions/enginegetmodeltexturenames.md) for CJ model

- Small memory optimization for the server browser

- Fixed [guiGetEnabled](mta://scripting/client/functions/guigetenabled.md) and [guiGetVisible](mta://scripting/client/functions/guigetvisible.md) for tabs

- Fixed binds that were attached directly to controls getting reset when loading default binds in settings

- Fixed [getVehicleType](mta://scripting/shared/functions/getvehicletype.md) with trailers returning empty string client-side

- Fixed chat messages not updating while a map download is in progress

- Fixed server browser disabled tab option

- Added cached info for server browser favourites

- Fixed startup issues

- Make [setObjectScale](mta://scripting/shared/functions/setobjectscale.md) accept 1 scale value for each axis

- Fixed not properly working client's console logging

- Fixed readable depth buffer not working on some graphic cards

- Fixed object scale crash

- Refixed scaled objects not being rendered when the unscaled bounding box goes off-screen

- Made it able to set velocity on (dynamic) objects

- Fixed radararea not functioning when using negative numbers for dimensions

- Improved frozen process detection

- Fixed client quit issue

- Fixed quit crash when connection history drop-down is visible

- Fixed input settings inconsistencies

- Added vertical aim sensitivity setting

- Fixed [guiGetSelectedTab](mta://scripting/client/functions/guigetselectedtab.md) crash after removing a tab

- Added target position as alternative to [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)

- Added process priority setting

- Improved installer

- Fixed PNG files with alpha channel sometimes being all black

- Added car number plates, road sign text, CJ body parts and unnamed textures to [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md)

- Added some BASS API functions to voice - Details: [Google Code](http://code.google.com/p/mtasa-blue/source/detail?r=5247)

- Added clothing component textures to [engineImportTXD](mta://scripting/client/functions/engineimporttxd.md)

- Reduced stutter/lags on big maps

- Fixed [depth buffer](mta://reference/misc/depthbuffer.md) [shaders](https://wiki.multitheftauto.com/index.php?search=shaders) not working right with mirrors

- Fixed client crash after login and spawn

- Added ability to turn off sounds when MTA:SA is minimized

- Sped up deletion of certain client element types

- Enhanced quality on usage of non-power of two image sizes for [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)

- Added bitwise operator functions

- Added a record for when a player connects to a server

- Added *alphaTransparency* argument to [engineReplaceModel](mta://scripting/client/functions/enginereplacemodel.md)

- Fixed a server browser crash

- Added 'showframegraph' command for displaying frame timings

- Added 'sinfo' command to output server info

- Fixed freeze on connect

- Fixed [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md) returning wrong values sometimes

- Added the model id as an alternative parameter to [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- Fixed vehicles losing velocity on race respawn

### Server

#### New Functions

- Added [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- Added [sha256](mta://scripting/shared/functions/sha256.md)

- Added [getMoonSize](mta://scripting/shared/functions/getmoonsize.md)

- Added [setMoonSize](mta://scripting/shared/functions/setmoonsize.md)

- Added [resetMoonSize](mta://scripting/shared/functions/resetmoonsize.md)

- Added [bitAnd](mta://scripting/shared/functions/bitand.md)

- Added [bitNot](mta://scripting/shared/functions/bitnot.md)

- Added [bitOr](mta://scripting/shared/functions/bitor.md)

- Added [bitXor](mta://scripting/shared/functions/bitxor.md)

- Added [bitTest](mta://scripting/shared/functions/bittest.md)

- Added [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- Added [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- Added [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- Added [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- Added [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- Added [bitExtract](mta://scripting/shared/functions/bitextract.md)

- Added [bitReplace](mta://scripting/shared/functions/bitreplace.md)

#### New Events

- *None yet*

#### Changes / Bug Fixes

- Added crash handler for Linux (It outputs log files in dumps/)

- Added account name to [whowas](mta://reference/misc/server-commands.md) command

- Added an interior argument (optional) to [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) and [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md)

- Fixed an issue when ped rotation while in air goes opposite direction by adding *conformPedAirRotation* argument to [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- Added auto generation of correct [min_mta_version](mta://reference/misc/meta-xml.md) to 'upgrade' command

- Changed ['upgrade'](mta://reference/misc/server-commands.md) and ['check'](mta://reference/misc/server-commands.md) commands to also work on single resources

- Fixed file download not working on some servers

- Added network filter option

- Fixed server crash when deleting element in [onResourceStop](mta://scripting/server/events/onresourcestop.md)

- Same serial now can't be banned more than once

- Fixed [fixdb](https://wiki.multitheftauto.com/index.php?search=fixdb) problems

- Fixed an error with [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- Fixed [getVehicleSirensOn](mta://scripting/shared/functions/getvehiclesirenson.md) returning a nil value

- Fixed double collisions when changing marker type

- Added 3 new special detections - Details: [mtaserver.conf -> enablesd](mta://scripting/concepts/anti-cheat-guide.md)

- Fixed 'suppress' option in [dbConnect](mta://scripting/server/functions/dbconnect.md)

- Added access to a couple of [dbConnect](mta://scripting/server/functions/dbconnect.md) logging settings

- Tweaked ASE port usage

- Added cpu core stats for Linux server

- Changed account passwords to use salted sha256

- Fixed issue when element is destroyed client sided when created and parent set in different resource than the parent

- Sped up accounts upgrade

- Fixed target range, accuracy and weapon range

- Fixed [setRuleValue](mta://scripting/server/functions/setrulevalue.md) crash

- Fixed the client-side scripts "protected" attribute not working on Linux servers

- Fixed occasional crash when empty filename used for some functions

- Fixed a problem where [onResourceStart](mta://scripting/server/events/onresourcestart.md) is not triggered for the root element when using [startResource](mta://scripting/server/functions/startresource.md) from inside a (root attached) event handler

- Added resource name and bandwidth usage to function performance stats

- Added [latency_reduction](https://wiki.multitheftauto.com/index.php?search=latency_reduction) option to [mtaserver.conf](https://wiki.multitheftauto.com/index.php?search=mtaserver.conf)

- Fixed and re-enabled [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- Fixed [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) not working on children

- Added "shared" script type to [meta.xml](mta://reference/misc/meta-xml.md)

- Decreased CPU usage by speeding up event lookups

- Fixed *visibleTo* argument not checking for errors in [outputChatBox](mta://scripting/shared/functions/outputchatbox.md)

- Tidied ASE functionality

- Fixed Windows server HTTP download compression (for [fetchRemote](mta://scripting/shared/functions/fetchremote.md))

- Fixed client using HTTP download compression

- Fixed vehicle extrapolation camera smoothness when viewing remote vehicles

- Updated server performance stats

- Fixed Linux core number in stats

- Slightly sped up server startup

- Fixed trailers desync

- Fixed train desync

- Synchronized ped traffic light

- Fixed markers created by .map-files having wrong colshapes

- Added process memory to performance stats

- Fixed server 'per player entity' crash

- Fixed [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md) after [cancelEvent](mta://scripting/shared/functions/cancelevent.md) of [onVehicleStartEnter](mta://scripting/server/events/onvehiclestartenter.md) causing network trouble

- Added 'hitanim' glitch to [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md) (shot hit animation)

- Added server setting to change syncer distances

- Added server multiple IP support

- Fixed [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md) after [xmlSetNodeValue](https://wiki.multitheftauto.com/index.php?title=XmlSetNodeValue&action=edit&redlink=1) causing a crash

- Fixed [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md) not returning the correct values

### Resources

- [**fallout**] Fixed freecam locks

- [**scoreboard**] Added support for data to be drawn as image - Details: [Google Code](http://code.google.com/p/mtasa-resources/source/detail?r=882)

- [**voice**] Added 'mutevoice' and 'unmutevoice' commands for players to mute other players permanently - Details: [Google Code](http://code.google.com/p/mtasa-resources/source/detail?r=882)

- [**admin**] Added custom ban duration when banning player via GUI

- [**admin**] Added ability to delete resource in 'Resources' tab (new [ACL](https://wiki.multitheftauto.com/wiki/ACL) right 'command.delete')

- [**admin**] Added ability to stop all resources in 'Resources' tab

- [**admin**] More informations about resources now showing in 'Resources' tab

- [**admin**] Added ability to shutdown the server in 'Server' tab

- [**admin**] Changing vehicle's color now supports new RGB system, color is picked using color picker

- [**admin**] Vehicle's lights color can now be changed

- [**admin**] Server FPS Limit can now be changed in 'Server' tab

- [**webadmin**] Added 'Players' tab where you can kick/ban players on server

- [**ipb**] Added Ingame Performance Browser - Details: [Google Code](http://code.google.com/p/mtasa-resources/source/detail?r=896)

- [**votemanager**] Fixed an error when votemanager can't start votekick, votekill or voteban, if the player, who we want to vote, name contains 1 character

- [**race**] Added editor visualization of checkpoint connections

- [**admin**] Added ability to view players' screen

### Editor

- Fixed 'Locked Time' option resetting

- Reduced the size of map files

- Fixed some settings not resetting when you start a new map after working in another

- Fixed weapon model changes to 1337 after saving/loading some times

- Fixed problem with invalid editor_dump

- Fixed not loading objects properly when a vehicle position attribute isn't saved

- Added ability to remove world objects in editor

- Added ability to include low LOD models for some objects

- Map Editor won't remove script lines in meta.xml

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and Google Code repositories:*

- MTA:SA: from  [r4600](http://code.google.com/p/mtasa-blue/source/list?num=25&start=4605) and [above](http://code.google.com/p/mtasa-blue/source/list)

- Resources: from [r875](http://code.google.com/p/mtasa-resources/source/list?num=25&start=883) and [above](http://code.google.com/p/mtasa-resources/source/list)
