---
doc_id: "mta-wiki:11764"
title: "GetRemoteRequests"
source_title: "GetRemoteRequests"
source_url: "https://wiki.multitheftauto.com/wiki/GetRemoteRequests"
revision_id: 81221
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# GetRemoteRequests

Gets all [fetchRemote](mta://scripting/shared/functions/fetchremote.md) and [callRemote](mta://scripting/server/functions/callremote.md) requests currently running.

## Syntax

```
table getRemoteRequests ( [ resource theResource = nil ] )
```

### Optional Arguments

- **theResource**: the resource to get all requests from

## Returns

Returns a table with all requests, false if an invalid resource was provided

## Example

Click to collapse [-]
Server

This example prints how many request are currently pending.

```
function CMD_requestInfo(player, _, resourceName)
    local res = resourceName and getResourceFromName(resourceName) or not resourceName and nil
	
    if(res == false) then
        outputChatBox("There is no resource named '" .. resourceName .. "'", player)
        return
    elseif(res and getResourceState(res) ~= "running") then
        outputChatBox("The provided resource '" .. resourceName .. "' is not running", player)
        return
    end

    local requests = getRemoteRequests(res)
	
    outputChatBox(("There are %d request%s running"):format(#requests, #requests == 1 and '' or 's'), player)
end

addCommandHandler("requestinfo", CMD_requestInfo)
```

Click to collapse [-]
Client

This example prints how many request are currently pending.

```
function CMD_requestInfo(_, resourceName)
    local res = resourceName and getResourceFromName(resourceName) or not resourceName and nil
	
    if(res == false) then
        outputChatBox("There is no resource named '" .. resourceName .. "'")
        return
    elseif(res and getResourceState(res) ~= "running") then
        outputChatBox("The provided resource '" .. resourceName .. "' is not running")
        return
    end

    local requests = getRemoteRequests(res)
	
    outputChatBox(("There are %d request%s running"):format(#requests, #requests == 1 and '' or 's'))
end

addCommandHandler("requestinfo", CMD_requestInfo)
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- getRemoteRequests

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
