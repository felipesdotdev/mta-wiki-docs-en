---
doc_id: "mta-wiki:6007"
title: "UpdateResourceACLRequest"
source_title: "UpdateResourceACLRequest"
source_url: "https://wiki.multitheftauto.com/wiki/UpdateResourceACLRequest"
revision_id: 81046
language: "en"
categories: ["Server_functions"]
---

# UpdateResourceACLRequest

This function changes the access for one ACL request of the given resource.

| [[{{{image}}}\|link=\|]] | Note: This function is protected by default and must be explicitly allowed in the server ACL. |
| --- | --- |
|  |  |

## Syntax

```
bool updateResourceACLRequest ( resource theResource, string rightName, bool access [, string byWho = "" ] )
```

### Required Arguments

- **theResource:** the resource to set the ACL request for.

- **rightName:** a string with the name of the right to set the access for. This has to match an existing ACL request.

- **access:** a boolean value setting the access. True is for allow, and false for deny.

### Optional Arguments

- **byWho:** a string value to identity who is changing the setting.

### Returns

Returns true if the setting was changed, or *false* if no change was required or there was a problem with the arguments.

## Example

This function will allow all ACL requests from 'theResource'

```
function allowAllACLRequests(theResource)
  local requests = getResourceACLRequests (theResource)
  for _,request in ipairs(requests) do
    updateResourceACLRequest ( theResource, request.name, true ) 
  end
end
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

- [startResource](mta://scripting/server/functions/startresource.md)

- [stopResource](mta://scripting/server/functions/stopresource.md)

- updateResourceACLRequest
  

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
