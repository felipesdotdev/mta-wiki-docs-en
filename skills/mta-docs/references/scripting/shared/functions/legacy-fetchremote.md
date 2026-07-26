---
doc_id: "mta-wiki:14484"
title: "Legacy/fetchRemote"
source_title: "Legacy/fetchRemote"
source_url: "https://wiki.multitheftauto.com/wiki/Legacy/fetchRemote"
revision_id: 81404
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# Legacy/fetchRemote

This function allows you to post and receive data from HTTP servers. The calls are asynchronous so you do not get an immediate result from the call, instead a callback function you specify is called when the download completes.

In the case when the call fails, a string containing "ERROR" followed by an integer containing the error reason will be passed to the callback function. The reason for failure will be similar to errors found with websites - file not found, server not found and timeouts.

If you are using fetchRemote to connect to a PHP script, you can use **file_get_contents('php://input')** to read the **postData** sent from this function.

| [[{{{image}}}\|link=\|]] | Note: Client side function only works with the server the player is connected to unless the domain has been accepted with requestBrowserDomains |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: function won't trigger inside another fetchRemote function |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: When using toJSON for submitting data, make sure to use string.sub(data, 2, -2) to remove the brackets as many APIs will not understand the request |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This page only contains legacy implementations. For current implementation check fetchRemote |
| --- | --- |
|  |  |

## Syntax

```
bool fetchRemote ( string URL, [ string queueName = "default" ], [ int connectionAttempts = 10, int connectTimeout = 10000 ], function callbackFunction, [ string postData = "",  bool postIsBinary = false ], [ arguments... ] )
```

### Required Arguments

- **URL:** A full URL in the format *http://hostname/path/file.ext*. A port can be specified with a colon followed by a port number appended to the hostname.

- **callbackFunction:** This is the function that should receive the data returned from the remote server. The callback argument list should be:

- ***responseData*** - A string containing the remote response or "ERROR" if there was a problem

- ***error*** - A number containing the error number or zero if there was no error. A list of possible error values are:

- **1-89**: See [cURL website](http://curl.haxx.se/libcurl/c/libcurl-errors.html) or its mirror at [cURL errors](mta://reference/misc/curl-errors.md)

- **400-599**: See [HTTP status codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)

- **1002**: Download aborted

- **1003**: Failed to initialize

- **1004**: Unable to parse url

- **1005**: Unable to resolve host name

- **1006**: Destination IP not allowed

- **1007**: File error

- ***arguments...*** - The arguments that were passed into fetchRemote

### Optional Arguments

ADDED/UPDATED IN VERSION 1.5.3-9.11270 :

- **queueName:** Name of the queue to use. Any name can be used. If not set, the queue name is "default". Requests in the same queue are processed in order, one at a time.

- **connectionAttempts:** Number of times to retry if the remote host does not respond. *In the case of a non-responding remote server, each connection attempt will timeout after 10 seconds. Therefore, the default setting of 10 connection attempts means it will be 100 seconds before your script gets a callback about the error. Reducing this value to 2 for example, will decrease that period to 20 seconds*

- **connectTimeout:** Number of milliseconds each connection attempt will take before timing out

- **postData:** A string specifying any data you want to send to the remote HTTP server.

- **postIsBinary :** A boolean specifying if the data is text, or binary.

- **arguments:** Any arguments you may want to pass to the callback.

ADDED/UPDATED IN VERSION 1.5.4-9.11342 :

## Syntax

```
bool fetchRemote ( string URL[, table options ], callback callbackFunction[, table callbackArguments ] )
```

### Required Arguments

- **URL:** A full URL in the format *http://hostname/path/file.ext*. A port can be specified with a colon followed by a port number appended to the hostname.

- **callbackFunction:** This is the function that should receive the data returned from the remote server. The callback argument list should be:

- ***responseData*** - A string containing the remote response

- ***responseInfo*** - A table containing:

- ***success*** - A boolean indicating if the request was successful.

- ***statusCode*** - An integer status/error code

- ***headers*** - A table containing the HTTP response headers

- ***arguments...*** - The arguments that were passed into fetchRemote

### Optional Arguments

- **options:** A table containing any request options:

- **queueName:** Name of the queue to use. Any name can be used. If not set, the queue name is "default". Requests in the same queue are processed in order, one at a time.

- **connectionAttempts:** Number of times to retry if the remote host does not respond. *(Defaults to 10)*

- **connectTimeout:** Number of milliseconds each connection attempt will take before timing out. *(Defaults to 10000)*

- **postData:** A string specifying any data you want to send to the remote HTTP server.

- **postIsBinary :** A boolean specifying if the data is text, or binary. *(Defaults to false)*

- **method:** A string specifying the request method. *(Defaults to GET or POST)*

- **headers:** A table containing HTTP request headers. *e.g.{ Pragma="no-cache" }*

- **maxRedirects:** An integer limiting the number of HTTP redirections to automatically follow. *(Defaults to 8)*

- **username:** A string specifying the username for protected pages.

- **password:** A string specifying the password for protected pages.

ADDED/UPDATED IN VERSION 1.5.4-9.11413 :

- - **formFields:** A table containing form items to submit. (for POST method only)  *e.g.{ name="bob", email="bob@example.com" }*

- **arguments:** A table containing arguments you may want to pass to the callback.

### Returns

ADDED/UPDATED IN VERSION 1.5.7-9.20307 :

Returns a ***request*** value which can be used with [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md) or [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

## Example

This example shows you how you can fetch an image from a web page, and transfer it to a particular client:

Click to collapse [-]
Server

```
function startImageDownload( playerToReceive )
    fetchRemote ( "http://www.example.com/image.jpg", myCallback, "", false, playerToReceive )
end

function myCallback( responseData, errorCode, playerToReceive )
    if errorCode == 0 then
        triggerClientEvent( playerToReceive, "onClientGotImage", resourceRoot, responseData )
    end
end
```

Click to collapse [-]
Client

```
addEvent( "onClientGotImage", true )
addEventHandler( "onClientGotImage", resourceRoot,
    function( pixels )
        if myTexture then
            destroyElement( myTexture )
        end
        myTexture = dxCreateTexture( pixels )
    end
)

addEventHandler("onClientRender", root,
    function()
        if myTexture then
            local w,h = dxGetMaterialSize( myTexture )
            dxDrawImage( 200, 100, w, h, myTexture )
        end
    end
)
```

ADDED/UPDATED IN VERSION 1.5.4-9.11413 :

Example sending email via a web service (adopted from examples on [https://documentation.mailgun.com/en/latest/user_manual.html](https://documentation.mailgun.com/en/latest/user_manual.html))

Click to collapse [-]
Server

```
sendOptions = {
    queueName = "My Mailgun queue",
    connectionAttempts = 3,
    connectTimeout = 5000,
    formFields = {
        from="Excited User <excited@samples.mailgun.org>",
        to="devs@mailgun.net",
        subject="Hello",
        text="Testing some Mailgun awesomness!",
    },
    username="api",
    password="key-3ax6xnjp29jd6fds4gc373sgvjxteol0",
}
fetchRemote( "https://api.mailgun.net/v3/samples.mailgun.org/messages", sendOptions, mailgunCompleteCallback )

function mailgunCompleteCallback(data, info)
    outputDebugString( "mailgunComplete"
            .. " success:" .. tostring(info.success)
            .. " statusCode:" .. tostring(info.statusCode)
            .. " data:" .. tostring(data)
            )
end
```

Changing post content on IPS forum.

Click to collapse [-]
Server

```
local apiKey = "12345678123456781234567812345678" -- key from ips admin panel
local forumAddress = "https://yourForum.com"
function setPostContent(postID,content)
  local sendOptions = {
    queueName = "updatePost",
    connectionAttempts = 1,
    connectTimeout = 50,
    formFields = {
      post = content,
    },
  }
  fetchRemote( forumAddress.."/api/forums/posts/"..postID.."?key="..apiKey, sendOptions, function()end)
end

setPostContent(1, "this is a first post on this forum")
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.1-9.04605 | Added connectionAttempts argument |
| --- | --- |

| 1.3.2 | Added client side |
| --- | --- |

| 1.5.3-9.11270 | Added queueName argument |
| --- | --- |

| 1.5.4-9.11342 | Added alternative syntax |
| --- | --- |

| 1.5.4-9.11413 | Added formFields |
| --- | --- |

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
