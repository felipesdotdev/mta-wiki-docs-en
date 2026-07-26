---
doc_id: "mta-wiki:3872"
title: "HandlingGetABS"
source_title: "HandlingGetABS"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetABS"
revision_id: 80934
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetABS

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the ABS (Anti-lock Braking System) setting of a handling element or vehicle ID.

## Syntax

```
bool handlingGetABS ( handling theHandling )
bool handlingGetABS ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the ABS setting, *or*

- **vehicleID:** the vehicle ID of which you want to get the ABS setting.

### Returns

If you specified a handling element, returns its ABS setting if one is set (*true* if ABS is active, *false* if not), or *nil* otherwise. If you specified a vehicle ID, returns the ABS setting that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
