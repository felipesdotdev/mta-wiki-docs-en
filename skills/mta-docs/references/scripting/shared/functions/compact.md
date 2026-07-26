---
doc_id: "mta-wiki:13659"
title: "Compact"
source_title: "Compact"
source_url: "https://wiki.multitheftauto.com/wiki/Compact"
revision_id: 78875
language: "en"
categories: ["Useful_Functions"]
---

# Compact

This function performs a search in a given table and returns a new table containing the values of specified variable name strings.

## Syntax

```
table compact(table Array, table/string Variable)
```

### Required Arguments

- **Array:** the [table](mta://reference/misc/table.md) handles it recursively.

- **Variable**: [table](mta://reference/misc/table.md) or [string](mta://reference/misc/string.md) takes a variable number of parameters. Each parameter can be either a string containing the name of the variable, or an array of variable names. The array can contain other arrays of variable names inside it.

### Returns

Returns the output [table](mta://reference/misc/table.md) with all the variables added to it.

## Code

```
function compact(g, ...)
    local args = {...}
    local tbl = {}
    g = g or _G
    for i, v in ipairs(args) do
        for w in string.gmatch(v, "[%w_]+") do
            tbl[v] = g[w]
        end
    end
    return tbl
end
```

## Example

Click to collapse [-]
Shared Function

```
-- AND FORMAT FUNCTION --- With EXEMPLE
function format(s, tab)
    return (s:gsub('($%b{})', function(w) return tab[w:sub(3, -2)] or w end))
end

function compact(g, ...)
    local args = {...}
    local tbl = {}
    g = g or _G
    for i, v in ipairs(args) do
        for w in string.gmatch(v, "[%w_]+") do
            tbl[v] = g[w]
        end
    end
    return tbl
end

function testCompact()
   local tbl = {
       firstname = "Peter",
       lastname = "Griffin",
       age = 41
   }
   return format("My lastname is ${lastname} and age its ${age}", compact(tbl, "lastname",'age'))
end

outputChatBox( testCompact() )
```

**Author:** @FroPop
