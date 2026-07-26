---
doc_id: "mta-wiki:8529"
title: "Utf8.sub"
source_title: "Utf8.sub"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.sub"
revision_id: 50962
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.380201+00:00"
---

# Utf8.sub

Returns a substring of the string passed. The substring starts at *i*. If the third argument *j* is not given, the substring will end at the end of the string. If the third argument is given, the substring ends at and includes *j*.

## Syntax

```
string utf8.sub ( string input [, int i = 1, int j = utf8.len( input ) ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **i:** An integer representing the beginning position (may be negative).

- **j:** An integer representing the ending position (may be negative).

### Returns

Returns a *string* substring of the original string, containing the selected range from the original string.

## Example

Click to collapse [-]
Client

This example shows how to extract a substring from a UTF-8 string.

```
local input = "Yarın Salı"

local output = utf8.sub( input, 1, 4 )
outputConsole( output ) -- Yarı

local output = utf8.sub( input, -4 )
outputConsole( output ) -- Salı

local output = utf8.sub( input, -4, -1 )
outputConsole( output ) -- Salı
```

Click to collapse [-]
Server

```
local input = "Happy Now"

local output = utf8.sub( input, 1, 5 )
outputChatBox( output, root, 255,255,255,true ) -- Happy

local output = utf8.sub( input, -3 )
outputChatBox( output, root, 255,255,255,true ) -- Now

local output = utf8.sub( input, -3, -1 )
outputChatBox( output, root, 255,255,255,true ) -- Now
```

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

- [utf8.lower](mta://scripting/shared/functions/utf8-lower.md)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- utf8.sub

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
