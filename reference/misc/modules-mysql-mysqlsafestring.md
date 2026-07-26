---
doc_id: "mta-wiki:2469"
title: "Modules/MySQL/MysqlSafeString"
source_title: "Modules/MySQL/MysqlSafeString"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MySQL/MysqlSafeString"
revision_id: 21622
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.835238+00:00"
---

# Modules/MySQL/MysqlSafeString

|  | This function is provided by the external module MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

This function escapes a given string so it's safe to pass as a query to [mysqlQuery](mta://reference/misc/modules-mysql-mysqlquery.md). Please use this as sanity checking function to prevent bad things like SQL injection.

The function needs an already established connection to a MySQL database, because it reads out the character set from that database to escape the string.

## Syntax

```
string mysqlSafeString ( mysql mysqlobj, string query )
```

### Required Arguments

- **mysqlobj** : A *mysql* object created by [mysqlCreate](mta://reference/misc/modules-mysql-mysqlcreate.md)

- **query** : The MySQL query that needs to be escasped

### Optional Arguments

*None*

## Example

```
function onMySQLOpen ( result )
	if ( result ) then
		outputServerLog ( "MySQL connection established." )
		-- do the safe query
		local safe = mysqlSafeString ( db, some_string_passed_by_a_user )
		mysqlQuery ( db, "onMySQLResult", "SELECT ".. safe .." FROM test" )
	else
		outputServerLog ( "MySQL connection failed." )
	end
end

function mysqltest ()
	db = mysqlCreate ()
	mysqlOpen ( db, "onMySQLOpen", "localhost", "bastage", "bastage_pw", "test", 3306 )
end
```
