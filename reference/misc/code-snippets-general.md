---
doc_id: "mta-wiki:5348"
title: "Code Snippets General"
source_title: "Code Snippets General"
source_url: "https://wiki.multitheftauto.com/wiki/Code_Snippets_General"
revision_id: 79860
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:11:21.514179+00:00"
---

# Code Snippets General

This page contains general purpose code snippets.

*(You can test your code in [http://www.lua.org/demo.html](http://www.lua.org/demo.html))*

# Mathematical Snippets

### Generating Pseudo-Random Numbers

```
math.random( 3, 9 ) -- Generates a random integer between 3 and 9 inclusively.
math.Rand( 3, 9 ) -- Generates a random real number (floating point) between 3 and 9 inclusively.
```

### Better Rounding

- This allows you to round to a decimal point instead of to a whole number.

```
-- Rounds to the 2nd decimal point
-- Usage: math.AdvRound( 1.6443132, 2 ); 
--
function math.AdvRound( val, d )
	d = d or 0;
	
	return math.Round( val * (10 ^ d) ) / (10 ^ d);
end
```

### Toggling a Boolean

```
local Boolean = false
 -- Toggle the boolean.
Boolean = not Boolean
-- or, in C-style notation:
Boolean = !Boolean
```

# Variables

### Defining Multiple Variables

```
-- X = 1, Y = 2, Z = 3.
local X, Y, Z = 1, 2, 3
```

### Using OR

```
-- If Y is non-nil, set X to Y; otherwise, set X to 0.
local X = Y or 0
```

### Switching Two Variables without Making a Third

```
a,b = b,a
```

# Loops and statements

### Looping through Every Character in a String

```
for i = 1, string.len( strToLoop ) do
    local Character = string.sub( strToLoop, i, i )
     -- Do stuff with Character here.
end
```

### Using 'repeat, until'

```
repeat
num = math.random( 200 )
Msg( num .. "\n" )
until( num == 25 )
```

### Doing 'if .. then ... else' in One Line

```
local value = ( x > 1 ) && "X is greater" || "X isn't greater";
--and in STD. Lua notation:
local value = ( x > 1 ) and "X is greater" or "X isn't greater";
--basic format for Inline Conditionals:
local value = (Condition) and TrueValue or FalseValue;
```

### Returning 'if .. then ... else'

```
return current < max and func( current + 1, max ) or nil
```

# Miscellaneous

### Convert XYToRelative (by Cazomino05)

Converts an XY co-ordinate to a relative size requires the resolution you tested it on (you can find it in gta display settings)

```
function ConvertXYToRelative(Resx, Resy, x, y)
    local Rx = (1/Resx)*x
    local Ry = (1/Resy)*y
    return Rx,Ry
end

-- EXAMPLE
function ResourceStarted(resource)
    if (resource ~= getThisResource()) then
        return
    end
    local x,y = ConvertXYToRelative(800, 600, 400, 300)
    outputChatBox("Relative sizes:  "..x..", "..y)
end
addEventHandler("onResourceStart", getRootElement(), ResourceStarted)
```
