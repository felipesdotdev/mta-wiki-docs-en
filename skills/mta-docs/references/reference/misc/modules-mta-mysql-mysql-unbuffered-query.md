---
doc_id: "mta-wiki:3611"
title: "Modules/MTA-MySQL/mysql unbuffered query"
source_title: "Modules/MTA-MySQL/mysql unbuffered query"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_unbuffered_query"
revision_id: 24960
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql unbuffered query

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Executes an unbuffered query in the server and retreives the result.

```
IMPORTANT: It is strongly recommended to call mysql_free_result after a query,
specially if it returns some data. Query results can be automatically deleted
by the lua garbage collector, so if you forget to free a result it will be
freed at some time in the future, but it doesn't know the real result data size
in memory so it can delay the memory destroying more than it should.
```

```
IMPORTANT: Unbuffered queries are to iterate a set of results improving the
performance since they are not pre-loaded in memory, so if you execute an unbuffered
query you must iterate all the result rows. For more information about unbuffered
queries visit http://dev.mysql.com/doc/refman/5.0/en/mysql-use-result.html
```

## Syntax

```
MySQLResult mysql_unbuffered_query ( MySQLConnection handler, string query )
```

### Required arguments

- **handler:** A valid MySQL link

- **query:** The executing query

### Returns

In case of error this function returns nil. IF not, a MySQLResult handler. Check the MySQL result managing functions to see how to retreive the data from it.

## Example

**Example 1:**

```
local result = mysql_unbuffered_query(handler, "SELECT * FROM some_table")
if (not result) then
  outputDebugString("Error executing the query: (" .. mysql_errno(handler) .. ") " .. mysql_error(handler))
else
  local numrows = 0
  for result,row in mysql_rows(result) do -- We MUST iterate all the query resulting rows
    numrows = numrows + 1
  end
  outputDebugString("The query returned a total of " .. numrows .. " rows")
  mysql_free_result(result) -- Freeing the result is IMPORTANT
end
```

## See also

### Result managing functions

- [mysql_data_seek](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

- [mysql_fetch_field](mta://reference/misc/modules-mta-mysql-mysql-fetch-field.md)

- [mysql_fields](mta://reference/misc/modules-mta-mysql-mysql-fields.md)

- [mysql_fetch_lengths](mta://reference/misc/modules-mta-mysql-mysql-fetch-lengths.md)

- [mysql_fetch_row](mta://reference/misc/modules-mta-mysql-mysql-fetch-row.md)

- [mysql_rows](mta://reference/misc/modules-mta-mysql-mysql-rows.md)

- [mysql_fetch_assoc](mta://reference/misc/modules-mta-mysql-mysql-fetch-assoc.md)

- [mysql_rows_assoc](mta://reference/misc/modules-mta-mysql-mysql-rows-assoc.md)

- [mysql_field_length](mta://reference/misc/modules-mta-mysql-mysql-field-length.md)

- [mysql_field_name](mta://reference/misc/modules-mta-mysql-mysql-field-name.md)

- [mysql_field_seek](mta://reference/misc/modules-mta-mysql-mysql-field-seek.md)

- [mysql_field_tell](mta://reference/misc/modules-mta-mysql-mysql-field-tell.md)

- [mysql_num_fields](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)

- [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)

- [mysql_result](mta://reference/misc/modules-mta-mysql-mysql-result.md)

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)

### MySQL handler functions

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

- mysql_unbuffered_query

- [mysql_set_character_set](mta://reference/misc/modules-mta-mysql-mysql-set-character-set.md)

- [mysql_stat](mta://reference/misc/modules-mta-mysql-mysql-stat.md)

- [mysql_warning_count](mta://reference/misc/modules-mta-mysql-mysql-warning-count.md)
