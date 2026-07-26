---
doc_id: "mta-wiki:4647"
title: "GetResourceMapRootElement"
source_title: "GetResourceMapRootElement"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceMapRootElement"
revision_id: 80421
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:23.316649+00:00"
---

# GetResourceMapRootElement

This function retrieves the root element of a certain [map](https://wiki.multitheftauto.com/index.php?title=Map&action=edit&redlink=1) in a specified [resource](mta://reference/misc/resource.md).

## Syntax

```
element getResourceMapRootElement ( resource theResource, string mapName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getMapRootElement(...)*

### Required Arguments

- **theResource:** the resource where the map is located

- **mapName:** name of the maps which root element we want to retrieve, file extension is required

### Returns

Returns an the resource's map root [element](mta://reference/misc/element.md) if the map exists and resource specified was valid and active (currently running), *false* otherwise.

## Example

This example shows how to get all elements of specific type only from one map.

```
-- We have 2 map files in our meta.xml: island_1.map, island_2.map.
-- These maps contains objects, vehicles, pickups, etc.
-- After resource start we must found all vehicles only from island_1.map and lock them.

-- `resourceRoot` is predefined script variable containing current resource root pointer
addEventHandler( 'onResourceStart', resourceRoot,
    function()
        -- `resource` is predefined script variable containing current resource pointer
        local island_1_mapRoot = getResourceMapRootElement( resource, 'island_1.map' )
        local island_1_vehicles = getElementsByType( 'vehicle', island_1_mapRoot )
        
        for vehicle in ipairs(island_1_vehicles) do
            setVehicleLocked( vehicle, true )
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

- getResourceMapRootElement

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
