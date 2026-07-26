---
doc_id: "mta-wiki:7094"
title: "BitOr"
source_title: "BitOr"
source_url: "https://wiki.multitheftauto.com/wiki/BitOr"
revision_id: 46346
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
---

# BitOr

This function performs a bitwise OR-conjunction on two or more (unsigned) 32-bit [integers](mta://reference/misc/int.md). See [Bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#OR) for more details.

## Syntax

```
uint bitOr ( uint var1, uint var2, ... )
```

### Required arguments

- **varN:** The value you want to perform an OR-conjunction on

### Returns

Returns the conjuncted value.

## Example

This example will do a bitwise OR of x1, x2, ...

```
local x1 = 0x31 -- binary: 0011 0001
local x2 = 0x19 -- binary: 0001 1001

bitOr(x1, x2)   -- return  0011 1001
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- bitOr

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
