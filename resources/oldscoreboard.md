---
doc_id: "mta-wiki:6425"
title: "Resource : OldScoreboard"
source_title: "Resource:OldScoreboard"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AOldScoreboard"
revision_id: 79073
language: "en"
categories: ["Resource", "Historical"]
generated_at: "2026-07-26T16:17:13.411325+00:00"
---

# Resource : OldScoreboard

|  | Historical: This page is retained for historical reference. |
| --- | --- |
| This is the old scoreboard from MTA:SA Deathmatch DP1 to DP3. The new one is here . |  |

The scoreboard displays connected players, teams, pings and other data in a gridlist for players ingame. It also has a javascript-enabled web interface, so it can be viewed from a browser.

When you add a column to the scoreboard, it's linked to the element data field of the same name, so if you add the "score" column, element data in the field "score" will be shown for all players and teams.

## Exported serverside functions

You can call them from another resource using call():

```
call(getResourceFromName("scoreboard"), "addScoreboardColumn", "wanted level")
```

```
bool addScoreboardColumn( string columnName, [ element visibleToElement = getRootElement(), int columnPosition = #columns - 1, float columnSize = 0.1 ] )
bool removeScoreboardColumn( string columnName )
bool setPlayerScoreboardForced( player thePlayer, bool forced )
table getScoreboardColumns( ) --returns an ordered array of {name=columnName,size=columnSize} entries
bool resetScoreboardColumns( ) --leaves only "name, ping"
```

You can set the scoreboard data with setElementData:

```
setElementData ( thePlayer, "wanted level", 3 ) --3 is inserted in the player's wanted level column
```

## Issues/TODO

- Columns name must be unique, you can't add a column with the same name to different elements yet

- Scoreboard data for web listing is being sent all at once, should allow sending of separate chunks
