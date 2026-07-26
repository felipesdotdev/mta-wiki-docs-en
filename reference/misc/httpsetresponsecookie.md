---
doc_id: "mta-wiki:3363"
title: "HttpSetResponseCookie"
source_title: "HttpSetResponseCookie"
source_url: "https://wiki.multitheftauto.com/wiki/HttpSetResponseCookie"
revision_id: 34960
language: "en"
categories: []
generated_at: "2026-07-26T16:15:43.696213+00:00"
---

# HttpSetResponseCookie

This function sets the value for the specified HTTP cookie of the current HTML page.

## Syntax

```
bool httpSetResponseCookie ( string cookieName, string cookieValue )
```

## Required Arguments

- **cookieName:** the HTTP cookie whose value is being set.

- **cookieValue:** the new value for the specified cookie.

### Returns

Returns *true* if the cookie value was set successfully, *false* otherwise.

## Example

This example is going to get the current users account name and save their name to a cookie.

```
<* local accName = getAccountName(user)
     if not accName then return end
     httpSetResponseCookie("userName",accName) *>
<!DOCTYPE html>
<html>
     <body onLoad="getAcc();">
          Your Account Name is: <span id="accnam"></span>
     <script>
          //getCookie function from w3schools.com
          function getCookie(c_name){
               var i,x,y,ARRcookies=document.cookie.split(";");
               for (i=0;i<ARRcookies.length;i++){
                    x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
                    y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
                    x=x.replace(/^\s+|\s+$/g,"");
                    if (x==c_name)
                         return unescape(y);
               }
          }

          function getAcc(){
               var acc = document.getElementById("accnam");
               var name = getCookie("userName");
               if(!name || name!="")
                    acc.innerHTML = name;
               else
                    acc.innerHTML = "Could not get your account name!";
          }
     </script>
     </body>
</html>
```

## See Also

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- [httpClear](mta://reference/misc/httpclear.md)

- [httpRequestLogin](mta://reference/misc/httprequestlogin.md)

- [httpSetResponseCode](mta://reference/misc/httpsetresponsecode.md)

- httpSetResponseCookie

- [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md)

- [httpWrite](mta://reference/misc/httpwrite.md)
