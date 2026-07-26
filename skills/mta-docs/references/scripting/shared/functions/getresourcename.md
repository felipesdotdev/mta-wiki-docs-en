---
doc_id: "mta-wiki:2620"
title: "GetResourceName"
source_title: "GetResourceName"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceName"
revision_id: 79904
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
---

# GetResourceName

This function gets the name of the specified resource.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

Specifying the resource parameter is not mandatory now, in this case this resource is used as a basis

| [[{{{image}}}\|link=\|]] | Note: Every resource has a predefined global variable called resourceName whose value is the name of that resource. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: If you want to access the name of any resource-data you should use getElementID . |
| --- | --- |
|  |  |

## Syntax

```
string getResourceName ( [ resource res = getThisResource() ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):getName(...)*

**Variable**: *.name*

**Counterpart**: *[renameResource](mta://scripting/server/functions/renameresource.md)*

### Arguments

- **res:** The resource you wish to get the name of.

### Returns

Returns a string with the resource name in it, or *false* if the resource does not exist.

## Example

Click to collapse [-]
Server

This simple example outputs a message in the console whenever a resource starts, stating the name of the resource.

```
addEventHandler("onResourceStart", getRootElement(),
    function(res)
        outputConsole("Resource " .. getResourceName(res) .. " just started.")
    end
)
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- getResourceName

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
