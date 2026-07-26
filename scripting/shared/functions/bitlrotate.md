---
doc_id: "mta-wiki:8535"
title: "BitLRotate"
source_title: "BitLRotate"
source_url: "https://wiki.multitheftauto.com/wiki/BitLRotate"
revision_id: 46733
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:12:11.169976+00:00"
---

# BitLRotate

This functions performs a bitwise circular left-rotation on the integer **value** by integer **n** positions.
See [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation#Rotate_no_carry) for more details.

## Syntax

```
int bitLRotate ( int value, int n )
```

### Required arguments

- **value:** The value you want to perform the rotation on.

- **n:** The amount of positions to rotate the value by.

### Returns

Returns the circular left-rotated value as *integer*.

## Example

This example shows the usage of the function bitLRotate.

```
local value = 0xF -- binary: 1111, decimal: 15
local positions = 0x1 -- binary: 0001, decimal: 1
local shifted = bitLRotate( value, positions ) -- binary: 0001 1110, decimal: 30

local value = 0xF -- binary: 1111, decimal: 15
local positions = 0x3 -- binary: 0011, decimal: 3
local shifted = bitLRotate( value, positions ) -- binary: 0111 1000, decimal: 120

local value = 0x3F -- binary: 0011 1111, decimal: 63
local positions = 0xA -- binary: 1010, decimal: 10
local shifted = bitLRotate( value, positions ) -- binary: 1111 1100 0000 0000, decimal: 64.512
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- bitLRotate

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
