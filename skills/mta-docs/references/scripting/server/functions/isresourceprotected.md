---
doc_id: "mta-wiki:12370"
title: "IsResourceProtected"
source_title: "IsResourceProtected"
source_url: "https://wiki.multitheftauto.com/wiki/IsResourceProtected"
revision_id: 81238
language: "en"
categories: ["Server_functions", "Changes_in_1.5.7"]
---

# IsResourceProtected

This will check if a resource is currently protected, as defined in [mtaserver.conf](mta://reference/misc/server-mtaserver-conf.md).

## Syntax

```
bool isResourceProtected(resource theResource)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):isProtected(...)*

**Variable**: *.protected*

### Required Arguments

- **theResource:** the resource to check

### Returns

Returns *true* if the resource is 'protected', *false* otherwise.

## Example

This example creates a command which allows you to check if the given resource with the name provided is protected. The command is "/isprotected [Resource Name]".

```
function resourceProtectedCommand(thePlayer, command, resourceName)
    if resourceName then -- If the player provided a resource name.
        local theResource = getResourceFromName(resourceName) -- Get the resource element.
        if theResource then -- If we have an element, the resource must exist.
            local protectedResource = isResourceProtected(theResource) -- Check to see if the resource is protected.
            if protectedResource then -- if it is protected.
                outputChatBox("This resource is a protected resource in the server config.", thePlayer, 0, 255, 0)
            else -- If the resource is not protected.
                outputChatBox("This resource is not a protected resource in the server config.", thePlayer, 0, 255, 0)
            end
        else -- A resource with the name didn't exist.
            outputChatBox("A resource with the name '" .. resourceName .. "' does not exist!", thePlayer, 255, 0, 0)
        end
    else -- The player didn't provide a resource name.
        outputChatBox("Please specify a resource name.", thePlayer, 255, 0, 0)
    end
end
addCommandHandler("isprotected", resourceProtectedCommand)
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

- isResourceProtected

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
