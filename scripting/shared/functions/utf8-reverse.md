---
doc_id: "mta-wiki:8528"
title: "Utf8.reverse"
source_title: "Utf8.reverse"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.reverse"
revision_id: 46654
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:02.361685+00:00"
---

# Utf8.reverse

Reverses the input string.

## Syntax

```
string utf8.reverse ( string input )
```

### Required Arguments

- **input:** A string character sequence

### Returns

Returns a *string* containing the reversed original UTF-8 string.

## Example

Click to collapse [-]
Client

This example shows how to reverse a UTF-8 string.

```
local input = "今日は素晴らしい日です"
local output = utf8.reverse( input )
outputConsole( output ) -- すで日いしら晴素は日今
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

- utf8.reverse

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
