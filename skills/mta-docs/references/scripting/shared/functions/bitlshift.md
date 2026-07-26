---
doc_id: "mta-wiki:8537"
title: "BitLShift"
source_title: "BitLShift"
source_url: "https://wiki.multitheftauto.com/wiki/BitLShift"
revision_id: 46740
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# BitLShift

This functions performs a logical left shift on the integer **value** by integer **n** positions. In a *logical shift*, zeros are shifted in to replace the discarded bits.
See [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation#Logical_shift) for more details.

## Syntax

```
int bitLShift ( int value, int n )
```

### Required arguments

- **value:** The value you want to perform the shift on.

- **n:** The amount of positions to shift the value by.

### Returns

Returns the logical left shifted value as *integer*.

## Example

This example shows the usage of the function bitLShift.

```
local value = 0xFFFFFFFF -- binary: 1111 1111 1111 1111 1111 1111 1111 1111, decimal: 4.294.967.295
local positions = 0x4 -- binary: 0100, decimal: 4
local shifted = bitLShift( value, positions ) -- binary: 1111 1111 1111 1111 1111 1111 1111 0000, decimal: 4.294.967.280

-- Comparsion:
-- binary: 1111 1111 1111 1111 1111 1111 1111 1111, decimal: 4.294.967.295
-- binary: 1111 1111 1111 1111 1111 1111 1111 0000, decimal: 4.294.967.280
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- bitLShift

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
