---
doc_id: "mta-wiki:7748"
title: "Resource : Gang Manager/getGangPermissions"
source_title: "Resource:Gang Manager/getGangPermissions"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/getGangPermissions"
revision_id: 40167
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:12.512890+00:00"
---

# Resource : Gang Manager/getGangPermissions

Gets current permissions of the gang.

## Syntax

```
int int int int int int getGangPermissions ( string Gang )
```

### Required Arguments

- **Gang:** ID of the gang you wish to get permissions of

### Returns

- **MinSettings:** Minimal member level required to edit settings

- **MinRules:** Minimal member level required to edit rules

- **MinDeposit:** Minimal member level required to deposit money

- **MinWithdraw:** Minimal member level required to withdraw money

- **MinLevel:** Minimal member level required to change level of members with lower level

- **MinInvKick:** Minimal member level required to invite and kick members with lower level
