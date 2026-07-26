---
doc_id: "mta-wiki:8514"
title: "Utf8.escape"
source_title: "Utf8.escape"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.escape"
revision_id: 46674
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:02.093289+00:00"
---

# Utf8.escape

Escapes a string to a UTF-8 format string. It supports several escape formats, see the formatting table.

## Syntax

```
string utf8.escape ( string input )
```

### Required Arguments

- **input:** A string character sequence

### Returns

Returns a *string* containing the escaped UTF-8 characters from the original string.

### Formatting

| Format | Description |
| --- | --- |
| %ddd | ddd is a decimal number with variable length |
| %{ddd} | same as above, but enclosed in brackets |
| %uddd | same as %ddd , 'u' stands for unicode |
| %u{ddd} | same as above, but enclosed in brackets |
| %xhhh | hexadigit version of %ddd |
| %x{hhh} | same as above, but enclosed in brackets |
| %? | '?' stands for any other character to be escaped |

## Example

Click to collapse [-]
Server

This example escapes two byte-string literals to UTF-8 format by using the utf8.escape function.

```
local output = utf8.escape( "%123 %u123 %{123} %u{123} %xABC %x{ABC}" )
print( output ) -- { { { { ઼ ઼

local output = utf8.escape( "%%123 %? %d %%u" )
print( output ) -- %123 ? d %u
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- utf8.escape

- [utf8.find](mta://scripting/shared/functions/utf8-find.md)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- [utf8.gmatch](mta://scripting/shared/functions/utf8-gmatch.md)

- [utf8.gsub](mta://scripting/shared/functions/utf8-gsub.md)

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](mta://scripting/shared/functions/utf8-lower.md)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
