---
doc_id: "mta-wiki:8538"
title: "BitRShift"
source_title: "BitRShift"
source_url: "https://wiki.multitheftauto.com/wiki/BitRShift"
revision_id: 46739
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:12:11.204366+00:00"
---

# BitRShift

This functions performs a logical right shift on the integer **value** by integer **n** positions. In a *logical shift*, zeros are shifted in to replace the discarded bits.
See [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation#Logical_shift) for more details.

## Syntax

```
int bitRShift ( int value, int n )
```

### Required arguments

- **value:** The value you want to perform the shift on.

- **n:** The amount of positions to shift the value by.

### Returns

Returns the logical right shifted value as *integer*.

## Example

This example shows the usage of the function bitRShift.

```
local value = 0xFFFFFFFF -- binary: 1111 1111 1111 1111 1111 1111 1111 1111, decimal: 4.294.967.295
local positions = 0x4 -- binary: 0100, decimal: 4
local shifted = bitRShift( value, positions ) -- binary: 0000 1111 1111 1111 1111 1111 1111 1111, decimal: 26.8435.455

-- Comparsion:
-- binary: 1111 1111 1111 1111 1111 1111 1111 1111, decimal: 4.294.967.295
-- binary: 0000 1111 1111 1111 1111 1111 1111 1111, decimal: 26.8435.455
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- bitRShift

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
