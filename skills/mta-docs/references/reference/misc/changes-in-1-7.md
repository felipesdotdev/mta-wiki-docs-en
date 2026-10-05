---
doc_id: "mta-wiki:14593"
title: "Changes in 1.7"
source_title: "Changes in 1.7"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.7"
revision_id: 82914
language: "en"
categories: ["Changelog", "Incomplete"]
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

## Platform requirements

MTA:SA 1.7 requires Windows 10 or later. Windows 7 and 8.x are no longer supported by this release. 32-bit x86 server builds have been removed; the client remains 32-bit. ([e0d8ccd](https://github.com/multitheftauto/mtasa-blue/commit/e0d8ccdf9509f03a15af86ad97aaf7da71975fde))

## 4 Deprecations

These changes will take effect in this version and scripts may need to be manually upgraded when updating:

- Changed [base64Encode](mta://scripting/shared/functions/base64encode.md) and [base64Decode](mta://scripting/shared/functions/base64decode.md) to throw a warning on use, please upgrade to [encodeString](mta://scripting/shared/functions/encodestring.md) and [decodeString](mta://scripting/shared/functions/decodestring.md) instead ([30a83b0](https://github.com/multitheftauto/mtasa-blue/commit/30a83b0af164fb6920a2a60e089d08a6f5622f7d) by **Nico834**)

- Changed [setHelicopterRotorSpeed](mta://scripting/client/functions/sethelicopterrotorspeed.md) and [getHelicopterRotorSpeed](mta://scripting/client/functions/gethelicopterrotorspeed.md) to throw a warning on use, please upgrade to [setVehicleRotorSpeed](mta://scripting/client/functions/setvehiclerotorspeed.md) and [getVehicleRotorSpeed](mta://scripting/client/functions/getvehiclerotorspeed.md) instead ([82000c3](https://github.com/multitheftauto/mtasa-blue/commit/82000c34830b51ace2d14e39f3b487feb1aac1da) by **FileEX**)

- Changes [setPedOnFire](mta://scripting/shared/functions/setpedonfire.md) and [isPedOnFire](mta://scripting/shared/functions/ispedonfire.md) to throw a warning on use, please upgrade to [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md) and [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md) instead ([7ad96e2](https://github.com/multitheftauto/mtasa-blue/commit/7ad96e2e78fe41f8924d3f105b1683f7363c6fcb) by **FileEX**)

- Changes [removeAllGameBuildings](mta://scripting/client/functions/removeallgamebuildings.md) and [restoreAllGameBuildings](mta://scripting/client/functions/restoreallgamebuildings.md) to throw a warning on use, please upgrade to [removeGameWorld](mta://scripting/client/functions/removegameworld.md) and [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md) instead ([d7adae6](https://github.com/multitheftauto/mtasa-blue/commit/d7adae68791ce237704acc06bf794b5fbda96f95#diff-93c130ddb85da32121129a437ac5b28ba16fa17f6e3506e4cddfb7bc3d8eb9fbR180) by **TheNormalnij**)

## Notable Changes

- Support for Discord Rich Presence ([fdaa3ac](https://github.com/multitheftauto/mtasa-blue/commit/fdaa3aca3e233c7aba69d0fd5f85e78288a4401a), [ef26810](https://github.com/multitheftauto/mtasa-blue/commit/ef26810df4542283fee8edcc165bc9be22f2ca98), [acfbd40](https://github.com/multitheftauto/mtasa-blue/commit/acfbd40df1ff1432ea1d6663c005d43fce22899c) by **znjvder**, **tederis**, **patrikjuvonen** and **Deihim007**)

- Added support for [Building](https://wiki.multitheftauto.com/wiki/Building)'s ([81242ed](https://github.com/multitheftauto/mtasa-blue/commit/81242edb9295efbf4bf8b198b12d577a0877aec2), [eb6b18a](https://github.com/multitheftauto/mtasa-blue/commit/eb6b18a5d49a7f0f34bdbf42b15f933e42876cf8) by **TheNormalnij**)

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

These are some statistics since the [previous release](https://wiki.multitheftauto.com/wiki/Changes_in_1.6.0).

- This is the **28th** 1.x.x release

- **1,207** days

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

**Note:** Last update to these statistics was made 914 days ago.

## 97 New Features

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

- New and updated [object](https://wiki.multitheftauto.com/wiki/Object) functions

- **[Updated]** Added [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md) to server-side ([7c939ad](https://github.com/multitheftauto/mtasa-blue/commit/7c939adb892c08836462a78cd9b987884cdb49ee) by **FileEX**)

- **[Updated]** Added [breakObject](mta://scripting/shared/functions/breakobject.md) to server-side ([aa1a785](https://github.com/multitheftauto/mtasa-blue/commit/aa1a7853f46fc796a94f38b7df2a5293fb941ba2) by **FileEX**)

- **[Updated]** Added [respawnObject](mta://scripting/shared/functions/respawnobject.md) and [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md) to server-side ([9d65bb6](https://github.com/multitheftauto/mtasa-blue/commit/9d65bb673c4df16def27e97a4af74d3b0c7eedc9) by **FileEX**)

- **[New]** Added [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md) ([9d65bb6](https://github.com/multitheftauto/mtasa-blue/commit/9d65bb673c4df16def27e97a4af74d3b0c7eedc9) by **FileEX**)

- New **file-path** functions

- Added [pathListDir](mta://scripting/shared/functions/pathlistdir.md), [pathIsFile](mta://scripting/shared/functions/pathisfile.md) and [pathIsDirectory](mta://scripting/shared/functions/pathisdirectory.md) ([74781c6](https://github.com/multitheftauto/mtasa-blue/commit/74781c6295b5b6dc81cd95d4cfab7900d88d7524) by **Tracer**)

- New [marker](https://wiki.multitheftauto.com/wiki/Marker) functions

- Added [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md) and [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md) ([071378e](https://github.com/multitheftauto/mtasa-blue/commit/071378ec4326408a9520c79c96befca995d097f6) by **FileEX**)

- New [timer](mta://reference/misc/timer.md) functions

- Added [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md) and [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md) ([69aa420](https://github.com/multitheftauto/mtasa-blue/commit/69aa420f21fde3ac56e3d3bbc62ef0f060295c0a) by **jvstns**)

- New and updated **world** functions

- **[New]** Added [resetWorldProperties](mta://scripting/shared/functions/resetworldproperties.md) ([6df889e](https://github.com/multitheftauto/mtasa-blue/commit/6df889e78328b80f8e4bdc02f8761472cf87c54c) by **FileEX**)

- **[Updated]** Added [isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md) and [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) also to server-side ([938b306](https://github.com/multitheftauto/mtasa-blue/commit/938b306add48245e578ba6036f1a77521e277194) by **samr46**)

- New and updated [vehicle](https://wiki.multitheftauto.com/wiki/Vehicle) functions

- **[New]** Added [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md) ([9f54cfc](https://github.com/multitheftauto/mtasa-blue/commit/9f54cfcd7a584f413db731052ebed921acfc71ea) by **FileEX**)

- **[Upated]** Added [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md) to server-side ([e9e5819](https://github.com/multitheftauto/mtasa-blue/commit/e9e5819c394987de2b9a5d581c4df9fd47057d9d#diff-49b4b89bf4463f38e70a325131b4da66457d783b1401dde0ffbad723624f8612R130) by **Proxy-99**)

- **[Updated]** Added [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md) and [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md) to client-side ([682cdca](https://github.com/multitheftauto/mtasa-blue/commit/682cdca3c37248a9e725b461ba322db413653f25) by **Proxy-99**)

- Updated [player](https://wiki.multitheftauto.com/wiki/Player) functions

- Added [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md) to client-side ([8403da5](https://github.com/multitheftauto/mtasa-blue/commit/8403da54ecfd20d6b9740fb79d90ac936d316112) by **Nico834**)

- Updated [ped](https://wiki.multitheftauto.com/wiki/Ped) functions

- Added [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md) to server-side ([e71f482](https://github.com/multitheftauto/mtasa-blue/commit/e71f4828b46bb69b9622a11d0f700a79f986ee9b) by **Nico834**)

- New [element](mta://reference/misc/element.md) functions

- Added [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md) and [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md) ([7ad96e2](https://github.com/multitheftauto/mtasa-blue/commit/7ad96e2e78fe41f8924d3f105b1683f7363c6fcb) by **FileEX**)

### Client

- Added cutscene-bone support to [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md), including facial and finger bones ([953ad6e](https://github.com/multitheftauto/mtasa-blue/commit/953ad6e08bb6754f23ed796174bb341e02bc9e0f) by **FileEX**)

- Added controller selection, separate trigger deadzone and saturation settings, and a vibration option ([b0d128a](https://github.com/multitheftauto/mtasa-blue/commit/b0d128acbe42564d2a4ab4d93e012410b47e7515) by **x6c85**)

- Enabled sirens for all vehicle types, including custom models ([1e35601](https://github.com/multitheftauto/mtasa-blue/commit/1e3560118a37190910b22ffc82ccec70d4dd88c7) by **Federico Romero**)

- Added an "Enable video acceleration" browser setting ([ddb9249](https://github.com/multitheftauto/mtasa-blue/commit/ddb92490288993d924bbff33d1e449e4c56d7bb4) by **lopsi**)

- Allowed local browsers to load existing files generated within their owning resource even when those files are not listed in meta.xml ([b2d8fb5](https://github.com/multitheftauto/mtasa-blue/commit/b2d8fb5aac02b13cfb78e287cc189c6df782a56c) by **Mohab**)

#### Functions

- Added a seat-number option to [setPedEnterVehicle](mta://scripting/client/functions/setpedentervehicle.md), while retaining the existing passenger flag ([7be6d05](https://github.com/multitheftauto/mtasa-blue/commit/7be6d053605b91a15509246eb966961e5d1a7af7) by **MohabCodeX**)

- Added [getResources](mta://scripting/server/functions/getresources.md) to client-side ([5ab1e03](https://github.com/multitheftauto/mtasa-blue/commit/5ab1e03469536f250992fc44dde84f203b882867) by **Xenius97**)

- Added [setSearchLightColor](mta://scripting/client/functions/setsearchlightcolor.md) and [getSearchLightColor](mta://scripting/client/functions/getsearchlightcolor.md) to control searchlight colour and alpha ([c40bae1](https://github.com/multitheftauto/mtasa-blue/commit/c40bae13feea134b77a2350e7b36254058a46321) by **FileEX**)

- Extended [getVehicleWheelFrictionState](mta://scripting/client/functions/getvehiclewheelfrictionstate.md) support to bikes, BMXs, quads, monster trucks and trailers ([e5b7f24](https://github.com/multitheftauto/mtasa-blue/commit/e5b7f24eef93384178cfdaa4b9f4b78c7ba6b8d0) by **Xenius97**)

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

- New [building](https://wiki.multitheftauto.com/wiki/Building) functions ([81242ed](https://github.com/multitheftauto/mtasa-blue/commit/81242edb9295efbf4bf8b198b12d577a0877aec2), [eb6b18a](https://github.com/multitheftauto/mtasa-blue/commit/eb6b18a5d49a7f0f34bdbf42b15f933e42876cf8) by **TheNormalnij**)

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

- New [ped](https://wiki.multitheftauto.com/wiki/Ped) functions

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

- New [player](https://wiki.multitheftauto.com/wiki/Player) functions

- Added [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md) ([03e851a](https://github.com/multitheftauto/mtasa-blue/commit/03e851a2f5ff2d917ba3c7a1c7577fdb5b8d2a6f), [5f21c32](https://github.com/multitheftauto/mtasa-blue/commit/5f21c32fb0725140d6d03476e08de330d429b55a) by **FileEX**)

- New **HUD** functions ([5ea0e0f](https://github.com/multitheftauto/mtasa-blue/commit/5ea0e0fb23b21750207b23191db92562cf9b822c) by **FileEX**)

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

- New [vehicle](https://wiki.multitheftauto.com/wiki/Vehicle) functions

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

- New [browser](https://wiki.multitheftauto.com/wiki/Browser) functions

- Added [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md) ([bfdfdb5](https://github.com/multitheftauto/mtasa-blue/commit/bfdfdb5f44726df85626e6e3e06c2a319c0c8962) by **Lpsd**)

- New **weapons** functions

- Added [setWeaponRenderEnabled](mta://scripting/client/functions/setweaponrenderenabled.md) & [isWeaponRenderEnabled](mta://scripting/client/functions/isweaponrenderenabled.md) ([efed59b](https://github.com/multitheftauto/mtasa-blue/commit/efed59b7dc7b076219f1c8a868ef8aa028582127) by **FileEX**)

#### Events

- Added the "down" state to [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md) for resources specifying a minimum client version of 1.7.0-7.26369 or later ([af669ac](https://github.com/multitheftauto/mtasa-blue/commit/af669acfdf703e5c100980a49edc029876c4c4cb), [539d0a2](https://github.com/multitheftauto/mtasa-blue/commit/539d0a21a49cad7980c3defb901440131d24c055) by **Xenius97, Marek Kulik**)

- Added [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md) ([b2cf029](https://github.com/multitheftauto/mtasa-blue/commit/b2cf02943924c4972d2a695cdbfd7c9873fc3cbb) by **Pieter-Dewachter**)

- Added [onClientBrowserConsoleMessage](mta://scripting/client/events/onclientbrowserconsolemessage.md) ([#3676](https://github.com/multitheftauto/mtasa-blue/pull/3676), [d296a65](https://github.com/multitheftauto/mtasa-blue/commit/d296a653c5ce2ecfd4f7150d74391b703b773baf) by **gownosatana** and **Tracer**)

### Server

- Added glob-pattern support for map files in [meta.xml](mta://reference/misc/meta-xml.md) ([d2a3176](https://github.com/multitheftauto/mtasa-blue/commit/d2a3176c05533c79701cfa1d15f5afaab8941f95) by **efejotaese2**)

#### Functions

- New [ACL](https://wiki.multitheftauto.com/wiki/ACL) functions

- Added [aclObjectGetGroups](mta://scripting/server/functions/aclobjectgetgroups.md) ([cf46bd8](https://github.com/multitheftauto/mtasa-blue/commit/cf46bd8487bdb2d0cafdab1f43936357f670fe10) by **Tracer**)

- New **acl-account** functions

- Added [getAccountType](mta://scripting/server/functions/getaccounttype.md) ([545f54b](https://github.com/multitheftauto/mtasa-blue/commit/545f54b6ae0bfc721abba12402ad3787ed9ae811) by **Tracer**)

- Added [setAccountSerial](mta://scripting/server/functions/setaccountserial.md) ([a0c2e41](https://github.com/multitheftauto/mtasa-blue/commit/a0c2e410f225ebd245a7c5b8031812cf94360097) by **camargo2019**)

- New [vehicle](https://wiki.multitheftauto.com/wiki/Vehicle) functions

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

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md) can now be cancelled. ([3ab39b8](https://github.com/multitheftauto/mtasa-blue/commit/3ab39b825cb47bc9aba14263157ff665ba1a576f) by **ArranTuna**)

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

## 340 Changes and Bug Fixes

### Shared

- Rejected non-finite velocity and turn velocity ([6b26ac8](https://github.com/multitheftauto/mtasa-blue/commit/6b26ac82932e02b88b17abbc1b985cab0c5557b3) by **Mohamed Maatallah**)

- Fixed [fromJSON](mta://scripting/shared/functions/fromjson.md) crashing with large input ([74ea654](https://github.com/multitheftauto/mtasa-blue/commit/74ea654a42cf4e47ea692bafbc94e6932104fe67) by **FileEX**)

- Fixed [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md) not removing nodes from saved XML files ([4abd727](https://github.com/multitheftauto/mtasa-blue/commit/4abd727de8784ee7eb7d66b46577e8624ee4581b) by **Batuhan Tonga**)

- Fixed [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md) bounds checks ([5f738e0](https://github.com/multitheftauto/mtasa-blue/commit/5f738e06914cd86fe74e9d619a7d3fc3cfea75b5) by **Havi**)

- Fixed nested-event cancel reason loss without breaking outer cancel ([b04e85d](https://github.com/multitheftauto/mtasa-blue/commit/b04e85dbe79e3ba8466935e1c6282746ecde0dc4) by **lopsi**)

- Completed element getter/setter support for building alpha and collisions, projectile alpha and freezing, and custom-weapon collision and frozen states ([ab69040](https://github.com/multitheftauto/mtasa-blue/commit/ab6904070b5c424c8c5b95e09cd58e0f2b5ab2c7) by **x6c85**)

- Restored [pregMatch](mta://scripting/shared/functions/pregmatch.md) capture-group extraction after the PCRE2 migration ([19eb8ca](https://github.com/multitheftauto/mtasa-blue/commit/19eb8ca93657f3b5924ec393569647be2eac7774) by **Mohab**)

- Fixed OOP APIs returning separate coordinates instead of Vector objects where vectors are expected ([7f28b3b](https://github.com/multitheftauto/mtasa-blue/commit/7f28b3b05b60489257523167911e7a7cf17ce47d) by **Batuhan Tonga**)

- Fixed bullet synchronization errors, duplicate shots and crashes, and improved validation of player and custom-weapon shots ([6b1d591](https://github.com/multitheftauto/mtasa-blue/commit/6b1d59186c474ae016ab0d8b174169947a4c6782) by **FileEX**)

- Fixed [onMarkerHit](mta://scripting/server/functions/onmarkerhit.md) not firing in interiors ([1c95abc](https://github.com/multitheftauto/mtasa-blue/commit/1c95abce23893764785f61553fda461622e010ac) by **Batuhan Tonga**)

- Removed the unintended 1 MB limit on latent events and allowed for packet overhead in event-size checks ([8cb1c89](https://github.com/multitheftauto/mtasa-blue/commit/8cb1c89caa2b145a7cbf8dac88b5861b8ca76959), [2189a0d](https://github.com/multitheftauto/mtasa-blue/commit/2189a0dbffb57a3f5996b1e58357b2ed028cb386) by **Xenius97**, **lopsi**)

- Improved voice packet handling and playback; fixed rejected packets, stuttering, lost speech, memory leaks, crashes and stalls, and hardened handling of abusive voice traffic ([f1683fd](https://github.com/multitheftauto/mtasa-blue/commit/f1683fda8c0082c7225ea19c3d8eafaec61d0ac7), [707593b](https://github.com/multitheftauto/mtasa-blue/commit/707593b59120310f5c15f797d79054a82f07fcc2), [0729ba8](https://github.com/multitheftauto/mtasa-blue/commit/0729ba82c0837b460fe8580d3647f3e5ae277239), [a452a49](https://github.com/multitheftauto/mtasa-blue/commit/a452a4978f03e4e950d906539c6b286ced63578c), [e520498](https://github.com/multitheftauto/mtasa-blue/commit/e520498205eef201243168867b00d36406cca29f), [9e28567](https://github.com/multitheftauto/mtasa-blue/commit/9e28567e9c73c9845a3aedb47c00623aa683fc35) by **Moriska Sosiska**, **lopsi**, **Dutchman101**)

- Improved nickname validation consistency on the client and server ([6c54a2d](https://github.com/multitheftauto/mtasa-blue/commit/6c54a2df44a4da07e43d774c5536cfd4b3458559), [7866eba](https://github.com/multitheftauto/mtasa-blue/commit/7866eba418ce9dd75c5e9ab2cf87fd35121f1cca) by **Dutchman101**)

- Fixed player damage information being omitted from vehicle synchronization ([5151689](https://github.com/multitheftauto/mtasa-blue/commit/5151689c60539cac150acaef0f35e707c3563b78) by **Bob**)

- Fixed building synchronization and resource ownership, swapped health/armour pickup values, and animation timing in entity-add packets ([59fa331](https://github.com/multitheftauto/mtasa-blue/commit/59fa3316314240aa1d2251b48e9be1c9695d4720) by **Bob**)

- Added safer recursive Lua table decoding and join-packet bit reads ([50ef80c](https://github.com/multitheftauto/mtasa-blue/commit/50ef80c05f09f3a14af896c020fe39cd87dce2a3), [5d1bd07](https://github.com/multitheftauto/mtasa-blue/commit/5d1bd0776588dae3c15674a0253cb7327e2964a9) by **Mohamed Maatallah**, **Dutchman101**)

- Fixed crashes when reading incomplete Lua arguments and tables from network packets ([c68e618](https://github.com/multitheftauto/mtasa-blue/commit/c68e6187573a8850332bcce65613b9cd7f117701), [7c349cf](https://github.com/multitheftauto/mtasa-blue/commit/7c349cfe4210b30551ac34700f61de5f074a2b54), [2e9d445](https://github.com/multitheftauto/mtasa-blue/commit/2e9d445fe456c925881df090e48c82e12006cd14) by **Dutchman101**)

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

- Fixed render-object leaks when changing ped models ([b416282](https://github.com/multitheftauto/mtasa-blue/commit/b4162826c7800239ea9adc5baab2fcbe64093172) by **Mohamed Maatallah**)

- Fixed texture-dictionary and animation-block reference leaks when replacing clump models ([c3f6fd3](https://github.com/multitheftauto/mtasa-blue/commit/c3f6fd3913ad710ac47be7a4902187ca7ded9d41) by **Mohamed Maatallah**)

- Fixed crash when playing SFX with invalid audio indices ([6e2cf0c](https://github.com/multitheftauto/mtasa-blue/commit/6e2cf0c4589261e9ff3c2a8998e685de4d37af7f) by **Havi**)

- Fixed CEF browser handling during screenshots ([08c5a46](https://github.com/multitheftauto/mtasa-blue/commit/08c5a46dac428d6d46c723d8bc503d4289fd1e89) by **Havi**)

- Fixed incorrect alpha blending in render targets ([1fe39e7](https://github.com/multitheftauto/mtasa-blue/commit/1fe39e791feaabcdc567c6670b22997cde5c822f) by **Pedro Henrique**)

- Fixed building pool resize corrupting the world ([495a8a0](https://github.com/multitheftauto/mtasa-blue/commit/495a8a0037d53918aff9cc606feb904e20c91937) by **Federico Romero**)

- Fixed players warping while being pulled out of vehicles ([65e9acf](https://github.com/multitheftauto/mtasa-blue/commit/65e9acf7ab162da997a6aabd8cb67ab3b49902da) by **Federico Romero**)

- Fixed stealth kill animation playing on the wrong ped/player ([bc13850](https://github.com/multitheftauto/mtasa-blue/commit/bc138501427f6565b61c423f776b99402cec21fd) by **Federico Romero**)

- Fixed streaming memory never scaling up for a large gta3.img ([f9315f8](https://github.com/multitheftauto/mtasa-blue/commit/f9315f8f58a0c82f960cb61a0c23534e4fa1d780) by **Flash**)

- Fixed [getPedTargetEnd](mta://scripting/client/functions/getpedtargetend.md) during drive-by ([bd43788](https://github.com/multitheftauto/mtasa-blue/commit/bd43788cd0693849a34da218ec8004c29c51c830) by **Mohab**)

- Fixed vehicle chassis sway at high framerates ([48d8c0a](https://github.com/multitheftauto/mtasa-blue/commit/48d8c0a8d877c952ac7dd61ef2c578ca1d6e1a4a) by **Mohab**)

- Fixed diving too deep and rising too slowly at high FPS ([f65cbbd](https://github.com/multitheftauto/mtasa-blue/commit/f65cbbd45c6ee7f46df07350a17b4cbae67e7fa9) by **Flash**)

- Fixed Ctrl getting stuck in the GUI after Ctrl+Alt ([cf640af](https://github.com/multitheftauto/mtasa-blue/commit/cf640af67c03e135fbb7beb5d935c4348ef7dec6) by **Flash**)

- Fixed [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md) not firing for boat collisions ([43ee092](https://github.com/multitheftauto/mtasa-blue/commit/43ee092d60f0a4db7bb17ae42f2fe815ef5701ee) by **Flash**)

- Fixed [unbindKey](mta://scripting/shared/functions/unbindkey.md) removing every script bind on the key ([791b77c](https://github.com/multitheftauto/mtasa-blue/commit/791b77cb5d3ff6ddebc485a7eb5268a4bac9b506) by **Flash**)

- Fixed removed world models reappearing after building pool resize ([d47eb88](https://github.com/multitheftauto/mtasa-blue/commit/d47eb88d1cfc0303517dc22c4756e322b8bf8c41) by **Nicolás Barrios**)

- Fixed vehicle shadows remaining visible at zero alpha ([50dc4b9](https://github.com/multitheftauto/mtasa-blue/commit/50dc4b901e62e71b3ae809164090a2008b0d9b54) by **Dryxio**)

- Fixed camera jitter while aiming and walking at high FPS ([00da956](https://github.com/multitheftauto/mtasa-blue/commit/00da95660e1b010741e2f8a1cd160928c275ef67) by **Federico Romero**)

- Fixed remote melee strafing and special-attack sync ([0c98db3](https://github.com/multitheftauto/mtasa-blue/commit/0c98db37ac63bc4c47879384a53e75eddc4db5e7) by **Dryxio**)

- Fixed vehicle door model flags not applying via [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md) ([e968252](https://github.com/multitheftauto/mtasa-blue/commit/e968252e23b89a4df430798ad5973f5aaf9f5f9a) by **Federico Romero**)

- Fixed [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md) firing twice for cancelled tyre damage ([1e0227f](https://github.com/multitheftauto/mtasa-blue/commit/1e0227f50465bd8c8f5f39a96eb061455c2abcb2) by **Youssef Maged**)

- Fixed ped shadows remaining visible at zero alpha ([7376438](https://github.com/multitheftauto/mtasa-blue/commit/7376438f4d9d415fea9c827a60a6c04e7ddc1fb9) by **Dryxio**)

- Fixed client debugscript not buffering startup logs ([416480c](https://github.com/multitheftauto/mtasa-blue/commit/416480c08caf59e5b062ed8e0fdc573b4a6f4c1c) by **Mohab**)

- Fixed Forklift forks not working on custom vehicle models ([b987fe1](https://github.com/multitheftauto/mtasa-blue/commit/b987fe1c31254ae0cae4d9a92b1cf08688723993) by **Federico Romero**)

- Fixed "No Joystick found" log spam ([d343ed0](https://github.com/multitheftauto/mtasa-blue/commit/d343ed0cae80c5509ee92a8e710fb7444c4e1909) by **Xenius97**)

- Fixed AlwaysOnTop CEGUI elements appearing above the main menu and console ([a124b3e](https://github.com/multitheftauto/mtasa-blue/commit/a124b3ea87b345a96e0b5d18b888471085963698) by **Mohab**)

- Fixed [getVehicleName](mta://scripting/shared/functions/getvehiclename.md) returning empty string for requested models ([4b766ae](https://github.com/multitheftauto/mtasa-blue/commit/4b766ae92db1e7efbcb72b74af4fcbd4c2a17a54) by **justn**)

- Fixed bikes breaking when their steering lock is set to zero ([ef0e22c](https://github.com/multitheftauto/mtasa-blue/commit/ef0e22cb031cbfd9e9e38ee2034f13826a67312f) by **Federico Romero**)

- Fixed [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) objects having no physics ([5b4142a](https://github.com/multitheftauto/mtasa-blue/commit/5b4142a159044082b7c3c3cfa7401bf7fd086d3b) by **Federico Romero**)

- Changed [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md) to report the vehicle position for explosion and fire damage ([794e384](https://github.com/multitheftauto/mtasa-blue/commit/794e384df10d542ce7acd39a3fe846d66992118d) by **Batuhan Tonga**)

- Fixed vehicle door and panel damage states resetting on custom model change ([7e8d2a9](https://github.com/multitheftauto/mtasa-blue/commit/7e8d2a9b72dcfce01191535348307e7f33cec73f) by **Mohab**)

- Fixed crouchbug firing delay when crouchbug glitch is enabled ([ac738fd](https://github.com/multitheftauto/mtasa-blue/commit/ac738fda96f1686b22d23ab92a91b50e388f5d0d) by **Mohab**)

- Fixed hydraulics not working on monster trucks ([a23f00b](https://github.com/multitheftauto/mtasa-blue/commit/a23f00b0f76cd367051b7a38ed47f04cc30933a6) by **Federico Romero**)

- Fixed settings restart prompt lost after language/skin change ([6ff14f5](https://github.com/multitheftauto/mtasa-blue/commit/6ff14f5083bd9c49ad3ef7fdf8132754c6230311) by **Batuhan Tonga**)

- Fixed joystick not being detected after reconnecting ([f3e3586](https://github.com/multitheftauto/mtasa-blue/commit/f3e3586e020a7261fb5db88b3f3f411bbbe05cd1) by **Federico Romero**)

- Fixed jetpack staying visible and audible across interiors ([93bc379](https://github.com/multitheftauto/mtasa-blue/commit/93bc37933dca2468e69d1d93d5684cbd90008fe4) by **Federico Romero**)

- Fixed [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) not working on buildings ([29f5500](https://github.com/multitheftauto/mtasa-blue/commit/29f5500faed5f72ae11832b6dc531fb99873c017) by **Federico Romero**)

- Fixed audio only working after opening settings ([ed886be](https://github.com/multitheftauto/mtasa-blue/commit/ed886beff487f57a846cd7693f7e11d494d7f7ca) by **Dryxio**)

- Fixed crash when detaching an element from a colshape hit event ([756e992](https://github.com/multitheftauto/mtasa-blue/commit/756e99222583df66d18f73b3e3f99602b6fe7a65) by **Federico Romero**)

- Fixed aim/arm getting stuck after playing a custom animation ([4581b97](https://github.com/multitheftauto/mtasa-blue/commit/4581b9750e8935083a8077b6acc901bd21103e22) by **Federico Romero**)

- Fixed water staying invisible across dimensions ([ba3a895](https://github.com/multitheftauto/mtasa-blue/commit/ba3a895e8230daf1abe9e23277b0fadf2cd7d22a) by **Federico Romero**)

- Fixed dead peds replaying their death animation on stream in ([21ca995](https://github.com/multitheftauto/mtasa-blue/commit/21ca9951b290846a6256e15df8f884fcf666d309) by **Federico Romero**)

- Fixed [engineImageLink](https://wiki.multitheftauto.com/index.php?title=EngineImageLink&action=edit&redlink=1) not applying to weapon models ([6adbd9e](https://github.com/multitheftauto/mtasa-blue/commit/6adbd9e5a16c41cca7b72c14acff6954a288bcc9) by **Federico Romero**)

- Fixed [getElementRadius](mta://scripting/client/functions/getelementradius.md) returning false for buildings ([16b6aa2](https://github.com/multitheftauto/mtasa-blue/commit/16b6aa2818483cb3dfc76c2f3b70ef5b02fe531d) by **Federico Romero**)

- Fixed [testSphereAgainstWorld](mta://scripting/client/functions/testsphereagainstworld.md) returning no hit element for buildings ([b069947](https://github.com/multitheftauto/mtasa-blue/commit/b06994738227711e05cedb2b4b3ce7e237bcb801) by **Federico Romero**)

- Fixed jump and climb ignoring [setElementCollidableWith](mta://scripting/client/functions/setelementcollidablewith.md) ([a52806a](https://github.com/multitheftauto/mtasa-blue/commit/a52806aff876f70fe5b5fbd857a3243abfac8a28) by **Federico Romero**)

- Fixed custom weapons keeping pointers to destroyed elements ([dc8250c](https://github.com/multitheftauto/mtasa-blue/commit/dc8250c9139281286c2bb90443b40802337fea18) by **Havi**)

- Fixed swinging chassis handling flag not applying ([357062d](https://github.com/multitheftauto/mtasa-blue/commit/357062d2b3e685d592e6ec1976c3fa765eb5e448) by **Federico Romero**)

- Fixed targeting marker staying on screen after death ([8d3eccb](https://github.com/multitheftauto/mtasa-blue/commit/8d3eccb52afc3e6d31c427fbb708714373a5c253) by **Federico Romero**)

- Fixed [getPedAnimation](mta://scripting/client/functions/getpedanimation.md) for short-lived partial animations ([4f02566](https://github.com/multitheftauto/mtasa-blue/commit/4f0256651753f8943dcffdedb107d53edd5dbf88) by **Batuhan Tonga**)

- Fixed DirectInput data queries while GUI has focus ([d564415](https://github.com/multitheftauto/mtasa-blue/commit/d564415ae58c3660bb0d3cd509c9be97dfc60101) by **Havi**)

- Fixed vehicle headlights not lighting other vehicles ([210e362](https://github.com/multitheftauto/mtasa-blue/commit/210e3624e8e2c090a6904be28e8886402fad4b8a) by **Dryxio**)

- Fixed crashes and TXD slot leaks in model cleanup ([6900903](https://github.com/multitheftauto/mtasa-blue/commit/6900903696a5da63b79f27b409c5db2c5a3fac83) by **Havi**)

- Fixed [getElementBoneMatrix](mta://scripting/client/functions/getelementbonematrix.md) to return Matrix when OOP is enabled ([0c1bd38](https://github.com/multitheftauto/mtasa-blue/commit/0c1bd38f635a859c4b63e4bd78832c01bbe3ab7b) by **Batuhan Tonga**)

- Fixed crashes when assigning invalid model texture-dictionary IDs ([8e968ef](https://github.com/multitheftauto/mtasa-blue/commit/8e968efa863196dfc06933c8e757997e7d073ff4) by **Havi**)

- Fixed size overflows when handling plain texture pixels ([361671c](https://github.com/multitheftauto/mtasa-blue/commit/361671c79b49cd68ea34e9f5ef3e6af32f49155d) by **Havi**)

- Fixed client crash from invalid sound FFT band counts ([7a853b6](https://github.com/multitheftauto/mtasa-blue/commit/7a853b6608d104f11ca3038ca10e53cafc8feae9) by **Havi**)

- Fixed chat scale loading and precision ([3705d36](https://github.com/multitheftauto/mtasa-blue/commit/3705d36e5a3c54aa0b9600c1301360849d12bc05) by **Havi**)

- Fixed chat preset colors without an alpha value ([3a6361f](https://github.com/multitheftauto/mtasa-blue/commit/3a6361fe91025e1124313a379fa101263dd2877d) by **Havi**)

- Fixed disabled server browser tabs being restored as enabled ([92d31aa](https://github.com/multitheftauto/mtasa-blue/commit/92d31aabe20baec2379b20595fe208b4b3da37d8) by **Havi**)

- Fixed client crash on invalid [setTrainTrack](mta://scripting/shared/functions/settraintrack.md) track number ([0775ac7](https://github.com/multitheftauto/mtasa-blue/commit/0775ac7891244b59b1676a554da76fb6866a4110) by **Havi**)

- Fixed [getPedTask](mta://scripting/client/functions/getpedtask.md) crash with invalid primary task index ([78695db](https://github.com/multitheftauto/mtasa-blue/commit/78695dbdcf6b55dbef6bac6e9379213b1224d392) by **Havi**)

- Fixed animation query crash for streamed-out peds ([dad7bb3](https://github.com/multitheftauto/mtasa-blue/commit/dad7bb37f512fb0067723c8bcd1dcee6996281fd) by **Havi**)

- Fixed client crash when firing at streamed-out vehicle wheels ([e4a4fdb](https://github.com/multitheftauto/mtasa-blue/commit/e4a4fdba52be0cfc7497934879eb398686f02d69) by **Havi**)

- Fixed camera colliding against scripted objects while spectating ([08db4c8](https://github.com/multitheftauto/mtasa-blue/commit/08db4c834034b201e34f7f91fd01b971a5da4f77) by **lopsi**)

- Fixed attached entities staying too bright ([37c73df](https://github.com/multitheftauto/mtasa-blue/commit/37c73df1bfeb9dc988c0b051ee5356b874536b5e) by **Federico Romero**)

- Fixed aim pose desync when a weapon is given while the aim/fire button is held ([436a88a](https://github.com/multitheftauto/mtasa-blue/commit/436a88a796d9b84849f5ef73fd693a61c87cfe2c) by **Federico Romero**)

- Fixed [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md) desync right after [createVehicle](mta://scripting/shared/functions/createvehicle.md) ([49ccae6](https://github.com/multitheftauto/mtasa-blue/commit/49ccae674cbab09892c88163f879934482916b31) by **Federico Romero**)

- Fixed [getVehicleDummyPosition](mta://scripting/client/functions/getvehicledummyposition.md) returning 0,0,0 for the second exhaust ([de32969](https://github.com/multitheftauto/mtasa-blue/commit/de329692c870bb35b790f450ba6db2fcb4f924d5) by **Federico Romero**)

- Fixed incorrect LOD rotations after removing world models ([40c9561](https://github.com/multitheftauto/mtasa-blue/commit/40c9561c0c3e4e83d0bcff75ab2a08c1fa1f1126) by **FileEX**)

- Fixed crash from disabling driveby during weapon fire ([bf58b4e](https://github.com/multitheftauto/mtasa-blue/commit/bf58b4e9aca7434de1e98389448617eb1669a3f6) by **Federico Romero**)

- Fixed a crash when [engineFreeModel](mta://scripting/client/functions/enginefreemodel.md) overlaps deferred [destroyElement](mta://scripting/shared/functions/destroyelement.md) cleanup ([3ab54e4](https://github.com/multitheftauto/mtasa-blue/commit/3ab54e406e5b264a67016401d6cddee22cf30ce8) by **Federico Romero**)

- Fixed crash when freeing a vehicle model while its detached parts exist ([065b49d](https://github.com/multitheftauto/mtasa-blue/commit/065b49d3494ae4d2c5ff6d95af4462132b45b2ae) by **Federico Romero**)

- Fixed the Rhino middle wheels rendering incorrectly ([d94039f](https://github.com/multitheftauto/mtasa-blue/commit/d94039ffe9ab16e05daea105023e907c2e79f4f2) by **Javid Majidzade**)

- Fixed CJ clothes leaking between players ([e2e715a](https://github.com/multitheftauto/mtasa-blue/commit/e2e715a83e203c4f962a5b68a89e3ed7367814ef) by **Federico Romero**)

- Fixed a crash when creating object models from weapon models ([8dd5c76](https://github.com/multitheftauto/mtasa-blue/commit/8dd5c762db1d10bc3a43f3dd243f85e4921c0df1) by **Federico Romero**)

- Fixed wrong depth sorting and face culling behavior in mirrors ([22364b4](https://github.com/multitheftauto/mtasa-blue/commit/22364b484647b4d82fd30a4b669e931a03399bd2) by **rx**)

- Made the crash dialog resizable and constrained it to the desktop ([7ced959](https://github.com/multitheftauto/mtasa-blue/commit/7ced959169b397dbf31db2dbbd1dfffef784a3ba) by **Marek Kulik**)

- Reduced TXD load memory before import ([e1c7e92](https://github.com/multitheftauto/mtasa-blue/commit/e1c7e922c58533b7cb8ee5bd3669fe0e0e581c23) by **Mohamed Maatallah**)

- Fixed SVG texture color banding ([bb7e811](https://github.com/multitheftauto/mtasa-blue/commit/bb7e81142265851d8f687173e71434eb7bd224b5) by **Mohamed Maatallah**)

- Fixed vehicle audio reinitialization churn ([b42742d](https://github.com/multitheftauto/mtasa-blue/commit/b42742df759e186edc7c1503d7e486bdfa25d65b) by **Mohamed Maatallah**)

- Avoided duplicate resource checksum refresh on start ([2239a7b](https://github.com/multitheftauto/mtasa-blue/commit/2239a7b1dfbc3e9b23a25f7292148440d1e8d97c) by **Mohamed Maatallah**)

- Fixed [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md)/[dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md) failing on browser elements ([eacbb18](https://github.com/multitheftauto/mtasa-blue/commit/eacbb18b065382d27e0ec5dbe3251742375929c5) by **lopsi**)

- Fixed client-side [createExplosion](mta://scripting/shared/functions/createexplosion.md) ignoring makeSound and camShake parameters ([95e0752](https://github.com/multitheftauto/mtasa-blue/commit/95e0752322f4beed58f741a0c3e0f25c5ef57ba1) by **lopsi**)

- Fixed GUI font changes throwing an exception for unknown font names ([874d192](https://github.com/multitheftauto/mtasa-blue/commit/874d1924b5b17169d7e46ad4da8be0878cc3f7dc) by **lopsi**)

- Fixed use-after-free crashes involving collision data shared by paired timed models ([0f7294b](https://github.com/multitheftauto/mtasa-blue/commit/0f7294b0a33e3685e178d171c30962a02ffda13f) by **Mohamed Maatallah**)

- Preserved shared LOD links for world models ([9c3737d](https://github.com/multitheftauto/mtasa-blue/commit/9c3737de2e52edfa6f5e4c60cabe0a8a906bca8d) by **Mohamed Maatallah**)

- Preserved plane rotor speed when a vehicle is recreated ([a4f1820](https://github.com/multitheftauto/mtasa-blue/commit/a4f1820cb05ca92957b6d22deecec9e6645da579) by **Mohamed Maatallah**)

- Fixed raw OGG playback in [playSound3D](mta://scripting/client/functions/playsound3d.md) and audible seams when looping ([b05a5e1](https://github.com/multitheftauto/mtasa-blue/commit/b05a5e1078780d5f9f334a850291007fd6317ec4) by **Mohamed Maatallah**)

- Fixed radar_map HUD component freezing blips ([e1cff67](https://github.com/multitheftauto/mtasa-blue/commit/e1cff673dab5ae0f07308ca049685869ae051e15) by **Saifaldin Eabyad**)

- Fixed [isElementStreamedIn](mta://scripting/client/functions/iselementstreamedin.md) returning false for localPlayer ([c28b4eb](https://github.com/multitheftauto/mtasa-blue/commit/c28b4eb1702fab4ff33514797eec585c6fa8679c) by **Nao**)

- Avoided fixed camera mode on no-op [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md) calls ([776f9b2](https://github.com/multitheftauto/mtasa-blue/commit/776f9b2c28bfee0975d948d13f3b52d38e683388) by **lopsi**)

- Fixed component visibility regression for single-version atomics ([f99a7fa](https://github.com/multitheftauto/mtasa-blue/commit/f99a7fab52cc2c836b8b19b157a2d7f58e3d513b) by **lopsi**)

- Fixed client spoiler upgrade placement on unsupported vehicle models ([491bddb](https://github.com/multitheftauto/mtasa-blue/commit/491bddb91861a7e4180e27804ea33d5857a94e9b) by **lopsi**)

- Fixed incorrect vehicle physics for extended handling entries (Faggio, Hotring Racers, etc.) ([4259958](https://github.com/multitheftauto/mtasa-blue/commit/4259958f6b6a017b4f59e239740a13faa8baccc1) by **lopsi**)

- Fixed Discord Rich Presence being enabled despite opting out ([0db2398](https://github.com/multitheftauto/mtasa-blue/commit/0db2398908a9efc9220c0330ef5b9f33506f7285) by **lopsi**)

- Fixed ring markers rendering underground ([fefd706](https://github.com/multitheftauto/mtasa-blue/commit/fefd706053227b0867d3b76de8ab4ebf9bc89748) by **lopsi**)

- Made [guiSetInputEnabled](mta://scripting/client/functions/guisetinputenabled.md) show the cursor when GUI input is enabled ([5bd6ba9](https://github.com/multitheftauto/mtasa-blue/commit/5bd6ba983c22925f0a628cb5c363a5a0d405ac88) by **João Luis**)

- Fixed [isElementOnScreen](mta://scripting/client/functions/iselementonscreen.md) for markers ([f4b0897](https://github.com/multitheftauto/mtasa-blue/commit/f4b08978598c3679fb5bd945bfa57723c12d4b82) by **FileEX**)

- Fixed sniper bullet sync on maximum bandwidth reduction ([49cbd31](https://github.com/multitheftauto/mtasa-blue/commit/49cbd31dc3baf0fd8b5391322260439610fde2cd) by **Arran**)

- Fixed [getElementRotation](mta://scripting/shared/functions/getelementrotation.md) and [getElementModel](mta://scripting/shared/functions/getelementmodel.md) returning false for buildings ([8d43487](https://github.com/multitheftauto/mtasa-blue/commit/8d43487ead2da34408d6edcf333fb1749e98bcfa) by **Youssef Maged**)

- Fixed movement and attacks becoming blocked when the fastfire glitch is enabled ([ba8ff97](https://github.com/multitheftauto/mtasa-blue/commit/ba8ff9720df5a6eb0ddcf4ca76a7f1b83086cd43) by **Youssef Maged**)

- Fixed browser rendering not resuming after [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md) ([3f359b4](https://github.com/multitheftauto/mtasa-blue/commit/3f359b493c49ad0be940ea3e18b2ba18b3b4887f) by **x6c85**)

- Improved streaming performance by retaining cached models that are still in use ([49f106d](https://github.com/multitheftauto/mtasa-blue/commit/49f106dff4dd107ae58831611b5cbebc3c2208eb) by **Dutchman101**)

- Fixed startup window ordering and kept the launcher window on top ([0d455c8](https://github.com/multitheftauto/mtasa-blue/commit/0d455c80f9e82efd749049ad5a26af5ab81f5024), [51713c8](https://github.com/multitheftauto/mtasa-blue/commit/51713c8314c38e87a87dc6a25270de27e1072775) by **lopsi**, **Youssef Maged**)

- Fixed custom vehicle model support for tow hooks, aircraft, spoilers, Dumper ramps, Cement Truck drums, Dozer blades, ZR-350 headlights and trailer attachment ([002ba47](https://github.com/multitheftauto/mtasa-blue/commit/002ba4791bc7c61be3e91cd5c078473c80bda4ac), [a5728fa](https://github.com/multitheftauto/mtasa-blue/commit/a5728fab93dc3891ef98930b84185bdc8a7ae794), [b953f96](https://github.com/multitheftauto/mtasa-blue/commit/b953f9668320ad0cb64f75201c82e9b213310ac2), [593cfc0](https://github.com/multitheftauto/mtasa-blue/commit/593cfc0608e475cafbbc2a892848a62bd54baf50), [98b8df6](https://github.com/multitheftauto/mtasa-blue/commit/98b8df60b2a7b1397f01becfcae321b82fd0c044), [3f0dcde](https://github.com/multitheftauto/mtasa-blue/commit/3f0dcde782e95c45faa7fa5747bd3588e6d3e002), [fb64c2e](https://github.com/multitheftauto/mtasa-blue/commit/fb64c2e3e4741d97ba231b7bd388de8dea7502a1), [ba13ae6](https://github.com/multitheftauto/mtasa-blue/commit/ba13ae6e40ce5138ce53910d5231d9fb7704ee68) by **Federico Romero**, **FJS**)

- Preserved exact radio and SFX volume settings across restarts and restored their migration when upgrading ([da8c3aa](https://github.com/multitheftauto/mtasa-blue/commit/da8c3aa7f87db58150f56ad64375f2297336afbc), [b8c7b90](https://github.com/multitheftauto/mtasa-blue/commit/b8c7b9067dbde470db2c001d8b71d60a6eb961b3) by **Mohab**, **lopsi**)

- Reduced FPS limiter CPU usage and improved frame pacing ([ed3ede4](https://github.com/multitheftauto/mtasa-blue/commit/ed3ede4912e5ff75da15276f68b82be41abcc861) by **Federico Romero**)

- Improved resource startup/shutdown handling and checksum processing ([484f0f5](https://github.com/multitheftauto/mtasa-blue/commit/484f0f5a8f7c58df95540c501e3869995f3fd8ba) by **Dutchman101**)

- Fixed partial custom animations leaving peds rigid, including animations from custom IFP banks ([500d818](https://github.com/multitheftauto/mtasa-blue/commit/500d81895d171677fb14300606d44d69989a472c), [b785d45](https://github.com/multitheftauto/mtasa-blue/commit/b785d454d851fae2f3aa47898fbfd9c5553540cd) by **Federico Romero**)

- Fixed crashes from out-of-range vehicle siren data and strengthened bounds checks throughout siren handling ([cbda874](https://github.com/multitheftauto/mtasa-blue/commit/cbda8742091df159e78c5d432392940f2dc9d8f0), [4f3216c](https://github.com/multitheftauto/mtasa-blue/commit/4f3216c8568cfdc8f9af5ec50adbd768c183d5b2) by **Havi**, **Dutchman101**)

- Fixed the V-Sync checkbox not reflecting the saved setting ([c983fbb](https://github.com/multitheftauto/mtasa-blue/commit/c983fbbbb8a2c828dfbea7df3c02bba8969f9922) by **SpeedyFolf**)

- Fixed objects repeatedly streaming in and out and reduced object stream-in delay ([9d27fbb](https://github.com/multitheftauto/mtasa-blue/commit/9d27fbb306dee550aca7af2603d6bd6762392122), [9f74460](https://github.com/multitheftauto/mtasa-blue/commit/9f744604ea3e8a0bdc512add6263dfd0fc32e303) by **Arran**, **Sam**)

- Added the current and required client versions to server update dialogs ([bbe157d](https://github.com/multitheftauto/mtasa-blue/commit/bbe157d50681083d77a0f67e13b265dc1c4255bd) by **Batuhan Tonga**)

- Fixed crashes caused by invalid COL header sizes ([9d10449](https://github.com/multitheftauto/mtasa-blue/commit/9d1044972333f3da40e28f36f6c89735cd27d280) by **Havi**)

- Fixed a crash while allocating animation-blend data ([e54e6e5](https://github.com/multitheftauto/mtasa-blue/commit/e54e6e59c78db3b699fc53da517e126eb35ed0cd) by **Dutchman101**)

- Fixed the unoccupied-vehicle synchronization list growing without bound when exiting vehicles ([6bbb61b](https://github.com/multitheftauto/mtasa-blue/commit/6bbb61bfc82dc7bb1d79052bb7bdc24c1bf7d821) by **lopsi**)

- Fixed [isPedDead](mta://scripting/shared/functions/ispeddead.md) staying true after a ped is revived with [setElementHealth](mta://scripting/shared/functions/setelementhealth.md) ([ab2313d](https://github.com/multitheftauto/mtasa-blue/commit/ab2313ddc3fef299e34217465f8a2f3ef1806c6a) by **lopsi**)

- Extended per-entity reference scaling to vehicles ([3e1bcba](https://github.com/multitheftauto/mtasa-blue/commit/3e1bcbadf3e13d95230c6815e050e10a61ea312b) by **Mohamed Maatallah**)

- Fixed building lights, coronas and vehicle shadows flickering during weather transitions ([501725f](https://github.com/multitheftauto/mtasa-blue/commit/501725fa149d7e2adec0b91d65d2ebf8cc831add), [57b07f4](https://github.com/multitheftauto/mtasa-blue/commit/57b07f4d8ea9428cc960b4da56babe87ade2d660), [13fddf7](https://github.com/multitheftauto/mtasa-blue/commit/13fddf754d3b9955ac4b43e6c6b8e3bbff571230), [c12ffaf](https://github.com/multitheftauto/mtasa-blue/commit/c12ffaf27bc150cb46c7dbd0bb2f3ff6a5bf84e0), [5798687](https://github.com/multitheftauto/mtasa-blue/commit/5798687102995eb0013389880d1d621cd9d0a288), [160d6b1](https://github.com/multitheftauto/mtasa-blue/commit/160d6b1300b57df4cb85dde86efa8fa96f8dedbb) by **Mohamed Maatallah**, **Federico Romero**)

- Fixed a neon-texture rendering regression ([1e4d53e](https://github.com/multitheftauto/mtasa-blue/commit/1e4d53eb71e88de1455d2a4dd3c16d2ad19ee5ed) by **Federico Romero**)

- Fixed a collision gap while models are being restreamed ([ddc3969](https://github.com/multitheftauto/mtasa-blue/commit/ddc3969951bfe3b145bd4f5acb7b12cc0f11e6d3) by **Nao**)

- Prevented excess detached vehicle parts and repeated aircraft wreck components, including when engine autostart is disabled ([f43b1c6](https://github.com/multitheftauto/mtasa-blue/commit/f43b1c6b75d531aa1cbc9550cf3a5363a317cd27), [4ec3e90](https://github.com/multitheftauto/mtasa-blue/commit/4ec3e90851023d9151ab8d36e8d75646c7a21450) by **lopsi**, **Federico Romero**)

- Fixed [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md) not firing after player death ([0ab45c9](https://github.com/multitheftauto/mtasa-blue/commit/0ab45c99ded2793989ba227acb440c73db1b1eb7) by **lopsi**)

- Fixed [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md) rendering failures and its ordering relative to world rendering and sun/moon flares ([3cc19e1](https://github.com/multitheftauto/mtasa-blue/commit/3cc19e131fbb6b0b3ef569d12814249d1bd71f39), [9e1f4b4](https://github.com/multitheftauto/mtasa-blue/commit/9e1f4b491f5eab702fc95f95821c84f57495c644), [fa8110e](https://github.com/multitheftauto/mtasa-blue/commit/fa8110e741b39cffb1cdc24fd170d833103214be) by **Dutchman101**, **Nao**, **lopsi**)

- Fixed [getVehicleSirensOn](mta://scripting/shared/functions/getvehiclesirenson.md) and [setVehicleSirensOn](mta://scripting/shared/functions/setvehiclesirenson.md) for the Rhino and Barracks ([83ca44a](https://github.com/multitheftauto/mtasa-blue/commit/83ca44a43063504f97a0db84b96a53a5bd7dc9ff) by **Mohamed Maatallah**)

- Fixed [showCursor](mta://scripting/shared/functions/showcursor.md) control toggling when the cursor is globally unlocked ([3ef0190](https://github.com/multitheftauto/mtasa-blue/commit/3ef0190ad39d4a51a98ea909e7e8c90c4cce61ce) by **Mohamed Maatallah**)

- Fixed installation-root detection failures causing updater U01 errors ([de4c559](https://github.com/multitheftauto/mtasa-blue/commit/de4c559b5bf1911e9c208d4b270a0426af948f06) by **Dutchman101**)

- Fixed instant-respawn flows leaving players dead or stuck and misleading "NETWORK TROUBLE" messages during death ([560b53d](https://github.com/multitheftauto/mtasa-blue/commit/560b53dddc06968f77cd0f24e631ea85c55de935), [9b5585a](https://github.com/multitheftauto/mtasa-blue/commit/9b5585a6b3a2a1a340f9e2d2874ea791b52e53d6), [85a46bd](https://github.com/multitheftauto/mtasa-blue/commit/85a46bd2cc19559f21addb5580b149d1282f0b96) by **lopsi**)

- Fixed the camera clipping through default world objects at speed ([dd0b5fb](https://github.com/multitheftauto/mtasa-blue/commit/dd0b5fb3a9948e9999b9804855b93dead2e77aef) by **lopsi**)

- Fixed sound-effect functions reporting success when applying the effect fails, including on Windows 11 24H2 ([6946e99](https://github.com/multitheftauto/mtasa-blue/commit/6946e998a8cbb9fc483007e85757c4b41acdac36) by **Mohamed Maatallah**)

- Stopped repeated FPS limiter messages spamming the console ([7817086](https://github.com/multitheftauto/mtasa-blue/commit/7817086365f0e7bea36e842810c382fd7b62a7ce) by **Arran**)

- Improved browser rendering performance and memory usage; fixed missing [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md) events and intermittent blank rendering ([ddb9249](https://github.com/multitheftauto/mtasa-blue/commit/ddb92490288993d924bbff33d1e449e4c56d7bb4), [c953cbb](https://github.com/multitheftauto/mtasa-blue/commit/c953cbbac0509496a2984b96b3bf3851fc033d8e), [3964410](https://github.com/multitheftauto/mtasa-blue/commit/396441087eca05d5247d3a7cdd9538f1823e2fad) by **lopsi**)

- Fixed vehicle-camera floating-point stack corruption and removed the temporary camera recovery workarounds ([20ee184](https://github.com/multitheftauto/mtasa-blue/commit/20ee184e6463bc3d519d577dd21bf04c1e9eef70), [3143cc4](https://github.com/multitheftauto/mtasa-blue/commit/3143cc494d718021180b4c4b6c1e1a86068a0f34) by **Mohamed Maatallah**, **lopsi**)

- Added more nouns to the nickname generator ([299cb2c](https://github.com/multitheftauto/mtasa-blue/commit/299cb2cacec394ddb7e745fb7e43581eb1aa2971) by **SpeedyFolf**)

- Fixed jetpack weapon switching and weapon-model visibility ([df6119e](https://github.com/multitheftauto/mtasa-blue/commit/df6119e1429a4f372a30d48c4628fc3abace9fb4) by **FileEX**)

- Fixed a crash while rebuilding clothing ([251c2ca](https://github.com/multitheftauto/mtasa-blue/commit/251c2ca7a57525c50c8e1ca858faeb1b9394a670) by **Dutchman101**)

- Fixed resource download handling on join and batched checksum mismatches ([374ec90](https://github.com/multitheftauto/mtasa-blue/commit/374ec905639a6de6352be497cc0119c942763a4f), [7e3c9ea](https://github.com/multitheftauto/mtasa-blue/commit/7e3c9ea51fb704704cf4cbaccb3f0daf3280769a) by **Dutchman101**)

- Fixed server-list population failures ([44b81d6](https://github.com/multitheftauto/mtasa-blue/commit/44b81d67f3f75c37e6f9dcb19a08fd3f56361484), [0c05baa](https://github.com/multitheftauto/mtasa-blue/commit/0c05baa4a65d1128f880996ffd52362e72fe4547) by **Dutchman101**)

- Added a timeout to repeated failed streaming-file reads and fixed plane weapon dummy fallback positions ([3e6a82b](https://github.com/multitheftauto/mtasa-blue/commit/3e6a82baeb11851f6da6fa68559127bf2d0dcbb8) by **lopsi**, **Dutchman101**)

- Fixed a timed-object collision crash ([c182403](https://github.com/multitheftauto/mtasa-blue/commit/c1824033c2e56db105730ed1cb0a06d7f720c042) by **FileEX**)

- Improved crash reporting and restricted Windows Error Reporting dialogs to fail-fast exceptions ([fcce26d](https://github.com/multitheftauto/mtasa-blue/commit/fcce26d5133615e4d3cb5e43838efdfb1e2db414), [9e1a38c](https://github.com/multitheftauto/mtasa-blue/commit/9e1a38c4e4a504fa9a1d1e0df7c33fcb5237a18a), [641b060](https://github.com/multitheftauto/mtasa-blue/commit/641b060f2f78381278233d1e3554d59e8a80c3c3) by **lopsi**, **Mohamed Maatallah**, **Dutchman101**)

- Reverted the experimental texture-streaming overhaul, including the expanded TXD pool, and applied stability fixes ([2dbea92](https://github.com/multitheftauto/mtasa-blue/commit/2dbea9204c4fa29f90d2606eebd77440a255d6b8) by **lopsi**, **rx**, **FileEX**, **Dutchman101**, **Xenius97**, **Marek Kulik**)

- Fixed [isVehicleOnGround](mta://scripting/shared/functions/isvehicleonground.md) detection for rotated vehicles and wheel contact ([c41067f](https://github.com/multitheftauto/mtasa-blue/commit/c41067fd990716bca4022059e7078c9c2ca2cf92) by **FileEX**)

- Fixed focus-state reporting in [isMTAWindowFocused](mta://scripting/client/functions/ismtawindowfocused.md) and [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md) after joining or starting minimized ([4e497de](https://github.com/multitheftauto/mtasa-blue/commit/4e497dec042acde29ae1b2ad22f311f665255fe0) by **FileEX**)

- Fixed searchlights not working for some players ([4ba48a3](https://github.com/multitheftauto/mtasa-blue/commit/4ba48a37ad5ddd77cd26be745cac666fb91e7727) by **FileEX**)

- Fixed [setSearchLightColor](mta://scripting/client/functions/setsearchlightcolor.md) affecting the Police Maverick's searchlight color ([725f47d](https://github.com/multitheftauto/mtasa-blue/commit/725f47d0afcb39aef085ddbb593cfed296d6edb4) by **FileEX**)

- Fixed objects becoming invisible when their alpha was below 141 ([6bd6db5](https://github.com/multitheftauto/mtasa-blue/commit/6bd6db55aabbf35dfb69dec574e1a75193785312) by **FileEX**)

- Fixed vehicle component lists not refreshing after replacing the vehicle model ([f3e7c52](https://github.com/multitheftauto/mtasa-blue/commit/f3e7c524d7b9e11d1d61e976b06ff5fa8706e59d) by **FileEX**)

- Fixed [engineLoadDFF](mta://scripting/client/functions/engineloaddff.md) rejecting valid DFF files ([e01616e](https://github.com/multitheftauto/mtasa-blue/commit/e01616eb706f404934618d811d4344669558a859) by **PrimelPrime**)

- Fixed restoring and synchronizing vehicle suspension handling properties ([7a663ae](https://github.com/multitheftauto/mtasa-blue/commit/7a663ae90b86277832c8a4647bcf04fa3799e31c) by **Dutchman101**)

- Fixed freezes and improved asset-loading performance when joining heavily modded servers ([7e69069](https://github.com/multitheftauto/mtasa-blue/commit/7e690694b0460167b1d0fb913b6ad08470fba427), [dd38398](https://github.com/multitheftauto/mtasa-blue/commit/dd3839895c12f6c5c5f5427f6cd18c7ef68a3710), [655767b](https://github.com/multitheftauto/mtasa-blue/commit/655767b2453a06e1c85e1c5e4e9e10762c155a08) by **Dutchman101**)

- Improved installation-path detection, launching and updating to address additional causes of U01 and CL16 errors ([c15736e](https://github.com/multitheftauto/mtasa-blue/commit/c15736eae5e58570b58378e8e34413359790bfbf), [4200137](https://github.com/multitheftauto/mtasa-blue/commit/4200137453cfddbee05726ce83b022bc56af6218), [f9dd679](https://github.com/multitheftauto/mtasa-blue/commit/f9dd679a409fa3facdb213841bebb5deaabc7d79) by **Dutchman101**)

- Prevented buffer overflows caused by invalid sizes in modified audio-bank files ([4307347](https://github.com/multitheftauto/mtasa-blue/commit/430734748b789fd6bff42bb3b49ea2be82844ce9) by **Dutchman101**)

- Fixed a crash when [setElementPosition](mta://scripting/shared/functions/setelementposition.md) is called on a ped from a damage handler ([3f4f11a](https://github.com/multitheftauto/mtasa-blue/commit/3f4f11aa9c3edd5db4c09bc6898a9387cf02574b) by **Dutchman101**)

- Fixed an additional crash when video memory is exhausted ([573b331](https://github.com/multitheftauto/mtasa-blue/commit/573b3310cd3045f91e7783b90500f4942344b28f) by **Dutchman101**)

- Extended integrity-violation exit messages to cover core and client modules ([0ba9b28](https://github.com/multitheftauto/mtasa-blue/commit/0ba9b2891b3b6f11a0dfb1477a9c629704cbd7a5) by **Dutchman101**)

- Fixed [engineRequestTXD](mta://scripting/client/functions/enginerequesttxd.md) failure handling and [engineFreeTXD](mta://scripting/client/functions/enginefreetxd.md) not releasing its allocated TXD slot ([6cf8cc6](https://github.com/multitheftauto/mtasa-blue/commit/6cf8cc6c18b035eea37054057931be89e00c88e0) by **Dutchman101**)

- Improved cleanup of audio streaming threads when shutting down the client ([6cf8cc6](https://github.com/multitheftauto/mtasa-blue/commit/6cf8cc6c18b035eea37054057931be89e00c88e0) by **Dutchman101**)

- Improved streaming memory reclamation before loading large textures ([6cf8cc6](https://github.com/multitheftauto/mtasa-blue/commit/6cf8cc6c18b035eea37054057931be89e00c88e0) by **Dutchman101**)

- Fixed crashes in key-bind argument handling and loading saved key binds ([4c47402](https://github.com/multitheftauto/mtasa-blue/commit/4c474025fc83ab757a84092a45de1bda42a96128) by **Dutchman101**)

- Fixed memory-safety and stack-buffer-overrun issues in GTA crash fixes and clothing handling ([0530c83](https://github.com/multitheftauto/mtasa-blue/commit/0530c83c7a762abb4e60f3c5fe895f4b32378c00), [e0bbc88](https://github.com/multitheftauto/mtasa-blue/commit/e0bbc889c322eca45cbacb93bd0752047c6d428c) by **Dutchman101**)

- Fixed GUI freezes and slow redraws when working with grid lists ([f9c4693](https://github.com/multitheftauto/mtasa-blue/commit/f9c46930439cb4580dfeebc849f0b1c91b12e170) by **Dutchman101**)

- Fixed crashes in pickup effects and object LOD handling ([66eba7a](https://github.com/multitheftauto/mtasa-blue/commit/66eba7a3936a54fae97b46e6152c92fb7b618d69), [4eb4a7c](https://github.com/multitheftauto/mtasa-blue/commit/4eb4a7ccbb84c902b6d67e0c7333e8bf85c0c4ee), [b46f5fe](https://github.com/multitheftauto/mtasa-blue/commit/b46f5feb901d2070f06d78af2138c8cfe26a64f1) by **Dutchman101**)

- Fixed several freezes caused by recursive file access and file-loading or checksum operations ([b9fd12c](https://github.com/multitheftauto/mtasa-blue/commit/b9fd12c5895dcf2ad6275a7637df4a3c25ff0739), [7bc2315](https://github.com/multitheftauto/mtasa-blue/commit/7bc2315081840572be19adcc5936abf99870f94a), [a87d5d9](https://github.com/multitheftauto/mtasa-blue/commit/a87d5d9e379c8f373dadd20ac2b56ecbbcb213a8), [eeec3d8](https://github.com/multitheftauto/mtasa-blue/commit/eeec3d8de387609429b4a7d2fbb79886307ba047) by **Dutchman101**)

- Fixed heap-corruption crashes when Direct3D texture and buffer resources outlive the graphics device ([7c91b20](https://github.com/multitheftauto/mtasa-blue/commit/7c91b20986ddce31e8d626c99ce0ecef9d9c486c) by **Dutchman101**)

- Improved file loading and checksum handling, including recovery from stalled reads ([a8957f9](https://github.com/multitheftauto/mtasa-blue/commit/a8957f9c31aa09a35312f03b2967c96e90131a0e), [4c53a76](https://github.com/multitheftauto/mtasa-blue/commit/4c53a765f6d9ad3f92ade134fb14895752b941b5) by **Dutchman101**)

- Added SVG content filtering for unsupported elements, event attributes and external references ([43d1064](https://github.com/multitheftauto/mtasa-blue/commit/43d10644a3306e017e8e3797de1e71107a3023ad) by **Dutchman101**)

- Fixed GTA:SA in-game presence detection in Steam ([7911713](https://github.com/multitheftauto/mtasa-blue/commit/79117137ae266045f903607d29f854d293cfe8a2) by **Marek Kulik**)

- Made local server components optional: hide Host Game and Map Editor when the server folder is absent, and skip server files during updates ([f007727](https://github.com/multitheftauto/mtasa-blue/commit/f00772702e8032fb59392720532df28a9d8d8f65) by **Xenius97**)

- Stopped showing the antivirus warning when running under Wine ([fc574ff](https://github.com/multitheftauto/mtasa-blue/commit/fc574ffc4a585aea60a17125b148489892663a31) by **Xenius97**)

- Fixed IFP loading freezes and crashes, and [engineReplaceAnimation](mta://scripting/client/functions/enginereplaceanimation.md) failing on animation groups that are not yet loaded ([7296eab](https://github.com/multitheftauto/mtasa-blue/commit/7296eab8e781056fa620c97c28415a67c238976a), [c063c48](https://github.com/multitheftauto/mtasa-blue/commit/c063c481b1769143c4a85df79791a8b7d673827d), [108c478](https://github.com/multitheftauto/mtasa-blue/commit/108c4786da4b663bf3d524f0690e7a2b85ced646) by **Dutchman101**)

- Fixed [processLineAgainstMesh](mta://scripting/client/functions/processlineagainstmesh.md) crashing on coloured meshes without texture coordinates ([16cab21](https://github.com/multitheftauto/mtasa-blue/commit/16cab21fb689d2e4a6da0f9f571778c70a524f26) by **Xenius97**)

- Fixed a race condition that could freeze the game when changing the streaming buffer size ([5f2e79a](https://github.com/multitheftauto/mtasa-blue/commit/5f2e79a10b0897db21d916de723490cc57b6004f) by **Dutchman101**)

- Fixed the server browser's Internet tab not populating automatically ([957fcd3](https://github.com/multitheftauto/mtasa-blue/commit/957fcd3e201fb1a358c6a2a918c05847cb2e59b7) by **Dutchman101**)

- Fixed the showmemstat command crashing in the main menu ([48c243c](https://github.com/multitheftauto/mtasa-blue/commit/48c243c0b457135dacfff10cbaea4e278033e55f) by **Xenius97**)

- Fixed stale entity-pool references causing crashes when GTA streams entities out ([777bd2e](https://github.com/multitheftauto/mtasa-blue/commit/777bd2ea92798436c5ad69fb2c443208f93e8262), [e9ab581](https://github.com/multitheftauto/mtasa-blue/commit/e9ab581095162e8a3ddd2e781d008d0ac373ed27) by **Dutchman101**)

- Fixed crashes when loading COL files with inconsistent or missing shadow-mesh data ([0f651ca](https://github.com/multitheftauto/mtasa-blue/commit/0f651ca2a0d1cb9c29481a8d090ee049f0da7708) by **Dutchman101**)

- Fixed crashes when getting bone positions from ped models without an animation hierarchy ([446ec92](https://github.com/multitheftauto/mtasa-blue/commit/446ec92b59b1a3cddf0199a45286144937ab65a5) by **Dutchman101**)

- Improved Direct3D device-loss recovery and fixed rendering-state corruption and crashes, including cases involving recording overlays or invalid effects ([44ae6e7](https://github.com/multitheftauto/mtasa-blue/commit/44ae6e7bbe67463f2c414ebad78a3074c261502d), [1b21194](https://github.com/multitheftauto/mtasa-blue/commit/1b21194be4075f93264d4f42cb5052137f36d361), [eadbc9f](https://github.com/multitheftauto/mtasa-blue/commit/eadbc9fef64484251d07ba8f7b4fdb09d36527f6), [8a63b6a](https://github.com/multitheftauto/mtasa-blue/commit/8a63b6ad5493d0e309f74395350862ddf14262d0) by **Dutchman101**)

- Added recovery for additional GTA crashes caused by exhausted video memory ([6a3b3af](https://github.com/multitheftauto/mtasa-blue/commit/6a3b3af02f3e812f092a60f8dced8e630824e017), [2381b12](https://github.com/multitheftauto/mtasa-blue/commit/2381b120c43ee8e473d5022cec8a492e8a051226), [0d8ff91](https://github.com/multitheftauto/mtasa-blue/commit/0d8ff91d044e0b97f439b3cd4a562211e6c74690) by **Dutchman101**)

- Fixed crashes while rendering fading or translucent entities with [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md) ([37fc495](https://github.com/multitheftauto/mtasa-blue/commit/37fc4959d2ded990ef8da09c292097d67c86ba1c), [1192325](https://github.com/multitheftauto/mtasa-blue/commit/1192325237276eb350d9b45c47feca860a1ae511) by **Dutchman101**)

- Fixed prolonged freezes from repeated failed streaming-file reads ([a276a18](https://github.com/multitheftauto/mtasa-blue/commit/a276a18cf53ef2b1d600e5b2ce4f8107b66ad62d), [2f51ce8](https://github.com/multitheftauto/mtasa-blue/commit/2f51ce8316613804b0c5afcf5a943357ecf77fff) by **Dutchman101**)

- Fixed stale spatial-database entries after element deletion and unsafe [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md) access during cleanup ([f129051](https://github.com/multitheftauto/mtasa-blue/commit/f129051bd659cc4d925f84f39e79f5aa6e815e37) by **Dutchman101**)

- Disabled the freeze watchdog by default to avoid terminating clients during slow but recoverable server-asset loading ([d566de5](https://github.com/multitheftauto/mtasa-blue/commit/d566de594629db5e4c96757c5e1fd4cf4386dd70) by **Dutchman101**)

- Fixed Seasparrow and Hunter guns not firing correctly ([e6c5153](https://github.com/multitheftauto/mtasa-blue/commit/e6c5153e30225217610b14a85ff0eb4a1d1fe429) by **Dutchman101**)

- Fixed expanded building-pool cleanup, stale entity pointers and pool-slot handling ([f41ccda](https://github.com/multitheftauto/mtasa-blue/commit/f41ccda9f4a3c6cc1272592abbce40e513de843a), [9b62794](https://github.com/multitheftauto/mtasa-blue/commit/9b62794d5abe5fcd055a9ca7ff387f0baf0ffc33), [1605c50](https://github.com/multitheftauto/mtasa-blue/commit/1605c502d828ee79f416b1edb317883bb195509a), [5aa6455](https://github.com/multitheftauto/mtasa-blue/commit/5aa6455703067a7512d5d42a17e8268be395f891) by **Dutchman101**)

- Fixed crashes in clothing-model rebuilding ([663c61a](https://github.com/multitheftauto/mtasa-blue/commit/663c61acbad4821b7dc37f9c050c7c5100497256), [f972479](https://github.com/multitheftauto/mtasa-blue/commit/f97247901ecf49ce06b815de849b93f2e08d27fc) by **Dutchman101**)

- Fixed SVG rendering crashes with malformed content or invalid dimensions ([1f85862](https://github.com/multitheftauto/mtasa-blue/commit/1f85862bba17cc175e8aecd5df93658ef19f0b96) by **Dutchman101**)

- Fixed crashes while updating streamed-in peds and querying ped movement state ([0ec0b60](https://github.com/multitheftauto/mtasa-blue/commit/0ec0b60f6fc693cce2afff079ed82f37592e42de), [5ece86b](https://github.com/multitheftauto/mtasa-blue/commit/5ece86b8acdd8ae3ad0ceb1f0627452341af56a9) by **Dutchman101**)

- Fixed vehicle-handling crashes, including custom vehicles created with [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md) ([aaac36a](https://github.com/multitheftauto/mtasa-blue/commit/aaac36a5abaf514ef1b490d3acc6eb7899a60562), [57e9d6b](https://github.com/multitheftauto/mtasa-blue/commit/57e9d6bc2280aca00f325f774e6f15cb3d4fe3ac) by **Dutchman101**)

- Improved building-removal, entity-bound and object-LOD processing performance ([929f4ef](https://github.com/multitheftauto/mtasa-blue/commit/929f4ef6da8dc552dd7080804f811dbf649a7872), [1727173](https://github.com/multitheftauto/mtasa-blue/commit/1727173d762c13d18c45828d64472994b7f6151b), [5091198](https://github.com/multitheftauto/mtasa-blue/commit/50911988d520c66a26d5e79743637314303a618e) by **Dutchman101**)

- Added a clearer message when the client exits because of an anti-cheat integrity violation ([18a5fb9](https://github.com/multitheftauto/mtasa-blue/commit/18a5fb90e45fc34156b7d900982aa4172e56c56d) by **Dutchman101**)

- Fixed the Rhino's behaviour on slopes ([1d0f4b9](https://github.com/multitheftauto/mtasa-blue/commit/1d0f4b9a77137028a768f9e159a3604cf686bf9f) by **Dutchman101**)

- Fixed [setVehicleComponentVisible](mta://scripting/client/functions/setvehiclecomponentvisible.md) showing undamaged components instead of respecting their damage state ([62028cf](https://github.com/multitheftauto/mtasa-blue/commit/62028cfecfd34b44aee4a9f493614eac8b0327f0) by **FileEX**)

- Fixed garages automatically opening or closing after the player dies or is arrested ([3e879e6](https://github.com/multitheftauto/mtasa-blue/commit/3e879e6b2f9281c65a43615e40962fab20289b1d) by **FileEX**)

- Fixed physical objects losing their rotation after streaming out and back in ([889b4c2](https://github.com/multitheftauto/mtasa-blue/commit/889b4c2d2a6c225004d7416b33e0ed3f7d7a1b90) by **FileEX**)

- Enabled headlight cones and coronas on the Rhino ([b690277](https://github.com/multitheftauto/mtasa-blue/commit/b6902774064c4715c49b33d0d1e57e7b565bff0e) by **rxyyy**)

- Improved client streaming performance when managing large numbers of elements ([6ae640e](https://github.com/multitheftauto/mtasa-blue/commit/6ae640e238e728d24925e4c71678a653a49bcefc) by **PrimelPrime**)

- Improved PostFX settings controls and added a Load defaults button ([16cdf3f](https://github.com/multitheftauto/mtasa-blue/commit/16cdf3f7720252687d9ca83f459232869ee8d375) by **omar-o22**)

- Fixed the CPU-affinity setting being applied too early during startup ([afb6fd7](https://github.com/multitheftauto/mtasa-blue/commit/afb6fd75ea05f44e46c2671418420b25719649a3) by **FileEX**)

- Clarified the first-time Discord Rich Presence data-sharing prompt ([9490ddb](https://github.com/multitheftauto/mtasa-blue/commit/9490ddb7fa626438c16ce484c51a5b000f4a7bc1) by **Lpsd**)

- Fixed texture-related crashes when restarting resources ([6154954](https://github.com/multitheftauto/mtasa-blue/commit/615495439d0dc4ca14ea501dc21354492d18d12a) by **Dutchman101**)

- Improved texture and shader loading, including shader matching on custom DFF models and after textures stream back in ([be2b2be](https://github.com/multitheftauto/mtasa-blue/commit/be2b2be4fe055634b0a7354f6421a9a07430f0e8) by **Dutchman101**)

- Fixed invalid model streaming accesses and a custom TXD tracking leak ([09d8852](https://github.com/multitheftauto/mtasa-blue/commit/09d8852ca0777c4789659fc96bc476313ccdde26) by **Dutchman101**)

- Fixed shader-related crashes when textures are unloaded ([876f2ec](https://github.com/multitheftauto/mtasa-blue/commit/876f2ecf5ccd9fc8b8308f10b121d74200df1def) by **Dutchman101**)

- Fixed textures becoming mixed when reapplying replacements that share a TXD ([f492e4d](https://github.com/multitheftauto/mtasa-blue/commit/f492e4d68e5223c78bc33712b8d0cc0450e1598c) by **Dutchman101**)

- Fixed texture memory leaks and improved texture replacement and restoration performance ([3ec8987](https://github.com/multitheftauto/mtasa-blue/commit/3ec89878945c5e86d64e560c7b1fe6e02665d5db) by **Dutchman101**)

- Fixed client freezes caused by corrupted texture lists during texture replacement and removal ([23f7911](https://github.com/multitheftauto/mtasa-blue/commit/23f7911287b3db31eec3aad5eb75e2d5a8ddfb91) by **Dutchman101**)

- Fixed main-menu refresh rate detection ([3d02b86](https://github.com/multitheftauto/mtasa-blue/commit/3d02b86df9f26934c81a96f1feacdc3e112bffc0) by **Dutchman101**)

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

- Fixed server-created ped deaths being synchronized despite synchronization being disabled ([9a05cea](https://github.com/multitheftauto/mtasa-blue/commit/9a05cea2e7697041c43cb6cc433b072c393211eb) by **justin**)

- Fixed lost [onPlayerConnect](mta://scripting/server/events/onplayerconnect.md) cancel reason ([63b2fc0](https://github.com/multitheftauto/mtasa-blue/commit/63b2fc0ce36a7927578b3d0d92a7ba9906781312) by **Federico Romero**)

- Fixed chat priority starvation under high load ([3d7128a](https://github.com/multitheftauto/mtasa-blue/commit/3d7128a8931c7b984ff3e6420f640144b9d410e2) by **Mohamed Maatallah**)

- Fixed HTTP response cookies using incorrect map keys ([02bd336](https://github.com/multitheftauto/mtasa-blue/commit/02bd33673c7ddba1d754aec35b90c3fd4cef00f6) by **Saifaldin Eabyad**)

- Fixed invalid ped skin IDs accepted by map/XML ped loading ([01c72fc](https://github.com/multitheftauto/mtasa-blue/commit/01c72fc4ab7de8e2436247152966983af0b133bc) by **lopsi**)

- Stopped logging ACL requests for rights a resource already has ([b1ccf89](https://github.com/multitheftauto/mtasa-blue/commit/b1ccf895e1f6762f347bea19d5fa34e9cf525b66) by **Mohamed Maatallah**)

- Fixed vehicle syncer hijacking through push synchronization ([f5bb36f](https://github.com/multitheftauto/mtasa-blue/commit/f5bb36f68281bbdd4afee81f274b52c3c569533e) by **Mohamed Maatallah**)

- Improved pulse sleeping on busy servers ([82d3dfe](https://github.com/multitheftauto/mtasa-blue/commit/82d3dfec4987dae24b459fef7aae1cd85d788dc7) by **Mohamed Maatallah**)

- Expanded "Player packet usage" statistics to include all packet types ([590a503](https://github.com/multitheftauto/mtasa-blue/commit/590a503ba5facfb536540a72817099db5597f2fc) by **Arran**)

- Improved server crash-handler reliability and prevented secondary failures from losing useful crash dumps ([5564f14](https://github.com/multitheftauto/mtasa-blue/commit/5564f1446829472328cc8ce8744af7ea93cb2659), [3f20e4f](https://github.com/multitheftauto/mtasa-blue/commit/3f20e4fd6555d357ce622ae2b6bebd658f943758), [9428164](https://github.com/multitheftauto/mtasa-blue/commit/94281643d7e5e1833fcdbfeaf68dc13d72ca6bf8), [2ae12e4](https://github.com/multitheftauto/mtasa-blue/commit/2ae12e438880caf0f3a39a4238acb1bb9958184d) by **Dutchman101**)

- Hardened server handling of malformed or excessive Lua payloads, latent transfers, screenshots, satchels, diagnostic packets and resource-start requests ([17fbf76](https://github.com/multitheftauto/mtasa-blue/commit/17fbf769934c9957f1c5821deed15c4f856836f6), [e22ffc4](https://github.com/multitheftauto/mtasa-blue/commit/e22ffc4634b4204230341264e67727c7fda8baf7), [4c34dbe](https://github.com/multitheftauto/mtasa-blue/commit/4c34dbe6620da20ea3490b1fb3e0007df8a10283), [d5b1645](https://github.com/multitheftauto/mtasa-blue/commit/d5b164504f6505a83568d1e447c5427f19415f2f), [2017171](https://github.com/multitheftauto/mtasa-blue/commit/2017171bf8ddcedc25301afb3a3795fa3e683655), [b627445](https://github.com/multitheftauto/mtasa-blue/commit/b627445d18e8888f2fe5d8021b5d93cfe922f2d5), [47e512c](https://github.com/multitheftauto/mtasa-blue/commit/47e512ca491128e591cd91d5708cfedacda9dbc1) by **Dutchman101**)

- Improved minimum-client-version enforcement reliability ([f4cfdeb](https://github.com/multitheftauto/mtasa-blue/commit/f4cfdeb61311075d3a7ae7793bbdfb22ceb73180) by **Dutchman101**)

- Removed 32-bit x86 server builds and required Windows 10 or later for the Windows server ([e0d8ccd](https://github.com/multitheftauto/mtasa-blue/commit/e0d8ccdf9509f03a15af86ad97aaf7da71975fde) by **lopsi**)

- Fixed camera synchronization when a player is standing on another element ([e96c8d4](https://github.com/multitheftauto/mtasa-blue/commit/e96c8d4fc04d2986307c74d7c364e546e4c699f5) by **Arran**)

- Fixed server-side positions of attached elements when their parent is rotated ([42a6a43](https://github.com/multitheftauto/mtasa-blue/commit/42a6a437604e7e62f1109f69d2e617db9e25c095) by **Xenius97**)

- Fixed server-side attachment rotation offsets and rotation calculations ([13c3b87](https://github.com/multitheftauto/mtasa-blue/commit/13c3b870fbb9b7a5bb6a824f55dc0ae210b02724) by **DamonOne**)

- Fixed server crashes when serving resource files and HTML pages over HTTP under memory allocation failures ([24c9c67](https://github.com/multitheftauto/mtasa-blue/commit/24c9c67693c2cf4419f6ca17bfc5d58c6892d4fd) by **Dutchman101**)

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

- Optimized Lua timer queue processing ([0beeb53](https://github.com/multitheftauto/mtasa-blue/commit/0beeb538e8340df68449a62e495a0ecc9164b924) by **Youssef Maged**)

- Optimized debug-hook management and the Lua timing profiler ([7fab391](https://github.com/multitheftauto/mtasa-blue/commit/7fab3910e26ec55616e967abd00dbc3cca33e848), [69b86b6](https://github.com/multitheftauto/mtasa-blue/commit/69b86b6c7bad82671319af7f97bfe72674beb08a) by **Mohab**)

- Improved GUI exception handling, avoided catching unrelated crashes, and fixed GUI parent casting ([6921e23](https://github.com/multitheftauto/mtasa-blue/commit/6921e23c6ecbaa3871011a0231ecf42385c1a4e0), [1df2b01](https://github.com/multitheftauto/mtasa-blue/commit/1df2b017cab59e98596e3b8239a8b05f1844f5f3), [22d10a4](https://github.com/multitheftauto/mtasa-blue/commit/22d10a4a4b81c43c92f4fc9a665ed250e0bff838) by **Dutchman101**, **lopsi**)

- Improved Steam library-loading reliability ([81fc135](https://github.com/multitheftauto/mtasa-blue/commit/81fc1355aa700a74d0834fb35e98a20d8d97ac87) by **Dutchman101**)

- Improved Windows version detection by avoiding compatibility-manifest shims ([21564b8](https://github.com/multitheftauto/mtasa-blue/commit/21564b8f354d30a1c245589d9fdf7f78facc608f) by **lopsi**)

- Fixed the nightly installer's configuration-file path ([7450aa0](https://github.com/multitheftauto/mtasa-blue/commit/7450aa018831c63b2548d2ae6f9f4d2f13e2ea8c) by **lopsi**)

- Restricted crash-symbol discovery to client binary directories ([330c23a](https://github.com/multitheftauto/mtasa-blue/commit/330c23a82d214e0469317416515772ac02dc3d71) by **Havi**)

- Added diagnostics for GTA exiting before the loading screen ([2242861](https://github.com/multitheftauto/mtasa-blue/commit/2242861840dc41c30cba320cf2f53fdc655a645b) by **Dutchman101**)

- Added Lua-function return support to the new argument parser ([6139037](https://github.com/multitheftauto/mtasa-blue/commit/6139037a039bc851dd4d8fa90017c431e70adb38) by **FileEX**)

- Migrated audio functions to the new argument parser ([212aa65](https://github.com/multitheftauto/mtasa-blue/commit/212aa65ae423dd7d5ab188984a6615edf95c557f) by **Youssef Maged**)

- Added automated client testing and sync-structure round-trip tests ([53521fa](https://github.com/multitheftauto/mtasa-blue/commit/53521fa8382632e8010ff1910724ff856ef2028f), [c4f5585](https://github.com/multitheftauto/mtasa-blue/commit/c4f55858c93afb4886f0227bf8d2c4cd6313e962) by **lopsi**)

- Disabled the freeze watchdog in Debug builds as well as release builds and set its optional timeout to 30 seconds ([936dec4](https://github.com/multitheftauto/mtasa-blue/commit/936dec4e3be5bc99bc0033b40f00fdddafcb3e8f) by **lopsi**)

- Improved diagnostics for heap-corruption and fast-fail exits, and prevented recursive debug output during stack-overflow handling ([010645f](https://github.com/multitheftauto/mtasa-blue/commit/010645ff5c6d8cdfb0a97c0253487a6bb132504b), [f5c4ec8](https://github.com/multitheftauto/mtasa-blue/commit/f5c4ec83028dfd8b9c593a08b5210a2aebe819f3) by **Dutchman101**)

- Fixed a crash in thread-pool handling ([31cda26](https://github.com/multitheftauto/mtasa-blue/commit/31cda26a0f94c760a59481eb2eaefefcd7858add) by **Dutchman101**)

- Improved numeric range validation, overflow checks and type safety across client and server code ([8a6e73a](https://github.com/multitheftauto/mtasa-blue/commit/8a6e73afc5283b4167f4bac5965745cbbdfa3eb6) by **Dutchman101**)

- Fixed server builds on RHEL/Fedora when using the mysql-devel package ([8eb7135](https://github.com/multitheftauto/mtasa-blue/commit/8eb71357f9b74517b87282b841b63b98a7216a1c) by **AlexTMjugador**)

- Restricted experimental train-track support to custom builds and fixed track IDs shifting when a default track is removed ([c78be3a](https://github.com/multitheftauto/mtasa-blue/commit/c78be3a36b5ec6f3358e4729e8faa8f6b3af8924), [b1d33b4](https://github.com/multitheftauto/mtasa-blue/commit/b1d33b48d2ccc681a4880a4f66ed2f33ff72ff79) by **qaisjp**)

- Prevented false freeze reports while a debugger is attached ([9acfad8](https://github.com/multitheftauto/mtasa-blue/commit/9acfad8d72686ce57667c7eb8c44f8d450d1e86d) by **FileEX**)

- Replaced launcher file-equivalence checks with native Windows file-identity checks ([9009984](https://github.com/multitheftauto/mtasa-blue/commit/9009984cb56ba17b89bfb1ce336f7e1c8b59d3f0) by **Marek Kulik**)

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

## 18 Vendor Updates

### Client

- Updated CEF to 152.0.5+gb129680+chromium-152.0.7977.54 ([322a139](https://github.com/multitheftauto/mtasa-blue/commit/322a139950084bd3d4e64fa071beebadf78b8b84), [543b4e1](https://github.com/multitheftauto/mtasa-blue/commit/543b4e19ec32e43ab453fbdf44f01e7e4c0743fb) by **Dutchman101**, **lopsi**)

- Updated LunaSVG to revision 0dd60d1 ([5b1c7d1](https://github.com/multitheftauto/mtasa-blue/commit/5b1c7d15ac9fe32d4370e445bc7060fa07578393) by **Lpsd**)

- Updated libpng to 1.6.50 ([[3]](https://github.com/multitheftauto/mtasa-blue/commit/c24b39d41fd768337c3d336a944588d53dfaba44) by **Nico834**)

- Updated Unifont to 15.1.05 ([02115a5](https://github.com/multitheftauto/mtasa-blue/commit/02115a5c00e2480bbb3b829b655869e7436de955) by **Dutchman101**)

### Server

- Replaced the EHS HTTP server with cpp-httplib ([45c5323](https://github.com/multitheftauto/mtasa-blue/commit/45c5323eb669ea839f18251a97642f1e6f402734) by **lopsi**)

- Updated cURL to 8.14.1 ([[4]](https://github.com/multitheftauto/mtasa-blue/commit/7c27c20da7503c68234cde0b726f10a3dcdf85e3) by **Nico834**)

- Updated MySQL to 8.4.0 & OpenSSL to 3.3.1 ([a44d673](https://github.com/multitheftauto/mtasa-blue/commit/a44d673bb8731506418fdbaa6690b339a98d82c1) by **botder**)

- Updated SQLite to 3.46.0 ([30e31af](https://github.com/multitheftauto/mtasa-blue/commit/30e31af2ca1ae96e03386670a9df6db70336b968) by **Dutchman101**)

### Shared

- Updated FreeType to 2.14.3 ([1c71d77](https://github.com/multitheftauto/mtasa-blue/commit/1c71d772fda4bbca2b36fb63bea0df4535be4889) by **lopsi**)

- Replaced PCRE1 with PCRE2 ([293063b](https://github.com/multitheftauto/mtasa-blue/commit/293063b6b4edb29a15d23b6f22a68e7a1cad777b), [7ea5d40](https://github.com/multitheftauto/mtasa-blue/commit/7ea5d40004cfc6d3a1440cbbc563f0eab8613250) by **lopsi**)

- Updated libcurl to 8.20.0 ([5dd92ca](https://github.com/multitheftauto/mtasa-blue/commit/5dd92ca6e8bceca453c68b42f98fd9bd6e231e63) by **lopsi**)

- Updated json-c to revision d1018cf ([24126f6](https://github.com/multitheftauto/mtasa-blue/commit/24126f6977cc808b0c0abad39cf700e500eb447a) by **lopsi**)

- Replaced TinyXML with TinyXML2 ([a750e58](https://github.com/multitheftauto/mtasa-blue/commit/a750e5824f3a873a5110548678a67ca52e1bf739) by **lopsi**)

- Updated mbedTLS to 3.6.4 ([[5]](https://github.com/multitheftauto/mtasa-blue/commit/45955dad5471f49e2784e37cbafd1b92196abe96) by **Nico834**)

- Updated 7-Zip Standalone plugins to 24.07 (24.7.0.0) ([9b979b2](https://github.com/multitheftauto/mtasa-blue/commit/9b979b2d5c7f4b885046a85d9895e58416563890) by **Dutchman101**)

- Updated nvapi from r550 to r555 ([5fdcada](https://github.com/multitheftauto/mtasa-blue/commit/5fdcada80a18af530381b04f54c3c69b6988f479) by **Dutchman101**)

- Updated unrar to 7.0.9 ([ab9461b](https://github.com/multitheftauto/mtasa-blue/commit/ab9461be5777427261bc3a330acb4c0f5cdc2c8b) by **Dutchman101**)

- Updated zlib from 1.2.13 to 1.3 ([0f37ac0](https://github.com/multitheftauto/mtasa-blue/commit/0f37ac0b18845e9f035d0ca45bbb41b9cd1aa979) by **Dutchman101**)

## Resources

### 95+ Changes and Bug Fixes

**admin**

- Fixed resource settings for resource names containing special characters ([164886b](https://github.com/multitheftauto/mtasa-resources/commit/164886bf7cc05cc29060c236909cf43161c35589) by **Elabyad247**)

- Fixed the Nepalese flag's aspect ratio ([6aacf71](https://github.com/multitheftauto/mtasa-resources/commit/6aacf718a3d29fe0b8f5e87563c3c71d36058743) by **SpeedyFolf**)

- Added buttons to enable, disable and delete selected ACL rights ([839b1d1](https://github.com/multitheftauto/mtasa-resources/commit/839b1d1f784de598e308a18fcf29cb1798913690) by **rekznoz**)

- Fixed the ACL deletion permission name and obtained player versions directly on the server ([e69d8dc](https://github.com/multitheftauto/mtasa-resources/commit/e69d8dc7ec3b18028b8a260394200ee37c3c0a71) by **DmitriyColeman**)

- Fixed search fields interpreting special characters as Lua patterns ([ea7917f](https://github.com/multitheftauto/mtasa-resources/commit/ea7917fee2a01a99dedf10256b8a38d6c31e5858) by **omar-o22**)

- Moved anonymous-admin state from synchronized element data to server-side tables with permission-checked updates ([8a717a2](https://github.com/multitheftauto/mtasa-resources/commit/8a717a2d4e4eb7bd716aab4977eab3fab44f3572) by **omar-o22**)

- Added a Delete All button for stored screenshots, controlled by the command.deleteallscreenshot ACL right ([defb2e5](https://github.com/multitheftauto/mtasa-resources/commit/defb2e5a92457f52cec46b20aeb2ed3bdcd749a3) by **rekznoz** and **Lpsd**)

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

- Fixed ACL handling for resource names containing special characters ([164886b](https://github.com/multitheftauto/mtasa-resources/commit/164886bf7cc05cc29060c236909cf43161c35589) by **Elabyad247**)

- Added a mute-management panel with database-backed mute records and fixed anonymous-admin handling ([1963f78](https://github.com/multitheftauto/mtasa-resources/commit/1963f7884020cb01a05346c59d7e12dc4ca76fb8), [6f0e337](https://github.com/multitheftauto/mtasa-resources/commit/6f0e337e4cf2de31f0d716e089378e1105ed74d9) by **omar-o22**, **ArranTuna**)

- Implemented the automatic-scripts controls ([45be6b1](https://github.com/multitheftauto/mtasa-resources/commit/45be6b164c8890cd93574eb287bb594f62fe9ea0) by **ArranTuna**)

- Fixed click handlers to act on the intended mouse-button state ([60b670e](https://github.com/multitheftauto/mtasa-resources/commit/60b670e0d8d3fef39e1f698a83a782573e4efb45) by **ArranTuna**)

- Fixed errors when closing player statistics and sending admin chat from console commands ([883452e](https://github.com/multitheftauto/mtasa-resources/commit/883452e98e71ce8a03b17641a3708cdd1f50ea79), [ada67cf](https://github.com/multitheftauto/mtasa-resources/commit/ada67cf2f2877080f992dcf738479fa87644972e) by **NightWatch404**)

- Changed world-special-property controls to use the server-side API ([5697879](https://github.com/multitheftauto/mtasa-resources/commit/5697879d10967aa7935576f9547891b6e9a448e7) by **ArranTuna**)

- Removed unused performance options ([44def18](https://github.com/multitheftauto/mtasa-resources/commit/44def18f11507c9ea9ff9309b635d0d9049d8699) by **ArranTuna**)

- Improved radar teleporting with collision preloading, ground-height detection, server-side permission checks and logging ([4423fa5](https://github.com/multitheftauto/mtasa-resources/commit/4423fa5639fd04921f55ae2e63ca8b2cbf3e30de) by **DmitriyColeman**)

- Fixed search fields interpreting special characters as Lua patterns ([ea7917f](https://github.com/multitheftauto/mtasa-resources/commit/ea7917fee2a01a99dedf10256b8a38d6c31e5858) by **omar-o22**)

- Moved anonymous-admin state from synchronized element data to server-side tables with permission-checked updates ([8a717a2](https://github.com/multitheftauto/mtasa-resources/commit/8a717a2d4e4eb7bd716aab4977eab3fab44f3572) by **omar-o22**)

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

- Fixed newly created objects being saved with zero scale ([578598a](https://github.com/multitheftauto/mtasa-resources/commit/578598a68a70ca9ca069716f09193352a2da0ea2) by **q8X**)

- Fixed vehicle rotation conversion and loading/saving old race maps with legacy rotations ([2a84fc6](https://github.com/multitheftauto/mtasa-resources/commit/2a84fc682e58187b23dad63457f1746960116382), [9805a53](https://github.com/multitheftauto/mtasa-resources/commit/9805a539f6117551caaa915df8cd1ccfde9c018f) by **q8X**)

- Fixed save/load errors leaving the editor permanently locked ([f19727e](https://github.com/multitheftauto/mtasa-resources/commit/f19727ec5057da9d94176d9a331924bb6266371e) by **ArranTuna**)

- Preserved settings unknown to older editor versions ([090a112](https://github.com/multitheftauto/mtasa-resources/commit/090a11209928f7146fd14a193f1e8167e4e82b64) by **ArranTuna**)

- Added optional hover bounding-box highlights, disabled by default, and fixed duplicate boxes and highlights remaining in test mode ([bbffcbe](https://github.com/multitheftauto/mtasa-resources/commit/bbffcbe8fe191deb3c01fd61994fbd44774a52be), [0175e20](https://github.com/multitheftauto/mtasa-resources/commit/0175e209c8714c798589bcb09eab529b9254ddfa), [af5df72](https://github.com/multitheftauto/mtasa-resources/commit/af5df728adf3d9d35c613384112add456b039232), [83af5fe](https://github.com/multitheftauto/mtasa-resources/commit/83af5fe89a0c1db7f5e98a9f9a818ad6190690ed) by **x-Crown**, **ArranTuna**)

- Added local-space movement controls ([c7fd4e7](https://github.com/multitheftauto/mtasa-resources/commit/c7fd4e74ff2d77aaedf0bd223597331cf52ecf4e) by **q8X**)

- Fixed debug errors when saving maps ([cda943e](https://github.com/multitheftauto/mtasa-resources/commit/cda943e194caf7bb5b8520dc9972c0c0f2ae143d) by **ArranTuna**)

- Added simple moving objects with configurable offsets, movement speed and delay, including movement previews in the editor ([25ba6cd](https://github.com/multitheftauto/mtasa-resources/commit/25ba6cd81d1b12431e1e66e71d286d6b00953bf5) by **IIYAMA12**)

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

- Added missing vehicles (Rancher Lure, RC Cam, damaged Glendale, and damaged Sadler) to the vehicle list ([ffae4bb](https://github.com/multitheftauto/mtasa-resources/commit/ffae4bbbdc81de9d2225fae322de258a81f3b51d) by **SpeedyFolf**)

**fallout**

- Refactor & many improvements ([c733b69](https://github.com/multitheftauto/mtasa-resources/commit/c733b69a735d004235ba61b1201ac1412acc6482) by **IIYAMA12**)

**freeroam**

- Fixed the cursor being hidden while another GUI is still open ([a1da280](https://github.com/multitheftauto/mtasa-resources/commit/a1da280a65061f986f14a047bd6e871a761207d7) by **ArranTuna**)

- Added missing vehicles (Rancher Lure, damaged Glendale, and damaged Sadler) to the vehicle list ([9053fc9](https://github.com/multitheftauto/mtasa-resources/commit/9053fc905775a4cee01f830e3801e0cb48e9bed6) by **SpeedyFolf**)

- Added weapon ID 13 to the weapon list ([8c5506f](https://github.com/multitheftauto/mtasa-resources/commit/8c5506fd3b2b91b8ba808fc85813940e8b538fc1) by **SpeedyFolf**)

- Updated skins.xml ([cacbe40](https://github.com/multitheftauto/mtasa-resources/commit/cacbe40a805402dec3a62180b987d4b777817ea6) by **shadylua**)

- Added Walk styles ([4a18d75](https://github.com/multitheftauto/mtasa-resources/commit/4a18d7585a2fa45eaed18d4b4796744a235a23c5) by **shadylua**)

- Security improvements ([2ec9213](https://github.com/multitheftauto/mtasa-resources/commit/2ec92132036d0dc073279dda3c88d71f578d651f) by **IIYAMA12**)

- Fixed freezetime flickering ([b40f27b](https://github.com/multitheftauto/mtasa-resources/commit/b40f27be0274b641c2cddd4c75a6f86f73ea4941), [817aa1e](https://github.com/multitheftauto/mtasa-resources/commit/817aa1ea9130fbccb1a23b7410309af2f8a21ddc) by **ricksterhd123** and **jlillis**)

- Fixed map key bind interferes with race editor help ([e62bc54](https://github.com/multitheftauto/mtasa-resources/commit/e62bc5471433b347b16c15709d469209cf202390) by **MittellBuurman**)

- Fixed player blips staying visible after closing spawn map with F1 ([1a5031c](https://github.com/multitheftauto/mtasa-resources/commit/aaf2dd7ed7a0b6b6c6609a4ee5d8319101e8a674) by **omar-o22**)

**hedit**

- Filled missing translations, added English fallback text, and improved the saved-handling list and confirmation dialogs ([b5ccbd8](https://github.com/multitheftauto/mtasa-resources/commit/b5ccbd8a4dfc28a23079645172da6f32e524aeb9) by **denjifb**)

- Added the missing Turkish translation for the handling preset Delete button ([64dba8e](https://github.com/multitheftauto/mtasa-resources/commit/64dba8e12f81146b2b0d231753d952619c07ffb7) by **denjifb**)

- Added German localization  ([bc33634](https://github.com/multitheftauto/mtasa-resources/pull/568/commits/c58df8666fbccfb0be73f27c52aa680dae2f0c1a) by **shadylua**)

- Added Brazilian Portuguese localization  ([d1b85d7](https://github.com/multitheftauto/mtasa-resources/commit/d1b85d7dda45293ce497cf03f21eea2f59100b89) by **ricksterhd123**)

- Added Hungarian localization  ([53050dd](https://github.com/multitheftauto/mtasa-resources/commit/53050dd0bf73a164969480c9277fc3c6b0601b7e) by **Nico834**)

- Updated Turkish localization  ([3044d00](https://github.com/multitheftauto/mtasa-resources/commit/3044d00a796488870556b19b088ac505c332952c) by **mahlukat5**)

- Updated Spanish localization  ([b74c239](https://github.com/multitheftauto/mtasa-resources/commit/b74c2393cc15e403d4588ebb671659c16cc36269) by **kxndrick0**)

**internetradio**

- Reduced CPU usage and improved radio playback and track-name handling ([ca490a4](https://github.com/multitheftauto/mtasa-resources/commit/ca490a4a1558c9a648a0262b2b5b4b33dd70c3ed), [963db3a](https://github.com/multitheftauto/mtasa-resources/commit/963db3ae13ebeab3e2e39e005142ecd4f97ad245), [62a1805](https://github.com/multitheftauto/mtasa-resources/commit/62a1805716c63a2d3a88de8547c8db823a0643a5) by **Dutchman101**)

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

- Removed repeated debug logging when using the map editor ([50a8649](https://github.com/multitheftauto/mtasa-resources/commit/50a8649114051cea31069529149a24a926501a61) by **ArranTuna**)

- Fixed that the resource "playercolors" should be activated for teams ([2cd28db](https://github.com/multitheftauto/mtasa-resources/commit/2cd28db5fa891f361c5af07a491532378a820b83) by **T-MaxWiese-T**)

- Real-time update of settings ([9505b18](https://github.com/multitheftauto/mtasa-resources/commit/9505b181fe7fc2bab53142746f73bc64a8fd984d) by **Nico834**)

- Improved debug messages ([4084e5d](https://github.com/multitheftauto/mtasa-resources/commit/4084e5d369907d3ededd1b2eb19c916983680154) by **T-MaxWiese-T**)

- Fixed that when a player changed or joined teams the color of the blip was not updated ([ff80005](https://github.com/multitheftauto/mtasa-resources/commit/ff80005f114a3d010624f7d54510ffde47dddb00) by **T-MaxWiese-T**)

**playercolors**

- Player nametag color should revert to team color when the resource is stopped ([d45d2d0](https://github.com/multitheftauto/mtasa-resources/commit/d45d2d0cd963186639d76ab1cb27ef6a042cd0bd) by **T-MaxWiese-T**)

- Fixed chat messages sent twice ([0547cf7](https://github.com/multitheftauto/mtasa-resources/commit/0547cf72514a7dc7efc987f47903c35b310a3b22) by **Fernando-A-Rocha**)

**performancebrowser**

- Added configurable client-side Lua timing recordings, disabled on the client by default ([4c2a6ae](https://github.com/multitheftauto/mtasa-resources/commit/4c2a6ae96637d2c895eb7dcd09a820ed8cd199fe) by **jjustns**)

- Added Lua time recordings to the web performance browser to record resources with high server CPU usage ([faa1d3b](https://github.com/multitheftauto/mtasa-resources/commit/faa1d3b554c961b07a500e29fa0838be9e793ba6) by **Xenius97** and **Lpsd**)

- Fixed player names not being reinitialized on change ([3e0166d](https://github.com/multitheftauto/mtasa-resources/commit/3e0166dc7fa9c11c596a7958b02423b6aeff8410) by **YelehaUwU**)

**reload**

- Prevented restarting a weapon reload while the player is already reloading ([4ae0ea4](https://github.com/multitheftauto/mtasa-resources/commit/4ae0ea47d717ea1a9e5c28d7a914fad174169403) by **DmitriyColeman**)

**runcode**

- Added aclrequest for loadstring function ([c40b809](https://github.com/multitheftauto/mtasa-resources/commit/c40b8095f054b6e87b46e1d53d9b6ec77cf943c7) by **IIYAMA12**)

**scoreboard**

- Replaced drawing arrow from path to texture ([128f269](https://github.com/multitheftauto/mtasa-resources/commit/128f26952810804df6acb233ca9476853caa1286) by **srslyyyy**)

**speedometer**

- Added a numeric km/h readout and headlight-status icon ([e63fb50](https://github.com/multitheftauto/mtasa-resources/commit/e63fb505263de3f93f261002586e3639a0505faa) by **DateFTP**)

- Updated the speedometer artwork and fixed scaling on different resolutions and aspect ratios ([bb4471e](https://github.com/multitheftauto/mtasa-resources/commit/bb4471e76d04499ff17a91c5b9ce3226718bfbec) by **Haxardous**)

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

- Fixed render-target restoration, coroutine handling and missing-node checks ([269d876](https://github.com/multitheftauto/mtasa-resources/commit/269d87614de01a83313eb610186dbd4870cc7642) by **iManGaaX**)

- Added export functions for custom logic ([537d92d](https://github.com/multitheftauto/mtasa-resources/commit/537d92d11b357cf9e795a7bb3ec87c13fa62c7bc) by **T-MaxWiese-T**)

**deathmatch**

- Fixed spectating errors when no other players are available ([ad9c8f8](https://github.com/multitheftauto/mtasa-resources/commit/ad9c8f8e1c33f4bb1e939e32ec9d2895bfc87327) by **ArranTuna**)

- Improvements and update ([a01ec8a](https://github.com/multitheftauto/mtasa-resources/commit/a01ec8a86e636ca61f25a03d4ee30bd898754cbd), [b94ffdd](https://github.com/multitheftauto/mtasa-resources/commit/b94ffddfd5b230544d54e5eca8c9c5d87dc69128) by **jlillis**

**race**

- Made the race-finish ranking board scrollable ([68dd658](https://github.com/multitheftauto/mtasa-resources/commit/68dd658c6e6094dc3b4a93e2530b084b178552f0) by **ArranTuna**)

- Added the Rustler to the armed-vehicle list ([e742dc9](https://github.com/multitheftauto/mtasa-resources/commit/e742dc9ec2f01f0a553820939b1b38dc8418d288) by **SpeedyFolf**)

- Fixed automatic nextid assignment breaking ([2c695a9](https://github.com/multitheftauto/mtasa-resources/commit/2c695a9e793825a8cafd2ee3be490d2d8e9ad318) by **LotsOfS**)

**voice_local**

- Improvements ([53cf63d](https://github.com/multitheftauto/mtasa-resources/commit/53cf63d83169018e0de9f45ecb565958855d717d) by **Fernando-A-Rocha**)

**Others / Uncategorized**

- Refactor of resources meta.xml ([6713b07](https://github.com/multitheftauto/mtasa-resources/commit/6713b07a459739c06112ac3e608776f3f0696144) by **Fernando-A-Rocha**)

**assault**

- Fixed numeric-string conversion errors ([dcb7045](https://github.com/multitheftauto/mtasa-resources/commit/dcb7045132e4bc73ac9f253a19f23a85e6f739d0) by **ArranTuna**)

**deathmessages**

- Fixed errors when a vehicle has no controller ([a2c21c9](https://github.com/multitheftauto/mtasa-resources/commit/a2c21c92c602f5e774dc299e0880d68a714c125f) by **iManGaaX**)

**dialogs**

- Fixed button checks and sound-volume validation ([81b2454](https://github.com/multitheftauto/mtasa-resources/commit/81b245426f0da055dfa323e4a9667ca7a74dd717) by **iManGaaX**)

**freecam**

- Smoothed camera movement ([02d2363](https://github.com/multitheftauto/mtasa-resources/commit/02d2363363cca85791eb7b9202f5704ffb445aa1) by **ArranTuna**)

**helpmanager**

- Replaced help tabs with a grid list, improved column sizing and fixed resource-element handling ([2fdfb4b](https://github.com/multitheftauto/mtasa-resources/commit/2fdfb4b2d889d5a8f79ec4a098a767aef34bbff0), [b715fb2](https://github.com/multitheftauto/mtasa-resources/commit/b715fb289549a15462ebaedf1c173b09f395f56e), [1779da0](https://github.com/multitheftauto/mtasa-resources/commit/1779da0ebc8adc485361796b872a79ee7d97b266) by **ArranTuna**, **iManGaaX**)

**killmessages**

- Fixed texture-cache leaks and vehicle-occupant icon lookup ([1205e30](https://github.com/multitheftauto/mtasa-resources/commit/1205e303f0cc6a788885def3085fbc8ade42487a) by **iManGaaX**)

**security**

- Fixed player-data leaks on quit and added element validation ([d06e21c](https://github.com/multitheftauto/mtasa-resources/commit/d06e21c2730187774ce19d8feadb9ba68f7d2000) by **iManGaaX**)

**spawnmanager**

- Fixed runtime errors and spawn-data validation ([8102caa](https://github.com/multitheftauto/mtasa-resources/commit/8102caa749f848981f5e814ec2b252f67d3bd5b7) by **iManGaaX**)

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
