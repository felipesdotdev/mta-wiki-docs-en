---
doc_id: "mta-wiki:2610"
title: "GetResourceConfig"
source_title: "GetResourceConfig"
source_url: "https://wiki.multitheftauto.com/wiki/GetResourceConfig"
revision_id: 30187
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetResourceConfig

This function is used to return the root node of a configuration file. Config files must be predefined in a resource's [meta file](mta://reference/misc/meta-xml.md).  An alternative way to load XML files is to use [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md).

## Syntax

```
xmlnode getResourceConfig ( string filePath )
```

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'settings.xml' in the resource 'ctf', it can be accessed from another resource this way: *getResourceConfig(":ctf/settings.xml")*.

If the file is in the current resource, only the file path is necessary, e.g. *getResourceConfig("settings.xml")*.

### Returns

Returns the root node of the specified configuration file. If the file is corrupted, not defined in the meta file or doesn't exist, returns false.

## Example

Click to collapse [-]
Server

This example opens a configuration file and prints the value of the 'attr' attribute of the first 'group' node.

```
function resourceStart ( )                         -- When the resource is started
    local node = getResourceConfig( "config.xml" )  -- get the configuration file
    local subNode = xmlFindChild( node, "group", 0 )      -- get a subnode in it
    outputChatBox( xmlNodeGetAttribute( subNode, "attr" ),root )    -- output its attributes value to chatbox
end
addEventHandler ( "onResourceStart", resourceRoot, resourceStart )
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- getResourceConfig

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)
