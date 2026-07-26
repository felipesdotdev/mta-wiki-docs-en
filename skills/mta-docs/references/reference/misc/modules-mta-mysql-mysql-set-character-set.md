---
doc_id: "mta-wiki:3613"
title: "Modules/MTA-MySQL/mysql set character set"
source_title: "Modules/MTA-MySQL/mysql set character set"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_set_character_set"
revision_id: 24961
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql set character set

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Changes the character set used for the current MySQL session.

## Syntax

```
bool mysql_set_character_set ( MySQLConnection handler, string charset_name )
```

### Required arguments

- **handler:** A valid MySQL link

- **charset_name:** The new character set name

### Returns

It it succeeds returns true, in other case returns false.

## Example

**Example 1:**

```
handler = mysql_connect("localhost", "user", "password", "mta_users")
if (not handler) then
  outputDebugString("Unable to connect to the MySQL server")
elseif (not mysql_set_character_set(handler, "utf8")) then -- Change the charset to UTF-8
  outputDebugString("Unable to change the connection character set to utf8: ("
                    .. mysql_errno(handler) .. ")" .. mysql_error(handler))
  mysql_close(handler) -- Close the connection afther the error
end
```

## See also

- [mysql_connect](mta://reference/misc/modules-mta-mysql-mysql-connect.md)

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

- mysql_set_character_set

- [mysql_stat](mta://reference/misc/modules-mta-mysql-mysql-stat.md)

- [mysql_warning_count](mta://reference/misc/modules-mta-mysql-mysql-warning-count.md)
