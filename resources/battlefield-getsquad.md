---
doc_id: "mta-wiki:5161"
title: "Resource : Battlefield/getSquad"
source_title: "Resource:Battlefield/getSquad"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABattlefield/getSquad"
revision_id: 31095
language: "en"
categories: []
generated_at: "2026-07-26T16:17:10.140564+00:00"
---

# Resource : Battlefield/getSquad

Purpose

This command retrieves a [squad](mta://resources/battlefield-squad--8a0693ff.md) element when given the name or [shortname](https://wiki.multitheftauto.com/index.php?title=Resource:Battlefield/shortname&action=edit&redlink=1) of a squad and the team.

## Syntax

```
squad getSquad ( [string squadName, string squadShortn], team squadTeam )
```

### Required Arguments

- **squadTeam:** The [team](mta://reference/misc/team.md) element the squad will be attached to.

### Optional Arguments

- **squadName:** The name of the squad.

- **squadShortn:** The shortname of the squad.

### Returns

Returns the *squad element* if it was found, otherwise *false*.

## Function Source

```
nameTable = { "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel" }
function getSquad ( name, team )
	local squads = getElementsByType ( "squad" )
	for k,v in ipairs ( squads ) do
		local sTeam = getElementData ( v, "team" )
		if team == sTeam then
			for j,l in ipairs ( nameTable ) do
				shortn = string.lower ( string.sub ( l, 1, 1 ) )
				if name == l or name == shortn then
					return v
				else
					return false
				end
			end
		else
			return false
		end
	end
end
```

| Return to Battlefield Resource |
| --- |
