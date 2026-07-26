---
doc_id: "mta-wiki:10372"
title: "ExtinguishFire"
source_title: "ExtinguishFire"
source_url: "https://wiki.multitheftauto.com/wiki/ExtinguishFire"
revision_id: 57142
language: "en"
categories: ["Client_functions", "Changes_in_1.5.5"]
---

# ExtinguishFire

This function is used to extinguish all spreading fire, or spreading fire at specified coordinates.

## Syntax

```
bool extinguishFire ( [ float x, float y, float z [, float radius = 1.0 ] ] )
```

### Optional Arguments

- **x, y, z:** the coordinates at which any fire will be extinguished.

- **radius:** a [float](mta://reference/misc/float.md) value indicating the radius in which to extinguish fire.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This example creates 10 fires and then instantly extinguishes them.

```
local start = {0, 0, 4}

for i = 1, 10 do
    createFire(start[1] + i, start[2], start[3])
end

extinguishFire(start[1], start[2], start[3], 10)
```

## See Also

- [createFire](mta://scripting/client/functions/createfire.md)

- extinguishFire
