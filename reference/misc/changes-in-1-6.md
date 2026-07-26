---
doc_id: "mta-wiki:12210"
title: "Changes in 1.6"
source_title: "Changes in 1.6"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.6"
revision_id: 82817
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:10:31.682045+00:00"
---

# Changes in 1.6

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

1.6.0 was released on June 16, 2023. Beta was initially released on April 7, 2023.

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.5.9...1.6.0](https://github.com/multitheftauto/mtasa-blue/compare/1.5.9...1.6.0)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/9](https://github.com/multitheftauto/mtasa-blue/milestone/9)

- Resources GitHub commit log: [https://github.com/multitheftauto/mtasa-resources/compare/1.5.9...1.6.0](https://github.com/multitheftauto/mtasa-resources/compare/1.5.9...1.6.0)

- Pre-release announcement on forums: [https://forum.multitheftauto.com/topic/140285-multi-theft-auto-san-andreas-16-is-ready-for-testing/](https://forum.multitheftauto.com/topic/140285-multi-theft-auto-san-andreas-16-is-ready-for-testing/)

- Release announcement on forums: [https://forum.multitheftauto.com/topic/140935-multi-theft-auto-san-andreas-16-is-released/](https://forum.multitheftauto.com/topic/140935-multi-theft-auto-san-andreas-16-is-released/)

## Important notice to Windows 7 and 8.x users

If you are using Windows 7 or 8.x, please upgrade your system to Windows 10 or 11 as soon as possible. Windows 7 and 8.x are no longer supported by Microsoft (since January 2020 and January 2023 respectively) and most software (including Google Chrome and Steam) which means you are running an insecure system. Multi Theft Auto will also eventually drop Windows 7 and 8.x support sometime in the future, so it would be a good idea to start looking at upgrade options right now. Thank you!

**CEF in MTA is no longer updated for Windows 7 or 8.x. This is because CEF no longer supports those versions of Windows. This is bad for security, so please upgrade to Windows 10+ and MTA to 1.6+**

## 12 Backwards Incompatible Changes

These changes will take effect in this version and scripts may need to be manually upgraded when updating:

- Bloodring Banger (504) is now defined as doorless, to fix animations to be consistent with single player, this also causes [setVehicleLocked](mta://scripting/shared/functions/setvehiclelocked.md) to not lock the vehicle anymore, as entry happens through the window.

- [callRemote](mta://scripting/server/functions/callremote.md) callbacks currently set the error code to *nil* when there is no error. In this version, to be consistent with [fetchRemote](mta://scripting/shared/functions/fetchremote.md), the error code reported will be **0** ([#294](https://github.com/multitheftauto/mtasa-blue/issues/294)).

- Since Aug 2015, we replaced the custom *mtalocal://* URL scheme with **[http://mta/resourceName/blah.html](http://mta/resourceName/blah.html)**. The *mtalocal://* URL scheme will now be removed ([#1071](https://github.com/multitheftauto/mtasa-blue/issues/1071)).

- Since Jul 2016 if you provide an invalid string like *"randomstring"* when a function expects a number, the string will be treated as **0** and raise a script warning. This will be now an error. You will still be able to provide strings containing numbers (e.g. *"100"* and *"12.34"*), this change only affects invalid strings ([#1043](https://github.com/multitheftauto/mtasa-blue/issues/1043)).

- Some functions expect only unsigned integers (positive numbers), and since Jan 2016 providing negative numbers would be a warning. This will now be an error ([#1070](https://github.com/multitheftauto/mtasa-blue/issues/1070)).

- When providing a width and height of *(0, 0)* to [createBrowser](mta://scripting/client/functions/createbrowser.md) or [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md) you will encounter a script error instead of a warning, introduced in Feb 2019 ([#1069](https://github.com/multitheftauto/mtasa-blue/issues/1069)).

- The previously unused *z* argument in [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) now calculates elements in 3D space instead of 2D space ([#1994](https://github.com/multitheftauto/mtasa-blue/pull/1994)).

- Flamethrower ammo is no longer multiplied by 10 ([#481](https://github.com/multitheftauto/mtasa-blue/issues/481)).

- Server-side [createBlip](mta://scripting/shared/functions/createblip.md) now syncs blip size and color regardless of icon ID, previously only icon ID 0 had its size and color synced to clients ([#1399](https://github.com/multitheftauto/mtasa-blue/issues/1399)).

- Server-side [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md) and [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md) cap has been raised from 99.999.999 (8 digits) to 999.999.999 (9 digits) to match the maximum native UI value ([#2654](https://github.com/multitheftauto/mtasa-blue/issues/2654)).

- Players are now synced when exiting vehicle ([#2084](https://github.com/multitheftauto/mtasa-blue/pull/2084)).

- Server-side objects that were unbreakable by default, but would have been breakable client-side by default, are now breakable by default also server-side ([commit](https://github.com/multitheftauto/mtasa-blue/compare/d701fbe15b4cece7a6cd6242c3819e68deb7aae2...57d5be3d3e323394a8926a79f3da9cd3814e44a2)).

## 5 Deprecations

These changes will take effect in this version and scripts may need to be manually upgraded when updating:

- Changed [getCameraShakeLevel](mta://scripting/client/functions/getcamerashakelevel.md), [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md) to throw a warning on use, please upgrade to [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md) and [setCameraDrunkLevel](mta://scripting/client/functions/setcameradrunklevel.md) instead ([2651903](https://github.com/multitheftauto/mtasa-blue/commit/2651903e6a03c78a0571089b142b175f11f41bab) by **Unde-R**)

- Changed [givePedJetPack](mta://scripting/server/functions/givepedjetpack.md), [removePedJetPack](mta://scripting/server/functions/removepedjetpack.md) and [doesPedHaveJetPack](mta://scripting/shared/functions/doespedhavejetpack.md) to throw a warning on use, please upgrade to [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md) and [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md) instead ([804c66b](https://github.com/multitheftauto/mtasa-blue/commit/804c66b88e0324eb6b2d9c83fdf7606ba05566c6) by **qaisjp**)

## Notable Changes

This update is primarily focused on fixes and changes rather than new features, but there are a lot of features planned for the next release!

- Many high FPS related inconsistency issues have been fixed by Merlin!

- Script support for custom IMG containers, and ability to set model flags. Thanks to TheNormalnij!

- A number of graphical effects

- Added support for vehicle sun glare effect. Thanks to gta191977649 and TheNormalnij.

- Added corona rain reflections. Thanks to lopezloo.

- Added big sun lens flare effect. Thanks to gta191977649.

- Added dynamic ped shadows. Thanks to lopezloo.

- Grass should now render correctly. Thanks to TFP-dev.

- ARM support for MTA server is here! This support should still considered experimental. Thanks to botder.

- Added new *Default 2023*, *GWEN Blue* and *GWEN Orange* GUI skins. Thanks to Haxardous.

- Added missing GTA special [character skins](mta://reference/misc/character-skins.md) (3, 4, 5, 6, 8, 42, 65, 86, 119, 273, 289). Thanks to Allerek.

- Pictures taken with the camera weapon are now saved in higher quality. Thanks to lopezloo.

- Many stability improvements

- Many synchronization improvements

- Many varying size fixes, quality of life improvements, updates and security enhancements to both core and resources!

- Updates to all language translations from our [Crowdin](https://multitheftauto.crowdin.com)

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-5-9.md).

- This is the **27th** 1.x.x release

- **623** days of which **553** for beta release

- **12** backwards incompatible changes

- **26** new functions

- **1** new event

- **5** deprecations

- **289+** bug fixes and changes

- **956+** commits ([mtasa-blue](https://github.com/multitheftauto/mtasa-blue/compare/1.5.9...1.6.0))  ([mtasa-resources](https://github.com/multitheftauto/mtasa-resources/compare/1.5.9...1.6.0))

- **199** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aopen+is%3Aissue+created%3A2021-10-01..2023-06-16))

- **102** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+milestone%3A%221.6.0%22))

- **92** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+closed%3A2021-10-01..2023-06-16+no%3Amilestone+-label%3Ainvalid))

- **44** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Aopen+is%3Apr+created%3A2021-10-01..2023-06-16))

- **219** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Amerged+milestone%3A%221.6.0%22))

- **107** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2021-10-01..2023-06-16))

- **45+** contributors of which **17+** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2021-10-01&to=2023-06-16&type=c))

- **100+** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **23** vendor updates

**Note:** Last update to these statistics was made 1,135 days ago.

## 15 New Features

### Shared

- Added RSA support on [encodeString](mta://scripting/shared/functions/encodestring.md), along with a new function ([e7e3ba5](https://github.com/multitheftauto/mtasa-blue/commit/e7e3ba5b337f791203ef977bd083a28226614da7), [39bc23f](https://github.com/multitheftauto/mtasa-blue/commit/39bc23f136d82a4849a7b09edfa65fc927b52acc) and [83185ef](https://github.com/multitheftauto/mtasa-blue/commit/83185ef2fbc1ee086cc7acb1a97b4b15bf939a88) by **Inder00**, **Pirulax** and **TheNormalnij**)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- Added HMAC support on [encodeString](mta://scripting/shared/functions/encodestring.md) ([eebf228](https://github.com/multitheftauto/mtasa-blue/commit/eebf228224860eed030d59d629e905dc9a79b13c) by **Inder00**)

- Added [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md) ([dd571b4](https://github.com/multitheftauto/mtasa-blue/commit/dd571b4793ac6773c634a1cdc6b28bfa00891127) by **botder**)

### Client

- Added support for loading custom IMG containers ([075dfee](https://github.com/multitheftauto/mtasa-blue/commit/075dfeeac88ddf52063f9ec38a68669ce7c9a948) by **TheNormalnij**)

- [engineLoadIMG](mta://scripting/client/functions/engineloadimg.md)

- [engineImageLinkDFF](mta://scripting/client/functions/engineimagelinkdff.md)

- [engineImageLinkTXD](mta://scripting/client/functions/engineimagelinktxd.md)

- [engineRestoreDFFImage](mta://scripting/client/functions/enginerestoredffimage.md)

- [engineRestoreTXDImage](mta://scripting/client/functions/enginerestoretxdimage.md)

- [engineAddImage](mta://scripting/client/functions/engineaddimage.md)

- [engineRemoveImage](mta://scripting/client/functions/engineremoveimage.md)

- [engineImageGetFilesCount](mta://scripting/client/functions/engineimagegetfilescount.md)

- [engineImageGetFiles](mta://scripting/client/functions/engineimagegetfiles.md)

- [engineImageGetFile](mta://scripting/client/functions/engineimagegetfile.md)

- [engineGetModelTXDID](mta://scripting/client/functions/enginegetmodeltxdid.md)

- Added support for model flags ([ec314df](https://github.com/multitheftauto/mtasa-blue/commit/ec314df0362829ed52a52aa3ac0b1302c2097c3a) by **TheNormalnij**)

- [engineSetModelFlags](mta://scripting/client/functions/enginesetmodelflags.md)

- [engineGetModelFlags](mta://scripting/client/functions/enginegetmodelflags.md)

- [engineResetModelFlags](mta://scripting/client/functions/engineresetmodelflags.md)

- [engineGetModelFlag](mta://scripting/client/functions/enginegetmodelflag.md)

- [engineSetModelFlag](mta://scripting/client/functions/enginesetmodelflag.md)

- Added vehicle sun glare effect to [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) and [isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md) ([1fac287](https://github.com/multitheftauto/mtasa-blue/commit/1fac28795ece272f0a7fe0b697c793b315ac3459) by **gta191977649** and **TheNormalnij** and [3068896](https://github.com/multitheftauto/mtasa-blue/commit/3068896767976610332272a35ceda28fd33bb75f) and [da49960](https://github.com/multitheftauto/mtasa-blue/commit/da49960feb6651e1cb6efb8a63408eb8ad89c30e) by **gta191977649**)

- Added support for WebM files to [playSound](mta://scripting/client/functions/playsound.md) and [playSound3D](mta://scripting/client/functions/playsound3d.md) ([545a22a](https://github.com/multitheftauto/mtasa-blue/commit/545a22a531b9f4eee01e3d502cbb38b0d95b4c4f) by **theSarrum**)

- Added corona rain reflections ([c4caa4b](https://github.com/multitheftauto/mtasa-blue/commit/c4caa4b7e82291aca67056fc0f2e9835322f7db9) by **lopezloo**)

- Added [isCapsLockEnabled](mta://scripting/client/functions/iscapslockenabled.md) function ([e84a15e](https://github.com/multitheftauto/mtasa-blue/commit/e84a15e1ea4d47769e14917243ddb2eac54ae5ee) by **Lpsd**)

- Added [isMTAWindowFocused](mta://scripting/client/functions/ismtawindowfocused.md) and [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md) ([2438e4f](https://github.com/multitheftauto/mtasa-blue/commit/2438e4f9e7fbdeb67a8013fc17f268e6d19f2044) by **Lpsd**)

- Added [getElementLighting](mta://scripting/client/functions/getelementlighting.md) ([bc54720](https://github.com/multitheftauto/mtasa-blue/commit/bc54720421d0dcfa188a9e418d36fb732f061002) by **samr46**)

- Added [setChatboxCharacterLimit](mta://scripting/client/functions/setchatboxcharacterlimit.md) and [getChatboxCharacterLimit](mta://scripting/client/functions/getchatboxcharacterlimit.md), and increased character limit to 255 ([82801ab](https://github.com/multitheftauto/mtasa-blue/commit/82801ab353a5ea50f69c16904d7e678f620729c3) by **Lpsd**)

- Added [getAllElementData](mta://scripting/shared/functions/getallelementdata.md) ([0ff6607](https://github.com/multitheftauto/mtasa-blue/commit/0ff6607a6f8196c3b82d1289a315a53fa709da32) by **Unde-R** and **StrixG**)

### Server

- Added ARM support for the server executable ([8fc9004](https://github.com/multitheftauto/mtasa-blue/commit/8fc9004ec945a2ab74f4262ed0de267752f66675) and [d01bf2e](https://github.com/multitheftauto/mtasa-blue/commit/d01bf2eafc3059d4eff764c228dc6b82d5af7ffe) by **botder**)

- Added [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md) and [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md), also added support for the *breakable* map object attribute ([commit](https://github.com/multitheftauto/mtasa-blue/compare/d701fbe15b4cece7a6cd6242c3819e68deb7aae2...57d5be3d3e323394a8926a79f3da9cd3814e44a2) by **patrikjuvonen**)

## 192+ Changes and Bug Fixes

### Shared

- **[Breaking change]** Change bad numberstring warning to error ([9baf6a5](https://github.com/multitheftauto/mtasa-blue/commit/9baf6a5b6b3fdeb5abaf76c1e2863354aa88e36a) by **patrikjuvonen**)

- **[Breaking change]** Change unsigned type check from warning to error ([1cd1b61](https://github.com/multitheftauto/mtasa-blue/commit/1cd1b61b4b45e4fcfe2e0e1cb36bf09d74419618) by **patrikjuvonen**)

- **[Breaking change]** Added proper 3D radius check to [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) ([3b2b8fa](https://github.com/multitheftauto/mtasa-blue/commit/3b2b8fa9017fa27f47af0c6c3090c881a8a44327) by **Pirulax**)

- Added [cancelEvent](mta://scripting/shared/functions/cancelevent.md) support for [onElementModelChange](mta://scripting/server/events/onelementmodelchange.md) and [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md) ([7e72552](https://github.com/multitheftauto/mtasa-blue/commit/7e7255280d3c42f7a36329f496d72c2b9efafe57) by **TheNormalnij**)

- Fixed calling of [onClientColShapeLeave](mta://scripting/client/events/onclientcolshapeleave.md), [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md), [onColShapeLeave](mta://scripting/server/events/oncolshapeleave.md) and [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md) even if the element was destroyed ([f6177e4](https://github.com/multitheftauto/mtasa-blue/commit/f6177e43408053bf8d01fd9b55c478d770945340) by **Inder00**)

- Fixed [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md) returning the player instead of their vehicle, if available ([05b7ea2](https://github.com/multitheftauto/mtasa-blue/commit/05b7ea2d9c936b727ac057d3307d40a434f40352) by **botder**)

- Fixed several code warnings ([e43aa1b](https://github.com/multitheftauto/mtasa-blue/commit/e43aa1ba1dfd5c27fec50924938ac14444ff045e) by **botder**)

- Fixed a crash in CLatentTransferManager ([6220faa](https://github.com/multitheftauto/mtasa-blue/commit/6220faa318c076d1fbd79050edf6eb53aa43819d) by **botder**)

- Implemented ped far sync interval ([3c49beb](https://github.com/multitheftauto/mtasa-blue/commit/3c49beb6d36067a884e534140e31cae3297d2c2d) by **Zangomangu**)

- Improved [addEvent](mta://scripting/shared/functions/addevent.md) when sharing events over multiple resources ([f3811cb](https://github.com/multitheftauto/mtasa-blue/commit/f3811cb47633589ec5f1b0dd409045eb8c4133a0) by **Pieter-Dewachter**)

- Improved player sync when exiting vehicle ([e5026e7](https://github.com/multitheftauto/mtasa-blue/commit/e5026e7b71449042449ae3ce19af7e91a3166cdc) by **Zangomangu**)

- Removed leftover Discord integration ([9708440](https://github.com/multitheftauto/mtasa-blue/commit/9708440462cd5ee815769bf5dfbdbe90d704cd26) by **Lpsd**)

- Removed protocol error 14 ([828ec46](https://github.com/multitheftauto/mtasa-blue/commit/828ec464d3c761143af749720fe94f9e17712ccb) by **botder**)

- Updated source translations

### Client

- **[Breaking change]** Error out when creating a browser with size smaller than 1x1 ([a26417f](https://github.com/multitheftauto/mtasa-blue/commit/a26417f2f4f313f23cf96add09c75fd8d0256b6d) by **patrikjuvonen**)

- **[Breaking change]** Removed *mtalocal://* URL scheme and error out on bad usage ([c4c01e2](https://github.com/multitheftauto/mtasa-blue/commit/c4c01e29d29d214e51c7d689d8753e37e31c5e27) by **patrikjuvonen**)

- **[Breaking change]** Fixed incorrect Bloodring Banger enter/exit animation ([2c6058d](https://github.com/multitheftauto/mtasa-blue/commit/2c6058d3772ef8dae77df6ad0b2421a86abbe746) by **lopezloo**)

- **[Deprecation]** Changed [getCameraShakeLevel](mta://scripting/client/functions/getcamerashakelevel.md), [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md) to throw a warning on use, please upgrade to [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md) and [setCameraDrunkLevel](mta://scripting/client/functions/setcameradrunklevel.md) instead ([2651903](https://github.com/multitheftauto/mtasa-blue/commit/2651903e6a03c78a0571089b142b175f11f41bab) by **Unde-R**)

- Added hook to change vehicle damage debris to the vehicle color ([952448d](https://github.com/multitheftauto/mtasa-blue/commit/952448d46c9ac6066dc9d51e26b9da41808077e9) by **Merlin**)

- Added missing chat_text_outline CVAR to [getChatboxLayout](mta://scripting/client/functions/getchatboxlayout.md) function ([5cc419c](https://github.com/multitheftauto/mtasa-blue/commit/5cc419ca173301b03db15b0ae122fe970e96c2ef) by **Pieter-Dewachter**)

- Added missing getType method for [camera](mta://scripting/client/functions/camera.md) element ([a89d975](https://github.com/multitheftauto/mtasa-blue/commit/a89d975d7b959fe6c9b0af73ef6261cdb3763715) by **TheNormalnij** and **StrixG**)

- Added missing model ids and names scraped from .ide files ([062dea3](https://github.com/multitheftauto/mtasa-blue/commit/062dea31dc1a918d440bf7c87bd6957a7d9204ad) by **Merlin**)

- Added new world special property *coronaztest* ([093ecf4](https://github.com/multitheftauto/mtasa-blue/commit/093ecf47422f535053f2f4b321bc32ee1c63befd) by **gta191977649**)

- Added pthread and x64 files to the uninstall process ([6ae2ff1](https://github.com/multitheftauto/mtasa-blue/commit/6ae2ff14e966f7792de3b995d7c8e9655cd5bc75) by **patrikjuvonen**)

- Added ability to enable/disable custom weapons collisions ([e27d97d](https://github.com/multitheftauto/mtasa-blue/commit/e27d97dbc79e7cadc1740211b4fe2e746970d8b5) by **lopezloo**)

- Added dynamic ped shadows ([74c359b](https://github.com/multitheftauto/mtasa-blue/commit/74c359bcaa62fe6a6e8aaa281d247f9ee53778cc) and [136e9cf](https://github.com/multitheftauto/mtasa-blue/commit/136e9cf449d4370e5f30090d5adb7783814e02e0) by **lopezloo**)

- Added new default GUI skin (*Default 2023*) ([2d9e033](https://github.com/multitheftauto/mtasa-blue/commit/2d9e03324b07e355031ecb3263477477f1a91399) by **Haxardous** and [6ae0f65](https://github.com/multitheftauto/mtasa-blue/commit/6ae0f657b1aec4c93d823fef3529412cc754631f) by **botder**)

- Added new GUI skins *GWEN Blue* and *GWEN Orange* ([88a26fe](https://github.com/multitheftauto/mtasa-blue/commit/88a26fe4f35739d8b39ec14361b2ec97bae4b250) by **Haxardous**)

- Added missing files to data checks ([8531840](https://github.com/multitheftauto/mtasa-blue/commit/8531840ac690ff6534fabe6947b565c0fc59a418) by **Dutchman101**)

- Added *resource.ip2c* object to [acl.xml](mta://tutorials/access-control-list.md) *RPC* group ([960a661](https://github.com/multitheftauto/mtasa-blue/commit/960a6614c6962ec5a991076a05e7dd59bc87b0d7) by **Fernando-A-Rocha**)

- Added missing GTA special skins (3, 4, 5, 6, 8, 42, 65, 86, 119, 273, 289) ([b10b2bf](https://github.com/multitheftauto/mtasa-blue/commit/b10b2bfc4b73493f7143542a7158b00384d4a1a9) by **Allerek**)

- Added ability to get debug setting *(SettingDebugMode)* in [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md) ([e628e40](https://github.com/multitheftauto/mtasa-blue/commit/e628e402a8d9817d5a20bbcb4bc6105e99f67609) by **vyn666**)

- Added ability to restream LOD models in [engineRestreamWorld](mta://scripting/client/functions/enginerestreamworld.md) using new parameter *includeLODs* ([39f0394](https://github.com/multitheftauto/mtasa-blue/commit/39f03949edbf33f9b7c10c1e14ede178a734c515) by **TFP-dev**)

- Avoid hierarchy in [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([8e94ec1](https://github.com/multitheftauto/mtasa-blue/commit/8e94ec19f8f71ceb0b8eb09e9a7bbc7b33b1cd36) and [85203a6](https://github.com/multitheftauto/mtasa-blue/pull/2440/commits/85203a6222dfa989b8877defb0abb8a47891a59e) by **TheNormalnij** and **Lpsd**)

- Allow allocation of *timed-object* models using [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([f0a2424](https://github.com/multitheftauto/mtasa-blue/commit/f0a2424dd411f5eb454b554addf1eb217090f55b) by **TheNormalnij**)

- Changed *Enter a domain...* text from web settings into a placeholder ([dc82419](https://github.com/multitheftauto/mtasa-blue/commit/dc8241903184cf889502925b78c4d48d3413f0f4) by **patrikjuvonen**)

- Changed GUI *relative* argument to be *false* by default ([9b022b6](https://github.com/multitheftauto/mtasa-blue/commit/9b022b632ddcb3989311332b0c9cf41356d54f55) by **ghostkc12**)

- Changed [setVehiclesLODDistance](mta://scripting/client/functions/setvehiclesloddistance.md) and [setPedsLODDistance](mta://scripting/client/functions/setpedsloddistance.md) to be able to override client setting ([a44db24](https://github.com/multitheftauto/mtasa-blue/commit/a44db243df08cd729c850652e44994de1ceedcb1) by **samr46**)

- Changed max *fpslimit* to 32767 ([50d8040](https://github.com/multitheftauto/mtasa-blue/commit/50d80403182b1ac377502e08e29ec6ef51214c78) by **Merlin**)

- Changed default vector wrapping from clamp to wrap ([0dcdac3](https://github.com/multitheftauto/mtasa-blue/commit/0dcdac3946adb3e318fe92c6f86ebf024cdca045) by **Lpsd**)

- Changed to proxy dll method for loading core.dll into GTA process ([ffd2a4b](https://github.com/multitheftauto/mtasa-blue/commit/ffd2a4bad56d90b52deab8b55b9cbee65623228b), [c78d725](https://github.com/multitheftauto/mtasa-blue/commit/c78d7255861dd18ed9e6ecdf94c02d21e5cda932), [80e4078](https://github.com/multitheftauto/mtasa-blue/commit/80e4078d80504b81c9103f4c8b5c84ff4a40ef7a) and [3365030](https://github.com/multitheftauto/mtasa-blue/commit/336503042c5d60b53d1e10cd420410bbdd057b71) by **botder** and **ccw**)

- Check custom ped models before replacement ([d999e3e](https://github.com/multitheftauto/mtasa-blue/commit/d999e3e97770a11f4df25cd96c8bbe360c1fd4d9) by **botder**)

- Cleaned up and refactored server code ([693976b](https://github.com/multitheftauto/mtasa-blue/commit/693976b7131a87df71d81256a80cc48b22ab7bcf) and [cd1d208](https://github.com/multitheftauto/mtasa-blue/commit/cd1d2088a92b685b3b6294acb388fc1154ddbee4) by **botder**)

- Cleaned up *CClientVehicle.cpp* file ([8b806be](https://github.com/multitheftauto/mtasa-blue/commit/8b806be300c94bd15f1fa7575322bf31caf5234e) by **botder**)

- Cleaned up game_sa project ([76b21f7](https://github.com/multitheftauto/mtasa-blue/commit/76b21f7ed5b23f7d734eae20d089bb50336f8518), [e0abb30](https://github.com/multitheftauto/mtasa-blue/commit/e0abb3087a63e79b4273f8185920d00472b1354a), [889b6c8](https://github.com/multitheftauto/mtasa-blue/commit/889b6c8ea719cd1a9152ffee9a382a50ee960c51), [90bcdb4](https://github.com/multitheftauto/mtasa-blue/commit/90bcdb487ebd9949173186f78de7d2b22b588f96), [d7082ed](https://github.com/multitheftauto/mtasa-blue/commit/d7082ed1109094e89524cdf4e7d63ad2c2d6c65b), [c9c97f1](https://github.com/multitheftauto/mtasa-blue/commit/c9c97f1ad4887098b12efd78587b7ec6bed86971), [3f5b874](https://github.com/multitheftauto/mtasa-blue/commit/3f5b8741b1faae4682942499355ec9a92fcd81a1), [d085fb9](https://github.com/multitheftauto/mtasa-blue/commit/d085fb989e86be9668cd3e9f3f4426eefe55df6d), [5e781d5](https://github.com/multitheftauto/mtasa-blue/commit/5e781d51beb923c6f8e3e9f3d904bba3c2d7225e), [4dff64f](https://github.com/multitheftauto/mtasa-blue/commit/4dff64f1803af86a6c9666f0e972136a6d8c4948) by **Merlin**)

- Clean up file paths better ([2fb2b35](https://github.com/multitheftauto/mtasa-blue/commit/2fb2b35b6aff26f1b2f104a56c4dab04fb5a8366) by **patrikjuvonen**)

- Clear client script memory after load ([ce50b9e](https://github.com/multitheftauto/mtasa-blue/commit/ce50b9ee6c9112db0358e3ddba354021ca084588) by **Pirulax** and [cece630](https://github.com/multitheftauto/mtasa-blue/commit/cece630440c577f747e9ee890fd1563a542269e7) by **botder**)

- Decreased joystick saturation minimum from 51 to 0 ([4fcf3eb](https://github.com/multitheftauto/mtasa-blue/commit/4fcf3eb4c8db02b0ebefd580646ff6618c13e127) by **patrikjuvonen**)

- Detect graphics libraries in MTA directory ([a0645ac](https://github.com/multitheftauto/mtasa-blue/commit/a0645accecc1a6f1288671c988fff79f663e3bde) by **botder**)

- Disabled camera collisions for detached vehicle parts and projectiles ([1c00ef9](https://github.com/multitheftauto/mtasa-blue/commit/1c00ef9b13dae5b8b23abcb94b236790252ecd42) by **lopezloo**)

- Disabled system context menu ([34d61b5](https://github.com/multitheftauto/mtasa-blue/commit/34d61b53c03d974027f3b145ec6090dcf7e9c2b0) by **lopezloo**)

- Ensure files are within bounds ([07d0cf7](https://github.com/multitheftauto/mtasa-blue/commit/07d0cf77e990e2b25a4f2c99fd110645a3db225a) by **patrikjuvonen**)

- Fixed access violation in [getVehicleWheelFrictionState](mta://scripting/client/functions/getvehiclewheelfrictionstate.md) for vehicles not streamed in ([dde0e59](https://github.com/multitheftauto/mtasa-blue/commit/dde0e59055b5092cac5f16dd8bb06f1ff91ddeed) by **botder**)

- Fixed a small memory leak for [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([b2a625b](https://github.com/multitheftauto/mtasa-blue/commit/b2a625b100ff037908b002b586ca81692c24b2ae) by **TheNormalnij**)

- Fixed broken doors and damage sync for custom vehicles ([51d3288](https://github.com/multitheftauto/mtasa-blue/commit/51d3288f06b62561837d9e6d5470b1476cbe6c30) by **BCG2000**)

- Fixed camera to autofocus on new car on [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md) ([607b57d](https://github.com/multitheftauto/mtasa-blue/commit/607b57d36b72db62e976ef04c7bfa1d35f39da9a) by **TheNormalnij**)

- Fixed chatbox when using *inputBlocked* argument ([bd62e56](https://github.com/multitheftauto/mtasa-blue/commit/bd62e563e082533e3c35df877cf99ccdd54f5be8) by **Pieter-Dewachter**)

- Fixed crash when pickup has invalid custom model ([1b17869](https://github.com/multitheftauto/mtasa-blue/commit/1b17869cb58277d596d2865c2a2f777963fe18be) by **TheNormalnij**)

- Fixed crash when removing key binds while processing a key stroke ([90f757d](https://github.com/multitheftauto/mtasa-blue/commit/90f757d26f2c49b02cc5f67e7146c2c7db0dcbe0) by **botder**)

- Fixed [getVehicleType](mta://scripting/shared/functions/getvehicletype.md) and [getVehicleMaxPassengers](mta://scripting/shared/functions/getvehiclemaxpassengers.md) not returning specific values and players cannot enter as passengers on vehicles added with [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([141438f](https://github.com/multitheftauto/mtasa-blue/commit/141438fe462795c136f92b4fca9901e03dcec3f2) by **BCG2000**)

- Fixed interiors lacking radio ([e573959](https://github.com/multitheftauto/mtasa-blue/commit/e573959da339f9c19eef9f4b8a54e2da50b402ac) by **lopezloo**)

- Fixed key binds breaking on resource stop ([8c78fba](https://github.com/multitheftauto/mtasa-blue/commit/8c78fbaca9b837f11fe846792e4a9bf2ca43a8c9) and [280131f](https://github.com/multitheftauto/mtasa-blue/commit/280131fd07af4863cb40bad3ae32e1c0f02135e9) by **botder**)

- Fixed mirrored position of *light_front_second* vehicle dummy ([32aeb0e](https://github.com/multitheftauto/mtasa-blue/commit/32aeb0e67915744402fdac0619b8807db6352957) by **botder**)

- Fixed [setElementModel](mta://scripting/shared/functions/setelementmodel.md) forcing an element to be streamed in no matter the distance from [localPlayer](mta://scripting/client/functions/localplayer.md) ([467df06](https://github.com/multitheftauto/mtasa-blue/commit/467df061b5fadcee81bb7c0c4fb6cf23e741b3eb) by **TheNormalnij**)

- Fixed sync of damaged light states and wheel states ([fe48d09](https://github.com/multitheftauto/mtasa-blue/commit/fe48d0968042b0bc5e5375c0c2f8f9ee2ed951ba) by **Addlibs**)

- Fixed unused binds descriptions are always in English ([32962a6](https://github.com/multitheftauto/mtasa-blue/commit/32962a6a90178dbf4638df83c0985db1826ed8b1) by **patrikjuvonen**)

- Fixed single player HUD setting affecting MTA ([7ead65d](https://github.com/multitheftauto/mtasa-blue/commit/7ead65dcf207befd0eafadbaff3ac5aae62b0a08) by **Merlin**)

- Fixed [isElementInWater](mta://scripting/shared/functions/iselementinwater.md) returning false if ped or player is in vehicle in water ([29f3038](https://github.com/multitheftauto/mtasa-blue/commit/29f303860e5404aa98a2a69ca5a3b6e80eebd2df) by **Santi**)

- Fixed refresh rate limited to 60Hz in full screen mode for some setups ([5207a31](https://github.com/multitheftauto/mtasa-blue/commit/5207a314272fda9b54443edd30efb11e6e846dd6) and [5c77d97](https://github.com/multitheftauto/mtasa-blue/commit/5c77d974c10fc5096b0ecf600343f7c975e8a2c2) by **samr46**)

- Fixed water sound level outside of game boundaries on [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md) ([aed0554](https://github.com/multitheftauto/mtasa-blue/commit/aed055497e2662119ba178b878c74c28aa5e018f) by **samr46**)

- Fixed muzzle flash not showing for the last bullet in magazine ([80b17d9](https://github.com/multitheftauto/mtasa-blue/commit/80b17d96097c6977915c91f31ae2161a1bce1fdc) by **Merlin**)

- Fixed various high FPS related issues

- Fixed health bar blinking faster on high FPS ([df4d35d](https://github.com/multitheftauto/mtasa-blue/commit/df4d35d2a14cba7fc5549b13cc6cf221d2e7132a) by **Merlin**)

- Fixed walking while aiming on high FPS ([e64d311](https://github.com/multitheftauto/mtasa-blue/commit/e64d311f62de2bd848c07b59f4f53a30826c1bed) by **Merlin**)

- Fixed aircraft and boat lights blinking faster on high FPS ([f597c46](https://github.com/multitheftauto/mtasa-blue/commit/f597c46a45dea26742a680b5a2ab56d6dcb02368) by **Merlin**)

- Fixed breakable objects decaying faster on high FPS ([7c26ddd](https://github.com/multitheftauto/mtasa-blue/commit/7c26dddcc4ad68dbd79509494bb560fc3f784766) by **Merlin**)

- Fixed rocket launcher spawning too many effects on high FPS ([167adda](https://github.com/multitheftauto/mtasa-blue/commit/167addab6694e76d177989fb4caf3c5bf252dfc7) by **Merlin**)

- Fixed wheels spawning too many surface effects on high FPS ([d2b2c45](https://github.com/multitheftauto/mtasa-blue/commit/d2b2c45789747d8412a207e6c7b3094e8556ac73) by **Merlin**)

- Fixed stuntplane and cropduster spawning too many smoke trail particles on high FPS ([e9cc0a3](https://github.com/multitheftauto/mtasa-blue/commit/e9cc0a3d515165072863a6b1d3b1652814c24924) by **Merlin**)

- Fixed water cannon decaying much faster on high FPS ([32c04f0](https://github.com/multitheftauto/mtasa-blue/commit/32c04f0b25c959007b96d42cdbfefbadca22ca64) by **Merlin**)

- Fixed [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md) shaking too fast on high FPS ([893858d](https://github.com/multitheftauto/mtasa-blue/commit/893858ddc5a768194b435da40230fca8ef7da752) by **Merlin**)

- Fixed [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md) spawning too many particles on high FPS ([2e1042f](https://github.com/multitheftauto/mtasa-blue/commit/2e1042fd67b4438cf2f8e207af241ad98a4e1a88) by **Merlin**)

- Fixed more high FPS issues ([bcc56b5](https://github.com/multitheftauto/mtasa-blue/commit/bcc56b5ee6df43697069f38977d09eae23f7e62c) by **Merlin**)

- Fixed money animation playing faster on high FPS

- Fixed walking through water spawn too many particles on high FPS

- Fixed spawning too many weather particles on high FPS

- Fixed airplane spawning too many damage particles on high FPS

- Fixed vehicles spawning too much sand and water particles on high FPS

- Fixed boats spawning too many particles on high FPS

- Fixed spawning too many rain particles on vehicles on high FPS

- Fixed airplanes spawning too many particles when damaged on high FPS

- Fixed vehicles spawning too many exhaust particles on high FPS

- Fixed spawning too many particles while swimming on high FPS

- Fixed helicopters taking off faster on high FPS ([40c178e](https://github.com/multitheftauto/mtasa-blue/commit/40c178ed787b50ef3fc1d878d794b6b885bc00b9) by **Merlin**)

- Fixed more high FPS issues ([7c8a1ab](https://github.com/multitheftauto/mtasa-blue/commit/7c8a1ab93d091b06262749b482d6c8142ca69eea) by **Merlin**)

- Fixed fog moving too fast on high FPS

- Fixed glass shards spinning and expanding too fast on high FPS

- Fixed boats being slow on high FPS

- Fixed camera drunk/shake level not resetting on server disconnect ([3f71f1b](https://github.com/multitheftauto/mtasa-blue/commit/3f71f1b64f0359ea2309224d46e1aa65d2d7c3c3) by **Lpsd**)

- Fixed grass not rendering ([52798a2](https://github.com/multitheftauto/mtasa-blue/commit/52798a2d923bdb4e29f6fb9c63178e30e40479b6) by **TFP-dev**)

- Fixed server browser search input disappearing at times ([7c75015](https://github.com/multitheftauto/mtasa-blue/commit/7c750151a1f5ee11330fec23664359f4d2c535e9) by **lopezloo**)

- Fixed interior radio crash ([d003360](https://github.com/multitheftauto/mtasa-blue/commit/d00336070f6f726b66445213f43b50e605aefcd4) by **TheNormalnij** and [7eb3613](https://github.com/multitheftauto/mtasa-blue/commit/7eb36134dab77b2edf28d6efe6ef9c82c1e9d3f0) by **Lpsd**)

- Fixed installer overwriting MTA shortcuts ([d557104](https://github.com/multitheftauto/mtasa-blue/commit/d55710491940a5023545208ce14c087a78aa37e4) by **se16n**)

- Fixed a typo in fakelag command text ([39e7268](https://github.com/multitheftauto/mtasa-blue/commit/39e726857ec7b9a146323d63200d3e1c8031478d) by **JessePinkman**)

- Fixed zoom_in/out binds being inverted & fix ability to control zoom by weapon_next/previous binds ([4a4bcbc](https://github.com/multitheftauto/mtasa-blue/commit/4a4bcbc413ad33b56acd7284c81361187c7df8d6) by **darkdrifter**)

- Fixed a game crash if FxEmitterBP_c::LoadTextures failed to load main texture ([5a598d7](https://github.com/multitheftauto/mtasa-blue/commit/5a598d70161a85a961de462f28279d38df70aae3) and [9667cbe](https://github.com/multitheftauto/mtasa-blue/commit/9667cbea40a2b834107c781411a2c9658fec5073) by **botder**)

- Fixed a crash in FxPrim_c::Enable ([05c639c](https://github.com/multitheftauto/mtasa-blue/commit/05c639c05faf2b01ab001adaff33b503ce2d36b7) by **botder**)

- Fixed model replacement for unstreamed models ([c667e2a](https://github.com/multitheftauto/mtasa-blue/commit/c667e2ad05c97511e7b5cf63d223f762eea41e10) and [7d8718c](https://github.com/multitheftauto/mtasa-blue/commit/7d8718cde378787818637936a9873dfab689638c) by **botder**)

- Fixed desktop shortcut creation in installer script ([1c04346](https://github.com/multitheftauto/mtasa-blue/commit/1c043468b52348589d0ae379f914e490c0630cdf) and [3f6dac6](https://github.com/multitheftauto/mtasa-blue/commit/3f6dac669b5aed51a695cc59e13e3b552e0340e3) by **botder**)

- Fixed broken client Windows GDF file and updated its hardcoded version and URLs ([d54afd7](https://github.com/multitheftauto/mtasa-blue/commit/d54afd76ed67ba80cfb2fb221229ca01a4f42508) and [579775d](https://github.com/multitheftauto/mtasa-blue/commit/579775d79b166c82c1c2a3c1b020eb2febfff202) by **patrikjuvonen**)

- Fixed a client crash caused by buffer overflow issues in *GetNameAndDamage* ([1129399](https://github.com/multitheftauto/mtasa-blue/commit/1129399a129f44d6c729064603d5e84578290411) and [1fc700f](https://github.com/multitheftauto/mtasa-blue/commit/1fc700f5030b21d1c4f6ef65d76a3a3c9d987fd4) by **Pirulax** and [29dfe4b](https://github.com/multitheftauto/mtasa-blue/commit/29dfe4bd095170a131b27f9687262995ad301489) by **Pieter-Dewachter**)

- Fixed a client crash caused by GOOGLE_API_KEY, GOOGLE_DEFAULT_CLIENT_ID and GOOGLE_DEFAULT_CLIENT_SECRET environment variables ([9f8e6cd](https://github.com/multitheftauto/mtasa-blue/commit/9f8e6cd2c588ff4516572707cffe943175937ae5) by **TEDERIs**)

- Fixed a client crash on disconnect after using [engineSetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginesetmodelphysicalpropertiesgroup.md) on custom models ([047f709](https://github.com/multitheftauto/mtasa-blue/commit/047f709a2b71e08cb8d1362c0387882b6db886dd) by **TheNormalnij**)

- Fixed launching MTA with ARM emulation ([9fa2d19](https://github.com/multitheftauto/mtasa-blue/commit/9fa2d19ed77987df89b02ea39cc742dcbcc08cca) by **botder**)

- Fixed a client crash after resetting bind ([0454e3c](https://github.com/multitheftauto/mtasa-blue/commit/0454e3c0420c57ef22b241738d7f7a1463223cb5) by **Dutchman101**)

- Fixed CEF crashing on Wine ([ca04b07](https://github.com/multitheftauto/mtasa-blue/commit/ca04b07cd87dd192e60e8df236f314e86b8b108f) by **vahook**)

- Fixed download progress calculation ([74c2a5d](https://github.com/multitheftauto/mtasa-blue/commit/74c2a5d1295af626a0fa77252de5fbd5123c5af9) by **Lpsd**)

- Fixed random foliage on replaced collisions ([0a1cbb8](https://github.com/multitheftauto/mtasa-blue/commit/0a1cbb88b93727416b88b845546d36295f2651e2) by **TFP-dev**)

- Fixed get/set vehicle model wheel size memory leak ([de3dc70](https://github.com/multitheftauto/mtasa-blue/commit/de3dc70e406b08b7bccf92294e178ebbfc9abda9) by **TheNormalnij**)

- Fixed camera tilt not working when camera is fading ([bda1506](https://github.com/multitheftauto/mtasa-blue/commit/bda150604931e334968349acc1c61db0fd05f2c1) by **patrikjuvonen**)

- Fixed visit news button text overflow with localized string ([1e1d3d5](https://github.com/multitheftauto/mtasa-blue/commit/1e1d3d5ba39bf2aeabaec692cf57dd30e362cbe9) by **theSarrum**)

- Fixed various issues with the uninstaller, it now does a better job at cleaning up leftover files and registry entries (multiple commits by **patrikjuvonen**)

- Fixed 'Offline' checkbox label autosizing in the server browser ([0291f82](https://github.com/multitheftauto/mtasa-blue/commit/0291f82bd104a89d7d9d2ce3d54a57e5ea8e5d1d) by **patrikjuvonen**)

- Fixed shortcuts created by the installer ([741103d](https://github.com/multitheftauto/mtasa-blue/commit/741103df4d5ab6f068415ebbd56f1511f9806907) by **patrikjuvonen**)

- Fixed [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md) affecting other shaders ([2bb5054](https://github.com/multitheftauto/mtasa-blue/commit/2bb50548b3a18e9998c721aeb670980dc220d727) by **tederis**)

- Fixed crash when streamed in object with custom model is deleted (on disconnect) ([5df6d1f](https://github.com/multitheftauto/mtasa-blue/commit/5df6d1f9e3c9bf5568150f206062ae4f276ac36b) by **botder**)

- Fixed a crash related to when ped weapon slot is being set ([87644f5](https://github.com/multitheftauto/mtasa-blue/commit/87644f5fd4340a6f381e4f08342a0d2b39c626b2) by **botder**)

- Fixed a crash related to providing an empty string in [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md) ([2cd5784](https://github.com/multitheftauto/mtasa-blue/commit/2cd578402eb2197154abded0cab29a4b450a7b27) by **CrosRoad95**)

- Fixed various cursor alpha issues ([87e3dce](https://github.com/multitheftauto/mtasa-blue/commit/87e3dce37ca2fde416be90df9693e712985047e0) by **Lpsd**)

- Group windows under a single taskbar button on Windows ([56fbfc3](https://github.com/multitheftauto/mtasa-blue/commit/56fbfc3b69400a86dd682dfbb86ee02bc2e3f3ca) by **botder**)

- Implemented *delete* control character handling in chatbox ([0648e9c](https://github.com/multitheftauto/mtasa-blue/commit/0648e9c56e2e607e399ee3305751d5873a68614e) by **patrikjuvonen**)

- Improved [setSoundEffectParameter](mta://scripting/client/functions/setsoundeffectparameter.md) error messages ([cf5d166](https://github.com/multitheftauto/mtasa-blue/commit/cf5d16630f8e0ffa560e1abd1a83b03892d2274e) by **Pirulax** and **botder**)

- Improved CEF DX utilization & thread-safety fixes ([8863f60](https://github.com/multitheftauto/mtasa-blue/commit/8863f603fb9cfa50ffc3822e378b5af6b1090cf9) by **TEDERIs**)

- Improved SVG stability ([403df24](https://github.com/multitheftauto/mtasa-blue/commit/403df24fce070b630ac2f474933daaab62efbc44) by **TEDERIs**)

- Improved unescape safety ([ed5e6c4](https://github.com/multitheftauto/mtasa-blue/commit/ed5e6c4fc06a9ecef21897dbcbe323fa0550e976) by **Jusonex**)

- Improved http error safety ([88b623e](https://github.com/multitheftauto/mtasa-blue/commit/88b623ec72da363f83544f540287514fcf8e3bbe) by **Jusonex**)

- Improved camera weapon picture quality ([2acf0cd](https://github.com/multitheftauto/mtasa-blue/commit/2acf0cda21c3d4c489c5b1f888a48dc2d647994e) by **lopezloo**)

- Massively increase quality of splash image ([ab2a1b9](https://github.com/multitheftauto/mtasa-blue/commit/ab2a1b974fc29f9ae8fc009b633283a77a3c4825) and [4a82776](https://github.com/multitheftauto/mtasa-blue/commit/4a82776bfccd8ecd91caf9972bd686dfd0ff05a7) by **botder** and [11c3116](https://github.com/multitheftauto/mtasa-blue/commit/11c3116cc29197223b796d7e557907c2fa958c74) by **Dutchman101**)

- Refactored key binds ([2878168](https://github.com/multitheftauto/mtasa-blue/commit/2878168ba2749dfedc8fcc7c5c80637891c7277c), [5c0afad](https://github.com/multitheftauto/mtasa-blue/commit/5c0afad233bd5ae1a8835356f7de62db8be066fa), [6e87551](https://github.com/multitheftauto/mtasa-blue/commit/6e8755178780a45c729f8f2d48514f360c63754c) and [73e4e42](https://github.com/multitheftauto/mtasa-blue/commit/73e4e420b6948ae1bfda0c80d643e43550da2745) by **botder**)

- Removed async tasks in SVG and updated callback usage ([3157905](https://github.com/multitheftauto/mtasa-blue/commit/31579051cc046bc5cb55c59fc4e9e70ec1bdce34) by **Lpsd**)

- Removed now unnecessary strafe workaround ([a331072](https://github.com/multitheftauto/mtasa-blue/commit/a331072759e69f36062ed1c9b848f6df6f808c9a) by **Merlin**)

- Removed dummy window from taskbar ([7dccdf4](https://github.com/multitheftauto/mtasa-blue/commit/7dccdf47924299518ef33a57d8c0df9ee8de7405) by **lopezloo**)

- Do not reset handling for custom models on a non-local vehicle ([3c3af04](https://github.com/multitheftauto/mtasa-blue/commit/3c3af040173b66e21bbc587fbca48548866bb2b7) by **Inder00**)

- Show dialog for dxgi.dll in GTA install directory ([fb26d72](https://github.com/multitheftauto/mtasa-blue/commit/fb26d72b66a2223237c3f022dfad39230232dc3f) by **botder**)

- Split grenade collision from weapon collision ([0e2b203](https://github.com/multitheftauto/mtasa-blue/commit/0e2b203aa1d12f15931eb7d9522a5edf987f45ff) by **Merlin**)

- Internationalized news window title ([a446f02](https://github.com/multitheftauto/mtasa-blue/commit/a446f02701b6cd8325c13ab9e71b1e651bd3d827) by **patrikjuvonen**)

- Updated main menu images ([d38c107](https://github.com/multitheftauto/mtasa-blue/commit/d38c107372a05d73f5efd8813575c3ac4f740d60) by **patrikjuvonen**)

- Updated CGUI images ([c1a958c](https://github.com/multitheftauto/mtasa-blue/commit/c1a958c7fc6f7e9f5e1937fb59bbd1fa341da86e) by **patrikjuvonen**)

- Updated en_US images, added *latest_news.png* ([42693d8](https://github.com/multitheftauto/mtasa-blue/commit/42693d806b132e4299173059f423c61fa13f5c21) and [cd0cce7](https://github.com/multitheftauto/mtasa-blue/commit/cd0cce740cb63b2b2c6c79a7bd4ebc3fad6ad9aa) by **patrikjuvonen**)

- Updated main menu logo ([4b9a3a4](https://github.com/multitheftauto/mtasa-blue/commit/4b9a3a4a7717db059277a5fdb9f2653bb90b7496) and [aa1e1d4](https://github.com/multitheftauto/mtasa-blue/commit/aa1e1d4336068438b2436efbc71b7a9231199e45) by **patrikjuvonen**)

- Updated translations ([73c6457](https://github.com/multitheftauto/mtasa-blue/commit/73c6457b6ccb845c640cb5da738a4d10bc84901d) by **patrikjuvonen**)

- Updated various non-https links to https ([2722466](https://github.com/multitheftauto/mtasa-blue/commit/2722466f0f837151aeae4ab4acba3bff3be19257) by **patrikjuvonen**)

- Updated credits ([894c0f7](https://github.com/multitheftauto/mtasa-blue/commit/894c0f7e2538188fb5d4d7c71fd548ee3a9d92f1) by **patrikjuvonen**)

- Fixed inability to warp client-side ped to client-side trailer ([4e7fd05](https://github.com/multitheftauto/mtasa-blue/commit/4e7fd058f0b8600660d60d8a0d69abdadef98032) by **Tracer**)

### Server

- **[Breaking change]** Changed [callRemote](mta://scripting/server/functions/callremote.md) to return 0 as *errno* upon successful request to be consistent with [fetchRemote](mta://scripting/shared/functions/fetchremote.md) ([507de5f](https://github.com/multitheftauto/mtasa-blue/commit/507de5fc63fe207bb4f9d77706f7c54e1ffb3ba1) by **patrikjuvonen**)

- **[Breaking change]** Fixed flamethrower ammo to not be multiplied by 10 ([35ea5e4](https://github.com/multitheftauto/mtasa-blue/commit/35ea5e48fb7de6ce729961cfd24b68f3a2fd1c78) by **patrikjuvonen**)

- **[Breaking change]** Fixed [createBlip](mta://scripting/shared/functions/createblip.md) to sync blip size and color regardless of icon ID ([049e976](https://github.com/multitheftauto/mtasa-blue/commit/049e9762777828a416d9331d671250a267dc4fc5) by **patrikjuvonen**)

- **[Breaking change]** Server-side objects that were unbreakable by default, but would have been breakable client-side by default, are now breakable by default also server-side. Also added server-side support for [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md), [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md), and the *breakable* map object attribute ([commit](https://github.com/multitheftauto/mtasa-blue/compare/d701fbe15b4cece7a6cd6242c3819e68deb7aae2...57d5be3d3e323394a8926a79f3da9cd3814e44a2))

- **[Deprecation]** Changed [givePedJetPack](mta://scripting/server/functions/givepedjetpack.md), [removePedJetPack](mta://scripting/server/functions/removepedjetpack.md) and [doesPedHaveJetPack](mta://scripting/shared/functions/doespedhavejetpack.md) to throw a warning on use, please upgrade to [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md) and [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md) instead ([804c66b](https://github.com/multitheftauto/mtasa-blue/commit/804c66b88e0324eb6b2d9c83fdf7606ba05566c6) by **qaisjp**)

- Added a space between quit reasons when redirecting ([84e6e90](https://github.com/multitheftauto/mtasa-blue/commit/84e6e901754b80603a938d97e0b350d2c35f1f54) by **patrikjuvonen**)

- Added *persist* parameter to [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md) ([3485fd3](https://github.com/multitheftauto/mtasa-blue/commit/3485fd3ac770dd0e0a0be3c0258aad1784c1b700) by **MegadreamsBE**)

- Added limits to ehs form fields ([7642b05](https://github.com/multitheftauto/mtasa-blue/commit/7642b05138f23cc35b5b5e01021dafa33506ff90) by **botder** and **patrikjuvonen**)

- Added limits to acl object length ([c497e23](https://github.com/multitheftauto/mtasa-blue/commit/c497e23fb818103764b6cb6d457d201de6e82afa) by **patrikjuvonen**)

- Consider only affected players for element data stats ([2b549e4](https://github.com/multitheftauto/mtasa-blue/commit/2b549e49c7a3456cb668debdf6b02db9a981281c) by **TEDERIs**)

- Fixed server executable name for x64 on Windows ([a11758c](https://github.com/multitheftauto/mtasa-blue/commit/a11758c71cbbdd4eea9362aba255e324b374c20c) by **botder**)

- Fixed [onPedDamage](mta://scripting/server/events/onpeddamage.md) not working ([143102a](https://github.com/multitheftauto/mtasa-blue/commit/143102a38acdabba8d7837252fd8c95f704d4ef8) by **xLive**)

- Fixed kicking player while redirecting ([c56add8](https://github.com/multitheftauto/mtasa-blue/commit/c56add86d36034b1f32c5ef010b28156c022246e) by **TeteX1**)

- Fixed [banPlayer](mta://scripting/server/functions/banplayer.md) not kicking all players with the same IP address ([d073b61](https://github.com/multitheftauto/mtasa-blue/commit/d073b61877fb106d2d681c09816ef034cdb6454f) by **patrikjuvonen**)

- Fixed a crash caused by latent events ([934967f](https://github.com/multitheftauto/mtasa-blue/commit/934967ffcf3840dd9f16450bd718e87e1919ce9d) by **tederis**)

- Fixed server console history not working right with utf ([1813cb4](https://github.com/multitheftauto/mtasa-blue/commit/1813cb4f92cbe68a2f04732e3e52407a78b304c8) by **patrikjuvonen**)

- Improved ehs authentication checking ([2a84701](https://github.com/multitheftauto/mtasa-blue/commit/2a8470135b6b5a36ce159e6f62561cc333b2abe8) by **patrikjuvonen**)

- The vehicle "Street Clean Trailer (611)" now uses the same default color from its truck "Utility Van (552)" instead of being always fully black ([6e5cd4a](https://github.com/multitheftauto/mtasa-blue/commit/6e5cd4a61338d8cb1851c9ad54d683b978aecc98) by **Lord-Henry**)

- Updated and fixed server launcher icon ([8729c9f](https://github.com/multitheftauto/mtasa-blue/commit/8729c9f0a6fb2d396cd057abd0b7815be318aa0f) by **patrikjuvonen**)

- Updated default FPS limit to 74 in *mtaserver.conf* ([6c1f318](https://github.com/multitheftauto/mtasa-blue/commit/6c1f3184764aca0655b5b64fe88ca0a73b2b69c8) by **Dutchman101**)

- Use vector length method instead of manual distance calculation when using [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) server-side ([a3c83c8](https://github.com/multitheftauto/mtasa-blue/commit/a3c83c8927c709ca1999f2664d791274c3a7b969) by **NanoBob**)

- Fixed [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md) causing a C++ runtime assertion failure ([eba619d](https://github.com/multitheftauto/mtasa-blue/commit/eba619db22c515ad32e48052ee8c5d9d2c3303c8) by **Tracer**)

### More Technical Changes and Bug Fixes

Click to collapse [-]

- Added null-pointer checks in CWorld::FindObjectsKindaCollidingSectorList ([8e8aa3a](https://github.com/multitheftauto/mtasa-blue/commit/8e8aa3ab41928bd01c09c231679e0ecbc9bf7c97) by **Merlin**)

- Added a weak crash fix for CPed::GetBonePosition ([3d1b87a](https://github.com/multitheftauto/mtasa-blue/commit/3d1b87a7c11ef1cdde0c1475923f4a1b80b7f3fb) by **botder**)

- Added null-pointer check for a few RpClump functions ([3e348d1](https://github.com/multitheftauto/mtasa-blue/commit/3e348d140618346c9dfadbbd752f450f5535a6cf) and [4582f8a](https://github.com/multitheftauto/mtasa-blue/commit/4582f8a81d5dee0713067a5f3ea71948264d077b) by **botder**)

- Added check for active resource in CLuaDefs::CanUseFunction ([4a94343](https://github.com/multitheftauto/mtasa-blue/commit/4a94343ed44ff66c75d3c04ed2d45fae842054d5) by **Lpsd**)

- Fixed a bug with ErrorPrintf for server-side modules ([29e11de](https://github.com/multitheftauto/mtasa-blue/commit/29e11deb2db248856ab7992379ead5fc0966bcad) by **theSarrum**)

- Various code clean ups and refactors

- Refactored CBufferRef to use std::shared_ptr ([49fa848](https://github.com/multitheftauto/mtasa-blue/commit/49fa84851caf21458809d955a8131edb61ff4086) by **Pirulax**)

- Removed non-existent vendor from include ([9616ae1](https://github.com/multitheftauto/mtasa-blue/commit/9616ae131b1583682612b41a4f52fc35eb83db06) by **patrikjuvonen**)

- Got rid of *std::function* in *AsyncTaskSched* ([c372dc3](https://github.com/multitheftauto/mtasa-blue/commit/c372dc38ff76ca8ff33f853e4384ab4a9d657881) by **Pirulax**)

- Improved performance of CClientObjectManager::UpdateLimitInfo ([0160e18](https://github.com/multitheftauto/mtasa-blue/commit/0160e1828127b0f183425074401d8bab6391dc9b) by **Merlin**)

- Initialized *lastSyncType* variable in [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md) ([ca3b0b7](https://github.com/multitheftauto/mtasa-blue/commit/ca3b0b778e9695ce7da6391eda14429aa055d1f2) by **botder**)

- Removed CRefCountableST ([4482f13](https://github.com/multitheftauto/mtasa-blue/commit/4482f133eff87396029ee1c1d71a02125fbb0834) by **Pirulax**)

- Updated GitHub issue templates ([9b2dbbb](https://github.com/multitheftauto/mtasa-blue/commit/9b2dbbb8ad81edfc0d0837d43e2a9af57bfb8e8a), [70e59bb](https://github.com/multitheftauto/mtasa-blue/commit/70e59bb576dad330de243243791a1cb5bf441f91) and [07204d2](https://github.com/multitheftauto/mtasa-blue/commit/07204d2a989ad882950bcb66d0bb8ef5293089d5) by **patrikjuvonen**)

- Updated launchers ([5b4ce8a](https://github.com/multitheftauto/mtasa-blue/commit/5b4ce8a741fefb09980c3f4ff998d79218c4aef4) by **patrikjuvonen**, [368864b](https://github.com/multitheftauto/mtasa-blue/commit/368864b1bd61d5c7eabf14e13014dea7f01e57bd) and [11c3116](https://github.com/multitheftauto/mtasa-blue/commit/11c3116cc29197223b796d7e557907c2fa958c74) by **Dutchman101**)

- Upgraded l10n scripts to use python3 and automate pot file generation ([583f2b9](https://github.com/multitheftauto/mtasa-blue/commit/583f2b94c3d1039fab249843781fa42a8cea1782) by **darkdreamingdan** and **patrikjuvonen**)

- Upgraded to Visual Studio 2022 and v143 toolset ([3d94c21](https://github.com/multitheftauto/mtasa-blue/commit/3d94c21db1780c0f35148492ff6cc59dba3892bc), [bbd0c42](https://github.com/multitheftauto/mtasa-blue/commit/bbd0c4244cc2d93809ed2d892c9110fa54e3d5e3), [d3079d5](https://github.com/multitheftauto/mtasa-blue/commit/d3079d5b9f2b837a91d5f503df7f03f55c6a66fc) and [5a7bb84](https://github.com/multitheftauto/mtasa-blue/commit/5a7bb84fe5dab7a18415f07000ff22d4f77cc594) by **Dutchman101** and [96e690e](https://github.com/multitheftauto/mtasa-blue/commit/96e690ed8f04bf044d2d561b7ef5d4671a7691fc), [d8cfdea](https://github.com/multitheftauto/mtasa-blue/commit/d8cfdea9a6068481a0a31cf1e3e5c1520b03af68) and [f2dda37](https://github.com/multitheftauto/mtasa-blue/commit/f2dda37aba06f1394c3495a5717365d37df449b4) by **botder**)

- Overhauled game launch logic (various commits by **botder**)

- Overhauled loader (various commits by **botder**)

- Overhauled updater (various commits by **botder**)

- Decoupled Windows 7, 8 and 8.1 into their own branch to support Windows 10+ CEF updates (by **patrikjuvonen**)

- Refactor BitStream to use std::string_view ([66ff543](https://github.com/multitheftauto/mtasa-blue/commit/66ff543986f65db1e51235bef2647df1d6e397bc) by **Pirulax**)

- Various Docker related improvements and tweaks by **botder**

## 23 Vendor Updates

### Client

- Updated BASS libraries (various commits, [c557f77](https://github.com/multitheftauto/mtasa-blue/commit/c557f77a1330df432622fb9cd1921970f24a3699) by **Dutchman101**)

- Updated CEF from Chromium 94.0.4606.61 (CEF 94.4.2+g6a963ca)

- Windows 7, 8 and 8.1 only: to Chromium 109.0.5414.120 (CEF 109.1.18+gf1c41e4) (various commits by **Dutchman101**, **patrikjuvonen** and **Lpsd**)

- Windows 10+: to Chromium 114.0.5735.110 (CEF 114.2.10+g398e3c3) ([28544e4](https://github.com/multitheftauto/mtasa-blue/commit/28544e4881bf06b1a8966eacab8e9c073eb757e7) by **Dutchman101**)

- Updated freetype from 2.10.4 to 2.13.0 ([bce4ae7](https://github.com/multitheftauto/mtasa-blue/commit/bce4ae768ab4075fc08e2919787e58591899eee5) and [68cc675](https://github.com/multitheftauto/mtasa-blue/commit/68cc67513cac6ed99f71f2522e686c3750e384e7) by **patrikjuvonen**)

- Updated libspeex from 1.2rc2 to 1.2 and libspeexdsp from 1.2rc2 to 1.2rc3 ([deef8dc](https://github.com/multitheftauto/mtasa-blue/commit/deef8dcb534991376f51bd27c5293a78bb2e80ee) by **patrikjuvonen**)

- Updated lunasvg from 2.2.0 to 2.3.8 ([929b3ee](https://github.com/multitheftauto/mtasa-blue/commit/929b3eef88caff448f5aed224bcfde0929003019) by **Lpsd** and **patrikjuvonen**)

- Updated libpng from 1.6.37 to 1.6.39 ([94bab09](https://github.com/multitheftauto/mtasa-blue/commit/94bab0928f776a86bf77cab612d4d58a4549ec7b) by **patrikjuvonen**)

- Updated nvapi to r530 ([6d5bb39](https://github.com/multitheftauto/mtasa-blue/commit/6d5bb39b4b8ea753cc9d3dfc367bb9f993176d00) by **patrikjuvonen**)

- Updated libjpeg from 9d to 9e ([c6aafc6](https://github.com/multitheftauto/mtasa-blue/commit/c6aafc659bf93fa9875c25683b63c27379ec2a0c) by **patrikjuvonen**)

- Updated unifont from 13.0.06 to 15.0.06 ([b81eec8](https://github.com/multitheftauto/mtasa-blue/commit/b81eec8a9a999c080a0e59f4f669f00c7e59ebc3) by **patrikjuvonen**)

### Server

- Updated sqlite from 3.36.0 to 3.42.0 ([0f072bc](https://github.com/multitheftauto/mtasa-blue/commit/0f072bc9ba2c65ff85634faca8f1e60bcd7b6804) by **patrikjuvonen**)

- Updated mysql-connector-c from 6.0.2 to 6.1.11 ([9f88f41](https://github.com/multitheftauto/mtasa-blue/commit/9f88f41909780e914879dd385f5975006a8b818c) by **patrikjuvonen**)

- Updated minizip from 1.01e to 1.1 ([76ce14e](https://github.com/multitheftauto/mtasa-blue/commit/76ce14e9cc97c6d357e962d38c07743d922c4b96) by **patrikjuvonen**)

### Shared

- Updated curl from 7.79.1 to 8.1.2 ([602e918](https://github.com/multitheftauto/mtasa-blue/commit/602e91866bda621c03bd2e1fe3da2e992e8d7167) by **patrikjuvonen**)

- Updated mbedtls from 2.27.0 to 2.28.3 ([d8e29be](https://github.com/multitheftauto/mtasa-blue/commit/d8e29bea30d46098ea2da170c4aae24564c5b44a) and [b233b85](https://github.com/multitheftauto/mtasa-blue/commit/b233b85eed85d2e0246daaed85a4ae47900b32ae) by **patrikjuvonen**)

- Updated cryptopp from 8.6.0 to 8.7.0 ([c10ca92](https://github.com/multitheftauto/mtasa-blue/commit/c10ca9249cb027598dac99dff19f65b95641d58d) by **patrikjuvonen**)

- Updated zlib from 1.2.11 to 1.2.13 ([6df121b](https://github.com/multitheftauto/mtasa-blue/commit/6df121b676811b62deca5a55cd0a6bbacc149f6c) by **patrikjuvonen** and [e467585](https://github.com/multitheftauto/mtasa-blue/commit/e467585d70058551ba9e69beaf86c782c374115c) by **Lpsd**)

- Updated unrar from 6.02 to 6.21 ([66a16ff](https://github.com/multitheftauto/mtasa-blue/commit/66a16ff78331f5b632be63d010ee666d01681ba0) and [e816959](https://github.com/multitheftauto/mtasa-blue/commit/e816959ff511e2a6cca1c067ec1d3c413589d2f3) by **patrikjuvonen** and [66017cd](https://github.com/multitheftauto/mtasa-blue/commit/66017cd0ec47b7bcc64dc7be8d27234517dccc17) by **Lpsd**)

- Updated json-c from 0.15 to 0.16 ([4cfbaa7](https://github.com/multitheftauto/mtasa-blue/commit/4cfbaa76ca834a0bac8d97f873e5bfde844834ff) by **patrikjuvonen**)

- Updated NSIS from nsis-2.46.5-unicode to nsis-3.08 and 4 plugins and scripts ([423b55d](https://github.com/multitheftauto/mtasa-blue/commit/423b55d7aca79bc9c8b59574bf7dde780b239c10) by **patrikjuvonen** and [commits](https://github.com/multitheftauto/mtasa-blue/compare/11feb0411152213594e342c54f21dc2375216cf5...a30df1b23fd11dc4977380d672694cb18cc92b99) by **Dutchman101**)

## Resources

### 61+ Changes and Bug Fixes

- Added a new "restore" button within Editor's "Current Elements" window ([15fbc95](https://github.com/multitheftauto/mtasa-resources/commit/15fbc95f61f493e96a927f8f4fa483f25be2cd13) by **Haxardous** and **Fernando-A-Rocha**)

- Fixed empty if branches ([2660580](https://github.com/multitheftauto/mtasa-resources/commit/2660580de2750ca617a86f7e3ccb8235331935a8) by **ArranTuna**)

- Fixed inconsistent indentation ([49d3259](https://github.com/multitheftauto/mtasa-resources/commit/49d325928a8de114587568196d2ad4f1207f5d8d) and [2d68470](https://github.com/multitheftauto/mtasa-resources/commit/2d684707648b13c028d386a27abbcc08b22f3945) by **ArranTuna**)

- Fixed lines containing trailing whitespaces ([555a8ba](https://github.com/multitheftauto/mtasa-resources/commit/555a8ba0caf188fa6a0bdc755530ba4e9e9b121a) by **ArranTuna**)

- Fixed lint errors ([ccf98a1](https://github.com/multitheftauto/mtasa-resources/commit/ccf98a117cd57d9459036bc227d3499a66a10b19) and [7ee8890](https://github.com/multitheftauto/mtasa-resources/commit/7ee88903da99c837f268a13c7281fdf9476ea9ed) by **ArranTuna**)

- Fixed lint warnings ([b139dd9](https://github.com/multitheftauto/mtasa-resources/commit/b139dd9f878a89f6de01f9416b81605705af30ba), [372a8fa](https://github.com/multitheftauto/mtasa-resources/commit/372a8fab81e6a367ab3c2531885966617b563f9b), [ad1522f](https://github.com/multitheftauto/mtasa-resources/commit/ad1522f221aecee76fe42ed5f15b77785a299589), [3868016](https://github.com/multitheftauto/mtasa-resources/commit/386801682dc437e8527def6ece63d607b95ae775), [a7fbea7](https://github.com/multitheftauto/mtasa-resources/commit/a7fbea7a549328a7a3aa074b635cb2638252b027), [a474c54](https://github.com/multitheftauto/mtasa-resources/commit/a474c544bd8d01b799addb84d91e98b606e93081) and [18a495c](https://github.com/multitheftauto/mtasa-resources/commit/18a495cefa6b5fb343f5576f54bce19e75a412f8) by **ArranTuna**)

- Fixed "shadowing definition of loop variable" lint warnings ([02233db](https://github.com/multitheftauto/mtasa-resources/commit/02233dbc7d20205c2ce28da06a93d1637d841b7b) by **ArranTuna**)

- Fixed elementbrowser and resourcemanager not working by removing legacy JSON library and some ajax refactoring ([bde31f8](https://github.com/multitheftauto/mtasa-resources/commit/bde31f8a890057f2a7e02940f37489037b3de9a8) by **4O4**)

- Removed some unused variables ([0d424d1](https://github.com/multitheftauto/mtasa-resources/commit/0d424d13eabd9ef68c5282c46fc24c4f880b1c95) by **ArranTuna**)

- Replaced [getLocalPlayer](mta://scripting/client/functions/getlocalplayer.md) with [localPlayer](mta://scripting/client/functions/localplayer.md) across multiple resources ([01f7695](https://github.com/multitheftauto/mtasa-resources/commit/01f7695d3a49ce97639666773c274b747a7a158d) by **ArranTuna**)

- Replaced [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md) with [resourceRoot](mta://reference/misc/resourceroot.md) across multiple resources ([0dee496](https://github.com/multitheftauto/mtasa-resources/commit/0dee4961826feaad364fcb1565cba0824a4e1849) by **ArranTuna**)

- Replaced [getRootElement](mta://scripting/shared/functions/getrootelement.md) with [root](mta://reference/misc/root.md) across multiple resources ([9582a82](https://github.com/multitheftauto/mtasa-resources/commit/9582a82ea92d9e8f89a958dd7b33d82698ed1c9f) by **ArranTuna**)

- Upgraded admin2, interiors, parachute and freeroam resources to use the new jetpack functions ([c618a18](https://github.com/multitheftauto/mtasa-resources/commit/c618a18c6698839074014b747c3826f60feae0c6) by **xLive**)

- [admin] Fixed "previously defined" warnings ([4ffc5d0](https://github.com/multitheftauto/mtasa-resources/commit/4ffc5d067f48a83d2df7c375a512fb0de83e576c) and [3ed3219](https://github.com/multitheftauto/mtasa-resources/commit/3ed3219498813e130650231ff10a9fbe99c30fd9) by **ArranTuna**)

- [admin] Removed non-existent functions ([a594174](https://github.com/multitheftauto/mtasa-resources/commit/a5941740d3ee16b42ad883e7eecdb30266f692d5) by **ghostkc12**)

- [admin] Removed serial validation ([c6259f6](https://github.com/multitheftauto/mtasa-resources/commit/c6259f627936cea2743a40201a04a23dc78d5e7a) by **srslyyyy**)

- [admin] Improved admin to use a newly added server event instead of a client script ([0cb4877](https://github.com/multitheftauto/mtasa-resources/commit/0cb4877b2770666f95c01ba75f208315f1edc4bf) by **srslyyyy**)

- [admin] Updated ip2c mirror link ([9ad4c36](https://github.com/multitheftauto/mtasa-resources/commit/9ad4c366ae5704ee7d79d64912ee0ec9f12e977d) by **Dutchman101**)

- [admin] Updated *IpToCountryCompact.csv* ([310c59f](https://github.com/multitheftauto/mtasa-resources/commit/310c59f0c94013dc258e68d9e82dd84e4da05ea4) by **Dutchman101**)

- [admin] Fixed "No map selected!" message box when clicking search map editbox ([0b7d576](https://github.com/multitheftauto/mtasa-resources/commit/0b7d576607b62759ad7c2dd21ff0259e6358b4a8) by **Mkl21**)

- [admin2] Fixed spectator player action buttons ([01af273](https://github.com/multitheftauto/mtasa-resources/commit/01af273a6664c0db152a743a972a6f5fa02f8851) by **Dark-Dragon**)

- [admin2] Fixed various sorting related gridlist issues ([e0d1642](https://github.com/multitheftauto/mtasa-resources/commit/e0d1642b8a6fea3a822786c9a7cc7f8e4e1145e9) by **Dark-Dragon**)

- [admin2] Added missing set nick functionality ([39c40e6](https://github.com/multitheftauto/mtasa-resources/commit/39c40e61360579f9eb44d038f17712495b0022d6) by **Dark-Dragon**)

- [ajax] Use *application/json* request header when sending a JSON POST request ([11c466a](https://github.com/multitheftauto/mtasa-resources/commit/11c466a102556369887eba944128cd0641ff018a) by **Xenius97**)

- [ctf] Various fixes, cleanups and refactoring ([609ac0c](https://github.com/multitheftauto/mtasa-resources/commit/609ac0cc614944ec7e53292ad705b046134cc41f) by **IIYAMA12**)

- [deathmatch] Major refactor ([9f57aa8](https://github.com/multitheftauto/mtasa-resources/commit/9f57aa898b214a8fd3d5d1cad94c793d49d8c804) by **jlillis**)

- [editor] Fixed some debug warnings ([5e9f222](https://github.com/multitheftauto/mtasa-resources/commit/5e9f2220b645c369e9654c577403530c076e1749) by **ArranTuna**)

- [editor] Improved some debug outputs ([be3477d](https://github.com/multitheftauto/mtasa-resources/commit/be3477dc310f0f77a33531cc59ccdd7e1cd0e6ec) by **ArranTuna**)

- [editor] Small improvements in editor_main ([7816898](https://github.com/multitheftauto/mtasa-resources/commit/7816898d991a072b35e62ccf06c73775f39cb3eb) by **srslyyyy**)

- [editor] Updated gamemodestopper.lua in editor_main ([bfad624](https://github.com/multitheftauto/mtasa-resources/commit/bfad62487c08237f6227546b98878fd05ec08474), [3063712](https://github.com/multitheftauto/mtasa-resources/commit/3063712ac88d489eecae0263bf6ae086959ff6b5) and [7955351](https://github.com/multitheftauto/mtasa-resources/commit/7955351e58844bdbefa76d8e82102a6c829f4496) by **srslyyyy**)

- [editor] Fixed a typo in text ([8722f2b](https://github.com/multitheftauto/mtasa-resources/commit/8722f2b1ea85acca225dd700779ea18d2ffd0fac) by **Dutchman101**)

- [editor] Rotation improvements ([ced470e](https://github.com/multitheftauto/mtasa-resources/commit/ced470eb0ead7c48df948a17533fda8cbe656b0d) by **Zangomangu**)

- [editor] Fixed delete button not restoring element ([f0d0285](https://github.com/multitheftauto/mtasa-resources/commit/f0d0285faf853c47133eab106c05ccad5fc9ce71) by **Haxardous**)

- [editor] Removed breakable workaround in favour of the now native support for it ([33e54e4](https://github.com/multitheftauto/mtasa-resources/commit/33e54e445fed5b1ebec31f4a2ff993ff91186b40), [1798167](https://github.com/multitheftauto/mtasa-resources/commit/17981673c602baeecfd5a508c45c7bc711e8e02b) and [006eefb](https://github.com/multitheftauto/mtasa-resources/commit/006eefb63bbe3ea1d4cf500942860f40ae481cbd) by **patrikjuvonen**)

- [editor_main] Improved scripting extensions ([7a8ae06](https://github.com/multitheftauto/mtasa-resources/commit/7a8ae063c127fcb62a7d50d565355e1bb2bd7038) by **srslyyyy**)

- [editor_main] Disabled unused OOP in *meta.xml* for scripting extensions ([95f3c36](https://github.com/multitheftauto/mtasa-resources/commit/95f3c36307512bb35e7efb727e101c1bbc136564) by **srslyyyy**)

- [editor_main] Fixed version warning ([29e1ae0](https://github.com/multitheftauto/mtasa-resources/commit/29e1ae023b2746c4528c1064e6743d40877c9518) by **srslyyyy**)

- [freecam] Added support for changing field of view ([a960ba4](https://github.com/multitheftauto/mtasa-resources/commit/a960ba478a72996456376da23aaac538e0572e18) by **Xenius97**)

- [freecam] Fixed freecam mouse & key input by ignoring it when MTA window not focused ([316f536](https://github.com/multitheftauto/mtasa-resources/commit/316f536eb4816a6993e5690e730211c4cabb55e7) by **Fernando-A-Rocha**)

- [gameplay] Added button to delete handlings in hedit ([0835ecd](https://github.com/multitheftauto/mtasa-resources/commit/0835ecd1f77fe98b1dcc84130d068f8fadb6af0d) and [6509b74](https://github.com/multitheftauto/mtasa-resources/commit/6509b7424c3c2d6b38054e86904cc5b9a9c7fa78) by **ricksterhd123**, **Inder00**, **Disinterpreter** and **Dutchman101**)

- [gameplay] Fixed a debug warning in freeroam ([36b4f00](https://github.com/multitheftauto/mtasa-resources/commit/36b4f00181e804111a83b4bd8083be88325fded3) by **ArranTuna**)

- [gameplay] Fixed steering lock glitch on bikes and motorcycles in hedit ([f76952b](https://github.com/multitheftauto/mtasa-resources/commit/f76952b7606a7121d26eea086b7382554d5247e0) and [d252b9f](https://github.com/multitheftauto/mtasa-resources/commit/d252b9f7a849ddacb0dd84b72c51b80899c33c76) by **Dutchman101**)

- [gameplay] Fixed typos in hedit and sfxbrowser ([814437b](https://github.com/multitheftauto/mtasa-resources/commit/814437b19d05924373810f3961e6768744f45b90) by **TheNormalnij**)

- [gameplay] Settings support and code refactor for joinquit ([bbd536d](https://github.com/multitheftauto/mtasa-resources/commit/bbd536d18abb27850bb4ec0895031558a2c90501) by **itslewiswatson**)

- [gameplay] Small fixes for defaultstats ([b09bd68](https://github.com/multitheftauto/mtasa-resources/commit/b09bd68c960644e339a1e74f6002e3822f13191b) by **srslyyyy**)

- [gameplay] Small optimization on servers that use a lot of element data in parachute ([7b9d047](https://github.com/multitheftauto/mtasa-resources/commit/7b9d047fae1c3163aa7b2a380be87a149bf51906) and [d252b9f](https://github.com/multitheftauto/mtasa-resources/commit/d252b9f7a849ddacb0dd84b72c51b80899c33c76) by **Dutchman101**)

- [gameplay] Some improvements in deathpickups ([aa9782e](https://github.com/multitheftauto/mtasa-resources/commit/aa9782ea996bbe684587c8e9cf542a575a23779f) by **srslyyyy**)

- [hay] Fixed hay not resetting ([036ff61](https://github.com/multitheftauto/mtasa-resources/commit/036ff6142b48b97d47456d8cb16d40e71b7ca57b) by **Dark-Dragon**)

- [hedit] Added translations for delete button ([2b7439d](https://github.com/multitheftauto/mtasa-resources/commit/2b7439d8eba579f4f8fb21ddf1301454aface76a) by **ricksterhd123** and **Disinterpreter**)

- [ip2c] Added new **ip2c** default resource (decoupled from admin resource) ([f64d657](https://github.com/multitheftauto/mtasa-resources/commit/f64d65737bdefc300a0744592562455afdc3338b) by **Fernando-A-Rocha** and **srslyyyy**)

- [play] Refactored code ([7b66c78](https://github.com/multitheftauto/mtasa-resources/commit/7b66c7855735a4d43845863802814952d45773ab) by **srslyyyy**)

- [playerblips] Various improvements ([9e79974](https://github.com/multitheftauto/mtasa-resources/commit/9e79974593c08f44266bf75279db1537a1f05d69) by **jlillis**)

- [rustlerbombs] Added new **rustlerbombs** default resource ([49961eb](https://github.com/multitheftauto/mtasa-resources/commit/49961eb6b907774fdd7d56e53bc050dacd118434) by **Dutchman101**)

- [scoreboard] Trigger events improvements ([9be00d6](https://github.com/multitheftauto/mtasa-resources/commit/9be00d67a73bb66a04218668c85e26c7eff6db5c) by **srslyyyy**)

- [scoreboard] Performance improvements ([3d3c592](https://github.com/multitheftauto/mtasa-resources/commit/3d3c592b4522d5dcb33f9eb22e09bceaa29fb058) and [89f1224](https://github.com/multitheftauto/mtasa-resources/commit/89f122497a9771923391276e432b1b449a79dd5e) by **srslyyyy**)

- [scoreboard] Make */setcountry* command available to all players, rather than just admins ([d8cff2d](https://github.com/multitheftauto/mtasa-resources/commit/d8cff2da8745de34a4d0d6812e32920d98abbb8b) by **Dutchman101**)

- [scoreboard] Add 'fake ping' (*/setping*) command, to complement */setcountry* and make it more believable for users ([7aea1cc](https://github.com/multitheftauto/mtasa-resources/commit/7aea1cc503c3b500f1f8beb00e63a44de2376e47) and [d06f1d5](https://github.com/multitheftauto/mtasa-resources/commit/d06f1d56a462d9c48e97c8da4d473635f5c88b0c) by **Dutchman101**)

- [voice_local] Added new **voice_local** default resource ([25d4a4f](https://github.com/multitheftauto/mtasa-resources/commit/25d4a4f91f2277816819506a6e7fc62e727e6ef8) by **Dutchman101**)

- [web] Fixed resourcemanager ([37348ce](https://github.com/multitheftauto/mtasa-resources/commit/37348cecb60a6c999c316398a17f866d54569953) by **ArranTuna**)

- [webadmin] Fixed a typo in CSS ([70361a4](https://github.com/multitheftauto/mtasa-resources/commit/70361a4b19fb2773903de3431c37ab34a3252a03) by **RatajVaver**)

- [webmap] Switched to assets.multitheftauto.com domain for loading map tiles ([218f2c7](https://github.com/multitheftauto/mtasa-resources/commit/218f2c7ff17884f6905593ab716c52a38f2e90ed) by **patrikjuvonen**)

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
