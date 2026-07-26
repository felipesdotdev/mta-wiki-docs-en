---
doc_id: "mta-wiki:3639"
title: "Modules/MTA-MySQL/mysql field name"
source_title: "Modules/MTA-MySQL/mysql field name"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_field_name"
revision_id: 24974
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.285110+00:00"
---

# Modules/MTA-MySQL/mysql field name

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns the name of a given field in the last executed query. The offset of the field must be an integer between **1** and **[mysql_num_fields()](https://wiki.multitheftauto.com/index.php?title=Modules/MTA-MySQL/mysql_num_rows/mysql_num_fields&action=edit&redlink=1)**

## Syntax

```
int mysql_field_name ( MySQLResult result, int offset )
```

### Required arguments

- **result:** A valid MySQL result

- **offset:** A valid offset

### Returns

The given field name.

### Example

**Example 1:**

```
local result = mysql_query(handler, "SELECT name FROM account WHERE id='1' LIMIT 1") -- Execute the query
if (result) then
  local str = mysql_field_name(result, 1)
  outputDebugString(str) -- Will print 'name'
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

- [mysql_rows_assoc](mta://reference/misc/modules-mta-mysql-mysql-rows-assoc.md)

- [mysql_field_length](mta://reference/misc/modules-mta-mysql-mysql-field-length.md)

- mysql_field_name

- [mysql_field_seek](mta://reference/misc/modules-mta-mysql-mysql-field-seek.md)

- [mysql_field_tell](mta://reference/misc/modules-mta-mysql-mysql-field-tell.md)

- [mysql_num_fields](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)

- [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)

- [mysql_result](mta://reference/misc/modules-mta-mysql-mysql-result.md)

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)
