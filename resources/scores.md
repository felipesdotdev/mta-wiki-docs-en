---
doc_id: "mta-wiki:3435"
title: "Resource : Scores"
source_title: "Resource:Scores"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AScores"
revision_id: 30871
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:59.878634+00:00"
---

# Resource : Scores

This resource provides kills, deaths, suicides, kill/death ratio and alive/dead status columns.

## Usage

Include "scores" in your resource (this also includes the scoreboard, so you don't need to do it).
From your script, select the columns that you want enabled through the settings system, and then force an update (this is necessary since we don't have settings registry events yet).

Example:

```
set("scores.kills", true) --enable kills column
set("scores.deaths", true) --enable deaths column
set("scores.self", false) --disable self-kills column
--...
call(getResourceFromName("scores"), "updateActiveColumns")
```

Keep in consideration that the columns do not have set defaults, so you should explicitly enable or disable all of them.

## Columns

**kills**

**deaths**

**self**

**ratio**

**status**

## Exported functions

### Server

```
bool updateActiveColumns ( )
```

Changes the active scoreboard columns according to the resource's current settings.
