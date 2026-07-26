---
doc_id: "mta-wiki:7095"
title: "BitXor"
source_title: "BitXor"
source_url: "https://wiki.multitheftauto.com/wiki/BitXor"
revision_id: 46347
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
---

# BitXor

This function performs a bitwise XOR-conjunction (exclusive OR) on two or more (unsigned) 32-bit [integers](mta://reference/misc/int.md). See [Bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#XOR) for more details.

## Syntax

```
uint bitXor ( uint var1, uint var2, ... )
```

### Required arguments

- **varN:** The value you want to perform a XOR-conjunction on

### Returns

Returns the conjuncted value.

## Example

This example will do a bitwise XOR of x1, x2, ...

```
local x1 = 0x14 -- binary: 0001 0100
local x2 = 0x1C -- binary: 0001 1100

bitXor(x1, x2)  -- return  0000 1000
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- bitXor

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
