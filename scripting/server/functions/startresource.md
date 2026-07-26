---
doc_id: "mta-wiki:2615"
title: "StartResource"
source_title: "StartResource"
source_url: "https://wiki.multitheftauto.com/wiki/StartResource"
revision_id: 80431
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:52.486957+00:00"
---

# StartResource

This function starts a resource either persistently or as a dependency of the current resource. If you start the resource persistently, the resource will run until stopped either using [stopResource](mta://scripting/server/functions/stopresource.md) or by the server admin. A resource started as a dependency will stop when your resource stops, if no other resources have it as a depdendency. This is the same effect as using an *include* in your [meta.xml](mta://reference/misc/meta-xml.md) file.

The function also allows you to specify a number of boolean options. These allow you to disable the loading of various aspects of the resource. This is generally useful for editors rather than for actual gamemodes. It could also be used as a way to preview a resource before enabling the scripting aspects, though this could produce unreliable results. There is no way for a resource to tell if it is being run with any of these booleans set.

## Syntax

```
bool startResource ( resource resourceToStart, [bool persistent = false, bool startIncludedResources = true, bool loadServerConfigs = true, bool loadMaps = true, bool loadServerScripts = true, bool loadHTML = true, bool loadClientConfigs = true, bool loadClientScripts = true, bool loadFiles = true] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):start(...)*

### Required Arguments

- **resourceToStart:** The resource that should be started.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **persistent:** A boolean specifying if the resource should continue to run even after the current resource has been stopped or not. If this is *true* then the resource will run until another resource or user terminates it or the server shuts down. If this is *false* then *resourceToStart* will stop when *thisResource* stops.

- **startIncludedResources:** A boolean specifying if the resource's included/dependant resources will be started.

- **loadServerConfigs:** A boolean specifying if server side config (XML) files should be loaded with the resource.

- **loadMaps:** A boolean specifying if any .map files will be started with the resource.

- **loadServerScripts:** A boolean specifying if server side script files should be started alongside the resource.

- **loadHTML:** A boolean specifying if HTML files should be started alongside the resource.

- **loadClientConfigs:** A boolean specifying if client configs should be loaded alongside the resource.

- **loadClientScripts:** A boolean specifying if client scripts should be loaded and started alongside the resource.

- **loadFiles:** A boolean specifying if client-side files should be loaded alongside the resource.

### Returns

Returns *true* if the resource has been started successfully, *false* otherwise.

## Example

This example starts a specified resource with the command; "/resource-start".

```
function startTheResource ( thePlayer, command, resourceName )
	if ( resourceName ) then -- Check if they specified a resource name
		local resource = getResourceFromName ( resourceName ) -- Get the resource
		
		local start = startResource ( resource ) -- Start the resource
		if ( start ) then -- If it was successfully started...
			outputChatBox ( resourceName .. " was started successfully.", thePlayer, 255, 0, 0 )
		else -- If it wasn't successfully started...
			outputChatBox ( "This resource doesn't exist.", thePlayer, 255, 0, 0 )
		end
	else -- If they didn't put a resource name...
		outputChatBox ( "Please specify a resource to start.", thePlayer, 255, 0, 0 )
	end
end
addCommandHandler ( "resource-start", startTheResource ) -- Make it trigger when somebody types "/resource-start"
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

- [restartResource](mta://scripting/server/functions/restartresource.md)

- [setResourceInfo](mta://scripting/server/functions/setresourceinfo.md)

- startResource

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
