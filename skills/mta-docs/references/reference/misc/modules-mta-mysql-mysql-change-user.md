---
doc_id: "mta-wiki:3599"
title: "Modules/MTA-MySQL/mysql change user"
source_title: "Modules/MTA-MySQL/mysql change user"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_change_user"
revision_id: 44522
language: "en"
categories: ["Utility_templates"]
---

# Modules/MTA-MySQL/mysql change user

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Changes the current MySQL session authentication.

## Syntax

```
bool mysql_change_user ( MySQLConnection handler, string new_username, string new_password [, string new_database ] )
```

### Required arguments

- **handler:** A valid MySQL link

- **new_username:** The new username

- **new_password:** The new username password

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **new_database:** Start the new session using a new default database

### Returns

It it succeeds returns true, in other case returns false

## Example

**Example 1:**

```
function resourceStart ( res )
  if (res == getThisResource()) then
    myhandler = mysql_connect("localhost", "writer_user", "password", "mta_users") -- Start with a read-write username
    if (not myhandler) then
      outputDebugString("Unable to connect to the database: (" .. mysql_errno(handler) .. ") " .. mysql_error(handler))
    else
      -- Apply some changes to the database here
      if (not mysql_change_user(myhandler, "localhost", "reader_user", "password", "mta_users")) then -- Change to a read-only user
        outputDebugString("Unable to set the database read-only user: (" ..
                           mysql_errno(handler) .. ") " .. mysql_error(handler))
        mysql_close(myhandler) -- Close the MySQL connection
      end
    end
  end
end

addEventHandler("onResourceStart", getRootElement(), resourceStart)
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

- mysql_change_user

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
