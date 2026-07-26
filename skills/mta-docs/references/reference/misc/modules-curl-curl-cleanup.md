---
doc_id: "mta-wiki:5586"
title: "Modules/cURL/curl cleanup"
source_title: "Modules/cURL/curl cleanup"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_cleanup"
revision_id: 40066
language: "en"
categories: []
---

# Modules/cURL/curl cleanup

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Cleans up the curl handle.

## Syntax

```
curlCleanup(curl handler)
```

## Required arguments

- **curl** The curl handler

## Returns

Nothing usefull

## Example

```
curl = curlInit("http://mtasa.com/");
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlPerform(curl);
    curlCleanup(curl);
    curlClose(curl);
end
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- curlCleanup

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
