---
doc_id: "mta-wiki:9470"
title: "IsResourceArchived"
source_title: "IsResourceArchived"
source_url: "https://wiki.multitheftauto.com/wiki/IsResourceArchived"
revision_id: 80424
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:16:00.130353+00:00"
---

# IsResourceArchived

Checks whether the specified resource is archived. (Currently running from a ZIP file)

## Syntax

```
bool isResourceArchived(resource resourceElement)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):isArchived(...)*

**Variable**: *.archived*

### Required Arguments

- **resourceElement:** The resource to check.

### Returns

Returns **true** if the selected resource is archived, **false** if it is not archived, and **nil** if some kind of problem occurred.

## Example

Click to collapse [-]
Example 1

This example stops the resource if it's archived.

```
addEventHandler("onResourceStart", resourceRoot,
	function(resourceElement)
		if isResourceArchived(resourceElement) then
			cancelEvent()
		end
	end
)
```

Click to collapse [-]
Example 2 (OOP)

This example stops the resource if it's archived by using the object oriented method. **(It's important to note that you need to enable OOP in meta.xml to use this)**

```
addEventHandler("onResourceStart", resourceRoot,
	function(resourceElement)
		if resourceElement:isArchived() then
			cancelEvent()
		end
	end
)
```

Click to collapse [-]
Example 3 (OOP)

This example stops the resource if it's archived by using the object oriented variable. **(It's important to note that you need to enable OOP in meta.xml to use this)**

```
addEventHandler("onResourceStart", resourceRoot,
	function(resourceElement)
		if resourceElement.archived then
			cancelEvent()
		end
	end
)
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

- isResourceArchived

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
