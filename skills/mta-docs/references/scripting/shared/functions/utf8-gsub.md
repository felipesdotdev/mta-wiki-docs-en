---
doc_id: "mta-wiki:8518"
title: "Utf8.gsub"
source_title: "Utf8.gsub"
source_url: "https://wiki.multitheftauto.com/wiki/Utf8.gsub"
revision_id: 63557
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# Utf8.gsub

Returns a copy of the original input string with replaced matches from the pattern by the replacement value.

| [[\|link=\|]] | Warning: This function may modify your input string even if no changes were made. Try it with runcode: srun utf8.gsub(utf8.char(66376), "", "") == utf8.char(66376) |
| --- | --- |
|  |  |

## Syntax

```
string utf8.gsub ( string input, string pattern, mixed replace [, int match_limit = utf8.len( input ) ] )
```

### Required Arguments

- **input:** A string character sequence

- **pattern:** A string match [pattern](http://lua-users.org/wiki/PatternsTutorial)

- **replace:** A string literal OR an integer value OR a function (see examples below) OR a table ({ match = replacement })

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **match_limit:** An integer to limit the number of substitutions made

### Returns

Returns a pair of values, the modified *string* and the *integer* number of substitutions made.

## Example

Click to collapse [-]
Server

This example shows how to remove color codes from a string and how to uppercase each single character in a string.

```
local text= "#ff0000This text is red"
local colorless = utf8.gsub( text, "#%x%x%x%x%x%x", "" )
print( colorless ) -- This text is red

print( utf8.gsub( "Nice wiki!", ".", utf8.upper ) ) -- NICE WIKI!
```

Click to collapse [-]
Server

This example uses a table to replace specific words in the input string by an other value.

```
local input = "We have nice weather in London"

local replacements = {
    ["weather"] = "food",
    ["London"] = "Germany"
}

local output = utf8.gsub( input, "%w+", replacements )
print( output ) -- We have nice food in Germany
```

Click to collapse [-]
Client

This example shows a simple bad word filter, which censors the word 'ugly' in the input string.

```
local input = "You are ugly!"

local badwords = {
    ["ugly"] = true
}

local output = utf8.gsub( input, "%w+",
    function (match)
        local lowerCase = utf8.lower( match )
        
        if badwords[ lowerCase ] then
            return string.rep( '*', utf8.len( match ) )
        end
        
        return match
    end
)

outputConsole( output ) -- You are ****!
```

## See Also

- [utf8.byte](https://wiki.multitheftauto.com/index.php?search=utf8.byte)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](https://wiki.multitheftauto.com/index.php?search=utf8.charpos)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](https://wiki.multitheftauto.com/index.php?search=utf8.find)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- [utf8.gmatch](https://wiki.multitheftauto.com/index.php?search=utf8.gmatch)

- utf8.gsub

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

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
