---
doc_id: "mta-wiki:8623"
title: "Changes in 1.5.3"
source_title: "Changes in 1.5.3"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.3"
revision_id: 75878
language: "en"
categories: ["Changelog"]
---

# Changes in 1.5.3

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

1.5.3 was released on October 20, 2016.

- Changelog on Mantis: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- Full changelog: [https://github.com/multitheftauto/mtasa-blue/commits/master?page=1](https://github.com/multitheftauto/mtasa-blue/commits/master?page=1)

## Main Additions / Changes

- Significantly reorganized build system

- Major code cleanups

- Fixed multiple popular crashes

- Improved streaming of low LOD objects and increased limits

- Updated many dependencies

- Added support for German Steam version of GTASA (thanks to Lakota, Mario and @Sh4dowReturns)

## Scripting

### Client

- Added [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md), [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md), [navigateBrowserBack](mta://scripting/client/functions/navigatebrowserback.md), [navigateBrowserForward](mta://scripting/client/functions/navigatebrowserforward.md), [reloadBrowserPage](mta://scripting/client/functions/reloadbrowserpage.md) (thanks to **mabako**!)

- Added [resizeBrowser](mta://scripting/client/functions/resizebrowser.md)

- Added [setVehicleWindowOpen](mta://scripting/client/functions/setvehiclewindowopen.md)

- Added alternative syntax to [guiGridListAddRow](mta://scripting/client/functions/guigridlistaddrow.md) and [guiGridListInsertRowAfter](mta://scripting/client/functions/guigridlistinsertrowafter.md)

- Added *browser* parameter to [getBrowserSource](mta://scripting/client/functions/getbrowsersource.md) callback

- Added [createTrayNotification](mta://scripting/client/functions/createtraynotification.md) and [isTrayNotificationEnabled](mta://scripting/client/functions/istraynotificationenabled.md) (thanks to **Necktrox**)

### Server

- Added support for multiple statements in [dbQuery](mta://scripting/server/functions/dbquery.md)/[dbExec](mta://scripting/server/functions/dbexec.md)

- Added manuallyChanged parameter to [onPlayerChangeNick](mta://scripting/server/events/onplayerchangenick.md)

- Added [onPlayerWeaponFire](mta://scripting/server/events/onplayerweaponfire.md) (thanks to **lopezloo**)

- Added [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md) (thanks to **zneext**)

- Added *readOnly* option to [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

### Shared (*Client & Server side*)

- Fixed [fileRead](mta://scripting/shared/functions/fileread.md) crashing when reading more than 10000 bytes

- Added [fileGetPath](mta://scripting/shared/functions/filegetpath.md)

- Added option for [addDebugHook](mta://scripting/shared/functions/adddebughook.md) to skip event/functions

- Added duplicate log line filter for script debugging

- Improved internal error logging

- Added [inspect](mta://scripting/shared/functions/inspect.md), [iprint](mta://scripting/shared/functions/iprint.md) and [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md) now works with any kind of vehicle, including motorbikes (thanks to **lopezloo**)

- Added blend parameter for [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md) (thanks to **lex128**)

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) calls *tostring* on the passed value now

- Added masking of certain function arguments when using [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

## Client

### Client: Additions

- Enabled code signing for *CEFLauncher.exe* to improve anti virus software compatibility

- Added client resource files path info to Advanced tab

- MTA uses the native resolution by default now

- Security tweaks

- Added support for objects and weapons in ped damage events (thanks to lopezloo)

- Added option for [addDebugHook](mta://scripting/shared/functions/adddebughook.md) to skip event/functions

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md) is now cancellable if the local player is entering the vehicle

- Water elements are now limited to a specific dimension

- Made Lua clear loaded files automatically when dereferenced

- Tweaked CEF performance significantly

- Improve linux compatibility

### Client: Bugfixes & Changes

- Removed VS2008 redistributable from installer as it is no longer required

- Fixed [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md) breaking JSON decoding (thanks to **mabako**)

- Updated CEF

- Tweaked optimus detection

- Added missing model name for model 6458

- Fixed LOD object issues (see [https://bugs.mtasa.com/view.php?id=9242](https://bugs.mtasa.com/view.php?id=9242))

- Fixed colshape related crashes (thanks to **lopezloo**)

- Tweaked logic of client resource file validation

- Fixed [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md) not muting the sound correctly on some websites e.g. YouTube

- Fixed client incorrectly handling 'no' answer to recommended update question

- Fixed self-created water becoming invisible sometimes (thanks to **lopezloo**)

- Fixed [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md) calculation (thanks to lex128)

- Fixed [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md) incorrectly handling keys sometimes (thanks to Necktrox)

- Fixed sniper scope disappearing after killing a ped (thanks to **lopezloo**)

- Fixed team members not fully synced until re-set by [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md) or respawn

- Fixed MTA sometimes not loading custom textures

- Deprecated [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md)

- Fixed [redirectPlayer](mta://scripting/server/functions/redirectplayer.md) with an empty host logging ambiguously

- Fixed a 1-frame lag of [attachElements](mta://scripting/shared/functions/attachelements.md)

- Changed [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md) to not recreate the object

- Fixed desktop resolution when minimizing with fullscreen borderless window mode

- Disabled CEF plugins (e.g. Flash Player)

- Fixed CEF popups (e.g. <select> boxes) not being rendered correctly

- Fixed MTA slowly updating position of attached elements

## Server

### Server: Additions

- Added icon for the Windows server

- Added server logging for [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- Added 8 byte integer support for varargs database queries

- Added option to block server admins who login with an unrecognized serial

### Server: Bugfixes & Changes

- Fixed compatibility issues on older CPU architectures

- Fixed modules being broken for some revisions

- Removed warnings for .png files with JPEG contents

- Changed remaining <min_mta_version> errors to warnings

- Changed server private IP error to a warning

- Fixed [dbPoll](mta://scripting/server/functions/dbpoll.md) returning early when timeout is used

- Fixed a connecting player being able to block resources from starting

- Fixed server crash when using db* functions during [onDebugMessage](mta://scripting/server/events/ondebugmessage.md) event

- Fixed [onElementStopSync](mta://scripting/server/events/onelementstopsync.md) not being triggered when player disconnects

- Fixed Fire Extinguisher not triggering [onPedWasted](mta://scripting/server/events/onpedwasted.md)

- Fixed [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md) returning the marker type

- Fixed protected resources being stoppable

- Fixed [aclReload](mta://scripting/server/functions/aclreload.md) reverting recently scripted ACL changes

## Resources

- Race: Fixed parameters in 'onGamemodeMapStop' event (thanks to **PhrozenByte**)

- Adminpanel: Added unban dates to bans and allowed defining custom ban times for offline bans (thanks to **Dutchman101**)

- Runcode: Improved support for return statements

- Runcode: Added hidden *me* variable

- Missiontimer: Fixed events triggering when client is not ready (thanks to **Einheit-101**)

## Editor

- Added map backups

- Enabled OOP support in [EDF](https://wiki.multitheftauto.com/index.php?search=EDF) scripreader (thanks to **PhrozenByte**)

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
