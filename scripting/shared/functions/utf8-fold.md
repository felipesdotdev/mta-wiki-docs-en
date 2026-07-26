---
doc_id: "mta-wiki:8516"
title: "Utf8.fold"
source_title: "Utf8.fold"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.fold"
revision_id: 70960
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:02.133895+00:00"
---

# Utf8.fold

| [[{{{image}}}\|link=\|]] | Note: You may want to read up on case folding for more information about the use of this function. |
| --- | --- |
|  |  |

Converts a UTF-8 string to folded case (lowercase), which can be used to compare two strings. If *input* is an integer, it's treat as a codepoint and a convert codepoint (integer) is returned.

## Syntax

```
string|int utf8.fold ( string|int input )
```

```
string|int utf8.lower ( string|int input )
```

### Required Arguments

- **input:** A string character sequence OR an integer value

### Returns

Returns a *string* in lowercase OR returns an *integer* (see description).

## Example

Click to collapse [-]
Server

This example shows how to convert a string to lowercase, which can be used to compare with other folded strings.

```
local output = utf8.lower( "WHAT ARE YOU UP TO? Do you like uppercase?" )
print( output ) -- what are you up to? do you like uppercase?

local value = utf8.fold( 1088 )
print( type( value ) ) -- number
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](mta://scripting/shared/functions/utf8-find.md)

- utf8.fold

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
