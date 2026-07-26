---
doc_id: "mta-wiki:6480"
title: "Database"
source_title: "Database"
source_url: "https://wiki.multitheftauto.com/wiki/Database"
revision_id: 79867
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:11:37.804912+00:00"
---

# Database

MTA uses a database system based on files. This system is sqlite, an embedded relational database management system.

## Files

There are two main database files for storing data:

- **internal.db:** this contains user account data (usernames, hashed passwords and account data stored by using the [setAccountData](mta://scripting/server/functions/setaccountdata.md) and [getAccountData](mta://scripting/server/functions/getaccountdata.md) functions).

- **registry.db:** this is the main database file, the scripting function [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md) work with this file.

## Functions

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)
