---
doc_id: "mta-wiki:4595"
title: "GetLoadedModules"
source_title: "GetLoadedModules"
source_url: "https://wiki.multitheftauto.com/wiki/GetLoadedModules"
revision_id: 42001
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:15.115145+00:00"
---

# GetLoadedModules

This function returns all the currently loaded [modules](mta://reference/misc/modules.md) of the server.

## Syntax

```
table getLoadedModules ()
```

### Returns

Returns a table of all the currently loaded [modules](mta://reference/misc/modules.md). If no modules are loaded, the table will be empty.

## Example

Adds a command that lists all loaded modules in the server log.

```
function checkModules()
	local modules = getLoadedModules()
	
	if #modules == 0 then
		return outputServerLog("No modules are loaded!")
	end
	
	for k,v in ipairs(modules) do
	        outputServerLog( v )
	end
		
	outputServerLog("Loaded " .. #modules .. " modules in total.")
end
addCommandHandler("modules", checkModules)
```

## See Also

- getLoadedModules

- [getModuleInfo](mta://scripting/server/functions/getmoduleinfo.md)
