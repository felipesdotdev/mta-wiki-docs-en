---
doc_id: "mta-wiki:8530"
title: "Utf8.width"
source_title: "Utf8.width"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.width"
revision_id: 46687
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.447051+00:00"
---

# Utf8.width

Calculates the width of UTF-8 strings with special/unprintable characters, which require special width treatment.

## Syntax

```
int utf8.width ( string|int input [, bool ambi_is_double = false, int default_width = 0 ] )
```

### Required Arguments

- **input:** A string character sequence OR a codepoint integer

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **ambi_is_double:** A boolean, if set to *true*, ambiguous character's width is 2 (see example below).

- **default_width:** An integer, if given, is used as width for unprintable characters.

### Returns

Returns the *integer* width of the input string OR the width of the codepoint integer.

## Example

Click to collapse [-]
Server

This example shows the difference when *ambi_is_double* is set to *false* or *true*.

```
local input = "днём"
local disabled = utf8.width( input, false )
local enabled = utf8.width( input, true )

print( disabled, enabled ) -- 4, 8
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

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- utf8.width

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
