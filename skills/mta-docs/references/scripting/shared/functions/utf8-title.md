---
doc_id: "mta-wiki:8522"
title: "Utf8.title"
source_title: "Utf8.title"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.title"
revision_id: 70959
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# Utf8.title

| [[{{{image}}}\|link=\|]] | Note: You may want to read up on case folding for more information about the use of this function. |
| --- | --- |
|  |  |

Converts a UTF-8 string to title case (uppercase). If *input* is an integer, it is treated as a codepoint and a converted codepoint (integer) is returned.

## Syntax

```
string utf8.title ( string|int input )
```

```
string utf8.upper ( string|int input )
```

### Required Arguments

- **input:** A string character sequence OR an integer value

### Returns

Returns a *string* in uppercase OR returns an *integer* (see description).

## Example

Click to collapse [-]
Client

This example shows how to convert a string to uppercase.

```
local output = utf8.upper( "WHAT ARE YOU UP TO? Do you like uppercase?" )
outputConsole( output ) -- WHAT ARE YOU UP TO? DO YOU LIKE UPPERCASE?

local value = utf8.title( 1088 )
outputConsole( value, type( value ) ) -- 1056, number
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

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](https://wiki.multitheftauto.com/index.php?search=utf8.lower)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](https://wiki.multitheftauto.com/index.php?search=utf8.next)

- [utf8.remove](https://wiki.multitheftauto.com/index.php?search=utf8.remove)

- [utf8.reverse](https://wiki.multitheftauto.com/index.php?search=utf8.reverse)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- utf8.title

- [utf8.upper](https://wiki.multitheftauto.com/index.php?search=utf8.upper)

- [utf8.width](https://wiki.multitheftauto.com/index.php?search=utf8.width)

- [utf8.widthindex](https://wiki.multitheftauto.com/index.php?search=utf8.widthindex)
