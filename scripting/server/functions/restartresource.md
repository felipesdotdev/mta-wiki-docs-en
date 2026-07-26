---
doc_id: "mta-wiki:2613"
title: "RestartResource"
source_title: "RestartResource"
source_url: "https://wiki.multitheftauto.com/wiki/RestartResource"
revision_id: 80429
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:34.736749+00:00"
---

# RestartResource

This function restarts a running resource. Restarting will destroy all the elements that the resource has created (as stopping the resource does).

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using restartResource function or it won't work. This function does not restart the resource immediately. Restarts are queued up until the end of the server's frame to ensure that they occur in the correct order (and that dependent resources can start and stop correctly). The resource being restarted will have an onResourceStop event triggered and the restarted instance will receive an onResourceStart event. Remember that the element and resource variables will be invalidated during the restart, though of course, the resource's name will not. |
| --- | --- |
|  |  |

## Syntax

```
bool restartResource ( resource theResource [, bool persistent = false, bool configs = true, bool maps = true, bool scripts = true, bool html = true, bool clientConfigs = true, bool clientScripts = true, bool clientFiles = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):restart(...)*

### Required Arguments

- **theResource:** the [resource](mta://reference/misc/resource.md) you want to restart.

### Optional Arguments

- **persistent:** Unused

- **configs:** Reload configs?

- **maps:** Reload maps?

- **scripts:** Reload (server) scripts?

- **html:** Reload html files (for resource web access)?

- **clientConfigs:** Reload client configs?

- **clientScripts:** Reload client scripts?

- **clientFiles:** Reload files?

### Returns

Returns *true* if the resource was restarted, *false* if the resource wasn't running, or an invalid resource was passed.

## Example

Example 1: This function restarts all running resources.

```
function restartAllResources()
	-- we store a table of resources
	local allResources = getResources()
	-- for each one of them,
	for index, res in ipairs(allResources) do
		-- if it's running,
		if getResourceState(res) == "running" then
			-- then restart it
			restartResource(res)
		end
	end
end
```

Example 2: This example will restart the specify resource every 3600000 milliseconds (hour).

```
setTimer(
    function()  
	--restarting this resource every hour
        restartResource(getThisResource())
    end,
3600000, 0)
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

- [getResourceLoadTime](mta://scripting/server/functions/getresourceloadtime.md)

- [getResourceMapRootElement](mta://scripting/server/functions/getresourcemaprootelement.md)

- [getResourceOrganizationalPath](mta://scripting/server/functions/getresourceorganizationalpath.md)

- [getResources](mta://scripting/server/functions/getresources.md)

- [isResourceArchived](mta://scripting/server/functions/isresourcearchived.md)

- [isResourceProtected](mta://scripting/server/functions/isresourceprotected.md)

- [refreshResources](mta://scripting/server/functions/refreshresources.md)

- [removeResourceFile](mta://scripting/server/functions/removeresourcefile.md)

- [renameResource](mta://scripting/server/functions/renameresource.md)

- restartResource

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
