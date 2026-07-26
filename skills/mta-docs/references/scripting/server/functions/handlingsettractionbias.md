---
doc_id: "mta-wiki:3897"
title: "HandlingSetTractionBias"
source_title: "HandlingSetTractionBias"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingSetTractionBias"
revision_id: 16328
language: "en"
categories: ["Server_functions"]
---

# HandlingSetTractionBias

Sets the traction bias of a handling element. This determines how the grip is distributed over the wheels.

## Syntax

```
bool handlingSetTractionBias ( handling theHandling, float bias )
```

### Required Arguments

- **theHandling:** the handling of which you want to change the traction bias.

- **bias:** the traction bias to set. This is a value between 0 and 1. If it's 0, the rear wheels have all the grip and the front wheels have no grip at all. If it's 1, the front wheels have grip and the rear wheels don't. A value of 0.5 gives front and rear wheels the same amount of grip.

### Returns

Returns *true* on success, *false* in case of failure.

## Example

```
--TODO
```

## See Also
