---
doc_id: "mta-wiki:3383"
title: "CallRemote"
source_title: "CallRemote"
source_url: "https://wiki.multitheftauto.com/wiki/CallRemote"
revision_id: 80412
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:10:39.767206+00:00"
---

# CallRemote

This function allows you to call functions that have been exported with HTTP access by other MTA servers. The calls are asynchronous so you do not get an immediate result from the call, instead a callback function you specify is called when the call returns.

You can also use this function to access a standard web page on a server you own by specifying the URL. The arguments you specify to callRemote are passed to the web page using HTTP POST as a [JSON](mta://reference/misc/json.md) array. This will always have an array as the root element. The page must return a JSON formated *array* in the page's body with the results of the call (or an empty array if there are no results).

You can use the [PHP SDK](mta://tutorials/php-sdk.md) to create PHP pages that can be called by this function. See the PHP SDK page for an example.

In addition, it is possible to use this function to get information about a resource in the MTA community, besides other things. Check out the [Community Resources](mta://reference/misc/community-resources.md) article.

In the case when the call fails, a string containing "ERROR" followed by an integer containing the error reason will be passed to the callback function. The reason for failure will be similar to errors found with websites - file not found, server not found and timeouts.

## Syntax

```
bool callRemote ( string host[, string queueName = "default" ][, int connectionAttempts = 10, int connectTimeout = 10000 ], string resourceName, string functionName, callback callbackFunction, [ arguments... ] )
```

**OR**

```
bool callRemote ( string URL[, string queueName = "default" ][, int connectionAttempts = 10, int connectTimeout = 10000 ], callback callbackFunction, [ arguments... ] )
```

### Required Arguments

- **host:** This is a host name - including the **HTTP** port - of the server you wish to connect to.

- **resourceName:** This is a name of the resource that contains the exported function you want to call.

- **functionName:** This is a string with the name of the function which you want to call.

- **URL:** A full URL in the format *http://hostname/path/file.ext*. A port can be specified with a colon followed by a port number appended to the hostname.

- **callbackFunction:** This is the function that should receive the data returned from the remote function call. The argument list should match the format of the data returned. The callback function will be passed a string containing "ERROR" followed by an integer indicating the error code when an error occurs calling the function. A list of error codes [can be found here](https://wiki.multitheftauto.com/wiki/Template:Error_codes_for_callRemote_and_fetchRemote).

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

ADDED/UPDATED IN VERSION 1.5.3-9.11270 :

- **queueName:** Name of the queue to use. Any name can be used. If not set, the queue name is "default". Requests in the same queue are processed in order, one at a time.

- **connectionAttempts:** Number of times to retry if the remote host does not respond. *In the case of a non-responding remote server, each connection attempt will timeout after 6 seconds. Therefore, the default setting of 10 connection attempts means it will be 60 seconds before your script gets a callback about the error. Reducing this value to 2 for example, will decrease that period to 12 seconds*

- **connectTimeout:** Number of milliseconds each connection attempt will take before timing out

- **arguments:** Any arguments you may want to pass to the function when it is called. Any number of arguments of can be specified, each being passed to the designated function. Most data types can be passed, including tables. The only values that cannot be passed are 'userdata' values such as xmlnodes - elements and resources can be passed though may be misinterpreted on other game servers (or cause warnings).

### Returns

Returns *true* if the function has been called, *false* otherwise.

## Example

This example shows you how you can call a PHP page from a Lua script. It just adds two numbers passed to it by the script and outputs these in the chat box.

**PHP:** (for the page that Lua expects to be at *http://www.example.com/page.php*)

```
[php]
include( "mta_sdk.php" );
$input = mta::getInput();
mta::doReturn($input[0] + $input[1]);
```

**Lua:**

```
-- result is called when the function returns
function result(sum)
    if sum ~= "ERROR" then
        outputChatBox(sum)
    end
end
function addNumbers(number1, number2)
    callRemote ( "http://www.example.com/page.php", result, number1, number2 )
end 
addNumbers ( 123, 456 ) -- call the function
```

**Example 2:** This example shows how you can join up multiple servers so they can share chat messages.

**meta.xml**
First, add *outputChatBoxRemote* as an HTTP exported function in your resource's meta.xml:

```
<export function="outputChatBoxRemote" http="true" />
```

**Lua:** Next, add this to a server-side script in your resource:

```
-- Remote function set with callRemote 'functionName' argument
-- Called from/on remote servers
function outputChatBoxRemote ( playerName, message, type, serverport )
    outputChatBox ( "From " .. playerName .. " on " .. serverport .. ": " .. message )
    return "hello sailor"
end

-- Callback set with callRemote 'callbackFunction' argument
-- Called on the local server when callRemote has completed successfully or with errors
function finishedCallback( responseData, errno )
    responseData = tostring(responseData)
    if responseData == "ERROR" then
        outputDebugString( "callRemote: ERROR #" .. errno )
    elseif responseData ~= "hello sailor" then
        outputDebugString( "callRemote: Unexpected reply: " .. responseData  )
    else
        -- callRemote completed successfully
    end
end

function playerChat ( message, type )
    callRemote ( "play.mtabeta.com:33004", getResourceName(getThisResource()), "outputChatBoxRemote", finishedCallback, getPlayerName(source), message, type, getServerPort() )
    callRemote ( "play.mtabeta.com:33005", getResourceName(getThisResource()), "outputChatBoxRemote", finishedCallback, getPlayerName(source), message, type, getServerPort() )
    callRemote ( "play.mtabeta.com:33006", getResourceName(getThisResource()), "outputChatBoxRemote", finishedCallback, getPlayerName(source), message, type, getServerPort() )
end
addEventHandler ( "onPlayerChat", getRootElement(), playerChat )
```

**ACL:**
Then, modify the ACL on each sending server to allow access to callRemote:

```
<group name="OutRPCGroup">
    <acl name="OutRPC" />
    <object name="resource.examplechat" />
</group>
<acl name="OutRPC">
    <right name="function.callRemote" access="true" />
</acl>
```

**ACL #2:**
Finally, modify the ACL on each receiving server to allow guest http communication with your resource:

```
<group name="InRPCGroup">
    <acl name="InRPC" />
    <object name="user.http_guest" />
</group>
<acl name="InRPC">
    <right name="resource.examplechat.http" access="true" />
</acl>
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.1-9.04605 | Added connectionAttempts argument |
| --- | --- |

| 1.5.3-9.11270 | Added queueName argument |
| --- | --- |

## See Also

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- callRemote

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

- [refreshResources](mta://scripting/server/functions/refreshresources.md)

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
