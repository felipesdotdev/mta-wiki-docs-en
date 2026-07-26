---
doc_id: "mta-wiki:2324"
title: "Modules/MySQL/MysqlOpen"
source_title: "MysqlOpen"
source_url: "https://wiki.multitheftauto.com/wiki/MysqlOpen"
revision_id: 21619
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.938057+00:00"
---

# Modules/MySQL/MysqlOpen

|  | This function is provided by the external module MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

This function opens a MySQL connection to a specific database on a database server. As soon as a connection is made (or timed out), the callback_function you passed as parameter is called and you can read/write to the database by using the [mysqlQuery](mta://reference/misc/mysqlquery.md) function.

## Syntax

```
bool mysqlOpen ( mysql mysqlobj, string callback_function, string host, string user, string password, string database_name, int port )
```

### Required Arguments

- **mysqlobj** : mysql object (requires an established connection)

- **callback_function** : The function that is called if the operation is done (see below)

- **host** : The database server hostname or IP address to use

- **user** : The database username to use

- **password** : The database password to use

- **database_name** : The database name to use

- **port** : The database server port (MySQL default port is *3306*)

### Callback Arguments

Your callback function has to accept the following arguments:

- **bool** result : Returns false on error, true on success

### Optional Arguments

*None*

## Example

```
function onMySQLOpen ( result )
	if ( result ) then
		outputServerLog ( "MySQL connection established." )
	else
		outputServerLog ( "MySQL connection failed." )
	end
end

function mysqltest ()
	db = mysqlCreate ()
	mysqlOpen ( db, "onMySQLOpen", "localhost", "bastage", "bastage_pw", "test", 3306 )
end
```
