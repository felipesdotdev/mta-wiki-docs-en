---
doc_id: "mta-wiki:7742"
title: "Resource : Gang Manager/setPlayerGang"
source_title: "Resource:Gang Manager/setPlayerGang"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/setPlayerGang"
revision_id: 40182
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# Resource : Gang Manager/setPlayerGang

Sets player's gang if the player is not currently in a gang.

## Syntax

Click to collapse [-]
Server

```
bool setPlayerGang ( player Player, string Gang )
```

## Required Arguments

- **Player:** Player element whose gang you want to set

- **Gang:** ID of the gang that you want to set as the player's gang

Click to collapse [-]
Client

```
bool setPlayerGang ( player Player, string Gang )
```

## Required Arguments

- **Player:** Player element whose gang you want to set

- **Gang:** ID of the gang that you want to set as the player's gang

## Returns

- **Success:** Boolean that is true if the player's gang has been set or false if the player already is in the gang
