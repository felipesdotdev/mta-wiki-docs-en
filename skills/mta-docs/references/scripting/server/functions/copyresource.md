---
doc_id: "mta-wiki:4650"
title: "CopyResource"
source_title: "CopyResource"
source_url: "https://wiki.multitheftauto.com/wiki/CopyResource"
revision_id: 81020
language: "en"
categories: ["Server_functions", "Utility_templates"]
---

# CopyResource

This function copies a specified [resource](mta://reference/misc/resource.md) with a new name.

## Syntax

```
resource copyResource ( resource theResource, string newResourceName [, string organizationalDir ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):copy(...)*

### Required Arguments

- **theResource:** the resource which is going to be copied

- **newResourceName:** the name that the copied resource will receive

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **organizationalDir**: A string containing the path where the resource should be copied to (e.g. "[gamemodes]/[amx]").

### Returns

Returns the [resource](mta://reference/misc/resource.md) element of the copy. Returns *false* if the arguments are incorrect.

## Example

```
-- This script can backup your resource with a easy command! /backupresource [resourcename]
function backupResource (player,command,resourcetobackup) -- start the function
  if (resourcetobackup) and (getResourceFromName(resourcetobackup)) then -- check if the resource is exist
    copyResource (getResourceFromName(resourcetobackup),resourcetobackup .. "_backup") -- copy the resource and give it the name [resource]_backup
    outputChatBox ("Resource " .. resourcetobackup .. " succesfully backed up!",player,255,0,0,false) -- say it's OK!
  else -- if it isn't exist
    outputChatBox ("Resource can't be backed up! (don't forget the parameters!)",player,255,0,0,false) -- say it isn't exist!
  end
end
addCommandHandler ("backupresource",backupResouce) -- add command
```

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- [callRemote](mta://scripting/server/functions/callremote.md)

- copyResource

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
