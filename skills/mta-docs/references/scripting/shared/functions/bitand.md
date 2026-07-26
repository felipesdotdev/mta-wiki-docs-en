---
doc_id: "mta-wiki:7091"
title: "BitAnd"
source_title: "BitAnd"
source_url: "https://wiki.multitheftauto.com/wiki/BitAnd"
revision_id: 81434
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
---

# BitAnd

This function performs a bitwise AND-conjunction on two or more (unsigned) 32-bit [integers](mta://reference/misc/int.md). See [Bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#AND) for more details.

## Syntax

```
uint bitAnd ( uint var1, uint var2, ... )
```

### Required arguments

- **varN:** The value you want to perform an AND-conjunction on

### Returns

Returns the conjuncted value.

## Example

```
local flags = 0x23 -- binary: 100011b
local mask = 0x20  -- binary: 100000b

-- Check if bit 1 is set
if bitAnd(flags, mask) ~= 0 then
    outputDebugString("Yeah. It's set")
else
    outputDebugString("I'm sorry ;(")
end
```

To test if a flag is set or not it's easier using [bitTest](mta://scripting/shared/functions/bittest.md).

## See Also

- bitAnd

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
