---
doc_id: "mta-wiki:3630"
title: "Modules/MTA-MySQL/mysql fields"
source_title: "Modules/MTA-MySQL/mysql fields"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_fields"
revision_id: 24967
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.334353+00:00"
---

# Modules/MTA-MySQL/mysql fields

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Creates an iterator for the result fields. When this function is called, the field cursor is set to the first field.

## Syntax

```
iterator mysql_fields ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

An iterator function to iterate all the result fields.

### Example

**Example 1:** This example shows how to print the rows of a result set showing the field name.

```
local result = mysql_query(handler, "SELECT * FROM account") -- Execute the query
for result,row in mysql_rows(result) do -- Iterate through all the result rows
  local i = 1
  for result,field in mysql_fields(result) do
    if (row[i] ~= mysql_null()) then
      outputDebugString("row[" .. field["name"] .. "] = " .. row[i])
    else
      outputDebugString("row[" .. field["name"] .. "] = NULL")
    end
    i = i + 1
  end
end
mysql_free_result(result) -- Free the result
```

## See also

- [mysql_data_seek](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

- [mysql_fetch_field](mta://reference/misc/modules-mta-mysql-mysql-fetch-field.md)

- mysql_fields

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
