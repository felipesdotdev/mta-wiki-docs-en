---
doc_id: "mta-wiki:1777"
title: "OnMapUnload"
source_title: "OnMapUnload"
source_url: "https://wiki.multitheftauto.com/wiki/OnMapUnload"
revision_id: 80559
language: "en"
categories: ["Historical", "MTA_Wiki:Delete", "Archived"]
generated_at: "2026-07-26T16:16:24.192093+00:00"
---

# OnMapUnload

|  | Historical: This page is retained for historical reference. |
| --- | --- |
| This event no longer exists since 2011 |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: This event no longer exists. Actions: Delete (Administrators) - Discuss - What links here - Category |  |

This event is triggered when the map is changed or unloaded.

## Example

This example displays a message in the textbox when the map is changed / unloaded

```
addEventHandler ( "onMapUnload", root, "onMapUnload" )
function onMapUnload ( )
  outputChatBox ( "Script Unloaded!", root, 255, 255, 255 )
end
```

## See also

- [loadMapData](mta://scripting/server/functions/loadmapdata.md)

- [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md)

- [saveMapData](mta://scripting/server/functions/savemapdata.md)
