---
doc_id: "mta-wiki:2709"
title: "Resource Web Access"
source_title: "Resource Web Access"
source_url: "https://wiki.multitheftauto.com/wiki/Resource_Web_Access"
revision_id: 80069
language: "en"
categories: ["Changes_in_1.6.0", "Changes_in_1.5.8", "Changes_in_1.3.1", "Scripting_Concepts", "Tutorials"]
---

# Resource Web Access

The Multi Theft Auto Server provides a web interface that resources can use in a variety of ways. This document's purpose is to explain what these ways are and how to go about using them.

| [[{{{image}}}\|link=\|]] | Note: If you are looking for a tutorial on how to use the in-game web browser and create websites using CEF, please visit CEF Tutorial instead. |
| --- | --- |
|  |  |

## Overview

There are three key parts that make up this system.

- **Pages:** The ability to serve any http items (specified the meta.xml) as a page or file.

- **Calls:** The ability to call any exported http functions (specified in the meta.xml).

ADDED/UPDATED IN VERSION 1.6.0 [r22639](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22639):

* **Router:** Use a designated http function to route requests within a resource manually (overriding the two parts above). 

## Pages

### Specifying a file in the meta

You can specify in your resource's meta file that certain files are accessible through the web server. To do this, you add a line:

```
<html src="filename.ext" />
```

You can then access this file from your web browser by visiting: [http://host:port/resourcename/filename.ext](http://host:port/resourcename/filename.ext)  

For example, on a locally hosted server using default http port with webmap started: [http://127.0.0.1:22005/webmap/map.htm](http://127.0.0.1:22005/webmap/map.htm)

### Binary files

Despite the misleading name, files specified using the html node can be of any type. If they are binary files (like images, zip files) then you need to specify this in the meta file, by adding *raw="true"* to the *html* node. This means that the files are not preprocessed before being sent to the web browser.

For example:

```
<html src="image.gif" raw="true" />
```

### Parsed files

If a file is not specified in the metafile as "raw", then it is passed through a pre-processor before it is returned to the client. This pre-processor works much like PHP or ASP but uses Lua. You can embed standard MTA scripts within HTML pages, controlling the output. Almost all standard MTA functions work, plus a number of special [HTTP Functions](https://wiki.multitheftauto.com/wiki/Template:HTTP_functions), such as [httpWrite](mta://reference/misc/httpwrite.md), a function that outputs text to the buffer.

For example:

```
<html>
    <body>
        This resource is called <* httpWrite( getResourceName(getThisResource()) ) *>
    </body>
<html>
```

There is a shorthand (in common with PHP and ASP) for this code, meaning that you can also write the above code as:

```
<html>
    <body>
        This resource is called <* = getResourceName(getThisResource()) *>
    </body>
<html>
```

Aside from HTTP functions, embedded Lua has access to the following environment variables that contain information about how the page was requested:

- table **requestHeaders**: This is a table containing all the headers that were requested with the page. You can set returned headers using [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md).

- table **form**: This is a table containing all the form data submitted to the page using HTTP POST combined with any variables passed in the querystring with HTTP GET.

- table **cookies**: This is a table of all the cookies. You can modify cookies using [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md).

- string **hostname**: This is a string containing the IP address or hostname that requested the page.

- string **url**: This is the URL of the page.

- account **user**: This is the account of the current user.

- string **requestBody**: This is the request body.

- string **method**: This is the request method.

It's important to note that parsed files are run in a separate virtual machine from the rest of your resource's code. As such, if you want to call a function in your resource's main code, you need to export the function and use the [call](mta://scripting/shared/functions/call.md) function from your parsed file.

## Calls

You can specify that certain exported functions in your resource are able to be called from the HTTP interface. All the SDKs (listed below) allow you to call these functions from a remote location.

To specify an exported http-accessible function, add the following to your meta.xml file:

```
<export function='functionName' http='true' />
```

You can code your function just as you would any normal function, returning as many values as you want, including tables and resources and most important elements. You *cannot* however return other 'userdata' values such as [xmlnodes](mta://reference/misc/xmlnode.md) or functions.

### Protocol

| [[{{{image}}}\|link=\|]] | Note: You don't need to know this unless you're writing your own HTTP request code. You can just use one of the SDKs listed below . |
| --- | --- |
|  |  |

Calls are done by requesting *http://<your IP>:<your port>/<resource_name>/call/<exported_function_name>* using HTTP POST. The body of the request should be a JSON array of the arguments for the function.

The request will return a JSON array of the value(s) returned from the function as the HTTP response.

The server supports HTTP Basic authentication and you can configure access via the ACL and the built-in accounts system.

### Calls from the HTTP web interface

Using calls is probably easiest from the web interface and can be done almost seamlessly.

First, add this to your meta.xml file:

```
<include resource="ajax" />
```

Secondly, add the following to the <head> section of the page you want to call from:

```
<* = exports.ajax:start(getResourceName(getThisResource())) *>
```

Finally, you can create a javascript block on your page and call your functions almost as if they were local. The only difference is that the calls are asynchronous - you should specify a callback function as the last argument for your call. This is called when the function returns.

Here's a simple example.

**meta.xml**

```
<meta>
   <include resource="ajax" />
   <script src='code.lua' />
   <html src='page.htm' default='true' />
   <export function='showChatMessage' http='true' />
</meta>
```

**code.lua**

```
function showChatMessage ( message )
    outputChatBox ( message )
    return 5;
end
```

**page.htm**

```
<html>
    <head>
        <* = exports.ajax:start(getResourceName(getThisResource())) *>
        <script type='text/javascript'>
            function say() {
                var message = document.getElementById('message')
                showChatMessage ( message.value, 
                    function ( number ) {
                        // the function has been called and returned something
                        message.value = "The function returned " + number;
                    }
                );
            }
        </script>
    </head>
    <body>
        <input type='text' id='message' /><input type='button' value='say' onclick='say();' />
    </body>
</html>
```

You can see (fairly complex) examples of how this can be done in the resources *resourcebrowser*, *resourcemanager* and *webadmin*.

## Router

ADDED/UPDATED IN VERSION 1.6.0 [r22639](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22639):

A router is a function that overrides both the function call mechanism and basic web server functionality, to allow a scripter to personalize the routing and client-response for each resource separately. For example, this allows a scripter to write an **api** named resource with a router function, that can serve any sort of information in a RESTy fashion. You may also take this further, and name the resource **v1** (or **v2**...) for easy API versioning. You can spin up and down the different resources as you wish, and users of your API can continue using an older version this way.

### How to setup a router function

A router function has to be specified in the meta.xml (see example below). You can name the function however you like, there are no restrictions, as long as the function can be found in the global Lua scope in your scripts. **Note:** You can have only one router function.

```
<export function="httpRouter" http="true" router="true" />
```

Then you have to specify the function in any Lua script:

```
function httpRouter(request)
    return 200 -- see below for a more complex return value
end
```

### Request

This section describes all the fields, that can be found in the **request** table passed to the router function for every call. The descriptions below use the following example URL:

`[http://127.0.0.1:22005/api/vehicles/123?meow=true](http://127.0.0.1:22005/api/vehicles/123?meow=true)` (**api** is the resource name)

| Field | Type | Description |
| --- | --- | --- |
| account | Account | An account that was used for this request (can be a guest account ). |
| method | string | One of the following: OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT, PATCH, * |
| path | string | The requested path within your resource: "/vehicles/123" |
| absolute_path | string | The absolute path from the URL: "/api/vehicles/123?meow=true" |
| hostname | string | The hostname of the web server: "127.0.0.1" |
| port | integer | The client port used by the web server: 56758 (can be anything, but never 22005) |
| body | string | The body portion of the request sent by the client |
| query | table | A key-value table (with string keys and values) with the path's query fields (only query) |
| formData | table | A key-value table (with string keys and values) with the request form data (both query and body fields) |
| cookies | table | A key-value table (with string keys and values) with the request cookies |
| headers | table | A key-value table (with string keys and values) with the request headers (like User-Agent) |

### Response

This section describes all the possible variants, that can be returned by the router function. There are three variants in total:

- Return literally nothing: response will use http status code *200* and an empty body.

- Return an [integer](https://wiki.multitheftauto.com/index.php?search=integer): response will convert the number to an http status code and use an empty body.

- Return a table: response will be filled with the fields from the table (defaults to http status code *200* and empty body, if not overriden by a table field).

#### Response table fields

| Field | Type | Description |
| --- | --- | --- |
| status | integer | A number that will be converted to an http status code. |
| body | string | A string that will be used for the response body. |
| headers | table | A key-value table (with string keys and values) that will be written to the header section of the response. |
| cookies | table | A table with simple string key and value entries, or any-type key with table values (key is not used), entries. Check the examples below, if it's unclear. |

### Examples

```
function httpRouter(request)
    -- HTTP status code 200 & empty body
end
```

```
function httpRouter(request)
    return 404 --< HTTP status code & empty body
end
```

```
function httpRouter(request)
    return {
        status = 404,
        body = "not found",
    }
end
```

```
function httpRouter(request)
    return {
        status = 505,
        body = "foo",
        cookies = {
            foo = "1234",
            {
                name = "bar",  -- Cookie name must always be a lowercase "name" key
                value = "6666",  -- Cookie value must always be a lowercase "value" key
                Version = "2",  -- Any other cookie field can use any case
            }
        },
        headers = {
            ["content-type"] = "text/html",
            ["etag"] = "c561c68d0ba92bbeb8b0f612a9199f722e3a621a",
            ["access-control-allow-origin"] = "*",
            ["x-custom-header"] = "MTA server",
        }
    }
end
```

## Securing the web interface

The [ACL](https://wiki.multitheftauto.com/index.php?search=ACL) has a number of rights that can affect what files can be accessed.

- **resource.ResourceName.http**: If enabled, the resource will be accessible from [http://server_ip:22005/ResourceName/](http://server_ip:22005/ResourceName/)

This works as with other ACL rights - You can enable it just for Admin users, or any other group of users you wish.

## SDK

There are a number of so-called 'SDKs' available that allow you to interface with the server from other programming languages. With these, you could (in theory) write whole gamemodes. In practice, this is probably a bad idea, but it is useful for statistics and administration. The PHP SDK is the most developed version. Feel free to modify or create your own SDKs - if you do please send us a copy.

- [Java SDK](mta://reference/misc/javasdk.md)

- [Javascript SDK](mta://tutorials/javascript-sdk.md)

- [Node.js SDK](https://www.npmjs.com/package/mtasa)

- [Rust SDK](https://crates.io/crates/mta-sdk)

- [Python SDK](https://pypi.org/project/MTA-SDK-Python/)

- [Perl SDK](mta://tutorials/perl-sdk.md)

- [PHP SDK](mta://tutorials/php-sdk.md)

- [C# SDK](mta://reference/misc/csharp-sdk.md)

## See Also

[callRemote](mta://scripting/server/functions/callremote.md) - Allows game servers to call functions on PHP pages (with the PHP SDK) and on other game servers.
