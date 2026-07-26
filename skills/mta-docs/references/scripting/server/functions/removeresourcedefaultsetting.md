---
doc_id: "mta-wiki:4648"
title: "RemoveResourceDefaultSetting"
source_title: "RemoveResourceDefaultSetting"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveResourceDefaultSetting"
revision_id: 73902
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events"]
---

# RemoveResourceDefaultSetting

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function doesn't work actually. See issues for more information. |  |

This function is used to remove a default setting from specified [resource](mta://reference/misc/resource.md).

## Syntax

```
bool removeResourceDefaultSetting ( resource theResource, string settingName )
```

### Required Arguments

- **theResource:** the resource which setting is to be removed

- **settingName:** name of the default setting which is to be removed

### Returns

Returns *true* if the default setting was successfully removed, *false* otherwise.

## Example

This example would check if the server has the freeroam resource and removes the default settings called "spawnmaponstart".

```
addEventHandler("onResourceStart",resourceRoot,function()
	local freeroamRes = getResourceFromName("Freeroam")
	if(freeroamRes)then
		removeResourceDefaultSetting(freeroamRes,"spawnmaponstart")
	end
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

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
