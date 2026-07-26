---
doc_id: "mta-wiki:2735"
title: "GetResourceRootElement"
source_title: "GetResourceRootElement"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceRootElement"
revision_id: 82712
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# GetResourceRootElement

This function retrieves a resource's root element. The resource's root element is the element in the element tree which is the parent of all elements that belong to a particular resource (except for elements specifically created elsewhere). You can attach event handlers to this element to easily capture events that originate from your resource (and global events that originate from the root element).

Note: every resource has a [predefined global variable](mta://reference/misc/predefined-variables-list--8354582f.md) called *resourceRoot* whose value is the root element of that resource.

## Syntax

```
element getResourceRootElement ( [resource theResource=getThisResource()] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getRootElement(...)*

**Variable**: *.rootElement*

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **theResource:** the resource whose root element we are getting. If not specified, assumes the current resource. (the resource returned from [getThisResource](mta://scripting/shared/functions/getthisresource.md))

### Returns

Returns an *element* representing the resource's root, *false* if the specified resource doesn't exist.

## Example

Click to collapse [-]
Server

This example retrieves the current resource's root element and attaches it to an onResourceStart event handler. This causes the event handler to get called only when the *current* resource is started rather than when *any* resource is started, thereby reducing unnecessary overhead.

```
-- get the root element of this resource (the resource that the script is a part of)
resourceRoot = getResourceRootElement()

-- create a function to handle the onResourceStart event
function onCurrentResourceStart(theResource)
    local resourceName = getResourceName(theResource)
    outputChatBox("Hello and welcome to " .. resourceName .. "!")
end

-- add the event handler
addEventHandler("onResourceStart", resourceRoot, onCurrentResourceStart)
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

- getResourceRootElement

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
