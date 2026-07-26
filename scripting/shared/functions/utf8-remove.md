---
doc_id: "mta-wiki:8527"
title: "Utf8.remove"
source_title: "Utf8.remove"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.remove"
revision_id: 47958
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.343775+00:00"
---

# Utf8.remove

This function removes a substring in a UTF-8 string by using a position range.

## Syntax

```
string utf8.remove ( string input, int start = 1 [, int stop = -1 ] )
```

### Required Arguments

- **input:** A string character sequence

- **start:** An integer representing the beginning position.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **stop:** An integer representing the ending position.

### Returns

Returns the *string* with the removed substring from the range.

## Example

Click to collapse [-]
Server

This example shows how to remove substrings from strings.

```
-- Keep the first and last character
local input = "яблоко"
local output = utf8.remove( input, 2, -2 ) 
print( output ) -- яо

-- Remove the last character
local input = "Банан"
local output = utf8.remove( input, -1, -1 )
print( output ) -- Бана
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

- utf8.remove

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
