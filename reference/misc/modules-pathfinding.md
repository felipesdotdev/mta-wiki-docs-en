---
doc_id: "mta-wiki:13569"
title: "Modules/Pathfinding"
source_title: "Modules/Pathfinding"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Pathfinding"
revision_id: 73989
language: "en"
categories: ["Outdated_Pages", "Modules"]
generated_at: "2026-07-26T16:16:13.854951+00:00"
---

# Modules/Pathfinding

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

| Module info |  |
| --- | --- |
| Name | ml_pathfind |
| Version | 1.0.3 |
| Author | StiviK, eXo-Reallife team |
| Module website | Here |
| Download link | Windows 32 bit Windows 64 bit Linux |
| License | MIT |
| Written in | C++ |
| Operating system | Cross-platform |
| Compatible with | 1.X |

This module provides ability to find the shortest path between two points in the world.

## Installation

### Windows

**32 bit:** Copy 32 bit ml_pathfind_win32.dll into the **MTA San Andreas\server\mods\deathmatch\modules\** directory.

**64 bit:** Copy 64 bit ml_pathfind_x64.dll into the **MTA San Andreas\server\x64\modules\** directory.
  
  

Then, add the following line in mtaserver.conf:

**32 bit:**

```
<module src="ml_pathfind_win32.dll" />
```

**64 bit:**

```
<module src="ml_pathfind_x64.dll" />
```

### GNU/Linux

Copy ml_pathfind.so into the **modules/** directory.

Then, add the following line in mtaserver.conf:

```
<module src="ml_sockets.so" />
```

## See Also

### Functions

- [loadPathGraph](mta://reference/misc/modules-pathfinding-loadpathgraph.md)

- [unloadPathGraph](mta://reference/misc/modules-pathfinding-unloadpathgraph.md)

- [findShortestPathBetween](mta://reference/misc/modules-pathfinding-findshortestpathbetween.md)

- [isGraphLoaded](mta://reference/misc/modules-pathfinding-isgraphloaded.md)

- [findNodeAt](mta://reference/misc/modules-pathfinding-findnodeat.md)

- [getNodeNeighbors](mta://reference/misc/modules-pathfinding-getnodeneighbors.md)
