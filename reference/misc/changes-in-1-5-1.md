---
doc_id: "mta-wiki:8411"
title: "Changes in 1.5.1"
source_title: "Changes in 1.5.1"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.1"
revision_id: 75880
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:12:09.180917+00:00"
---

# Changes in 1.5.1

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

1.5.1 was released on November 5, 2015.

- Changelog on Mantis: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- Full changelog: [https://github.com/multitheftauto/mtasa-blue/commits/1.5.0?page=1](https://github.com/multitheftauto/mtasa-blue/commits/1.5.0?page=1)

## Main Additions / Changes

- Fixed shotgun bullet sync

- Fixed minor Windows 10 compatibility issues

- Fixed a bunch of crashes

- Introduced a [new web scheme](mta://reference/misc/local-scheme-handler.md) and deprecated the old mtalocal://

- Removed dependency on DirectPlay

- Updated dependencies (e.g. CEF and Google Breakpad)

- Added a few autofixes

- Code cleanups

- Sped up client disconnect

- Added resumable downloads to auto-updater

- Fixed text in browsers not being selectable

- Improved CEF handling in the event of missing files

- Added file verification for local CEF files

- Added ability to add more ASE master servers to announce to

- Fixed warning message when Lua file is 0 bytes

- Fixed mtasa:// links not working correctly if MTA is already running

- Fixed team members not being fully synced clientside under certain circumstances

- Fixed Linux server basic backup missing some files

- Added option to skip server termination during update

- Changed requestBrowserDomains to display the cursor while GUI is open

- Fixed DLL path issues on some computers

- Fixed loading spinner overlaying itself sometimes

- Fixed a major memory leak

- Improved CEF debugging capabilities (see [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md))

## Scripting

### Scripting: New functions

#### Client

- [getBrowserSource](mta://scripting/client/functions/getbrowsersource.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md)

- [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md)

- [getBrowserVolume](mta://scripting/client/functions/getbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

#### Server

- [fileGetPath](mta://scripting/shared/functions/filegetpath.md)

#### Shared (*Client & Server side*)

### Scripting: New Events

#### Client

- None yet

#### Server

- None yet

### Scripting: Changes, Bugfixes and Additions

- Added *passwordType* for [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

## Client

### Client: Additions

- None yet

### Client: Bugfixes & Changes

- Added DDS support to dxCreateTexture

## Server

### Server: Additions

- None yet

### Server: Bugfixes & Changes

- Added callback to [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md)

- Fixed a few OOP issues

- Fixed createMarker triggering onMarkerHit

- Fixed moving objects being able to move frozen players (thanks to eeew2 for the patch)

## Resources

- None yet

## Editor

- None yet

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
