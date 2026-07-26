---
doc_id: "mta-wiki:8164"
title: "Changes in 1.5"
source_title: "Changes in 1.5"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5"
revision_id: 75881
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:12:06.084993+00:00"
---

# Changes in 1.5

1.5 was released on July 15, 2015.

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

- Added a built-in web browser into MTA (*CEF*) which can be controlled by scripts using a new [browser](mta://reference/misc/element-browser.md) element.

- Added light functions

## Scripting

### Scripting: New functions

#### Client

- [createBrowser](mta://scripting/client/functions/createbrowser.md)

- [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md)

- [focusBrowser](mta://scripting/client/functions/focusbrowser.md)

- [isBrowserFocused](mta://scripting/client/functions/isbrowserfocused.md)

- [getBrowserProperty](mta://scripting/client/functions/getbrowserproperty.md)

- [getBrowserTitle](mta://scripting/client/functions/getbrowsertitle.md)

- [getBrowserURL](mta://scripting/client/functions/getbrowserurl.md)

- [injectBrowserMouseDown](mta://scripting/client/functions/injectbrowsermousedown.md)

- [injectBrowserMouseMove](mta://scripting/client/functions/injectbrowsermousemove.md)

- [injectBrowserMouseUp](mta://scripting/client/functions/injectbrowsermouseup.md)

- [injectBrowserMouseWheel](mta://scripting/client/functions/injectbrowsermousewheel.md)

- [isBrowserLoading](mta://scripting/client/functions/isbrowserloading.md)

- [isBrowserDomainBlocked](mta://scripting/client/functions/isbrowserdomainblocked.md)

- [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md)

- [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md)

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [createLight](mta://scripting/client/functions/createlight.md)

- [getLightType](mta://scripting/client/functions/getlighttype.md)

- [getLightRadius](mta://scripting/client/functions/getlightradius.md)

- [getLightColor](mta://scripting/client/functions/getlightcolor.md)

- [getLightDirection](mta://scripting/client/functions/getlightdirection.md)

- [setLightRadius](mta://scripting/client/functions/setlightradius.md)

- [setLightColor](mta://scripting/client/functions/setlightcolor.md)

- [setLightDirection](mta://scripting/client/functions/setlightdirection.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md)

- [getPedOccupiedVehicleSeat](mta://scripting/shared/functions/getpedoccupiedvehicleseat.md)

- [getCameraShakeLevel](mta://scripting/client/functions/getcamerashakelevel.md)

- [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md)

#### Server

- None yet

#### Shared (*Client & Server side*)

- None yet

### Scripting: New Events

#### Client

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserWhistelistChange](https://wiki.multitheftauto.com/index.php?title=OnClientBrowserWhistelistChange&action=edit&redlink=1)

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

#### Server

- [onPlayerNetworkStatus](mta://scripting/server/events/onplayernetworkstatus.md)

### Scripting: Changes, Bugfixes and Additions

- Added *throttled* parameter to [playSound](mta://scripting/client/functions/playsound.md) and [playSound3D](mta://scripting/client/functions/playsound3d.md)

- Added resource meta option <download_priority_group> to allow certain client resources to download and start earlier or later than other resources when a player first connects to a server.

- Added number of simultaneous render targets capability to [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md).

- Added an option to [addAccount](mta://scripting/server/functions/addaccount.md) to check for case insensitive name clashes.

## Client

### Client: Additions

- Enabled low fragmentation heap for XP to reduce memory allocation problems.

- Added automatic TXD resizing for 32 bit OS users to help fix low memory crashes.

- Added quality argument to dxCreateFont.

- Added FOV setting in the Video tab.

- Added support for multiple render targets in shaders.

- Adds the ability to complete nicknames in the chatbox when the tab key is pressed.

- Synced server side peds weapons with clients.

- Added fix for bullet sync not applying damage to the local player during network interruptions by applying remote calculated damage.

### Client: Bugfixes & Changes

- Moved client log and config files to MTA\log and MTA\config

- Removed BASS error messages for players

- Tweaked streaming memory size calculation

## Server

### Server: Additions

- Added server shutdown disconnect message

### Server: Bugfixes & Changes

- Set 64 bit modules directory to "x64/modules"

- Fixed server ignoring module initialization failure

- Fixed [getAccountData](mta://scripting/server/functions/getaccountdata.md) leaking memory

- Fixed [removeBan](mta://scripting/server/functions/removeban.md) crashing the server under certain circumstances

- Fixed HTTP stats being wrong sometimes

- Fixed sync issues when destroying a vehicle while exitting

- Added reload to the default start-up list.

## Resources

- None yet

## Editor

- None yet

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and GitHub repositories:*

- [MTA: SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA: SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
