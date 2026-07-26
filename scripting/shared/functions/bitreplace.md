---
doc_id: "mta-wiki:7286"
title: "BitReplace"
source_title: "BitReplace"
source_url: "https://wiki.multitheftauto.com/wiki/BitReplace"
revision_id: 71557
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2", "Utility_templates"]
generated_at: "2026-07-26T16:11:53.788166+00:00"
---

# BitReplace

This function returns the unsigned number formed by var value with replacement specified at bits field to field + width - 1

## Syntax

```
uint bitReplace(uint var, uint replaceValue, int field [, int width = 1])
```

### Required arguments

- **var:** The value

- **replaceValue:** The replaceValue

- **field:** The field number

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **width:** Number of bits to extract

### Returns

Returns the replaced value/bit sequence.

## Example

```
function replaceColorAlpha(color, alpha)
   return bitReplace(color,alpha,24,8) -- return value with replaced bits 24-32 ( the alpha, http://en.wikipedia.org/wiki/RGBA_color_space ) 
end
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

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- bitReplace
