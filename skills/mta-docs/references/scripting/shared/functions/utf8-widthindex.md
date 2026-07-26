---
doc_id: "mta-wiki:8531"
title: "Utf8.widthindex"
source_title: "Utf8.widthindex"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.widthindex"
revision_id: 69055
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# Utf8.widthindex

Returns the location, offset and width of the character at the given location in the UTF-8 string.

## Syntax

```lua
int, int, int utf8.widthindex ( string input, int location [, bool ambi_is_double = false, int default_width = 0 ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/wiki/Optional_arguments).

- **ambi_is_double:** A boolean, if set to *true*, ambiguous character's width is 2 (see example).

- **default_width:** An integer, if given, is used as width for unprintable characters.

### Returns

Returns the given location, the offset in UTF-8 encoding (if cursor is in the middle of the wide char - offset will be 2) and the width of the character, otherwise only the location as *integer* will be returned.

## Example

Click to collapse [-]
Server

This example

```lua
local input = "днём"
local raw_width = utf8.width( input, true )

for location = 1, raw_width do
    print( utf8.widthindex( input, location, true ) )
end
```

Output *(enhanced, not raw)*:

| Character | Location | Offset | Width |
| --- | --- | --- | --- |
| д | 1 | 1 | 2 |
| д | 1 | 2 | 2 |
| н | 2 | 1 | 2 |
| н | 2 | 2 | 2 |
| ё | 3 | 1 | 2 |
| ё | 3 | 2 | 2 |
| м | 4 | 1 | 2 |
| м | 4 | 2 | 2 |

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](mta://scripting/shared/functions/utf8-find.md)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- [utf8.gmatch](mta://scripting/shared/functions/utf8-gmatch.md)

- [utf8.gsub](mta://scripting/shared/functions/utf8-gsub.md)

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](https://wiki.multitheftauto.com/wiki/Utf8.lower)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](https://wiki.multitheftauto.com/wiki/Utf8.upper)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- utf8.widthindex
