---
doc_id: "mta-wiki:8511"
title: "Utf8.byte"
source_title: "Utf8.byte"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.byte"
revision_id: 46668
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# Utf8.byte

Returns the codepoints for the i-th through j-th character of the string passed.

## Syntax

```lua
int,... utf8.byte ( string input [, int i=1, int j=1 ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/wiki/Optional_arguments).

- **i:** An integer representing the beginning position.

- **j:** An integer representing the ending position.

### Returns

Returns a sequence of *integer* values from the original string if successful, *nil* otherwise.

## Example

Click to collapse [-]
Server

This example will print every codepoint in the input string to the server console.

```lua
local input = "Ницца!"
local codepoints = { utf8.byte( input, 1, utf8.len(input) ) }

for index, codepoint in ipairs( codepoints ) do
    print( "Codepoint @ ".. index .." = ".. codepoint )
end
```

Output:

```lua
Codepoint @ 1 = 1053
Codepoint @ 2 = 1080
Codepoint @ 3 = 1094
Codepoint @ 4 = 1094
Codepoint @ 5 = 1072
Codepoint @ 6 = 33
```

Click to collapse [-]
Client

This example will print the codepoint of the first character (read: 'M') in the string literal.

```lua
local first = utf8.byte( "Multi Theft Auto", 1, 1 )
outputConsole( first ) -- 77
```

## See Also

- utf8.byte

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

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
