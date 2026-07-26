---
doc_id: "mta-wiki:10104"
title: "Changes in 1.5.6"
source_title: "Changes in 1.5.6"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.6"
revision_id: 75875
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:10:30.969685+00:00"
---

# Changes in 1.5.6

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

1.5.6 was released on September 6, 2018.

- Mantis changelog: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.5.5...1.5.6](https://github.com/multitheftauto/mtasa-blue/compare/1.5.5...1.5.6)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/3](https://github.com/multitheftauto/mtasa-blue/milestone/3)

- Release announcement on forums: [https://forum.mtasa.com/topic/111160-multi-theft-auto-san-andreas-156-is-released/](https://forum.mtasa.com/topic/111160-multi-theft-auto-san-andreas-156-is-released/)

## Main Additions / Changes

Click to collapse [-]

- Custom IFP animation support ([engineReplaceAnimation](mta://scripting/client/functions/enginereplaceanimation.md), [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md))

- New drawing function: [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md)

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-5-5.md).

- This is the **23rd** 1.x.x release, released [6.9.2018](https://buildinfo.mtasa.com/?Revision=14334)

- **334** days

- **40** new functions

- **2** new events

- **5** deprecations

- **100+** bug fixes and changes

- **461** commits ([see comparison](https://github.com/multitheftauto/mtasa-blue/compare/1.5.5...1.5.6))

- **83** new open Mantis issues

- **60** resolved Mantis issues

- **500** closed Mantis issues

- **88** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+created%3A2017-10-07..2018-09-06))

- **15** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aissue+milestone%3A1.5.6+closed%3A2017-10-07..2018-09-06))

- **15** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aissue+no%3Amilestone+closed%3A2017-10-07..2018-09-06))

- **29** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+created%3A2017-10-07..2018-09-06))

- **90** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+milestone%3A1.5.6+is%3Amerged))

- **35** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?utf8=%E2%9C%93&q=is%3Apr+no%3Amilestone+closed%3A2017-10-07..2018-09-06))

- **28** contributors of which **13** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2017-10-07&to=2018-09-06&type=c))

- **55** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **6** vendor updates

## Scripting

### Client

Click to collapse [-]

#### 19 New Functions

- Add [isVehicleWheelOnGround](mta://scripting/client/functions/isvehiclewheelonground.md) ([Mantis 0006132](https://bugs.mtasa.com/view.php?id=6132))

- Add [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md) for local vehicles ([Mantis 0009733](https://bugs.mtasa.com/view.php?id=9733))

- Add [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md) ([Mantis 0009664](https://bugs.mtasa.com/view.php?id=9664))

- Add [extinguishFire](mta://scripting/client/functions/extinguishfire.md)

- Add custom IFP animations using new [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md), [engineReplaceAnimation](mta://scripting/client/functions/enginereplaceanimation.md) and [engineRestoreAnimation](mta://scripting/client/functions/enginerestoreanimation.md) functions ([Mantis 0004571](https://bugs.mtasa.com/view.php?id=4571))

- Add [guiMemoIsReadOnly](mta://scripting/client/functions/guimemoisreadonly.md) and [guiEditIsReadOnly](mta://scripting/client/functions/guieditisreadonly.md) ([Mantis 0006962](https://bugs.mtasa.com/view.php?id=6962) [GitHub #236](https://github.com/multitheftauto/mtasa-blue/pull/236) by FileEX)

- Add [guiMemoGetVerticalScrollPosition](mta://scripting/client/functions/guimemogetverticalscrollposition.md) and [guiMemoSetVerticalScrollPosition](mta://scripting/client/functions/guimemosetverticalscrollposition.md) ([Mantis 0008957](https://bugs.mtasa.com/view.php?id=8957))

- Add [getPedsLODDistance](mta://scripting/client/functions/getpedsloddistance.md), [setPedsLODDistance](mta://scripting/client/functions/setpedsloddistance.md) and [resetPedsLODDistance](mta://scripting/client/functions/resetpedsloddistance.md) ([GitHub #231](https://github.com/multitheftauto/mtasa-blue/pull/231) by CrosRoad95)

- Add [guiEditGetMaxLength](mta://scripting/client/functions/guieditgetmaxlength.md) and [guiEditIsMasked](mta://scripting/client/functions/guieditismasked.md) ([GitHub #255](https://github.com/multitheftauto/mtasa-blue/pull/255) by FileEX)

- Add [guiWindowIsMovable](mta://scripting/client/functions/guiwindowismovable.md) and [guiWindowIsSizable](mta://scripting/client/functions/guiwindowissizable.md) ([GitHub #272](https://github.com/multitheftauto/mtasa-blue/pull/272) by FileEX)

- Add [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md)

#### 3 New Arguments & Parameters

- Add *immediate* argument to [setWorldSoundEnabled](mta://scripting/client/functions/setworldsoundenabled.md) to stop sound immediately ([Mantis 0009490](https://bugs.mtasa.com/view.php?id=9490))

- Add *postGUI* argument to [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

- Add *noiseEnabled* argument to [setCameraGoggleEffect](mta://scripting/client/functions/setcameragoggleeffect.md)

#### 16+ Bugfixes & Changes

- Add [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md)().SettingFullScreenStyle

- Add *health* attribute to [Element/Ped](mta://reference/misc/element-ped.md) ([Mantis 0009817](https://bugs.mtasa.com/view.php?id=9817))

- Return [vectors](mta://reference/misc/vector3.md) for vehicle component functions ([Mantis 0009507](https://bugs.mtasa.com/view.php?id=9507))

- Fix some issues with [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md) (recent change in behaviour)

- Fix [unbindKey](mta://scripting/shared/functions/unbindkey.md) malfunctioning as soon you bind the same command (function) to another key again ([Mantis 0009178](https://bugs.mtasa.com/view.php?id=9178))

- Fix OOP [ped:getBonePosition](mta://scripting/client/functions/getpedboneposition.md) returning multiple numbers instead of [Vector3](mta://reference/misc/vector3.md) ([Mantis 0009487](https://bugs.mtasa.com/view.php?id=9487))

- Fix OOP [vehicle:getMaxPassengers](mta://scripting/shared/functions/getvehiclemaxpassengers.md) method

- Fix incorrect name "Night_Strick" to "Night_Stick" when calling [engineGetModelIDFromName](mta://scripting/client/functions/enginegetmodelidfromname.md) or returning from [engineGetModelNameFromID](mta://scripting/client/functions/enginegetmodelnamefromid.md) (backward compatible)

- Fix [bindKey](mta://scripting/shared/functions/bindkey.md) and [unbindKey](mta://scripting/shared/functions/unbindkey.md) behaving incorrectly with commands under certain circumstances ([Mantis 0009178](https://bugs.mtasa.com/view.php?id=9178))

- Add *underworldwarp* [special world property](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) ([Mantis 0009807](https://bugs.mtasa.com/view.php?id=9807))

- Add OOP Team.[getPlayers()](mta://scripting/shared/functions/getplayersinteam.md) and Team.players to client-side ([Mantis 0009760](https://bugs.mtasa.com/view.php?id=9760))

- Add [getModelFromName](mta://scripting/shared/functions/getvehiclemodelfromname.md), [getNameFromModel](mta://scripting/shared/functions/getvehiclenamefrommodel.md), [getOriginalHandling](mta://scripting/shared/functions/getoriginalhandling.md), [getUpgradeSlotName](mta://scripting/shared/functions/getvehicleupgradeslotname.md) client-side [Vehicle](mta://reference/misc/vehicle.md) class methods ([Mantis 0009849](https://bugs.mtasa.com/view.php?id=9849))

- Add missing compatible [vehicle upgrades](mta://reference/misc/vehicle-upgrades.md) to [getVehicleCompatibleUpgrades](mta://scripting/shared/functions/getvehiclecompatibleupgrades.md) (and some other compatibility related checks) ([Mantis 0009433](https://bugs.mtasa.com/view.php?id=9433))

- Add [getVehicleModelExhaustFumesPosition](mta://scripting/client/functions/getvehiclemodelexhaustfumesposition.md) and [setVehicleModelExhaustFumesPosition](mta://scripting/client/functions/setvehiclemodelexhaustfumesposition.md) OOP variants ([Mantis 0009898](https://bugs.mtasa.com/view.php?id=9898))

- Fix an [integer](mta://reference/misc/int.md) overflow bug where cursor position got returned as high as 65535 for cursor events. Will now return a minus position instead.

- Fix *CVar* parameter not working on [getChatboxLayout](mta://scripting/client/functions/getchatboxlayout.md) ([Mantis 0009611](https://bugs.mtasa.com/view.php?id=9611))

### Server

Click to collapse [-]

#### 11 New Functions

- Add [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md)

- Add account functions: [getAccountIP](mta://scripting/server/functions/getaccountip.md), [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md), [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md), [setAccountName](mta://scripting/server/functions/setaccountname.md), [getAccountID](mta://scripting/server/functions/getaccountid.md) and [getAccountByID](mta://scripting/server/functions/getaccountbyid.md) ([Mantis 0009562](https://bugs.mtasa.com/view.php?id=9562))

- Add [tocolor](mta://scripting/shared/functions/tocolor.md) server-side as well ([GitHub #291](https://github.com/multitheftauto/mtasa-blue/pull/291) by patrikjuvonen)

- Add [getVehicleRespawnPosition](mta://scripting/server/functions/getvehiclerespawnposition.md) and [getVehicleRespawnRotation](mta://scripting/server/functions/getvehiclerespawnrotation.md) ([GitHub #334](https://github.com/multitheftauto/mtasa-blue/pull/334) by l0nger)

- Add [setVehicleRespawnRotation](mta://scripting/server/functions/setvehiclerespawnrotation.md) ([GitHub #338](https://github.com/multitheftauto/mtasa-blue/pull/338) by l0nger)

#### 2 New Events

- Add [onPickupLeave](mta://scripting/server/events/onpickupleave.md) and [onPlayerPickupLeave](mta://scripting/server/events/onplayerpickupleave.md) events ([Mantis 0009770](https://bugs.mtasa.com/view.php?id=9770))

#### 2 Deprecations

- Deprecate [givePedJetPack](mta://scripting/server/functions/givepedjetpack.md) and [removePedJetPack](mta://scripting/server/functions/removepedjetpack.md) by introducing [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md)

#### 2 New Arguments & Parameters

- Add *targetResource* argument to [refreshResources](mta://scripting/server/functions/refreshresources.md) function to target a specific resource

- Add *deleted* parameter to [onResourceStop](mta://scripting/server/events/onresourcestop.md)

#### 9+ Bugfixes & Changes

- Fix vehicle.handling and add [setter](mta://scripting/shared/functions/setvehiclehandling.md) to it

- Remove incorrect *matchingDimension* argument from [onPickupHit](mta://scripting/server/events/onpickuphit.md) and [onPlayerPickupHit](mta://scripting/server/events/onplayerpickuphit.md) events

- Increase reliability of weather blending functions and consistency of [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md) and [getWeather](mta://scripting/shared/functions/getweather.md) ([Mantis 0005204](https://bugs.mtasa.com/view.php?id=5204))

- [callRemote](mta://scripting/server/functions/callremote.md) will now send a *Content-Type: application/json* header

- Fix *bShallow* argument not working on [createWater](mta://scripting/shared/functions/createwater.md) server-side ([Mantis 0009608](https://bugs.mtasa.com/view.php?id=9608))

- Fix [setPlayerName](mta://scripting/server/functions/setplayername.md) and [redirectPlayer](mta://scripting/server/functions/redirectplayer.md) to only accept a [player](mta://reference/misc/player.md) element

- Fix [getPlayerName](mta://scripting/shared/functions/getplayername.md), [getPlayerIP](mta://scripting/server/functions/getplayerip.md) and [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md) to only accept a [player](mta://reference/misc/player.md) or [console](mta://reference/misc/element-console.md) element

- Extend ACL to allow *ModifyOtherObjects* only on a single resource ([learn more here](mta://tutorials/access-control-list.md)) ([6614d](https://github.com/multitheftauto/mtasa-blue/commit/6614d9ca56d7a9d64c486831715fd6342763ba2b) by botder)

- Tweak some vehicle respawn [position](mta://scripting/server/functions/setvehiclerespawnposition.md)/[rotation](mta://scripting/server/functions/setvehiclerespawnrotation.md) function OOP variants ([GitHub #338](https://github.com/multitheftauto/mtasa-blue/pull/338) by l0nger)

### Shared (*Client & Server side*)

Click to collapse [-]

#### 10 New Functions

- Add [clearChatBox](mta://scripting/shared/functions/clearchatbox.md)

- Add [encodeString](mta://scripting/shared/functions/encodestring.md) and [decodeString](mta://scripting/shared/functions/decodestring.md)

- Add [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- Add [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md) and [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md) ([GitHub #73](https://github.com/multitheftauto/mtasa-blue/pull/73) by lex128)

- Add [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- Add [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- Add [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- Add [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md)

#### 3 Deprecations

- Deprecate [doesPedHaveJetPack](mta://scripting/shared/functions/doespedhavejetpack.md) by introducing [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- Deprecate [getVehicleTurnVelocity](mta://scripting/shared/functions/getvehicleturnvelocity.md) and [setVehicleTurnVelocity](mta://scripting/shared/functions/setvehicleturnvelocity.md) by introducing [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md) and [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md) respectively

#### 3 New Arguments & Parameters

- Add *preEventFunction* and *postEventFunction* arguments to [addDebugHook](mta://scripting/shared/functions/adddebughook.md) (useful for code performance debugging)

- Add *elementsWithin* OOP variable to [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

#### 8+ Bugfixes & Changes

- Fix [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md) not working with negative dimensions

- Fix argument naming in RadarArea *Position methods

- Fix client-side [setElementData](mta://scripting/shared/functions/setelementdata.md) not updating the server when enabling synchronization on an existing key with the same value

- Fix [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md) not handling [Vector2](mta://reference/misc/vector2.md) arguments properly

- Fix [blip](mta://reference/misc/blip.md) *ordering* and *visibleDistance* arguments having [integer](mta://reference/misc/int.md) overflow issues ([Mantis 0006455](https://bugs.mtasa.com/view.php?id=6455))

- Clamp [blip](mta://reference/misc/blip.md) *size* properly between 0 and 25

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md) will now output errors found in the XML file if any ([Mantis 0009616](https://bugs.mtasa.com/view.php?id=9616))

- Add support for *$2a$* prefix to [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

## Client

Click to collapse [-]

### 5 Additions

- Updated and added translations for various languages, including Bulgarian, Indonesian and Chinese (Traditional)

- Enable switching camera view mode for trains ([GitHub #125](https://github.com/multitheftauto/mtasa-blue/pull/125) by ZReC)

- Added full axis option to joystick bindings

- Added master volume setting to audio settings ([Mantis 0009896](https://bugs.mtasa.com/view.php?id=9896))

- Added *reloadnews* command for developers

### 31 Bugfixes & Changes

- Fixed problems when using a controller with more than 7 axis

- Restore default exhaust fumes position when disconnecting

- Fix vehicle radio sometimes won't play

- Fixed incorrect path in [guiCreateStaticImage](mta://scripting/client/functions/guicreatestaticimage.md) error message

- Fixed [dxGetTextWidth](mta://scripting/client/functions/dxgettextwidth.md) returns wrong width of text ([Mantis 0009745](https://bugs.mtasa.com/view.php?id=9745))

- Fixed some minor memory leaks

- Improved client [fetchRemote](mta://scripting/shared/functions/fetchremote.md) reliability

- Fixed [dxGetStatus()](mta://scripting/client/functions/dxgetstatus.md).SettingWindowed sometimes being incorrect

- Averted one type of igdumd32.dll crash

- Added help dialog for crash at offset 003C51A8 (Corrupt anim hierarchy)

- Fixed client crash caused by invalid blip icon

- Fix animation getting stuck after carjack

- Restore console input focus after [guiMoveToBack](mta://scripting/client/functions/guimovetoback.md)

- Fixed client crash caused by destroying markers during hit/leave events

- Fixed shaders sometimes losing default values

- Fixed console displays an error message when pressing the key of a disabled MTA control ([Mantis 0009166](https://bugs.mtasa.com/view.php?id=9166))

- Fixed error when loading certain jpeg files with unicode Windows username

- Fixed [engineLoadDFF](mta://scripting/client/functions/engineloaddff.md)/[TXD](mta://scripting/client/functions/engineloadtxd.md) raw buffer not being deallocated after import

- Fixed 100% CPU usage while using the *debugscript* command and having the *chat text black/white outline* setting enabled

- Fixed crash caused by calling client-side [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md) with a ped

- Fixed crash caused by passing empty string to [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md) crashes client ([Mantis 0009844](https://bugs.mtasa.com/view.php?id=9844))

- Fixed several additional crashes

- Fixed issues with wearing a jetpack, choking or using animations at the same time ([Mantis 0009522](https://bugs.mtasa.com/view.php?id=9522))

- Freezing a ped wearing jetpack will no longer remove the jetpack automatically

- *Port* is now an optional parameter for the *connect* command, defaults to 22003 ([Mantis 0007047](https://bugs.mtasa.com/view.php?id=7047))

- Typing the *connect* command will no longer disconnect until all parameters have been checked ([Mantis 0007047](https://bugs.mtasa.com/view.php?id=7047))

- Removed the built-in *whowas* command ([Mantis 0006722](https://bugs.mtasa.com/view.php?id=6722))

- Added native language names

### 3 Vendor Updates

- Update BASS and sound-related dependencies

- Update CEF to 3.3440.1805.gbe070f9 ([Chromium 68.0.3440.84](https://chromereleases.googleblog.com/2018/07/stable-channel-update-for-desktop_31.html))

- Update libpng to 1.6.35

## Server

Click to collapse [-]

### 3 Additions

- Added Server SDK project

- Added *reloadacl* command ([Mantis 0009626](https://bugs.mtasa.com/view.php?id=9626))

- Added server console arrow up/down command history ([Mantis 0009814](https://bugs.mtasa.com/view.php?id=9814)) ([GitHub #274](https://github.com/multitheftauto/mtasa-blue/pull/274) by patrikjuvonen)

### 11 Bugfixes & Changes

- Fix for some cases of internal.db access errors

- Fix server crashing when using the *upgrade* command ([Mantis 0009530](https://bugs.mtasa.com/view.php?id=9530))

- Fix crash in account manager

- Fix [callRemote](mta://scripting/server/functions/callremote.md) call without queueName failing

- Excluded non-joined players from calls to [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md) and [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- Fix self-compiled server crash on [callRemote](mta://scripting/server/functions/callremote.md) ([Mantis 0009787](https://bugs.mtasa.com/view.php?id=9787))

- Fix server crash on server-window resize

- Server query fix for networks which block 1 byte UDP packets

- Remove fully deprecated functions from acl.xml and add new missing ones ([Mantis 0005701](https://bugs.mtasa.com/view.php?id=5701))

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md) wouldn't always set the rotation if an object was near the spawn point ([Mantis 0008540](https://bugs.mtasa.com/view.php?id=8540))

### 1 Vendor Update

- Update SQLite to [3.24.0](https://www.sqlite.org/releaselog/3_24_0.html) ([Mantis 0009916](https://bugs.mtasa.com/view.php?id=9916))

## Shared

Click to collapse [-]

### 2 Bugfixes & Changes

- Fixed curl not requesting compressed datum

- Fix cloned elements not getting removed on resource stop

### 2 Vendor Updates

- Update curl to [7.61.0](https://daniel.haxx.se/blog/2018/07/11/curl-7-61-0/) ([GitHub #270](https://github.com/multitheftauto/mtasa-blue/pull/270) by patrikjuvonen)

- Update json-c to [0.31.1](https://github.com/json-c/json-c/blob/master/ChangeLog) ([GitHub #268](https://github.com/multitheftauto/mtasa-blue/pull/268) by patrikjuvonen)

## Resources

Click to collapse [-]

- [admin] Added ban search feature to *Bans* tab

- [admin] Fixed gridlist sorting bug (contents getting corrupted/mangled up)

- [admin] Improved logging of responsible admin (any type of change to ACL through panel, details on actions like unbanning)

- [admin] Miscellaneous fixes: resizing ban details window (and extended its size for longer serials), broken Anonymous admin kicks, updated flags

- [admin] Added *copy serial* to ban details tab in *Bans* and enabled doubleclicking on a row to open that view

- [freeroam] Added player nick search (filtering) to F1 warp window

- [freeroam] Fixed vehicle label/controls disappearing randomly while in a vehicle

- [freeroam] Fixed some recurring client debug warnings

- [scoreboard] Added countryflags to TAB

- [traffic] Removed the *traffic* resource from official resources package due to it's inefficiency, size and bloatedness

## Editor

Click to collapse [-]

- Added *sirens* option and fixed *plate*

- Added a *Favourites* category under *All categories* in element browser

- Added sirens state option for mapped vehicles and fixed plate text

## Extra Information

*More detailed information available on [our Mantis Bug Tracker changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
