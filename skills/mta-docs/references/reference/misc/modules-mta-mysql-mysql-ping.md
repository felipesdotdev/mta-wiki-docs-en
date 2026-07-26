---
doc_id: "mta-wiki:3592"
title: "Modules/MTA-MySQL/mysql ping"
source_title: "Modules/MTA-MySQL/mysql ping"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_ping"
revision_id: 53013
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql ping

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Checks if the given MySQL connection is still alive.

## Syntax

```
bool mysql_ping ( MySQLConnection handler )
```

### Required arguments

- **handler:** A valid MySQL link

### Returns

true is the connection is still alive, false if not.

## Example

**Example 1:** This example checks if the MySQL connection is still alive when a player connects, to be able to fetch their data.

```
myhandler = mysql_connect("localhost", "user", "password", "mta_users")

function checkMySQLConnection ( )
  if (mysql_ping(myhandler) == false) then -- We lost the connection to the MySQL server
    outputDebugString("Lost connection to the MySQL server, reconnecting ...")
    mysql_close(myhandler)
    myhandler = mysql_connect("localhost", "user", "password", "mta_users") -- Reconnect to the MySQL server
  end
end

addEventHandler("onPlayerJoin", getRootElement(), checkMySQLConnection)
```

## See also

- [mysql_connect](mta://reference/misc/modules-mta-mysql-mysql-connect.md)

- [mysql_close](mta://reference/misc/modules-mta-mysql-mysql-close.md)

- [mysql_errno](mta://reference/misc/modules-mta-mysql-mysql-errno.md)

- [mysql_error](mta://reference/misc/modules-mta-mysql-mysql-error.md)

- mysql_ping

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
