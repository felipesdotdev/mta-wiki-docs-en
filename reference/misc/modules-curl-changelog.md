---
doc_id: "mta-wiki:7187"
title: "Modules/cURL/changelog"
source_title: "Modules/cURL/changelog"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/cURL/changelog"
revision_id: 36225
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.196518+00:00"
---

# Modules/cURL/changelog

The changelog for the module cURL

Version 1.2

- Added a data return value to curl_perform, it now returns curlcode, data

- Removed the second argument curl_perform, it now only accepts the curl handle

- fixed curl_init( string url ). It now works correctly
