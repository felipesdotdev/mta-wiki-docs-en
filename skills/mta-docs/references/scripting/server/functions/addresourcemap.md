---
doc_id: "mta-wiki:3312"
title: "AddResourceMap"
source_title: "AddResourceMap"
source_url: "https://wiki.multitheftauto.com/wiki/AddResourceMap"
revision_id: 80411
language: "en"
categories: ["Server_functions", "Utility_templates"]
---

# AddResourceMap

This function adds a new empty mapfile to an existing resource.

| [[{{{image}}}\|link=\|]] | Note: You can't add a map to a running resource. |
| --- | --- |
|  |  |

## Syntax

```
xmlnode addResourceMap ( string filePath, [ int dimension = 0 ] )
```

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the resource map in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the map file will be in, and 'path' is the path from the root directory of the resource to the file.

For example, if you want to create a map file named 'manycars.map' in the resource 'cdm', it can be created from another resource this way: *addResourceMap(":cdm/manycars.map")*.

If you want to create the map file in the current resource, only the file path is necessary, e.g. *addResourceMap("manycars.map")*.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **dimension:** the [dimension](mta://reference/misc/dimension.md) in which the map's objects will be placed.

### Returns

Returns the new map's root [xmlnode](mta://reference/misc/xmlnode.md) if the map was added successfully, *false* otherwise.

## Example

This example just adds a map to a gamemode resource called "cdm".

```
addResourceMap(":cdm/[maps]/New.map",0)
```

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- addResourceMap

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
