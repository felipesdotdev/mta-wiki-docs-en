---
doc_id: "mta-wiki:3880"
title: "HandlingGetSuspensionLowerLimit"
source_title: "HandlingGetSuspensionLowerLimit"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingGetSuspensionLowerLimit"
revision_id: 16303
language: "en"
categories: ["Server_functions"]
---

# HandlingGetSuspensionLowerLimit

Returns the suspension lower limit of a handling element or vehicle ID (how low the wheels can go).

## Syntax

```
float handlingGetSuspensionLowerLimit ( handling theHandling )
float handlingGetSuspensionLowerLimit ( int vehicleID )
```

### Required Arguments

- **theHandling:** the handling of which you want to get the suspension lower limit, *or*

- **vehicleID:** the vehicle ID of which you want to get the suspension lower limit.

### Returns

If you specified a handling element, returns its suspension lower limit if one is set, or *nil* otherwise. If you specified a vehicle ID, returns the suspension lower limit that currently applies to vehicles of that ID. Returns *false* in case of failure.

## Example

```
--TODO
```

## See Also
