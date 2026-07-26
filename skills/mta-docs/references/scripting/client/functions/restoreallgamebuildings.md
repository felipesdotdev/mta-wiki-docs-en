---
doc_id: "mta-wiki:14300"
title: "RestoreAllGameBuildings"
source_title: "RestoreAllGameBuildings"
source_url: "https://wiki.multitheftauto.com/wiki/RestoreAllGameBuildings"
revision_id: 82181
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0", "Deprecated"]
---

# RestoreAllGameBuildings

ADDED/UPDATED IN VERSION 1.6.0 [r22420](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22420):

This function cancels [removeAllGameBuildings](mta://scripting/client/functions/removeallgamebuildings.md) effect 

| [[{{{image}}}\|link=\|]] | Note: This function can destroy some scripted buildings if the building pool does not have enough free space for game buildings. |
| --- | --- |
|  |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use restoreGameWorld instead. See this pull request . |  |

## Syntax

```
nil restoreAllGameBuildings ( )
```

### Returns

This function does not return any value.

## Example

This example restores game buildings.

```
addEventHandler("onClientResourceStop", resourceRoot, function()
    restoreAllGameBuildings()
end)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22410](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22410):

- [createBuilding](mta://scripting/shared/functions/createbuilding.md)
