---
doc_id: "mta-wiki:4646"
title: "GetResourceDynamicElementRoot"
source_title: "GetResourceDynamicElementRoot"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceDynamicElementRoot"
revision_id: 71640
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:23.168491+00:00"
---

# GetResourceDynamicElementRoot

This function retrieves the *dynamic element root* of a specified [resource](mta://reference/misc/resource.md). The *dynamic element root* is the parent of elements that are created by scripts (e.g. with [createObject](mta://scripting/shared/functions/createobject.md)) unless they specify a different parent.

## Syntax

```
element getResourceDynamicElementRoot ( resource theResource )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getDynamicElementRoot(...)*

**Variable**: *.dynamicElementRoot*

### Required Arguments

- **theResource:** the resource of which dynamic element root we want.

### Returns

Returns an [element](mta://reference/misc/element.md) of the resource's dynamic element root if the resource specified was valid and active (currently running), *false* otherwise.

## Example

This example shows how to get all elements by specific type, created only by resource scripts (not maps).

```
-- We have some map files with many objects in our meta.xml.
-- And we have some objects, created by some resource scripts.

--      createObject(...) -- 1
--      createObject(...) -- 2
--      ...
--      createObject(...) -- 20

-- After resource start we must found all objects, created only
-- by current resource scripts (not maps) and make them invisible.

-- `resourceRoot` is predefined script variable containing current resource root pointer
addEventHandler( 'onResourceStart', resourceRoot,
    function()
        -- `resource` is predefined script variable containing current resource pointer
        local thisResourceDynamicRoot = getResourceDynamicElementRoot(resource)
        local onlyScriptObjects = getElementsByType( 'object', thisResourceDynamicRoot )
        
        for scriptObject in ipairs(onlyScriptObjects) do
            setElementAlpha( scriptObject, 0 )
        end
    end
)
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- getResourceDynamicElementRoot

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
