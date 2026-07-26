---
doc_id: "mta-wiki:8486"
title: "DbPrepareString"
source_title: "DbPrepareString"
source_url: "https://wiki.multitheftauto.com/wiki/DbPrepareString"
revision_id: 81191
language: "en"
categories: ["Server_functions"]
---

# DbPrepareString

This function escapes arguments in the same way as [dbQuery](mta://scripting/server/functions/dbquery.md), except dbPrepareString returns the query string instead of processing the query. This allows you to safely build complex query strings from component parts and help prevent (one class of) SQL injection.

## Syntax

```
string dbPrepareString ( element databaseConnection, string query [, var param1 [, var param2 ...]] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[connection](https://wiki.multitheftauto.com/index.php?search=connection):prepareString(...)*

### Required Arguments

- **databaseConnection:** A database connection element previously returned from [dbConnect](mta://scripting/server/functions/dbconnect.md)

- **query:** An SQL query. Positions where parameter values will be inserted are marked with a **?**

### Optional Arguments

- **paramX:** A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of **?** characters in the query string.

String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use **??**)

### Returns

Returns a prepare SQL query string, or *false* if an error occurred.

## Example

This example shows how to safely build a dynamic SELECT query

```
serialsToUse = { "111", "222", "333" }

local queryString = dbPrepareString( connection, "SELECT * FROM `player_info` WHERE true" )
for _,serial in ipairs(serialsToUse) do
    queryString = queryString .. dbPrepareString( connection, " AND `serial`=?", serial )
end
local handle = dbQuery( connection, queryString )
```

This example shows how to build an INSERT/UPDATE query for multiple rows. (Query syntax is MySQL only and assumes one column is a unique key)

```
local queryString = dbPrepareString( connection, "INSERT INTO `player_info` (name,serial,ispoopoohead) VALUES " )
for idx,info in ipairs(playerInfos) do
    if idx > 1 then
        queryString = queryString .. ","
    end
    queryString = queryString .. dbPrepareString( connection, "(?,?,?)", info.name, info.serial, info.ispoopoohead )
end
queryString = queryString .. dbPrepareString( connection, " ON DUPLICATE KEY UPDATE name=VALUES(name),serial=VALUES(serial),ispoopoohead=VALUES(ispoopoohead) " )
dbExec( connection, queryString );
```

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- dbPrepareString

- [dbQuery](mta://scripting/server/functions/dbquery.md)
