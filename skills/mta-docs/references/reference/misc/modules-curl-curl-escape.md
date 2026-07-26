---
doc_id: "mta-wiki:5587"
title: "Modules/cURL/curl escape"
source_title: "Modules/cURL/curl escape"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_escape"
revision_id: 40067
language: "en"
categories: []
---

# Modules/cURL/curl escape

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Escape url's. You wont need this function if you pass the url to curl_init.

## Syntax

```
curlEscape(curl handler, string url)
```

## Required arguments

- **curl** The curl handler

- **url** The url you want to escape

## Returns

The escaped url, if it fails it will return nil

## Example

```
curl = curlInit();
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlSetopt(curl, CURLOPT_URL, curlEscape(curl, "http://mtasa.com/"));
    curlClose(curl);
end
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- curlEscape

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
