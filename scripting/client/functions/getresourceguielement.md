---
doc_id: "mta-wiki:3993"
title: "GetResourceGUIElement"
source_title: "GetResourceGUIElement"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceGUIElement"
revision_id: 57559
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:23.208402+00:00"
---

# GetResourceGUIElement

This function retrieves a resource's GUI element. The resource's GUI element is the element in the element tree which is the default parent of all GUI elements that belong to a particular resource. It has a predefined variable called **guiRoot**, and each resource has one of these. You can attach event handlers to this element to easily capture events that originate from your resource (and global events that originate from the root element).

## Syntax

```
element getResourceGUIElement ( [ resource theResource = getThisResource( ) ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **theResource:** the resource whose GUI element we are getting. If not specified, assumes the current resource.

### Returns

Returns the root GUI element that contains all the other GUI elements.

## Example

This example provides a function for destroying all the GUI elements of a resource.

```
function destroyAllGUIs()
	-- Destroy all of the gui-root's children
	for _, guiElement in ipairs(getElementChildren(getResourceGUIElement())) do
		if isElement(guiElement) then -- This checks that the element still exists (in case we already destroyed it's parent).
			destroyElement(guiElement)
		end
	end
end
```

## See Also

- getResourceGUIElement
  

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
