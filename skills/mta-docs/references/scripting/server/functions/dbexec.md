---
doc_id: "mta-wiki:5893"
title: "DbExec"
source_title: "DbExec"
source_url: "https://wiki.multitheftauto.com/wiki/DbExec"
revision_id: 81031
language: "en"
categories: ["Server_functions"]
---

# DbExec

This function executes a database query using the supplied connection. No query result is returned.

| [[{{{image}}}\|link=\|]] | Tip: The server command debugdb 2 will output verbose information on each query to a logging file (usually logs/db.log ) |
| --- | --- |
|  |  |

## Syntax

```
bool dbExec ( element databaseConnection, string query [, var param1 [, var param2 ...]] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[connection](https://wiki.multitheftauto.com/index.php?search=connection):exec(...)*

### Required Arguments

- **databaseConnection:** A database connection element previously returned from [dbConnect](mta://scripting/server/functions/dbconnect.md)

- **query:** An SQL query. Positions where parameter values will be inserted are marked with a **?**

### Optional Arguments

- **paramX:** A variable number of parameters. These must be strings or numbers - it is important to make sure they are of the correct type. Also, the number of parameters passed must be equal to the number of **?** characters in the query string.

String parameters are automatically quoted and escaped as required. (If you do not want a string quoted, use **??**) Make sure that numbers are in number format as a string number is treated differently.

### Returns

Returns *true* unless the connection is incorrect, in which case it returns *false*.

## Example

This example executes an INSERT query:

```
dbExec( connection, "INSERT INTO table_name VALUES (?,?,?)", "aaa", "bbb", 10 )
```

This example shows how to use **??** for parts of the query that are not column values:

```
dbExec( connection, "UPDATE ?? SET ??=?", tableName, columnName, columnValue )
```

***Note**: It is usually good practice to surround table and column names with backticks (`) in case they contain spaces or SQL keywords (and therefore cause syntax errors). This is especially true when using variables for table and column names, as potential problems may not be apparent when the script is first written.*

This example shows how to use backticks and **??** for parts of the query that are not column values:

```
dbExec( connection, "UPDATE `??` SET `??`=?", tableName, columnName, columnValue )
```

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- dbExec

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
