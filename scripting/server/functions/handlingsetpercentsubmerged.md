---
doc_id: "mta-wiki:3934"
title: "HandlingSetPercentSubmerged"
source_title: "HandlingSetPercentSubmerged"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingSetPercentSubmerged"
revision_id: 82380
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated"]
generated_at: "2026-07-26T16:15:42.769809+00:00"
---

# HandlingSetPercentSubmerged

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Sets what percentage of the vehicle will be submerged if it enters water. A percentage of 0 means that it will stand on top of the water surface, a value of 100 means that it will immediately sink.

## Syntax

```
bool handlingSetPercentSubmerged ( handling theHandling, float percentage )
```

### Required Arguments

- **theHandling:** the handling of which you want to change the submersion percentage.

- **percentage:** the submersion percentage, a value from 0-100.

### Returns

Returns *true* on success, *false* in case of failure.

## Example

```
--TODO
```

## See Also
