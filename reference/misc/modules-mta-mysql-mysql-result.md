---
doc_id: "mta-wiki:3642"
title: "Modules/MTA-MySQL/mysql result"
source_title: "Modules/MTA-MySQL/mysql result"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_result"
revision_id: 24979
language: "en"
categories: []
generated_at: "2026-07-26T16:16:13.633075+00:00"
---

# Modules/MTA-MySQL/mysql result

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns a string with the value of the given field with the given offsets, being these:

- **row_offset**: An integer value between **1** and **[mysql_num_rows()](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)**

- **field_offset**: An integer value between **1** and **[mysql_num_fields()](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)**

If the offset is invalid it returns nil.

## Syntax

```
string mysql_result ( MySQLResult result, int row_offset, int field_offset )
```

### Required arguments

- **result:** A valid MySQL result

### Returns

A string with the data contained in the given offset.

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

- mysql_result

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)
