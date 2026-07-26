---
doc_id: "mta-wiki:3507"
title: "Resource : Maplimits"
source_title: "Maplimits"
source_url: "https://wiki.multitheftauto.com/wiki/Maplimits"
revision_id: 30739
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:08.002145+00:00"
---

# Resource : Maplimits

Map Limits is a resource that allows defining points in a .map file to border a map. A player outside the border area will lose health until he dies or returns to the game area.

## Usage

Syntax:

```
<maplimit>
	<point x="" y="" />
	<point x="" y="" />
	<point x="" y="" />
</maplimit>
```

When using maplimits in ones map, at least three points must be made.  

  

Note that the sequence of points **matters**. Start in the bottom left corner and work counter-clockwise.

For example, this would create a square shaped border:

```
<point x="0" y="0" />
<point x="1" y="0" />
<point x="1" y="1" />
<point x="0" y="1" />
```

While this would create two triangles:

```
<point x="0" y="0" />
<point x="1" y="1" />
<point x="0" y="1" />
<point x="1" y="0" />
```
