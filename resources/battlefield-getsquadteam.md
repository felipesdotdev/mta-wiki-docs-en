---
doc_id: "mta-wiki:5164"
title: "Resource : Battlefield/getSquadTeam"
source_title: "Resource:Battlefield/getSquadTeam"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABattlefield/getSquadTeam"
revision_id: 31076
language: "en"
categories: []
generated_at: "2026-07-26T16:16:58.596299+00:00"
---

# Resource : Battlefield/getSquadTeam

This function retrieves a squad element's team.

## Syntax

```
team getSquadTeam ( squad squadElement )
```

# Required Argument

- **squadElement**: The squad you want to retrieve the team from.

# Source Code

```
function getSquadTeam(squadElement)
	if(squadElement)then
		team = getElementData(squadElement,"team")
		return team
	else
		return false
	end
end
```

[Resource:Battlefield](mta://resources/battlefield.md)
