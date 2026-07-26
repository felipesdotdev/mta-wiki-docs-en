---
doc_id: "mta-wiki:8403"
title: "Changes in 1.5.8"
source_title: "Changes in 1.5.8"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.8"
revision_id: 72828
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:12:09.144914+00:00"
---

# Changes in 1.5.8

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

1.5.8 was released on October 11, 2020.

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.5.7...1.5.8](https://github.com/multitheftauto/mtasa-blue/compare/1.5.7...1.5.8)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/2](https://github.com/multitheftauto/mtasa-blue/milestone/2)

- Release announcement on forums: [https://forum.mtasa.com/topic/127609-multi-theft-auto-san-andreas-158-is-released/](https://forum.mtasa.com/topic/127609-multi-theft-auto-san-andreas-158-is-released/)

## Main Additions / Changes

Click to collapse [-]

- Added [dxDrawPrimitive3D](mta://scripting/client/functions/dxdrawprimitive3d.md) and [dxDrawMaterialPrimitive3D](mta://scripting/client/functions/dxdrawmaterialprimitive3d.md) ([#760](https://github.com/multitheftauto/mtasa-blue/pull/760) by **CrosRoad95**)

- Added functions to modify dynamic objects' behaviour ([#784](https://github.com/multitheftauto/mtasa-blue/pull/784) by **forkerer**)

- Added dynamic ped ID allocating using [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) and [engineFreeModel](mta://scripting/client/functions/enginefreemodel.md) ([#349](https://github.com/multitheftauto/mtasa-blue/commit/475544f1753ce1af24c4cdff7f0d0be48ede709b) by **lopezloo** + **Neproify** + **Arran** + **qaisjp**)

- Added functions to manipulate colshapes parameters ([#1215](https://github.com/multitheftauto/mtasa-blue/pull/1215) by **StrixG**)

- Added element data subscription functionality ([#1055](https://github.com/multitheftauto/mtasa-blue/pull/1055) by **tederis**)

- Added [engineGetModelTextures](mta://scripting/client/functions/enginegetmodeltextures.md) function ([#1058](https://github.com/multitheftauto/mtasa-blue/pull/1058) by **Lpsd**)

- Improve trailer sync ([#1247](https://github.com/multitheftauto/mtasa-blue/pull/1247) by **tederis**)

- Added wheel scaling functions ([#1641](https://github.com/multitheftauto/mtasa-blue/pull/1641), [#1644](https://github.com/multitheftauto/mtasa-blue/pull/1644), and [#1648](https://github.com/multitheftauto/mtasa-blue/pull/1648) by **AlexTMjugador**)

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-5-7.md).

- This is the **25th** 1.x.x release

- **407** days

- **1** deprecation

- **5** announced backwards incompatible changes

- **41** new functions

- **68+** bug fixes and changes

- **465** commits ([see comparison](https://github.com/multitheftauto/mtasa-blue/compare/1.5.7...1.5.8))

- **197** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aopen+is%3Aissue+created%3A2019-08-31..2020-10-11))

- **102** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+milestone%3A1.5.8))

- **108** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+closed%3A2019-08-31..2020-10-11+no%3Amilestone))

- **46** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Aopen+is%3Apr+created%3A2019-08-31..2020-10-11))

- **194** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+milestone%3A1.5.8+is%3Amerged))

- **36** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2019-08-31..2020-10-11))

- **39** contributors of which **27** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2019-08-31&to=2020-10-11&type=c))

- **98+** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **4** vendor updates

**Note:** Last update to these statistics was made
2,113 days ago.

## Scripting

Click to collapse [-]

### 5 Backwards Incompatible Changes

These changes will take effect in 1.6:

- [callRemote](mta://scripting/server/functions/callremote.md) callbacks currently set the error code to **nil** when there is no error. In 1.6, to be consistent with [fetchRemote](mta://scripting/shared/functions/fetchremote.md), the error code reported will be **0**. See [GitHub #294](https://github.com/multitheftauto/mtasa-blue/issues/294).

- Since July 2016 if you provide an invalid string like **"randomstring"** when a function expects a number, the string will be treated as **0** and raise a script warning. In 1.6 this will be an error. You will still be able to provide strings containing numbers (e.g. **"100"** and **"12.34"**), this change only affects invalid strings. See [GitHub #1043](https://github.com/multitheftauto/mtasa-blue/issues/1043).

- When providing a width and height of (0, 0) to [createBrowser](mta://scripting/client/functions/createbrowser.md) or [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md) you will encounter a script error instead of a warning. The warning was introduced Feb 2019. See [GitHub #1069](https://github.com/multitheftauto/mtasa-blue/issues/1069).

- Some functions expect only unsigned integers (positive numbers), and since Jan 2016 providing negative numbers would be a warning. This will now be an error. See [GitHub #1070](https://github.com/multitheftauto/mtasa-blue/issues/1070).

- Since Aug 2015, we replaced the custom **mtalocal://** URL scheme with **[http://mta/resourceName/blah.html](http://mta/resourceName/blah.html)**. This **mtalocal://** URL scheme will now be removed. See [GitHub #1071](https://github.com/multitheftauto/mtasa-blue/issues/1071).

This list is inconclusive and we may introduce more changes later.

## Client

Click to collapse [-]

### 21 New Functions

- Added [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md) (previously available server-side only) ([#810](https://github.com/multitheftauto/mtasa-blue/pull/810) by **StrixG**)

- Added [setPedArmor](mta://scripting/shared/functions/setpedarmor.md) (previously available server-side only) ([#811](https://github.com/multitheftauto/mtasa-blue/pull/811) by **StrixG**)

- Added [areVehicleLightsOn](mta://scripting/client/functions/arevehiclelightson.md) ([#938](https://github.com/multitheftauto/mtasa-blue/pull/938) by **StrixG**)

- Added [dxDrawPrimitive3D](mta://scripting/client/functions/dxdrawprimitive3d.md) and [dxDrawMaterialPrimitive3D](mta://scripting/client/functions/dxdrawmaterialprimitive3d.md) ([#760](https://github.com/multitheftauto/mtasa-blue/pull/760) by **CrosRoad95**)

- Added functions to modify dynamic objects' behaviour ([#784](https://github.com/multitheftauto/mtasa-blue/pull/784) by **forkerer**)

- [engineGetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginegetmodelphysicalpropertiesgroup.md)

- [engineRestoreModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginerestoremodelphysicalpropertiesgroup.md)

- [engineSetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginesetmodelphysicalpropertiesgroup.md)

- [engineGetObjectGroupPhysicalProperty](mta://scripting/client/functions/enginegetobjectgroupphysicalproperty.md)

- [engineRestoreObjectGroupPhysicalProperties](mta://scripting/client/functions/enginerestoreobjectgroupphysicalproperties.md)

- [engineSetObjectGroupPhysicalProperty](mta://scripting/client/functions/enginesetobjectgroupphysicalproperty.md)

- Added dynamic ped ID allocating using [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) and [engineFreeModel](mta://scripting/client/functions/enginefreemodel.md) ([#349](https://github.com/multitheftauto/mtasa-blue/commit/475544f1753ce1af24c4cdff7f0d0be48ede709b) by **lopezloo** + **Neproify** + **Arran** + **qaisjp**)

- Added [engineResetModelLODDistance](mta://scripting/client/functions/engineresetmodelloddistance.md) function ([#971](https://github.com/multitheftauto/mtasa-blue/pull/971) by **Lpsd**)

- Added [engineGetModelTextures](mta://scripting/client/functions/enginegetmodeltextures.md) function ([#1058](https://github.com/multitheftauto/mtasa-blue/pull/1058) by **Lpsd**)

- Added [resetBlurLevel](mta://scripting/client/functions/resetblurlevel.md) function ([#1266](https://github.com/multitheftauto/mtasa-blue/pull/1266) by **Luxy.c**)

- Added [dxGetTextSize](mta://scripting/client/functions/dxgettextsize.md) function ([#935](https://github.com/multitheftauto/mtasa-blue/pull/935) by **StrixG**)

- Added functions to modify vehicle wheels, visibly and in collision by ([#1641](https://github.com/multitheftauto/mtasa-blue/pull/1641), [#1644](https://github.com/multitheftauto/mtasa-blue/pull/1644), and [#1648](https://github.com/multitheftauto/mtasa-blue/pull/1648) by **AlexTMjugador**)

- [getVehicleWheelScale](mta://scripting/client/functions/getvehiclewheelscale.md)

- [getVehicleModelWheelSize](mta://scripting/client/functions/getvehiclemodelwheelsize.md)

- [setVehicleWheelScale](mta://scripting/client/functions/setvehiclewheelscale.md)

- [setVehicleModelWheelSize](mta://scripting/client/functions/setvehiclemodelwheelsize.md)

### 49 Bug Fixes & Changes

- Added new client setting to toggle external sounds ([#834](https://github.com/multitheftauto/mtasa-blue/pull/834) by **patrikjuvonen**)

- Fix crash when attempting to stream out a sound that's not streamed in (See commit [e1b7c73](https://github.com/multitheftauto/mtasa-blue/commit/e1b7c730448d12a5eeb452239e8053e86924294f) by **sbx320**)

- Fix [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md) *segments* argument being wrongly offset by one ([#1079](https://github.com/multitheftauto/mtasa-blue/pull/1079) by **ApeLsiN4eG**)

- Fix potential crash when moving objects (See commit [90895c2](https://github.com/multitheftauto/mtasa-blue/commit/90895c221549893501f5f717af3ca56878e29b5d) by **botder**)

- Update credits (See commit [39227d7](https://github.com/multitheftauto/mtasa-blue/commit/39227d795efafe940dc6c317c20b0162b1bd0bb3) by **qaisjp**)

- Don't apply damage to peds without a game entity (See commit [632130e](https://github.com/multitheftauto/mtasa-blue/commit/632130e36a96071290593fc3c677a536f7b19e1f) by **botder**)

- Fix doors state with setElementModel ([#599](https://github.com/multitheftauto/mtasa-blue/pull/599) by **FileEX**)

- Added CVAR _beta_qc_rightclick_command allowing you to reconnect by right clicking the "Quick Connect" button on the main menu (See commit [d1c60675](https://github.com/multitheftauto/mtasa-blue/commit/d1c60675fc0f0f62b69707ae81a82e6bbdf36042) by **qaisjp**)

- Added more data to [getPedAnimation](mta://scripting/client/functions/getpedanimation.md) ([#892](https://github.com/multitheftauto/mtasa-blue/pull/892) by **Dezash**)

- Added missing destroy method to DxFont ([#1259](https://github.com/multitheftauto/mtasa-blue/pull/1259) by **MegadreamsBE**)

- Increase [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md) limit (See commit [4c36d37](https://github.com/multitheftauto/mtasa-blue/commit/4c36d37056d2a1496904f394bf96303dd0f2b4c5) by **qaisjp**)

- Fix "ancient" weapon fire crash ([#1109](https://github.com/multitheftauto/mtasa-blue/pull/1109) by **saml1er**)

- Fix [bitExtract](mta://scripting/shared/functions/bitextract.md) (See commit [aa2df39d](https://github.com/multitheftauto/mtasa-blue/commit/aa2df39d3e40e5b446ffea376ef96df89916a9d0) by **ccw808**)

- Fix texture blending ([#1098](https://github.com/multitheftauto/mtasa-blue/pull/1098) by **StrixG**)

- Added client setting to toggle internet sound streams ([#834](https://github.com/multitheftauto/mtasa-blue/pull/834) by **patrikjuvonen**)

- Implement "remember this option" checkbox to NVidia Optimus dialog ([#1177](https://github.com/multitheftauto/mtasa-blue/pull/1177) by **Lpsd**)

- Fix inability to crouch when player has 1 HP ([#1138](https://github.com/multitheftauto/mtasa-blue/pull/1138) by **CrosRoad95**)

- Improve trailer sync ([#1247](https://github.com/multitheftauto/mtasa-blue/pull/1247) by **tederis**)

- Fix driveby for peds ([#1290](https://github.com/multitheftauto/mtasa-blue/pull/1290) by **Zangomangu**)

- Added "SettingHighDetailPeds" to [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md) ([#1384](https://github.com/multitheftauto/mtasa-blue/pull/1384) by **Patrick2562**)

- Added feature to remove server from the "Recent" tab in server browser ([#1381](https://github.com/multitheftauto/mtasa-blue/pull/1381) by **ecastro98**)

- Fix [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md) failure when there are too many vehicles streamed in ([#1431](https://github.com/multitheftauto/mtasa-blue/pull/1431) by **saml1er**)

- Fix issue with [engineReplaceModel](mta://scripting/client/functions/enginereplacemodel.md) kicking the player out of the vehicle ([#1433](https://github.com/multitheftauto/mtasa-blue/pull/1433) by **saml1er**)

- Moved exe patching to loader ([#1520](https://github.com/multitheftauto/mtasa-blue/pull/1520) by **ccw808**)

- Fix various return values when using OOP (e.g: [5110559b](https://github.com/multitheftauto/mtasa-blue/commit/5110559b7a7f2d258f01be1dce18fe63d8bca400), [88379b8d](https://github.com/multitheftauto/mtasa-blue/commit/88379b8ded766b2d35e171b6d11ef33cb2663b96) by **qaisjp**)

- Fixed incorrect VRAM detection ([#1589](https://github.com/multitheftauto/mtasa-blue/pull/1589) by **TheNormalnij**)

- Added ability to play sounds from raw data to playSound(3D) ([#1234](https://github.com/multitheftauto/mtasa-blue/pull/1234) by **Dezash**)

- Allow downloading of files from other resources ([#945](https://github.com/multitheftauto/mtasa-blue/pull/945) by **TheNormalnij**) - this affects:

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- Added ability to get raw controller analog value ([#1165](https://github.com/multitheftauto/mtasa-blue/pull/1165) by **Addlibs**)

- Added user agent workaround for YouTube TV ([#1243](https://github.com/multitheftauto/mtasa-blue/pull/1243) by **qaisjp**)

- Added missing destroy method to DxFont ([#1259](https://github.com/multitheftauto/mtasa-blue/pull/1259) by **MegadreamsBE**)

- Fix engineReplaceModel memory leak ([#1265](https://github.com/multitheftauto/mtasa-blue/pull/1265) by **saml1er**)

- Fix vehicle model memory leaks (See commit [46dbbe7](https://github.com/multitheftauto/mtasa-blue/commit/46dbbe7dd2c4621d7564cf272e8a432cf9f57300) by **saml1er**)

- Fix texture memory leak (See commit [d5722d5](https://github.com/multitheftauto/mtasa-blue/commit/d5722d5ac5c0ed0210849bf03c263ec88ea98c2a) by **saml1er**)

- Enable enter_exit for peds to fix alternative attack ([#1295](https://github.com/multitheftauto/mtasa-blue/pull/1295) by **Zangomangu**)

- Fix "Select device" hides under other program without MTA icon on a taskbar (See commit [2c5251a](https://github.com/multitheftauto/mtasa-blue/commit/2c5251a42a640ccc9ffa928cb2844c9295f47c6c) by **ccw808**)

- Fix primitive colors are always white ([#1312](https://github.com/multitheftauto/mtasa-blue/pull/1312) by **StrixG**)

- Added analog control sync for accelerate and brake_reverse ([#1164](https://github.com/multitheftauto/mtasa-blue/pull/1164) by **Addlibs**)

- Fix resetting dummies in vehicles with replaced models ([#1059](https://github.com/multitheftauto/mtasa-blue/pull/1059) by **forkerer** and **saml1er**)

- Return vector3 instead of number at ped's target ([#1379](https://github.com/multitheftauto/mtasa-blue/pull/1379) by **ecastro98**)

- Fix replaced weapon_crouch anim does not play if retainPedState is true ([#1414](https://github.com/multitheftauto/mtasa-blue/pull/1414) by **saml1er**)

- Fix nametags are interiorless ([3df58bd](https://github.com/multitheftauto/mtasa-blue/commit/3df58bd435b3c4052fa5e7fe57d534bdca7e0d2b) by **qaisjp**)

- Remove amx from the installer (See commit [7d4091f](https://github.com/multitheftauto/mtasa-blue/commit/7d4091fac6e41e6d9e199cd0a03c927dc48aac79) by **qaisjp**)

- Potential fix for vehicle dummies crash ([#1524](https://github.com/multitheftauto/mtasa-blue/pull/1524) by **saml1er**)

- Added  projectiles support for [getElementModel](mta://scripting/shared/functions/getelementmodel.md) ([#1550](https://github.com/multitheftauto/mtasa-blue/pull/1550) by **StrixG**)

- Fix getBoundKeys returning a table on empty argument ([#1615](https://github.com/multitheftauto/mtasa-blue/pull/1615) by **Tete**)

- Fix strange behavior (crashes, flickers, glitches) of Skimmer ([#1624](https://github.com/multitheftauto/mtasa-blue/pull/1624) by **ccw808**)

- Potential fixes for custom map collision crashes ([#1613](https://github.com/multitheftauto/mtasa-blue/pull/1613) by **saml1er**)

- Remove client entity check from [setPedArmor](mta://scripting/shared/functions/setpedarmor.md) ([#1638](https://github.com/multitheftauto/mtasa-blue/pull/1638) by **qaisjp**)

### 3 Vendor Updates

- Update BASS libraries ([#1551](https://github.com/multitheftauto/mtasa-blue/pull/1551) by **Dutchman101**)

- Update CEF from 76.1.13+gf19c584 (Chromium 76.0.3809.132) to 85.3.12+g3e94ebf ([Chromium 85.0.4183.121](https://chromereleases.googleblog.com/2020/09/stable-channel-update-for-desktop_21.html)) (See commit [#1698](https://github.com/multitheftauto/mtasa-blue/pull/1698) by **Jusonex** and **Dutchman101**)

- Update UnRAR from 5.71 to 5.91 ([#1606](https://github.com/multitheftauto/mtasa-blue/pull/1606) by **patrikjuvonen**)

## Server

Click to collapse [-]

### 3 New Functions

- Added [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md) and [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md) ([#826](https://github.com/multitheftauto/mtasa-blue/pull/826) by **knitz12**)

- Added [isResourceProtected](mta://scripting/server/functions/isresourceprotected.md) function ([#1254](https://github.com/multitheftauto/mtasa-blue/pull/1254) by **StrixG**)

### 10 Bug Fixes & Changes

- Fix [iprint](mta://scripting/shared/functions/iprint.md) to be able to read and output nil arguments properly ([#1064](https://github.com/multitheftauto/mtasa-blue/pull/1064) by **TheNormalnij**)

- Accept team & table of players in [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) ([#1213](https://github.com/multitheftauto/mtasa-blue/pull/1213) by **StrixG**)

- Fix /msg command duplicating when sent by Server Console ([#1411](https://github.com/multitheftauto/mtasa-blue/pull/1411) by **Dezash**)

- Make colshapes cloneable ([#1214](https://github.com/multitheftauto/mtasa-blue/pull/1214) by **StrixG**)

- Fix double chat messages if player is in team ([#1241](https://github.com/multitheftauto/mtasa-blue/pull/1241) by **StrixG** and **Luxy.c**)

- Don't queue a resource restart if resource is stopping ([#960](https://github.com/multitheftauto/mtasa-blue/pull/960) by **StrixG**)

- Added support for more map attributes ([#263](https://github.com/multitheftauto/mtasa-blue/pull/263) by **patrikjuvonen**)

- Fix server-client inconsistency for isElementAttached failure return ([866506d](https://github.com/multitheftauto/mtasa-blue/commit/866506d3f6ebe4a0d4d39664cc4e7d7c0cef1a7c) by **qaisjp**)

- Make [kickPlayer](mta://scripting/server/functions/kickplayer.md) accept the Console element as responsiblePlayer ([#1427](https://github.com/multitheftauto/mtasa-blue/pull/1427) by **qaisjp**)

- Fix stack overflow when attaching elements in maps ([#1663](https://github.com/multitheftauto/mtasa-blue/pull/1663) by **tederis**)

### 1 Vendor Update

- Update sqlite from 3.31.1 to 3.32.3 ([#1561](https://github.com/multitheftauto/mtasa-blue/pull/1561) by **patrikjuvonen**)

## Shared (*Client & Server side*)

Click to collapse [-]

### 17 New Functions

- Added [xmlLoadString](mta://scripting/shared/functions/xmlloadstring.md) ([#809](https://github.com/multitheftauto/mtasa-blue/pull/809) by **Lpsd**)

- Added request info & abort functions for [fetchRemote](mta://scripting/shared/functions/fetchremote.md)/[callRemote](mta://scripting/server/functions/callremote.md) ([#660](https://github.com/multitheftauto/mtasa-blue/pull/660) by **Luxy.c**)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- Added functions to manipulate colshapes parameters ([#1215](https://github.com/multitheftauto/mtasa-blue/pull/1215) by **StrixG**)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- Added [hasElementData](mta://scripting/shared/functions/haselementdata.md) function ([#1163](https://github.com/multitheftauto/mtasa-blue/pull/1163) by **Simi2**)

- Added element data subscription functionality ([#1055](https://github.com/multitheftauto/mtasa-blue/pull/1055) by **tederis**) - includes 3 new functions:

- [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md)

- [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)

- [hasElementDataSubscriber](mta://scripting/server/functions/haselementdatasubscriber.md)

- Adds 1 additional parameter to [setElementData](mta://scripting/shared/functions/setelementdata.md)

### 1 Deprecation

- Added deprecation message to [passwordHash](mta://scripting/shared/functions/passwordhash.md) when using custom salts ([#1208](https://github.com/multitheftauto/mtasa-blue/pull/1208) by **Luxy.c**)

### 9 Bug Fixes & Changes

- Added async [encodeString](mta://scripting/shared/functions/encodestring.md)/[decodeString](mta://scripting/shared/functions/decodestring.md) ([#1226](https://github.com/multitheftauto/mtasa-blue/pull/1226) by **StrixG**)

- Fix colshape and marker hit detection when attaching ([#1327](https://github.com/multitheftauto/mtasa-blue/pull/1327) by **Lpsd**)

- Fix driveby aiming being inverted in some cases ([#1442](https://github.com/multitheftauto/mtasa-blue/pull/1442) by **Zangomangu**)

- Added bIncludeWorldSeaLevel and bIncludeOutsideWorldLevel parameters to [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md) ([#1342](https://github.com/multitheftauto/mtasa-blue/pull/1342) by **TheNormalnij**)

- Added [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) level 4 to omit certain debug info ([#1167](https://github.com/multitheftauto/mtasa-blue/pull/1167) by **Addlibs**)

- Fix incorrect hash capitalisation ([#1527](https://github.com/multitheftauto/mtasa-blue/pull/1527) by **qaisjp**)

- Fix debugscript setting to 0 when using invalid characters ([#1602](https://github.com/multitheftauto/mtasa-blue/pull/1602) by **Unde-R**)

- Fix privilege escalation ([#1627](https://github.com/multitheftauto/mtasa-blue/pull/1627) by **ciber96**)

- Increase Lua integer formatting type from long to long long ([#1672](https://github.com/multitheftauto/mtasa-blue/pull/1672) by **sbx320**)

### 3 Vendor Updates

- Update curl from 7.68.0 to 7.72.0 ([#1562](https://github.com/multitheftauto/mtasa-blue/pull/1562) by **patrikjuvonen**)

- Update cryptopp from 8.1.0 to 8.2.0 ([#1637](https://github.com/multitheftauto/mtasa-blue/pull/1637) by **StrixG**)

- Update json-c from 0.13.1 to 0.15 ([#1605](https://github.com/multitheftauto/mtasa-blue/pull/1605) by **patrikjuvonen**)

Click to collapse [-]

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
