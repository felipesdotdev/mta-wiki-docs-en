---
doc_id: "mta-wiki:12861"
title: "Changes in 1.5.9"
source_title: "Changes in 1.5.9"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.9"
revision_id: 77044
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:10:31.434820+00:00"
---

# Changes in 1.5.9

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

1.5.9 was released on October 1, 2021.

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.5.8...1.5.9](https://github.com/multitheftauto/mtasa-blue/compare/1.5.8...1.5.9)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/7](https://github.com/multitheftauto/mtasa-blue/milestone/7)

- Resources GitHub commit log: [https://github.com/multitheftauto/mtasa-resources/compare/1.5.8...1.5.9](https://github.com/multitheftauto/mtasa-resources/compare/1.5.8...1.5.9)

- Release announcement on forums: [https://forum.mtasa.com/topic/132708-multi-theft-auto-san-andreas-159-is-released/](https://forum.mtasa.com/topic/132708-multi-theft-auto-san-andreas-159-is-released/)

## Notable Changes

Click to collapse [-]

- You can now use the new [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md) server-side event to trigger when client is ready! Thanks to Lpsd.

- You can now detect element interior or dimension change through two new client and server-side events [onElementInteriorChange](mta://scripting/server/events/onelementinteriorchange.md) and [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md) – should reduce some of your code! Thanks to Patrick and Strix.

- You can now edit element bone behavior through 7 new bone manipulation functions! Great for some dynamic animations. Get started at [setElementBonePosition](mta://scripting/client/functions/setelementboneposition.md) and [setElementBoneRotation](mta://scripting/client/functions/setelementbonerotation.md). Thanks to Saml1er.

- More vehicle customisation options! You can now edit vehicle dummy positions per vehicle. See [setVehicleDummyPosition](mta://scripting/client/functions/setvehicledummyposition.md). Thanks to botder.

- More audio customisation with sound effect parameters! See [setSoundEffectParameter](mta://scripting/client/functions/setsoundeffectparameter.md). Thanks to Strix and Sarrum.

- More client download transfer box customisation options! See for example [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md). Thanks to botder and CrosRoad95.

- You can now allocate custom objects and vehicles through [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md). One of the most sought after features in a long time. Thanks to TheNormalnij.

- You can now use scalable vector graphics (SVG) in MTA! See [svgCreate](mta://scripting/client/functions/svgcreate.md) for more info. Thanks to Lpsd.

- You can now use peds and vehicles as the camera target. Thanks to TheNormalnij.

- A lot more features for scripters to build even more immersive experiences with!

- Many synchronization improvements!

- Many varying size fixes, quality of life improvements, updates and security enhancements!

- Many default resource fixes, refactors and upgrades, including *webmap* working once again! We have also improved the detection of world objects in map editor (*editor_main* resource), so you can select many more objects that you couldn't before - such as bushes, fences and many more! You can now also remove world objects inside interiors. This should help mappers a lot.

## Backwards Compatibility

Click to collapse [-]

### 6 Backwards Incompatible Changes

These changes will take effect in **1.6.0**:

- [callRemote](mta://scripting/server/functions/callremote.md) callbacks currently set the error code to **nil** when there is no error. In 1.6.0, to be consistent with [fetchRemote](mta://scripting/shared/functions/fetchremote.md), the error code reported will be **0**. See [GitHub #294](https://github.com/multitheftauto/mtasa-blue/issues/294).

- Since July 2016 if you provide an invalid string like **"randomstring"** when a function expects a number, the string will be treated as **0** and raise a script warning. In 1.6.0 this will be an error. You will still be able to provide strings containing numbers (e.g. **"100"** and **"12.34"**), this change only affects invalid strings. See [GitHub #1043](https://github.com/multitheftauto/mtasa-blue/issues/1043).

- When providing a width and height of (0, 0) to [createBrowser](mta://scripting/client/functions/createbrowser.md) or [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md) you will encounter a script error instead of a warning. The warning was introduced Feb 2019. See [GitHub #1069](https://github.com/multitheftauto/mtasa-blue/issues/1069).

- Some functions expect only unsigned integers (positive numbers), and since Jan 2016 providing negative numbers would be a warning. This will now be an error. See [GitHub #1070](https://github.com/multitheftauto/mtasa-blue/issues/1070).

- Since Aug 2015, we replaced the custom **mtalocal://** URL scheme with **[http://mta/resourceName/blah.html](http://mta/resourceName/blah.html)**. This **mtalocal://** URL scheme will now be removed. See [GitHub #1071](https://github.com/multitheftauto/mtasa-blue/issues/1071).

- The previously unused *z* argument in [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) now calculates elements in 3D space instead of 2D space. See [GitHub #1994](https://github.com/multitheftauto/mtasa-blue/pull/1994).

This list is incomplete and we may introduce more changes later.

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-5-8.md).

- This is the **26th** 1.x.x release

- **355** days

- **49** new functions

- **16** new events

- **0** deprecations

- **77+** bug fixes and changes

- **334** commits ([see comparison](https://github.com/multitheftauto/mtasa-blue/compare/1.5.8...1.5.9))

- **189** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aopen+is%3Aissue+created%3A2020-10-11..2021-10-01))

- **81** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+milestone%3A%22Next+Release+%281.5.9%29%22))

- **135** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+closed%3A2020-10-11..2021-10-01+no%3Amilestone))

- **71** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Aopen+is%3Apr+created%3A2020-10-11..2021-10-01))

- **207** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Amerged+milestone%3A%22Next+Release+%281.5.9%29%22))

- **53** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2020-10-11..2021-10-01))

- **38** contributors of which **11** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2020-10-11&to=2021-10-01&type=c))

- **94+** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **13** vendor updates

**Note:** Last update to these statistics was made 1,759 days ago.

## Client

Click to collapse [-]

### 44 New Functions

- Added [getRoofPosition](mta://scripting/client/functions/getroofposition.md) ([#1518](https://github.com/multitheftauto/mtasa-blue/pull/1518) by **Pirulax**)

- Added [setVehicleVariant](mta://scripting/shared/functions/setvehiclevariant.md) (previously available server-side only) ([#1599](https://github.com/multitheftauto/mtasa-blue/pull/1599) by **StrixG**)

- Added [engineRestreamWorld](mta://scripting/client/functions/enginerestreamworld.md) ([#1735](https://github.com/multitheftauto/mtasa-blue/pull/1735) by **TheNormalnij**)

- Added functions to modify element bones behavior ([#1673](https://github.com/multitheftauto/mtasa-blue/pull/1673) by **Saml1er**)

- [setElementBonePosition](mta://scripting/client/functions/setelementboneposition.md)

- [setElementBoneRotation](mta://scripting/client/functions/setelementbonerotation.md)

- [getElementBonePosition](mta://scripting/client/functions/getelementboneposition.md)

- [getElementBoneRotation](mta://scripting/client/functions/getelementbonerotation.md)

- [setElementBoneMatrix](mta://scripting/client/functions/setelementbonematrix.md)

- [getElementBoneMatrix](mta://scripting/client/functions/getelementbonematrix.md)

- [updateElementRpHAnim](mta://scripting/client/functions/updateelementrphanim.md)

- Added [engineSetModelVisibleTime](mta://scripting/client/functions/enginesetmodelvisibletime.md) and [engineGetModelVisibleTime](mta://scripting/client/functions/enginegetmodelvisibletime.md) ([#1766](https://github.com/multitheftauto/mtasa-blue/pull/1766) by **TheNormalnij**)

- Added [setColorFilter](mta://scripting/client/functions/setcolorfilter.md) and [resetColorFilter](mta://scripting/client/functions/resetcolorfilter.md) ([#1611](https://github.com/multitheftauto/mtasa-blue/pull/1611) by **tederis**)

- Added [getVehicleWheelFrictionState](mta://scripting/client/functions/getvehiclewheelfrictionstate.md) ([#1839](https://github.com/multitheftauto/mtasa-blue/pull/1839) by **drop-club**)

- Added [setPedEnterVehicle](mta://scripting/client/functions/setpedentervehicle.md) and [setPedExitVehicle](mta://scripting/client/functions/setpedexitvehicle.md) ([#1748](https://github.com/multitheftauto/mtasa-blue/pull/1748) by **Zangomangu**)

- Added [setSoundLooped](mta://scripting/client/functions/setsoundlooped.md) and [isSoundLooped](mta://scripting/client/functions/issoundlooped.md) ([#657](https://github.com/multitheftauto/mtasa-blue/pull/657) by **FileEX**)

- Added [isTransferBoxAlwaysVisible](mta://scripting/client/functions/istransferboxalwaysvisible.md) ([#1955](https://github.com/multitheftauto/mtasa-blue/pull/1955) by **botder** and **CrosRoad95**)

- Added vehicle dependent dummy positions with functions ([#1982](https://github.com/multitheftauto/mtasa-blue/pull/1982) by **botder**)

- [getVehicleDummyPosition](mta://scripting/client/functions/getvehicledummyposition.md)

- [getVehicleModelDummyDefaultPosition](mta://scripting/client/functions/getvehiclemodeldummydefaultposition.md)

- [setVehicleDummyPosition](mta://scripting/client/functions/setvehicledummyposition.md)

- [resetVehicleDummyPositions](mta://scripting/client/functions/resetvehicledummypositions.md)

- Added [isBrowserRenderingPaused](mta://scripting/client/functions/isbrowserrenderingpaused.md) ([#1999](https://github.com/multitheftauto/mtasa-blue/pull/1999) by **cleoppa**)

- Added [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md) ([#2023](https://github.com/multitheftauto/mtasa-blue/pull/2023) by **cleoppa**)

- Added [showCol](mta://scripting/client/functions/showcol.md), [isShowCollisionsEnabled](mta://scripting/client/functions/isshowcollisionsenabled.md), [showSound](mta://scripting/client/functions/showsound.md) and [isShowSoundEnabled](mta://scripting/client/functions/isshowsoundenabled.md) ([#2025](https://github.com/multitheftauto/mtasa-blue/pull/2025) by **cleoppa**)

- Added [clearDebugBox](mta://scripting/client/functions/cleardebugbox.md) ([#2160](https://github.com/multitheftauto/mtasa-blue/pull/2160) by **cleoppa**)

- Added [isChatInputBlocked](mta://scripting/client/functions/ischatinputblocked.md) ([#2170](https://github.com/multitheftauto/mtasa-blue/pull/2170) by **Pieter-Dewachter**)

- Added [engineStreamingGetUsedMemory](mta://scripting/client/functions/enginestreaminggetusedmemory.md) ([#2269](https://github.com/multitheftauto/mtasa-blue/pull/2269) by **Pirulax**)

- Added [engineStreamingFreeUpMemory](mta://scripting/client/functions/enginestreamingfreeupmemory.md) ([#2268](https://github.com/multitheftauto/mtasa-blue/pull/2268) by **Pirulax**)

- Added [setSoundEffectParameter](mta://scripting/client/functions/setsoundeffectparameter.md) and [getSoundEffectParameters](mta://scripting/client/functions/getsoundeffectparameters.md) ([449c5c3](https://github.com/multitheftauto/mtasa-blue/commit/449c5c329732d77ea36ce0abc9595f1577dd1304) by **StrixG**)

- Added [setPedBleeding](mta://scripting/client/functions/setpedbleeding.md) and [isPedBleeding](mta://scripting/client/functions/ispedbleeding.md) ([#2308](https://github.com/multitheftauto/mtasa-blue/pull/2308) and [#2365](https://github.com/multitheftauto/mtasa-blue/pull/2365) by **StrixG** and **theSarrum**)

- Added [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md) ([#2315](https://github.com/multitheftauto/mtasa-blue/pull/2315) by **theSarrum**)

- Added new SVG functions ([#2026](https://github.com/multitheftauto/mtasa-blue/pull/2026) by **Lpsd**)

- [svgCreate](mta://scripting/client/functions/svgcreate.md)

- [svgGetDocumentXML](mta://scripting/client/functions/svggetdocumentxml.md)

- [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)

- [svgGetSize](mta://scripting/client/functions/svggetsize.md)

- [svgSetSize](mta://scripting/client/functions/svgsetsize.md)

### 10 New Events

- Added [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md) ([#1673](https://github.com/multitheftauto/mtasa-blue/pull/1673) by **Saml1er**)

- Added [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md) ([#1553](https://github.com/multitheftauto/mtasa-blue/pull/1553) by **StrixG**)

- Added [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md) and [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md) ([#1748](https://github.com/multitheftauto/mtasa-blue/pull/1748) by **Zangomangu**)

- Added [onClientResourceFileDownload](mta://scripting/client/events/onclientresourcefiledownload.md), [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md) and [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md) ([#1955](https://github.com/multitheftauto/mtasa-blue/pull/1955) by **botder** and **CrosRoad95**)

- Added [onClientObjectMoveStart](mta://scripting/client/events/onclientobjectmovestart.md) and [onClientObjectMoveStop](mta://scripting/client/events/onclientobjectmovestop.md) ([#2023](https://github.com/multitheftauto/mtasa-blue/pull/2023) by **cleoppa**)

- Added [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md) ([#2058](https://github.com/multitheftauto/mtasa-blue/pull/2058) by **Patrick2562**)

### 8 New Arguments & Parameters

- Added *macros* argument to [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md) ([#1573](https://github.com/multitheftauto/mtasa-blue/pull/1573) by **tederis**)

- Added *forceOverrideNextFrame* argument to [setAnalogControlState](mta://scripting/client/functions/setanalogcontrolstate.md) ([#1852](https://github.com/multitheftauto/mtasa-blue/pull/1852) by **LosFaul**)

- Added *interior* and *dimension* arguments to [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) ([#1915](https://github.com/multitheftauto/mtasa-blue/pull/1915) by **Pirulax**)

- Added *pedCameraMode* argument to [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md) ([#1418](https://github.com/multitheftauto/mtasa-blue/pull/1418) by **TheNormalnij**)

- Added *flipUV* argument to [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md) and [dxDrawMaterialSectionLine3D](mta://scripting/client/functions/dxdrawmaterialsectionline3d.md) ([#2193](https://github.com/multitheftauto/mtasa-blue/pull/2193) by **tederis**)

- Added *messageType* parameter to [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md) ([#1020](https://github.com/multitheftauto/mtasa-blue/pull/1020) by **Lpsd**)

- Added *lineHeight* argument to [dxDrawText](mta://scripting/client/functions/dxdrawtext.md) ([#2355](https://github.com/multitheftauto/mtasa-blue/pull/2355) by **Allerek**)

### 40 Bug Fixes & Changes

- Fixed crash when deleting a chatbox bind too early ([be57711](https://github.com/multitheftauto/mtasa-blue/commit/be577116f191526111e06487c8322c7799e03564) by **sbx320**)

- Added minimum version check for [resetBlurLevel](mta://scripting/client/functions/resetblurlevel.md) ([#1755](https://github.com/multitheftauto/mtasa-blue/pull/1755) by **StrixG**)

- Included skins added through [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) in [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md) ([#1437](https://github.com/multitheftauto/mtasa-blue/pull/1437) by **Pirulax**)

- Allow allocating new object models using [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([#1684](https://github.com/multitheftauto/mtasa-blue/pull/1684) by **TheNormalnij**)

- Allow allocating new vehicle models using [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([#1701](https://github.com/multitheftauto/mtasa-blue/pull/1701) by **TheNormalnij**)

- Events [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md), [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md), [onClientVehicleStartExit](mta://scripting/client/events/onclientvehiclestartexit.md) and [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md) now return [peds](mta://reference/misc/ped.md) as well ([#1748](https://github.com/multitheftauto/mtasa-blue/pull/1748) by **Zangomangu**)

- Fixed hectic bike rotation by filling CBikeSAInterface class ([#1884](https://github.com/multitheftauto/mtasa-blue/pull/1884) by **TheNormalnij**)

- Fixed [Sound.setPanningEnabled](mta://scripting/client/functions/setsoundpanningenabled.md) OOP-method not working due to typo in definition ([#1923](https://github.com/multitheftauto/mtasa-blue/pull/1923) by **StrixG**)

- Fixed ped task bug when special fighting near to a vehicle causing abnormal behavior ([#1943](https://github.com/multitheftauto/mtasa-blue/pull/1943) by **Zangomangu**)

- Fixed [getKeyState](mta://scripting/client/functions/getkeystate.md) not working with gamepad buttons ([#1944](https://github.com/multitheftauto/mtasa-blue/pull/1944) by **botder**)

- Disable gamepad controls if disabled by [showCursor](mta://scripting/shared/functions/showcursor.md) ([c4b9a84](https://github.com/multitheftauto/mtasa-blue/commit/c4b9a844c3dc8f8fd16776370dcdac12f189d32f) by **botder**)

- Keep console position and size when changing locale ([#1970](https://github.com/multitheftauto/mtasa-blue/pull/1970) by **xLuxy**)

- Fixed network trouble if falling into water while attempting to enter a vehicle ([#1986](https://github.com/multitheftauto/mtasa-blue/pull/1986) by **Zangomangu**)

- Abort vehicle entering for incompatible vehicles if ped is in water ([b3ba15b](https://github.com/multitheftauto/mtasa-blue/commit/b3ba15bad3a0943d83cefb90cddc6f9191667fa8) by **botder**)

- Lowered shadows and lights more towards ground level ([#2018](https://github.com/multitheftauto/mtasa-blue/pull/2018) by **patrikjuvonen** and **botder**)

- Fixed objects not returning world model position in [processLineOfSight](mta://scripting/client/functions/processlineofsight.md) ([#2083](https://github.com/multitheftauto/mtasa-blue/pull/2083) by **STR6**)

- Added keybind queue to improve performance ([#2123](https://github.com/multitheftauto/mtasa-blue/pull/2123) by **patrikjuvonen**)

- Added ped camera mode return value to [getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md) ([#1418](https://github.com/multitheftauto/mtasa-blue/pull/1418) by **TheNormalnij**)

- Fixed [setMarkerType](mta://scripting/shared/functions/setmarkertype.md) resetting marker position ([586d6d](https://github.com/multitheftauto/mtasa-blue/commit/586d6d6fa202de43e633c20f757e2b1282529106) by **botder**)

- Fixed [testLineAgainstWater](mta://scripting/client/functions/testlineagainstwater.md) working incorrectly outside of game boundaries ([#2192](https://github.com/multitheftauto/mtasa-blue/pull/2192) by **Allerek**)

- Fixed client vehicles blocking entry to server vehicle ([#2188](https://github.com/multitheftauto/mtasa-blue/pull/2188) by **Zangomangu**)

- Removed obsolete entry from forbodenList ([ff93fec](https://github.com/multitheftauto/mtasa-blue/commit/ff93fec93cb20c25577950c47bc22c0f9730a459) by **Dutchman101**)

- Reset vehicle explosion timer in CVehicleSA::SetHealth ([8b30d7a](https://github.com/multitheftauto/mtasa-blue/commit/8b30d7a4e43e6460a8203bb89b7133365a3e6a85) and [546beab](https://github.com/multitheftauto/mtasa-blue/commit/546beabf70a896ccf87c3138f028e8ef34f84c7d) by **botder**)

- Set game thread affinity to first CPU core ([dbc792b](https://github.com/multitheftauto/mtasa-blue/commit/dbc792b3d433378217c96b6b1418a21888ed1d5a) by **botder**)

- Added "TotalPhysicalMemory" to [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md) ([#2265](https://github.com/multitheftauto/mtasa-blue/pull/2265) by **Pirulax**)

- Added a UI button to delete servers from the "Recent" tab ([#2253](https://github.com/multitheftauto/mtasa-blue/pull/2253) by **iDannz1**)

- Trim keybind whitespace to avoid duplicates ([#2124](https://github.com/multitheftauto/mtasa-blue/pull/2124) by **patrikjuvonen**)

- Fixed a typo in the sa.dat file ([eff97c8](https://github.com/multitheftauto/mtasa-blue/commit/eff97c8ad3e725691d182c239997caeca51eba4d) by **ccw808**)

- Resolved remaining collisionless objects ([#2296](https://github.com/multitheftauto/mtasa-blue/pull/2296) by **Saml1er**, **TheNormalnij**, **ccw808**, **thisdp** and **botder**)

- Fixed attached players desync after reconnect ([#2290](https://github.com/multitheftauto/mtasa-blue/pull/2290) by **theSarrum**)

- Check clothes type parameter in several cases ([ce9d3de](https://github.com/multitheftauto/mtasa-blue/commit/ce9d3deab8ec7905264b3492bf11d3565ee5c149) by **Inder00** and **botder**)

- Updated some images ([f00c1a3](https://github.com/multitheftauto/mtasa-blue/commit/f00c1a38934b28eff8201708dd4b956272d27f13) by **patrikjuvonen**)

- Set CEF cache path ([adff688](https://github.com/multitheftauto/mtasa-blue/commit/adff688e77c16d0c5a63e047b60da97529f2b111) by **patrikjuvonen**)

- Fixed some capital letters not working in CEF ([6ed00b3](https://github.com/multitheftauto/mtasa-blue/commit/6ed00b324a980d43c342d87916d1a78bfd352d86) by **patrikjuvonen** and **botder**)

- Fixed domain permission window labels overflowing in some languages ([f7dcd6f](https://github.com/multitheftauto/mtasa-blue/commit/f7dcd6f249a367ddb9b81b07bea35b4fcb6145ee) by **patrikjuvonen**)

- Updated client translations ([6db5ba4](https://github.com/multitheftauto/mtasa-blue/commit/6db5ba4454a7f764871aae561b17898fd4e82318) by **patrikjuvonen**)

- Updated credits ([#2125](https://github.com/multitheftauto/mtasa-blue/pull/2125) by **patrikjuvonen**)

### 7 Vendor Updates

- Updated and replaced CEGUI-integrated [FreeType](https://www.freetype.org/) by adding it as its own dependency ([def86d0](https://github.com/multitheftauto/mtasa-blue/commit/def86d01971d84522803052f68374a92bd68fad4) and [2b70f96](https://github.com/multitheftauto/mtasa-blue/commit/2b70f96da7e4fb07effc371929e7e8f6297b8105) by **Jusonex**)

- Updated libjpeg from 9b to 9d ([#1963](https://github.com/multitheftauto/mtasa-blue/pull/1963) by **patrikjuvonen**)

- Updated Unifont from 5.1 to 13.0.06 ([8eeac9a](https://github.com/multitheftauto/mtasa-blue/commit/8eeac9a6465b2d6af7055cab01eb24beb72b8d2d) by **patrikjuvonen**)

- Updated BASS libraries ([#2377](https://github.com/multitheftauto/mtasa-blue/pull/2377) by **Dutchman101**)

- Updated CEF from 85.3.12+g3e94ebf (Chromium 85.0.4183.121) to 94.4.2+g6a963ca ([Chromium 94.0.4606.61](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_24.html)) (See commit [ae6caa9](https://github.com/multitheftauto/mtasa-blue/commit/ae6caa92c81b37ca29c7af0fbb7dffb4c57b14b6) by **patrikjuvonen**)

- Added lunasvg 2.3.0 ([#2026](https://github.com/multitheftauto/mtasa-blue/pull/2026) by **Lpsd**)

- Updated unrar from 5.91 to 6.02 ([#2384](https://github.com/multitheftauto/mtasa-blue/pull/2384) by **patrikjuvonen**)

## Server

Click to collapse [-]

### 6 New Events

- Added [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md) ([#1553](https://github.com/multitheftauto/mtasa-blue/pull/1553) by **StrixG**)

- Added [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md) and [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md) ([#1748](https://github.com/multitheftauto/mtasa-blue/pull/1748) by **Zangomangu**)

- Added [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md) ([#1651](https://github.com/multitheftauto/mtasa-blue/pull/1651) by **TeteX1**)

- Added [onElementInteriorChange](mta://scripting/server/events/onelementinteriorchange.md) ([#2058](https://github.com/multitheftauto/mtasa-blue/pull/2058) by **Patrick2562**)

- Added [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md) ([#2150](https://github.com/multitheftauto/mtasa-blue/pull/2150) by **Lpsd**)

### New Arguments & Parameters

- Added *exitCode* to [shutdown](mta://scripting/server/functions/shutdown.md) ([#2298](https://github.com/multitheftauto/mtasa-blue/pull/2298) by **botder**)

### 16 Bug Fixes & Changes

- Fixed wrong SQLite column in [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md) ([#1734](https://github.com/multitheftauto/mtasa-blue/pull/1734) by **emre1702**)

- Improved *help* command in server console ([#1639](https://github.com/multitheftauto/mtasa-blue/pull/1639) by **Unde-R**)

- Improved checksum error messages for internal HTTP servers ([#1778](https://github.com/multitheftauto/mtasa-blue/pull/1778) by **qaisjp**)

- Events [onVehicleStartEnter](mta://scripting/server/events/onvehiclestartenter.md), [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md), [onVehicleStartExit](mta://scripting/server/events/onvehiclestartexit.md) and [onVehicleExit](mta://scripting/server/events/onvehicleexit.md) now return [peds](mta://reference/misc/ped.md) as well ([#1748](https://github.com/multitheftauto/mtasa-blue/pull/1748) by **Zangomangu**)

- Fixed CLuaArgument not comparing tables recursively, causing unnecessary [setElementData](mta://scripting/shared/functions/setelementdata.md) resyncs even if values match ([76e52f8](https://github.com/multitheftauto/mtasa-blue/commit/76e52f820e4dadce75df6de0ea3378d02cc1bbb5) by **botder**)

- Enforce existing username length limit in account code ([#1995](https://github.com/multitheftauto/mtasa-blue/pull/1995) by **patrikjuvonen**)

- Refactored vehicle blowup code to fix [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md) triggering twice server-side ([#1997](https://github.com/multitheftauto/mtasa-blue/pull/1997) by **botder**)

- Added source map compatibility in CResourceHTMLItem ([#2207](https://github.com/multitheftauto/mtasa-blue/pull/2207) by **PauloKim1246**)

- Added missing [ColShape.elementsWithin](mta://scripting/shared/functions/getelementswithincolshape.md) ([#2186](https://github.com/multitheftauto/mtasa-blue/pull/2186) by **Pirulax**)

- Fixed info command displaying two statuses of a running resource ([#2292](https://github.com/multitheftauto/mtasa-blue/pull/2292) by **theSarrum**)

- Fixed respawning of blown vehicles ([7963997](https://github.com/multitheftauto/mtasa-blue/commit/796399704b1e0a2147bb7ba52ea95c34245ceebe) by **botder**)

- Don't allow dead peds to enter vehicles ([#2344](https://github.com/multitheftauto/mtasa-blue/pull/2344) by **Zangomangu**)

- Fixed missing new lines when outputting long messages in server console ([6256bb0](https://github.com/multitheftauto/mtasa-blue/commit/6256bb05ea752d2e2f406c516448ae948f493c79) by **patrikjuvonen**)

### 1 Vendor Update

- Updated sqlite from 3.32.3 to 3.36.0 ([#2284](https://github.com/multitheftauto/mtasa-blue/pull/2284) by **patrikjuvonen**)

## Shared (*Client & Server*)

Click to collapse [-]

### 5 New Functions

- Added transfer box customization functions [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md) and [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md) ([#1955](https://github.com/multitheftauto/mtasa-blue/pull/1955) by **botder** and **CrosRoad95**)

- Added [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md) and [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md) ([#1908](https://github.com/multitheftauto/mtasa-blue/pull/1908) by **CrosRoad95**)

- Added *intersectsSegmentTriangle* method to [Vector3](mta://reference/misc/vector3.md) ([#1711](https://github.com/multitheftauto/mtasa-blue/pull/1711) by **Pirulax**)

### 3 New Arguments & Parameters

- Added *bIncludeWorldSeaLevel* and *bIncludeOutsideWorldLevel* to [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md) ([#1402](https://github.com/multitheftauto/mtasa-blue/pull/1402) by **TheNormalnij**)

- Added new optional *inputBlocked* argument for [showChat](mta://scripting/shared/functions/showchat.md) ([#2170](https://github.com/multitheftauto/mtasa-blue/pull/2170) by **Pieter-Dewachter**)

### 9 Bug Fixes & Changes

- Fixed vehicle driver desynchronization after carjacker dies ([#1907](https://github.com/multitheftauto/mtasa-blue/pull/1907) by **Zangomangu**)

- Disabled train track functions ([#1920](https://github.com/multitheftauto/mtasa-blue/pull/1920) by **qaisjp**)

- Added request body and method to HTTP scripts ([#2053](https://github.com/multitheftauto/mtasa-blue/pull/2053) by **Disinterpreter**)

- Added aes128 encryption support to [encodeString](mta://scripting/shared/functions/encodestring.md) and [decodeString](mta://scripting/shared/functions/decodestring.md) ([#2235](https://github.com/multitheftauto/mtasa-blue/pull/2235) by **drop-club**)

- Fixed empty files returning an invalid checksum ([966de4e](https://github.com/multitheftauto/mtasa-blue/commit/966de4e209b4ce6b3e4e6a7ea0f53650038a049c) by **botder**)

- Added extra checks in CXMLImpl::ParseString to avoid crash when invalid XML data supplied ([#2282](https://github.com/multitheftauto/mtasa-blue/pull/2282) by **Lpsd**)

- Added ability to use peds and vehicles as a camera target using [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md) ([#1753](https://github.com/multitheftauto/mtasa-blue/pull/1753) by **TheNormalnij**)

### 5 Vendor Updates

- Updated detours from 1.2 to 4.0.1 ([#2022](https://github.com/multitheftauto/mtasa-blue/pull/2022) by **botder**)

- Updated mbedtls from 2.4.2 to 2.27.0 ([#2085](https://github.com/multitheftauto/mtasa-blue/pull/2085) and [38e9207](https://github.com/multitheftauto/mtasa-blue/commit/38e92079643779a0a1ef3b25ca5cfb4c99be2e52) by **botder** and **patrikjuvonen**)

- Updated curl from 7.72.0 to 7.79.1 ([#2373](https://github.com/multitheftauto/mtasa-blue/pull/2373) by **patrikjuvonen**)

- Updated pcre from 8.39 to 8.45 ([7d51758](https://github.com/multitheftauto/mtasa-blue/commit/7d517586c71a940f52cfa5ee1443b628882c9eed) by **patrikjuvonen**)

- Updated cryptopp from 8.2.0 to 8.6.0 ([#2385](https://github.com/multitheftauto/mtasa-blue/pull/2385) by **patrikjuvonen**)

## Resources

### 37+ Bug Fixes & Changes

- [admin] added an option to hide sensitive data. (works like streamer mode in some apps) (thanks to iDannz)

- [admin] added an option make the camera collide while spectate. (thanks to iDannz)

- [admin] added a command to send messages in admin chat (/a message). (thanks to rickchesterhd123)

- [admin] added an option to teleport to the selected position on the map. (thanks to Patrick2562)

- [admin] added save to some infos, so you don't have to reselect some options after reconnecting. (thanks to iDannz)

- [admin] fixed error in output messages (case the player has a nickname with more than 1 hex color). (thanks to androksi)

- [admin] fixed a bug that occurred when trying to restart a resource that wasn't running. (thanks to Dante386)

- [admin] fixed an error that occurred when clicking on the "Maps" tab if the resource 'mapmanager' was not running. (thanks to cleoppa and iDannz)

- [admin] improved the lists of 'give vehicle', 'give weapon' and 'slap'. (thanks to iDannz)

- [admin] replace 'give admin' button with permissions selection widget. (thanks to iDannz)

- [admin] tweaks to the interface. (thanks to iDannz)

- [cdm] removed the cdm resource from the official resources package.

- [editor] added an option to 'lock' elements. (thanks to xLive)

- [editor] added an option to choose the output directory before saving new maps. (thanks to umithyo, xLive and iDannz)

- [editor] added option to select some objects that do not have collisions. (thanks to Zangomangu and Tut)

- [editor] fixed an issue that occurred when saving element's dimension. (thanks to FileEX)

- [editor] fixed bug that made the camera be locked after clicking some buttons too fast. (thanks to androksi and iDannz)

- [editor] interior world models are now removable. (thanks to Zangomango)

- [freeroam] fixed an error in the command '/addclothes'. (thanks to xLive)

- [freeroam] fixed error when using negative numbers in the command '/color'. (thanks to xLive)

- [freeroam] improved the map image quality. (thanks to patrikjuvonen)

- [hedit] resource added to the official resources package.

- [ipb] fixed filter input-box that did not work. (thanks to iDannz)

- [killmessages] rewritten resource. (now detects deaths caused by vehicles (eg hydra), and also detects deaths caused by vehicle explosions). (thanks to iDannz)

- [mapcycler] added an option to pause cycling while the server is empty. (thanks to jlillis)

- [race] added configuration of transparency level during the ghost mode. (thanks to AfuSensi)

- [race] added fade car addon. (thanks to AfuSensi)

- [race] fix bug in pickup respawn. (thanks to LosFaul)

- [race] finish the map when there are only spectators. (thanks to xLive)

- [race] added possibility to use rotation attributes. (thanks to xLive)

- [resourcemanager] fixed problems on the dates of some information. (thanks to Dezash)

- [runcode] fixed a problem that caused the 'srun' command show the results to everyone. (thanks to Yamsha75)

- [speedometer] resource added to the official resources package.

- [trainhorn] resource added to the official resources package.

- [webmap] fixed and updated. (thanks to patrikjuvonen)

- [webstats] updated. (thanks to patrikjuvonen)

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
