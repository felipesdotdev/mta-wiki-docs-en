---
doc_id: "mta-wiki:5885"
title: "DbConnect"
source_title: "DbConnect"
source_url: "https://wiki.multitheftauto.com/wiki/DbConnect"
revision_id: 82787
language: "en"
categories: ["Server_functions", "Changes_in_1.6.0"]
---

# DbConnect

This function opens a connection to a database and returns an element that can be used with [dbQuery](mta://scripting/server/functions/dbquery.md). To disconnect use [destroyElement](mta://scripting/shared/functions/destroyelement.md).

| [[{{{image}}}\|link=\|]] | Note: Connecting and disconnecting many times can have a performance impact on the server. For optimal performance it is recommended that you use dbConnect only once when the resource starts, and share the connection element with the whole script. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: In MySQL 8.0 and later, you can choose between `caching_sha2_password` , `sha256_password` , or `mysql_native_password` for password management. If you opt for `caching_sha2_password` or `sha256_password` , SSL is not mandatory but recommended for secure authentication. If you choose `mysql_native_password` , you can set it as the default authentication plugin: In the `mysqld.cnf` configuration file, by adding or modifying the following line: default-authentication-plugin=mysql_native_password Using SQL queries (e.g., ALTER USER). In PHPMyAdmin (via the user settings page). Please note that starting with MySQL 9.0, `mysql_native_password` will no longer be available, and only `caching_sha2_password` and `sha256_password` will be supported. |
| --- | --- |
|  |  |

## Syntax

```
element dbConnect ( string databaseType, string host [, string username = "", string password = "", string options = "" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Connection](https://wiki.multitheftauto.com/index.php?search=Connection)(...)*

### Required Arguments

- **databaseType:** The type of database. This can be either *sqlite* or *mysql*

- **host:** The target to connect to. The format of this depends on the database type.

- For SQLite it is a [filepath](mta://reference/misc/filepath.md) to a SQLite database file. If the filepath starts with ":/" then the server's global databases directory is used. The file will be created if it does not exist.

- For MySQL it is a list of key=value pairs separated by semicolons. Supported keys are:

- **dbname**: Name of the database to use e.g. *dbname=test*

- **host**: Host address e.g. *host=127.0.0.1*

- **port**: Host port e.g. *port=3306* (optional, defaults to standard MySQL port if not used)

- **unix_socket**: Unix socket or named pipe to use (optional)

- **charset**: Communicate with the server using a character which is different from the default e.g. *charset=utf8* (optional)

### Optional Arguments

- **username:** Usually required for MySQL, ignored by SQLite

- **password:** Usually required for MySQL, ignored by SQLite

- **options :** List of key=value pairs separated by semicolons. Supported keys are:

- **share** which can be set to 0 or 1. (Default value for SQLite is "share=1", for MySQL is "share=0"). When set to 1, the connection is shared and will be used by other calls to dbConnect with the same host string. This is usually a good thing for SQLite connections, but not so good for MySQL unless care is taken.

- **batch** which can be set to 0 or 1. (Default is "batch=1"). When set to 1, queries called in the same frame are automatically batched together which can significantly speed up inserts/updates. The downside is you lose control of the feature that is used to achieve batching (For SQLite it is transactions, for MySQL it is autocommit mode). Therefore, if you use transactions, lock tables or control autocommit yourself, you may want to disable this feature.

- **autoreconnect** which can be set to 0 or 1. (Default value "autoreconnect=1"). When set to 1, dropped connections will automatically be reconnected. Note that session variables (incl. SET NAMES), user variables, table locks and temporary tables will be reset because of the reconnection. So if you use these fancy features, you will need to turn autoreconnect off and cope with dropped connections some other way.

- **log** which can be set to 0 or 1. (Default value "log=1"). When set to 0, activity from this connection will not be recorded in the [database debug log file](mta://reference/misc/server-commands.md).

- **tag** (Default value "tag=script"). A string which helps identify activity from this connection in the [database debug log file](mta://reference/misc/server-commands.md).

- **suppress** A comma separated list of error codes to ignore. (eg. "suppress=1062,1169").

- **multi_statements** Enable multiple statements (separated by a semi-colon) in one query. Use [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md) when building a multiple statement query to reduce SQL injection risks.

- **queue** Name of the queue to use. (Default value for SQLite is "sqlite", for MySQL default is the host string from the **host** argument). Asynchronous database queries in the same queue are processed in order, one at a time. Any name can be used.

- **use_ssl** which can be set to 0 or 1. (Default value is 0), ignored by SQLite

- ADDED/UPDATED IN VERSION 1.6.0 [r22497](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22497):

**get_server_public_key** which can be set to 0 or 1. (Default value is 1), ignored by SQLite. When set to 1, this enables the client to request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin.

### Returns

Returns a database connection element unless there are problems, in which case it return *false*.

## Remarks

Under certain platforms, for example on Unix-based OSes like Linux, using this function could fail with a debug warning containing "[Could not connect]" accompanied by a prior debug error explaining the problem. In that case you should check the [Server Manual](mta://getting-started/server-manual.md) to see if you have missed any recommended (best-effort) steps for server set-up.

## Example

This example opens a connection to a SQLite database file in the current resource

```
test_db = dbConnect( "sqlite", "file.db" )
```

This example opens a connection to a SQLite database file in another resource

```
test_db = dbConnect( "sqlite", ":resname/file.db" )
```

This example opens a connection to a SQLite database file in the global databases directory

```
test_db = dbConnect( "sqlite", ":/file.db" )
```

This example opens a connection to a SQLite database file in a sub directory of the global databases directory

```
test_db = dbConnect( "sqlite", ":/example/sub/dir/file.db" )
```

This example opens a connection to a MySQL database called 'frank' at server ip 1.2.3.4 using utf8 character set and allows the connection to be shared. Note that changing the database or other connection dependent settings affect all connections that are shared.

```
test_db = dbConnect( "mysql", "dbname=frank;host=1.2.3.4;charset=utf8", "username", "password", "share=1" )
```

This example opens a connection to a SQLite database is disallows sharing of the connection

```
test_db = dbConnect( "sqlite", "file.db", "", "", "share=0" )
```

This example output debug message, if the connection with SQLite database was established or not

```
test_db = dbConnect( "sqlite", "file.db" )

if test_db then
    outputDebugString( "Connection with database was successfully established." )
else
    outputDebugString( "Connection with database couldn't be established." )
end
```

The folowing example shows how you could approach a common resource for database operations with exported functions (**query** and **execute**):

```
function connect()
    DBConnection = dbConnect( "mysql", "dbname=DBNAME;host=HOST;charset=utf8", "USERNAME", "PASSWORD" )
    if (not DBConnection) then
        outputDebugString("Error: Failed to establish connection to the MySQL database server")
    else
        outputDebugString("Success: Connected to the MySQL database server")
    end
end

addEventHandler("onResourceStart",resourceRoot, connect)
 
function query(...)
    local queryHandle = dbQuery(DBConnection, ...)
    if (not queryHandle) then
        return nil
    end
    local rows = dbPoll(queryHandle, -1)
    return rows
end
 
function execute(...)
    local queryHandle = dbQuery(DBConnection, ...)
    local result, numRows = dbPoll(queryHandle, -1)
    return numRows
end

function getDBConnection()
    return DBConnection
end
```

The following example illustrates an exemplary approach to utilizing a common resource for database operations, employing exported functions such as **dbQuery**, **dbExec**, **dbQueryAsync**, **dbPrepareString**, and **dbQueryAsyncMultiple.**:

```
--[[

```meta.xml```
<export function="dbQueryAsync" type="server" />
<export function="dbQuery" type="server" />
<export function="dbExec" type="server" />
<export function="getTableName" type="server" />
<export function="dbPrepareString" type="server" />
<export function="dbQueryAsyncMultiple" type="server" />

```meta.xml end```
]]
--[[
example exported: = 
exports.nameres:dbQuery(-1, "test", "SELECT ID FROM ?? WHERE ID = ?", 1)

exports.nameres:dbExec("test", "UPDATE ?? SET test= ? WHERE ID = ?;", '0', 1)
exports.nameres:dbExec("test", "CREATE TABLE IF NOT EXISTS ?? (`ID` INT UNSIGNED NOT NULL PRIMARY KEY, `test` TEXT) COLLATE=utf8_unicode_ci;")

exports.nameres:dbExec("test", "INSERT INTO ?? (`ID`, `test`) VALUES (?, ?);", '1', '1')

function onPlayerQuit()
	exports.nameres:dbQueryAsync("onPlayerQuitCallback", {}, "test", "SELECT ID FROM ?? WHERE owner = ?", getAccountName(getPlayerAccount(source)))
end
function onPlayerQuitCallback(result, args)
	for _, row in ipairs(result) do
		destroyVehicle(vehiclesByID[row.ID])
	end
end
addEventHandler("onPlayerQuit", root, onPlayerQuit)

addEvent("dbCallback", false)
addEventHandler("dbCallback", resourceRoot, function(queryResult, callbackFunctionName, callbackArguments)
	_G[callbackFunctionName](queryResult, callbackArguments)
end)
]]

host = "IPHost" --"127.0.0.1" -- "localhost"
--unix_socket = "/var/run/mysqld/mysqld.sock"
dbname = "namedb"
user = "rootname"
password = "pass"

local unix_socket, host = unix_socket, host
local dbname, user, password = dbname, user, password
local mainDB

function connect()
	local startTick = getTickCount()
	mainDB = dbConnect("mysql", (unix_socket and "unix_socket="..unix_socket or "host="..host)..";dbname="..dbname, user, password)
	if (mainDB) then
		outputDebugString("[MYSQL] Connection: "..getTickCount()-startTick.." ms.")
	else
		outputDebugString("[MYSQL][ERROR] Connection failed!", 1)
		setTimer(connect, 5000, 1)
	end
end
connect()

_dbQuery = dbQuery
function dbQuery(timeout, tableName, query, ...)
	local result, errorCode, errorMessage = dbPoll(_dbQuery(mainDB, query, getResourceName(sourceResource).."_"..tableName, ...), timeout)
	if (not result) then
		outputDebugString (string.format("[MYSQL][ERROR] dbQuery error on %s (table `%s`)", query, tableName), 1)   
	end
	return result, errorCode, errorMessage
end

function dbQueryAsync(callbackFunctionName, callbackArguments, tableName, query, ...)
	local extraData = {
		sourceResourceRoot,
		callbackFunctionName,
		callbackArguments,
	}
	return _dbQuery(dbCallback, extraData, mainDB, query, getResourceName(sourceResource).."_"..tableName, ...)
end
function dbCallback(queryHandle, srcResRoot, callbackFunctionName, callbackArguments)
	local result, errorCode, errorMessage = dbPoll(queryHandle, 0)
	if (not result) then
		outputDebugString (string.format("[MYSQL][ERROR] dbCallback error %i (%s)", errorCode, errorMessage), 1)   
	end
	triggerEvent("dbCallback", srcResRoot, result, callbackFunctionName, callbackArguments)
end

_dbExec = dbExec
function dbExec(tableName, query, ...)
	-- We should also check if our database has fallen off, but unfortunately...
	return _dbExec(mainDB, query, getResourceName(sourceResource).."_"..tableName, ...)
end

function getTableName(tableName)
	return getResourceName(sourceResource).."_"..tableName
end

_dbPrepareString = dbPrepareString
function dbPrepareString(tableName, query, ...)
	return _dbPrepareString(mainDB, query, getResourceName(sourceResource).."_"..tableName, ...)
end

local multipleQueryTable = {}
function dbQueryAsyncMultiple(callbackFunctionName, callbackArguments, ...)
	local queries = {...}
	local packID = generateID()
	while (multipleQueryTable[packID]) do
		packID = generateID()
	end
	
	multipleQueryTable[packID] = {
		sourceResourceRoot = sourceResourceRoot,
		callbackFunctionName = callbackFunctionName,
		callbackArguments = callbackArguments,
		numberOfQueries = #queries,
		replies = {},
	}
	
	for queryNumber, query in ipairs(queries) do
		local extraData = {
			packID,
			queryNumber,
		}
		_dbQuery(multipleQueryCallback, extraData, mainDB, query.query, getResourceName(sourceResource).."_"..query.tableName, unpack(query))
	end
end

function multipleQueryCallback(queryHandle, packID, queryNumber)
	local result, errorCode, errorMessage = dbPoll(queryHandle, 0)
	if (not result) then
		outputDebugString(string.format("[MYSQL][ERROR] multipleQueryCallback error %i (%s)", errorCode, errorMessage), 1)   
	end
	
	local queryTable = multipleQueryTable[packID]
	queryTable.replies[queryNumber] = {
		result = result,
		errorCode = errorCode,
		errorMessage = errorMessage,
	}
	
	if (#queryTable.replies == queryTable.numberOfQueries) then
		triggerEvent("dbCallback", queryTable.sourceResourceRoot, queryTable.replies, queryTable.callbackFunctionName, queryTable.callbackArguments)
		multipleQueryTable[packID] = nil
	end
end

--[[
dbQueryAsyncMultiple(string callbackFunctionName, table callbackArguments, ...)
Where there is an ellipsis, there is a table of this kind for each request:
{
	string tableName,
	string query,
	arguments separated by commas
}

--The results will be displayed in a table, preserving the order of the executed queries. The table will look like this:
{
	{
		table result,
		number errorCode,
		string errorMessage,
	},
}
]]

-- Generating a string of characters
local symbols = {}
for _, range in ipairs({{48, 57}, {65, 90}, {97, 122}}) do -- numbers/lowercase chars/uppercase chars
	for i = range[1], range[2] do
		table.insert(symbols, string.char(i))
	end
end
local symbolCount = #symbols
function generateID()
	local str = ""
	for i = 1, 8 do
		str = str..symbols[math.random(1, symbolCount)]
	end
	return str
end
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.1-9.04817 | Added options 'log', 'tag' and 'suppress' |
| --- | --- |

| 1.3.5-9.06386 | Added option 'charset' |
| --- | --- |

| 1.5.2-9.07972 | Added option 'multi_statements' |
| --- | --- |

| 1.5.4-9.11138 | Added option 'queue' |
| --- | --- |

| 1.6.0-9.22396 | Added option 'use_ssl' |
| --- | --- |

| 1.6.0-9.22497 | Added option 'get_server_public_key' |
| --- | --- |

## See Also

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- dbConnect

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
