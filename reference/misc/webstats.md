---
doc_id: "mta-wiki:3513"
title: "Resource : Webstats"
source_title: "Webstats"
source_url: "https://wiki.multitheftauto.com/wiki/Webstats"
revision_id: 30905
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:55.199658+00:00"
---

# Resource : Webstats

Webstats provides Interesting and Exciting™ statistics about your game server!

## How to use

Webstats is accessible via HTTP only. Just start webstats and visit *http://yourserver:port/* and click Statistics in the resource browser's side bar.

## Scripters

Scripts can register your own stats with the resource, just do something like the following:

```
call(getResourceFromName("webstats"), "registerStat", getThisResource(), "getBlipCount", "Blips", "The number of blips")
function getBlipCount()
	return #getElementsByType("blip");
end
```

The syntax for calling *registerStat* is:

```
call(getResourceFromName("webstats"), "registerStat", getThisResource(), "yourFunctionName", "Stat name", "Stat description")
```

The function specified will be called every time the stats are updated (by default once a minute). You should return an number value.

Another example. This example counts the amount of damage done between each call to getDamageCount.

```
call(getResourceFromName("webstats"), "registerStat", getThisResource(), "getDamageCount", "Damage Given", "The amount of damage players have taken")
damagecount = 0
addEventHandler ( "onPlayerDamage",  getRootElement(), 
	function( attacker, attackerweapon, bodypart, loss )
		damagecount = damagecount + loss
	end
)

function getDamageCount()
	local ret = damagecount;
	damagecount = 0;
	return ret;
end
```
