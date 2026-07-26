---
doc_id: "mta-wiki:2609"
title: "GetThisResource"
source_title: "GetThisResource"
source_url: "https://wiki.multitheftauto.com/wiki/GetThisResource"
revision_id: 76286
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetThisResource

This function retrieves the resource from which the function call was made.

| [[{{{image}}}\|link=\|]] | Note: Every resource has a predefined global variable called resource that contains the resource pointer for that resource, in other words, the value that this function returns. |
| --- | --- |
|  |  |

## Syntax

```
resource getThisResource ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Resource class.*

**Method**: *[Resource](mta://reference/misc/resource.md).getThis(...)*

### Returns

Returns the resource in which the current script is.

## Example

This example retrieves the current resource's root element and attaches it to an onResourceStart event handler. This causes the event handler to get called only when the *current* resource is started rather than when *any* resource is started, thereby reducing unnecessary overhead.

```
local thisResource = getThisResource()
local resRoot = getResourceRootElement(thisResource)

addEventHandler("onResourceStart", resRoot, function()
   local resourceName = getResourceName(thisResource)
   iprint("You are in the " .. resourceName .. " resource!")
   iprint(thisResource == resource) -- true
   iprint(resRoot == resourceRoot) -- true
end)
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

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- getThisResource

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
