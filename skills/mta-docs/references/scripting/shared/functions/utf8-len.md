---
doc_id: "mta-wiki:8520"
title: "Utf8.len"
source_title: "Utf8.len"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.len"
revision_id: 47536
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
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

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

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

- [utf8.byte](https://wiki.multitheftauto.com/index.php?search=utf8.byte)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](https://wiki.multitheftauto.com/index.php?search=utf8.charpos)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](https://wiki.multitheftauto.com/index.php?search=utf8.find)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- [utf8.gmatch](https://wiki.multitheftauto.com/index.php?search=utf8.gmatch)

- [utf8.gsub](mta://scripting/shared/functions/utf8-gsub.md)

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- utf8.len

- [utf8.lower](https://wiki.multitheftauto.com/index.php?search=utf8.lower)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](https://wiki.multitheftauto.com/index.php?search=utf8.next)

- [utf8.remove](https://wiki.multitheftauto.com/index.php?search=utf8.remove)

- [utf8.reverse](https://wiki.multitheftauto.com/index.php?search=utf8.reverse)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](https://wiki.multitheftauto.com/index.php?search=utf8.upper)

- [utf8.width](https://wiki.multitheftauto.com/index.php?search=utf8.width)

- [utf8.widthindex](https://wiki.multitheftauto.com/index.php?search=utf8.widthindex)
