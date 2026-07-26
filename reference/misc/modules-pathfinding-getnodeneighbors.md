---
doc_id: "mta-wiki:13576"
title: "Modules/Pathfinding/getNodeNeighbors"
source_title: "Modules/Pathfinding/getNodeNeighbors"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Pathfinding/getNodeNeighbors"
revision_id: 73980
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.903927+00:00"
---

# Modules/Pathfinding/getNodeNeighbors

|  | This function is provided by the external module Pathfinding . You must install this module to use this function. |
| --- | --- |
|  |  |

This function gets "neighbours" of a certain node.

## Syntax

```
table getNodeNeighbors(int graphId, int nodeId, int depth)
```

### Required arguments

- **graphId:** The id of the graph

- **nodeId:** The id of the start node

- **depth:** The depth of the node neighbors

### Returns

Returns **4 integers** representing nodeId and his position if a node was found, **false** otherwise.

## Example

## See Also

### Functions

- [loadPathGraph](mta://reference/misc/modules-pathfinding-loadpathgraph.md)

- [unloadPathGraph](mta://reference/misc/modules-pathfinding-unloadpathgraph.md)

- [findShortestPathBetween](mta://reference/misc/modules-pathfinding-findshortestpathbetween.md)

- [isGraphLoaded](mta://reference/misc/modules-pathfinding-isgraphloaded.md)

- [findNodeAt](mta://reference/misc/modules-pathfinding-findnodeat.md)

- getNodeNeighbors
