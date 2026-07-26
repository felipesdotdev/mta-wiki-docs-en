---
doc_id: "mta-wiki:3868"
title: "HandlingGetEngineInertia"
source_title: "HandlingGetEngineInertia"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetEngineInertia"
revision_id: 80935
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetEngineInertia

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the engine interia of a handling element or vehicle ID. A higher inertia makes a slower car.

## Syntax

```
float handlingGetEngineInertia ( handling theHandling )
float handlingGetEngineInertia ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the inertia, *or*

- **vehicleID:** the vehicle ID of which you want to get the inertia.

### Returns

If you specified a handling element, returns its inertia if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the inertia that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
