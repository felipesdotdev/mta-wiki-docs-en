---
doc_id: "mta-wiki:8520"
title: "Utf8.len"
source_title: "Utf8.len"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.len"
revision_id: 47536
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.227836+00:00"
---

# Utf8.len

Returns the length of the string passed.

## Syntax

```
int utf8.len ( string input [, int i = 1, int j = utf8.len( input ) ] )
```

### Required Arguments

- **input:** A string character sequence

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **i:** An integer representing the beginning position for measuring the length of the section (may be negative).

- **j:** An integer representing the ending position for measuring the length of the section (may be negative).

### Returns

Returns the length of the string as an *integer*.

## Example

Click to collapse [-]
Client

This example calculates the length of the input of the command /length and shows it in the chatbox.

```
addCommandHandler("length", 
    function (command, ...)
        local input = table.concat({...}, " ")

        if input then
            local length = utf8.len( input )
            outputChatBox( "* Length of your input: ".. length )
        end
    end
)
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

- utf8.len

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
