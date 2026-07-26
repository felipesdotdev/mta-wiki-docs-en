---
doc_id: "mta-wiki:3360"
title: "HttpRequestLogin"
source_title: "HttpRequestLogin"
source_url: "https://wiki.multitheftauto.com/wiki/HttpRequestLogin"
revision_id: 21469
language: "en"
categories: []
generated_at: "2026-07-26T16:15:43.671447+00:00"
---

# HttpRequestLogin

This function makes the user's browser show a 'basic authentication' login box. The result of the login is handled automatically by the server. If the user has not logged in satisfactorily, you should just call the httpRequestLogin function again. It is the script's responsibility to judge when the user is logged in satisfactorily - you can use the *user* variable can be used to check if the user has logged in with an account you are happy with. If the logged in user doesn't meet whatever criteria you have, you can just call httpRequestLogin again and they will be re-promoted for their password.

This function works by setting a header ('Authentication') and a return code (403 - Authentication required). As such, nothing happens until you finish the page. The content of the page is generally not displayed unless the login fails.

## Syntax

```
bool httpRequestLogin ( )
```

### Returns

Returns *true* if the relevant headers and return codes have been set, *false* otherwise. Essentially, always returns *true*.

## Example

This example shows how you can make a page that only registered users can see.

```
<*
if isGuestAccount(user) then
   httpRequestLogin()
else
 *>
Welcome to the top secret area for registered users!
<*
end
 *>
```

## See Also

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- [httpClear](mta://reference/misc/httpclear.md)

- httpRequestLogin

- [httpSetResponseCode](mta://reference/misc/httpsetresponsecode.md)

- [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md)

- [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md)

- [httpWrite](mta://reference/misc/httpwrite.md)
