---
doc_id: "mta-wiki:3947"
title: "GetResourceLoadTime"
source_title: "GetResourceLoadTime"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceLoadTime"
revision_id: 80420
language: "en"
categories: ["Server_functions", "Changes_in_1.0"]
generated_at: "2026-07-26T16:15:23.287490+00:00"
---

# GetResourceLoadTime

Gets the date and time at which a resource was last loaded in the server.

## Syntax

```
int getResourceLoadTime ( resource res )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getLoadTime(...)*

**Variable**: *.loadTime*

### Required Arguments

- **res:** the resource you want to know the load time of.

### Returns

If successful, returns the UNIX timestamp when the resource was loaded, otherwise false. Use in conjunction with [getRealTime](mta://scripting/shared/functions/getrealtime.md) in order to retrieve detailed information.

## Example

This code outputs the date and time at which the scoreboard resource was last loaded.

```
local res = getResourceFromName ( "scoreboard" )
if res then
    local time = getRealTime(getResourceLoadTime(res)) --Gets all the data we need from UNIX time format, see getRealTime() for more details
    outputConsole ( "scoreboard was last loaded on: " ..  string.format("%i/%i/%i %i:%i:%i",time.monthday,time.month,time.year,time.hour,time.minute,time.second)) --this will be something like this: scoreboard was last loaded on: 10/07/2017 14:13:10
end
```

This code outputs the date and time at which the specified resource started.

```
function getLoadTime(p,c,res)
	local resource = getResourceFromName(tostring(res))
	if not res or not resource then
		outputChatBox("Syntax: /" .. c .. " [Resource Name]")
	else
		local time = getRealTime(getRealTime().timestamp-getResourceLoadTime(resource))
		outputChatBox("The resource " .. res .. " started at " .. string.format("%i/%i/%i %i:%i:%i",time.monthday,time.month,time.year,time.hour,time.minute,time.second))
	end
end
addCommandHandler("getResourceLoadTime", getLoadTime, false,false) --adds the command handler
```

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- [callRemote](mta://scripting/server/functions/callremote.md)

- [copyResource](mta://scripting/server/functions/copyresource.md)

- [createResource](mta://scripting/server/functions/createresource.md)

- [deleteResource](mta://scripting/server/functions/deleteresource.md)

- [getResourceACLRequests](mta://scripting/server/functions/getresourceaclrequests.md)

- [getResourceInfo](mta://scripting/server/functions/getresourceinfo.md)

- [getResourceLastStartTime](mta://scripting/server/functions/getresourcelaststarttime.md)

- [getResourceLoadFailureReason](mta://scripting/server/functions/getresourceloadfailurereason.md)

- getResourceLoadTime

- [getResourceMapRootElement](mta://scripting/server/functions/getresourcemaprootelement.md)

- [getResourceOrganizationalPath](mta://scripting/server/functions/getresourceorganizationalpath.md)

- [getResources](mta://scripting/server/functions/getresources.md)

- [isResourceArchived](mta://scripting/server/functions/isresourcearchived.md)

- [isResourceProtected](mta://scripting/server/functions/isresourceprotected.md)

- [refreshResources](mta://scripting/server/functions/refreshresources.md)

- [removeResourceFile](mta://scripting/server/functions/removeresourcefile.md)

- [renameResource](mta://scripting/server/functions/renameresource.md)

- [restartResource](mta://scripting/server/functions/restartresource.md)

- [setResourceInfo](mta://scripting/server/functions/setresourceinfo.md)

- [startResource](mta://scripting/server/functions/startresource.md)

- [stopResource](mta://scripting/server/functions/stopresource.md)

- [updateResourceACLRequest](mta://scripting/server/functions/updateresourceaclrequest.md)
  

- **Shared**

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
