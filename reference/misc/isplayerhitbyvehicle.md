---
doc_id: "mta-wiki:12398"
title: "IsPlayerHitByVehicle"
source_title: "IsPlayerHitByVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerHitByVehicle"
revision_id: 66884
language: "en"
categories: []
generated_at: "2026-07-26T16:15:59.215895+00:00"
---

# IsPlayerHitByVehicle

**isPlayerHitByVehicle**

## Syntax

```
bool isPlayerHitByVehicle(attacker)
```

### Required Arguments

- **attacker** : The element that attacks .

## Function Source

Click to collapse [-]
Function source

```
function isPlayerHitByVehicle (attacker)
	if not attacker then
		return
	end
	if getElementType(attacker) == 'vehicle' then
		cancelEvent()
	end
end
```

## Author

Lisek
In Discord Lisek#5811
