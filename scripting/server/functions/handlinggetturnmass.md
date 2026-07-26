---
doc_id: "mta-wiki:3863"
title: "HandlingGetTurnMass"
source_title: "HandlingGetTurnMass"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetTurnMass"
revision_id: 42748
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events"]
generated_at: "2026-07-26T16:15:42.629510+00:00"
---

# HandlingGetTurnMass

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: It has never existed. |  |

Returns the turn mass of a handling element or vehicle ID.

## Syntax

```
float handlingGetTurnMass ( handling theHandling )
float handlingGetTurnMass ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the turn mass, *or*

- **vehicleID:** the vehicle ID of which you want to get the turn mass.

### Returns

If you specified a handling element, returns its turn mass if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the turn mass that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
function getTurnMass ( player, command )
local vehicle = getPedOccupiedVehicle(player)
    if vehicle then
      str = handlingGetTurnMass(getElementModel(vehicle))
      outputChatBox("Your vehicle's handling turn mass is "..str,player,0,255,255)
    end
end
addCommandHandler ( "turnmass", getTurnMass )
```

## See Also
