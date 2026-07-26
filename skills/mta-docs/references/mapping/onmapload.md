---
doc_id: "mta-wiki:1775"
title: "OnMapLoad"
source_title: "OnMapLoad"
source_url: "https://wiki.multitheftauto.com/wiki/OnMapLoad"
revision_id: 80558
language: "en"
categories: ["Historical", "MTA_Wiki:Delete", "Archived"]
---

# OnMapLoad

|  | Historical: This page is retained for historical reference. |
| --- | --- |
| This event no longer exists since 2011 |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: This event no longer exists. Actions: Delete (Administrators) - Discuss - What links here - Category |  |

This event is triggered when a map is loaded.

## Syntax

```
void onMapLoad ( string name )
```

## Variables

- The source of this event refers to the loaded map.

- **name**: A string representing the name of the map

## Example

This example displays a message in the textbox when you load a map containing this lua

```
addEventHandler ( "onMapLoad", getRootElement(), "mapLoadChatBoxOutput" )
function mapLoadChatBoxOutput ( name )
	outputChatBox ( "Map "..name.." Loaded", root, 255, 255, 255 )
end
```

## See Also

- [loadMapData](mta://scripting/server/functions/loadmapdata.md)

- [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md)

- [saveMapData](mta://scripting/server/functions/savemapdata.md)
