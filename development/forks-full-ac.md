---
doc_id: "mta-wiki:13827"
title: "Forks Full AC"
source_title: "Forks Full AC"
source_url: "https://wiki.multitheftauto.com/wiki/Forks_Full_AC"
revision_id: 79869
language: "en"
categories: ["Development"]
generated_at: "2026-07-26T16:15:02.097509+00:00"
---

# Forks Full AC

| [[{{{image}}}\|link=\|]] | Note: Information on this page does not apply to the official builds of MTA. |
| --- | --- |
|  |  |

**Русская версия (может быть устаревшая, так как переведена вручную):** [RU/Полный античит MTA для форк-проектов](https://wiki.multitheftauto.com/wiki/RU/%D0%9F%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9_%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B8%D1%82_MTA_%D0%B4%D0%BB%D1%8F_%D1%84%D0%BE%D1%80%D0%BA-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2)

MTA forks that don't suffice to use "forks regular netc" (from bdata/netc.dll) as described in the [Forks](mta://development/forks.md) wiki page, due to it only offering a very limited AC (Anti-Cheat) protection, can explore the possibilities for using a new flavour of netc: "forks full AC". This however, comes with its own limitations pertaining to the nature of your forked project and implementations, matters that aren't easy to explain, but this page strives to do it as accurately as possible.

*This operation will turn your fork into a project with a "proper, method patching-based AC" as official MTA is described to have at the spoiler in this topic: [https://forum.multitheftauto.com/topic/66858-bounty-for-finding-security-flaws-and-working-cheats-in-mta/](https://forum.multitheftauto.com/topic/66858-bounty-for-finding-security-flaws-and-working-cheats-in-mta/) rather than at most 15% 'signature based' AC per the [Forks](mta://development/forks.md) wiki page's description of regular forks AC/netc.*

Basic idea:

- "forks full AC" netc module starts off providing 95% of AC features found in official MTA (multitheftauto.com > "Download" button) builds

- The more incompatible features/implementations (custom changes) your forked project has, which **you** may opt to 'silence' (by adding them to a detection # whitelist: **disableac** array in **mtaserver.conf** as documented in [Anti-cheat guide: DISABLEAC](https://wiki.multitheftauto.com/wiki/Anti-cheat_guide#%3Cdisableac%3E%3C/disableac%3E)), the lower said protection number in percentage will become.

- **For example**, if you have to disable 3 different detection types (let's say for russian forks, given external mod loading outside of MTA API/limit adjusters the most common ones are: 5, 6, 21) you would get a 85% of AC protection left. Although this number is relative, as it provides opportunities for cheat developers to use exactly the 'stripped' detection categories for making their hack work, like these 3 codes would already provide some specific avenues for writing to GTA memory.

Can you spot in which direction this is going? Later in this article a link to "forks full AC" will appear, and what you'll do with it is trial and error. Trying to integrate full AC support into your fork is a matter of "We can try, and if it ends up working, it's nice to have.. if we have to disable some detections, a protection percentage of anything higher than regular forks AC: 15% is already a huge gain.." and highly on a best effort basis. Because the reason we separated forks netc (from bdata/netc.dll) to one that lacks most AC features can be clear to any skilled developer: netc module (the AC) isn't designed to expect all types of customisations that a fork developer may add to their codebase, it was in the spirit of providing maximum freedom and flexibility. Especially as a lot of forks don't have the best developers, not knowing why they are better off following MTA (mtasa-blue) coding guidelines, project structure, and matching their custom inplementations as closely to how an MTA contributor that passes code review, would typically do it. So this is where 'clean' changes are separated from 'dirty modding', which is also often seen in Russian forks **that use one or more of the following approaches to their project's codebase:**
****

- Implementation of GTA SA modding projects in an external 'dirty' way, like limit adjuster (fastman92 etc)

- Raw loading of GTA SA modded data & .IMG files, through distribution of pre-modded GTA install folders to fork client players. Thereby completely ignoring the MTA API for replacing models and various game processes

- Miscellaneous dirty patches, in the broad sense of what is described in the paragraph above this. Also includes not following MTA "Raw memory access" guidelines found here: [https://github.com/multitheftauto/mtasa-blue/wiki/Dev-Tips](https://github.com/multitheftauto/mtasa-blue/wiki/Dev-Tips) which is a significant risk factor to scenario's not expected by netc.dll (the AC), as if it protects against memory modifications by knowing the origin, and you just put a dirty 'writeProcessMemory' or memcpy in a random .cpp file, it will cause a violation. This isn't all that's to it and a bad example, but just so you get the basic idea of why incompatibilities exist.

### Getting the most out of AC protection %

After understanding the above, and also our best-effort basis as such usage as a "full AC" for forks was never our intention and how it would be hard to support everyone's custom modification, you can figure that we cannot help you to investigate what is incompatible right after you start testing "full AC" netc in your fork. Therefore it is up to you to either disable as many detections as required (if you cannot fix them - where the 'cannot' is an indicator of lack of engineering oversight) or better yet, come up with fixes that allow you to avoid disabling too many, or any, detection types, thereby maximizing your potential AC features %.

This means that without MTA team's support, you are to figure out which customisations/integrations/not following MTA APIs/example problems as described earlier in this article.. are the culprit for each specific detection type that sends you AC kicks after putting "full AC" netc into your fork for testing purposes. We advise you clean up your integrations to avoid having to do a lot of manual digging/speculating on the culprit. For that, take care of entries from the bulleted list from the earlier paragraph. If a direct culprit was found however, on our best effort basis, you should without any guidance by MTA, come up with alternative (cleaner, more following MTA coding guidelines, APIs and project structure.. hence less likely incompatible with full AC and what it expects) implementations of the problematic customisation found in your fork's codebase. You can see where being able to use 'full AC for forks' becomes a favour rather than a given fact, especially with the state of codebase that a lot of forks, without starting their development in a 'full AC' scenario, have grown into by just writing what works for them without considering such aspects. The big picture of why we wouldn't support re-engineering process should now be clear. If you cannot deal with it, either get someone with a lot of engineering (CS) experience, or disable more AC detection types, and settle for anything that's higher than the 15% regular forks netc, better something than nothing. **But we will pertinently not be able to lend a hand.** Any misunderstanding of these concepts indicates a lack of developer completeness (individual skills, room to grow) and cannot be reflected upon the MTA devs.

# **Let's get to the point**

If you think that you understand all concepts described in this article, you can begin to implement "full AC for forks":

**DOWNLOAD: [https://mirror-cdn.multitheftauto.com/bdata/fork-support/netc.dll](https://mirror-cdn.multitheftauto.com/bdata/fork-support/netc.dll)** (so *instead* of using "bdata/netc.dll" from default mtasa-blue buildactions/install_data.lua)
Note that the version of netc.dll at the above link will be regularly updated to provide forks with all AC improvements delivered in official MTA as well. So it's recommended to fetch updates to your fork for optimal security & AC strength, on a regular basis

| [[{{{image}}}\|link=\|]] | Note: Important: As of June 2023, you must pull all mtasa-blue commits (update to 1.6) and sync your fork's codebase in order to use the latest netc version provided at the link above. There are incompatible changes that required updates on both sides. The netc module being offered fits for a fork based on MTA 1.6 |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Important: It's your own responsibility to add a file integrity/authencity checker, as obviously since the game DLLs are built by you (and not us) there is no way to embed such unique DLLs into our netc internal checklists, nor have anything within other modules to check netc itself. If you don't work this out, a cheater can just replace any module or add in a cheat payload with PE editing, this is the biggest risk factor when using "forks full AC". How far you'd like to go with file checks, like deciding to harden it on usermode (with heartbeats or so) or use your own secondary kernelmode AC driver, is up to you and the level of dedication to security your project has. If all you care about is a raised border towards cheating, you may go for basic file checker (MD5/SHA256) for all game modules There are more and similar bottlenecks that are too complicated to easily explain but are based on the "nothing is ever 100% secure" principle, of which many apply to bridging between official MTA and forks using 'full AC'. It is also good to reflect on the overall thing like this: MTA team spent years to build AC technology, and its providing (now unlocking) a lot to forks if they so wish, for free. Consider it as a main layer of anticheat that already protects a lot in GTA, we help you not to have to build such a huge amount of technology all by yourself. Now the point, what else you do, like you see this as main layer and then also build your own secondary layer of anticheat, maybe even on a novice level of what's technically understandable to your developers that have no serious AC development background - that's entirely up to you and your creativity, and how serious you take your project. If you want to complement the main layer provided by us, you are able to. |
| --- | --- |
|  |  |

- Replace netc.dll in your forked project with the above "forks-support" full AC netc.
- Make sure that version.h build type is set to UNSTABLE, as per the forks "mass consumption" recommendations in its comments: [Shared/sdk/version.h](https://github.com/multitheftauto/mtasa-blue/blob/master/Shared/sdk/version.h). If not the case, you will nullify the entire effort of getting full AC protection.

- Make sure that you upgraded the codebase of your fork to the active major version's (for which netc.dll) **master** commit of mtasa-blue, at least the "Default" version listed at [[1]](https://nightly.mtasa.com/ver/) as "Auto-update default" for the latest major version, then matching said revision to commit SHA1 hash with this tool: [https://buildinfo.mtasa.com/index.php](https://buildinfo.mtasa.com/index.php) - this means not to use the github release tag of a major version, because MTA is using "MTA-as-a-service" model, where players receive regular updates that contain all master changes for optimal quality and experience of new features. Latest netc.dll releases are based on this and may require master changes to be present.

- For your dedicated servers / nodes to which players will connect, use the server net modules from:  

Linux x64: [https://mirror-cdn.multitheftauto.com/bdata/net_64.so](https://mirror-cdn.multitheftauto.com/bdata/net_64.so) (rename to "net.so")  

Windows x64: [https://mirror-cdn.multitheftauto.com/bdata/net_64.dll](https://mirror-cdn.multitheftauto.com/bdata/net_64.dll) (rename to "net.dll")  

Never use x86 server for your fork, that's bad for many reasons. Not being encouraged, it will have no steps.

Let's continue with setting up the client and 'full AC'.

- Face some AC kicks in your forked client, the trial and error stage begins here. Now use the earlier parts of this guide to either disable AC detection types by disableac in mtaserver.conf, or better yet, spend more development manpower on properly fixing them & cleaning up your custom implementations, as advised earlier as well, to keep as much AC protection % as possible. We advise not going below 85% (as in the example of 'disableac' codes: 5, 6, 21 was mentioned to be relatively 85% and what most russian, mod-heavy forks would require to immediately run and let you connect)

Closing words: it will always be better to not be a fork in the first place. To use the official MTA client and simply create a server, eventually with a custom launcher that connects straight to your array of servers. To just contribute all customisations that you'll need (reason for becoming a fork instead) "upstream", which means in a PR, Pull request, to the official MTA repository at [https://github.com/multitheftauto/mtasa-blue](https://github.com/multitheftauto/mtasa-blue) so everyone benefits and you honour the license & not deal with the roadblocks, AC and new player influx included, of being a fork. MTA usually has 30,000 players online at the same time, which is also a huge pool of new player influx to discover your community. Better just don't be a fork, but if you really need to, this page is our active outreach towards forks to get a better degree of Anti-Cheat (AC) protection.  
  

We created this "full AC for forks" flavour of netc.dll in November/December 2022, and trialed the practical results and some specific patches to it for better support, with 2 of the biggest Russian MTA forks, both of which are preparing to release an update incorporating this in the coming few months. We also did an outreach to smaller fork developers that however chose to abuse it (and with that our trust) by immediately becoming toxic and trying to sell the "full AC" netc module we gave them, prompting this wiki article to be written and published in a hurry. Not nice, and please don't fall for any offers from said circle of toxic fork developers trying to sell you such an "full AC" netc, when you can get a newer version from the official source, from us in this article. The work on this article has in the context of said incident, been discussed in MTA development discord (invite: [https://discord.gg/GNN6PRtTnu](https://discord.gg/GNN6PRtTnu)) at this post: [https://discord.com/channels/801330706252038164/801330706252038170/1044757943071023155](https://discord.com/channels/801330706252038164/801330706252038170/1044757943071023155) and its equivalent in the main, official MTA discord (invite: [https://discord.gg/mtasa](https://discord.gg/mtasa)) at this post: [https://discord.com/channels/278474088903606273/278521065435824128/1044758439357849661](https://discord.com/channels/278474088903606273/278521065435824128/1044758439357849661)
