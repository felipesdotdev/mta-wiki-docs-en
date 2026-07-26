---
doc_id: "mta-wiki:7743"
title: "Resource : Gang Manager/setPlayerLevel"
source_title: "Resource:Gang Manager/setPlayerLevel"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/setPlayerLevel"
revision_id: 40183
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:01.583790+00:00"
---

# Resource : Gang Manager/setPlayerLevel

Sets player's level if the player is currently in a gang.

## Syntax

Click to collapse [-]
Server

```
bool setPlayerLevel ( player Player, integer Level )
```

## Required Arguments

- **Player:** Player whose level you want to change

- **Level:** Integer of the level you want to set as player's level from 1 to 5

Click to collapse [-]
Client

```
bool setPlayerLevel ( player Player, integer Level )
```

## Required Arguments

- **Player:** Player whose level you want to change

- **Level:** Integer of the level you want to set as player's level from 1 to 5

## Returns

- **Success:** Boolean that is true if the level was changed successfully or false otherwise
