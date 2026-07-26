---
doc_id: "mta-wiki:5274"
title: "Modules/cURL/curl setopt"
source_title: "Modules/cURL/curl setopt"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/curl_setopt"
revision_id: 40064
language: "en"
categories: []
---

# Modules/cURL/curl setopt

|  | This function is provided by the external module cURL . You must install this module to use this function. |
| --- | --- |
|  |  |

Set an curl option.

## Syntax

```
curlcode curlSetopt(curl handler, curloption option, bool/number/string value)
```

## Required arguments

- **handler** The curl handler.

- **option** An curl option, al the options are found [here](https://wiki.multitheftauto.com/index.php?title=Modules/cURL/CURLOPT&action=edit&redlink=1)

- **value** The value, this can be a string, number or boolean. At the [curl option list](https://wiki.multitheftauto.com/index.php?title=Modules/cURL/CURLOPT&action=edit&redlink=1) you can find wich option needs a string, number or boolean.

## Returns

Returns a curlcode. Nevermind it for now, i even don't know what it is. But it returns it.

## Example

```
curl = curlInit("http://mtasa.com/");
if not curl then
    outputDebugString("Can't connect to http://mtasa.com/ with cURL");
else
    curlSetopt(curl, CURLOPT_POST, true);
    curlClose(curl);
end
```

## See also

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- curlSetopt

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)
