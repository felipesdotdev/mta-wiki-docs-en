---
doc_id: "mta-wiki:2470"
title: "Modules/MySQL/MysqlCreate"
source_title: "Modules/MySQL/MysqlCreate"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MySQL/MysqlCreate"
revision_id: 21620
language: "en"
categories: []
---

# Modules/MySQL/MysqlCreate

|  | This function is provided by the external module MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

This function creates a MySQL object which you can use to communicate with a database.

## Syntax

```
mysql mysqlCreate ( )
```

### Required Arguments

*None*

### Optional Arguments

*None*

## Example

```
function onMySQLOpen ( result )
	if ( result ) then
		outputServerLog ( "MySQL connection established." )
		mysqlQuery ( db, "onMySQLResult", "SELECT * FROM test" )
	else
		outputServerLog ( "MySQL connection failed." )
	end
end

function mysqltest ()
	db = mysqlCreate ()
	mysqlOpen ( db, "onMySQLOpen", "localhost", "bastage", "bastage_pw", "test", 3306 )
end
```
