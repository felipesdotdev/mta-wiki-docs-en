---
doc_id: "mta-wiki:2621"
title: "GetResourceFromName"
source_title: "GetResourceFromName"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceFromName"
revision_id: 65009
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4.1"]
generated_at: "2026-07-26T16:15:23.196123+00:00"
---

# GetResourceFromName

This function is used to retrieve a resource from its name. A resource's name is the same as its folder or file archive name on the server (without the extension).

## Syntax

```
resource getResourceFromName ( string resourceName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Resource class. OOP function available client side*

**Method**: *[Resource](mta://reference/misc/resource.md).getFromName(...)*

### Required Arguments

- **resourceName:** the name of the resource you wish to get.

### Returns

Returns the [resource](mta://reference/misc/resource.md) with the specified name, or *false* if no resource of that name exists. Note that clientside this will also return *false* for resources that are in the *loaded* state, since the client is unaware of resources that have not been started.

## Example

Click to collapse [-]
Server

This example prints out a message to the chatbox when a resource named *playerblips* is started.

```
function onStart( theResource )
     local blipsResource = getResourceFromName ( "playerblips" ) -- get the resource of name "playerblips"
     if ( blipsResource and theResource == blipsResource ) then -- check if the resource started was it
          outputChatBox ( "Blips resource started!" )
     end
end
addEventHandler ( "onResourceStart", getRootElement(), onStart )
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- getResourceFromName

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
