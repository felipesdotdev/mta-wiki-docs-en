---
doc_id: "mta-wiki:4649"
title: "SetResourceDefaultSetting"
source_title: "SetResourceDefaultSetting"
source_url: "https://wiki.multitheftauto.com/wiki/SetResourceDefaultSetting"
revision_id: 73917
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events"]
generated_at: "2026-07-26T16:16:44.302008+00:00"
---

# SetResourceDefaultSetting

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function doesn't work actually. See issues for more information. |  |

This function is used to set a default setting for a specified [resource](mta://reference/misc/resource.md).

## Syntax

```
bool setResourceDefaultSetting ( resource theResource, string settingName, string/int/float settingValue )
```

### Required Arguments

- **theResource:** the resource where the setting is located

- **settingName:** the name of the default setting

- **settingValue:** the new value of the setting

### Returns

Returns *true* if the default setting was successfully set, *false* otherwise.

## Example

This example checks to see if the server has the freeroam server then sets "spawnmaponstart" to "false".

```
addEventHandler("onResourceStart",resourceRoot,function()
	local freeroamRes = getResourceFromName("Freeroam")
	if(freeroamRes)then
		setResourceDefaultSetting(freeroamRes,"spawnmaponstart","false")
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
