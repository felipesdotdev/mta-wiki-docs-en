---
doc_id: "mta-wiki:3879"
title: "HandlingGetSuspensionUpperLimit"
source_title: "HandlingGetSuspensionUpperLimit"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSuspensionUpperLimit"
revision_id: 16302
language: "en"
categories: ["Server_functions"]
---

# HandlingGetSuspensionUpperLimit

Returns the suspension upper limit of a handling element or vehicle ID (how high the wheels can go).

## Syntax

```
float handlingGetSuspensionUpperLimit ( handling theHandling )
float handlingGetSuspensionUpperLimit ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the suspension upper limit, *or*

- **vehicleID:** the vehicle ID of which you want to get the suspension upper limit.

### Returns

If you specified a handling element, returns its suspension upper limit if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the suspension upper limit that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
