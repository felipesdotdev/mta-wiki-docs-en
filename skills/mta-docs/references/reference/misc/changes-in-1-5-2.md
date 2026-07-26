---
doc_id: "mta-wiki:8491"
title: "Changes in 1.5.2"
source_title: "Changes in 1.5.2"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.2"
revision_id: 75879
language: "en"
categories: ["Changelog"]
---

# Changes in 1.5.2

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

1.5.2 was released on January 24, 2016.

- Changelog on Mantis: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- Full changelog: [https://github.com/multitheftauto/mtasa-blue/commits/1.5.1?page=1](https://github.com/multitheftauto/mtasa-blue/commits/1.5.1?page=1)

## Main Additions / Changes

## Scripting

### Client

- Added [createSearchLight](mta://scripting/client/functions/createsearchlight.md), [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md), [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md), [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md), [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md), [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md), [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md), [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md), [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- Added [setWindowFlashing](mta://scripting/client/functions/setwindowflashing.md)

- Fixed position calculation in [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md) (thanks to tederis)

- Added UsingDepthBuffer flag to [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md)

### Server

- Added [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- Fixed *Player.outputChat* behaving incorrectly

- Added [onPlayerACInfo](mta://scripting/server/events/onplayeracinfo.md) and [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

### Shared (*Client & Server side*)

- OOP tweaks and fixes

- Fixed colon cutting the message printed by assert and error

- Fixed loadstring and load not accepting UTF-8 strings with BOM

- Improved error handling for function parameter parsing

- Changed *coroutine.resume* to output errors by default

- Added https support for [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

## Client

### Client: Additions

- None yet

### Client: Bugfixes & Changes

- Updated CEF (and underlying Chromium)

- Fixed player reconnecting under certain circumstances when downloading a file from an external webserver

- Fixed door/component desync on vehicle stream-in/out

- Fixed multiple major crashes

- Security fixes

## Server

### Server: Additions

- Added some Linux libraries to the MTA package to improve compatibility with old systems

- Added server verification logic

### Server: Bugfixes & Changes

- Fixed input cursor causing server freezes

- Fixed refreshResources sometimes crashing the server

- Fixed file conflicts when a resource name contains square brackets

- Fixed Linux server startup error message formatting

- Improved version checks

## Resources

- None yet

## Editor

- None yet

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
