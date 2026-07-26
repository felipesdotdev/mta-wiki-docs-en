---
doc_id: "mta-wiki:3361"
title: "HttpSetResponseCode"
source_title: "HttpSetResponseCode"
source_url: "https://wiki.multitheftauto.com/wiki/HttpSetResponseCode"
revision_id: 12875
language: "en"
categories: []
---

# HttpSetResponseCode

This function sets the HTTP status code that will be sent for the current HTML page.

## Syntax

```
bool httpSetResponseCode ( int code )
```

## Required Arguments

- **code:** the HTTP status code to be set.

### Returns

Returns *true* if the code was set successfully, *false* otherwise.

## Example

Click to collapse [-]
Server/HTTP

This example displays a 'Page not found' error message and the response code 404. The location of the httpSetResponseCode call is unimportant - it can be placed anywhere in the document.

```
[html]<html>
<h1>Page not found!</h1>
<* httpSetResponseCode ( 404 ) *>
</html>
```

## See Also

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- [httpClear](mta://reference/misc/httpclear.md)

- [httpRequestLogin](mta://reference/misc/httprequestlogin.md)

- httpSetResponseCode

- [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md)

- [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md)

- [httpWrite](mta://reference/misc/httpwrite.md)
