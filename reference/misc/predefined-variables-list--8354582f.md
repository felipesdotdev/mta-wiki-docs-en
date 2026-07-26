---
doc_id: "mta-wiki:6107"
title: "Predefined variables list"
source_title: "Predefined variables list"
source_url: "https://wiki.multitheftauto.com/wiki/Predefined_variables_list"
revision_id: 79909
language: "en"
categories: ["Changes_in_1.6.0", "Scripting_Concepts"]
generated_at: "2026-07-26T16:16:29.695536+00:00"
---

# Predefined variables list

Lua Predefined variables

```
_G -- returns a table of all global variables
coroutine -- returns a table containing functions for threads
debug -- returns a table containing debug functions
math -- returns a table that contains mathematical functions
string -- returns a table containing functions for strings
table -- returns a table that contains functions for tables
_VERSION -- returns a string of the version of lua in format "Lua 5.1"
self -- used in methods
arg -- used in functions which use '...' as an argument (https://www.lua.org/pil/5.2.html)
```

## MTA Predefined variables

### Global

ADDED/UPDATED IN VERSION 1.6.0 [r22960](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22960):

resourceName -- returns the name of the resource the snippet was executed in 

Click to collapse [-]
Shared

```
exports -- returns a table of resource names containing all export functions
resource -- returns a resource element of the resource the snippet was executed in
resourceRoot -- returns a resource root element of the resource the snippet was executed in
resourceName -- returns the name of the resource the snippet was executed in 
root -- returns the root element of the server
```

Click to collapse [-]
Client only

```
guiRoot -- returns the root element of all GUI elements.
localPlayer -- returns the player element of the local player.
```

### Event Handlers

[More details about hidden variables in functions and events](https://wiki.multitheftauto.com/wiki/AddEventHandler)

Click to collapse [-]
Shared

```
source -- The player or element the event was attached to
this -- Element, which was attached function-handler.
eventName -- the name of the event ("onResourceStart", "onPlayerWasted" etc.)
sourceResource -- the resource that called the event
sourceResourceRoot -- the root of the resource that called the event
```

Click to collapse [-]
Server only

```
client -- the client that called the event
```

Please note, the above pre-defined variables may only be accessible in the relevant scope (i.e, an event handler callback function). Further functions defined within that scope may not have access to these pre-defined variables at the time of their execution.

For this reason, you should always explicitly redefine pre-defined variables as local variables, to ensure they are always available to new functions declared within that scope - for example:

```
function init()
    local player = source -- source is a pre-defined variable for this event, containing the player element

    local func = function()
        print(source) -- prints 'nil', source isn't available anymore
        print(player) -- prints player element
    end

    setTimer(func, 1000, 1) -- run above function after 1 second
end
addEventHandler("onPlayerResourceStart", root, init)
```

### Timer Callbacks

Click to collapse [-]
Shared

```
sourceTimer -- current timer in callback function.
```

### HTTP

List Predefined variables available in the HTTP files [(more info about it)](https://wiki.multitheftauto.com/wiki/Resource_Web_Access):

```
[php]
requestHeaders -- table, contains all HTTP headlines current page.
form -- table, contains all POST and GET settings, transferred current page.
cookies -- table, contains all COOKIE, transferred current page.
hostname -- string, contains IP or name host, which requested current page.
url -- string, URL current page.
user -- element, account user, which requested current page.
```

## See Also

[Element Tree](mta://reference/misc/element-tree.md)
