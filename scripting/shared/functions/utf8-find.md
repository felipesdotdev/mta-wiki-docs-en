---
doc_id: "mta-wiki:8515"
title: "Utf8.find"
source_title: "Utf8.find"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.find"
revision_id: 66932
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.114747+00:00"
---

# Utf8.find

Finds the first occurrence of the [pattern](http://lua-users.org/wiki/PatternsTutorial) in the string passed. If an instance of the pattern is found, a pair of values representing the start and the end of the matched string is returned.

## Syntax

```
int, int utf8.find ( string input, string pattern [, int startpos = 1, boolean plain = false ] )
```

### Required Arguments

- **input:** A string character sequence

- **pattern:** A string match [pattern](http://lua-users.org/wiki/PatternsTutorial) (you can disable pattern matching by using the optional fourth argument *plain*)

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **startpos:** An integer representing the beginning position.

- **plain:** A boolean, if pattern matching should be turned off

### Returns

Returns two *number* values for the beginning and ending position of the matched string, *nil* otherwise.

## Example

Click to collapse [-]
Server

This example shows how to search for parts of a string.

```
print( utf8.find( "Hello MTA User", "User" ) ) -- 11, 14
print( utf8.find( "Hello MTA User", "e" ) ) -- 2, 2
print( utf8.find( "Hello MTA User", "e", 3 ) ) -- 13, 13
print( utf8.find( "Привет Привет", "%s" ) ) -- 7, 7
print( utf8.find( "Привет Привет", "%s", 1, true ) ) -- nil

-- Comparsion of utf8.find and string.find
local startpos, endpos = utf8.find( "Привет", "и" )
print( startpos, endpos ) -- 3, 3

local startpos, endpos = string.find( "Привет", "и" )
print( startpos, endpos ) -- 5, 6
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- utf8.find

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
