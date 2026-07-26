---
doc_id: "mta-wiki:4324"
title: "Resource : Blipstreamer/getBlipStreamRadius"
source_title: "Resource:Spawnmanager/getBlipStreamRadius"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/getBlipStreamRadius"
revision_id: 18270
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:00.034254+00:00"
---

# Resource : Blipstreamer/getBlipStreamRadius

This function retrieves the current stream radius of a blip, or whether its streamable at all

## Syntax

```
bool getBlipStreamRadius ( element blip )
```

### Required Arguments

- **blip**: The blip in which you wish to retrieve the stream status for

### Returns

Returns a float representing the current radius for streaming, or *false* if streaming was not enabled.

## Example

This example outputs your own blip's stream radius

```
function outputMyStreamRadius(player)

	--Destroy any old attached blips
	for k,element in ipairs(getAttachedElements(source)) do
		if getElementType(element) == "blip" then
			local streamRadius = call(getResourceFromName"blipstreamer","getBlipStreamRadius",blip)
			if streamRadius then
				outputChatBox ( "Stream radius is: "..streamRadius )
			else
				outputChatBox ( "No stream radius!" )
			end
		end
	end
	--Create a new blip and make it streamable
	local blip = createBlipAttachedTo ( source, 0, 1 )
	)
end
addCommandHandler ( "mystreamradius", outputMyStreamRadius )
```
