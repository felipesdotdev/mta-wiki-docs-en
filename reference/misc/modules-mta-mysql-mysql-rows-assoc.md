---
doc_id: "mta-wiki:3637"
title: "Modules/MTA-MySQL/mysql rows assoc"
source_title: "Modules/MTA-MySQL/mysql rows assoc"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_rows_assoc"
revision_id: 24972
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.668848+00:00"
---

# Modules/MTA-MySQL/mysql rows assoc

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Creates an iterator for the result associative rows. When this function is called, the row cursor is set to the first result row.

## Syntax

```
iterator mysql_rows_assoc ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

An iterator function to iterate all the result rows in associative tables.

### Example

**Example 1:** This example prints all the accounts names

```
local result = mysql_query(handler, "SELECT * FROM account") -- Execute the query
if (result) then
  for result,row in mysql_rows_assoc(result) do
    outputDebugString(row["name"])
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

- [mysql_rows](mta://reference/misc/modules-mta-mysql-mysql-rows.md)

- [mysql_fetch_assoc](mta://reference/misc/modules-mta-mysql-mysql-fetch-assoc.md)

- mysql_rows_assoc

- [mysql_field_length](mta://reference/misc/modules-mta-mysql-mysql-field-length.md)

- [mysql_field_name](mta://reference/misc/modules-mta-mysql-mysql-field-name.md)

- [mysql_field_seek](mta://reference/misc/modules-mta-mysql-mysql-field-seek.md)

- [mysql_field_tell](mta://reference/misc/modules-mta-mysql-mysql-field-tell.md)

- [mysql_num_fields](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)

- [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)

- [mysql_result](mta://reference/misc/modules-mta-mysql-mysql-result.md)

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)
