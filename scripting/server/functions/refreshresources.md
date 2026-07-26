---
doc_id: "mta-wiki:5622"
title: "RefreshResources"
source_title: "RefreshResources"
source_url: "https://wiki.multitheftauto.com/wiki/RefreshResources"
revision_id: 80426
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:31.701550+00:00"
---

# RefreshResources

This function finds new resources and checks for changes to the current ones.

| [[{{{image}}}\|link=\|]] | Note: The resource using this function needs access to function.refreshResources in order for this function to work. You can give it the access by including an aclrequest command in its meta.xml file or by adding it to the admin ACL group. |
| --- | --- |
|  |  |

## Syntax

```
bool refreshResources ( [ bool refreshAll = false, resource targetResource = nil ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **refreshAll**: If *true* MTA will check for changes in all resources. If *false*, MTA will only check for new resources and try to reload resources with errors

ADDED/UPDATED IN VERSION 1.5.5-9.11718 :

- **targetResource**: If set, the refresh is restricted to the supplied resource only

**Note:** Checking for changes in all resources can result in lag for a short period of time. It should generally be avoided to set refreshAll to *true*.

### Returns

Returns true if refresh was successful, false otherwise.

## Example

Click to collapse [-]
Server

This example will refresh resources when a player uses the /refreshresources command just like the hardcoded /refreshall.

```
function commandRefreshResources(player)
    refreshResources(true)
    outputChatBox("Resources refreshed", player, 255, 255, 0)
end
addCommandHandler("refreshresources", commandRefreshResources)
```

This example will refresh only the named resource:

```
refreshResources(true, getResourceFromName("admin"))
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-9.11718 | Added targetResource argument |
| --- | --- |

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

- [getResourceMapRootElement](mta://scripting/server/functions/getresourcemaprootelement.md)

- [getResourceOrganizationalPath](mta://scripting/server/functions/getresourceorganizationalpath.md)

- [getResources](mta://scripting/server/functions/getresources.md)

- [isResourceArchived](mta://scripting/server/functions/isresourcearchived.md)

- [isResourceProtected](mta://scripting/server/functions/isresourceprotected.md)

- refreshResources

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
