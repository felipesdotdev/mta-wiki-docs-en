---
doc_id: "mta-wiki:3865"
title: "HandlingGetCenterOfMass"
source_title: "HandlingGetCenterOfMass"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetCenterOfMass"
revision_id: 82305
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
generated_at: "2026-07-26T16:15:42.418223+00:00"
---

# HandlingGetCenterOfMass

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the center of mass of a handling element or vehicle ID. This is a 3D vector relative to the center of the mesh.

## Syntax

```
float float float handlingGetCenterOfMass ( handling theHandling )
float float float handlingGetCenterOfMass ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you wish to get the center of mass, *or*

- **int vehicleID:** the vehicle ID of which you want to get the center of mass.

### Returns

If you specified a handling element, returns the x, y and z components of the center of mass vector of the handling element if it is set, or *nil* if not. If you specified a vehicle ID, returns the x, y, and z components of the center of mass that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
