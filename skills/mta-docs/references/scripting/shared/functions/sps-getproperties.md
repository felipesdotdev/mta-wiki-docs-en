---
doc_id: "mta-wiki:11452"
title: "SPS:getProperties"
source_title: "SPS:getProperties"
source_url: "https://wiki.multitheftauto.com/wiki/SPS%3AgetProperties"
revision_id: 62955
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SPS:getProperties

This function is used to retrieve all property elements.

## Syntax

```
table getProperties()
```

### Returns

Returns all **property** elements.

## Example

Click to collapse [-]
Serverside example

This example script outputs all property IDs to the chat.

```
addEventHandler("onResourceStart",root,
	function()
		local properties = getProperties()
		for i,property in ipairs(properties) do
			outputChatBox("ID: "..getPropertyID(property))
		end
	end
)
```
