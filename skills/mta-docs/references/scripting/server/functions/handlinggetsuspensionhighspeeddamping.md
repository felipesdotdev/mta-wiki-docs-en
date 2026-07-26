---
doc_id: "mta-wiki:3878"
title: "HandlingGetSuspensionHighSpeedDamping"
source_title: "HandlingGetSuspensionHighSpeedDamping"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSuspensionHighSpeedDamping"
revision_id: 16301
language: "en"
categories: ["Server_functions"]
---

# HandlingGetSuspensionHighSpeedDamping

Returns the high speed suspension damping strength of a handling element or vehicle ID.

## Syntax

```
float handlingGetSuspensionHighSpeedDamping ( handling theHandling )
float handlingGetSuspensionHighSpeedDamping ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the high speed suspension damping strength, *or*

- **vehicleID:** the vehicle ID of which you want to get the high speed suspension damping strength.

### Returns

If you specified a handling element, returns its high speed suspension damping if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the high speed suspension damping that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
