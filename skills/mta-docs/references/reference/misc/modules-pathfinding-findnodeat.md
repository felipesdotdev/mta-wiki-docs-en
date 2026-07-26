---
doc_id: "mta-wiki:13575"
title: "Modules/Pathfinding/findNodeAt"
source_title: "Modules/Pathfinding/findNodeAt"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Pathfinding/findNodeAt"
revision_id: 73979
language: "en"
categories: []
---

# Modules/Pathfinding/findNodeAt

|  | This function is provided by the external module Pathfinding . You must install this module to use this function. |
| --- | --- |
|  |  |

This function searches for certain node.

## Syntax

```
int, float, float, float findNodeAt(int graphId, float positionX, float positionY, float positionZ)
```

### Required arguments

- **graphId:** The id of the graph

- **positionX, positionY, positionZ:** The postion where to search for a node

### Returns

Returns **4 integers** representing nodeId and his position if a node was found, **false** otherwise.

## Example

## See Also

### Functions

- [loadPathGraph](mta://reference/misc/modules-pathfinding-loadpathgraph.md)

- [unloadPathGraph](mta://reference/misc/modules-pathfinding-unloadpathgraph.md)

- [findShortestPathBetween](mta://reference/misc/modules-pathfinding-findshortestpathbetween.md)

- [isGraphLoaded](mta://reference/misc/modules-pathfinding-isgraphloaded.md)

- findNodeAt

- [getNodeNeighbors](mta://reference/misc/modules-pathfinding-getnodeneighbors.md)
