---
doc_id: "mta-wiki:3882"
title: "HandlingGetSuspensionAntidiveMultiplier"
source_title: "HandlingGetSuspensionAntidiveMultiplier"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSuspensionAntidiveMultiplier"
revision_id: 40328
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:42.545456+00:00"
---

# HandlingGetSuspensionAntidiveMultiplier

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVehicleHandling instead. You can also use getModelHandling to retrieve the handling data per model. |  |

Returns the suspension antidive multiplier of a handling element or vehicle ID.

## Syntax

```
float handlingGetSuspensionAntidiveMultiplier ( handling theHandling )
float handlingGetSuspensionAntidiveMultiplier ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the suspension antidive multiplier, *or*

- **vehicleID:** the vehicle ID of which you want to get the suspension antidive multiplier.

### Returns

If you specified a handling element, returns its suspension antidive multiplier if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the antidive multiplier that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
