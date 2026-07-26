---
doc_id: "mta-wiki:3866"
title: "HandlingGetTractionMultiplier"
source_title: "HandlingGetTractionMultiplier"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetTractionMultiplier"
revision_id: 16277
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:42.620568+00:00"
---

# HandlingGetTractionMultiplier

Returns the traction multiplier of a handling element or vehicle ID. Low values correspond to slippery tires, high values mean good grip.

## Syntax

```
float handlingGetTractionMultiplier ( handling theHandling )
float handlingGetTractionMultiplier ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the traction multiplier, *or*

- **vehicleID:** the vehicle ID of which you want to get the traction multiplier.

### Returns

If you specified a handling element, returns its traction multiplier if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the traction multiplier that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
