---
doc_id: "mta-wiki:4596"
title: "GetModuleInfo"
source_title: "GetModuleInfo"
source_url: "https://wiki.multitheftauto.com/wiki/GetModuleInfo"
revision_id: 42021
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:15.628225+00:00"
---

# GetModuleInfo

This function returns information about the specified [module](mta://reference/misc/modules.md).

## Syntax

```
table getModuleInfo ( string moduleName )
```

### Required Arguments

- **moduleName:** A string containing the module you wish to get information of e.g. "hashing.dll"

### Returns

Returns a [table](mta://reference/misc/table.md) containing information about module. These keys are present in the table:

- **version**: Module version in format X.XX

- **name**: Module name

- **author**: Module author

If invalid name for module is passed, it will return *false*.

## Example

This example adds a command *checkmodules* with which you can view information about currently loaded modules.

```
function printModuleInfo ( thePlayer )
    local modules = getLoadedModules()
    if #modules == 0 then
        return outputConsole ( "There are no modules loaded!", thePlayer ) -- Return as no module is loaded, the for has nothing todo
    end

    for k, v in ipairs ( modules ) do
        local moduleInfo = getModuleInfo ( v )
        outputConsole ( moduleInfo.name .. "(" .. v .. ") v" .. moduleInfo.version .. ", author: " .. moduleInfo.author, thePlayer )
    end
end
addCommandHandler ( "checkmodules", printModuleInfo )
```

## See Also

- [getLoadedModules](mta://scripting/server/functions/getloadedmodules.md)

- getModuleInfo
