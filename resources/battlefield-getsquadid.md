---
doc_id: "mta-wiki:5169"
title: "Resource : Battlefield/getSquadShortn"
source_title: "Resource:Battlefield/getSquadID"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABattlefield/getSquadID"
revision_id: 31075
language: "en"
categories: []
generated_at: "2026-07-26T16:16:58.576397+00:00"
---

# Resource : Battlefield/getSquadShortn

This function retrieves the squad ID. The squad ID is simply a string representing the full squad name. The first letter of a squad name is the ID. It can be retrieved with the squad element.  
  

Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel

## Syntax

```
string getSquadID ( team squadTeam, squad squadElement )
```

# Required Arguments

- **squadTeam**: The team element the squad is attached to. if this is nil or false then it checks the second argument (squadElement).

- **squadElement**: The squad you want the ID/shortn from.

[Resource:battlefield](mta://resources/battlefield.md)
