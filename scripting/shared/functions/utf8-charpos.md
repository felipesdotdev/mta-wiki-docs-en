---
doc_id: "mta-wiki:8513"
title: "Utf8.charpos"
source_title: "Utf8.charpos"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.charpos"
revision_id: 46671
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.072964+00:00"
---

# Utf8.charpos

Converts the UTF-8 codepoint position to byte-string position.

| [[{{{image}}}\|link=\|]] | Note: Code point characters beyond the byte value range (0-127) require at least 2 bytes to represent the character |
| --- | --- |
|  |  |

## Syntax

```
int, int utf8.charpos ( string input [[, int charpos = 0 ], int offset = 1 ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **charpos:** An integer representing the beginning position (offset will be added/subtracted).

- **offset:** An integer representing the offset to charpos.

### Returns

Returns the *integer* position as in a byte string and the *integer* codepoint at this position, *nil* otherwise.

## Example

Click to collapse [-]
Server

This example takes the second codepoint character and shows the byte-string position and the codepoint character code.

```
local position, codepoint = utf8.charpos( "Привет", 2 )
print( position, codepoint )  -- 3, 1088
```

Click to collapse [-]
Client

This example extracts the first character by calculating the character length with the UTF8 functions and the inbuilt Lua function string.sub, which processes byte strings.

```
local input = "Привет мир" -- Hello World
local from = utf8.charpos( input, 1 ) -- 1
local to = utf8.charpos( input, 2 ) -- 3

local byteLength = to - from
outputConsole( byteLength ) -- 2

local character = string.sub( input, from, byteLength )
outputConsole( character ) -- П
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- utf8.charpos

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

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
