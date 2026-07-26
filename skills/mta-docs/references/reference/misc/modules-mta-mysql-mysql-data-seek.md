---
doc_id: "mta-wiki:3628"
title: "Modules/MTA-MySQL/mysql data seek"
source_title: "Modules/MTA-MySQL/mysql data seek"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MTA-MySQL/mysql_data_seek"
revision_id: 24964
language: "en"
categories: []
---

# Modules/MTA-MySQL/mysql data seek

|  | This function is provided by the external module MTA-MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

Sets the row cursor of a result in the given row offset. The offset must be a value between **1** and **[mysql_num_rows()](mta://reference/misc/modules-mta-mysql-mysql-num-rows.md)**.

## Syntax

```
mysql_data_seek ( MySQLResult result, int offset )
```

### Required arguments

- **result:** A valid MySQL result

- **offset:** A valid row offset

### Returns

This function doesn't return any value.

## See also

- mysql_data_seek

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

- [mysql_null](mta://reference/misc/modules-mta-mysql-mysql-null.md)
