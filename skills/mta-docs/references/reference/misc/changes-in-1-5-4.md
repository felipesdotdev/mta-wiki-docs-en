---
doc_id: "mta-wiki:9316"
title: "Changes in 1.5.4"
source_title: "Changes in 1.5.4"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.4"
revision_id: 75877
language: "en"
categories: ["Changelog"]
---

# Changes in 1.5.4

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

1.5.4 was released on April 22, 2017.

- Changelog on Mantis: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- Full changelog: [https://github.com/multitheftauto/mtasa-blue/commits/master?page=1](https://github.com/multitheftauto/mtasa-blue/commits/master?page=1)

## Main Additions / Changes

- Security tweaks for both server and client

- Enabled *Authorized Serial Protection* by default

- Code refactoring and improvements to our build system (also added Clang support)

## Scripting

### Client

- Added "sniper moon", "random foliage" and "extra air resistance" properties to [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md) (thanks to **ZReC**)

- Added [getVehiclesLODDistance](mta://scripting/client/functions/getvehiclesloddistance.md), [setVehiclesLODDistance](mta://scripting/client/functions/setvehiclesloddistance.md) and [resetVehiclesLODDistance](mta://scripting/client/functions/resetvehiclesloddistance.md) (thanks to **lopezloo**)

- Added [setDebugViewActive](mta://scripting/client/functions/setdebugviewactive.md)

### Shared (*Client & Server side*)

- Added [passwordHash](mta://scripting/shared/functions/passwordhash.md) and [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- Added *queue* name parameter to [fetchRemote](mta://scripting/shared/functions/fetchremote.md) to support parallel downloads

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) now supports element omnipresence, which means that an element can be in all dimensions at once (thanks to **zneext**)

## Client

### Client: Additions

### Client: Bugfixes & Changes

- Corona markers should now have a correct attach offset position (thanks to **lopezloo**)

- Fixed very lage radar areas not being visible (thanks to **ZReC**)

- Disabled CEF sandbox due to problems (might be re-enabled soon)

- Updated CEF and other 3rd party dependencies

- Fixes for some crashes and improvements for error handling for installation and startup issues

- Removed max password length limit for server account passwords (thanks to **4O4**)

- Improved multi-monitor support in windowed fullscreen mode

- Improved performance of [dxGetPixelsSize](mta://scripting/client/functions/dxgetpixelssize.md)

- Tweaked joystick support

- Fixed [playSound](mta://scripting/client/functions/playsound.md) not supporting unicode in URLs

- Increased default max streaming memory

## Server

### Server: Additions

- Added *fakelag* command

- Added option to allow locally modified (gta3.img) vehicles

### Server: Bugfixes & Changes

- Enabled *Authorized Serial Account Protection* by default

- Enabled *Database Credentials Protection* by default

- Fixes for weapons/fists desync

- SQLite or MySQL no longer makes the server freeze if the connection is lost

- Goggles no longer stay after player was killed (thanks to **ArranTuna**)

- Fixed console input via pipe on Windows

- Added option "-u" to server command line to disable stdout buffering (useful for screenlog)

## Resources

- Added new special detections to *acpanel*

- Added anti-command spam to *freeroam* (thanks to **dutchman101**)

- Fixed vehicle kills not being displayed properly (thanks to **ArranTuna**)

- Fixed abusable glitch in /anim command in *freeroam* (thanks to **dutchman101**)

- Added graceful exitting to *webbrowser*

- Fixed run commands overwritng 'results' global variable in *runcode*

## Editor

- Disabled breathing sounds

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
