---
doc_id: "mta-wiki:3930"
title: "HandlingGetDriveType"
source_title: "HandlingGetDriveType"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetDriveType"
revision_id: 80942
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
generated_at: "2026-07-26T16:15:42.462679+00:00"
---

# HandlingGetDriveType

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the drive type of a handling element or vehicle ID.

## Syntax

```
string handlingGetDriveType ( handling theHandling )
string handlingGetDriveType ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the drive type, *or*

- **vehicleID:** the vehicle ID of which you want to get the drive type.

### Returns

If you specified a handling element, returns its drive type if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the drive type that currently applies to vehicles of that ID. Returns *false* in case of failure.

Possible drive types are:

- **fwd:** car is front wheel driven

- **rwd:** car is rear wheel driven

- **awd:** car is all wheel driven

## Example

```
--TODO
```

## See Also
