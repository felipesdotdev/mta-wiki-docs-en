---
doc_id: "mta-wiki:3867"
title: "HandlingGetEngineAcceleration"
source_title: "HandlingGetEngineAcceleration"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetEngineAcceleration"
revision_id: 80943
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetEngineAcceleration

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the acceleration of a handling element or vehicle ID.

## Syntax

```
float handlingGetEngineAcceleration ( handling theHandling )
float handlingGetEngineAcceleration ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the acceleration, *or*

- **vehicleID:** the vehicle ID of which you want to get the acceleration.

### Returns

If you specified a handling element, returns its acceleration if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the acceleration that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
