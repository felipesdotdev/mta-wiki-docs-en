---
doc_id: "mta-wiki:2367"
title: "SaveMapData"
source_title: "SaveMapData"
source_url: "https://wiki.multitheftauto.com/wiki/SaveMapData"
revision_id: 76008
language: "en"
categories: ["Server_functions", "Utility_templates"]
---

# SaveMapData

This converts a set of elements in the element tree into XML. This is a format that can then be loaded as a map file. Each element represents a single XML node.

## Syntax

```
bool saveMapData ( xmlnode node, element baseElement [, bool childrenOnly = false ] )
```

### Required Arguments

- **node**: An existing node that should contain the contents of baseElement

- **baseElement**: The first element to output to the XML tree. This element and all its children (and their children, etc) will be output.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **childrenOnly**: Defines if you want to only save children of the specified element.

### Returns

## Example

Saving your resource's data to an [map file](https://forum.mtasa.com/topic/126081-map-files) (untested)

```
local mapFile = xmlCreateFile("saved.map", "map")

if mapFile then
	saveMapData(mapFile, resourceRoot)
	xmlSaveFile(mapFile)
	xmlUnloadFile(mapFile)
end
```

## See Also

- [loadMapData](mta://scripting/server/functions/loadmapdata.md)

- [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md)

- saveMapData
