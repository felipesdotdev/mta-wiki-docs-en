---
doc_id: "mta-wiki:3362"
title: "HttpSetResponseHeader"
source_title: "HttpSetResponseHeader"
source_url: "https://wiki.multitheftauto.com/wiki/HttpSetResponseHeader"
revision_id: 37231
language: "en"
categories: []
---

# HttpSetResponseHeader

This function sets the value for the specified HTTP response header of the current HTML page.

## Syntax

```
bool httpSetResponseHeader ( string headerName, string headerValue )
```

## Required Arguments

- **headerName:** the HTTP header whose value is being set. You can find a list of header names [here](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). Header names should be all *lower case* letters.

- **headerValue:** the new value for the specified header.

### Returns

Returns *true* if the header value was set successfully, *false* otherwise.

## Example

Using httpSetResponseHeader to set the content type. (Example from [httpWrite](mta://reference/misc/httpwrite.md))

```
<*
local file = fileOpen ( "icons/icon.png" )
if file then
	while not fileIsEOF(file) do            
		buffer = fileRead(file, 500)         
		httpWrite(buffer, buffer:len())
	end
	fileClose(file)                           
	httpSetResponseHeader ( "content-type", "image/png")
else
	*>
	Could not read file
	<*
end
*>
```

## See Also

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- [httpClear](mta://reference/misc/httpclear.md)

- [httpRequestLogin](mta://reference/misc/httprequestlogin.md)

- [httpSetResponseCode](mta://reference/misc/httpsetresponsecode.md)

- [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md)

- httpSetResponseHeader

- [httpWrite](mta://reference/misc/httpwrite.md)
