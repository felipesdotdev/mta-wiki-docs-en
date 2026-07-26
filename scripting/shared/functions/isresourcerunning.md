---
doc_id: "mta-wiki:14667"
title: "IsResourceRunning"
source_title: "IsResourceRunning"
source_url: "https://wiki.multitheftauto.com/wiki/IsResourceRunning"
revision_id: 82788
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:00.166150+00:00"
---

# IsResourceRunning

Syntax

- **isResourceRunning** You can insert this code example in your resources.

### Required Arguments

- **isResourceRunning:** The value to check resources

## Example check isResourceRunning(resName)

Click to collapse [-]
isResourceRunning

You can insert this code example in your resources.

```
function isResourceRunning(resName)
   local res = getResourceFromName(resName)
   return (res) and (getResourceState(res) == "running")
end

-- Example of inserting into system code:
--[[
if isResourceRunning("admin") then
   --code
else
   --alert
end

addCommandHandler('pos', function (commandName)
    if isResourceRunning("admin") then
       local x,y,z = getElementPosition(localPlayer)
       outputChatBox( x ..', '.. y ..', '.. z, 255, 255, 255 )
    else
       outputChatBox("The resource is not running 'admin'.", 255, 0, 0)
    end
end )
]]
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

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
