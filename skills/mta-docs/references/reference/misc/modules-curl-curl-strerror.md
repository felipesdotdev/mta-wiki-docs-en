---
doc_id: "mta-wiki:5589"
title: "Modules/cURL/curl strerror"
source_title: "Modules/cURL/curl strerror"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_strerror"
revision_id: 40069
language: "en"
categories: []
---

# Modules/cURL/curl strerror

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Returns a string with detailed information of an error.

## Syntax

```
curlStrerror(curl handler, CURLcode code)
```

## Required arguments

- **curl** The curl handler

- **code** The curl code

## Returns

The string containing the error, if the code was not found in the system it will return nil

## Example

```
curl = curlInit();
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlSetopt(curl, CURLOPT_URL, curlEscape(curl, "http://mtasa.com/"));
    result = curlPerform(curl);
    print(curlStrerror(curl, result)); -- Since we know that mta exists, we sure get the text 'No error.'
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

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- curlStrerror
