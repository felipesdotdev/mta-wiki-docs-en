---
doc_id: "mta-wiki:7077"
title: "MTA:Eir"
source_title: "MTA:Eir"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir"
revision_id: 50580
language: "en"
categories: ["Development"]
---

# MTA:Eir

MTA:Eir is an alternative multi-player modification to the MTA:BLUE core series. It is under development since August 2011 by midnightStar/The_GTA (Martin Turski). It started off with the first stable version of MTA:BLUE 1.2 and its netcode was later updated to MTA r3566 1.3 unstable. It aims to enrichen the MTA core with functionality, purpose and stability. It has been inspired by the limitations set forth by the current MTA:BLUE system. He wants to fulfill his dream: a perfect MTA:SA experience, for gamers and modders.

Team members: midnightStar, Remi-X, GodFather, GhostRider, Wafamde

IRC channel: irc.multitheftauto.com #mta.recore

SVN: [https://osdn.net/projects/green-candy/](https://osdn.net/projects/green-candy/)
Concept art: [http://s1320.photobucket.com/user/bloxman/library/](http://s1320.photobucket.com/user/bloxman/library/)

Bugtracker: [http://woovie.net/mantis/](http://woovie.net/mantis/)
Livestreams: [http://livestream.com/mtaeir](http://livestream.com/mtaeir)

## Important Related Links

### MTA:Eir

- [New Scripting Functions](mta://scripting/concepts/mta-eir-new-scripting-functions.md)

- [TODO List](mta://reference/misc/mta-eir-todo.md)

- [Documentation about engine functionality](mta://reference/misc/gta-sa-engine-research.md)

- [MTA:Eir FileSystem Documentation](mta://reference/misc/mta-eir-filesystem.md)

## A Personal Story

Prior to MTA:Eir development The_GTA has been active in the MTA community as scripter and (rarely) server host. He had developed his own gamemode which featured ped synchronization, an account system, spawn management, pickup management and vehicle spawns. He is the creator of the [pathrecorder](https://wiki.multitheftauto.com/index.php?title=Resource:Pathrecorder&action=edit&redlink=1), [resedit](mta://resources/resedit.md) and [openradio](https://wiki.multitheftauto.com/index.php?title=Resources:openradio&action=edit&redlink=1) resources. As a hobby, he has been working on several utilities: pathfinding, GUI environments, shaders, Lua script processors, GTAIII map converter (Scene2Res). In these projects he studied the concept of MTA. Using resedit he had hosted a scripting server where he inspired people with scripting ideas and taught them Lua. After that he moved on to total-conversion-oriented modding: he converted multiple GTAIII maps (Liberty City, Vice City, Gostown, GrandCarma, Anderius, Mushroomia, Myriad Isles, ...). After many hours of investigation on model loading and replacement he figured that MTA required an engine interaction overhaul.

Equipped with the knowledge about the MTA system, he began studying the source code.

- He concluded that game_sa merely was a drop-in functionality hook for expansion in the deathmatch module. It did not have proper managers for its own, for GTA:SA objects.

- Inside of deathmatch he has seen code which would be better placed inside game_sa due to its game engine nature (player input management, dff/txd/col classes, ...).

- Classes were cast virtual the same way as they were in game_sa resulting in unnecessary leaks of internal logic.

- Dozens of assertions were placed to check for NULL pointers although the documentation of said functions did not allow NULL pointers as arguments. The message to new developers was as if you did not have to inspect how MTA worked; just paste in your code, screw it with a wrench and expect the team to keep compatibility.

- When he found out about "cvars" in the MTA console he was excited: from Savage he knew them as dynamic variables which the user could play around with in a command-line language. Upon closer research he did not find the command-line language he hoped for.

- He saw classes written with static functions although they could have aswell been namespaces. He found namespaces to be an easier development method.

- He saw that MTA codebase consisted of many copy-pasted codelines, primarily between client and server. He wondered about code quality via environment specialization.

The_GTA disliked the management of the codebase. To fix it he knew that he had to create a fork: an independent codebase where he could do changes without MTA team approval. At the end of his mission he aims to merge the MTA:BLUE and MTA:Eir projects together to create the best MTA experience.

## Project aspirations and targets

- Restructure the game_sa layer to be game-engine like. Move input management code into game_sa (deathmatch:CClientPad should not be handling it). Manage GTA:SA objects, game_sa objects inside of game_sa, do not export internal pointers into deathmatch for security and stability reasons.

- Rewrite the code into a clean C++ syntax (no DWORD, WORD; follow MTA guidelines; add documentation; proper virtualization).

- Document the codebase, expose GTA:SA functionality -> new developers should not need GTA:SA ASM knowledge to code for MTA

- Replace obsolete, less-performant logic with more internally fitting logic (STL containers into C-arrays)

- Remove the multiplayer_sa layer -> move all its logical improvements into game_sa, clean C++ rewrite

- Upgrade Lua 5.1.4 to support classes itself (adapted from the MTA entity system) -> make MTA classes also Lua classes

### Reven Programming Department

The core principle of MTA:Eir development is **reven**. This is the skill to understand what GTA:SA is internally doing (ASM + classes + logic). It stands for **Reverse Engineering**. For this task The_GTA introduced the **Reven Programming Department**. Every code added to MTA should comply with GTA:SA logic. This means that code remains a quality standard set against the GTA:SA logic. MTA code should be able to

- compete with

- extend

- replace

Rockstar's inventions. Members of this group have the task to investigate the GTA:SA code and expose it into the MTA code by native C++ rewrite. They have to implement the code into the system while updating any affected, already present code. It requires a thorough understanding of the whole project.

- If ASM hooks were placed in the rewritten functions, said hooks should be rewritten into C++ too.

- If there were memory patches in the conflicting areas, the coder has to keep their logic compatible. If the memory patches targeted ASM flow, the new resulting logic should be put into the MTA codebase. The old GTA:SA Rockstar flow should be at least hinted at in comments. If the memory patched targeted variables, then special care in conversion is necessary: can said variable be imported into MTA internal? If not, the new C++ code has to access the GTA:SA memory location. GTA:SA variables can be imported into MTA code if GTA:SA does not reference the memory locations anymore.

Eventually MTA:Eir will be capable to manage GTA:SA activity itself. MTA:Eir has to redirect the program's flow in a way that it is multi-player compatible. Thus being an RPD member has high responsibility.

### Logic Programming Department

The members of this group harvest the logic that the RPD has exposed from GTA:SA. They should constantly be in touch with RPD members to know what GTA:SA is internally doing. In a common sense, they are in charge of the deathmatch module. If game features are requested, they are assigned to make them happen. This implies that they are also the testers of the logic that the RPD members exposed. Not only should they add new features into the engine. Most important is the improval of current logic, on their own devices. Members who are entrusted in this group need to be advanced C++ developers.

## MTA:BLUE 2.0/Eir Fork

In the end of March 2013 the MTA:Eir project has acquired a fork on the official MTA codebase. It is not the current, neither the final representation of MTA:Eir. Additions to it are result of negotiation between the MTA:Eir and the MTA:BLUE team. Unlike MTA:Eir, this fork is not "A Personal Story". Code which has been ported to it has been heavily tested on the MTA:Eir codebase. [ccw](https://wiki.multitheftauto.com/wiki/User:Ccw) has granted The_GTA the 2.0 branch. The_GTA is very thankful for this opportunity, since he has been seeking for it since the beginning of his development. The branch has later been changed into the current "eir" fork as the development team wanted to perform a "second-pass" before MTA:Eir code would be approved.

The project is estimated to reach full-pace in summer 2013.

### Patch overview

- basemodelinfo patch - major update to the GTA:SA streaming system to add multiplayer support to it. Included multiple other modules such as extensions to the RenderWare Interface, Placeable transformation matrix management and IMG limit breaker inspired by fastman92.

- another maintenance update - updated collision logic of the rewritten streaming system and fixed the EU crash which hindered players to join games, polished up classes and definitions, improved alpha rendering of game entities (fixed 100 ALPHAREF clip for setElementAlpha) and more.

### Bugreporting

Any bugs found in the build should be reported to midnightStar directly. Join the #mta.recore channel to do that. If midnightStar is not present, contact another team member and tell him to write down details about the bug. The bug-report should be filed just like in the MTA Mantis bugtracker (title, description, additional details, (optional) screenshots, video, contact e-mail address).

### Contributing

The_GTA welcomes contribution to the fork. Before you do though, contact him directly in the #mta.recore development channel. He will discuss details with you.
