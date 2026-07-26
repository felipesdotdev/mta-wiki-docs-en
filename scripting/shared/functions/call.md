---
doc_id: "mta-wiki:2611"
title: "Call"
source_title: "Call"
source_url: "https://wiki.multitheftauto.com/wiki/Call"
revision_id: 82833
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:10:32.269292+00:00"
---

# Call

| [[{{{image}}}\|link=\|]] | Important Note: Calls (exports) may incur a performance overhead - they are not equivalent in performance to calling functions in the same resource. Do not use exports in render events (like onClientRender ), or in fast processing logic, unless you want to kill performance. The sourceResource and sourceResourceRoot "hidden" variables are available even if you use exports.*:* Using this function straight away on resource start might cause elements to not be passed properly, use setTimer in order to delay function execution and to avoid this issue. |
| --- | --- |
|  |  |

This function is used to call a function from another resource (which must be running).

The function which you wish to call **must** first be exported within the resource's meta.  For example:

```
<meta>
	<info author="jbeta" type="script" description="Scoreboard resource" />
	<script src="scoreboard_client.lua" type="client"/>
	<script src="scoreboard_exports.lua" type="server"/>
	
	<script src="scoreboard_http.lua" type="server"/>
	
	<export function="getScoreboardColumns" http="true" />
	<export function="getScoreboardRows" http="true" />
	
	<export function="addScoreboardColumn" type="server"/>
	<export function="removeScoreboardColumn" type="server"/>
	
	<export function="setPlayerScoreboardForced" type="server"/>
	<export function="setScoreboardForced" type="client"/>
</meta>
```

This enables other resources to call a function from this resource.

You cannot call a server function from the client or vice versa. See [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) and [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) for possibilities to do that.

There is an easier syntax replacing this function. For example, you can instead of:

```
call ( getResourceFromName ( "resource" ), "exportedFunction", 1, "2", "three" )
```

do much like a normal call:

```
exports.resource:exportedFunction ( 1, "2", "three" )
```

If the resource name contains illegal characters (such as hyphens), you can also do:

```
exports["resource-name"]:exportedFunction ( 1, "2", "three" )
```

Two extra "hidden" variables are passed to the exported function:

- **sourceResource** - The resource that called the exported function

- **sourceResourceRoot** - The resource root element of the resource which called the exported function.

## Syntax

```
var... call ( resource theResource, string theFunction, [ arguments... ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[resource](mta://reference/misc/resource.md):call(...)*

### Required Arguments

- **theResource:** This is a resource pointer which refers to the resource you are calling a function from.

- **theFunction:** This is a string with the name of the function which you want to call.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **arguments:** Any arguments you may want to pass to the function when it is called. Any number of arguments of can be specified, each being passed to the designated function.

### Returns

Returns anything that the designated function has returned, if the function has no return, nil is returned. If the function does not exist, is not exported, or the call was not successful it will return false.

## Syntax

```
exports["resource_name"]:exportedFunction([ arguments... ])
```

```
exports.resource_name:exportedFunction([ arguments... ])
```

### Required Arguments

- **resource_name:** Resource name

- **exportedFunction:** The name of the function you want to call. Its **not** a string.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **arguments:** Any arguments you may want to pass to the function when it is called. Any number of arguments of can be specified, each being passed to the designated function.

### Returns

Returns anything that the designated function has returned, if the function has no return, nil is returned. If the function does not exist, is not exported, or the call was not successful it will return false.

## Example

Click to collapse [-]
Server

This extract shows adding of a "kills" column to the scoreboard resource. This then sets the *gameShowKills* variable to true(or false), telling the rest of the script to start outputting kills.

**Main Resource:**

```
function showKills ( option )
	if not option then
		-- Remove the "kills" column
		call(getResourceFromName("scoreboard"), "removeScoreboardColumn", "kills")
	else
		-- Add the "kills" column
		call(getResourceFromName("scoreboard"), "addScoreboardColumn", "kills")
		outputDebugString ( "Showing kills now..." )
	end
	gameShowKills = option 
end
```

**Scoreboard resource:**

```
function removeScoreboardColumn(columnName)
    -- What ever scripted ...
end

function addScoreboardColumn(columnName)
    -- What ever scripted ...
end
```

Inside the scoreboard resource's meta.xml:

```
<export function="removeScoreboardColumn" type="client" />
<export function="addScoreboardColumn" type="client" />
```

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- call

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
