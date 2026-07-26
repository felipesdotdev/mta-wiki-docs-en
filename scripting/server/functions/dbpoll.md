---
doc_id: "mta-wiki:5887"
title: "DbPoll"
source_title: "DbPoll"
source_url: "https://wiki.multitheftauto.com/wiki/DbPoll"
revision_id: 81029
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:11:32.149241+00:00"
---

# DbPoll

This function checks the progress of a database query.

## Syntax

```
table dbPoll ( handle queryHandle, int timeout [, bool multipleResults = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *queryHandle:poll(...)*

### Required Arguments

- **queryHandle:** A query handle previously returned from [dbQuery](mta://scripting/server/functions/dbquery.md)

- **timeout:** How many milliseconds to wait for a result. Use 0 for an instant response (which may return nil). Use -1 to wait until a result is ready. Note: A wait here will freeze the entire server just like executeSQLQuery

| [[{{{image}}}\|link=\|]] | Important Note: It is strongly recommended to use this function in callback, as presented in "This example shows how to obtain data without server freeze." |
| --- | --- |
|  |  |

### Optional Arguments

- **multipleResults:** Set to true to enable the return values from multiple queries

### Returns

- *nil:* Returns nil if the query results are not yet ready. You should try again in a little while. (If you give up waiting for a result, be sure to call [dbFree](mta://scripting/server/functions/dbfree.md))

- *false:* Returns false if the query string contained an error, the connection has been lost or the query handle is incorrect. This automatically frees the query handle, so you do not have to call [dbFree](mta://scripting/server/functions/dbfree.md).

- This also returns two extra values: (See the example on how the retrieve them)

- *int:* error code

- *string* error message

- *table:* Returns a table with the result of the query when the query has successfully completed. This automatically frees the query handle, so you do not have to call [dbFree](mta://scripting/server/functions/dbfree.md). If multipleResults is set to true, it will first return a table pertaining to one query, followed by the results for that query and so on for the next queries.

- This also returns extra values (only when multipleResults is set to true):

- *int:* number of affected rows

- *int:* last insert id

The table is of the format:

```
{
    { colname1=value1, colname2=value2, ... },
    { colname1=value3, colname2=value4, ... },
    ...
}
```

A subsequent table represents the next row.

| [[{{{image}}}\|link=\|]] | Note: If a column contained a number it is returned as a number, this includes things which were stored as string but are numbers such as "1" would be returned as 1. |
| --- | --- |
|  |  |

## Example

This example waits until a result is ready:

```
local result = dbPoll ( qh, -1 )
```

This example shows the possible return values:

```
local result, num_affected_rows, last_insert_id = dbPoll ( qh, -1 )

if result == nil then
    outputConsole( "dbPoll result not ready yet" )
elseif result == false then
    local error_code,error_msg = num_affected_rows,last_insert_id
    outputConsole( "dbPoll failed. Error code: " .. tostring(error_code) .. "  Error message: " .. tostring(error_msg) )
else
    outputConsole( "dbPoll succeeded. Number of affected rows: " .. tostring(num_affected_rows) .. "  Last insert id: " .. tostring(last_insert_id) )
end
```

This example shows how to handle the result if the query selected data:

```
local result = dbPoll ( qh, -1 )

if result then
    for _, row in ipairs ( result ) do

        -- by using a second loop (use it if you want to get the values of all columns the query selected):
        for column, value in pairs ( row ) do
            -- column = the mysql column of the table in the query
            -- value = the value of that column in this certain row
        end
		
        -- or without a second loop (use it if you want to handle every value in a special way):
        outputChatBox ( row["column"] ) -- it will output the value of the column "column" in this certain row
    end
end
```

This example shows how to print the results of the query:

```
local dbConnection = dbConnect("sqlite", "test.db")
local queryHandle = dbQuery(dbConnection, "SELECT * FROM `Test1`")
local queryResult = dbPoll(queryHandle, -1)
	
for rowID, rowData in ipairs(queryResult) do

	for columnName, columnValue in pairs(rowData) do
		outputChatBox(columnName..", "..columnValue)
	end
end
```

This is another example of printing the results:

```
local connection = dbConnect("sqlite", "test.db")
local queryhandle = dbQuery(connection, 'SELECT * FROM Test1')
local result = dbPoll(queryhandle, -1)
	
for rid, row in ipairs (fromJSON(toJSON(result))) do -- row represents the tables that are in 'result', which represent the rows
    for column, value in pairs (row) do -- column represents column name, value represents column value
	 outputChatBox(column..', '..value)
    end
end
```

This is another example of printing the results:

```
local connection = dbConnect("sqlite", "test.db")
local queryhandle = dbQuery( connection, 'INSERT INTO Test1 ("Name1", "Name2") VALUES ("Hello", "Hi");')
local result = dbPoll(queryhandle, -1)

outputChatBox(toJSON(result)) -- Shows only rowid 1 affected because we only used INSERT INTO statement and not a SELECT statement.

queryhandle = nil -- Making the query handle and result to nil
result = nil

queryhandle = dbQuery( connection, 'SELECT * FROM Test1;')
result = dbPoll(queryhandle, -1)
outputChatBox(toJSON(result)) -- Now shows rowid 2 affected.
```

This is another example of printing the results:

```
local connection = dbConnect("sqlite", "test.db")
local queryhandle = dbQuery( connection, 'INSERT INTO Test1 (Name1) VALUES ("Hello"); SELECT * FROM Test1')
local multiResults = dbPoll(queryhandle, -1)

for sid, statementResult in ipairs ( multiResults ) do
    local resultRows, num_affected_rows, last_insert_id =  unpack(statementResult) 
    for rid, row in ipairs ( resultRows ) do 
	 for column, value in pairs ( row ) do
	      outputChatBox(sid..", "..rid..", "..column..", "..tostring(value)..", "..num_affected_rows..", "..last_insert_id) -- Only shows SELECT statements
	end
    end			
end
```

This is another example of printing the results:

```
local connection = dbConnect("sqlite", "test.db")
local queryhandle = dbQuery( connection, 'INSERT INTO Test1 (Name1) VALUES ("Hello"); SELECT * FROM Test1')
local multiResults = dbPoll(queryhandle, -1)

for sid, statementResult in ipairs ( multiResults ) do
    local resultRows, num_affected_rows, last_insert_id =  unpack(statementResult) 
    for rid, row in ipairs ( resultRows ) do 
	for column, value in pairs ( row ) do
	       
	end
    end
    outputChatBox(sid..", "..num_affected_rows..", "..last_insert_id) -- Shows all statement ids, but only shows affected rows and last insert id
end
```

This example shows how to handle the result of a multiple statement query: (See [dbConnect](mta://scripting/server/functions/dbconnect.md) option **multi_statements**)

```
local multiResults = dbPoll ( qh, -1, true )

if multiResults then
    for sidx, statementResult in ipairs ( multiResults ) do
        local resultRows, numAffectedRows, lastInsertId = unpack(statementResult)
        for ridx, row in ipairs ( resultRows ) do
            for column, value in pairs ( row ) do
                outputDebugString( ""
                        .. " statement#" .. sidx
                        .. " row#" .. ridx
                        .. " column:" .. tostring(column)
                        .. " value:" .. tostring(value)
                        )
            end
        end
    end
end
```

This example shows how to obtain data without server freeze.

```
local dbConnection = dbConnect("sqlite", "sql.db")
local playerName = "testPlayer"

function onServerQueryCallback(queryHandler, extraData)
	local queryResult = dbPoll(queryHandler, 0)
	local validResult = type(queryResult) == "table"

	outputDebugString("Extra data which have been passed through dbQuery:", extraData)

	if not validResult then
		outputDebugString("Result ~= table")

		return false
	end

	outputDebugString("Query results:", queryResult)
end

dbQuery(onServerQueryCallback, {"Some data"}, dbConnection, "SELECT * FROM `Players` WHERE `playerName` = ?", playerName)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.4-9.05862 | Added 'last insert id' return value |
| --- | --- |

| 1.5.2-9.07972 | Added 'multipleResults' argument |
| --- | --- |

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- dbPoll

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
