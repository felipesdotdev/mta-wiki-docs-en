---
doc_id: "mta-wiki:6006"
title: "GetResourceACLRequests"
source_title: "GetResourceACLRequests"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceACLRequests"
revision_id: 81045
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:23.145214+00:00"
---

# GetResourceACLRequests

This function retrieves the ACL request section from the meta.xml file of the given resource.

## Syntax

```
table getResourceACLRequests ( resource theResource )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getACLRequests(...)*

**Variable**: *.aclRequests*

### Required Arguments

- **theResource:** the resource to get the ACL requests for.

### Returns

Returns a *table* with the ACL requests for the given resource, or *false* if the resource is not valid. A valid resource with no ACL requests will return an empty table.

## Example

This function lists ACL requests from all resources in the client console.

```
function showAllACLRequests()
  for _,resource in ipairs(getResources()) do
    local requests = getResourceACLRequests (resource)
    if #requests > 0 then
      outputConsole( getResourceName(resource).." has "..#requests.." ACL request(s)" )
      for i,request in ipairs(requests) do
        outputConsole( tostring(i)
                 .. "  name:" .. request.name
                 .. "  access:" .. tostring(request.access)
                 .. "  pending:" .. tostring(request.pending)
                 .. "  who:" .. request.who
                 .. "  date:" .. request.date
               )
      end
    end
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

- getResourceACLRequests

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
