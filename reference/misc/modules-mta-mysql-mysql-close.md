---
doc_id: "mta-wiki:3587"
title: "Modules/MTA-MySQL/mysql close"
source_title: "Modules/MTA-MySQL/mysql close"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_close"
revision_id: 53002
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.082402+00:00"
---

# Modules/MTA-MySQL/mysql close

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Closes an established connection to a MySQL server.

## Syntax

```
mysql_close ( MySQLConnection handler )
```

### Required arguments

- **handler:** A valid MySQL link

### Returns

This function doesn't return any value

## Example

**Example 1:** This example makes a MySQL connection and then closes it

```
handler = mysql_connect("localhost", "username", "password", "mta_users") -- Establish the connection
if ( not handler ) then -- The connection failed
  outputDebugString("Unable to connect to the MySQL server")
else
  mysql_close(handler) -- Close the connection
end
```

## See also

- [mysql_connect](mta://reference/misc/modules-mta-mysql-mysql-connect.md)

- mysql_close

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
