---
doc_id: "mta-wiki:5888"
title: "DbFree"
source_title: "DbFree"
source_url: "https://wiki.multitheftauto.com/wiki/DbFree"
revision_id: 81030
language: "en"
categories: ["Server_functions"]
---

# DbFree

This function frees a database query handle. dbFree only needs to be used if a result has not been obtained with [dbPoll](mta://scripting/server/functions/dbpoll.md)

## Syntax

```
bool dbFree ( handle queryHandle )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *queryHandle:free(...)*

### Required Arguments

- **queryHandle:** A query handle previously returned from [dbQuery](mta://scripting/server/functions/dbquery.md)

### Returns

Returns *true* if the handle was successfully freed, *false* otherwise.

## Example

##### These examples show when dbFree should be used:

Required because [dbPoll](mta://scripting/server/functions/dbpoll.md) was not called:

```
local qh = dbQuery( connection, "SELECT * FROM table_name" )
dbFree ( qh )
```

Required because [dbPoll](mta://scripting/server/functions/dbpoll.md) was not called:

```
function aaa()
    dbQuery( myCallback, connection, "SELECT * FROM table_name" )
end

function myCallback(qh)
    dbFree ( qh )
end
```

Required because [dbPoll](mta://scripting/server/functions/dbpoll.md) is called, but the result was not ready and no more attempts will be made:

```
local qh = dbQuery( connection, "SELECT * FROM table_name" )
local result = dbPoll( qh, 10 )     -- Get result with a timeout of 10ms
if result == nil then
    result = dbPoll( qh, 10 )       -- Try again to get result with a timeout of 10ms
    if result == nil then
        dbFree( qh )                -- Give up
    end
end
```

##### These examples show when dbFree should NOT be used:

Not required because [dbPoll](mta://scripting/server/functions/dbpoll.md) was called with a -1 timeout:

```
local qh = dbQuery( connection, "SELECT * FROM table_name" )
local result = dbPoll( qh, -1 )    -- Wait until result has been gotten
```

Not required because [dbPoll](mta://scripting/server/functions/dbpoll.md) was called from the callback:

```
function aaa()
    dbQuery( myCallback, connection, "SELECT * FROM table_name" )
end

function myCallback(qh)
    local result = dbPoll( qh, 0 )  -- Timeout doesn't matter here because the result will always be ready
end
```

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- dbFree

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
