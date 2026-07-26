---
doc_id: "mta-wiki:1292"
title: "Optional Arguments"
source_title: "Optional Arguments"
source_url: "https://wiki.multitheftauto.com/wiki/Optional_Arguments"
revision_id: 77250
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:16:27.070451+00:00"
---

# Optional Arguments

**Optional arguments** are arguments which can be optionally passed to any Lua function, including MTA: SA built-in ones. They are not required for the function to run, and can be unset (value == *[nil](mta://reference/misc/nil.md)*). Often, this kind of arguments do not make a huge difference in the behaviour of the function.

It's a Lua convention that the arguments written between square brackets are optional, so in this Wiki you can find functions with some arguments between square brackets too. That means they are optional and that providing them is not necessary.

Let's take a look at this common function:

```
vehicle createVehicle ( int model, float x, float y, float z, [ float rx, float ry, float rz ] )
```

In this example, *rx*, *ry*, and *rz* are optional arguments, because they are between square brackets. They do not need to be provided to the function; it will default to no rotation in every axis. If provided, the function will use the rotations specified instead.

## Why are optional arguments used?

More often than not, it's boring having to provide all the arguments of a certain function, especially if they are the same over and over again. The optional arguments allow the scripter to only pass the data that is really needed for his script, and that helps improving code readibility and size.

## Use of the optional arguments

Optional argument are used just like normal arguments. The only difference is that they will default to a certain value if no provided (in other words, if optionalArgument == nil then optionalArgument = defaultValue).

One common problem to new scripters is when they want to provide only an optional argument, without setting the ones that are before it. Well, this is really simple to "fix". Normally, they can be set to *[nil](mta://reference/misc/nil.md)*, so they will default to its corresponding values while the scripter is still able to set the one he really wants to. For example, if you want to only set the rotation in Z axis of the [createVehicle](mta://scripting/shared/functions/createvehicle.md) function (and don't know that *rx* and *ry* default to zero):

```
vehicle createVehicle ( int model, float x, float y, float z, [ float rx, float ry, float rz ] )
```

You can use:

```
local myAwesomeVehicle = createVehicle( getVehicleModelFromName( "Infernus" ), 0, 0, 5, nil, nil, 180 )
```

And the result will be an Infernus rotated 180 degrees in the Z axis in the center of the map.

|  | Warning: There are some built-in MTA: SA functions that don't follow this convention, especially when an optional argument is closely related to another (e.g. color arguments in DX functions, and probably others): instead of replacing the nil value, they output a 'bad argument' error and do nothing. Always check if this works with a function before using it in a script . |
| --- | --- |
|  |  |

## Scripting custom functions with optional arguments

Scripting functions with optional arguments is as easy as using *if* statements:

```
function aNotSoUsefulFunction( text )
    if type( text ) == "string" or type( text ) == "nil" then -- Check if correct arguments have been provided
        local realTextToOutput
        if text == nil then
            realTextToOutput = "I <3 optional arguments" -- If the text is nil (not specified), use a default one
        else
            realTextToOutput = text -- Use the text that the user specified if defined
        end
        outputChatBox( realTextToOutput ) -- Output the text
    end
end
```

You can also use [short-circuit evaluation](http://en.wikipedia.org/wiki/Short-circuit_evaluation), if you prefer to:

```
function aNotSoUsefulFunction( text )
    local realTextToOutput = ( type( text ) == "string" or type( text ) == "nil" ) and ( type( text ) == "string" and text or "I <3 optional arguments" ) or nil
    if realTextToOutput then -- Check if there is something to output
        outputChatBox( realTextToOutput ) -- Output the text
    end
end
```
