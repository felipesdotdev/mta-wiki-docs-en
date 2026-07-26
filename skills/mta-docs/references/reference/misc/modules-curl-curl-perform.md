---
doc_id: "mta-wiki:5588"
title: "Modules/cURL/curl perform"
source_title: "Modules/cURL/curl perform"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_perform"
revision_id: 40068
language: "en"
categories: []
---

# Modules/cURL/curl perform

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Let cURL do his work now, by call this function.

## Syntax

```
curlPerform(curl handler)
```

## Required arguments

- **curl** The curl handler

## Returns

Returns a curl code, if the code is CURLE_OK then your good. Other wise pass this code to curl_strerror, and then you will know what is going on.
On a success call it will return the data as a second argument.

## Example

```
curl = curlInit();
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlSetopt(curl, CURLOPT_URL, curlEscape(curl, "http://mtasa.com/"));
    result, data = curlPerform(curl);
    if result == CURLE_OK then
        print(data)
    end
    curlClose(curl);
end
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- curlPerform

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
