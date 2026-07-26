---
doc_id: "mta-wiki:8526"
title: "Utf8.next"
source_title: "Utf8.next"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.next"
revision_id: 46682
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.322990+00:00"
---

# Utf8.next

This is an iteration function to traverse each single codepoint of a UTF-8 string.

## Syntax

```
int, int utf8.next ( string input [[, int charpos = 0 ], int offset = 1 ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **charpos:** An integer representing the beginning position (offset will be added/subtracted).

- **offset:** An integer representing the offset to charpos.

### Returns

Returns the *integer* position in bytes and the *integer* codepoint at this position, *nil* otherwise.

## Example

Click to collapse [-]
Server

This example shows how to traverse a UTF-8 string the proper way without running into problems as in byte strings.

```
for position, codepoint in utf8.next, "utf8-string" do
    print( "Codepoint @ ".. position .." = ".. codepoint )
end

for position, codepoint in utf8.next, "Как" do
    print( "Codepoint @ ".. position .." = ".. codepoint )
end
```

Output:

```
// 1st iteration
Codepoint @ 1 = 117
Codepoint @ 2 = 116
Codepoint @ 3 = 102
Codepoint @ 4 = 56
Codepoint @ 5 = 45
Codepoint @ 6 = 115
Codepoint @ 7 = 116
Codepoint @ 8 = 114
Codepoint @ 9 = 105
Codepoint @ 10 = 110
Codepoint @ 11 = 103

// 2nd iteration
Codepoint @ 1 = 1050
Codepoint @ 3 = 1072
Codepoint @ 5 = 1082
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

- utf8.next

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
