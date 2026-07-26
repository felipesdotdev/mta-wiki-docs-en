---
doc_id: "mta-wiki:3635"
title: "Modules/MTA-MySQL/mysql null"
source_title: "Modules/MTA-MySQL/mysql null"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_null"
revision_id: 24981
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql null

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns a MySQL null type. MySQL NULL and lua nil are different concepts, and a table row can contain NULL values. In this case, you must check the value comparing it to mysql_null.

## Syntax

```
MySQLNullValue mysql_null ( )
```

### Returns

A MySQL NULL type.

### Example

**Example 1:** This example checks if the name of an account is null.

```
local result = mysql_query(handler, "SELECT name FROM account WHERE id='1' LIMIT 1") -- Execute the query
if (mysql_result(result, 1, 1) == mysql_null()) then
  outputDebugString("The name of the account #1 is null")
end
mysql_free_result(result) -- Free the result
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

- [mysql_field_name](mta://reference/misc/modules-mta-mysql-mysql-field-name.md)

- [mysql_field_seek](mta://reference/misc/modules-mta-mysql-mysql-field-seek.md)

- [mysql_field_tell](mta://reference/misc/modules-mta-mysql-mysql-field-tell.md)

- [mysql_num_fields](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)

- [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)

- [mysql_result](mta://reference/misc/modules-mta-mysql-mysql-result.md)

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- mysql_null
