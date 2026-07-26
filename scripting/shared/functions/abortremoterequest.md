---
doc_id: "mta-wiki:11766"
title: "AbortRemoteRequest"
source_title: "AbortRemoteRequest"
source_url: "https://wiki.multitheftauto.com/wiki/AbortRemoteRequest"
revision_id: 81223
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:10:19.246709+00:00"
---

# AbortRemoteRequest

Aborts a [fetchRemote](mta://scripting/shared/functions/fetchremote.md) or [callRemote](mta://scripting/server/functions/callremote.md) request.

## Syntax

```
bool abortRemoteRequest( request theRequest )
```

### Required Arguments

- **theRequest**: returned from [fetchRemote](mta://scripting/shared/functions/fetchremote.md), [callRemote](mta://scripting/server/functions/callremote.md) or [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

## Returns

Returns true on success, false when invalid request was provided

## Example

This example aborts all requests.

```
function CMD_abortRequests()
    local requests = getRemoteRequests()
	
    for _, request in ipairs(requests) do
        abortRemoteRequest(request)
    end
end

addCommandHandler("abortrequests", CMD_abortRequests)
```

## See Also

- abortRemoteRequest

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

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
