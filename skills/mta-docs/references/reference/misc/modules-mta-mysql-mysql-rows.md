---
doc_id: "mta-wiki:3633"
title: "Modules/MTA-MySQL/mysql rows"
source_title: "Modules/MTA-MySQL/mysql rows"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_rows"
revision_id: 24970
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql rows

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Creates an iterator for the result rows. When this function is called, the row cursor is set to the first result row.

## Syntax

```
iterator mysql_rows ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

An iterator function to iterate all the result rows.

### Example

**Example 1:** This example prints all the accounts names

```
local result = mysql_query(handler, "SELECT name FROM account") -- Execute the query
if (result) then
  for result,row in mysql_rows(result) do
    outputDebugString(row[1])
  end
  mysql_free_result(result) -- Free the result
end
```

## See also

- [mysql_data_seek](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

- [mysql_fetch_field](mta://reference/misc/modules-mta-mysql-mysql-fetch-field.md)

- [mysql_fields](mta://reference/misc/modules-mta-mysql-mysql-fields.md)

- [mysql_fetch_lengths](mta://reference/misc/modules-mta-mysql-mysql-fetch-lengths.md)

- [mysql_fetch_row](mta://reference/misc/modules-mta-mysql-mysql-fetch-row.md)

- mysql_rows

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
