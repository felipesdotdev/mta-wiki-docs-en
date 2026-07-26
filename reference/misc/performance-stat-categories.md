---
doc_id: "mta-wiki:9866"
title: "Performance Stat Categories"
source_title: "Performance Stat Categories"
source_url: "https://wiki.multitheftauto.com/wiki/Performance_Stat_Categories"
revision_id: 78782
language: "en"
categories: []
generated_at: "2026-07-26T16:16:28.108715+00:00"
---

# Performance Stat Categories

Performance Stats Categories

### Performance Stats Categories

#### Lua memory

- **1: name** -- Name of the resource, except for "Lua VM totals" which is all combined.

- **2: change** - Change in memory usage in the last 5 seconds.

- **3: current** - Current memory usage of the listed thing.[Eg. a resource, or Lua VM]

- **4: max** - Max memory usage of the resource since it started.

- **5: XMLFiles** - How many XML files are open by the resource.

- **6: refs** - How many event created by the  resource.

- **7: Timers** - How many timers the resource is using.

- **8: Elements** - How many elements the resource has created which are still in existence.

- **9: TextItems** - same.

- **10: DxFonts** - same.

- **11: GuiFonts** - same.

- **12: Textures** - same.

- **13: Shaders** - same.

- **14: RenderTargets** - same.

- **15: ScreenSources** - same.

- **16: WebBrowsers** - same.

#### Lib memory

- **1: name** This category is only used by developers.

- **2: change**

- **3: current**

- **4: max**

#### Lua timing

- **1: name** - Name

- **2: 5s.cpu** - CPU usage in the last 5 seconds.

- **3: 5s.time** - CPU time spent in last 5 seconds on this resource.

- **4: 5s.calls** - Unknown[Maybe functions calls]

- **5: 5s.avg** - 5s avg CPU usae

- **6: 5s.max** - 5s max CPU usage

- **7: 60s.cpu** - same, but 60s.

- **8: 60s.time** - same, but 60s.

- **9: 60s.calls** - same, but 60s.

- **10: 60s.avg** - same, but 60s.

- **11: 60s.max** - same, but 60s.

- **12: 300s.cpu** - same, but 300s.

- **13: 300s.time** - same, but 300s.

- **14: 300s.calls** -same, but 300s.

- **15: 300s.avg** - same, but 300s.

- **16: 300s.max** - same, but 300s.

#### Packet usage

- **1: Packet type** - Packet type, could be incoming, or outgoing.

- **2: Incoming.msgs/sec** <- Read the name..

- **3: Incoming.bytes/sec** <- Read the name..

- **4: Incoming.logic cpu** - Amount of logic thread CPU usage that processing these packets requires.

- **5: Outgoing.msgs/sec** <- Read the name..

- **6: Outgoing.bytes/sec** <- Read the name..

- **7: Outgoing.msgs share** <- Read the name..
