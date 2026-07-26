---
doc_id: "mta-wiki:3636"
title: "Modules/MTA-MySQL/mysql fetch assoc"
source_title: "Modules/MTA-MySQL/mysql fetch assoc"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_fetch_assoc"
revision_id: 24971
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.181543+00:00"
---

# Modules/MTA-MySQL/mysql fetch assoc

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns an associative table containing the current row of the last executed query. You can call this function repeatedly to retreive all the result rows. When there aren't more rows in the result it returns nil. You can go to a specific row calling [mysql_data_seek()](mta://reference/misc/modules-mta-mysql-mysql-data-seek.md)

## Syntax

```
table mysql_fetch_assoc ( MySQLResult result )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

An associative table with the current row

### Example

**Example 1:** This example shows the name of all the registered accounts

```
local result = mysql_query(handler, "SELECT * FROM account") -- Execute the query
if (result) then
  while true do
    local row = mysql_fetch_assoc(result)
    if (not row) then break end

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

- mysql_fetch_assoc

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
