---
doc_id: "mta-wiki:3629"
title: "Modules/MTA-MySQL/mysql fetch field"
source_title: "Modules/MTA-MySQL/mysql fetch field"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_fetch_field"
revision_id: 24965
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql fetch field

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns a table with information about a field in a query result. You can call repeatedly this function to return all the result fields, and when it reaches the end returns nil. You can also go to a specific field using [mysql_field_seek()](mta://reference/misc/modules-mta-mysql-mysql-field-seek.md).

## Syntax

```
table mysql_fetch_field ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

A table with information about a field with the following keys:

- **name:** The name of this field.

- **org_name:** If you used aliases in the query, the original name of the field.

- **table:** The table of this field.

- **org_table:** If you used aliases for the table, the original name of the table.

- **length:** The maximum length allowed by this field in the table definition.

- **max_length:** The maximum length of this field in all the result rows.

- **not_null:** True if the field can't be NULL (See [mysql_null()](mta://reference/misc/modules-mta-mysql-mysql-null.md)).

- **primary_key:** True if the field is the table primary key.

- **unique_key:** True if the field value is unique.

- **multiple_key:** True if the field is part of a key.

- **numeric:** True if the field is numeric.

- **blob:** True if the field is a BLOB.

- **unsigned:** True if the field is unsigned.

- **zerofill:** True if the field is zero filled.

- **type:** A string representing the type of this field.

### Example

**Example 1:** This example shows how to print the rows of a result set showing the field name.

```
local result = mysql_query(handler, "SELECT * FROM account") -- Execute the query
for result,row in mysql_rows(result) do -- Iterate through all the result rows
  mysql_field_seek(result, 1) -- Reset the field cursor to the first field
  for k,v in ipairs(row) do
    local field = mysql_fetch_field(result) -- Retreive the field data
    if (v ~= mysql_null()) then
      outputDebugString("row[" .. field["name"] .. "] = " .. v)
    else
      outputDebugString("row[" .. field["name"] .. "] = NULL")
    end
  end
end
mysql_free_result(result) -- Free the result
```

## See also

- [mysql_data_seek](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

- mysql_fetch_field

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
