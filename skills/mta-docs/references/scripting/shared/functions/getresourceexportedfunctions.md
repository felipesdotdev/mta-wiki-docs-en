---
doc_id: "mta-wiki:3946"
title: "GetResourceExportedFunctions"
source_title: "GetResourceExportedFunctions"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceExportedFunctions"
revision_id: 71639
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetResourceExportedFunctions

Returns a table containing the names of the functions that a resource exports. It will return the exports of the current resource if there is no argument passed in.

## Syntax

```
table getResourceExportedFunctions ( [ resource theResource = getThisResource( ) ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getExportedFunctions(...)*

**Variable**: *.exportedFunctions*

### Optional Arguments

- **theResource:** the [resource](mta://reference/misc/resource.md) of which you want to know the [exported functions](mta://scripting/shared/functions/call.md).

### Returns

Returns a [table](mta://reference/misc/table.md) of function names if successful, *false* otherwise.

## Example

This simple example will output the names of the functions that the "scoreboard" resource exports.

```
local res = getResourceFromName ( "scoreboard" )
if res then
    local functionNames = getResourceExportedFunctions ( res )
    outputConsole ( "The scoreboard resource exports " .. #functionNames .. " functions:" )
    for i, name in ipairs ( functionNames ) do
        outputConsole ( name )
    end
else
    outputConsole ( "Unable to find the scoreboard resource." )
end
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- getResourceExportedFunctions

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
