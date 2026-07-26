---
doc_id: "mta-wiki:5270"
title: "Modules/cURL"
source_title: "Modules/cURL"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL"
revision_id: 50700
language: "en"
categories: ["Modules"]
---

# Modules/cURL

| Module info |  |
| --- | --- |
| Name | MTA Curl |
| Version | 1.2 |
| Author | Alexander de Jong (mrdejong) |
| Module website | Here |
| Download link | 1.3 [1] |
| License | BSD |
| Written in | C++ |
| Operating system | Windows |
| Compatible with | 1.3.0, 1.3.1, 1.3.2, 1.3.5 |

MTA Curl module is a handy module to make restful api web calls. You could do everything with it.

The module is based on php cURL module.

If you found any bugs, please post them on the [github page](https://github.com/mrdejong/mta_curl/issues)

You can find the source at the [github repository](https://github.com/mrdejong/mta_curl)

Update 22-6-2014

Released version 1.4;

This release changed the function name syntax to adobt the mta syntax.

## cURL functions

- [curlInit](mta://reference/misc/modules-curl-curl-init.md)

- [curlClose](mta://reference/misc/modules-curl-curl-close.md)

- [curlSetopt](mta://reference/misc/modules-curl-curl-setopt.md)

- [curlPause](mta://reference/misc/modules-curl-curl-pause.md)

- [curlCleanup](mta://reference/misc/modules-curl-curl-cleanup.md)

- [curlEscape](mta://reference/misc/modules-curl-curl-escape.md)

- [curlPerform](mta://reference/misc/modules-curl-curl-perform.md)

- [curlStrerror](mta://reference/misc/modules-curl-curl-strerror.md)

## cURL variables

- [CURLPAUSE](mta://reference/misc/modules-curl-variables-curlpause.md)

## Changelog

## Version 1.4

- Changed function syntax.

- Cleaned the code up

## Version 1.2

- Added a data return value to curl_perform, it now returns curlcode, data

- Removed the second argument curl_perform, it now only accepts the curl handle

- fixed curl_init( string url ). It now works correctly
