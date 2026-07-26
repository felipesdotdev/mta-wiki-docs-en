---
doc_id: "mta-wiki:3631"
title: "Modules/MTA-MySQL/mysql fetch lengths"
source_title: "Modules/MTA-MySQL/mysql fetch lengths"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_fetch_lengths"
revision_id: 24968
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql fetch lengths

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns a table containing the length of the values of the last retreived row. If you didn't retreive any row or you are in the end of the result set, it returns nil.

## Syntax

```
table mysql_fetch_lengths ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

A table with the length of the values of the last retreived row.

### Example

**Example 1:** This example shows the length of an account name

```
local result = mysql_query(handler, "SELECT name FROM account WHERE id='1' LIMIT 1") -- Execute the query
if (result) then
  local row = mysql_fetch_row(result) -- Return the resulting row
  local lengths = mysql_fetch_lengths(result) -- Retreive the lengths of the result fields
  outputDebugString("The length of " .. row[1] .. " is " .. lengths[1])
  mysql_free_result(result) -- Free the result
end
```

## See also

- [mysql_data_seek](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

- [mysql_fetch_field](mta://reference/misc/modules-mta-mysql-mysql-fetch-field.md)

- [mysql_fields](mta://reference/misc/modules-mta-mysql-mysql-fields.md)

- mysql_fetch_lengths

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
