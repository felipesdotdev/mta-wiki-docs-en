---
doc_id: "mta-wiki:1548"
title: "LoadMapData"
source_title: "LoadMapData"
source_url: "https://wiki.multitheftauto.com/wiki/LoadMapData"
revision_id: 82238
language: "en"
categories: ["Server_functions"]
---

# LoadMapData

This function is intended to load data from a loaded XML file into the element tree. This could be used for loading an external map, or part of another map.

## Syntax

```
element loadMapData ( xmlnode node, element parent )
```

### Required Arguments

- **node:** The node that you wish to load into the [element tree](mta://reference/misc/element-tree.md).

- **parent:** The node you wish to be the parent of the new map data.

### Returns

Returns an [element](mta://reference/misc/element.md) object that corresponds to the root of the new data added, i.e. an element that represents the *node* xmlnode passed to the function. Returns *false* if the arguments are invalid.

## Example

**Example 1:** This example is a function that you could use to load an arbitary [map file](https://forum.mtasa.com/topic/126081-map-files) into the [element tree](mta://reference/misc/element-tree.md).

```
function loadMapFile(fileName)
	local xmlNode = getResourceConfig(fileName)

	if (xmlNode) then -- check if the file was loaded ok
		loadMapData(xmlNode, root) -- load the loaded xml file into the element tree
		xmlUnloadFile(xmlNode) -- Unload the xml file
	end
end
```

**Example 2:** This example will destroy the loaded map data after 30 seconds.

```
function loadMapFile(fileName)
	local xmlNode = getResourceConfig(fileName)

	if (xmlNode) then -- check if the file was loaded ok
	    nodeElement = loadMapData(xmlNode, root) -- load the loaded xml file into the element tree
		xmlUnloadFile(xmlNode) -- Unload the xml file
	end
end

setTimer(function() 
    destroyElement(nodeElement)
end,30000,1)
```

## See Also

- loadMapData

- [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md)

- [saveMapData](mta://scripting/server/functions/savemapdata.md)
