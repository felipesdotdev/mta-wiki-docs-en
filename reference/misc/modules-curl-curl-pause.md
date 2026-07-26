---
doc_id: "mta-wiki:6145"
title: "Modules/cURL/curl pause"
source_title: "Modules/cURL/curl pause"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_pause"
revision_id: 40065
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.253921+00:00"
---

# Modules/cURL/curl pause

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Pause a request or result

## Syntax

```
CURLcode curlPause(CURL handler, int bitmask)
```

## Required arguments

- **handler** The curl handler

- **bitmask** An integer representing what you want to pause. Read more about this [here](mta://reference/misc/modules-curl-variables-curlpause.md)

## Optional arguments

None

## Returns

Returns a CURLcode, if everything is oke it returns CURLE_OK

## Example

```
curlPause( curl, CURLPAUSE_RECV );
curlPerform( ... );
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- curlPause

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
