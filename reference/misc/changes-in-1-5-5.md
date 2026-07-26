---
doc_id: "mta-wiki:9628"
title: "Changes in 1.5.5"
source_title: "Changes in 1.5.5"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.5"
revision_id: 75876
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:12:31.710541+00:00"
---

# Changes in 1.5.5

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

1.5.5 was released on October 7, 2017.

- Changelog on Mantis: [https://bugs.mtasa.com/changelog_page.php](https://bugs.mtasa.com/changelog_page.php)

- Full changelog: [https://github.com/multitheftauto/mtasa-blue/commits/master?page=1](https://github.com/multitheftauto/mtasa-blue/commits/master?page=1)

## Main Additions / Changes

- Fixed a couple of crashes

- Updated dependencies

- Upgraded build tools and migrated to a Docker-based environment (now, we have support for VS2017 and GCC-6)

- Code cleanups

## Scripting

### Client

- Return vectors for vehicles component funcs (#9507)

- Made GUI-functions accept vectors

- Added [guiGetCursorType](mta://scripting/client/functions/guigetcursortype.md)

- Added *player* element to [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- Added *soundEnable* parameter to [createEffect](mta://scripting/client/functions/createeffect.md)

- Added [setVehicleModelExhaustFumesPosition](mta://scripting/client/functions/setvehiclemodelexhaustfumesposition.md) and [getVehicleModelExhaustFumesPosition](mta://scripting/client/functions/getvehiclemodelexhaustfumesposition.md)

### Server

- Added [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md), [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md) (client-only before)

- Added [isResourceArchived](mta://scripting/server/functions/isresourcearchived.md)

### Shared (*Client & Server side*)

- Added [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- Limit range in [setRainLevel](mta://scripting/shared/functions/setrainlevel.md)

- Extended [fetchRemote](mta://scripting/shared/functions/fetchremote.md) by request method, request headers, response headers, authentication, redirection and form fields

- Added RGB parameters to [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)/[onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

- Deprecated *setControlState*/*getControlState* in favour of [setPedControlState](mta://scripting/client/functions/setpedcontrolstate.md)/[getPedControlState](mta://scripting/client/functions/getpedcontrolstate.md)

- Added logging a warning when some functions are used on non-joined players (e.g. when called from [onPlayerConnect](mta://scripting/server/events/onplayerconnect.md))

- Fixed [coroutine.resume](mta://scripting/shared/functions/coroutine-resume.md) returning only the first argument

## Client

### Client: Additions

- Added 'localhost' to the hardcoded CEF whitelist

- Enabled [setPedStat](mta://scripting/shared/functions/setpedstat.md) for client side peds

- Added black outline option for chat text

- Added support for more gta_sa.exe variants

### Client: Bugfixes & Changes

- Fixed [getHeliBladeCollisionsEnabled](mta://scripting/client/functions/gethelibladecollisionsenabled.md) accepting incorrect arguments

- Fixed effect sounds playing at the wrong position (thanks to **ZRec**)

- Fixed swapped color channels in browsers on Intel integrated graphics

- Changed camera mode used for vehicle targets (for [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md))

- Fixed [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md) not properly working with melee

- Tweaked layout of chatbox settings

- Added chatbox positioning settings

- Fixed warpPedIntoVehicle during freefall preserves falling animation (#9381)

- Fixed some tasks not being cleared if ped is warped to passenger seat

- Fixed water jump animation remaining after warp

- Fixed radio name not always showing

- Improved disconnect time duration text

- Improved client connecting through firewalls

- Improved netcode

- Fixed FOV setting not updating

- Fixed spectate camera movement malfunctioning with vehicles with adjustable property (#5306)

- Fixed crash when removing child elements during events

- Fixed famous crash at offset 0x003F18CF

- Updated CEF

- Fixed aircraft engine sounds being missing sometimes

- Fixed vehicle gear sounds being broken while sitting as passenger (#9681)

- Fixed memory leak and crash in password functions

- Fixed a new crouchbug variant

- Added some missing translations (thanks to **Sergeanur**)

## Server

### Server: Additions

- Added password append option to *authserial* command

### Server: Bugfixes & Changes

- Hide account passwords from logs when using the /addaccount command

- Censored [onClientConsole](mta://scripting/client/events/onclientconsole.md) for login command

## Shared

### Shared: Bugfixes & Changes

- Migrated from OpenSSL to mbedtls

- Initial work on macOS server support

## Resources

- Updated *ipb* resource to 0.3 (includes code cleanups, tweaked GUI layout and client performance stats)

- Modernised *play* gamemode

- Fixed fast-flying glitch with hydra/hunter/jetpack on custom gravity (freeroam)

- Added support for hex colors to killmessages (thanks to **AboShanab**)

- Tweaked realdriveby a lot (thanks to **emre1702**)

- Tweaked admin report system (thanks to **Dezash**)

- Fixed warping to interiors on foot (freeroam)

- Added support for hex colors to joinquit

- Added support for blowing off heads (headshot)

- Fixed admin bugs: spectating players in another int/dimension, 'Ban serial/IP' GUI polished (admin)

- Optimized the Freeroam codebase to improve performance and usage & fixed various bugs in the process (freeroam)

- Added anti-bothering features to freeroam panel ('disable warp' & 'disable knifing', anti-ram vehicle ghostmode)

- Fixed player being stuck sometimes when entering interior (interiors)

## Editor

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
