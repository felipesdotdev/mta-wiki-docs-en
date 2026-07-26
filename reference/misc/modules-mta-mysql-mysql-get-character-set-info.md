---
doc_id: "mta-wiki:3600"
title: "Modules/MTA-MySQL/mysql get character set info"
source_title: "Modules/MTA-MySQL/mysql get character set info"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_get_character_set_info"
revision_id: 24949
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.370128+00:00"
---

# Modules/MTA-MySQL/mysql get character set info

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Retreives information about a character set

## Syntax

```
string, string, string, string, int, int mysql_get_character_set_info ( MySQLConnection handler, string character_set_name )
```

### Required arguments

- **handler:** A valid MySQL link

- **character_set_name:** The character set name

### Returns

The character set information:

- The charset name

- The charset collation

- The charset comment

- The charset directory

- Multi byte character min. length

- Multi byte character max. length

## Example

**Example 1:**

```
local name, collation, comment, directory, mbminlen, mbmaxlen =
      mysql_get_character_set_info(handler, "utf8") -- We will return information about the charset "utf8"

outputDebugString("UTF-8 charset information:\n" ..
                  "name: " .. name .. "\n" ..
                  "collation: " .. collation .. "\n" ..
                  "comment: " .. comment .. "\n" ..
                  "directory: " .. directory .. "\n" ..
                  "mbminlen: " .. mbminlen .. "\n" ..
                  "mbmaxlen: " .. mbmaxlen)
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

- mysql_get_character_set_info

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
