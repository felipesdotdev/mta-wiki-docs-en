---
doc_id: "mta-wiki:7195"
title: "BitExtract"
source_title: "BitExtract"
source_url: "https://wiki.multitheftauto.com/wiki/BitExtract"
revision_id: 72248
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
generated_at: "2026-07-26T16:11:51.071723+00:00"
---

# BitExtract

This function returns the unsigned number formed by the bits field to field + width - 1 (range: 0-31).

## Syntax

```
uint bitExtract ( uint var, int field [, int width = 1 ] )
```

### Required arguments

- **var:** The value

- **field:** The field number

- **width:** Number of bits to extract

### Returns

Returns the extracted value/bit sequence.

## Example

```
function getColorAlpha(color)
   return bitExtract(color,24,8) -- return bits 24-32 ( the alpha, http://en.wikipedia.org/wiki/RGBA_color_space ) 
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

- bitExtract

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
