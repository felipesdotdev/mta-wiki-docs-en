---
doc_id: "mta-wiki:3873"
title: "HandlingGetSteeringLock"
source_title: "HandlingGetSteeringLock"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSteeringLock"
revision_id: 80933
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetSteeringLock

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the steering lock of a handling element or vehicle ID (how strongly the car can steer).

## Syntax

```
float handlingGetSteeringLock ( handling theHandling )
float handlingGetSteeringLock ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the steering lock, *or*

- **vehicleID:** the vehicle ID of which you want to get the steering lock.

### Returns

If you specified a handling element, returns its steering lock if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the steering lock that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
