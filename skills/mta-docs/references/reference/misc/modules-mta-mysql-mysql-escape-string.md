---
doc_id: "mta-wiki:3597"
title: "Modules/MTA-MySQL/mysql escape string"
source_title: "Modules/MTA-MySQL/mysql escape string"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_escape_string"
revision_id: 24946
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql escape string

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Escapes a query string to avoid sql injection attacks. This function should be used for every executed query that uses any data given by the players.

## Syntax

```
string mysql_escape_string( MySQLConnection handler, string theString )
```

### Required arguments

- **handler:** A valid MySQL link

- **theString:** The string to escape

### Returns

The escaped string

## Example

**Example 1:** This example returns some offline player cash getting it from the database

```
function checkOfflineMoney(playerSource, commandName, targetName)
  local escapedName = mysql_escape_string(handler, targetName) -- Escape the string to avoid security holes
  local result = mysql_query(handler, "SELECT money FROM account WHERE name='" .. escapedName .. "'")
  if (not result) then
    outputDebugString("mysql_query failed: (" .. mysql_errno(handler) .. ") " .. mysql_error(handler)) -- Some error occurred
  else
    if (mysql_num_rows(result) == 0) then outputChatBox("Account not found", playerSource) -- We haven't results with that name
    else outputChatBox("The player has " .. mysql_result(result, 1, 1) .. "$", playerSource) end -- Send the money information
    mysql_free_result(result) -- Free the query result
  end
end
addCommandHandler("offlinecash", checkOfflineMoney)
```

## See also

- [mysql_connect](mta://reference/misc/modules-mta-mysql-mysql-connect.md)

- [mysql_close](mta://reference/misc/modules-mta-mysql-mysql-close.md)

- [mysql_errno](mta://reference/misc/modules-mta-mysql-mysql-errno.md)

- [mysql_error](mta://reference/misc/modules-mta-mysql-mysql-error.md)

- [mysql_ping](mta://reference/misc/modules-mta-mysql-mysql-ping.md)

- [mysql_select_db](mta://reference/misc/modules-mta-mysql-mysql-select-db.md)

- mysql_escape_string

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
