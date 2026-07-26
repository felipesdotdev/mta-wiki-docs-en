---
doc_id: "mta-wiki:8525"
title: "Utf8.ncasecmp"
source_title: "Utf8.ncasecmp"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.ncasecmp"
revision_id: 46681
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:02.298202+00:00"
---

# Utf8.ncasecmp

Compares two strings in lower-case and returns the difference indicator (see table below) as an integer value.

## Syntax

```
int utf8.ncasecmp ( string a, string b )
```

### Required Arguments

- **a:** A string character sequence

- **b:** A string character sequence

### Returns

Returns an *integer*, which indicates the difference, see the table below for further information.

### Indicators

| Value | Meaning |
| --- | --- |
| -1 | a < b |
| 0 | a == b |
| 1 | a > b |

## Example

Click to collapse [-]
Server

This example shows a simple comparsion of two different strings.

```
local a = "Hello"
local b = "World"
local result = utf8.ncasecmp( a, b )

if result == -1 then
    print( "a < b" ) -- printed
elseif result == 0 then
    print( "a == b" )
elseif result == 1 then
    print( "a > b" )
end
```

Click to collapse [-]
Server

This example shows how to greet a player, when he write 'hello' into the chat.

```
addEventHandler("onPlayerChat", root,
    function (message, messageType)
        if messageType == 0 and utf8.ncasecmp( message, "hello" ) == 0 then
            outputChatBox( "* Server: Hello!", source, 255, 100, 100 )
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

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](mta://scripting/shared/functions/utf8-lower.md)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- utf8.ncasecmp

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
