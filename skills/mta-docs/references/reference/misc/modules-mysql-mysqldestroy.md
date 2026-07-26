---
doc_id: "mta-wiki:1413"
title: "Modules/MySQL/MysqlDestroy"
source_title: "Modules/MySQL/MysqlDestroy"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/MySQL/MysqlDestroy"
revision_id: 21623
language: "en"
categories: []
---

# Modules/MySQL/MysqlDestroy

|  | This function is provided by the external module MySQL . You must install this module to use this function. |
| --- | --- |
|  |  |

This functions destroys a mysql object (gracefully), and cleans up any data it used.

## Syntax

```
nil mysqlClose ( mysql mysqlobj )
```

### Required Arguments

- **mysqlobj** : The [mysql](https://wiki.multitheftauto.com/index.php?title=Mysql&action=edit&redlink=1) object created by [mysqlCreate](mta://reference/misc/modules-mysql-mysqlcreate.md)

### Optional Arguments

*None*
