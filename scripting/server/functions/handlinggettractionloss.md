---
doc_id: "mta-wiki:3874"
title: "HandlingGetTractionLoss"
source_title: "HandlingGetTractionLoss"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetTractionLoss"
revision_id: 16296
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:42.614010+00:00"
---

# HandlingGetTractionLoss

Returns the traction loss of a handling element or vehicle ID. This value determines how much grip the car has on the road (higher number = more grip).

## Syntax

```
float handlingGetTractionLoss ( handling theHandling )
float handlingGetTractionLoss ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the traction loss, *or*

- **vehicleID:** the vehicle ID of which you want to get the traction loss.

### Returns

If you specified a handling element, returns its traction loss if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the traction loss that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
