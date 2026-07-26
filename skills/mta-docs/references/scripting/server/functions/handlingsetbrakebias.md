---
doc_id: "mta-wiki:3893"
title: "HandlingSetBrakeBias"
source_title: "HandlingSetBrakeBias"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingSetBrakeBias"
revision_id: 80954
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingSetBrakeBias

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setVehicleHandling instead. |  |

Sets the brake bias of a handling element. This determines how the braking power is distributed over the wheels.

## Syntax

```
bool handlingSetBrakeBias ( handling theHandling, float bias )
```

### Required Arguments

- **theHandling:** the handling of which you want to change the brake bias.

- **bias:** the bias to set. This is a value between 0 and 1. A value of 0 will put all the braking power in the rear wheels, and the front wheels will not brake at all. A value of 1 has only the front wheels brake. With a bias of 0.5, front and back wheels have the same braking power.

### Returns

Returns *true* on success, *false* in case of failure.

## Example

```
--TODO
```

## See Also
