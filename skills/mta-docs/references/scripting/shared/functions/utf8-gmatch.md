---
doc_id: "mta-wiki:8517"
title: "Utf8.gmatch"
source_title: "Utf8.gmatch"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.gmatch"
revision_id: 46637
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# Utf8.gmatch

This function returns a pattern finding iterator for UTF-8 strings. The iterator will search through the string **input** looking for instances of the pattern you passed. For more information on iterators read the [ForTutorial](http://lua-users.org/wiki/ForTutorial) and [IteratorsTutorial](http://lua-users.org/wiki/IteratorsTutorial).

## Syntax

```lua
iterator utf8.gmatch ( string input, string pattern )
```

### Required Arguments

- **input:** A string character sequence

- **pattern:** A string match [pattern](http://lua-users.org/wiki/PatternsTutorial)

### Returns

Returns an *function* for iterations on the **input** string by using the passed **pattern** string.

## Example

Click to collapse [-]
Server

This example prints every word in the UTF-8 string

```lua
for word in utf8.gmatch( "Как вас зовут?", "%a+" ) do 
    print( word )
end
```

Output:

```lua
Как
вас
зовут
```

## See Also

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](mta://scripting/shared/functions/utf8-find.md)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- utf8.gmatch

- [utf8.gsub](mta://scripting/shared/functions/utf8-gsub.md)

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](https://wiki.multitheftauto.com/wiki/Utf8.lower)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](https://wiki.multitheftauto.com/wiki/Utf8.upper)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)
