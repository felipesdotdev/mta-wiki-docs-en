---
doc_id: "mta-wiki:7741"
title: "Resource : Gang Manager/outputGangChat"
source_title: "Resource:Gang Manager/outputGangChat"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/outputGangChat"
revision_id: 40174
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:01.495755+00:00"
---

# Resource : Gang Manager/outputGangChat

Sends message to gang member chat.

## Syntax

Click to collapse [-]
Server

```
bool outputGangChat ( string Gang, string AccountName, string PlayerName, string Message )
```

## Required Arguments

- **Gang:** ID of the gang you wish to output message to

- **AccountName:** Name of the account that is the source of the message (can be any string)

- **PlayerName:** Name of the player that is the source of the message (can be any string)

- **Message:** Message to output to gang chat

Click to collapse [-]
Client

```
bool outputGangChat ( string Gang, string AccountName, string PlayerName, string Message )
```

## Required Arguments

- **Gang:** ID of the gang you wish to output message to

- **AccountName:** Name of the account that is the source of the message (can be any string)

- **PlayerName:** Name of the player that is the source of the message (can be any string)

- **Message:** Message to output to gang chat

## Returns

- **Success:** Boolean that is true if message was successfully sent or false otherwise
