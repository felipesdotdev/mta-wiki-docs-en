---
doc_id: "mta-wiki:4757"
title: "MTA 0.5 Known Issues"
source_title: "GTA3:MTA 0.5 Known Issues"
source_url: "https://wiki.multitheftauto.com/wiki/GTA3%3AMTA_0.5_Known_Issues"
revision_id: 74148
language: "en"
categories: ["MTA_0.5", "Historical", "Vice_City", "GTA3"]
generated_at: "2026-07-26T16:15:04.442206+00:00"
---

# MTA 0.5 Known Issues

|  | Historical: This page is retained for historical reference. |
| --- | --- |
| This article applies to an older version of Multi Theft Auto for GTAIII and Vice City. The current release is [ 0.5r2 ]. The updated article for 0.5r2 can be found here . |  |

This applies to MTA 0.5 (both GTA3:MTA and MTA:VC). The known issues for MTA:SA 1.x can be found [here](mta://getting-started/known-issues-faq.md).

*Server operators: ensure you are running the [MTAServer Patch 1 Hotfix](http://forum.mtasa.com/viewtopic.php?f=44&t=27645). [Windows.](http://files.mtasa.com/apps/0.5/mta05_server_win32_patch1_hotfix.zip) [Linux](http://files.mtasa.com/apps/0.5/mta05_server_linux_patch1_hotfix.tar.gz)*

- **Linux servers have a default MOTD set.**

Change the URL or remove it before you first run the server.

- **Linux servers have a default admin password set.**

Change the password before you first run the server.

- **In-game MOTDs appear as nonsense.**

We noticed this during testing but it wasn't fixed. This may be fixed in a future release. In the meantime, server admins can disable the MOTD by changing your mtaserver.conf and use the rich MOTD instead.

- **Australian and German EXEs (and possibly others) may produce an "invalid executable" error when you try to start a game.**

As Australian and German EXEs don't work reliably with MTA, this shouldn't be a huge problem. Try to obtain a standard EXE. You can try **Talidan'**s [invalid executable patcher](http://forum.mtasa.com/viewtopic.php?f=50&t=12180).

- **The in-game help marker says the game is MTA 0.4, when it clearly is MTA 0.5.**

This help marker was removed in [MTA 0.5r2.](http://forum.mtasa.com/viewtopic.php?f=31&t=31692)

- **Sometimes the URL of the Rich MOTD is appended to the server name when it appears in the client.**

This was fixed in Server Patch 1. It was caused by server names greater than 49 characters in length. If you are not using the patch, you must keep the server name under this limit.

- **The server's memory usage increases very quickly.**

This was fixed in Server Patch 1. It was caused by a memory leak.

- **Crash when MTA:VC DM is loading.**

We're not sure what causes this, but we know that about 60% of these crashes can be fixed by upgrading to Vice City 1.1. [Here's](http://updates.rockstargames.com/patches/vicecity/vicepatch_11.zip) the 1.1 patch download. If you're already using 1.1, try the next issue's solution.

- **Crash when either GTA3 or Vice City are loading.**

Make sure you run GTA3 or Vice City at least once in single player without MTA before actually running it with MTA.

- **Freeze when client tries to display dialog asking for game path.**

There have been a couple of occurrence of this, and we'd be interested to see why this is. You can avoid it by manually setting the path in the mta.ini in the Multi Theft Auto directory.

For Vice City, your mta.ini should contain (replace the path if necessary):

```
[Game-VC]
Version=0
Location=C:\Program Files\Rockstar Games\Grand Theft Auto Vice City\gta-vc.exe
```

For GTA3:MTA, your mta.ini should contain (replace the path if necessary):

```
[Game-GTA3]
Version=1
Location=C:\Program Files\Rockstar Games\GTAIII\gta3.exe
```

- **Crash on client startup.**

This is likely caused by the client failing to download the welcome message, since it is no longer being hosted. Fix this by adding "DontGetLatest=1" on the second line of your "mta.ini" in your Multi Theft Auto folder (under "[Main]"). Alternatively, try creating a blank file called "mtaclientwelcome.dat" in your MTA folder - this is probably only relevant if this is the first time you've run the MTA 0.5 client. Change the following value in mta.ini.

```
DontGetLatest=1
```

- **XFire crashes game during loading.**

Both XFire and MTA use similar methods for integrating themselves into the game. We've contacted XFire to offer our support for them in implementing support for MTA, but they haven't responded. If you wish to use XFire in MTA, contact XFire. In the meantime, disable XFire before you play.

- **MTA claims "Suspected Trainer Usage."**

Try closing every other open window first. If that doesn't work, try reinstalling MTA 0.5. It has also been reported that changing game version from 1.0 to 1.1 (for Vice City) can fix this, though we're not sure why.  

Further update: All the error reports that have come in about this are using Vice City 1.0. Try updating to [1.1](http://updates.rockstargames.com/patches/vicecity/vicepatch_11.zip).

Update: It has been reported that "Kaspersky Anti Hacker" can set off this error. We advise that you close "Kaspersky Anti Hacker" if you wish to play MTA 0.5.

- **If you try to spawn as a Crusader twice, you get disconnected for trainer usage.**

Fixed in [0.5r2.](http://forum.mtasa.com/viewtopic.php?f=31&t=31692)

- **You join a server and are told you are banned, even though you aren't in the ban list.**

The cause of this is unknown. You may be banned by a over-general ban in the server's ban list.

- **In MTA:VC Stunt, RC vehicles can appear locked when you try to enter them.**

This should be fixable by exiting Vice City, and starting the game again. Also fixed in [0.5r2](http://forum.mtasa.com/viewtopic.php?f=31&t=31692).

- **GTA3:MTA Shoreside Vale: Two players and two vehicles appear on the character select screen, followed shortly by a crash.**

Fixed in [0.5r2.](http://forum.mtasa.com/viewtopic.php?f=31&t=31692)

- **Attempting to connect to a server with Admin enabled and Admin+ disabled causes the server to crash when trying to use Admin+.**

This was fixed in Server Patch 1.

- **MTA:mA times out as soon as you connect to a server.**

This was fixed in Server Patch 1. It was caused by a bug in mIRC. Scripts sending multiple messages to a player upon joining the server can also cause this. Limit your scripts if this occurs. You can also use [Aeron](https://forum.mtasa.com/profile/470-aeron/)'s possible fix, located [here](https://forum.mtasa.com/topic/9458-mtama-flood-timeout-bug/#comment-127874).

- **MTA:VC (either map) crashes when you try to get on a bike as passenger when it has no driver.**

The cause of this is still under investigation.

- **Your server doesn't appear in the server list, or appears as "unscanned".**

This isn't an issue, but ensure that you have the correct port open for ASE to query through. This should be your server port plus 123. For example, with the default port of 2003, port 2126 should be open. This port is UDP.  

**NOTE**: The All-Seeing Eye server browser is no longer operational, but an external server browser is bundled with the [MTA 0.5 repack](http://files.mtasa.com/apps/0.5/mta05_full_installer_repack.exe). You still must forward the proper port as described for your server to show up on Game-Monitor.

- **You receive the error "ERROR: The ServerName, ServerPort, GameMap, GameHour, GameMins, Weather and BannedFile MUST be specified in the configuration file" when you run your server, and all fields are filled in.**

*Only affects Server Patch 1 Hotfix*  

Ensure that your server name is 49 characters or less. This is a misleading error. This may be fixed in a future release.

- **Client crashes when you join a server.**

This crash may be caused by the client trying to download the rich text MOTD specified by the server and failing (e.g. the site its trying to get it from is down, or the URL is invalid). If this happens, the client will crash. This may be fixed in the next client release.

- **You have quite a few files on your computer called MTAChat.txt.**

MTAChat.txt, as you probably guessed, stores a chat log. This feature was added at the last moment and not properly tested. Consequently, this problem has occurred. This is probably due to how the client has been launched (the start path determines where it saves the chat, not the install path). Don't worry about it, really... this may be fixed or disabled in the next client version. In the meantime, feel free to delete any files you don't want.

- **You receive "System Error &H80070583 (-2147023485)" (or similar) when running the Server Config Tool, or when clicking "Setup Server" in the client.**

This can be fixed by deleting the file called "MTAServerConfigTool.exe.manifest" in your Multi Theft Auto folder.

- **Upon hitting "Start Game" the client informs you your client is modified.**

This is an error with the way we temporarily replace some of the games files. When you install take a back up of both weapon.dat and weapon.mta from the /data/ directory in your Grand Theft Auto folder and put them somewhere safe. If you get this error close the client, REPLACE both files and retry.

- **An error appears that begins with "<font face="Arial" size=2>".**

This meant that an error had occurred, but the error reporter system was overloaded and couldn't send the error report. The error reporter system is no longer functional, so this may continue to occur. Just click the button and ignore it.

- **When playing GTA3 you receive an "Invalid Executable" error.**

This is probably because you are using GTA3 version 1.0 instead of 1.1. You can get the GTA3 1.1 patch [here](http://updates.rockstargames.com/patches/grandtheftauto3/GTA3patch1.1.zip). If this doesn't work, or you already have GTA3 1.1, make sure you have the USA/UK EXE; you can try **Talidan'**s [invalid executable patcher](http://forum.mtasa.com/viewtopic.php?f=50&t=12180). Failing that, try to obtain one elsewhere.

- **Your virus scanner informs you that the Multi Theft Auto 0.5 executable is a virus or malware.**

MTA does **not** contain any viruses, malware, adware or spyware. If your virus scanner informs you that it is infected, either you have a virus on your computer that is infecting your files, or one of our mirrors has been infected with a virus, or your virus scanner is making a mistake. McAfee has been known to make this mistake. We've informed Norton and McAfee of this, but they've yet to fix it. In the meantime, disable your virus scanner while playing. Also, ensure you only download from the Multi Theft Auto or Project Redivivus websites. Also be aware that in later years, a common, known false positive has been triggered by anti-malware scanners regarding the MTA 0.5 client executable and its installer. This is due to the way the internal code was protected from disassembly with the use of packing software and obfuscation. [This link](http://files.mtasa.com/apps/0.5/mta05_full_installer_repack.exe) is hosted by our webhost. Use this if you doubt the validity of your copy of MTA.

- **You get a crash at the address 652F30 when starting the game.**

This is caused by having the incorrect GXT file. To fix this, copy all the GXT files from the Grand Theft Auto Vice City\TEXT folder except the "american.gxt" into the Grand Theft Auto Vice City\MTA folder. You should also ensure your game language is set to English.

- **I cannot speak in the game at all, or users do not see what I am saying.**

Try adding MTA as an exception in Data Execution Prevention. Also, when running MTA, make sure you run it as an administrator. Some users have also reported restarting the client a few times or restarting their computer may help, although it is unknown why.

- **I've heard there is a MTA 0.5 Server Exploit Bug. Is this true?**

Yes. The bug involves an admin exploit that can be used by a malicious user to gain access to the "Set MOTD" administration command, that is used to modify the "motd.txt" (Message Of The Day) file. The exploit can then be used to crash the dedicated server. The affected platform is Microsoft Windows. The bug still exists on all other platforms, but is currently not exploitable. We strongly recommend anyone running a dedicated server to apply the temporary fix. To fix this exploit, the "motd.txt" file, located in the server directory, will have to be set to read-only. Deleting motd.txt will not fix the problem. Please follow the steps for your server platform. This may be fixed by default in a future release.  

  

**Microsoft Windows**  

Change the "motd.txt" file attributes to Read-only.

1. Open up Windows Explorer and navigate to your server directory.  

2. Right click on "motd.txt" and select Properties.  

3. Under Attributes, make sure the Read-only box is ticked 4. Click OK.  

  

***nix Platforms**
Chmod your "motd.txt" file to 444, read-only mode.

1. Cd "/path/to/your/server/directory".  

2. Chmod 444 "motd.txt".

- **I am using Windows Vista or Windows 7. Do I need to do anything special?**

Some users have experienced issues under Windows Vista and Windows 7 when trying to run MTA, however, there are some fixes! Make sure to add MTA as an exception in Data Execution Prevention. Also, when running MTA, make sure you run it as an administrator only.

- **When running Windows Vista or 7 with the MTA 0.5 Repack, you are unable to connect to a server in MTAClient after pressing "Connect" in MTABrowser.**

Run MTABrowser.exe as an Administrator: Right-Click -> "Run As Administrator".

- **When using the MTA 0.5 repack, the server list appears twice, or only shows some of the full list.**

Don't press the Refresh button too quickly. The cause of this is not yet known.

- **Your client times out as soon as you connect to a server. Players all time out when they connect to your server.**

This has been an unknown problem for quite some time now, but it seems it is caused not by MTA or the MTAServer but by MTA:mA, or more specifically scripts running on it. If the scripts send multiple messages to the player when they join it is highly likely to time them out. This results in nobody being able to play. This can also be caused by servers using excessively long names.

For now a fix is available for MTA:mA [here](http://forum.mtasa.com/viewtopic.php?p=181919#181919) (hopefully GRS will also be updated soon).

Please follow **Aeron'**s instructions regarding its use.

A big thank-you to **Mike** for discovering the cause of this problem and **Aeron** for getting a fix out so quickly.
