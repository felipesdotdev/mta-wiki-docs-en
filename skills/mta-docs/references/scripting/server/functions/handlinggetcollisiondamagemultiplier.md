---
doc_id: "mta-wiki:3883"
title: "HandlingGetCollisionDamageMultiplier"
source_title: "HandlingGetCollisionDamageMultiplier"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetCollisionDamageMultiplier"
revision_id: 80940
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingGetCollisionDamageMultiplier

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. |  |

Returns the collision damage multiplier of a handling element or vehicle ID. The higher the value, the more sensitive the vehicle is to collisions.

## Syntax

```
float handlingGetCollisionDamageMultiplier ( handling theHandling )
float handlingGetCollisionDamageMultiplier ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the collision damage multiplier, *or*

- **vehicleID:** the vehicle ID of which you want to get the collision damage multiplier.

### Returns

If you specified a handling element, returns its collision damage multiplier if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the collision multiplier that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
