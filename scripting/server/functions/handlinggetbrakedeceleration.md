---
doc_id: "mta-wiki:3870"
title: "HandlingGetBrakeDeceleration"
source_title: "HandlingGetBrakeDeceleration"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetBrakeDeceleration"
revision_id: 80938
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
generated_at: "2026-07-26T16:15:42.405074+00:00"
---

# HandlingGetBrakeDeceleration

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the brake deceleration of a handling element or vehicle ID (how strongly the car can lock its tires while braking).

## Syntax

```
float handlingGetBrakeDeceleration ( handling theHandling )
float handlingGetBrakeDeceleration ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the brake deceleration, *or*

- **vehicleID:** the vehicle ID of which you want to get the brake deceleration.

### Returns

If you specified a handling element, returns its brake deceleration if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the brake deceleration that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
