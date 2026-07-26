---
doc_id: "mta-wiki:13265"
title: "Client on Linux using Lutris Manual"
source_title: "Client on Linux using Lutris Manual"
source_url: "https://wiki.multitheftauto.com/wiki/Client_on_Linux_using_Lutris_Manual"
revision_id: 79863
language: "en"
categories: ["Support"]
generated_at: "2026-07-26T16:10:34.400977+00:00"
---

# Client on Linux using Lutris Manual

|  | Warning: Before reading this manual, it's advised to have read our main Client on Linux Manual . This manual for Lutris is a thing on the side, based on personal preference of individual Linux users. Both manuals can supplement eachother |
| --- | --- |
|  |  |

## Requirements

- Basic knowledge about the [Wine Prefix](https://linuxconfig.org/using-wine-prefixes)

- [Lutris](https://lutris.net/downloads/)

- Lutris Wine Runner: latest version of proton-ge 8.x

- A prefix with GTA:SA V1.0 installation (Lutris can be used)

- [MTA Installer](https://www.mtasa.com/)

- During this tutorial, make sure to only use 32-bit prefix for MTA:SA, or else you will run into a libcef.dll incompatibility issue and performance problems.

## Installing MTA

- On Lutris, Add a Game:

- Game Info -> Name: Multi Theft Auto

- Game Options -> Wine Prefix: *Same as the GTA:SA installation prefix*.

```
Make sure all prefixes for MTA/GTA are 64-bit, to avoid running into a plethora of issues.
```

- - Runner Options -> Wine Version: latest version of lutris 7.x   
 Note: if for any reason it doesn't work, try the latest confirmed working version: 7.2

- Runner Options -> Enable DXVK/VKD3D: Disabled

- On Lutris, click on Multi Theft Auto and on the bottom bar, click on the Wine popup menu and select Winetricks

- Select the default wineprefix -> Install a font -> Check Tahoma and Verdana

- On Lutris, click on Multi Theft Auto and on the bottom bar, click on the Wine popup menu and select Run EXE inside Wine prefix

- On the File Manager that appears, find and select the MTA Setup executable that you downloaded

- Run the setup

- Untick "Install DirectX" and "Dedicated server"

- Before finishing setup, make sure you untick Run MTA

- Open this folder in your MTA directory (eg. "{Wine Prefix path}/drive_c/Program Files (x86)/MTA San Andreas 1.5/MTA")

- Open your terminal emulator here, run   
 

```
cp libcef.dll chrome_elf.dll icudtl.dat natives_blob.bin v8_context_snapshot.bin snapshot_blob.bin CEF
```

   
 (issue workaround source is on [github](https://github.com/multitheftauto/mtasa-blue/issues/1000))

- On Lutris, right click Multi Theft Auto and select Configure

- Game Options -> Executable: Should point to "Multi Theft Auto.exe" inside the Wine Prefix path (eg. "{Wine Prefix path}/drive_c/Program Files (x86)/MTA San Andreas 1.5/Multi Theft Auto.exe")

- On Lutris, launch Multi Theft Auto

- You should be greeted with an "Error serial", but that's actually a good sign, continue to solve it

- In order to solve the "Error serial", [download and run the Linux Native MTA Server](https://wiki.multitheftauto.com/wiki/Server_Manual#Linux_installation)

- **After about a minute running the server**, close it

- On Lutris, launch Multi Theft Auto

- MTA should launch without any issues, as well as successfully connect to servers

## Updating MTA

Updating MTA through the client itself doesn't work. You have to manually download the new version of [MTA Installer](https://www.mtasa.com/), and install it by repeating Steps 2 and 3 on [Installing MTA](#Installing_MTA) section

## Tips

- This setup works with MTA 1.5.9 (tested)

- There are probably some Lutris Scripts available for installing MTA, but doing it manually should work better (tested)

- If you want you can ignore any Wine Mono and Wine Gecko installation prompts, as they are not needed for MTA (tested)

- Instead of using the Lutris one, the latest version of wine-tkg [[1]](https://github.com/Frogging-Family/wine-tkg-git/releases/) should work as well if you prefer.  
 If for some reason the latest version doesn't work, try out older versions from that page

- For audio streaming, installing "wmp10" using Winetricks from Lutris might help (untested)

- Make sure you also check [Client on Linux Manual](mta://getting-started/client-on-linux-manual.md) for more info

### Known issues

- MTA isn't starting (even with fonts installed)

- Try to start MTA:SA in a virtual desktop

Go to WineConfig, choose the tab "Graphics" and select "Emulate a virtual desktop".

- Try to delete your gta_sa.set file

which is located in the "GTA San Andreas User Files" folder, which can be found in your home directory.  
**(Remember to create a copy, if you're playing San Andreas in singleplayer)**

- Try to delete your MTA config file

which is: "MTA San Andreas 1.5/MTA/coreconfig.xml"  
**(Also remember to create a copy, if you don't want to lose your edited MTA configuration)**

- "libcef.dll" MTA crash upon joining servers, or during gameplay (when server uses CEF and your CEF web browser is enabled)

Check step 5 on [Installing MTA](#Installing_MTA) section

- MTA won't start on Ubuntu 12.04 LTS [Temporary fix is available [here](https://forum.mtasa.com/topic/36206-mta-13-wont-start-on-ubuntu-1204/#comment-366248). Although, just updating away from such an old version of Ubuntu is the recommended way to go] Also i reccomend using ZorinOS/LMDE/EndeavourOS instead of ubuntu.

- "SD #16 Error" when connecting to a server

- "No audio card detected" when launching either GTA:SA or MTA

- Using standard Full-screen mode on MTA might cause some occasional artifacts

- Enabling DXVK might not break GTA:SA, but it breaks MTA

- Using Linux brings a higher-than-usual chance for game crashes due to various reasons (sometimes to do with resources & mods on individual servers)

*** Making the mistake of using a 64-bit prefix may *specifically* result in:**

- "libcef.dll" incompatibility => game crash

- Even higher chance for instability, lag issues and game crashes

.. and much more

### Specific issues with workarounds

**Crash when connecting**  

Sometimes the audio-server makes problems (could be related to PulseAudio), in this case, you've to go to WineConfig and choose the tab Audio, then deselect "ALSA" and select "EsoundD". Save the settings and restart MTA.  
  

**Crash in basswma.dll module while streaming audio**  

Workaround: Install Windows Media Player 11  

Before carrying this out, [install Winetricks](https://wiki.winehq.org/Winetricks)

```
winetricks -q wmp11

If that doesnt solve the issue, try an older version:
winetricks -q wmp10
```

**Closing words**  

To avoid many of the roadblocks when it comes to Linux/Wine issues in general, just use 32-bit Prefix as suggested. However, if you still run into issues, you can inform yourself better about MTA's Linux/Mac support levels and background by joining the [MTA discord](https://discord.gg/mtasa) and going to #help-support channel, to specifically read information at this pinned message: [https://discord.com/channels/278474088903606273/278521065435824128/894932698269900830](https://discord.com/channels/278474088903606273/278521065435824128/894932698269900830)

We realize that the wiki pages & documentation regarding Linux, macOS support (such as: through Wine, Lutris, HeroicGamesLauncher etc) is far from perfect, and that the list of potential issues you can run into isn't complete. As the MTA discord linked post tries to explain, these platforms are supported on a best-effort basis (in a technical sense, not an user support sense) and even then you'll find others on the MTA discord that are Linux users & play MTA after performing some workarounds, that may be willing to help you. These people are also advised to add any known issue (and workaround for it) to the wiki documentations, so if that sounds like you then feel free to edit this page for instance, and help future users that find themselves in the same situation as you were. Linux/Wine just gives really obscure, hard to fix issues with MTA and other applications/games, including niche ones that individual users happen to resolve somehow.. that's the point.
