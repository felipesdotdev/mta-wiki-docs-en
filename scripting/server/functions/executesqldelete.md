---
doc_id: "mta-wiki:2258"
title: "ExecuteSQLDelete"
source_title: "ExecuteSQLDelete"
source_url: "https://wiki.multitheftauto.com/wiki/ExecuteSQLDelete"
revision_id: 44583
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:14:59.843667+00:00"
---

# ExecuteSQLDelete

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use executeSQLQuery instead. See the examples at executeSQLQuery for equivalent DELETE usage. |  |

This function deletes any rows (from the database) that meet the specified conditions in the specified table.

The SQLite database contains globally stored data and can be used by scripts to store and retrieve data in a structured manner.

The executed SQL query is the following:

```
[sql]DELETE FROM <table> WHERE <conditions>
```

## Syntax

```
bool executeSQLDelete ( string tableName, string conditions )
```

### Required Arguments

- **tableName:** The name of the table you want to modify.

- **conditions:** The conditions that need to be met before a row is deleted.

### Returns

The function returns a *boolean* which is *true* on success, and *false* on failure.

### Example

This example creates a table and add's a command to delete the row called "row" inside the table.

```
-- Create's the table named "table" on resource start.
function tableCreate()
    executeSQLCreateTable("table", "row TEXT")
end
addEventHandler("onResourceStart", getResourceRootElement(), tableCreate)

-- Add's a command "deleterow" to delete the row called "row"

function rowDelete()
    executeSQLDelete("table", "row")
end
addCommandHandler("deleterow", rowDelete)
```

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
