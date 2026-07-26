---
doc_id: "mta-wiki:8524"
title: "Utf8.match"
source_title: "Utf8.match"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.match"
revision_id: 46680
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.268837+00:00"
---

# Utf8.match

Extract substrings by matching patterns in the input string. This function can be used to extract specific information from a string.

## Syntax

```
string,... utf8.match ( string input, string pattern [, int index = 1 ] )
```

### Required Arguments

- **input:** A string character sequence

- **pattern:** A string match [pattern](http://lua-users.org/wiki/PatternsTutorial)

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **index:** An integer representing the beginning position for the pattern matching

### Returns

Returns a sequence of *string* matches from the **input** string, *nil* otherwise.

## Example

Click to collapse [-]
Server

This example shows how to extract values from an input string by using a pattern to match the value parts.

```
local input = "Level: 5, Rank: General, 128.42 points"
local level, rank, points = utf8.match( input, "Level: (%d+), Rank: (.-), (%d+.?%d*) points" )
level, points = tonumber( level ), tonumber( points )

print( level, rank, points ) -- 5, General, 128.42
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

- utf8.match

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
