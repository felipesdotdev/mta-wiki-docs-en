---
doc_id: "mta-wiki:14372"
title: "Default resources"
source_title: "Default resources"
source_url: "https://wiki.multitheftauto.com/wiki/Default_resources"
revision_id: 80100
language: "en"
categories: ["Development"]
---

# Default resources

This page is related to the [mtasa-resources](https://github.com/multitheftauto/mtasa-resources) project, the **Default Lua resources that come with the Multi Theft Auto (MTA) multiplayer mod**.

| [[{{{image}}}\|link=\|]] | Note: This article is currently Work In Progress |
| --- | --- |
|  |  |

## Download

These resources are available for **download** as a full ZIP archive on the **Official Resources** webpage at [https://mirror-cdn.multitheftauto.com/mtasa/resources/](https://mirror-cdn.multitheftauto.com/mtasa/resources/). You may also obtain the files by downloading the GitHub Repository as a zip archive or by cloning it to your machine using Git.

## Resources

All resources described below can be found in the [mtasa-resources official GitHub repository](https://github.com/multitheftauto/mtasa-resources). To learn about a resource's history and recent changes, view the **Git Commit History** available online.

### Administration

##### [admin](https://wiki.multitheftauto.com/index.php?search=admin)

MTA's default admin panel. Originally created by lil_Toady.

##### admin2

A general overhaul to MTA's default admin panel which is currently in development and meant to eventually replace the original admin resource.

##### ip2c

Utility resource to find the country associated with a certain IP-address range.

##### runcode

Runcode allows the user to quickly execute code via the use of an ingame command. Use /run [your code] for server-side or /crun [your code] for client-side code execution. Typically used for testing on development servers, not recommended for production level servers.

### Map Editor

##### [editor](https://wiki.multitheftauto.com/index.php?search=editor)

MTA's default map editor system, allowing you to create maps for gamemodes.

##### [edf](https://wiki.multitheftauto.com/index.php?search=edf)

EDF stands for Editor Definition File. This resource is the core functionality behind .edf files.

### Gamemodes

##### [assault](mta://resources/assault.md)

In assault one team has to fulfill certain tasks within a time limit while the other team has to prevent their opponents from completing them.

##### briefcaserace

In briefcase race multiple teams compete to deliver briefcases to their destination.

##### [ctf](mta://resources/ctf.md)

In capture the flag two or more teams compete to steal and capture the flags of the opposing teams.

##### ctv

In capture the vehicle two or more teams compete to deliver vehicles to their home base before the opponents.

##### deathmatch

Deathmatch is a free-for-all gamemode where the goal is to reach a certain frag limit before anyone else.

##### fallout

In fallout players compete to stay on top of falling platforms for as long as possible.

##### hay

In hay players attempt reach the top of a tall tower made from moving hay bales.

##### play

MTA's default freeroam gamemode. It will spawn players around certain areas all over San Andreas and spawn in vehicles for them to explore the world with.

##### [race](mta://resources/race.md)

MTA's race gamemode features both checkpoint races and last-man-standing style destruction derbies. Originally created by arc_ with lots of improvements from ccw.

##### [stealth](mta://resources/stealth.md)

The stealth gamemode features noise and stealth mechanics as well as many gadgets players can choose from. Two teams compete to be the last one standing. Originally created by slothman and talidan.

##### tdm

A basic team deathmatch mode where two teams compete to reach a given frag limit before the other.

##### tdma

Team death match arena is another team death match gamemode. It functions similarly to 'tdm' but is usually played on smaller, more concealed maps with spawn points establishing a clear frontline separating the teams.

### Gameplay

##### deathpickups

This resource will spawn weapon pickups near player corpses after they died.

##### defaultstats

While running, this resource will make sure to give players maximum stats for stamina, weapon skills and more.

##### freeroam

Freeroam provides players with a simple to use GUI window to do simple things like teleport, spawn vehicles or weapons, select a skin or play animations. It's used by the 'play'-gamemode.

##### gps

GPS is able to calculate and display the quickest road path between two points on the map. Use /path2 [x] [y] [z] with your desired destination coordinates to receive directions on your mini-map.

##### headshot

While this resource is running a single shot to a player's head will result in an instant kill.

##### [hedit](https://wiki.multitheftauto.com/index.php?search=hedit)

Powerful in-game handling editor to adjust various vehicle handling properties in real-time.

##### mapfixes

Patches some flaws in the default MTA world, caused by missing objects that would usually be loaded in the singleplayer game via mission-scripts.

##### [realdriveby](mta://resources/realdriveby.md)

Enables advanced drive-bys with more weapons and configurable restrictions. Originally created by talidan.

##### reload

Enables players to reload their current weapon with a configurable (default 'r') key.

##### sfxbrowser

GUI browser to find and play sound effects from GTA:SA's sound banks. After starting the resource use /sfxbrowser to open.

### Managers

##### [helpmanager](https://wiki.multitheftauto.com/index.php?search=helpmanager)

A GUI-interface meant to provide a central location for other resources to provide helpful insight on how to use them.

##### [mapcycler](mta://resources/mapcycler.md)

Enables servers to cycle between select lists of maps and gamemodes automatically.

##### [votemanager](https://wiki.multitheftauto.com/index.php?search=votemanager)

A resource to provide servers with the ability to start and process votes like mapvotes, kickvotes and more.

## Development

The [mtasa-resources](https://github.com/multitheftauto/mtasa-resources) project is open source. Contributions can be done in various ways: not only with code, but also with documentation and bug reporting, for example.

##### Contributing

Everyone is welcome to participate in improving the resource pack. Read more about the development process here: [Default resources - Contributing](mta://reference/misc/default-resources-contributing.md)
