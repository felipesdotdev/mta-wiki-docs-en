---
doc_id: "mta-wiki:13414"
title: "Resource : EntityData/restrictions key"
source_title: "Resource:EntityData/restrictions key"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AEntityData/restrictions_key"
revision_id: 73067
language: "en"
categories: []
---

# Resource : EntityData/restrictions key

Restrictions key

Set of data validation functions for the key according to the assumed array in the flag.

# Introduction

setKeyFlag("Example Key", {type = string type,  value = string value, bettwen = table bettwen, function func = function value operation, int len = length only works for string data operations})

The flag function mainly consists of an array and basic concepts such as:

- string type - A specific data type from Lua and the MTA platform.

- string value - The type of data type

- table bettwen - An array with two numeric values ​​from to, the first must be the smallest and the second largest.

- function func - A function that checks the correctness of data according to your needs, the function structure consists of the default value parameter already added.

- int len - The value of the maximum accepted data length works for string

# Explanation

We divide the type into: userdata, number, string, table, boolean values ​​are not checked by the flag, if they are used, this fragment can be omitted.
The accepted types of values ​​for particular things are these:

- userdata:

- resource-data

- xml-node

- lua-timer

- vector2

- vector3

- vector4

- matrix

- account

- db-query

- acl

- acl-group

- ban

- text-item

- text-display

- vehicle

- ped

- player

- object

- gui

- element

- number

- int

- float

- string

- table

# Bettwen

can use the term bettwen for numeric and string values, 
The structure of the structure is as follows, example:

```
setKeyFlag("Example Key", {type = "number",  value = "int", bettwen = {0, 50} })
```

Values ​​that will be adopted will be between 0 and 50, in the case of others they will not be 
assigned to the element.

# func

A custom function that you can engage if you lack any data validation capabilities for a key.

```
local funcExample = [[
function(value)
    return value%2 == 0
end]]
setKeyFlag("Example Key", {type = "number",  value = "int", func = funcExample })

-- OR

funcCheckEven = function(value)
    return value%2 == 0
end
setKeyFlag("Example Key", {type = "number",  value = "int", func = funcCheckEven})
```

This function will check if the number we give is even if it allows it to be assigned to an element.

# len value

Length checking for the string data type

```
setKeyFlag("descrpition", {type = "string", len = 25})
```

If the value for the description key is 25 characters, then it will be assigned to the element.
