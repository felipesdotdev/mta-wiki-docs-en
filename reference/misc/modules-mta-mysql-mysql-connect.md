---
doc_id: "mta-wiki:3584"
title: "Modules/MTA-MySQL/mysql connect"
source_title: "Modules/MTA-MySQL/mysql connect"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_connect"
revision_id: 52990
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:13.103022+00:00"
---

# Modules/MTA-MySQL/mysql connect

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Makes a connection to a MySQL server and returns a handler to it.

## Syntax

```
MySQLConnection mysql_connect ( string hostname, string username, string password, string database, [ int port=3306, string unix_socket=nil, string client_flags=""] )
```

### Required arguments

- **hostname:** The hostname to connect to

- **username:** The database username

- **password:** The username password

- **database:** The starting database

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **port**: The MySQL port

- **unix_socket**: When connecting in unix systems to a local database, the path for the unix socket (usually /var/run/mysqld/mysqld.sock)

- **client_flags**: The connection flags, with the format *"flag1|flag2|flag3"*. The list of flags is:

- **compress:** Use compression protocol.

- **found_rows:** Return the number of found (matched) rows, not the number of changed rows.

- **ignore_sigpipe:** Prevents the client library from installing a SIGPIPE  signal handler. This can be used to avoid conflicts with a handler that the application has already installed.

- **ignore_space:** Allow spaces after function names. Makes all functions names reserved words.

- **interactive:** Allow interactive_timeout seconds (instead of wait_timeout seconds) of inactivity before closing the connection. The client's session wait_timeout  variable is set to the value of the session interactive_timeout variable.

- **local_files:** Enable LOAD DATA LOCAL handling.

- **no_schema:** Don't allow the db_name.tbl_name.col_name  syntax. This is for ODBC. It causes the parser to generate an error if you use that syntax, which is useful for trapping bugs in some ODBC programs.

### Returns

A valid MySQL handler if it was able to connect, or nil if it was unable.

## Example

**Example 1:** This example makes a MySQL connection and checks if it was succesful.

```
handler = mysql_connect("localhost", "username", "password", "mta_users") -- Establish the connection
if ( not handler ) then -- The connection failed
  outputDebugString("Unable to connect to the MySQL server")
else
  mysql_close(handler) -- Close the connection
end
```

**Example 2:** This example makes a MySQL connection and set charset

```
local charset = "utf8";
local handler = mysql_connect("127.0.0.1", "username", "password", "database", 3306, "/var/lib/libmysqlclient.so.15", "")

if (handler) then
	mysql_query(handler, "SET NAMES '"..charset.."'")
	mysql_query(handler, "SET OPTION CHARACTER SET "..charset.."")
	mysql_query(handler, "SET CHARACTER SET '"..charset.."'")
end
```

## See also

- mysql_connect

- [mysql_close](mta://reference/misc/modules-mta-mysql-mysql-close.md)

- [mysql_errno](mta://reference/misc/modules-mta-mysql-mysql-errno.md)

- [mysql_error](mta://reference/misc/modules-mta-mysql-mysql-error.md)

- [mysql_ping](mta://reference/misc/modules-mta-mysql-mysql-ping.md)

- [mysql_select_db](mta://reference/misc/modules-mta-mysql-mysql-select-db.md)

- [mysql_escape_string](mta://reference/misc/modules-mta-mysql-mysql-escape-string.md)

- [mysql_affected_rows](mta://reference/misc/modules-mta-mysql-mysql-affected-rows.md)

- [mysql_change_user](mta://reference/misc/modules-mta-mysql-mysql-change-user.md)

- [mysql_get_character_set_info](mta://reference/misc/modules-mta-mysql-mysql-get-character-set-info.md)

- [mysql_get_client_info](mta://reference/misc/modules-mta-mysql-mysql-get-client-info.md)

- [mysql_get_client_version](mta://reference/misc/modules-mta-mysql-mysql-get-client-version.md)

- [mysql_get_host_info](mta://reference/misc/modules-mta-mysql-mysql-get-host-info.md)

- [mysql_get_proto_info](mta://reference/misc/modules-mta-mysql-mysql-get-proto-info.md)

- [mysql_get_server_info](mta://reference/misc/modules-mta-mysql-mysql-get-server-info.md)

- [mysql_get_server_version](mta://reference/misc/modules-mta-mysql-mysql-get-server-version.md)

- [mysql_hex_string](mta://reference/misc/modules-mta-mysql-mysql-hex-string.md)

- [mysql_info](mta://reference/misc/modules-mta-mysql-mysql-info.md)

- [mysql_insert_id](mta://reference/misc/modules-mta-mysql-mysql-insert-id.md)

- [mysql_query](mta://reference/misc/modules-mta-mysql-mysql-query.md)

- [mysql_unbuffered_query](mta://reference/misc/modules-mta-mysql-mysql-unbuffered-query.md)

- [mysql_set_character_set](mta://reference/misc/modules-mta-mysql-mysql-set-character-set.md)

- [mysql_stat](mta://reference/misc/modules-mta-mysql-mysql-stat.md)

- [mysql_warning_count](mta://reference/misc/modules-mta-mysql-mysql-warning-count.md)
