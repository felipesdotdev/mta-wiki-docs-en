---
doc_id: "mta-wiki:11765"
title: "GetRemoteRequestInfo"
source_title: "GetRemoteRequestInfo"
source_url: "https://wiki.multitheftauto.com/wiki/GetRemoteRequestInfo"
revision_id: 81222
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# GetRemoteRequestInfo

Gets informations of an [fetchRemote](mta://scripting/shared/functions/fetchremote.md) or [callRemote](mta://scripting/server/functions/callremote.md) request info.

## Syntax

```
table getRemoteRequestInfo ( request theRequest [, int postDataLength = 0 [, bool includeHeaders = false ] ] )
```

### Required Arguments

- **theRequest**: returned from [fetchRemote](mta://scripting/shared/functions/fetchremote.md), [callRemote](mta://scripting/server/functions/callremote.md) or [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

## Returns

Returns a table when valid, false otherwise
The table contains:

- **bytesReceived:** A number specifying the amount of data received so far. Zero means the download is queued

- **bytesTotal:** A number specifying the final download size. Will be zero if the remote HTTP server has not set the 'Content-Length' header

- **currentAttempt:** A number specifying the current connection attempt

- **type:** A string specifying either "fetch" or "call"

- **url:** A string specifying the URL

- **resource:** The resource which started the request, or false if the resource has since been stopped/restarted

- **queue:** A string specifying the queue name

- **method:** A string specifying the HTTP method. e.g. "GET" or "POST"

- **connectionAttempts:** A number specifying max number connection attempts as declared in the fetchRemote call

- **connectionTimeout:** A number specifying connection attempt timeout as declared in the fetchRemote call

- **postData:** A string containing the request post data as declared in the fetchRemote call

- **headers:** A table containing the request HTTP headers as declared in the fetchRemote call

## Example

Click to collapse [-]
Server

This example gets infos about all pending requests and prints them in debugscript

```
function CMD_requestInfo(player, _, resourceName)
    local res = resourceName and getResourceFromName(resourceName) or not resourceName and nil
	
    if(res == false) then
        outputServerLog("There is no resource named '" .. resourceName .. "'")
        return
    elseif(res and getResourceState(res) ~= "running") then
        outputServerLog("The provided resource '" .. resourceName .. "' is not running")
        return
    end
	
    local requests = getRemoteRequests(res)
	
    for _, request in ipairs(requests) do
        local requestInfo = getRemoteRequestInfo(request)
		
        if(requestInfo) then
            iprint(requestInfo)
        end
    end
end

addCommandHandler("requestinfo", CMD_requestInfo)
```

Click to collapse [-]
Client

This example gets infos about all pending requests and prints them in debugscript

```
function CMD_requestInfo(player, _, resourceName)
    local res = resourceName and getResourceFromName(resourceName) or not resourceName and nil
	
    if(res == false) then
        outputChatBox("There is no resource named '" .. resourceName .. "'")
        return
    elseif(res and getResourceState(res) ~= "running") then
        outputChatBox("The provided resource '" .. resourceName .. "' is not running")
        return
    end
	
    local requests = getRemoteRequests(res)
	
    for _, request in ipairs(requests) do
        local requestInfo = getRemoteRequestInfo(request)
		
        if(requestInfo) then
            iprint(requestInfo)
        end
    end
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

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- getRemoteRequestInfo
