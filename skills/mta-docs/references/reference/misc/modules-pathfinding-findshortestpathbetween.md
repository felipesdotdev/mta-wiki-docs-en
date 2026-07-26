---
doc_id: "mta-wiki:13573"
title: "Modules/Pathfinding/findShortestPathBetween"
source_title: "Modules/Pathfinding/findShortestPathBetween"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Pathfinding/findShortestPathBetween"
revision_id: 73984
language: "en"
categories: []
---

# Modules/Pathfinding/findShortestPathBetween

|  | This function is provided by the external module Pathfinding . You must install this module to use this function. |
| --- | --- |
|  |  |

This function finds the shortest path between 2 points in the world.

## Syntax

```
bool findShortestPathBetween(int graphId, float startX, float startY, float startZ, float endX, float endY, float endZ, function callback)
```

### Required arguments

- **graphId:** The id of the graph

- **startX, startY, startZ**: The start position

- **endX, endY, endZ**: The end position

- **callback**: The callback function (parameters: table nodes)

### Returns

Returns **true** if the route calculation has been scheduled successfully, **false** otherwise.

## Example

## Issues

| Issue ID | Description |
| --- | --- |
| 8 | Providing callback function to findShortestPathBetween crashes the server |

## See Also

### Functions

- [loadPathGraph](mta://reference/misc/modules-pathfinding-loadpathgraph.md)

- [unloadPathGraph](mta://reference/misc/modules-pathfinding-unloadpathgraph.md)

- findShortestPathBetween

- [isGraphLoaded](mta://reference/misc/modules-pathfinding-isgraphloaded.md)

- [findNodeAt](mta://reference/misc/modules-pathfinding-findnodeat.md)

- [getNodeNeighbors](mta://reference/misc/modules-pathfinding-getnodeneighbors.md)
