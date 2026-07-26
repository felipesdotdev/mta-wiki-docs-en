---
doc_id: "mta-wiki:5273"
title: "Modules/cURL/curl close"
source_title: "Modules/cURL/curl close"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_close"
revision_id: 40063
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.219117+00:00"
---

# Modules/cURL/curl close

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Closes the curl engine.

## Syntax

```
curlClose(curl handler)
```

## Required arguments

- **curl** The curl handler

## Returns

True on succes, false otherwise

## Example

```
curl = curlInit("http://mtasa.com/");
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlClose(curl);
end
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- curlClose

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
