---
doc_id: "mta-wiki:5878"
title: "DeleteResource"
source_title: "DeleteResource"
source_url: "https://wiki.multitheftauto.com/wiki/DeleteResource"
revision_id: 81025
language: "en"
categories: ["Server_functions"]
---

# DeleteResource

This function deletes a resource from the MTA memory and moves it to the **/resources-cache/trash/** directory.

## Syntax

```
bool deleteResource ( string resourceName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Resource class.*

**Method**: *[Resource](mta://reference/misc/resource.md).delete(...)*

### Required Arguments

- **resourceName:** The name of resource to delete.

### Returns

Returns *true* if the resource has been deleted successfully, *false* otherwise.

## Example

This example adds a command to delete a certain resource (admins only, no spaces in resource name allowed).

```
addCommandHandler ( "removeresource",
function ( playerSource, commandName, name )
    --Check if it is an admin using this command
    if not isObjectInACLGroup ( "user." .. getAccountName ( getPlayerAccount ( playerSource ) ), aclGetGroup ( "Admin" ) ) then
        outputChatBox ( "You are not allowed to use this command", playerSource )
        return
    end 
    --Did the user pass a valid resource name?
    if not name or name == "" or name == " " then
        outputChatBox ( "An invalid resource name has been passed (/removeresource <name>)", playerSource )
        return
    end
    --Let us check if the resource name exists
    --Get all resources
    local resourceTable = getResources ( ) 
    for resourceKey, resourceValue in ipairs ( resourceTable ) do
        local resourceName = getResourceName ( resourceValue )
        --Does the resource exist?
        if name == resourceName then
            --Stop the resource (maybe it is running)
            stopResource ( resourceValue )
            --Delete it
            local deleted = deleteResource ( name )
            if deleted then
                outputChatBox ( "Resource " .. name .. " has been successfully removed", playerSource )
            else
                outputChatBox ( "There is an unknown problem with the resource", playerSource )			
            end
            --The function is finished and was successful, return to stop it
            return
        end
    end
    --If a resource with the specified name does not exist show an error message
    outputChatBox ( "The specified resource does not exist", playerSource )
end )
```

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- [callRemote](mta://scripting/server/functions/callremote.md)

- [copyResource](mta://scripting/server/functions/copyresource.md)

- [createResource](mta://scripting/server/functions/createresource.md)

- deleteResource

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
