---
doc_id: "mta-wiki:7352"
title: "Famous crash offsets and their meaning"
source_title: "Famous crash offsets and their meaning"
source_url: "https://wiki.multitheftauto.com/wiki/Famous_crash_offsets_and_their_meaning"
revision_id: 81535
language: "en"
categories: ["Development", "Support"]
generated_at: "2026-07-26T16:15:00.438696+00:00"
---

# Famous crash offsets and their meaning

This wiki page contains the reason for many well-known MTA crashes that you may experience. Use CTRL + F and search for your Crash Offset to find the relevant entry.

Example crash dialog info:

```
Version = 1.5.6-release-14664.0.000
Time = Mon Oct  8 12:20:00 2018
Module = C:\Program Files (x86)\Rockstar Games\GTA San Andreas\gta_sa.exe
Code = 0xC0000005
Offset = 0x003C91CC

EAX=0F77A3C8  EBX=0F77A3B8  ECX=0177FAA0  EDX=00139700  ESI=00000000
EDI=00000001  EBP=0177FC50  ESP=0177FA80  EIP=007C91CC  FLG=00210202
CS=0023   DS=002B  SS=002B  ES=002B   FS=0053  GS=002B
```

(Note: always use the "Offset" value from the crash dialog to identify your crash and match it up with those listed on this wiki page)

**Most MTA crashes are caused by something that the user is able to resolve because it depends on their system, choice of server or game mods.**
This page seeks to be helpful for the aforementioned reason; you'll know where to look for when you get a certain type of crash.

For further advice on resolving issues, scroll down to the bottom of this page.

## Module = gta_sa.exe or proxy_sa.exe

| Offset(s) | Meaning |
| --- | --- |
| 0x00134134 | Bad model or corrupted GTA3.img. Use unmodded GTA install to check, or incase of server mods, ask server owner to identify and replace the corrupt mod. Note for server owners and modellers: if you open the crash dump (.dmp) as text with notepad and search for keyword `CEntity_GetBoundRect - No collision for model` you can often identify the bad model ID. |
| 0x00348CF4 | Caused by s0beit d3d9.dll |
| 0x003F0C37 0x003F0BF7 | Bad vehicle model. Use unmodded GTA install to check, or incase of server mods, ask server owner to identify and replace the corrupt mod. |
| 0x003C91CC 0x003C920C | Out of video memory. This can happen on servers with unoptimized mods and (faulty) scripts that abuse video memory, or even when you have a powerful graphics card in case the stuff on a server is extremely unoptimized so that it starts hitting GTA limits. If you have a powerful graphics card and more players suffer from this crash type, inform the server owner of this problem as it probably means their scripters & designers don't know what they are doing. More information is available at these forum links: here and here (example case) |
| 0x00357DEC | Out of video memory (probably). |
| 0x003F5A3A | Memory crash, usually happens on heavily unoptimized servers. It can be a result of either out of video memory or reaching technical limits of RAM usage, but more often a combination of both.. hence it's put as "heavily unoptimized servers". Contact the server owner and ask for optimization, or find other servers to play on. |
| 0x004A1ED4 | Out of system memory (RAM) |
| 0x011630F8 0x011630FE 0x01162FE3 0x011630F2 | This crash is a result of problems with collision models. It might be due to unoptimized collisions that your PC (or MTA's technical limits, due to bad server mods) cannot handle, or due to corrupt collision models. We still don't know a lot about all of the circumstances related to this crash. Our first advise would be to ensure that your GTA is unmodded, and otherwise to ask server owner to identify and resolve issues with bad/unoptimized collision models. |
| 0x00137D6E | Out of system memory (RAM). This co-incides with loading collisions; the risk to get this crash is high when joining a mod-heavy server with a weak PC and small amount of memory. To resolve this crash, mind the servers you're playing on (optimization) or get a faster PC. Sub-type of "Running out of memory": most often a direct result of running out of address space, so upgrading to 64-bit Windows installation might solve it |
| 0x0014F406 | Possibly "Running out of memory": a direct result of running out of address space, so upgrading to 64-bit Windows installation might solve it. |
| 0x00171A10 | Sometimes when joining a server, maybe related to bad server mods. |
| 0x000C9F98 | Possibly bad skin model or texture (clothes mods for multi-clump skins such as CJ). Use unmodded GTA install to check or incase of server mods, ask server owner to identify and disable mods on such skins, or any resource manipulating clothes or ped accesoires. |
| 0x00349B7B | Bad skin model. Use unmodded GTA install to check or incase of server mods, ask server owner to identify and replace the corrupt skin mod. Information for modellers & server owners: corruption in the anim hierarchy in ped's skin DFF or bones configuration |
| 0x00165096 | Bad model (containing a corrupt collision model). Use unmodded GTA install to check or incase of server mods, ask server owner to identify and replace the corrupt mod. Information for modellers & server owners: corruption in one or multiple col spheres (or their radius) within the DFF model. |
| 0x001D6E6A | Either out of video memory, or bad model/texture. Information for modellers & server owners: in case the culprit is a model, then corruption is in "prelit" (Night colors) structure of the model. Ask your modeller to recreate prelit data. |
| 0x000DFE92 0x000DFF90 | Bad sound mods or faulty audio driver/device. Use unmodded GTA install to check, or update your audio drivers. The problem is often known to be entirely missing or emptied/corrupted audio files (such as in \Rockstar Games\GTA San Andreas\audio > SFX or other subfolder), so you may alternatively be able to restore a targeted backup. Do not use 'compressed' GTA re-packs for this reason of cut-out audio files. |
| 0x000CFCD6 | Allocation failure as a result of (re-)connecting to servers after a lengthy playing session on a server with bad practise in their scripts (abusing RAM and anim functions). This crash may be 'fixed' (averted) by MTA in future, we're working on it! It's related to anims in memory and clearing them. |
| 0x00771848 | Crash because of issue with GTA data files (MTA fails to open them which could mean they are corrupted/modded & incompatible or missing) Use unmodded GTA install to check |
| 0x001B6B2F | Crash because of issue with DATA\DEFAULT.DAT or DATA\CARCOLS.DAT file in your GTA installation folder (may be missing or modded/corrupted). Use unmodded GTA install to check |
| 0x003EC9DA | Crash possibly because of issue with ANIM\PED.IFP file in your GTA installation folder (may be missing or modded/corrupted). Use unmodded GTA install to check |
| 0x003F18CF 0x003F190F | Bad model. Use unmodded GTA install to check or in case of server mods, ask server owner to identify and replace the corrupt mod. This crash has been averted (fixed by MTA), but due to technical limitations will still occur for Windows XP users. Information for modellers & server owners: due to the nature of corruption, the model introduces a risk to crash, it could happen at any given moment while nearby. |
| 0x0019BD39 | Bad model. Use unmodded GTA install to check or in case of server mods, ask server owner to identify and replace the corrupt mod. This crash usually occurs when you fire a weapon while the corrupt model is streamed in (physically nearby). |
| 0x000C9691 | Bad or missing vehicle model. This usually happens when you deleted a model from your GTA3.img without restoring the original or putting another model in its place. Or when the DFF isn't a valid model file at all. Restore GTA3.img or use unmodded GTA install to check, and if that doesn't work then ask server owner to identify and replace the corrupt mod, since it can also still be a bad model (or a dodgy script, that, tell them this: deals with vehicle types, variants, upgrades etc, in an improper way) |
| 0x0000F67C 0x0000F663 | Custom models which are not working with volumetric shadows. Fix models or disable volumetric shadows in Settings->Video. |
| 0x00423FD0 | Bad GTA mods or corrupted GTA3.img. Re-install GTA (with a clean and original version) to solve this crash. Note: known crash for common pirated copies & torrents of GTA, due to missing, bad or corrupted .dat, .col and .ipl files (pre-installed mods). MTA only supports the original, legally purchased version of GTA. |
| 0x000A2CF3 | Corrupted, missing or modded GTA San Andreas\models > effects.fxp file. If restoring that file to original doesn't fix the crash, use unmodded GTA as it can also be due to related GTA data files (ones that have to do with effects). |
| 0x001A49D4 | Bad mod (custom player.img in GTA San Andreas\models). Restore player.img to original or use unmodded GTA. Note: this crash can also be triggered when a player with CJ model (or CJ clothes) appears on your screen, on a server you're playing on. Your custom player.img cannot handle that and will cause a crash. |

## Resolving out-of-memory crashes

If you're experiencing crashes that, according to the table of common crashes, are related to any sort of running out of memory, then we advise you to;

- Mind the type of servers you're playing on, especially in combination with how powerful your PC is. There's lots of bloated, mod-heavy servers out there in MTA that demand the better of your PC and may also abuse memory through inefficient scripts besides custom mods (or even with the lack thereof).

We could write a book about the real cause (which is that such servers have bad scripters, or those that don't know what optimization is, and that they add everything, including bloated models and textures, without reviewing it) but we won't do that here.

If you have a slow or older generation PC, then we advise you to avoid certain "fancy" servers with huge resource downloads and such.

- Install 64-bits version of Windows rather than x86 (32-bit)

**If you still want to play on servers that may easily get upper hand on your system, then;**

- Upgrade your PC's hardware for enhanced performance; consider replacing the videocard with one suitable for gaming, or adding additional system memory (RAM). Re-installing Windows can sometimes also help a bunch if your OS in general is slow and not well-maintained. Alternatively, perform some mainentance (consult someone with tech experience, or make a start by updating drivers and running various junk cleaners & renowned PC performance optimization tools)

- Follow the instructions listed at [https://forum.mtasa.com/topic/78081-32-bit-windows-crashing/](https://forum.mtasa.com/topic/78081-32-bit-windows-crashing/)

- Remove any mods to your GTA installation (preferably re-install) because mods may take up video memory and RAM, enough to cause your high memory usage and subsequent crashes.
Also you should definately try lowering streaming memory, by going into Settings->Advanced->Streaming memory-> and setting it to Min.

Remember that GTA is an old game, and MTA places a lot of power in the hands of scripters (to mess up with a lack of optimization). Even if you have a high amount of RAM (for example 8gb, 16gb) you can't expect it to all be usable.. old games have technical limits and limited address space. Server scripters can do really cool and insanely realistic stuff while using far below 3.6GB RAM (the absolute technical limit in SA), but only as long they have scripters and modellers/designers that know about optimization. Strictly taken, no server, no matter how modded or beautiful.. should need to use above 2GB of RAM. Most decent servers use between 800MB - 1.6GB anyways. If you wish to learn more about this subject or are a server owner that wants to realize their mistakes, please join the MTA discord at [https://discord.gg/mtasa](https://discord.gg/mtasa) and go to the #general channel, then open that channel's pinned post about optimization ecosystem problems (written by Dutchman101).

Please note that in general, **any crash** with exception code **0xE06D7363** (on an MTA module, and not gta_sa.exe like this wiki page is focused on) is also a memory-related issue, and comes back to the memory abuse by servers and mods described above.

## Resolving crashes related to custom models

If you're experiencing crashes that, according to the table of common crashes, are related to corrupt custom models, then we advise you to re-install GTA from the original game source (DVD or Steam, so no pre-modded repacks) or restore targeted file back-ups in case you understand which (type of) model may cause the crash.

In case you're only experiencing the crashes while playing on a certain server, there's a high chance that server is loading custom server models, and then we recommend you to contact the server owner so they can investigate and potentially identify & replace the corrupted model to stop the crashes. Until they take successful action, on that server you can try to avoid physically facing the mod you believe results in a crash (like not spawning said vehicle or using said skin). 
Let us remind you of the chance that the bad model is in your GTA3.img, but by coincidence you never physically come near that model on other servers, and the server you're crashing the most on happens to force usage of that model ID upon you (like as regularly used vehicle or skin); therefore it cannot be ruled out that it's possibly still your client mod, despite you only crashing on a single server, and it's worth at least re-installing your GTA to try it out.

If you are a server owner and wouldn't prefer letting go of your beloved (corrupt) model, then you can ask an experienced modeller to try fix the corruption by modifying/revising it.
The alternative of crashing many players, potentially resulting in player loss for your server, isn't fine either way. For this reason, keeping a sharp eye on trends of players reporting (or shouting) that they crashed, and following up with them to get the crash details (to try match them up to model crashes from the table on this wiki page), may be a good idea.

Adding upgradable components (named "ug_upgradename") outside of chassis_dummy, will cause crashes once the vehicle has the respective upgrade component spawned.

More information about offsets: [GTA_Crash_Codes](mta://reference/misc/gta-crash-codes.md)
