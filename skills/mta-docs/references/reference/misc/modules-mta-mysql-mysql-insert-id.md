---
doc_id: "mta-wiki:3609"
title: "Modules/MTA-MySQL/mysql insert id"
source_title: "Modules/MTA-MySQL/mysql insert id"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_insert_id"
revision_id: 24958
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql insert id

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns the value generated for an AUTO_INCREMENT field in the last query.

For more information about when is this value updated visit [http://dev.mysql.com/doc/refman/5.0/en/mysql-insert-id.html](http://dev.mysql.com/doc/refman/5.0/en/mysql-insert-id.html)

## Syntax

```
int mysql_insert_id ( MySQLConnection handler )
```

### Required arguments

- **handler:** A valid MySQL link

### Returns

The value generated for an AUTO_INCREMENT field in the last query.

## Example

**Example 1:** This example creates an account for a player when they use /register, and tells them their database id.

```
function RegisterPlayer(playerSource, commandName, _password)
  local name = mysql_escape_string(handler, getPlayerName(playerSource)) -- Escape the strings to avoid SQL-Injection
  local password = mysql_escape_string(handler, _password)
  local query = "INSERT INTO account SET name='" .. name .. "', password=MD5('" .. password .. "')"

  if (mysql_query(handler, query)) then
    outputChatBox("Account created successfuly with id #" .. mysql_insert_id(handler), playerSource)
  else
    outputChatBox("An error has occured when trying to create your account.", playerSource)
  end
end

addCommandHandler("register", RegisterPlayer)
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

- mysql_insert_id

- [mysql_query](mta://reference/misc/modules-mta-mysql-mysql-query.md)

- [mysql_unbuffered_query](mta://reference/misc/modules-mta-mysql-mysql-unbuffered-query.md)

- [mysql_set_character_set](mta://reference/misc/modules-mta-mysql-mysql-set-character-set.md)

- [mysql_stat](mta://reference/misc/modules-mta-mysql-mysql-stat.md)

- [mysql_warning_count](mta://reference/misc/modules-mta-mysql-mysql-warning-count.md)
