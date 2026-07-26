---
doc_id: "mta-wiki:14593"
title: "Changes in 1.7"
source_title: "Changes in 1.7"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.7"
revision_id: 82634
language: "en"
categories: ["Changelog", "Incomplete"]
generated_at: "2026-07-26T16:10:32.769985+00:00"
---

# Changes in 1.7

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

**This changelog is partial and needs updating. It is updated progressively to keep the page always up to date.**

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.6.0...master](https://github.com/multitheftauto/mtasa-blue/compare/1.6.0...master)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/10](https://github.com/multitheftauto/mtasa-blue/milestone/10)

- Resources GitHub commit log: [https://github.com/multitheftauto/mtasa-resources/compare/1.6.0...master](https://github.com/multitheftauto/mtasa-resources/compare/1.6.0...master)

- Release announcement on forums: TBA

## Important notice to Windows 7 and 8.x users

If you are using Windows 7 or 8.x, please upgrade your system to Windows 10 or 11 as soon as possible. Windows 7 and 8.x are no longer supported by Microsoft (since January 2020 and January 2023 respectively) and most software (including Google Chrome and Steam) which means you are running an insecure system. Multi Theft Auto will also eventually drop Windows 7 and 8.x support sometime in the future, so it would be a good idea to start looking at upgrade options right now. Thank you!

**CEF in MTA is no longer updated for Windows 7 or 8.x. This is because CEF no longer supports those versions of Windows. This is bad for security, so please upgrade to Windows 10+ and MTA to 1.6+**

## 4 Deprecations

These changes will take effect in this version and scripts may need to be manually upgraded when updating:

- Changed [base64Encode](mta://scripting/shared/functions/base64encode.md) and [base64Decode](mta://scripting/shared/functions/base64decode.md) to throw a warning on use, please upgrade to [encodeString](mta://scripting/shared/functions/encodestring.md) and [decodeString](mta://scripting/shared/functions/decodestring.md) instead ([30a83b0](https://github.com/multitheftauto/mtasa-blue/commit/30a83b0af164fb6920a2a60e089d08a6f5622f7d) by **Nico834**)

- Changed [setHelicopterRotorSpeed](mta://scripting/client/functions/sethelicopterrotorspeed.md) and [getHelicopterRotorSpeed](mta://scripting/client/functions/gethelicopterrotorspeed.md) to throw a warning on use, please upgrade to [setVehicleRotorSpeed](mta://scripting/client/functions/setvehiclerotorspeed.md) and [getVehicleRotorSpeed](mta://scripting/client/functions/getvehiclerotorspeed.md) instead ([82000c3](https://github.com/multitheftauto/mtasa-blue/commit/82000c34830b51ace2d14e39f3b487feb1aac1da) by **FileEX**)

- Changes [setPedOnFire](mta://scripting/shared/functions/setpedonfire.md) and [isPedOnFire](mta://scripting/shared/functions/ispedonfire.md) to throw a warning on use, please upgrade to [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md) and [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md) instead ([7ad96e2](https://github.com/multitheftauto/mtasa-blue/commit/7ad96e2e78fe41f8924d3f105b1683f7363c6fcb) by **FileEX**)

- Changes [removeAllGameBuildings](mta://scripting/client/functions/removeallgamebuildings.md) and [restoreAllGameBuildings](mta://scripting/client/functions/restoreallgamebuildings.md) to throw a warning on use, please upgrade to [removeGameWorld](mta://scripting/client/functions/removegameworld.md) and [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md) instead ([d7adae6](https://github.com/multitheftauto/mtasa-blue/commit/d7adae68791ce237704acc06bf794b5fbda96f95#diff-93c130ddb85da32121129a437ac5b28ba16fa17f6e3506e4cddfb7bc3d8eb9fbR180) by **TheNormalnij**)

## Notable Changes

- Support for Discord Rich Presence ([fdaa3ac](https://github.com/multitheftauto/mtasa-blue/commit/fdaa3aca3e233c7aba69d0fd5f85e78288a4401a), [ef26810](https://github.com/multitheftauto/mtasa-blue/commit/ef26810df4542283fee8edcc165bc9be22f2ca98), [acfbd40](https://github.com/multitheftauto/mtasa-blue/commit/acfbd40df1ff1432ea1d6663c005d43fce22899c) by **znjvder**, **tederis**, **patrikjuvonen** and **Deihim007**)

- Added support for [Building](mta://development/building.md)'s ([81242ed](https://github.com/multitheftauto/mtasa-blue/commit/81242edb9295efbf4bf8b198b12d577a0877aec2), [eb6b18a](https://github.com/multitheftauto/mtasa-blue/commit/eb6b18a5d49a7f0f34bdbf42b15f933e42876cf8) by **TheNormalnij**)

- Added the ability to generate a nickname ([12c50ee](https://github.com/multitheftauto/mtasa-blue/commit/12c50eee66898771244074a3a44818dab36a7ac3) by **Nico834**)

- Added *meta.xml* loading files pattern ([90e2737](https://github.com/multitheftauto/mtasa-blue/commit/90e2737d0a5eb12f34d2fd3c1f270bedf34cda35) by **W3lac3**)

- Added world properties (time cycle and weather related features) with new functions: [setWorldProperty](mta://scripting/client/functions/setworldproperty.md), [getWorldProperty](mta://scripting/client/functions/getworldproperty.md), [resetWorldProperty](mta://scripting/client/functions/resetworldproperty.md) ([a75f1e9](https://github.com/multitheftauto/mtasa-blue/commit/a75f1e9a03e74f7c9d4ae9e5aef8433af84d5ea2) by **Samr46**)

- Added file-system related functions (list files and folders in directories) ([74781c6](https://github.com/multitheftauto/mtasa-blue/commit/74781c6295b5b6dc81cd95d4cfab7900d88d7524) by **Tracer**)

- Added the ability to change the color and size of the target arrow in the checkpoint marker ([071378e](https://github.com/multitheftauto/mtasa-blue/commit/071378ec4326408a9520c79c96befca995d097f6) by **FileEX**)

- Added the ability to change the alpha of checkpoint and arrow marker ([7988852](https://github.com/multitheftauto/mtasa-blue/commit/7988852cf3af9e78f662d76544dc00db408b5c87) by **FileEX**)

- Fixed weapon issues when using the jetpack ([180fbc0](https://github.com/multitheftauto/mtasa-blue/commit/180fbc0b5fdba95450e7a519f78f7588849349bf), [a68c2c4](https://github.com/multitheftauto/mtasa-blue/commit/a68c2c4232c28c6ba5595a814b89be976c4fa9c3) by **FileEX**)

- Fixed vehicle windows not being visible from the inside when the lights are on ([934c1d6](https://github.com/multitheftauto/mtasa-blue/commit/934c1d6cfef19902cc391c896bbe2f80ba5a4f70) by **FileEX**)

- Fixed old [setElementModel](mta://scripting/shared/functions/setelementmodel.md) memory leak ([4e7afa2](https://github.com/multitheftauto/mtasa-blue/commit/4e7afa2586c6992a75ac5312378c1096d87148ae) by **tederis**)

- Enabled WebGL (GPU Acceleration) in CEF ([0263011](https://github.com/multitheftauto/mtasa-blue/commit/026301168d2cd8239650a4f0aa33ff0be6d752dc) by **TFP-dev**)

- Refactored **Quick Connect button** ([5b59e22](https://github.com/multitheftauto/mtasa-blue/commit/5b59e2236b30ec696ac1c05f8bb4e509ec06c0f7) by **Fernando-A-Rocha**)

- Added setting to save camera photos in documents folder ([3419b9b](https://github.com/multitheftauto/mtasa-blue/commit/3419b9b7a20e3d1893d673a2a07ee1a0efda1bd5) by **ffsPLASMA**)

- Added HUD customization ([5ea0e0f](https://github.com/multitheftauto/mtasa-blue/commit/5ea0e0fb23b21750207b23191db92562cf9b822c) by **FileEX**)

- Added sync peds/players animations for new players ([b32eafc](https://github.com/multitheftauto/mtasa-blue/commit/b32eafc70816ece8ad995d98d380d8f6e9950475) by **FileEX**)

- From now on, animation progress is preserved even after a restream; the animation will not start from the beginning. ([ad0d6bf](https://github.com/multitheftauto/mtasa-blue/commit/ad0d6bfdd7bf56b78f7c8c1b9a60597ef9b6dca3) by **FileEX**)

- Added ability to replace CJ clothing models ([6b82365](https://github.com/multitheftauto/mtasa-blue/commit/6b823653ecf68e181de91392d5d8931488f90f20) by **W3lac3**)

- New MTA splash window ([215173e](https://github.com/multitheftauto/mtasa-blue/commit/215173eeb1e015c0381ce94f95429c36ab1b4430) by **botder**)

- Fixed multiple damage instances in certain areas during explosions ([3bce408](https://github.com/multitheftauto/mtasa-blue/commit/3bce4080ec66a993096f9e7fb039cc7d5d0d8175) by **FileEX**)

- From now on, before disconnecting from the server using the main menu, you will be asked to confirm if you really want to do it ([6aa763f](https://github.com/multitheftauto/mtasa-blue/commit/6aa763fb79701c57402fccca9ae6c0f396fb8f3c) by **tonievalue**)

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-6-0.md).

- This is the **28th** 1.x.x release

- **1,136** days

- **39** new functions

- **12** new events

- **4** deprecations

- **50+** bug fixes and changes

- **734** commits ([mtasa-blue](https://github.com/multitheftauto/mtasa-blue/compare/1.6.0...master))  ([mtasa-resources](https://github.com/multitheftauto/mtasa-resources/compare/1.6.0...master))

- **78** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aopen+is%3Aissue+created%3A2023-06-16..2024-10-01))

- **29** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+milestone%3A%221.6.1%22))

- **28** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?q=is%3Aclosed+is%3Aissue+closed%3A2023-06-16..2024-10-01+no%3Amilestone+-label%3Ainvalid))

- **30** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Aopen+is%3Apr+created%3A2023-06-16..2024-10-01))

- **81** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Amerged+milestone%3A%221.6.1%22))

- **26** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+is%3Aunmerged+closed%3A2023-06-16..2024-10-01))

- **2+** contributors of which **0+** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2023-06-16&to=2024-10-01&type=c))

- **100+** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **3** vendor updates

**Note:** Last update to these statistics was made 843 days ago.

## 86 New Features

### Shared

- Added new *special world properties* to [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) function

- Added **fireballdestruct** special world property ([938b306](https://github.com/multitheftauto/mtasa-blue/commit/938b306add48245e578ba6036f1a77521e277194) by **samr46**)

- Added **roadsignstext** special world property ([4a746ec](https://github.com/multitheftauto/mtasa-blue/commit/4a746eca1b5a546a19344a76573a5108ff9d79e6) by **FileEX**)

- Added **extendedwatercannons** special world property ([13a5395](https://github.com/multitheftauto/mtasa-blue/commit/13a53959f52c978b416c00b428938f82818b2312) by **FileEX**)

- Added **tunnelweatherblend** special world property ([9a0790e](https://github.com/multitheftauto/mtasa-blue/commit/9a0790ec7fab1efb7817eead371744fcd47da5c5) by '**gta191977649**)

- Added **ignorefirestate** special world proeprty ([46f3580](https://github.com/multitheftauto/mtasa-blue/commit/46f3580fbd8ea5cf48c14cf8fee0bd6eb6691854) by **FileEX**)

- Added **flyingcomponents** special world property ([5ee6414](https://github.com/multitheftauto/mtasa-blue/commit/5ee641436821ae8a59484ac721a4ec929d5cc152) by **FileEX**)

- Added **vehicleburnexplosions** special world property ([88d303c](https://github.com/multitheftauto/mtasa-blue/commit/88d303c0bbcc0ed4fee958df2d16ace562ce0108) by **samr46**)

- Added **vehicle_engine_autostart** special world property ([8b3f344](https://github.com/multitheftauto/mtasa-blue/commit/8b3f3440f8bc485f90d466a3fe6f3e5819de9c2f) by **samr46**)

- Added new *glitches* to [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md) function

- Added **vehicle_rapid_stop** glitch ([3f5801e](https://github.com/multitheftauto/mtasa-blue/commit/3f5801e65d8a51d112b686485d4a2491151c3311), [ef792d6](https://github.com/multitheftauto/mtasa-blue/commit/ef792d6af62443f97014621334c7188dddb4ef29) by **samr46** and **Merlin**)

- New **file** functions

- Added [fileGetContents](mta://scripting/shared/functions/filegetcontents.md) ([22930d8](https://github.com/multitheftauto/mtasa-blue/commit/22930d854ce67d84a4a3b65a61b98a9ffd3f9e38) by **botder**)

- Added [fileGetHash](mta://scripting/shared/functions/filegethash.md) ([94f944f](https://github.com/multitheftauto/mtasa-blue/commit/94f944f508b99b5d7e84fbb0be07a483e10517a9) by **botder**)

- New and updated [object](mta://reference/misc/object.md) functions

- **[Updated]** Added [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md) to server-side ([7c939ad](https://github.com/multitheftauto/mtasa-blue/commit/7c939adb892c08836462a78cd9b987884cdb49ee) by **FileEX**)

- **[Updated]** Added [breakObject](mta://scripting/shared/functions/breakobject.md) to server-side ([aa1a785](https://github.com/multitheftauto/mtasa-blue/commit/aa1a7853f46fc796a94f38b7df2a5293fb941ba2) by **FileEX**)

- **[Updated]** Added [respawnObject](mta://scripting/shared/functions/respawnobject.md) and [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md) to server-side ([9d65bb6](https://github.com/multitheftauto/mtasa-blue/commit/9d65bb673c4df16def27e97a4af74d3b0c7eedc9) by **FileEX**)

- **[New]** Added [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md) ([9d65bb6](https://github.com/multitheftauto/mtasa-blue/commit/9d65bb673c4df16def27e97a4af74d3b0c7eedc9) by **FileEX**)

- New **file-path** functions

- Added [pathListDir](mta://scripting/shared/functions/pathlistdir.md), [pathIsFile](mta://scripting/shared/functions/pathisfile.md) and [pathIsDirectory](mta://scripting/shared/functions/pathisdirectory.md) ([74781c6](https://github.com/multitheftauto/mtasa-blue/commit/74781c6295b5b6dc81cd95d4cfab7900d88d7524) by **Tracer**)

- New [marker](mta://reference/misc/marker.md) functions

- Added [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md) and [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md) ([071378e](https://github.com/multitheftauto/mtasa-blue/commit/071378ec4326408a9520c79c96befca995d097f6) by **FileEX**)

- New [timer](mta://reference/misc/timer.md) functions

- Added [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md) and [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md) ([69aa420](https://github.com/multitheftauto/mtasa-blue/commit/69aa420f21fde3ac56e3d3bbc62ef0f060295c0a) by **jvstns**)

- New and updated **world** functions

- **[New]** Added [resetWorldProperties](mta://scripting/shared/functions/resetworldproperties.md) ([6df889e](https://github.com/multitheftauto/mtasa-blue/commit/6df889e78328b80f8e4bdc02f8761472cf87c54c) by **FileEX**)

- **[Updated]** Added [isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md) and [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) also to server-side ([938b306](https://github.com/multitheftauto/mtasa-blue/commit/938b306add48245e578ba6036f1a77521e277194) by **samr46**)

- New and updated [vehicle](mta://reference/misc/vehicle.md) functions

- **[New]** Added [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md) ([9f54cfc](https://github.com/multitheftauto/mtasa-blue/commit/9f54cfcd7a584f413db731052ebed921acfc71ea) by **FileEX**)

- **[Upated]** Added [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md) to server-side ([e9e5819](https://github.com/multitheftauto/mtasa-blue/commit/e9e5819c394987de2b9a5d581c4df9fd47057d9d#diff-49b4b89bf4463f38e70a325131b4da66457d783b1401dde0ffbad723624f8612R130) by **Proxy-99**)

- **[Updated]** Added [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md) and [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md) to client-side ([682cdca](https://github.com/multitheftauto/mtasa-blue/commit/682cdca3c37248a9e725b461ba322db413653f25) by **Proxy-99**)

- Updated [player](mta://reference/misc/player.md) functions

- Added [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md) to client-side ([8403da5](https://github.com/multitheftauto/mtasa-blue/commit/8403da54ecfd20d6b9740fb79d90ac936d316112) by **Nico834**)

- Updated [ped](mta://reference/misc/ped.md) functions

- Added [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md) to server-side ([e71f482](https://github.com/multitheftauto/mtasa-blue/commit/e71f4828b46bb69b9622a11d0f700a79f986ee9b) by **Nico834**)

- New [element](mta://reference/misc/element.md) functions

- Added [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md) and [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md) ([7ad96e2](https://github.com/multitheftauto/mtasa-blue/commit/7ad96e2e78fe41f8924d3f105b1683f7363c6fcb) by **FileEX**)

### Client

#### Functions

- New **engine** functions

- Added **streaming** functions ([7ffc312](https://github.com/multitheftauto/mtasa-blue/commit/7ffc31243c1dbca8ed5e7b0f8c05da239aa918bd), [6c86ebb](https://github.com/multitheftauto/mtasa-blue/commit/6c86ebbf0801c45d5e0bcbb9d9f2e8fd55525b15), [3c44dc5](https://github.com/multitheftauto/mtasa-blue/commit/3c44dc5dcde0a5f98ff470ce9bc64443d47de807) by **Pirulax**)

- [engineStreamingSetMemorySize](mta://scripting/client/functions/enginestreamingsetmemorysize.md)

- [engineStreamingGetMemorySize](mta://scripting/client/functions/enginestreaminggetmemorysize.md)

- [engineStreamingRestoreMemorySize](mta://scripting/client/functions/enginestreamingrestorememorysize.md)

- [engineStreamingSetBufferSize](mta://scripting/client/functions/enginestreamingsetbuffersize.md)

- [engineStreamingGetBufferSize](mta://scripting/client/functions/enginestreaminggetbuffersize.md)

- [engineStreamingRestoreBufferSize](mta://scripting/client/functions/enginestreamingrestorebuffersize.md)

- [engineStreamingSetModelCacheLimits](mta://scripting/client/functions/enginestreamingsetmodelcachelimits.md)

- Added **model-streaming** functions ([008eaa7](https://github.com/multitheftauto/mtasa-blue/commit/008eaa7e36ae74bbab7c5bc9861d8f0f890eb945) by **TheNormalnij**)

- [engineStreamingRequestModel](mta://scripting/client/functions/enginestreamingrequestmodel.md)

- [engineStreamingReleaseModel](mta://scripting/client/functions/enginestreamingreleasemodel.md)

- [engineStreamingGetModelLoadState](mta://scripting/client/functions/enginestreaminggetmodelloadstate.md)

- Added new **TXD** functions ([3e9a373](https://github.com/multitheftauto/mtasa-blue/commit/3e9a3735a8022a0acabaa3041c8a3f8d91e547b7) by **TheNormalnij**)

- [engineSetModelTXDID](mta://scripting/client/functions/enginesetmodeltxdid.md)

- [engineResetModelTXDID](mta://scripting/client/functions/engineresetmodeltxdid.md)

- Added **pools** functions ([bdf1221](https://github.com/multitheftauto/mtasa-blue/commit/bdf12215d1f6e73d87f5cb0881049aa224b46b65) by **TheNormalnij**)

- [engineGetPoolCapacity](mta://scripting/client/functions/enginegetpoolcapacity.md)

- [engineSetPoolCapacity](mta://scripting/client/functions/enginesetpoolcapacity.md)

- [engineGetPoolDefaultCapacity](mta://scripting/client/functions/enginegetpooldefaultcapacity.md)

- [engineGetPoolUsedCapacity](mta://scripting/client/functions/enginegetpoolusedcapacity.md)

- Added [enginePreloadWorldArea](mta://scripting/client/functions/enginepreloadworldarea.md) ([5b72fb9](https://github.com/multitheftauto/mtasa-blue/commit/5b72fb9d3c9e6813cdf56e53d1a1e72958abd3cf) by **MegadreamsBE**)

- New functions for **Discord RPC** ([fdaa3ac](https://github.com/multitheftauto/mtasa-blue/commit/fdaa3aca3e233c7aba69d0fd5f85e78288a4401a), [ef26810](https://github.com/multitheftauto/mtasa-blue/commit/ef26810df4542283fee8edcc165bc9be22f2ca98), [acfbd40](https://github.com/multitheftauto/mtasa-blue/commit/acfbd40df1ff1432ea1d6663c005d43fce22899c) by **znjvder**, **tederis**, **patrikjuvonen** and **Deihim007**)

- [setDiscordApplicationID](mta://scripting/client/functions/setdiscordapplicationid.md)

- [setDiscordRichPresenceDetails](mta://scripting/client/functions/setdiscordrichpresencedetails.md)

- [setDiscordRichPresenceState](mta://scripting/client/functions/setdiscordrichpresencestate.md)

- [setDiscordRichPresenceAsset](mta://scripting/client/functions/setdiscordrichpresenceasset.md)

- [setDiscordRichPresenceSmallAsset](mta://scripting/client/functions/setdiscordrichpresencesmallasset.md)

- [setDiscordRichPresenceButton](mta://scripting/client/functions/setdiscordrichpresencebutton.md)

- [resetDiscordRichPresenceData](mta://scripting/client/functions/resetdiscordrichpresencedata.md)

- [isDiscordRichPresenceConnected](mta://scripting/client/functions/isdiscordrichpresenceconnected.md)

- [setDiscordRichPresencePartySize](mta://scripting/client/functions/setdiscordrichpresencepartysize.md)

- [setDiscordRichPresenceStartTime](mta://scripting/client/functions/setdiscordrichpresencestarttime.md)

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)

- New [building](mta://development/building.md) functions ([81242ed](https://github.com/multitheftauto/mtasa-blue/commit/81242edb9295efbf4bf8b198b12d577a0877aec2), [eb6b18a](https://github.com/multitheftauto/mtasa-blue/commit/eb6b18a5d49a7f0f34bdbf42b15f933e42876cf8) by **TheNormalnij**)

- [createBuilding](mta://scripting/shared/functions/createbuilding.md)

- **[Deprecated]** [removeAllGameBuildings](mta://scripting/client/functions/removeallgamebuildings.md)

- **[Deprecated]** [restoreAllGameBuildings](mta://scripting/client/functions/restoreallgamebuildings.md)

- New **world** functions

- Added [processLineAgainstMesh](mta://scripting/client/functions/processlineagainstmesh.md) ([acb80a3](https://github.com/multitheftauto/mtasa-blue/commit/acb80a3945d0d5e0230b8a41394a3fe3e70b8d0b) by **Pirulax**)

- Added **volumetric shadows** functions ([6c93a49](https://github.com/multitheftauto/mtasa-blue/commit/6c93a49c4c2381f4ce84df195d98d36372a47d37) by **Proxy-99**)

- [setVolumetricShadowsEnabled](mta://scripting/client/functions/setvolumetricshadowsenabled.md)

- [isVolumetricShadowsEnabled](mta://scripting/client/functions/isvolumetricshadowsenabled.md)

- [resetVolumetricShadows](mta://scripting/client/functions/resetvolumetricshadows.md)

- Added [testSphereAgainstWorld](mta://scripting/client/functions/testsphereagainstworld.md) ([aa90aa5](https://github.com/multitheftauto/mtasa-blue/commit/aa90aa5f31e59df455af33b49e3eee5e4f107bfd) by **FileEX**)

- Added [removeGameWorld](mta://scripting/client/functions/removegameworld.md) and [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md) ([d7adae6](https://github.com/multitheftauto/mtasa-blue/commit/d7adae68791ce237704acc06bf794b5fbda96f95) by **TheNormalnij**)

- New **drawing** functions

- Added [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md) ([f886a35](https://github.com/multitheftauto/mtasa-blue/commit/f886a359dd4a680c080da7f132db0527116b5d7a), [04ef14b](https://github.com/multitheftauto/mtasa-blue/commit/04ef14bbf2182b356155f28d4ed972b0f293632f) by **CrosRoad95** and **tederis**)

- New **effects/fx** functions

- Added [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md) ([8f2730d](https://github.com/multitheftauto/mtasa-blue/commit/8f2730d2e260c3319cb51101c6aedb45e22bbd89) by **FileEX**)

- New [ped](mta://reference/misc/ped.md) functions

- Added [resetPedVoice](mta://scripting/client/functions/resetpedvoice.md) ([18986a4](https://github.com/multitheftauto/mtasa-blue/commit/18986a4542db5eb72f6d0dfffb80cb8bb6eb1442) by **Tracer**)

- Added new animation features ([aa0591c](https://github.com/multitheftauto/mtasa-blue/commit/aa0591c6f7b529a27b4ed8667e1dc70e68bd9386) by **Tracer**)

- [getPedAnimationProgress](mta://scripting/client/functions/getpedanimationprogress.md)

- [getPedAnimationSpeed](mta://scripting/client/functions/getpedanimationspeed.md)

- [getPedAnimationLength](mta://scripting/client/functions/getpedanimationlength.md)

- Added [killPedTask](mta://scripting/client/functions/killpedtask.md) ([e4a502b](https://github.com/multitheftauto/mtasa-blue/commit/e4a502bc7619dc3913c70d169f6105ecfb0633ff) by **Proxy-99**)

- Added ped shadow features ([26d1828](https://github.com/multitheftauto/mtasa-blue/commit/26d18288730fd3a7a854152da60c9acd18ab6c6f) by **Proxy-99**)

- [setDynamicPedShadowsEnabled](mta://scripting/client/functions/setdynamicpedshadowsenabled.md)

- [isDynamicPedShadowsEnabled](mta://scripting/client/functions/isdynamicpedshadowsenabled.md)

- [resetDynamicPedShadows](mta://scripting/client/functions/resetdynamicpedshadows.md)

- Added [playPedVoiceLine](mta://scripting/client/functions/playpedvoiceline.md) ([7067ac1](https://github.com/multitheftauto/mtasa-blue/commit/7067ac1a73bb0b8c5a1f37794504a00e9703332e) by **FileEX**)

- New [player](mta://reference/misc/player.md) functions

- Added [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md) ([03e851a](https://github.com/multitheftauto/mtasa-blue/commit/03e851a2f5ff2d917ba3c7a1c7577fdb5b8d2a6f), [5f21c32](https://github.com/multitheftauto/mtasa-blue/commit/5f21c32fb0725140d6d03476e08de330d429b55a) by **FileEX**)

- New **HUD** functions ([5ea0e0f](https://github.com/multitheftauto/mtasa-blue/commit/5ea0e0fb23b21750207b23191db92562cf9b822c) by **FileEX**)

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

- New [vehicle](mta://reference/misc/vehicle.md) functions

- Added [setVehicleWheelsRotation](mta://scripting/client/functions/setvehiclewheelsrotation.md) ([aeb113d](https://github.com/multitheftauto/mtasa-blue/commit/aeb113d269fffee7d9ac435ce87b51e905e9efa6) by **gta191977649**)

- Added [getVehicleEntryPoints](mta://scripting/client/functions/getvehicleentrypoints.md) ([bf588c1](https://github.com/multitheftauto/mtasa-blue/commit/bf588c163cd5bc134771e3842a6585212f06307f) by **MegadreamsBE**)

- Added [setVehicleSmokeTrailEnabled](mta://scripting/client/functions/setvehiclesmoketrailenabled.md) and [isVehicleSmokeTrailEnabled](mta://scripting/client/functions/isvehiclesmoketrailenabled.md) for planes ([a5dfc52](https://github.com/multitheftauto/mtasa-blue/commit/a5dfc5223358127299511b618ab29da08ff23030) by **Proxy-99**)

- Added [setVehicleRotorState](mta://scripting/client/functions/setvehiclerotorstate.md) and [getVehicleRotorState](mta://scripting/client/functions/getvehiclerotorstate.md) for planes and helicopters ([c7644f2](https://github.com/multitheftauto/mtasa-blue/commit/c7644f2773c37c4e3d40b00807f2e962daca83b6#diff-9a175949acc865a4deea435d73c2082716ab68c6811ef1a657783f3d420dc00fR165) by **FileEX**)

- Added **vehicle audio** functions: ([53ee579](https://github.com/multitheftauto/mtasa-blue/commit/53ee579670ef4ecec28f44627ff99321bba48cbd) by **TheNormalnij**)

- [setVehicleModelAudioSetting](mta://scripting/client/functions/setvehiclemodelaudiosetting.md)

- [getVehicleModelAudioSettings](mta://scripting/client/functions/getvehiclemodelaudiosettings.md)

- [resetVehicleModelAudioSettings](mta://scripting/client/functions/resetvehiclemodelaudiosettings.md)

- [setVehicleAudioSetting](mta://scripting/client/functions/setvehicleaudiosetting.md)

- [getVehicleAudioSettings](mta://scripting/client/functions/getvehicleaudiosettings.md)

- [resetVehicleAudioSettings](mta://scripting/client/functions/resetvehicleaudiosettings.md)

- New **camera** functions ([40ec398](https://github.com/multitheftauto/mtasa-blue/commit/40ec398bb15e775d1552286eb86fe7aa0dffefa4), [d9c2793](https://github.com/multitheftauto/mtasa-blue/commit/d9c2793de2a9f0782ec59cf0ef9907abf935d421) by **Tracer**)

- [shakeCamera](mta://scripting/client/functions/shakecamera.md)

- [resetShakeCamera](mta://scripting/client/functions/resetshakecamera.md)

- New **game-time** functions ([b8b7ce5](https://github.com/multitheftauto/mtasa-blue/commit/b8b7ce555e2f0f0dd74425ac7c91786374513bee) by **Proxy-99**)

- [setTimeFrozen](mta://scripting/client/functions/settimefrozen.md)

- [isTimeFrozen](mta://scripting/client/functions/istimefrozen.md)

- [resetTimeFrozen](mta://scripting/client/functions/resettimefrozen.md)

- New [element](mta://reference/misc/element.md) functions

- Added [setElementBoneQuaternion](mta://scripting/client/functions/setelementbonequaternion.md) and [getElementBoneQuaternion](mta://scripting/client/functions/getelementbonequaternion.md) ([10098b0](https://github.com/multitheftauto/mtasa-blue/commit/10098b0984bf5d5955ea1764e28f616c8a60714f) by **gownosatana**)

- Added [setElementLighting](mta://scripting/client/functions/setelementlighting.md) ([90fd98a](https://github.com/multitheftauto/mtasa-blue/commit/90fd98a6381991cfa926a9a65b9b934d0343e2b1) by **FileEX**)

- New [browser](mta://reference/misc/browser.md) functions

- Added [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md) ([bfdfdb5](https://github.com/multitheftauto/mtasa-blue/commit/bfdfdb5f44726df85626e6e3e06c2a319c0c8962) by **Lpsd**)

- New **weapons** functions

- Added [setWeaponRenderEnabled](mta://scripting/client/functions/setweaponrenderenabled.md) & [isWeaponRenderEnabled](mta://scripting/client/functions/isweaponrenderenabled.md) ([efed59b](https://github.com/multitheftauto/mtasa-blue/commit/efed59b7dc7b076219f1c8a868ef8aa028582127) by **FileEX**)

#### Events

- Added [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md) ([b2cf029](https://github.com/multitheftauto/mtasa-blue/commit/b2cf02943924c4972d2a695cdbfd7c9873fc3cbb) by **Pieter-Dewachter**)

- Added [onClientBrowserConsoleMessage](https://wiki.multitheftauto.com/index.php?title=OnClientBrowserConsoleMessage&action=edit&redlink=1) ([#3676](https://github.com/multitheftauto/mtasa-blue/pull/3676), [d296a65](https://github.com/multitheftauto/mtasa-blue/commit/d296a653c5ce2ecfd4f7150d74391b703b773baf) by **gownosatana** and **Tracer**)

### Server

#### Functions

- New [ACL](mta://tutorials/acl.md) functions

- Added [aclObjectGetGroups](mta://scripting/server/functions/aclobjectgetgroups.md) ([cf46bd8](https://github.com/multitheftauto/mtasa-blue/commit/cf46bd8487bdb2d0cafdab1f43936357f670fe10) by **Tracer**)

- New **acl-account** functions

- Added [getAccountType](mta://scripting/server/functions/getaccounttype.md) ([545f54b](https://github.com/multitheftauto/mtasa-blue/commit/545f54b6ae0bfc721abba12402ad3787ed9ae811) by **Tracer**)

- Added [setAccountSerial](mta://scripting/server/functions/setaccountserial.md) ([a0c2e41](https://github.com/multitheftauto/mtasa-blue/commit/a0c2e410f225ebd245a7c5b8031812cf94360097) by **camargo2019**)

- New [vehicle](mta://reference/misc/vehicle.md) functions

- Added new vehicle respawn functions ([1ff7137](https://github.com/multitheftauto/mtasa-blue/commit/1ff7137fd4477626d7ef4abfb1c696872cdf0eab), [d93287d](https://github.com/multitheftauto/mtasa-blue/commit/d93287de761e568400b3b555a277e4ead6546ca3) by **Tracer**)

- [isVehicleRespawnable](mta://scripting/server/functions/isvehiclerespawnable.md)

- [getVehicleRespawnDelay](mta://scripting/server/functions/getvehiclerespawndelay.md)

- [getVehicleIdleRespawnDelay](mta://scripting/server/functions/getvehicleidlerespawndelay.md)

- Added [createBuilding](mta://scripting/shared/functions/createbuilding.md) to server-side also ([6e22129](https://github.com/multitheftauto/mtasa-blue/commit/6e221298f4998c576ebf5a783cd0761b89117a7a) by **TheNormalnij**)

- Security improvements for element-data system ([750d09a](https://github.com/multitheftauto/mtasa-blue/commit/750d09adb9fd35f4c1b7786966b7ca292e35c200) by **TheNormalnij**)

- Added [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md) event

- Added **elementdata_whitelisted** tag to the **mtaserver.conf**

- Added **clientChangesPolicy** argument to the [setElementData](mta://scripting/shared/functions/setelementdata.md).

- Added new [mta_server.conf](mta://reference/misc/server-mtaserver-conf.md) tags:

- Added [vehicle_contact_sync_radius](mta://reference/misc/server-mtaserver-conf.md) tag ([e3338c2](https://github.com/multitheftauto/mtasa-blue/commit/e3338c2fbbdb500c4ce28dc0677ceadef1f1ca4c) by **MegadreamsBE**)

- Added [check_duplicate_serials](mta://reference/misc/server-mtaserver-conf.md) tag ([e094942](https://github.com/multitheftauto/mtasa-blue/commit/e094942b75117a49cae8c35d6508f37d0cf511fe) by **Nico834**)

- Added [elementdata_whitelisted](mta://reference/misc/server-mtaserver-conf.md) tag [750d09a](https://github.com/multitheftauto/mtasa-blue/commit/750d09adb9fd35f4c1b7786966b7ca292e35c200) by **TheNormalnij**)

#### Events

- Added [onExplosion](mta://scripting/server/events/onexplosion.md) event ([9edffc4](https://github.com/multitheftauto/mtasa-blue/commit/9edffc4997579583407e8c2910264b344cf626a3) by **botder**)

- Added [onPlayerProjectileCreation](mta://scripting/server/events/onplayerprojectilecreation.md) and [onPlayerDetonateSatchels](mta://scripting/server/events/onplayerdetonatesatchels.md) events ([bc40402](https://github.com/multitheftauto/mtasa-blue/commit/bc404021f66228fb00f1f136a606425da6075daa) by **Zangomangu**)

- Added [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md) event ([eae47fe](https://github.com/multitheftauto/mtasa-blue/commit/eae47fe2f432d9053c425fd515ea27f963c254ec) by **Lpsd**)

- Added [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md) ([cfe9cd9](https://github.com/multitheftauto/mtasa-blue/commit/cfe9cd9d0006580e7e70dc9e93672e3d1d3b9836) by **Tracer**)

- Added [onPlayerTeamChange](mta://scripting/server/events/onplayerteamchange.md) ([c4e18c6](https://github.com/multitheftauto/mtasa-blue/commit/c4e18c618db299ea05f5395c798f2a7d6515f5ea) by **esmail9900**)

- Added [onAccountCreate](mta://scripting/server/events/onaccountcreate.md) and [onAccountRemove](mta://scripting/server/events/onaccountremove.md) ([545f54b](https://github.com/multitheftauto/mtasa-blue/commit/545f54b6ae0bfc721abba12402ad3787ed9ae811) by **Tracer**)

- Added [onPlayerTriggerInvalidEvent](mta://scripting/server/events/onplayertriggerinvalidevent.md) ([5b4122d](https://github.com/multitheftauto/mtasa-blue/commit/5b4122d35f725e4d258b408253c93e7cbd2ec783) by **Lpsd**)

- Added [onPlayerChangesWorldSpecialProperty](mta://scripting/server/events/onplayerchangesworldspecialproperty.md) event ([bbf511d](https://github.com/multitheftauto/mtasa-blue/commit/bbf511d4c5a94fc42d4ead201446fcef8ae430ec) by **Nico834**)

- Added [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md) event ([750d09a](https://github.com/multitheftauto/mtasa-blue/commit/750d09adb9fd35f4c1b7786966b7ca292e35c200) by **TheNormalnij**)

- Added [onShutdown](mta://scripting/server/events/onshutdown.md) ([aa20c7d](https://github.com/multitheftauto/mtasa-blue/commit/aa20c7d279ac92f1f98c54e79fda7fe00de64e50) by **FileEX**)

- Added [onPedWeaponReload](mta://scripting/server/events/onpedweaponreload.md) and [onPlayerWeaponReload](mta://scripting/server/events/onplayerweaponreload.md) ([e71f482](https://github.com/multitheftauto/mtasa-blue/commit/e71f4828b46bb69b9622a11d0f700a79f986ee9b) by **Nico834**)

- Added [onPlayerTeleport](mta://scripting/server/events/onplayerteleport.md) ([a38e6ac](https://github.com/multitheftauto/mtasa-blue/commit/4000ea4edb37d2d2caeb60a5977f7a38c8a22f06) by **imfelipedev**)

- Added [onAccountNameChange](https://wiki.multitheftauto.com/index.php?title=OnAccountNameChange&action=edit&redlink=1) ([078d46b](https://github.com/multitheftauto/mtasa-blue/commit/078d46b13164c940f3a713039e1a1be6d52c6c76) by **Davis22d**)

## 77 Changes and Bug Fixes

### Shared

- Fixed random toggle of world special properties ([bf95b1d](https://github.com/multitheftauto/mtasa-blue/commit/bf95b1d16e31f36899350e2acac4bb8adfad5cdd) by **samr46**)

- Many debugscript fixes

- Fixed [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)/[onDebugMessage](mta://scripting/server/events/ondebugmessage.md) recognizing level 4 as 0 ([783971e](https://github.com/multitheftauto/mtasa-blue/commit/783971efbdfcae622dbc03fd7647c337c2a3a306) by **Tracer**)

- Fixed outputDebugString level 4 colors ([5d4d7df](https://github.com/multitheftauto/mtasa-blue/commit/5d4d7df3b8ff703cf954f3af394c811c489dcb18) by **MegadreamsBE**)

- Fixed [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) level 4 not being logged ([1951a5e](https://github.com/multitheftauto/mtasa-blue/commit/1951a5e62d35b2cf4ec292d294f8c818b8463418) by **MegadreamsBE**)

- Fixed outputDebugString with level 4 not showing ([b459973](https://github.com/multitheftauto/mtasa-blue/commit/b459973f8ad00aff79042a338a70700a21b426dc) by **srslyyyy**)

- Ped sync improvements ([f5b599c](https://github.com/multitheftauto/mtasa-blue/commit/f5b599c9f45777f924f7980cadb2d3cc6431d8b8) by **tederis**)

- Fixed "Using setElementHealth on a dead ped makes it invincible" ([8368883](https://github.com/multitheftauto/mtasa-blue/commit/836888379dc3e434752ad20c10a8d7d33ffc65a2) by **FileEX**)

- Fixed setting player model resets their current weapon slot ([f7ce562](https://github.com/multitheftauto/mtasa-blue/commit/f7ce562b645cb05a18658df62d093b753b881bb9) by **FileEX**)

- Fixed a bug where *"arrow"* and *"checkpoint"* markers ignored the alpha color ([7988852](https://github.com/multitheftauto/mtasa-blue/commit/7988852cf3af9e78f662d76544dc00db408b5c87) by **FileEX**)

- Fixed the goggle effect resetting after changing skin ([1dd2914](https://github.com/multitheftauto/mtasa-blue/commit/1dd291409f791891b54ccf6b1d1cebe08cff13c0) by **Proxy-99**)

- Fixed satchels detaching after changing skin ([d93dbf2](https://github.com/multitheftauto/mtasa-blue/commit/d93dbf2ca598bf3508364bc7c6337d82c3d9ccb2) by **FileEX**)

- Added **resourceName** global variable and added current resource as default argument for [getResourceName](mta://scripting/shared/functions/getresourcename.md) ([49fb6c6](https://github.com/multitheftauto/mtasa-blue/commit/49fb6c68a27ad85e5abcd563f4c4f8c568305fdb) by **Nico834**)

- Added new parameters **animGroup** & **animID** for wasted events [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md), [onPedWasted](mta://scripting/server/events/onpedwasted.md), [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md) ([ecd6ed9](https://github.com/multitheftauto/mtasa-blue/commit/ecd6ed98ca129e7f45bda14384a503bee09495a7) by **Nico834** and **G-Moris**)

- Added optional **ignoreAlphaLimits** argument for [createMarker](mta://scripting/shared/functions/createmarker.md) to maintain backward compatibility after adding the ability to change alpha for arrow and checkpoint markers ([121048c](https://github.com/multitheftauto/mtasa-blue/commit/121048cb9a14c28dcefca9bf2d4e955ef920a087) by **FileEX**)

- Added optional **property** argument for [getVehicleHandling](mta://scripting/shared/functions/getvehiclehandling.md) ([a08e38d](https://github.com/multitheftauto/mtasa-blue/commit/a08e38d6507fdc1c051c2b84727c83dd9c418649) by **XJMLN**)

- Fixed health value issues ([612f9a6](https://github.com/multitheftauto/mtasa-blue/commit/612f9a6715059baa43182e891258d9c3ceb19591) by **Tracer**)

- Fixed [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md) negative remaining duration ([1c6cab5](https://github.com/multitheftauto/mtasa-blue/commit/1c6cab5a94c8c6ff5cf9b1fc0c9bc04808c922f8) by **jvstns**)

- Fixed changing [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md) doesn't update contact element ([71c683f](https://github.com/multitheftauto/mtasa-blue/commit/71c683f547aac34e876601d24c881227fe3ca05f) by **FileEX**)

- Removed ability to skip [addDebugHook](mta://scripting/shared/functions/adddebughook.md) ([2fecd74](https://github.com/multitheftauto/mtasa-blue/commit/2fecd74fdd453efdcbdddfd8f3fa3c092640cf9f) by **PlatinMTA**)

- Fixed hydraulics stopping working after using [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md) ([f968363](https://github.com/multitheftauto/mtasa-blue/commit/f96836397a075585d4d112eb7d0240f1abf361d4) by **FileEX**)

- Fixed helicopter rotor unaffected by vehicle alpha ([55d3922](https://github.com/multitheftauto/mtasa-blue/commit/55d39225254c0b9961c1423b0d5695beff20072b) by **FileEX**)

- Add **spawnFlyingComponent & breakGlass** arguments for [setVehiclePanelState](mta://scripting/shared/functions/setvehiclepanelstate.md) ([5b69d70](https://github.com/multitheftauto/mtasa-blue/commit/5b69d700c848e36b2f427bbc6ba5b2c905592783) by **FileEX**)

- Fixed armor synchronization ([583e675](https://github.com/multitheftauto/mtasa-blue/commit/583e675da976fbf90f45804ad834d8fe33c779a1) by **Nico834**)

- Fixed jetpack disappearing after changing position and coming back after changing skin ([de26a9e](https://github.com/multitheftauto/mtasa-blue/commit/de26a9e98519350f0486290ce886595068c02470) by **FileEX**)

- Added support for **ZLIB** compression to [encodeString](mta://scripting/shared/functions/encodestring.md) & [decodeString](mta://scripting/shared/functions/decodestring.md). ([6230161](https://github.com/multitheftauto/mtasa-blue/commit/6230161f8d0c83b60aec3f4afa5be88dd213b88b) by **samr46**)

- Fixed a bug where hex color codes were included in the chat message length. ([9a0b1d5](https://github.com/multitheftauto/mtasa-blue/commit/9a0b1d59233f7001e991262b4df9d1c17850dc08) by **shadylua**)

### Client

- Update d3dcompiler_47.dll from CEF ([75a1a29](https://github.com/multitheftauto/mtasa-blue/commit/75a1a298113721343090a06d60394f63f64df9ca) and [6d8fd8c](https://github.com/multitheftauto/mtasa-blue/commit/6d8fd8cc2fe7377318583f70abf58dcdb7d09cb0) by **patrikjuvonen**)

- Updated translations from Crowdin ([29baf29](https://github.com/multitheftauto/mtasa-blue/commit/29baf29a0143706eb08ef76c4743a452a7f83600) by **patrikjuvonen**)

- Added Azerbaijani to client languages

- Resolved cursor being invisible with main menu open in certain scenarios ([bb1f675](https://github.com/multitheftauto/mtasa-blue/commit/bb1f675e6fee0ca3967f05afb5d2592dec9459b2) by **Lpsd**)

- Partially fixed screen flickering on high memory usage ([1a88646](https://github.com/multitheftauto/mtasa-blue/commit/1a886460a9fab1041cfba38078ae544b0fa51240) by **Zangomangu**)

- Added *texture hit info* parameter to [processLineOfSight](mta://scripting/client/functions/processlineofsight.md) ([86f3344](https://github.com/multitheftauto/mtasa-blue/commit/86f3344d1371a9783c2c7b755b895160a03ff6cd) by **Pirulax**)

- Fixed CStreamingSA::GetUnusedStreamHandle ([38624a4](https://github.com/multitheftauto/mtasa-blue/commit/38624a4c2d18f4b60064d49069d3bcd81fbb4385) by **tederis**)

- IMG count extension ([1a60f60](https://github.com/multitheftauto/mtasa-blue/commit/1a60f6094b6660d29cabae780e6fbea5f5f1abf2) by **tederis**)

- Fixed a desync state after aborted carjacking ([3f510fc](https://github.com/multitheftauto/mtasa-blue/commit/3f510fcdc7722cdfcb2e09ea43990b56aa43162b) by **Zangomangu**)

- Allowed allocating clump models ([428561f](https://github.com/multitheftauto/mtasa-blue/commit/428561f1ebab49b8370ef0f022510cd67e98ab59) by **TheNormalnij**)

- Fixed crash in CEF init ([c782826](https://github.com/multitheftauto/mtasa-blue/commit/c782826c955dfbdbaa67852a245e1c601d6b9f2c) by **TheNormalnij**)

- Fixed "Changing vehicle model from doorless or "doorful" causes doors to fall off" ([d6659da](https://github.com/multitheftauto/mtasa-blue/commit/d6659dae263e2883d9e479ca271f0e9c8e622f95) by **FileEX**)

- Fixed "Wheel visibility when using setVehicleWheelStates"  ([51c9257](https://github.com/multitheftauto/mtasa-blue/commit/51c9257a427957642932a216bd76cb7de59fea1b) by **FileEX**)

- Added new world special property *burnflippedcars* ([938b306](https://github.com/multitheftauto/mtasa-blue/commit/938b306add48245e578ba6036f1a77521e277194) by **samr46**)

- Streaming buffer restore and fixes ([6c86ebb](https://github.com/multitheftauto/mtasa-blue/commit/6c86ebbf0801c45d5e0bcbb9d9f2e8fd55525b15) by **Pirulax**)

- Fixed Unicode file path passed in CClientIMG ([c57f07b](https://github.com/multitheftauto/mtasa-blue/commit/c57f07bfad8b02953dbe7b2b6e9b9de08ba88226) by **TheNormalnij**)

- Added new world special property *fireballdestruct* ([219ad73](https://github.com/multitheftauto/mtasa-blue/commit/219ad73d600140724eefcf5ca4040ac417cdee12) by **samr46**)

- Fixed "Hide question box when hiding main menu" ([4beff04](https://github.com/multitheftauto/mtasa-blue/commit/4beff0447f093c66594a5f32ad5e52c7d7188ce9) by **XJMLN**)

- Fixed engineFreeModel regression ([b52500e](https://github.com/multitheftauto/mtasa-blue/commit/b52500e92fb2591c092a6e66121471f098a2e044) by **TheNormalnij**)

- Fixed assert when model info is missing ([d431e5e](https://github.com/multitheftauto/mtasa-blue/commit/d431e5e16120b63beafbfe69110da601d12a76bb) by **TheNormalnij**)

- Fixed engineFreeModel crashes ([c289c22](https://github.com/multitheftauto/mtasa-blue/commit/c289c22fb9a13730b7fd793752d84adbf2b928ee) by **TheNormalnij**)

- Filtered URLs in requestBrowserDomains with incorrect symbols ([74bbb06](https://github.com/multitheftauto/mtasa-blue/commit/74bbb068acc6757ff0e04d0c63b999236e51ce63) by **TheNormalnij**)

- Fixed issues with ped shaders ([3bc1e6d](https://github.com/multitheftauto/mtasa-blue/commit/3bc1e6d98ab13a9e7db95cc616b4645dc761889b) by **Merlin**)

- Fixed 3D primitives disappearing ([04a1e2b](https://github.com/multitheftauto/mtasa-blue/commit/04a1e2ba9157e4a1a91297f91554b72a87bf0ed4) by **tederis**)

- Fixed [svgSetSize](mta://scripting/client/functions/svgsetsize.md) issues ([721c2b6](https://github.com/multitheftauto/mtasa-blue/commit/721c2b6d0f0c4ab016be079f1d4e28dec0123a6d) by **Nico834**)

- Fixed the marker flickering issue during water cannon effects ([e83f700](https://github.com/multitheftauto/mtasa-blue/commit/e83f700ee24904c0411b4dad3e695b3c3e30d9e4) by **Merlin**)

- Fixed buildings removal ([1b40db7](https://github.com/multitheftauto/mtasa-blue/commit/1b40db7cb5b63966ee97d0cbe79190360e1d32a0) by **tederis**)

- Fixed crashes caused by [createBuilding](mta://scripting/shared/functions/createbuilding.md) with [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([6245a68](https://github.com/multitheftauto/mtasa-blue/commit/6245a68f3d97fc222d78fbc66b67f422a13710bf) by **TheNormalnij**)

- Fixed wrong getModelMatrix result for buildings ([f691946](https://github.com/multitheftauto/mtasa-blue/commit/f691946bc2d3dac75bd27d31886cd6b66d55811d) by **TheNormalnij**)

- Fixed crashes for *timed-object* in [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([229389a](https://github.com/multitheftauto/mtasa-blue/commit/229389a4bd1c4c02010ba27ce26a428b41b68560) by **TheNormalnij**)

- Fixed incorrect colors for 3D draws ([1f2c6e7](https://github.com/multitheftauto/mtasa-blue/commit/1f2c6e75fb71b01f0053f151e766a232ed33692b) by **Nico834**)

- Add missing definition GuiGridList::getColumnWidth ([b34b1d5](https://github.com/multitheftauto/mtasa-blue/commit/b34b1d5362291bcf00c7a0a0b694f60e1dccb363) by **Lpsd**)

- Fixed [resetPedVoice](mta://scripting/client/functions/resetpedvoice.md) not working at all ([3d8bd50](https://github.com/multitheftauto/mtasa-blue/commit/3d8bd504f009fc2aa66e1dc9d35427a889ccd6aa) by **Tracer**)

- Added LOD support for buildings ([77ab3e6](https://github.com/multitheftauto/mtasa-blue/commit/77ab3e64a3c6dacdcee02a223b67aec6c5b97ec2) by **TheNormalnij**)

- Added render stages for 3D primitives (new *stage* parameter) ([8414476](https://github.com/multitheftauto/mtasa-blue/commit/841447684c2d1992656555f81d73da52b2ce5c4f) by **tederis**)

- Added disable option for [engineSetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginesetmodelphysicalpropertiesgroup.md) ([b6216ca](https://github.com/multitheftauto/mtasa-blue/commit/b6216cad058582b0feb34e98e94531d4acbf7c5b) by **TheNormalnij**)

- Fixed return correct value for stuntDistance parameter ([1f464d6](https://github.com/multitheftauto/mtasa-blue/commit/1f464d61c8c5f1400faa5472ccb67d2436d52903) by **XJMLN**)

- Fixed [engineRestoreModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginerestoremodelphysicalpropertiesgroup.md) restores incorrect group ([291dfb4](https://github.com/multitheftauto/mtasa-blue/commit/291dfb4bc9bd72307a4ba4b42ffcbfc03ded4e38) by **TheNormalnij**)

- Fixed OGG sound files can't be played as RAW data ([2764b79](https://github.com/multitheftauto/mtasa-blue/commit/2764b7983c4e1bde20b894ebcfef5f230b149030) by **FileEX**)

- Implement [getElementBoundingBox](mta://scripting/client/functions/getelementboundingbox.md) for buildings ([7b228da](https://github.com/multitheftauto/mtasa-blue/commit/7b228daea3e0dc22d808abcf0eb568d99efcf63d) by **TheNormalnij**)

- Fixed streaming size check after [engineAddImage](mta://scripting/client/functions/engineaddimage.md) ([5cdc04d](https://github.com/multitheftauto/mtasa-blue/commit/5cdc04d6d61f40e89a5da3d27ae9575f4a419a08) by **TheNormalnij**)

- Fixed [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) crash ([ae98b04](https://github.com/multitheftauto/mtasa-blue/commit/ae98b04753b54208961759b295bef44f0ffafe43) by **TheNormalnij**)

- Fixed crash when using [extinguishFire](mta://scripting/client/functions/extinguishfire.md) in [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md) event ([d6ae4e9](https://github.com/multitheftauto/mtasa-blue/commit/d6ae4e9e24b0b7de704a3cbeec25dfd661b4a3fc) by **FileEX**)

- Fixed weapon models being invisible when using the jetpack with [setJetpackWeaponEnabled](mta://scripting/server/functions/setjetpackweaponenabled.md) ([a68c2c4](https://github.com/multitheftauto/mtasa-blue/commit/a68c2c4232c28c6ba5595a814b89be976c4fa9c3) by **FileEX**)

- Fixed animations validation to avoid crashes ([27a24b5](https://github.com/multitheftauto/mtasa-blue/commit/27a24b551d86c6fbf9ee308603f24b011e941399) by **G-Moris**)

- Fixed a bug where the "attacker" parameter is always nil in the [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md) event if the object is glass ([dca5e20](https://github.com/multitheftauto/mtasa-blue/commit/dca5e2065af4a0195526541f9a8285db0401616e) by **FileEX**)

- Fixed a bug where the [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md) event was not triggered if the glass was broken by an explosion ([dca5e20](https://github.com/multitheftauto/mtasa-blue/commit/dca5e2065af4a0195526541f9a8285db0401616e) by **FileEX**)

- Fixed a bug that prevented players from switching weapons with an active jetpack ([180fbc0](https://github.com/multitheftauto/mtasa-blue/commit/180fbc0b5fdba95450e7a519f78f7588849349bf) by **FileEX**)

- Fixed a bug where hitElement in the [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md) event was always nil for projectiles ([43cc7b3](https://github.com/multitheftauto/mtasa-blue/commit/43cc7b3e34eb4680120eb8ebf40d31d845850df2) by **FileEX**)

- Fixed a bug where hydra flares did not work with [createProjectile](mta://scripting/client/functions/createprojectile.md) ([2bdac16](https://github.com/multitheftauto/mtasa-blue/commit/2bdac16d1d868f396786fbfdcfa2595004e1fff5) by **FileEX**)

- Fixed inconsistent extra component names ([d4f8849](https://github.com/multitheftauto/mtasa-blue/commit/d4f884935626c638dca0f7f45c71cfb22c4e2d72) by **FileEX**)

- Fixed a bug where after changing the key in the bind settings, only the key for the "down" status changed, while the "up" key remained unchanged.([3ebefc3](https://github.com/multitheftauto/mtasa-blue/commit/3ebefc37951e24cbfb25035d99045d67571b5324) by **FileEX**)

- Maked frame graph scale accordingly to resolution ([e431474](https://github.com/multitheftauto/mtasa-blue/commit/e431474c676a253004a26d86fc9e1a6100d329d4) by **ffsPLASMA**)

- Fixed old [setElementModel](mta://scripting/shared/functions/setelementmodel.md) memory leak ([4e7afa2](https://github.com/multitheftauto/mtasa-blue/commit/4e7afa2586c6992a75ac5312378c1096d87148ae) by **tederis**)

- Fixed [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md) returns invalid *air_ressistance* property ([b51e111](https://github.com/multitheftauto/mtasa-blue/commit/b51e1116283e9ec453881d3c48229b96c6198d5a) by **FileEX**)

- Fixed missing states in [getPedControlState](mta://scripting/client/functions/getpedcontrolstate.md) ([3333a11](https://github.com/multitheftauto/mtasa-blue/commit/3333a115f1a14f00378161681aeba609b4e993c0) by **FileEX**)

- Fixed for randomly bright objects after weapon change  ([9b9120c](https://github.com/multitheftauto/mtasa-blue/commit/9b9120c73ec97bf1b2f24703889a62fc19326f1f) by **FileEX**)

- Fixed some small problems with Device Selection Dialog ([6f90880](https://github.com/multitheftauto/mtasa-blue/commit/6f90880bee4d9169d4eda5f6afc63f4ed1bf652f) by **forkerer**)

- Allow dynamic models to be created as buildings ([642438e](https://github.com/multitheftauto/mtasa-blue/commit/642438ec1302daba50b6f6069844e96cbaa31818) by **TheNormalnij**)

- Fixed crash when disconnecting from server after creating projectiles ([9ab6104](https://github.com/multitheftauto/mtasa-blue/commit/9ab6104d9c1ec246fde29ae6bf303ae5848bbbe1) by **TheNormalnij**)

- Allow client peds to enter/exit client vehicles ([#3678](https://github.com/multitheftauto/mtasa-blue/pull/3678), [67beec7](https://github.com/multitheftauto/mtasa-blue/commit/67beec77b06897552dc2c756c15283bfdc19b143) by **gownosatana** and **Tracer**)

- Use immersive dark mode on game window ([fd95204](https://github.com/multitheftauto/mtasa-blue/commit/fd9520498919ae191c718c49b2a5c742bbbf8239) by **FileEX**)

- Added damageable objects support for [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([21593b9](https://github.com/multitheftauto/mtasa-blue/commit/21593b9239765343ad5a4975c9f8424e571a036d) by **TheNormalnij**)

- Fixed crash with [setElementHealth](mta://scripting/shared/functions/setelementhealth.md) in [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md) event ([2d3397d](https://github.com/multitheftauto/mtasa-blue/commit/2d3397df56827f7c218689873f8b4741ea9af44e) by **FileEX**)

- Fixed [setPedControlState](mta://scripting/client/functions/setpedcontrolstate.md) is aborted when ped created/player join ([8117ebc](https://github.com/multitheftauto/mtasa-blue/commit/8117ebcb95d3e3c35c400ee073a6ebab81e3f9fb) by **FileEX**)

- Added **buildings** support to [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md) ([fe1dd06](https://github.com/multitheftauto/mtasa-blue/commit/fe1dd063170aef6a866bc241c305278a73200fdd) by **TheNormalnij**)

- Fixed unintended behavior for ped control states ([a38e6ac](https://github.com/multitheftauto/mtasa-blue/commit/a38e6acaf5c0fd83b5627660439f36d380cd26e6) by **Nico834**)

- Fixed SVG colors bug ([04f297b](https://github.com/multitheftauto/mtasa-blue/commit/04f297b7b1aecb3753c8fbfa19fa9627abf422b4) by **TheNormalnij**)

- Fixed "CEF Launcher" process remaining after closing MTA ([a6c0027](https://github.com/multitheftauto/mtasa-blue/commit/a6c00278a5329e3b2b870b298d78565b14a7bed2) by **botder**)

- Removed *login* cmd from chat history ([4639aea](https://github.com/multitheftauto/mtasa-blue/commit/4639aea8a5544bfa4460bfcc8bba1d5b032e931a) by **PlatinMTA**)

- Fixed in-game updater dialog incorrectly showing 0% progress ([40d9ac1](https://github.com/multitheftauto/mtasa-blue/commit/40d9ac11a9864d4f26c9eb1979e3a30ec0624061) by **Dutchman101**)

- Fixed invalid references counter to TXD after [engineSetModelTXDID](mta://scripting/client/functions/enginesetmodeltxdid.md) (top 1 crash according to players crash stats) ([1b7e9e8](https://github.com/multitheftauto/mtasa-blue/commit/1b7e9e82997fb4ac2eec5722d9134299902a16e6) by **TheNormalnij**)

- Fixed server cache memory leak on connecting to another server ([e347659](https://github.com/multitheftauto/mtasa-blue/commit/e3476592fc46dc28f9da98f525797ae94ebf3ec3) by **Lpsd**)

- Added the ability to set CPU affinity (CPU 0) in the **advanced** tab in the settings ([d04c92b](https://github.com/multitheftauto/mtasa-blue/commit/d04c92b24e7b85f6015fa93192ddda06e9023c85) by **FileEX**)

- Fixed crash in *CClientDisplayManager* (top 2 crash according to players crash stats) ([0df0a4b](https://github.com/multitheftauto/mtasa-blue/commit/0df0a4b40f7aea7c16473d0844a03fcece888420) by **Lpsd**)

- Set main menu FPS limit to current display refresh rate ([acbcc8e](https://github.com/multitheftauto/mtasa-blue/commit/acbcc8e03ba8ac677a9c2c8182fb6f24868cae46) by **samr46**)

- [setSoundEffectParameter](mta://scripting/client/functions/setsoundeffectparameter.md) and [getSoundEffectParameters](mta://scripting/client/functions/getsoundeffectparameters.md) can be now used also on players! ([20851ec](https://github.com/multitheftauto/mtasa-blue/commit/20851ecf7d69cc42fc00a62446a87d7e99c1e19d) by **tederis**)

- Fixed elements sometimes being visible from other dimensions in the current dimension ([9af03b3](https://github.com/multitheftauto/mtasa-blue/commit/9af03b3263a5a320e2f92140f6caa6c94b9fe9a5), [1dff560](https://github.com/multitheftauto/mtasa-blue/commit/1dff560099459bc1b8248ef50643886158b0d731) by **FileEX** & **tederis**)

- Fixed bug "Copying text from CEF Browser shows Chinese characters in console" ([892beb0](https://github.com/multitheftauto/mtasa-blue/commit/892beb0457b461d5afd5d91e86763181bdb972d3) by **ColombuxMaximus**)

- Fixed a bug where hidden vehicle components became visible after changing the variant or handling ([1d81347](https://github.com/multitheftauto/mtasa-blue/commit/1d81347ee7e2614cd94e4b1807947d2c98b3305f) by **ColombuxMaximus**)

- Fixed persian characters in main menu & CEGUI ([efb2edf](https://github.com/multitheftauto/mtasa-blue/commit/efb2edfa853aa9a95f39ed9a843c3230b2e627cf) by **tzwer**)

- Added new movement states to [getPedMoveState](mta://scripting/client/functions/getpedmovestate.md) and fixed incorrect returning of "fall" ([c43c1b9](https://github.com/multitheftauto/mtasa-blue/commit/c43c1b98b8ec0b7253d98c65b405ead482a765d8), [797331f](https://github.com/multitheftauto/mtasa-blue/commit/797331fadbca4367f6cfd43633e48af44a99a115) by **FileEX**)

- Fixed a bug where friendly fire did not prevent fire damage ([9c43977](https://github.com/multitheftauto/mtasa-blue/commit/9c4397707dd2a94d8a6124d6b502d39793f0d2ba) by **FileEX**)

- Fixed [engineReplaceModel](mta://scripting/client/functions/enginereplacemodel.md) memory leak & potential crash ([1dbbfd0](https://github.com/multitheftauto/mtasa-blue/commit/1dbbfd025c5ff791f31e1ef4f255514198f88d0c) by **FileEX**)

- Fixed **ALT + F4** not working ([93963a9](https://github.com/multitheftauto/mtasa-blue/commit/93963a98f24fdb5e8374baaddaa6d99260be967e) by **lopezloo**)

- Fixed [setPedOnFire](mta://scripting/shared/functions/setpedonfire.md) doesn't cancel **TASK_SIMPLE_PLAYER_ON_FIRE** ([2a2f31b](https://github.com/multitheftauto/mtasa-blue/commit/2a2f31bccd9d90adfc2b03f1f63248b9d016c725) by **FileEX**)

- Fixed crash related to buildings ([4bcded5](https://github.com/multitheftauto/mtasa-blue/commit/4bcded5c89caffd005b266021d3c1bbd83a554cb) by **tederis**)

- Fixed client freeze in some locations on the map ([3a376e4](https://github.com/multitheftauto/mtasa-blue/commit/3a376e479201b30b27488a5a674d7d816397e79a) by **tederis**)

- Added disconnect warning when using quick connect while connected to server ([be39566](https://github.com/multitheftauto/mtasa-blue/commit/be395665c0f5094793b923e9f4fb94056ccff961) by **omar-o22**)

- Added missing trashcan in help section ([853a7d5](https://github.com/multitheftauto/mtasa-blue/commit/853a7d54a25bc09ee421ac837f22201882ece1b7) by **omar-o22**)

- Fixed [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) not working with building element type ([5ad35b4](https://github.com/multitheftauto/mtasa-blue/commit/5ad35b46004f4e758348a1a0c0b1024d4becb3c4), [24bd218](https://github.com/multitheftauto/mtasa-blue/commit/24bd2187c099a60881cabb001fbb6bb326044c81) by **PlatinMTA** and **omar-o22**)

- Fixed [getElementDistanceFromCentreOfMassToBaseOfModel](mta://scripting/client/functions/getelementdistancefromcentreofmasstobaseofmodel.md) not working with building element type ([20d36cd](https://github.com/multitheftauto/mtasa-blue/commit/20d36cd3ef687108acf99f97b02965fa5dd6003b) by **omar-o22**)

- Added ability to remove all domains from whitelist and blacklist ([280b6cd](https://github.com/multitheftauto/mtasa-blue/commit/280b6cd9917eb8e624fa037f3783eb958123a7a2) by **omar-o22**)

### Server

- Fixed bullet sync check in CBulletsyncPacket by verifying total ammo instead of clip ammo ([ca06762](https://github.com/multitheftauto/mtasa-blue/commit/ca06762413833e1c7f8d17970334607763414a45) by **shadylua**)

- Check deprecated account name length on [banPlayer](mta://scripting/server/functions/banplayer.md) to fix all players getting kicked ([b5e2332](https://github.com/multitheftauto/mtasa-blue/commit/b5e2332ca5857f3e984467ca0cb8163ec998ea06) by **patrikjuvonen**)

- Fixed a crash in CHandlingManager ([b6867a0](https://github.com/multitheftauto/mtasa-blue/commit/b6867a0d2ed0b4ab12a4461c3f1ca7d667bdedbc) by **Olya-Marinova**)

- Removed min-version lua function from old MTA versions ([222b272](https://github.com/multitheftauto/mtasa-blue/commit/222b2720c93f29977fffb722f8d42ea3fb5f790d) by **Olya-Marinova**)

- Disallow loadstring by default ([89e2d37](https://github.com/multitheftauto/mtasa-blue/commit/89e2d375d12deb026ee91fedc5e1ced04dc9a723) by **srslyyyy**)

- Added valid values for 'donotbroadcastlan' setting ([f8d4422](https://github.com/multitheftauto/mtasa-blue/commit/f8d4422ad75c0d7f21894f9f868aa37ec6993a35) by **Dark-Dragon**)

- Fixed "ped revives when syncer changes" ([af604ae](https://github.com/multitheftauto/mtasa-blue/commit/af604ae7dfec742661206fb809f149140ce3a960) by **Zangomangu**)

- Fixed files not unloading after renaming ([2846e27](https://github.com/multitheftauto/mtasa-blue/commit/2846e2794af1d9d441b7b988f49af521bd765fb0) by **W3lac3**)

- Added ability to limit client triggered events via [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) ([eae47fe](https://github.com/multitheftauto/mtasa-blue/commit/eae47fe2f432d9053c425fd515ea27f963c254ec) by **Lpsd**)

- Added FileExists check to CMainConfig::AddMissingSettings ([1ebaa28](https://github.com/multitheftauto/mtasa-blue/commit/1ebaa28e0381fb114b946f2f5a4d4bc5834ebd03) by **Lpsd**)

- Added server side weapon related checks ([86448ea](https://github.com/multitheftauto/mtasa-blue/commit/86448ea52c7ee13e554a907c424aa3c891e51e31) by **NanoBob**)

- Added [dbConnect](mta://scripting/server/functions/dbconnect.md) option for MySQL *"use_ssl=0"* ([e647676](https://github.com/multitheftauto/mtasa-blue/commit/e6476767a9b6848467f0d123830dd2f90bd4442d) by **Lpsd**)

- Added *content* parameter to [onPlayerPrivateMessage](mta://scripting/server/events/onplayerprivatemessage.md) event ([79f8ed6](https://github.com/multitheftauto/mtasa-blue/commit/79f8ed6a374d62e5cf1ec707b2ba25e3a959f509) by **FileEX**)

- Fix ability to move server-side vehicles that are far away from the player. New parameter can be set in the [mtaserver.conf](mta://reference/misc/server-mtaserver-conf.md) ([e3338c2](https://github.com/multitheftauto/mtasa-blue/commit/e3338c2fbbdb500c4ce28dc0677ceadef1f1ca4c) by **MegadreamsBE**)

- Added *sync* parameter for vehicles ([f88d313](https://github.com/multitheftauto/mtasa-blue/commit/f88d31306d3c7fadfbc1542c85922612fd00b131) by **znvjder**)

- Fixed server-side pickup collision size ([49d9751](https://github.com/multitheftauto/mtasa-blue/commit/49d97513e1eb2e0c96c5aa5a1d542d14131edd76) by **Proxy-99**)

- Fixed *CSimBulletsyncPacket* crash ([ee8bc92](https://github.com/multitheftauto/mtasa-blue/commit/ee8bc92907a112a5584844329dbb07cc82326ad1) by **G-Moris**)

- Fixed onVehicleExit doesn't trigger if pulled out ([af4f7fa](https://github.com/multitheftauto/mtasa-blue/commit/af4f7facca73bb68238437e6eff3504bd6f1cfe0) by **Proxy-99**)

- Fixed arguments in [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md) being ignored when nil was passed ([f6f544e](https://github.com/multitheftauto/mtasa-blue/commit/f6f544e6b54054a06497fdf94cd077b862af8055) by **FileEX**)

- Fixed Sirens not removed correctly ([9e41962](https://github.com/multitheftauto/mtasa-blue/commit/9e419620069ec8ad5828c50295c1901685166cf9) by **Proxy-99**)

- Fixed a bug where [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md) did not update data in [getPedWeapon](mta://scripting/shared/functions/getpedweapon.md) and [getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md) ([9615523](https://github.com/multitheftauto/mtasa-blue/commit/9615523faf84f584179412fb8e0cc04f9f4ee48f) by **FileEX**)

- Added **player** parameter to [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md) ([1ec1f5b](https://github.com/multitheftauto/mtasa-blue/commit/1ec1f5be69d3ef99bd2e26fd3d008a7cecd0a5ad) by **FileEX**)

- Excluded **meta.xml** from glob patterns for security reasons ([78f6d66](https://github.com/multitheftauto/mtasa-blue/commit/78f6d669adc97c51a825250dd4dbf1a4a4a0ff15) by **FileEX**)

- Fixed the bug where changing a vehicle to one with a different number of seats caused passengers to experience network trouble ([1fcd732](https://github.com/multitheftauto/mtasa-blue/commit/1fcd732ca9031060602c8e2425e40ce602d35253) by **FileEX**)

- Glob patterns added to meta.xml for HTML files ([7e6b4d0](https://github.com/multitheftauto/mtasa-blue/commit/7e6b4d02ec113b7ce3a6fd9937a6e8ad0a1ad9cb) by **FileEX**)

- Fixed console not maintaining position & size when GUI skin changed ([[1]](https://github.com/multitheftauto/mtasa-blue/commit/30d8e6dbfe75db47cf396aa909f43c24c4dbe127) by **NanoBob**)

- Added **includeCustom** argument for [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md) clientside ([[2]](https://github.com/multitheftauto/mtasa-blue/commit/889567a7a0ecb8a8b8d938826d2395ef9f43a76b) by **Fernando-A-Rocha**)

- Fixed **min_mta_version** tag for server ([8c0a01b](https://github.com/multitheftauto/mtasa-blue/commit/8c0a01bac62ecc3e9510133dee9f8d6700065f03) by **Fernando-A-Rocha**)

- Allowed user to pass multiple resource names to start/stop/restart ([6f5fb9c](https://github.com/multitheftauto/mtasa-blue/commit/6f5fb9c65ee93a5c1692b0d3516a483dcea48f08) by **botder**)

- Added sync peds/players animations for new players ([b32eafc](https://github.com/multitheftauto/mtasa-blue/commit/b32eafc70816ece8ad995d98d380d8f6e9950475) by **FileEX**)

- Optimized processing big files by server ([cb90339](https://github.com/multitheftauto/mtasa-blue/commit/cb90339aad461d3ee8c1008f2da10934afc38a4c) by **AlexTMjugador**)

- Separate icon for *mta-server.exe* ([6cb9d3e](https://github.com/multitheftauto/mtasa-blue/commit/6cb9d3edf9686749e524f136985cefb53772898e) by **Nico834**)

- Fixed a bug that caused warnings in debugscript when using depracated function names as variable names ([f23e395](https://github.com/multitheftauto/mtasa-blue/commit/f23e39521b7e35ad5389e467360fbc525c099887) by **YelehaUwU**)

- [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md) can now be cancelled! ([fcb5b03](https://github.com/multitheftauto/mtasa-blue/commit/fcb5b038981066f561f3792c2ae3d97d76d9d0fe) by **Nico834**)

- Added **eventName** parameter to [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md) ([76d7764](https://github.com/multitheftauto/mtasa-blue/commit/76d7764c7ec408b77eb7b12379e88882e014527f) by **ColombuxMaximus**)

### More Technical Changes and Bug Fixes

Click to collapse [-]

- Updated CLuaFunctionParser.h ([55647f4](https://github.com/multitheftauto/mtasa-blue/commit/55647f4023c78a846870f7c96069fab411cff5c5) by **Xenius97**)

- Fixed build after above update ([9dcc651](https://github.com/multitheftauto/mtasa-blue/commit/9dcc651d42ae78b7b04257e7612c5b594cb0fffd) by **Pirulax**)

- Fixed std::unordered_map<std::string, std::string> parsing ([0055924](https://github.com/multitheftauto/mtasa-blue/commit/005592417b42de63c3d8ba9c572a81cdc8f96164) by **tederis**)

- Addendum to [#3251](https://github.com/multitheftauto/mtasa-blue/pull/3251) ([9544a34](https://github.com/multitheftauto/mtasa-blue/commit/9544a34a28d3b4e766d7d07a44d63a8fe45dc506) by **Lpsd**)

- Fixes for [#3251](https://github.com/multitheftauto/mtasa-blue/pull/3251) ([07013d2](https://github.com/multitheftauto/mtasa-blue/commit/07013d24766a6259f4115bd0349a86f790dbf5d0) by **Lpsd**)

- Fixed SetStreamingBufferSize possibly accessing memory out-of-bounds ([e08b84f](https://github.com/multitheftauto/mtasa-blue/commit/e08b84fbfe6ad0431605b31c2ba5a50a8f116dc9) by **Pirulax**)

- Added a check to verify itemList validity ([6680737](https://github.com/multitheftauto/mtasa-blue/commit/668073787fa6b952d0f1520e8ccae0999dbdba13) by **R4ven47**)

- Various code clean ups and refactors

- Removed COffsetsMP and EU addresses ([52b0115](https://github.com/multitheftauto/mtasa-blue/commit/52b0115a2d9157b7a153b5f24316ff6fd053e79b) by **Merlin**)

- Removed COffsets and EU addresses ([959141d](https://github.com/multitheftauto/mtasa-blue/commit/959141de324126245d2b5ebf029c924302ff64e9) by **Merlin**)

- Clean ups *multiplayer_sa* code ([3898204](https://github.com/multitheftauto/mtasa-blue/commit/38982043978dd1ec72230569a6d534792e7c18bd) by **CrosRoad95**)

- Removed old easter-egg & debug code ([b26f80c](https://github.com/multitheftauto/mtasa-blue/commit/b26f80c3d72d628d63807529b408be4b61a5be60), [530212f](https://github.com/multitheftauto/mtasa-blue/commit/530212f34fc44e95599ca5e39e608583ecdbb5cc) by **botder** and **Merlin**)

- Refactored entity hierarchy  ([fdaced0](https://github.com/multitheftauto/mtasa-blue/commit/fdaced046a9421a39de87b81eaf0f7de7c234c4b) by **Tracer**)

- Removed unused symbol from *CConsole* class ([4fe9084](https://github.com/multitheftauto/mtasa-blue/commit/4fe9084a2e5c5eeed4b0a9a30a07607c812e923b) by **Nico834**)

- Refactored *CLuaBlipDefs* ([d05d09b](https://github.com/multitheftauto/mtasa-blue/commit/d05d09be8b9bd1327e37631411fa1e3b16c4dbb7), [c278c12](https://github.com/multitheftauto/mtasa-blue/commit/c278c12debfd346377354017992543fc7cf6397b) by **FileEX**)

- Refactored *CLuaTeamDefs* ([74ffa1d](https://github.com/multitheftauto/mtasa-blue/commit/74ffa1d0138ab3d848b0e081ca265f18ae6c7bd8), [f37bbad](https://github.com/multitheftauto/mtasa-blue/commit/f37bbada1381370eeadabd4f4dde2a024ec48f5f) by **Nico834**)

- Removed dead *CAnimManagerSA* code ([d18d7d3](https://github.com/multitheftauto/mtasa-blue/commit/d18d7d35fb50fdeea3f70ad688a5857b29867185) by **G-Moris**)

- Refactored class hierarchy and removed VTBL hacks ([61d1caf](https://github.com/multitheftauto/mtasa-blue/commit/61d1caffb5bfa9c620c08d43280150906dd172d5) by **TheNormalnij**)

- Refactored *CWeaponSA* and *CPedSA* classes ([a3b7c85](https://github.com/multitheftauto/mtasa-blue/commit/a3b7c8519d0d167c66e70c8c7ed5d2f810b7ae39), [2526a7d](https://github.com/multitheftauto/mtasa-blue/commit/2526a7dd6cde545e600792dcac3ab1b8ece0edec) by **FileEX**)

- Cleaning up client Common.h and moving enums to separate files ([1e56571](https://github.com/multitheftauto/mtasa-blue/commit/1e56571479217f787b6444d48770f8aa69f14387) by **FileEX**)

- Addd Comments to Frame Rate Fixes in CMultiplayerSA_FrameRateFixes.cpp ([e4e6d1b](https://github.com/multitheftauto/mtasa-blue/commit/e4e6d1b5a9609cb093a191db405c61339d4280d2) by **Merlin**)

- Fixed build after CEF update ([9980252](https://github.com/multitheftauto/mtasa-blue/commit/9980252446a6869609b1afa1ae1168282a99cb17) by **TheNormalnij**)

- Bump chromedriver from 114.0.2 to 119.0.1 in /utils/localization/generate-images ([5d8d375](https://github.com/multitheftauto/mtasa-blue/commit/5d8d3756d98b0272687b87c30adca2961eee86c8))

- Bump axios from 1.4.0 to 1.6.1 in /utils/localization/generate-images ([ba01801](https://github.com/multitheftauto/mtasa-blue/commit/ba018013085058905aa789c4fa3f39c4ed32fc69))

- Fixed file lock after img:destroy ([c2ccfd2](https://github.com/multitheftauto/mtasa-blue/commit/c2ccfd2c648a2d3f33ead2169262c30533f79bac) by **TheNormalnij**)

- Bump follow-redirects from 1.15.2 to 1.15.6 in /utils/localization/generate-images ([437dbcd](https://github.com/multitheftauto/mtasa-blue/commit/437dbcd8024c5217c22ef0e38719f93f33f47ce5))

- Fix permission check in File.create method ([92144a4](https://github.com/multitheftauto/mtasa-blue/commit/92144a4d7383af09dfa05b7bcd3db09fa487e6fd) by **theSarrum**)

- mbedTLS fix for cURL 8.8.0 ([4f7e0d8](https://github.com/multitheftauto/mtasa-blue/commit/4f7e0d87ec04e44d2e47f5b869c2d7c765817c0f) by **Lpsd**)

- Discord RPC Tweaks ([8ef351e](https://github.com/multitheftauto/mtasa-blue/commit/8ef351eabe46fd50da096247d8b6fc74508cb911) by **theSarrum**)

- Fixed small overhead in argument parser for strings ([d20582d](https://github.com/multitheftauto/mtasa-blue/commit/d20582d770dfd2a1677d9981005b3b6d28fb8e4e) by **TheNormalnij**)

- Bump ws from 8.13.0 to 8.17.1 in /utils/localization/generate-images ([cc172fc](https://github.com/multitheftauto/mtasa-blue/commit/cc172fcae7654ead0d3530a4819c71f76205a175))

- Generic exception type for argument parser instead of std::invalid_argument ([2043acf](https://github.com/multitheftauto/mtasa-blue/commit/2043acfdb210a8f1158501e2fbb431b625bbf74d) by **tederis**)

- Added comments for hooks in CMultiplayerSA_CrashFixHacks.cpp ([0327cb1](https://github.com/multitheftauto/mtasa-blue/commit/0327cb1bef9b234451f8a22ece9c6c70fdc9adb0) by **FileEX**)

- Optimization handling ([e3a8bd9](https://github.com/multitheftauto/mtasa-blue/commit/e3a8bd96d4eccb30e439ba8bd4a2029d01586154), [5ac6c8a](https://github.com/multitheftauto/mtasa-blue/commit/5ac6c8adad9c9ffd4a1c299c7cd548713e485bd6) by **G-Moris**)

- Added ability to use varargs in ArgumentParser functions ([8c2f95a](https://github.com/multitheftauto/mtasa-blue/commit/8c2f95a5ffade0e7fb212b62282e69d7f433d36f) by **Tracer**)

- Fixed google-breakpad in newer GCC versions ([5508c7e](https://github.com/multitheftauto/mtasa-blue/commit/5508c7e4058ad9d29cacc9964f8e84df2c60d14f) by **Tracer**)

- Validate serial on player join ([84437e4](https://github.com/multitheftauto/mtasa-blue/commit/84437e49e6ebca758e1e87d93e7846f9aa99a673) by **Fernando-A-Rocha**)

- Extract TXD class ([fedd239](https://github.com/multitheftauto/mtasa-blue/commit/733683d70dc037fdcbb256fb17d86e93b) by **TheNormalnij**)

- Fixed a bug with desynchronization of the values of some fields of the *CTickRateSettings* structure ([af5b696](https://github.com/multitheftauto/mtasa-blue/commit/af5b6968e0a28dbde7d92f3828dead0f1a936eec), [514a3b3](https://github.com/multitheftauto/mtasa-blue/commit/514a3b36d09906f09bb32e900c39dc09b1c29d10) by **nweb**)

- Fixed *MinClientReqCheck* and improve resource upgrade ([f095410](https://github.com/multitheftauto/mtasa-blue/commit/f0954109c0644c551ae3ec1df4474d1857e4bed8) by **Fernando-A-Rocha**)

- Refactored and improved player map (F11) ([2c5cf32](https://github.com/multitheftauto/mtasa-blue/commit/2c5cf3226a573637b91d8b255d57113b7043dc28) by **Fernando-A-Rocha**)

- Fixed *CVector* optional arguments ([6a70cf7](https://github.com/multitheftauto/mtasa-blue/commit/6a70cf7def14db86980a499d0fdf4c63565915e1) by **Tracer**)

- Fixed memory overwriting by *EnumToString* & *StringToEnum* ([3ab068b](https://github.com/multitheftauto/mtasa-blue/commit/3ab068ba213abca718ace47ac3bb8df9e4b1c3fc) by **FileEX**)

- Allow using *std::variant* with several pointers ([9d776c8](https://github.com/multitheftauto/mtasa-blue/commit/9d776c8bfc2680fc28857fc0a5dc4a4e40d4c3bf) by **tederis**)

- Fixed argument parser not distinguishing arrays from maps ([d4388a2](https://github.com/multitheftauto/mtasa-blue/commit/d4388a2452f4427bd56c3d93b80d4ea74c05b6e5) by **FileEX**)

- Fixed crash with nested arrays/maps in new argument parser ([ca877d3](https://github.com/multitheftauto/mtasa-blue/commit/ca877d33471fabbe970cf03d9d6d9b3413b6daa1) by **tederis**)

## 13 Vendor Updates

### Client

- Updated libpng to 1.6.50 ([[3]](https://github.com/multitheftauto/mtasa-blue/commit/c24b39d41fd768337c3d336a944588d53dfaba44) by **Nico834**)

- Updatee CEF to 127.3.5+g114ea2a+chromium-127.0.6533.120 ([bca4dff](https://github.com/multitheftauto/mtasa-blue/commit/bca4dff8dc490328000d7653a9166704d859b7e5) by **Dutchman101**)

- Updated Unifont to 15.1.05 ([02115a5](https://github.com/multitheftauto/mtasa-blue/commit/02115a5c00e2480bbb3b829b655869e7436de955) by **Dutchman101**)

### Server

- Updated cURL to 8.14.1 ([[4]](https://github.com/multitheftauto/mtasa-blue/commit/7c27c20da7503c68234cde0b726f10a3dcdf85e3) by **Nico834**)

- Updated MySQL to 8.4.0 & OpenSSL to 3.3.1 ([a44d673](https://github.com/multitheftauto/mtasa-blue/commit/a44d673bb8731506418fdbaa6690b339a98d82c1) by **botder**)

- Updated SQLite to 3.46.0 ([30e31af](https://github.com/multitheftauto/mtasa-blue/commit/30e31af2ca1ae96e03386670a9df6db70336b968) by **Dutchman101**)

### Shared

- Updated mbedTLS to 3.6.4 ([[5]](https://github.com/multitheftauto/mtasa-blue/commit/45955dad5471f49e2784e37cbafd1b92196abe96) by **Nico834**)

- Updated 7-Zip Standalone plugins to 24.07 (24.7.0.0) ([9b979b2](https://github.com/multitheftauto/mtasa-blue/commit/9b979b2d5c7f4b885046a85d9895e58416563890) by **Dutchman101**)

- Updated freetype to freetype-37cefe3 (freetype/freetype@37cefe3) ([89e022c](https://github.com/multitheftauto/mtasa-blue/commit/89e022cb8586aba5bdacd7b56c7d45c9b7b95f97) by **Dutchman101**)

- Updated nvapi from r550 to r555 ([5fdcada](https://github.com/multitheftauto/mtasa-blue/commit/5fdcada80a18af530381b04f54c3c69b6988f479) by **Dutchman101**)

- Updated unrar to 7.0.9 ([ab9461b](https://github.com/multitheftauto/mtasa-blue/commit/ab9461be5777427261bc3a330acb4c0f5cdc2c8b) by **Dutchman101**)

- Updated FreeType to 2.13.2 ([a783e99](https://github.com/multitheftauto/mtasa-blue/commit/a783e994264d4e954489e31459505c53759ca7f1) by **Dutchman101**)

- Updated zlib from 1.2.13 to 1.3 ([0f37ac0](https://github.com/multitheftauto/mtasa-blue/commit/0f37ac0b18845e9f035d0ca45bbb41b9cd1aa979) by **Dutchman101**)

## Resources

### 46+ Changes and Bug Fixes

**admin**

- Removed execute code functionality for safety reasons ([507a049](https://github.com/multitheftauto/mtasa-resources/commit/507a04937524997410e450a6d4292974fa801bf8) by **srslyyyy**)

- Updated skins.xml ([b530648](https://github.com/multitheftauto/mtasa-resources/commit/b5306484a789cc59b05f4182505ac07df3d90e07) by **shadylua**)

- Fixed warnings ([d7b0202](https://github.com/multitheftauto/mtasa-resources/commit/d7b02022fa8168fc300dd562118100265cf0688b) by **jlillis**)

- Making the admin window focused ([33f7cc9](https://github.com/multitheftauto/mtasa-resources/commit/33f7cc938d243687fa36fa300ec588b2d057d02c) by **Proxy-99**)

- Resource settings button is only displayed if there are settings ([0224ef5](https://github.com/multitheftauto/mtasa-resources/commit/0224ef52c699f27bd6e0e6364fbc81ecd0ec345f) by **T-MaxWiese-T**)

- Fixed nil index error and removed invalid characters causing syntax errors ([7985739](https://github.com/multitheftauto/mtasa-resources/commit/79857393ddb42f52ee05cf5758d5fdc8c2ff845c) by **rad3sh**)

- Allow disabling/enabling default reporting system ([0dbb83d](https://github.com/multitheftauto/mtasa-resources/commit/0dbb83df7d3e9a20a2c897612db778bf4e395c92) by **Viude**)

- Updated clientcheckban setting to ban serial instead of IP ([fa5beb9](https://github.com/multitheftauto/mtasa-resources/commit/fa5beb96e10d9f30d9565ca212fe901f88e413a5) by **Viude**)

- Fixed that double clicking on a resource without setting opened the GUI settings window ([82d5b83](https://github.com/multitheftauto/mtasa-resources/commit/82d5b835b503594101a99041498501e19a433a79) by **T-MaxWiese-T**)

- Fixed gridlist bug in weapons/vehicles ([6ba5a88](https://github.com/multitheftauto/mtasa-resources/commit/6ba5a88b8a5da4a9df67f20347056754ea5a2c87) by **omar-o22**)

**admin2**

- Forward-ported permissions widget from admin1 and minor fixes ([25dcc4c](https://github.com/multitheftauto/mtasa-resources/commit/25dcc4c655de26de0a2d0eb1b55ef7f3b3f6725e) by **Dark-Dragon**)

- Fixed /report message viewer widget and minor fixes ([6dbdf2c](https://github.com/multitheftauto/mtasa-resources/commit/6dbdf2cf90d0e447879bea86942e01caf949b8f5) by **Dark-Dragon**)

- Refactored bans functionality ([d8c35b0](https://github.com/multitheftauto/mtasa-resources/commit/d8c35b0a38a295d119054c4328a892c4e26be358) by **jlillis**)

- Fixed messagebox not showing ([5afe024](https://github.com/multitheftauto/mtasa-resources/commit/5afe0247e6ca44c5754a2d9a6a0af7bc8b57f967) by **FileEX**)

- Added missing glitches and world properties ([6856aa0](https://github.com/multitheftauto/mtasa-resources/commit/6856aa075c8e5674379c2a89f355d8b167ab6fdb) by **FileEX**)

- Added content for "Users" sub-tab in the "Rights" tab ([3f8ecca](https://github.com/multitheftauto/mtasa-resources/commit/3f8ecca953cc3dfa84e4d1b38b6b4c41f323688b) by **FileEX**)

- Removed execute code functionality for safety reasons ([c4bc73a](https://github.com/multitheftauto/mtasa-resources/commit/c4bc73a2b088b98116ece27065cc7f5a1dced15b) by **jlillis**)

- Replaced checkboxes with a gridlist for glitches and special world properties ([1dcb295](https://github.com/multitheftauto/mtasa-resources/commit/1dcb2953757c6741c93b9c63db33c032183047bc) by **FileEX**)

- Added ability to change server configuration settings ([118d58e](https://github.com/multitheftauto/mtasa-resources/commit/118d58e383f631f111fe3f2463480182235c71d1) by **FileEX**)

- Added content for "Resources" sub-tab in the "Rights" tab ([f16577e](https://github.com/multitheftauto/mtasa-resources/commit/f16577e24ca9125eac5f2e96621077ad0d213b69) by **FileEX**)

- Making the admin window focused ([33f7cc9](https://github.com/multitheftauto/mtasa-resources/commit/33f7cc938d243687fa36fa300ec588b2d057d02c) by **Proxy-99**)

- Fixed panel bind bug after reconnect ([c96bdd5](https://github.com/multitheftauto/mtasa-resources/commit/c96bdd5297cf180f947596c1eded8929b4982e6c) by **ricksterhd123**)

- Added the new world special ([08ef1d0](https://github.com/multitheftauto/mtasa-resources/commit/08ef1d07ee44540d1f74737e4871288568222331) by **omar-o22**)

- Updated add ban GUI style ([52aec17](https://github.com/multitheftauto/mtasa-resources/commit/52aec17bda8b63be70f02385400cf649952ac3ea) by **omar-o22**)

**chatmanager**

- Added a new resource for chat handling and management ([4e45cb7](https://github.com/multitheftauto/mtasa-resources/commit/4e45cb75a8780b0c191031091a4fcd2d76442aa7), [3f0f0d0](https://github.com/multitheftauto/mtasa-resources/commit/3f0f0d09a640178e01de71fa9e9b2caa9c21bcfa) by **omar-o22** and **srslyyyy**)

**defaultstats**

- Don't re-apply stats on every respawn ([9fde199](https://github.com/multitheftauto/mtasa-resources/commit/9fde199ec5025052468df0255bf5c5011ef29718) by **Dutchman101**)

- Fixed issue where defaultstats did not set player stats correctly ([567d10c](https://github.com/multitheftauto/mtasa-resources/commit/567d10c552305dae3f57d5c422a34c25f22fdc12) by **MittellBuurman**)

**editor**

- Various fixes for local spawned or invalid elements ([4e3c579](https://github.com/multitheftauto/mtasa-resources/commit/4e3c57941cd789cff8d9ce240e99edca871a345d) by **chris1384**)

- Various bug fixes and improvements ([4674fa9](https://github.com/multitheftauto/mtasa-resources/commit/4674fa9c6dbff7a1073fb949cac44588c65df3fb) by **IIYAMA12**)

- Fixed rotation issues ([679c01b](https://github.com/multitheftauto/mtasa-resources/commit/679c01b93132050548a86dba25ead7feaf9d5a1f) by **Nico834**)

- Toggleable rotation mechanic and improve threshold ([83e2c79](https://github.com/multitheftauto/mtasa-resources/commit/83e2c79cbd959aa54c55d4220a5b4d38747e8353) by **chris1384**)

- Added missing objects and collisions ([4e83755](https://github.com/multitheftauto/mtasa-resources/commit/4e83755d51345c0dc8e2e0f2ddf61588bf854641) by **THEGizmoOfficial**)

**edf**

- Fixed massive lag after stopping *editor* resource ([4674fa9](https://github.com/multitheftauto/mtasa-resources/commit/4674fa9c6dbff7a1073fb949cac44588c65df3fb) by **IIYAMA12**)

**editor_main**

- Improvements ([5bf553f](https://github.com/multitheftauto/mtasa-resources/commit/5bf553f85cb9c53027814fe666268cb24ed66b2e), [e9b75fd](https://github.com/multitheftauto/mtasa-resources/commit/e9b75fd615922c7d70f4e435a05fa933dcb9d2a5) by **q8X**)

- Add xmlns namespace when saving map ([23fa3f3](https://github.com/multitheftauto/mtasa-resources/commit/23fa3f38f71c2f3d28780df1b3ce163ab2eaae84) by **omar-o22**)

**editor_gui**

- Fixed test panel issues ([e558c84](https://github.com/multitheftauto/mtasa-resources/commit/e558c846e8b0589997f342f431b36fdc371da000) by **chris1384**)

**fallout**

- Refactor & many improvements ([c733b69](https://github.com/multitheftauto/mtasa-resources/commit/c733b69a735d004235ba61b1201ac1412acc6482) by **IIYAMA12**)

**freeroam**

- Updated skins.xml ([cacbe40](https://github.com/multitheftauto/mtasa-resources/commit/cacbe40a805402dec3a62180b987d4b777817ea6) by **shadylua**)

- Added Walk styles ([4a18d75](https://github.com/multitheftauto/mtasa-resources/commit/4a18d7585a2fa45eaed18d4b4796744a235a23c5) by **shadylua**)

- Security improvements ([2ec9213](https://github.com/multitheftauto/mtasa-resources/commit/2ec92132036d0dc073279dda3c88d71f578d651f) by **IIYAMA12**)

- Fixed freezetime flickering ([b40f27b](https://github.com/multitheftauto/mtasa-resources/commit/b40f27be0274b641c2cddd4c75a6f86f73ea4941), [817aa1e](https://github.com/multitheftauto/mtasa-resources/commit/817aa1ea9130fbccb1a23b7410309af2f8a21ddc) by **ricksterhd123** and **jlillis**)

- Fixed map key bind interferes with race editor help ([e62bc54](https://github.com/multitheftauto/mtasa-resources/commit/e62bc5471433b347b16c15709d469209cf202390) by **MittellBuurman**)

- Fixed player blips staying visible after closing spawn map with F1 ([1a5031c](https://github.com/multitheftauto/mtasa-resources/commit/aaf2dd7ed7a0b6b6c6609a4ee5d8319101e8a674) by **omar-o22**)

**hedit**

- Added German localization  ([bc33634](https://github.com/multitheftauto/mtasa-resources/pull/568/commits/c58df8666fbccfb0be73f27c52aa680dae2f0c1a) by **shadylua**)

- Added Brazilian Portuguese localization  ([d1b85d7](https://github.com/multitheftauto/mtasa-resources/commit/d1b85d7dda45293ce497cf03f21eea2f59100b89) by **ricksterhd123**)

- Added Hungarian localization  ([53050dd](https://github.com/multitheftauto/mtasa-resources/commit/53050dd0bf73a164969480c9277fc3c6b0601b7e) by **Nico834**)

- Updated Turkish localization  ([3044d00](https://github.com/multitheftauto/mtasa-resources/commit/3044d00a796488870556b19b088ac505c332952c) by **mahlukat5**)

- Updated Spanish localization  ([b74c239](https://github.com/multitheftauto/mtasa-resources/commit/b74c2393cc15e403d4588ebb671659c16cc36269) by **kxndrick0**)

**internetradio**

- Fixed that the GUI window of the resource "internetradio" collides with the GUI window of the resource "helpmanager" ([313f3dd](https://github.com/multitheftauto/mtasa-resources/commit/313f3dde6b7cdb389f11f1a62a6d3e8c093c159f) by **T-MaxWiese-T**)

- Improvements ([a3c9e17](https://github.com/multitheftauto/mtasa-resources/commit/a3c9e17cf6b85374b5f9b5881937aee97da94745) by **srslyyyy**)

- Added attaching to vehicles ([3dd5cbd](https://github.com/multitheftauto/mtasa-resources/commit/3dd5cbd32f092337707277fbecc5ee54988e07fc) by **ds1-e**)

- Added admin commands ([https://github.com/multitheftauto/mtasa-resources/commit/5c160212e190f74461d65fac1668cda07a2d0b11](https://github.com/multitheftauto/mtasa-resources/commit/5c160212e190f74461d65fac1668cda07a2d0b11) by **ds1-e**)

- Added ability to show speaker owner ([6189fc1](https://github.com/multitheftauto/mtasa-resources/commit/6189fc1eefce29c8467c5a1093eaa8bfd8ed97f0) by **ds1-e**)

- Fixed playSound3D and track name showing in other dimensions ([d4c04db](https://github.com/multitheftauto/mtasa-resources/commit/d4c04db009cdd68913fdb47bbc73acd91e63f981) by **mateo-14**

- Added ability to edit the volume ([73ecb61](https://github.com/multitheftauto/mtasa-resources/commit/73ecb610fdc096926291e8c24c56eea7c43bb4d6), [254700c](https://github.com/multitheftauto/mtasa-resources/commit/254700cffdf5c6b054e8f6e17afb4b7342593a85) by **omar-o22** and **srslyyyy**)

**ip2c**

- Added missing fetchRemote aclrequest ([e1364c3](https://github.com/multitheftauto/mtasa-resources/commit/e1364c3ebcc956dbf7f61e2d89741837776edec2) by **Fernando-A-Rocha**)

- Added backed up file and .gitignore to ignore the real one (auto-updated) ([e182291](https://github.com/multitheftauto/mtasa-resources/commit/e182291a53c3c76a2cf45834ba313aa9d18c16f4) by **Fernando-A-Rocha**)

**ipb**

- Replaced the onClientResource start event with the onPlayerResourceStart event ([cca3a05](https://github.com/multitheftauto/mtasa-resources/commit/cca3a05adf7fc940b913453a5fad5d5f3c8e3518) by **srslyyyy**)

**parachute**

- Fixed warnings about min_mta_version ([b4119cc](https://github.com/multitheftauto/mtasa-resources/commit/b4119cca4665d63a3043f14c1624ce9c96700b96) by **NetroX1993**)

**playerblips**

- Fixed that the resource "playercolors" should be activated for teams ([2cd28db](https://github.com/multitheftauto/mtasa-resources/commit/2cd28db5fa891f361c5af07a491532378a820b83) by **T-MaxWiese-T**)

- Real-time update of settings ([9505b18](https://github.com/multitheftauto/mtasa-resources/commit/9505b181fe7fc2bab53142746f73bc64a8fd984d) by **Nico834**)

- Improved debug messages ([4084e5d](https://github.com/multitheftauto/mtasa-resources/commit/4084e5d369907d3ededd1b2eb19c916983680154) by **T-MaxWiese-T**)

- Fixed that when a player changed or joined teams the color of the blip was not updated ([ff80005](https://github.com/multitheftauto/mtasa-resources/commit/ff80005f114a3d010624f7d54510ffde47dddb00) by **T-MaxWiese-T**)

**playercolors**

- Player nametag color should revert to team color when the resource is stopped ([d45d2d0](https://github.com/multitheftauto/mtasa-resources/commit/d45d2d0cd963186639d76ab1cb27ef6a042cd0bd) by **T-MaxWiese-T**)

- Fixed chat messages sent twice ([0547cf7](https://github.com/multitheftauto/mtasa-resources/commit/0547cf72514a7dc7efc987f47903c35b310a3b22) by **Fernando-A-Rocha**)

**performancebrowser**

- Fixed player names not being reinitialized on change ([3e0166d](https://github.com/multitheftauto/mtasa-resources/commit/3e0166dc7fa9c11c596a7958b02423b6aeff8410) by **YelehaUwU**)

**runcode**

- Added aclrequest for loadstring function ([c40b809](https://github.com/multitheftauto/mtasa-resources/commit/c40b8095f054b6e87b46e1d53d9b6ec77cf943c7) by **IIYAMA12**)

**scoreboard**

- Replaced drawing arrow from path to texture ([128f269](https://github.com/multitheftauto/mtasa-resources/commit/128f26952810804df6acb233ca9476853caa1286) by **srslyyyy**)

**speedometer**

- Display at resource start ([31a5ac4](https://github.com/multitheftauto/mtasa-resources/commit/31a5ac4013c3633647178e695474da6632eb38b8) by **Nico834**)

- Preventing pointer overflow ([8689cdc](https://github.com/multitheftauto/mtasa-resources/commit/8689cdc247a3fd16125524aac04eb054c398084c) by **Nico834**)

**superman**

- Fixes and improvements ([2b3bc10](https://github.com/multitheftauto/mtasa-resources/commit/2b3bc102225b2f1c3144cffe290175e9a2c71728), [e1c06c3](https://github.com/multitheftauto/mtasa-resources/commit/e1c06c3c2581c16a6e05401381263a47dd6ac5f0), [1e4319d](https://github.com/multitheftauto/mtasa-resources/commit/1e4319d180be0f482d42f2f32fbf2c1e5cd440cc) by **ds1-e**)

- Fixed a bug where you couldn't move after death while Superman is active ([715ee57](https://github.com/multitheftauto/mtasa-resources/commit/715ee57664287083f7ecb299f534bc3093f796a0) by **omar-o22**)

**votemanager**

- Fixed lint error ([c863007](https://github.com/multitheftauto/mtasa-resources/commit/c8630075317123e510645464a3bf56ebb244573b) by **Dark-Dragon**)

**mapfixes**

- A new resource has been added that fixes many holes and bugs in the default map ([23f6bd9](https://github.com/multitheftauto/mtasa-resources/commit/23f6bd94370440af5ed79a47bda1ff0caf92fa8e) by **Fernando-A-Rocha**)

**gps**

- Added export functions for custom logic ([537d92d](https://github.com/multitheftauto/mtasa-resources/commit/537d92d11b357cf9e795a7bb3ec87c13fa62c7bc) by **T-MaxWiese-T**)

**deathmatch**

- Improvements and update ([a01ec8a](https://github.com/multitheftauto/mtasa-resources/commit/a01ec8a86e636ca61f25a03d4ee30bd898754cbd), [b94ffdd](https://github.com/multitheftauto/mtasa-resources/commit/b94ffddfd5b230544d54e5eca8c9c5d87dc69128) by **jlillis**

**race**

- Fixed automatic nextid assignment breaking ([2c695a9](https://github.com/multitheftauto/mtasa-resources/commit/2c695a9e793825a8cafd2ee3be490d2d8e9ad318) by **lotsofs**)

**voice_local**

- Improvements ([53cf63d](https://github.com/multitheftauto/mtasa-resources/commit/53cf63d83169018e0de9f45ecb565958855d717d) by **Fernando-A-Rocha**)

**Others / Uncategorized**

- Refactor of resources meta.xml ([6713b07](https://github.com/multitheftauto/mtasa-resources/commit/6713b07a459739c06112ac3e608776f3f0696144) by **Fernando-A-Rocha**)

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
