---
doc_id: "mta-wiki:7641"
title: "Changes in 1.4"
source_title: "Changes in 1.4"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.4"
revision_id: 50646
language: "en"
categories: ["Changelog", "Changes_in_1.4"]
---

# Changes in 1.4

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

- Localization of MTA's menus

- [OOP](mta://tutorials/oop.md) classes

- [Matrices](mta://reference/misc/matrix.md) and [Vectors](mta://reference/misc/vector.md)

- Significantly improved train synchronization

- Improved all sound functions to work with player elements

## Scripting

### Scripting: New functions

#### Client

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getLocalization](mta://scripting/client/functions/getlocalization.md)

- [isChatVisible](mta://scripting/client/functions/ischatvisible.md)

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [isTrainChainEngine](mta://scripting/client/functions/istrainchainengine.md)

#### Server

- [isBan](mta://scripting/server/functions/isban.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

#### Shared (*Client & Server side*)

- [isElementWaitingForGroundToLoad](mta://scripting/client/functions/iselementwaitingforgroundtoload.md)

- Added additional optional parameter bInstant to setPlayerMoney to instantly set the money without counting up/down

- Fixed toJSON/fromJSON not handling binary data properly

### Scripting: New Events

#### Client

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

#### Server

- [onWeaponFire](mta://scripting/server/events/onweaponfire.md)

### Scripting: Changes, Bugfixes and Additions

- Fixed getResourceConfig() not working on foreign resources

- Fixed the Brown Streak Carriage (ID: 570)

- Changed attachTrailerToVehicle to support trains

## Client

### Client: Additions

- Distinguish between left and right Shift, Ctrl and Alt presses.

- Added SettingHUDMatchAspectRatio, SettingAspectRatio to dxGetStatus.

- Added support for the use of [Opus Codec](https://en.wikipedia.org/wiki/Opus_codec) audio files in playSound and playSound3D.

### Client: Bugfixes & Changes

- Fixed the money "counts down" GTA-Style when you change a server.

- Fixed peds being invulnerable to gun fire when doing a drive by.

- Fixed onClientPlayerDamage not triggering for spray can.

- Satchels should now be removed on [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md).

- Fixed getPedMoveState returns false when moving in crouch state

- Fixed guiScrollPaneGetVerticalScrollPosition returning strange and stepped values.

- Fixed setPedCameraRotation not working.

- Fixed peds continuing to fire their weapons after running out of ammo.

- Fixed radio titles not always showing.

- Fixed radio music skipping when browsing between different channels.

- Fixed user track skip (F5) being disabled.

- Fixed vehicles falling through the map.

## Server

### Server: Additions

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) should now apply to children

- More descriptive module error messages

- Commands: unloadmodule and reloadmodule

- Added server side custom weapons.

### Server: Bugfixes & Changes

- Fixed 128 character limit in [setAccountData](mta://scripting/server/functions/setaccountdata.md)

- Wildcard bans should now be checked properly on connect

- Fixed Team members not being sent to clients if set in [onResourceStart](mta://scripting/server/events/onresourcestart.md).

## Resources

- None yet

## Editor

- None yet

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and Google Code repositories:*

- [MTA: SA Blue](https://code.google.com/p/mtasa-blue/source/list)

- [MTA: SA Official Resources](https://code.google.com/p/mtasa-resources/source/list)
