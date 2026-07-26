---
doc_id: "mta-wiki:14563"
title: "Client on Linux using Bottles/Soda Manual"
source_title: "Client on Linux using Bottles/Soda Manual"
source_url: "https://wiki.multitheftauto.com/wiki/Client_on_Linux_using_Bottles/Soda_Manual"
revision_id: 82822
language: "en"
categories: []
---

# Client on Linux using Bottles/Soda Manual

Requirements

- A Linux distribution supporting Bottles/Soda (e.g. Linux Mint). This guide uses Bazzite which is based on Fedora

- Bottles with Soda runner (you can download from [Flathub](https://flathub.org/apps/com.usebottles.bottles))

- A copy of GTA:SA

- [MTA Installer .exe](https://www.multitheftauto.com/)

## Installing Bottles/Soda

- Install Bottles via your Distro package manager. For Bazzite, the "Discover App Store" provides the latest builds to install

- After installing, launch Bottles and let it do some initialization on first startup

- When it's loaded up, click on the plus icon on the top left corner to create a new Bottle

- Enter a name for the Bottle, this can be a generic name like "Gaming Stuff" since it won't be limited to just GTA/MTA

- Make sure to select "Gaming" option, the Runner should be:

- Choose "soda-9.0-1" (or a newer soda Runner if available)

- Click on "Create" and let the setup create the new environment, this can take a few minutes

- The Bottle should now appear in the list, click on it to open it

- Download the latest build of MTA:SA from the website, important note: Use the windows 10+ version, not the older win7/8.x one!

- After the installer got downloaded, click on the blue icon which says "Run Executable..." and select the MTA installer

- Navigate through the MTA installer until you reach the point where you have to locate the GTA:SA installation

- Now you need a copy of GTA:SA, in this case I downloaded mine from Steam. Right click GTA:SA in your library, go to Properties, Installed Files and select "Browse Files" which opens the file explorer

- Go back to the Bottles application, on top right side of window should be three vertical points as an icon, click on it and select "Browse Files" to open a new file explorer window with the Bottles drive_c directory

- Copy the GTA folder from Steam location to drive_c/Program Files (x86) folder

- After copying, go back to the MTA installer window, adjust the file path of the GTA installation to "C:\Program Files (x86)\Grand Theft Auto San Andreas\" or whatever your GTA installation is called

- Before completing the installation, uncheck the "Launch MTA" tickbox, we do NOT want to run MTA from the installer instance

- Inside your Bottles window, click on "+ Add Shortcuts..." and find the "Multi Theft Auto.exe", which should be located in "drive_c/Program Files (x86)/MTA San Andreas 1.6/"

- **You are good to go now**, just click on the play icon.

- You can also add MTA to your Bottles library via three dots icon so it looks like this:

Scroll down to [#Issues and solutions](#Issues_and_solutions) for additional resolutions to common problems.

## Manually updating MTA

- To install a newer version of MTA manually, for example nightly, simply download the installer executable from nightly website.

- Go into your Bottle where you previously installed GTA and MTA.

- Click on the blue button on top that says "Run executable..." and select the new MTA installer you just downloaded.

- Simply click through the MTA installer to the end (GTA path and settings will be taken from the installed version) and remove the check box which says "Run MTA:SA" at the end.

- Click on MTA:SA shortcut to run the newly installed version.

## Installing a second major version, for example 1.7 next to 1.6

- Before installing a new major version, go inside your Bottle and rename the already existing MTA installation shortcut from "Multi Theft Auto" to "Multi Theft Auto 1.6". Do the same for server shortcut if there is one.

- Download the 1.7 MTA installer and run it via the blue icon "Run executable...".

- Go through the installation setup as described above in "Manually updating MTA".

- After 1.7 got installed next to already existing 1.6 version, if the Bottle does not show a new shortcut for 1.7, add one manually. Rename the shortcut to "Multi Theft Auto 1.7" to avoid confusion.

## Issues and solutions

You might need to do all of these steps.

- MTA fails to start because of missing fonts (Verdana, Tahoma, etc...)

- Download the fonts verdana.ttf, tahoma.ttf, tahomabd.ttf and micross.ttf from the internet and put them in **"drive_c/windows/Fonts/"** folder

- [This section of the main Client on Linux manual](mta://getting-started/client-on-linux-manual.md) contains more information and download links

- Alternatively go to your bottle, scroll down to Dependencies and click on "allfonts" to install all fonts supplied by Windows.

- MTA starts and brings up main menu but the application window constantly flickers

- Try to navigate to Settings, Video tab and change Fullscreen mode to Standard

- The CEF component does not load (NOT crashing), for example joining FFS Gaming server, you see no login/register panel (CEF based)

- Go to your MTA installation folder, go to MTA sub folder: **"drive_c/Program Files (x86)/MTA San Andreas 1.6/MTA/"** and copy the following files to **CEF** folder inside that **MTA** folder:

- CEFLauncher.exe

- CEFLauncher_DLL.dll

- cefweb.dll

- chrome_100_percent.pak

- chrome_200_percent.pak

- chrome_elf.dll

- icudtl.dat

- libcef.dll

- resources.pak

- v8_context_snapshot.bin

- You did the previous step by moving CEF files manually and now installed a new version (nightly) of MTA and CEF completely crashes.

- Go to your MTA/CEF folder and delete the mentioned files above, then start MTA. If MTA reports an integrity failure upon start, run the MTA installer again.

- Certain unicode characters do not render properly in chatbox and on DX elements and fall back to square/box characters. (But they render correctly on ingame console window or CEGUI elements)

- The issue is still being investigated...

- DX fonts/texts are mashed together/cut off.

- This is an issue within Wine, see [https://bugs.winehq.org/show_bug.cgi?id=59018](https://bugs.winehq.org/show_bug.cgi?id=59018)

- MTA does not start after installing/updating, no splash screen is shown, the Wine console says: "wine: Call from 7BF6CB38 to unimplemented function KERNEL32.dll.CopyFile2, aborting"

- Change the runner to "caffe-9.7"

## Tweaks and tinkering

Inside your Bottle, you can change various settings for potential tweaks etc.
Recommended tweaks are: LatencyFlex, Discrete Graphics, Feral GameMode
