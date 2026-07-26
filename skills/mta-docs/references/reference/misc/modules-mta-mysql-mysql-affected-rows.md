---
doc_id: "mta-wiki:3598"
title: "Modules/MTA-MySQL/mysql affected rows"
source_title: "Modules/MTA-MySQL/mysql affected rows"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_affected_rows"
revision_id: 24947
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql affected rows

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns the number of changed rows (for UPDATE), inserted rows (for INSERT) or deleted rows (for DELETE) in the last query. For SELECT statements it works like [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md).

## Syntax

```
int mysql_affected_rows ( MySQLConnection handler )
```

### Required arguments

- **handler:** A valid MySQL link

### Returns

The number of affected rows in the last query.

## Example

**Example 1:** This example shows the number of deleted rows after deleting all accounts starting with 'A'

```
mysql_query(handler, "DELETE FROM account WHERE name LIKE 'A%'")
outputDebugString("We deleted a total of " .. mysql_affected_rows(handle) .. " accounts starting with 'A'")
```

## See also

- [mysql_connect](mta://reference/misc/modules-mta-mysql-mysql-connect.md)

- [mysql_close](mta://reference/misc/modules-mta-mysql-mysql-close.md)

- [mysql_errno](mta://reference/misc/modules-mta-mysql-mysql-errno.md)

- [mysql_error](mta://reference/misc/modules-mta-mysql-mysql-error.md)

- [mysql_ping](mta://reference/misc/modules-mta-mysql-mysql-ping.md)

- [mysql_select_db](mta://reference/misc/modules-mta-mysql-mysql-select-db.md)

- [mysql_escape_string](mta://reference/misc/modules-mta-mysql-mysql-escape-string.md)

- mysql_affected_rows

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
