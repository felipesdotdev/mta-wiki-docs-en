---
doc_id: "mta-wiki:8512"
title: "Utf8.char"
source_title: "Utf8.char"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.char"
revision_id: 46667
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.049024+00:00"
---

# Utf8.char

Generates a string representing the character codepoints as arguments.

## Syntax

```
string utf8.char ( [ int codepoints... ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **codepoints:** An variable argument sequence of code points representing the desired unicode characters.

### Returns

Returns a *string* representation of the codepoints passed.

## Example

Click to collapse [-]
Server

This example separates an input string into single codepoints and then joins these back together, representing the original input string.

```
local input = "Hello World"
local codepoints = { utf8.byte( input, 1, utf8.len(input) ) }
local joined = utf8.char( unpack(codepoints) )

print( joined ) -- Hello World
```

Click to collapse [-]
Server

This example takes three code points to generate the string "MTA".

```
local mta = utf8.char( 77, 84, 65 )
print( mta ) -- MTA
```

Click to collapse [-]
Client

This example takes the first five code points from the input string and then joins them back together.

```
local input = "Mutli Theft Auto"
local codepoints = {}

-- Extract first 5 characters (read: Mutli)
for index = 1, 5 do
    codepoints[index] = utf8.byte( input, index )
end

local output = ""

-- Join the first 5 characters together
for index = 1, #codepoints do
    output = output .. utf8.char( codepoints[index] )
end

outputConsole( output ) -- Multi
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- utf8.char

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

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
