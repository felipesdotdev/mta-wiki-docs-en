---
doc_id: "mta-wiki:3607"
title: "Modules/MTA-MySQL/mysql hex string"
source_title: "Modules/MTA-MySQL/mysql hex string"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_hex_string"
revision_id: 24956
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql hex string

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Converts a string to an hexadecimal representation of it. It is useful to insert binary data in blob fields, or to retreive and show it in your resources. It doesn't append '0x' or 'X' to the retreived string, the programmer must add it.

## Syntax

```
string mysql_hex_string ( string theString )
```

### Required arguments

- **theString:** The string to convert

### Returns

An hexadecimal formatted string.

## Example

**Example 1:** This function receives a string with a binary file content and stores it in a blob field of the database.

```
function savePlayerAvatar(playerName, imgRawData)
  local imgHexData = mysql_hex_string(imgRawData)
  mysql_query(handler, "UPDATE account SET avatar='0x" .. imgHexData .. "' WHERE name='" .. playerName .. "'")
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

- mysql_hex_string

- [mysql_info](mta://reference/misc/modules-mta-mysql-mysql-info.md)

- [mysql_insert_id](mta://reference/misc/modules-mta-mysql-mysql-insert-id.md)

- [mysql_query](mta://reference/misc/modules-mta-mysql-mysql-query.md)

- [mysql_unbuffered_query](mta://reference/misc/modules-mta-mysql-mysql-unbuffered-query.md)

- [mysql_set_character_set](mta://reference/misc/modules-mta-mysql-mysql-set-character-set.md)

- [mysql_stat](mta://reference/misc/modules-mta-mysql-mysql-stat.md)

- [mysql_warning_count](mta://reference/misc/modules-mta-mysql-mysql-warning-count.md)
