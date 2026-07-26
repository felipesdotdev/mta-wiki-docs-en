---
doc_id: "mta-wiki:7755"
title: "Resource : Gang Manager/setGangPermissions"
source_title: "Resource:Gang Manager/setGangPermissions"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AGang_Manager/setGangPermissions"
revision_id: 40179
language: "en"
categories: ["Server_functions"]
---

# Resource : Gang Manager/setGangPermissions

Sets permission levels of the gang.

## Syntax

```
bool setGangPermissions ( string Gang, integer MinSettings, integer MinRules, integer MinDeposit, integer MinWithdraw, integer MinLevel, integer MinInvKick )
```

### Required Arguments

- **Gang:** ID of the gang you wish to set permissions of

- **MinSettings:** Minimal member level required to edit settings

- **MinRules:** Minimal member level required to edit rules

- **MinDeposit:** Minimal member level required to deposit money

- **MinWithdraw:** Minimal member level required to withdraw money

- **MinLevel:** Minimal member level required to change level of members with lower level

- **MinInvKick:** Minimal member level required to invite and kick members with lower level

### Returns

- **Success:** Boolean that is true if gang permissions were successfully set
