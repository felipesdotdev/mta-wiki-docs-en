---
doc_id: "mta-wiki:4908"
title: "Client on Linux Manual"
source_title: "Getting MTASADM to work with wine"
source_url: "https://wiki.multitheftauto.com/wiki/Getting_MTASADM_to_work_with_wine"
revision_id: 82640
language: "en"
categories: ["Needs_Checking", "Support"]
generated_at: "2026-07-26T16:15:30.890684+00:00"
---

# Client on Linux Manual

|  | This article needs checking. |
| --- | --- |
| Reason(s): MTA:SA support on Linux is on a best-effort basis, and you can run into a long list of issues. Also see "Known issues" paragraph |  |

|  | Warning: This page is for Linux players ONLY , for Windows go here . |
| --- | --- |
|  |  |

## Other Methods

These are related Client on Linux methods for other setups:

### Lutris

Lutris can be used instead for easier Prefix management, see
[Client on Linux using Lutris Manual](mta://getting-started/client-on-linux-using-lutris-manual.md)

### Bottles/Soda

Bottles can also be used in conjunction with the Soda runner, see
[Client on Linux using Bottles/Soda Manual](mta://getting-started/client-on-linux-using-bottles-soda-manual.md)

### Steam Deck

Steam Deck mobile device can also be used to play MTA, see
[Client on Steam Deck Manual](mta://getting-started/client-on-steam-deck-manual.md)

## Before you start

First of all, please ensure your computer fits the requirements needed.
Read the [Client Manual](mta://getting-started/client-manual.md) page for further informations, or join us on [Discord](https://mtasa.com/discord).

It is recommended to use **32-bit Wine prefix**. But if you do not want to install 32-bit libs, or your distro ships with enforced WoW64 Wine mode, use 64-bit Wine prefix instead, although 64-bit Wine prefix introduces some instability, bugs and potential performance issues, but it's still very playable.

### Requirements

The hardware requirements for Multi Theft Auto: San Andreas are the same as on Windows.
For software requirements, you need:

- Wine (get it on your package manager (synaptic, apt, pacman, yum, etc.); follow instructions [here](https://www.winehq.org/download/ubuntu) if you're using Ubuntu; (Install Wine Staging if you want better audio quality (experimental))

- Winetricks (same as wine, get it on your package manager, or follow instructions [here](https://wiki.winehq.org/Winetricks))

- **(for 32-bit wine bottle only)** 32-bit GPU mesa drivers for your GPU (for arch, use package lib32-mesa)

- **(for 32-bit wine bottle only)** 32-bit Audio drivers (for arch, follow instructions [here](https://wiki.archlinux.org/title/wine#Sound)

- TLS libraries (for arch, use packages gnutls and **(lib32-gnutls for 32-bit wine bottle only)**)

- MTA:SA version 1.6 or newer (1.6 contains many improvements for Wine)

- Windows fonts:

- tahoma.ttf

- tahomabd.ttf

- verdana.ttf

You can download them from following places:

- Get them on the Internet, e.g. [fontonic.com](http://fontonic.com/)

- Get the zip archive with the 3 fonts [here](https://drive.google.com/open?id=0B4SUSkTXjliXZnBXV2pEWkdTTms).

- Get them via your package manager (apt, pacman (ttf-tahoma and ttf-ms-fonts from AUR))

## Create new prefix

Firstly, we need to create a new prefix:

- Start Winetricks

- Select **Create new prefix**

- If you can, select **32-bit prefix**. If you did not installed 32-bit libraries, or you have enforced WoW64, create **64-bit prefix**.

- Write name of prefix, we will use **mtasa**

## Installing the game

(You can skip this if you installed the game via Steam or other supported Games Store)
Install the game from DVD or ISO into our prefix, by executing following command:

```
WINEPREFIX=~/.local/share/wineprefixes/mtasa wine /mnt/setup.exe
```

(Replace /mnt/setup.exe with path to installer's setup.exe)

Complete the installation as usual, you can keep installation path as is.  

Afterwards, download the MTA installer from [mtasa.com](http://www.mtasa.com), and execute it inside our prefix with following command:

```
WINEPREFIX=~/.local/share/wineprefixes/mtasa wine ~/Downloads/mtasa-1.6.exe
```

(As previously, change path to the installer)  

Keep the options as is, only change is required if installation path of GTA is different from default, in that case, browse the path to the game.

## Configuring prefix

Firstly, we need to assure that our prefix have required fonts, mentioned in Requirements part. If you installed those fonts via package manager or into your Linux system, Wine should be able to pick them up automatically.

If that doesn't work, manually install them in

```
~/.local/share/wineprefixes/mtasa/drive_c/windows/Fonts
```

If you installed Wine Staging, we can enable **Environmental Audio Extensions (EAX)**, which is experimental feature, although I didn't encountered any issues with it.
You can enable it as follows:

- Open Winetricks

- Select **mtasa prefix**

- Select **Run winecfg**

- Go to **Staging** tab

- Enable Environmental Audio Extensions (EAX)

### For 64-bit prefix

Normally for DirectX games, DirectX to OpenGL shim is used. Wine WoW64 have significant performance issues in games using OpenGL.
Because of this, it is recommended to install DXVK through WineTricks. In the past, DXVK did not worked with MTA, although, so far it works quite nicely, although it's less stable as on 32-bit bottle with internal DirectX to OpenGL shim.

- Open Winetricks

- Select **mtasa prefix**

- Select **Install a Windows DLL or component**

- Select **dxvk**

## Running the game

Once installed, double-clicking on the Desktop shortcut or menu item should work. If not, try in a terminal the following command:

```
WINEPREFIX=~/.local/share/wineprefixes/mtasa wine ~/.local/share/wineprefixes/mtasa/drive_c/Program\ Files/MTA\ San\ Andreas\ 1.6\Multi\ Theft\ Auto.exe
```

### Known issues

- MTA isn't starting (even with fonts installed)

- Try to start MTA:SA in a virtual desktop

Go to WineConfig, choose the tab "Graphics" and select "Emulate a virtual desktop".

- Try to delete your gta_sa.set file

which is located in the "GTA San Andreas User Files" folder, which can be found in your home directory.  
**(Remember to create a copy, if you're playing San Andreas in singleplayer)**

- Try to delete your MTA config file

which is: "MTA San Andreas 1.6/MTA/coreconfig.xml"  
**(Also remember to create a copy, if you don't want to lose your edited MTA configuration)**

- "SD #16 Error" when connecting to a server

- "No audio card detected" when launching either GTA:SA or MTA

- Using standard Full-screen mode on MTA might cause some occasional artifacts

- Enabling DXVK might not break GTA:SA, but it breaks MTA (NOTE: DXVK seems to work on latest versions of Wine, DXVK and MTA)

- Using Linux brings a higher-than-usual chance for game crashes due to various reasons (sometimes to do with resources & mods on individual servers)

- CEF crashes with some wine versions. Use [workaround](https://github.com/multitheftauto/mtasa-blue/issues/1000) for this issue

*** Making the mistake of using a 64-bit prefix may *specifically* result in:**

- "SD #16 Error" when connecting to a server

- "libcef.dll" MTA crash upon joining servers, or during gameplay (when server uses CEF and your CEF web browser is enabled)

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

**Special Detections (SD)**  

This was already described above in general terms, of possible issues if you're not using 32-bit prefix as is recommended. But for this "Specific issues" section we will go in-depth more regarding **SD #21** kick from AC that commonly affects Linux/Wine users:  

If you are using a 64-bit wine version/prefix you may have problems with [Special Detections](http://wiki.multitheftauto.com/wiki/Anti-cheat_guide#.3Cenablesd.3E.3C.2Fenablesd.3E). If the server you are trying to connect keeps showing something like [this](http://i.imgur.com/33T8a82.jpg), then you should make a [32 bit wine prefix](https://wiki.archlinux.org/title/Wine#WINEARCH) (or bottle).

```
export WINEARCH=win32 WINEPREFIX=~/.winegta
winecfg
```

Look at your Windows version and press OK to create the prefix. Now you have a 32-bit wine prefix on ~/.winegta.
Install GTA:SA and them MTA.
After this, MTA and GTA have been installed within ~/.winegta prefix which is a 32-bit wine environment.

**Note**: In some scenario's, while creating your 32-bit prefix, it may be needed to change Windows version on the bottom to Windows 7. But avoid it whenever possible.
  
  

**Serial Validation fails**  

On some Linux systems, MTA may fail the serial validation step during first startup. This workaround might work if your machine uses only NVMe storage devices.  

To check wether your system is affected, run:

```
ls -l /dev/disk/by-id
```

If the output doesn't contain any entry starting with "ata-" or "scsi-", then this might be the cause of serial validation problems for you.  

You can work around this issue by temporarily connecting any SATA-based storage device to your system. This includes:

- internal SATA HDDs/SSDs

- external USB hard drives that use USB–SATA bridge controllers

Once the device is connected, the system will expose the required ata-* or scsi-* identifiers. While the device is still connected, [start the MTA Server natively on Linux](https://wiki.multitheftauto.com/wiki/Server_Manual#Linux_installation) (not through Wine), then launch MTA client using your preferred way. The serial validation should now succeed.  

After successful validation, the SATA device usually no longer needs to remain connected unless the Wine prefix is recreated or MTA requires serial verification again.
  
  

**Font Artifacts**  

If you see weird fonts artifacts [like this](https://media.discordapp.net/attachments/278521065435824128/1000827089022373978/unknown.png) then you need to add a new DLL override to your prefix/bottle.

- Open **Wine configuration** for your prefix/bottle, go to the Libraries tab

- Click on the '**New override for library**:' dropdown and select '**d3dx9_42'**

- Click on '**Edit...'** and select '**Builtin (Wine)'** then 'OK'

Apply all the changes and you're good to go.  

(Make sure you have '**d3dx9_42'** installed in your prefix)

```
winetricks d3dx9_42
```

(NOTE: This does not work anymore, MTA stops due integrity check failure.)

**Closing words**  

To avoid many of the roadblocks when it comes to Linux/Wine issues in general, just use 32-bit Prefix as suggested. However, if you still run into issues, you can inform yourself better about MTA's Linux/Mac support levels and background by joining the [MTA discord](https://discord.gg/mtasa) and going to #help-support channel, to specifically read information at this pinned message: [https://discord.com/channels/278474088903606273/278521065435824128/894932698269900830](https://discord.com/channels/278474088903606273/278521065435824128/894932698269900830)

We realize that the wiki pages & documentation regarding Linux, macOS support (such as: through Wine, Lutris, PlayOnLinux, Parallels Desktop etc) is far from perfect, and that the list of potential issues you can run into isn't complete. As the MTA discord linked post tries to explain, these platforms are supported on a best-effort basis (in a technical sense, not an user support sense) and even then you'll find others on the MTA discord that are Linux users & play MTA after performing some workarounds, that may be willing to help you. These people are also advised to add any known issue (and workaround for it) to the wiki documentations, so if that sounds like you then feel free to edit this page for instance, and help future users that find themselves in the same situation as you were. Linux/Wine just gives really obscure, hard to fix issues with MTA and other applications/games, including niche ones that individual users happen to resolve somehow.. that's the point.

## See Also

- [nightly.mtasa.com](http://nightly.mtasa.com/) - For nightly builds.

- [https://bugs.mtasa.com/view.php?id=8895](https://bugs.mtasa.com/view.php?id=8895) - a bug report containing useful info for running MTA in Wine
