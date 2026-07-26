---
doc_id: "mta-wiki:3864"
title: "HandlingGetDragCoefficiency"
source_title: "HandlingGetDragCoefficiency"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetDragCoefficiency"
revision_id: 80941
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
generated_at: "2026-07-26T16:15:42.448743+00:00"
---

# HandlingGetDragCoefficiency

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: It has never existed. |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the drag coefficient (amount of air resistance) of a handling element or a vehicle ID.

## Syntax

```
float handlingGetDragCoefficiency ( handling theHandling )
float handlingGetDragCoefficiency ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling you wish to get the drag coefficient of, *or*

- **vehicleID:** the vehicle ID you wish to get the drag coefficient of.

### Returns

If you specified a handling element, returns its drag coefficient if one was set, or *nil* otherwise. If you specified a (valid) vehicle ID, returns the drag coefficient that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
function getDragCoefficiency ( player, command )
local vehicle = getPedOccupiedVehicle(player)
    if vehicle then
      str = handlingGetDragCoefficiency(getElementModel(vehicle))
      outputChatBox("Your vehicle's handling drag coefficiency is "..str,player,0,255,255)
    end
end
addCommandHandler ( "dragcoe", getDragCoefficiency )
```

## See Also
