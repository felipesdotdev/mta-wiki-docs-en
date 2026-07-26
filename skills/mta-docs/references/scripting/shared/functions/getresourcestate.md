---
doc_id: "mta-wiki:2608"
title: "GetResourceState"
source_title: "GetResourceState"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceState"
revision_id: 78902
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetResourceState

This function returns the state of a given resource

## Syntax

```
string getResourceState ( resource theResource )
```

### Required Arguments

- **theResource:** The resource you wish to get the state of.

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getState(...)*

**Variable**: *.state*

### Returns

If successful returns a string with the resource state in it, *false* otherwise.
The state can be one of:

- **loaded**

- **running**

- **starting**

- **stopping**

- **failed to load** - Use [getResourceLoadFailureReason](mta://scripting/server/functions/getresourceloadfailurereason.md) to find out why it failed.

## Example

This example returns the state of a given resource. Syntax: */state <Resource Name>*

```
function getState( player, command, resourceName )
	if not resourceName then
		outputChatBox( "Syntax: " .. command .. " [resource name]", player, 255, 0, 0 )
		return
	end
	local resource = getResourceFromName( resourceName )
	if not resource then
		outputChatBox( "Error: No resource with name " .. resourceName .. " exists.", player, 255, 0, 0 )
		return
	end
	local state = getResourceState( resource )
	outputChatBox( "Resource " .. resourceName .. " is " .. state, player, 0, 0, 255 )
end

addCommandHandler( "state", getState )
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- getResourceState

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
