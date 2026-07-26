---
doc_id: "mta-wiki:5272"
title: "Modules/cURL/curl init"
source_title: "Modules/cURL/curl init"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_init"
revision_id: 40062
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.243265+00:00"
---

# Modules/cURL/curl init

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Initialize the curl engine.

## Syntax

```
curl curlInit([string url])
```

## Required arguments

- There are no required arguments.

## Optional arguments

- **url** The url which you want to connect too.

## Returns

A valid curl handler on succes, otherwise it returns false

## Example

```
curl = curlInit("http://mtasa.com/");
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    -- lets do something here.
end
```

## See also

- curlInit

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
