---
doc_id: "mta-wiki:3869"
title: "HandlingGetMaxVelocity"
source_title: "HandlingGetMaxVelocity"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetMaxVelocity"
revision_id: 80952
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetMaxVelocity

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the maximum velocity of a handling element or vehicle ID.

## Syntax

```
float handlingGetMaxVelocity ( handling theHandling )
float handlingGetMaxVelocity ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the maximum velocity, *or*

- **vehicleID:** the vehicle ID of which you want to get the maximum velocity.

### Returns

If you specified a handling element, returns its maximum velocity if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the maximum velocity that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
