---
doc_id: "mta-wiki:7736"
title: "Resource : Gang Manager/deleteGang"
source_title: "Resource:Gang Manager/deleteGang"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/deleteGang"
revision_id: 40159
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:12.477104+00:00"
---

# Resource : Gang Manager/deleteGang

Deletes gang from the database.

## Syntax

Click to collapse [-]
Server

```
bool deleteGang ( string Gang )
```

## Required Arguments

- **Gang:** ID of the gang you wish to delete

Click to collapse [-]
Client

```
bool deleteGang ( string Gang )
```

## Required Arguments

- **Gang:** ID of the gang you wish to delete

## Returns

- **Success:** Boolean that is true if the gang was deleted or false otherwise
