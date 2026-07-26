---
doc_id: "mta-wiki:14299"
title: "RemoveAllGameBuildings"
source_title: "RemoveAllGameBuildings"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveAllGameBuildings"
revision_id: 82179
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0", "Deprecated"]
---

# RemoveAllGameBuildings

ADDED/UPDATED IN VERSION 1.6.0 [r22420](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22420):

This function is used to remove all world buildings and frees building pool. 

| [[{{{image}}}\|link=\|]] | Note: This function does not affect buildings created using the createBuilding function |
| --- | --- |
|  |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use removeGameWorld instead. See this pull request . |  |

## Syntax

```
nil removeAllGameBuildings ( )
```

### Returns

This function does not return any value.

## Example

This example removes game buildings.

```
addEventHandler("onClientResourceStart", resourceRoot, function()
    removeAllGameBuildings()
end)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22410](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22410):

- [createBuilding](mta://scripting/shared/functions/createbuilding.md)
