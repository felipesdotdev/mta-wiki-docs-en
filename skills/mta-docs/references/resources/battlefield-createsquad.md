---
doc_id: "mta-wiki:5152"
title: "Resource : Battlefield/createSquad"
source_title: "Resource:Battlefield/createSquad"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABattlefield/createSquad"
revision_id: 22989
language: "en"
categories: []
---

# Resource : Battlefield/createSquad

Purpose

Creates a squad element. [Click here to read more about squads.](https://wiki.multitheftauto.com/index.php?search=Click%20here%20to%20read%20more%20about%20squads.)

## Syntax

```
squad createSquad ( team squadTeam, string shortName )
```

### Required Arguments

- **squadTeam:** The [team](https://wiki.multitheftauto.com/index.php?search=team) element the squad will be attached to.

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
