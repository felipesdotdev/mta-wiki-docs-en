---
doc_id: "mta-wiki:7740"
title: "Resource : Gang Manager/leaveGang"
source_title: "Resource:Gang Manager/leaveGang"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/leaveGang"
revision_id: 40173
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:01.480217+00:00"
---

# Resource : Gang Manager/leaveGang

Removes player from his current gang.

## Syntax

Click to collapse [-]
Server

```
bool leaveGang ( player Player )
```

## Required Arguments

- **Player:** Player who you want to leave his current gang that he is in

Click to collapse [-]
Client

```
bool leaveGang ( player Player )
```

## Required Arguments

- **Player:** Player who you want to leave his current gang that he is in

## Returns

- **Success:** Boolean that is true if player left his gang or false if player is the current leader of his gang
