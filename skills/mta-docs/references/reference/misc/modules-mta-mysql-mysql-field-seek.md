---
doc_id: "mta-wiki:3640"
title: "Modules/MTA-MySQL/mysql field seek"
source_title: "Modules/MTA-MySQL/mysql field seek"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_field_seek"
revision_id: 24975
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql field seek

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Sets the field cursor of a result in the given field offset. The offset must be a value between **1** and **[mysql_num_fields()](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)**.

## Syntax

```
int mysql_field_seek ( MySQLResult result, int offset )
```

### Required arguments

- **result:** A valid MySQL result

- **offset:** A valid field offset

### Returns

The previous field cursor.

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

- mysql_field_seek

- [mysql_field_tell](mta://reference/misc/modules-mta-mysql-mysql-field-tell.md)

- [mysql_num_fields](mta://reference/misc/modules-mta-mysql-mysql-num-fields.md)

- [mysql_num_rows](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)

- [mysql_result](mta://reference/misc/modules-mta-mysql-mysql-result.md)

- [mysql_free_result](mta://reference/misc/modules-mta-mysql-mysql-free-result.md)

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)
