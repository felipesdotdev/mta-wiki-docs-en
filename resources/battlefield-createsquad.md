---
doc_id: "mta-wiki:5152"
title: "Resource : Battlefield/createSquad"
source_title: "Resource:Battlefield/createSquad"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABattlefield/createSquad"
revision_id: 22989
language: "en"
categories: []
generated_at: "2026-07-26T16:17:10.129070+00:00"
---

# Resource : Battlefield/createSquad

Purpose

Creates a squad element. [Click here to read more about squads.](mta://resources/battlefield-squad--8a0693ff.md)

## Syntax

```
squad createSquad ( team squadTeam, string shortName )
```

### Required Arguments

- **squadTeam:** The [team](mta://reference/misc/team.md) element the squad will be attached to.

- **shortName:** The [shortname](https://wiki.multitheftauto.com/index.php?title=Resource:Battlefield/shortname&action=edit&redlink=1) for the squad.

### Returns

Returns the *squad element* if it was created, otherwise *false*.

## Function Source

```
function createSquad ( team, shortn )
	squad = createElement ( "squad", team, shortn )
	if squad then
		return squad
	else
		return false
	end
end
```

| Return to Battlefield Resource |
| --- |
