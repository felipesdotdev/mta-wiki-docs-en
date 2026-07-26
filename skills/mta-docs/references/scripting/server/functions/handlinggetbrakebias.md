---
doc_id: "mta-wiki:3871"
title: "HandlingGetBrakeBias"
source_title: "HandlingGetBrakeBias"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetBrakeBias"
revision_id: 82304
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetBrakeBias

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the brake bias of a handling element or vehicle ID (the distribution of the braking power over the front and back tires).

## Syntax

```
float handlingGetBrakeBias ( handling theHandling )
float handlingGetBrakeBias ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the brake bias, *or*

- **vehicleID:** the vehicle ID of which you want to get the brake bias.

### Returns

If you specified a handling element, returns its brake bias if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the brake bias that currently applies to vehicles of that ID. Returns *false* in case of failure.

The brake bias is a value between 0 and 1. 0 means the car only brakes on its back tires, 1 that it only brakes on the front tires. 0.5 means that front and back tires brake with the same strength.

## See Also
