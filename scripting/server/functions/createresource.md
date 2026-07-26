---
doc_id: "mta-wiki:3332"
title: "CreateResource"
source_title: "CreateResource"
source_url: "https://wiki.multitheftauto.com/wiki/CreateResource"
revision_id: 80414
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:10:38.426332+00:00"
---

# CreateResource

This function creates an new, empty resource. This creates a directory matching the name you specify on disk, then creates an empty meta.xml file with a <meta> element in it.

## Syntax

```
resource createResource ( string resourceName [, string organizationalDir ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Resource](mta://reference/misc/resource.md)(...)*

### Required Arguments

- **resourceName:** The name of the new resource. This should be a valid file name. It's recommended that you do not have spaces or non-ASCII characters in resource names.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **organizationalDir**: A string containing the path where the resource should be created (e.g. "[gamemodes]/[amx]").

### Returns

Returns the [resource](mta://reference/misc/resource.md) element of the new resource if successful, *false* otherwise. This could fail if the resource name already is in use, if a directory already exists with the name you've specified (but this isn't a valid resource) or if the name you specify isn't valid. It could also fail if the disk was full or for other similar reasons.

## Example

This example creates a new resource named what the player specified. The command is "/new-resource <name>".

```
function createNewResource ( source, command, resourceName ) -- Define the source and add a resourceName argument.
	if ( resourceName ) then -- Check if they entered a resource name, and if they did...
		local resourceName = tostring ( resourceName ) -- Convert the name into a string.
		local newResource = createResource ( resourceName ) -- Create the new resource.
			if ( newResource ) then -- Check if the resource has been created, if so then...
				outputChatBox ( "New resource created succcessfully.", source, 255, 0, 0 ) -- Output it's done.
			else -- If the resource wasn't made successfully then...
				outputChatBox ( "An un-expected error occured.", source, 255, 0, 0 ) -- Output it failed.
			end
	else -- If they didn't enter a resource name...
		outputChatBox ( "Please specify a name for your new resource.", source, 255, 0, 0 ) -- Tell them to specify a name.
	end
end
addCommandHandler ( "new-resource", createNewResource ) -- Make it trigger when somebody types "/new-resource <name>".
```

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- [callRemote](mta://scripting/server/functions/callremote.md)

- [copyResource](mta://scripting/server/functions/copyresource.md)

- createResource

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
