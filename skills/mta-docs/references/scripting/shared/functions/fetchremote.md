---
doc_id: "mta-wiki:6071"
title: "FetchRemote"
source_title: "FetchRemote"
source_url: "https://wiki.multitheftauto.com/wiki/FetchRemote"
revision_id: 81406
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FetchRemote

This function allows you to post and receive data from HTTP servers. The calls are asynchronous so you do not get an immediate result from the call, instead a callback function you specify is called when the download completes.

| [[{{{image}}}\|link=\|]] | Note: Client side function only works with the server the player is connected to unless the domain has been accepted with requestBrowserDomains |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: function won't trigger inside another fetchRemote function |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: When using toJSON for submitting data, make sure to use string.sub(data, 2, -2) to remove the initial and final brackets, as many APIs will not understand the request |
| --- | --- |
|  |  |

|  | This page describes the current implementation. For older versions check legacy version |
| --- | --- |
|  |  |

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

- ***statusCode*** - An integer status/error code. See the list of possible error values below.

- ***headers*** - A table containing the HTTP response headers

- ***arguments...*** - The arguments that were passed into fetchRemote

### Callback **statusCode** error values

- **1-89**: See [cURL website](http://curl.haxx.se/libcurl/c/libcurl-errors.html) or its mirror at [cURL errors](mta://reference/misc/curl-errors.md)

- **400-599**: See [HTTP status codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)

- **1002**: Download aborted

- **1003**: Failed to initialize

- **1004**: Unable to parse url

- **1005**: Unable to resolve host name

- **1006**: Destination IP not allowed

- **1007**: File error

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

- **formFields:** A table containing form items to submit. (for POST method only)  *e.g.{ name="bob", email="bob@example.com" }*

- **callbackArguments:** A table containing arguments you may want to pass to the callback.

### Returns

Returns a ***request*** value which can be used with [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md) or [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

## Example

Click to collapse [-]
Server - Example 1

Sending email via a web service (adopted from examples on [https://documentation.mailgun.com/en/latest/user_manual.html](https://documentation.mailgun.com/en/latest/user_manual.html))

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

Click to collapse [-]
Server - Example 2

Changing post content of an IPS forum thread via its API.

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

## See Also

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- fetchRemote

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
