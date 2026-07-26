---
doc_id: "mta-wiki:2549"
title: "ResetMapInfo"
source_title: "ResetMapInfo"
source_url: "https://wiki.multitheftauto.com/wiki/ResetMapInfo"
revision_id: 82690
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:33.332695+00:00"
---

# ResetMapInfo

This function is used to reset the state of a player.  It is intended to restore a player to their default state as if they had just joined the server, without any scripts affecting the player.

## Syntax

```
bool resetMapInfo ( [ player thePlayer = root ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **thePlayer:** The specific player you wish to restore the state of.  Not specifying this will result in all players map info being reset.

## Returns

Returns *true* if the map info was reset successfully, otherwise *false*.

## Example

This will reset all map info when the resource is stopped.

```
function onResourceStop()
	resetMapInfo()
end
addEventHandler("onResourceStop", resourceRoot, onResourceStop)
```

## See Also

- [loadMapData](mta://scripting/server/functions/loadmapdata.md)

- resetMapInfo

- [saveMapData](mta://scripting/server/functions/savemapdata.md)
