---
doc_id: "mta-wiki:3881"
title: "HandlingGetSuspensionFrontRearBias"
source_title: "HandlingGetSuspensionFrontRearBias"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSuspensionFrontRearBias"
revision_id: 82306
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated"]
generated_at: "2026-07-26T16:15:42.572325+00:00"
---

# HandlingGetSuspensionFrontRearBias

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the suspension bias of a handling element or vehicle ID.

## Syntax

```
float handlingGetSuspensionFrontRearBias ( handling theHandling )
float handlingGetSuspensionFrontRearBias ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the suspension bias, *or*

- **vehicleID:** the vehicle ID of which you want to get the suspension bias.

### Returns

If you specified a handling element, returns its suspension bias if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the suspension bias that currently applies to vehicles of that ID. Returns *false* in case of failure.

The suspension bias is a number between 0 and 1. If it's 0, the back tires have all the suspension and the front tires have none. If it's 1, the front tires have suspension and the back tires have none. If it's 0.5, front and back tires have the same suspension strength.

## Example

```
--TODO
```

## See Also
