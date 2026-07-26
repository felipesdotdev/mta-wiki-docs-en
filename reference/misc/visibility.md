---
doc_id: "mta-wiki:1895"
title: "Visibility"
source_title: "Visibility"
source_url: "https://wiki.multitheftauto.com/wiki/Visibility"
revision_id: 74154
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:16:54.451146+00:00"
---

# Visibility

The visibility system for markers and blips works by the following rule: if something is visible to a certain element, it is also visible to all of that element's children. Also, everything is visible to the root element by default.

This means that if you want to make e.g. a blip only visible for a few specific players, you need to do two things:

- Make the blip invisible to the root element, using [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md). The blip is now hidden for all players.

- Make the blip visible again for the desired players.

The same things go for markers.

Tip: If you only want something to be visible to certain players the most efficient and least buggy thing to do is to when creating the element instead of the default visibility of root, set it to resourceRoot (no player will see it as no player is a child of resourceRoot) and then use [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md) on specific players. Otherwise there is a chance that players will see the blip for a fraction of a second, as the blip is created but then destroyed right after.

This is bad (chance of being seen on minimap for about 50ms):

```
a = createBlip(0, 0, 0, 41)
setElementVisibleTo(a, root, false)
setElementVisibleTo(a, somePlayer, true)
```

This is good:

```
a = createBlip(0, 0, 0, 41, 1, 2, 3, 4, 5, 6, 9999, resourceRoot)
setElementVisibleTo(a, somePlayer, true)
```
