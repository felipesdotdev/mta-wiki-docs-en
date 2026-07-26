---
doc_id: "mta-wiki:11982"
title: "Physics raycast type"
source_title: "Physics raycast type"
source_url: "https://wiki.multitheftauto.com/wiki/Physics_raycast_type"
revision_id: 65138
language: "en"
categories: []
generated_at: "2026-07-26T16:16:29.004834+00:00"
---

# Physics raycast type

Physics raycast types

used in

- [physicsRayCast](mta://scripting/client/functions/physicsraycast.md)

## "isclear"

| Key | Value | Description |
| --- | --- | --- |
| hit | bool | do hit has occur |

## "default"

| Key | Value | Description |
| --- | --- | --- |
| hit | bool | do hit has occur |
| hitpoint | table | position of hit. |
| hitnormal | table | normal vector world center aligned. |
| shape | physics-shape | if something got hit, returns shape it hits. |
| rigidbody | rigid-body | contains rigid body if was hit, false otherwise |
| staticcollision | static-collision | contains static collision if was hit, false otherwise |

## "multiple"

Returns table with all hits where each hit is table from "default" type
