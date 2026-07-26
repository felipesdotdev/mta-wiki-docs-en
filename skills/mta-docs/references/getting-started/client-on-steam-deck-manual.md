---
doc_id: "mta-wiki:14393"
title: "Client on Steam Deck Manual"
source_title: "Client on Steam Deck Manual"
source_url: "https://wiki.multitheftauto.com/wiki/Client_on_Steam_Deck_Manual"
revision_id: 82483
language: "en"
categories: ["Support"]
---

# Client on Steam Deck Manual

| [[\|link=\|]] | Warning: This page was created with limited knowledge of running Multi Theft Auto on the Steam Deck. Further testing is needed and steps may change as more knowledge is gained. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Connecting a keyboard and mouse to your Steam Deck is recommended when following this guide. |
| --- | --- |
|  |  |

## Other Methods

A more simpler and straight forward way is using Bottles/Soda on Steam Deck, see
[Client on Linux using Bottles/Soda Manual](mta://getting-started/client-on-linux-using-bottles-soda-manual.md)

The instructions below can still be used on Steam Deck but require more fiddling around with Proton and the system.

## Prerequisites

- A Steam Deck with the default OS (SteamOS) installed

- A copy of GTA San Andreas, either through Steam or copied over into your SteamOS

- Multi Theft Auto installer (download latest Win10+ release [here](https://multitheftauto.com))

- Windows fonts (Download a ZIP archive with all three [here](https://drive.google.com/open?id=0B4SUSkTXjliXZnBXV2pEWkdTTms) and extract it):

- tahoma.ttf

- tahomabd.ttf

- verdana.ttf

## MTA installation

- Switch to desktop mode if not there already.

- Download the latest Multi Theft Auto version from the [official website](https://multitheftauto.com).

- Add the installer as a non-Steam game (open up the context menu and click "Add To Steam").

- Switch to game mode.

- Locate the installer in the non-Steam game section in your Steam library.

- Open the context menu and click "properties", then switch to the "compatibility tab". Here select the latest (non-experimental) version of Proton.

- Close properties and run the installer.

- Follow all the steps, it's advisable to not change the path to your MTA installation. Select (or type) your GTA San Andreas installation path when prompted.

### Locating your MTA installation

Proton creates a virtual filesystem for Windows. We need to locate the path it created for your MTA installation as we'll need it for the next steps.

- Switch to desktop mode.

- Navigate to 

```
/home/deck/.local/share/Steam/steamapps/compatdata/
```

- Locate the folder (these folders represent app IDs) that contains your installation. Either by sorting by newest or by opening them up and navigating to 

```
/home/deck/.local/share/Steam/steamapps/compatdata/<ID>/pfx/drive_c/Program Files (x86)/
```

 to verify that a folder for MTA (MTA San Andreas 1.6) exists.

- Note down this ID once found.

### Installing Windows fonts

- Copy the fonts you downloaded and put them in 

```
/home/deck/.local/share/Steam/steamapps/compatdata/<ID>/pfx/drive_c/windows/fonts
```

### Getting MTA to run

| [[{{{image}}}\|link=\|]] | Note: Testing has shown that it's advisable to have a PC with an existing MTA installation running during your first startup. This is similar to running MTA in a VM, as it will take on the serial from this PC which should prevent the "serial cannot be validated" error. |
| --- | --- |
|  |  |

You're nearly there. We're now going to swap the MTA installation executable with the MTA launcher itself in your existing non-Steam game setup.

- Switch to game mode.

- Navigate to your non-Steam game section in your Steam library and locate the installer from earlier.

- Open up properties and look for "target".

- Modify the existing target with the path to your MTA installation (make sure to keep the double quotes!). By default it would be as follows: 

```
"/home/deck/.local/share/Steam/steamapps/compatdata/<ID>/pfx/drive_c/Program Files (x86)/MTA San Andreas 1.6"
```

- Start Multi Theft Auto and enjoy! You may have to select your GTA San Andreas installation path once more.

## Troubleshooting

- Missing tahoma.ttf/verdana.ttf font error

- Download the fonts [here](https://drive.google.com/open?id=0B4SUSkTXjliXZnBXV2pEWkdTTms) and put them in 

```
/home/deck/.local/share/Steam/steamapps/compatdata/<ID>/pfx/drive_c/windows/fonts
```

- Flickering taskbar after MTA started (desktop mode)

- Workarround for now, go to settings -> video tab and change resolution to 1280x720 windowed (DO NOT USE FULLSCREEN MODE)

- MTA crashes when entering main menu after selecting fullscreen mode in video settings tab (D3D9.dll crash offset ED711)

- Manually revert this setting by going to 

```
/home/deck/.local/share/Steam/steamapps/compatdata/<ID>/pfx/drive_c/Program Files (x86)/MTA San Andreas 1.6/MTA/config
```

 and opening coreconfig.xml with KWrite application. Search for "display_fullscreen_style" and change the property from 0 to 1.

- There was a problem validating your serial

- Follow the guide over [here](https://updatesa.multitheftauto.com/sa/trouble/?tr=serial-validation) and setup the linux server on steamdeck

- Cannot start linux server on steamdeck due to missing libncurses5 file/lib

- Download the ncurses5-compat-libs [here](https://arch.alerque.com/x86_64/ncurses5-compat-libs-6.2-1-x86_64.pkg.tar.zst). After downloading, open terminal inside Downloads folder and run following commands:

```
sudo steamos-readonly disable
sudo pacman -U ncurses5-compat-libs-6.2-1-x86_64.pkg.tar.zst
sudo steamos-readonly enable
```

## See Also

- [nightly.mtasa.com](http://nightly.mtasa.com/) - For nightly builds.
