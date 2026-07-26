---
doc_id: "mta-wiki:3359"
title: "HttpClear"
source_title: "HttpClear"
source_url: "https://wiki.multitheftauto.com/wiki/HttpClear"
revision_id: 12857
language: "en"
categories: []
generated_at: "2026-07-26T16:15:43.662273+00:00"
---

# HttpClear

This function removes all text from the current HTML output.

## Syntax

```
bool httpClear ( )
```

### Returns

Returns *true* if the output buffer was cleared successfully, *false* otherwise.

## Example

This sample resource page adds a message to be outputted saying there are players in the server, but clears output if the server is empty so a blank page is displayed instead.

```
[html]
<html>
   <head/>
   <body>
      There are some players in the server.
   </body>
</html>
<*
```

```
if getPlayerCount() == 0 then

  httpClear()

end
```

```
[html]*>
```

## See Also

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- httpClear

- [httpRequestLogin](mta://reference/misc/httprequestlogin.md)

- [httpSetResponseCode](mta://reference/misc/httpsetresponsecode.md)

- [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md)

- [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md)

- [httpWrite](mta://reference/misc/httpwrite.md)
