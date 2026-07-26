---
doc_id: "mta-wiki:7096"
title: "BitTest"
source_title: "BitTest"
source_url: "https://wiki.multitheftauto.com/wiki/BitTest"
revision_id: 38870
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
---

# BitTest

This function performs an AND-conjunction on two or more (unsigned) 32-bit [integers](mta://reference/misc/int.md) and checks, whether the conjuncted value is zero or not. See [Bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#AND) for more details.

## Syntax

```
bool bitTest ( uint var1, uint var2, ... )
```

### Required arguments

- **varN:** The value you want to perform the operation on (see above)

### Returns

Returns *true* if the conjuncted value is **not** zero, *false* otherwise. If a bad argument was passed to bitTest, you'll get *nil*.

## Example

```
local flags = 0x23 -- binary: 100011b
local mask = 0x20  -- binary: 100000b

-- Check if bit 1 is set
if bitTest(flags, mask) then
    outputDebugString("Yeah. It's set")
else
    outputDebugString("I'm sorry ;(")
end
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- bitTest

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
