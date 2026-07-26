---
doc_id: "mta-wiki:1885"
title: "ExecuteSQLDropTable"
source_title: "ExecuteSQLDropTable"
source_url: "https://wiki.multitheftauto.com/wiki/ExecuteSQLDropTable"
revision_id: 49368
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# ExecuteSQLDropTable

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use executeSQLQuery instead. See the examples at executeSQLQuery for equivalent DROP TABLE usage. |  |

This function drops a table in the registry. This function doesn't do anything when the table doesn't exist.

The executed SQL query is the following:

```
DROP TABLE table
```

## Syntax

```
bool executeSQLDropTable ( string tableName )
```

### Required Arguments

- **tableName:** The name of the table you want to drop.

### Returns

The function returns *true* on success, and *false* on failure.

### Example

This example lets you drop an SQL table with the command: dropsqltable. Note: This command should be restricted to admins if you use it.

```
function removeSQLTable(thePlayer, command, SQLtable)
	if (SQLtable) then -- Make sure the player entered an argument.
		success = executeSQLDropTable(SQLtable) -- Drop the table
		if (success) then -- If executeSQLDropTable returns true, it passes this if check to display a confirmation message
			outputChatBox("SQL Table "..SQLtable.." successfully dropped.", thePlayer, 0, 255, 0)
		else
			outputChatBox("SQL Table "..SQLtable.." was not successfully dropped.", thePlayer, 255, 0, 0)
		end
	end
end
addCommandHandler("dropsqltable", removeSQLTable)
```

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
