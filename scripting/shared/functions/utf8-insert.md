---
doc_id: "mta-wiki:8519"
title: "Utf8.insert"
source_title: "Utf8.insert"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.insert"
revision_id: 46678
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:02.206561+00:00"
---

# Utf8.insert

Inserts a substring into input string. If insert-position is given, the substring will be inserted before the character at this index, otherwise the substring will concatenate to input. The insert position may be negative.

## Syntax

```
string utf8.insert ( string input [, int insert_pos = utf8.len( input ) + 1 ], string substring )
```

### Required Arguments

- **input:** A string character sequence

- **substring:** A string character sequence which should be inserted

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **insert_pos:** An integer representing the position, where the substring will be inserted at.

### Returns

Returns a *string* with the inserted substring value.

## Example

Click to collapse [-]
Server

This example shows a command handler for '/insert [something]', which will concatenate the '[something]' after the 'hello ' string in 2 ways.

```
addCommandHandler("insert", 
    function (player, command, word)
        if word then
            local output = utf8.insert( "hello ", word )
            outputChatBox( output, player )
            
            local output = utf8.insert( "hello ", utf8.len( "hello " ) + 1, word )
            outputChatBox( output, player )
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

- utf8.insert

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
