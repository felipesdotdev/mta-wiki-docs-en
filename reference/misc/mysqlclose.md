---
doc_id: "mta-wiki:2325"
title: "Modules/MySQL/MysqlDestroy"
source_title: "MysqlClose"
source_url: "https://wiki.multitheftauto.com/wiki/MysqlClose"
revision_id: 21623
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.928533+00:00"
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
