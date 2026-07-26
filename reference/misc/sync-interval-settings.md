---
doc_id: "mta-wiki:6357"
title: "Sync interval settings"
source_title: "Sync interval settings"
source_url: "https://wiki.multitheftauto.com/wiki/Sync_interval_settings"
revision_id: 79093
language: "en"
categories: []
generated_at: "2026-07-26T16:16:54.724255+00:00"
---

# Sync interval settings

About player sync

Player key sync is always done on demand. i.e. Player presses W, (or pushes forward on the joystick), and the sync for that is sent straight away to the server, and then to the other clients.
There is no setting to limit key sync as it is an essential component to minimize latency.
The 'player_sync_interval' below, is the interval between positional and rotational corrections to key sync. This is in case the movement interpreted by the key sync system on remote clients has introduced any errors.

## Default values

| Name | Default (ms) | Valid range | Description |
| --- | --- | --- | --- |
| player_sync_interval | 100 | 50-4000 | Time between key sync correction updates for players. (Note: Player key sync is always done on demand and is not affected by any setting) (Note2: Don't set player_sync_interval interval too high, it will cause fake network troubles) |
| lightweight_sync_interval | 1500 | 50-4000 | Time between updates for very far away players |
| camera_sync_interval | 500 | 50-4000 | How often to tell the server of any client side changes to the local players camera position and target. |
| ped_sync_interval | 400 | 50-4000 | Time between updates for non-player peds |
| ped_far_sync_interval | 2000 | 50-4000 | Time between updates for non-player peds for clients which are far away from the ped. |
| unoccupied_vehicle_sync_interval | 1000 | 50-4000 | Time between updates for unoccupied vehicles |
| keysync_mouse_sync_interval | 100 | 50-4000 | Minimum gap between mouse movement updates being sent to the server |
| keysync_analog_sync_interval | 100 | 50-4000 | Minimum gap between joystick partial axes movement updates being sent to the server. (Full axes movement is treated as key sync and is not limited by this setting) |

## Suggested settings

### Bandwith and CPU saver

| player_sync_interval | 200 |
| --- | --- |
| lightweight_sync_interval | 3000 |

### Bandwith and CPU super saver

| player_sync_interval | 300 |
| --- | --- |
| lightweight_sync_interval | 4000 |

### Less annoying unoccupied vehicles

| unoccupied_vehicle_sync_interval | 500 |
| --- | --- |

### Uber sync (bandwidth and CPU intensive)

| player_sync_interval | 50 |
| --- | --- |
| keysync_mouse_sync_interval | 50 |
| keysync_analog_sync_interval | 50 |
