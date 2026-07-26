---
doc_id: "mta-wiki:5874"
title: "Resource : TextSpeech"
source_title: "Resource:TextSpeech"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ATextSpeech"
revision_id: 29418
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:00.210059+00:00"
---

# Resource : TextSpeech

TextSpeech gives you the ability to get spoken text by Google's TextToSpeech.

## Events

**Note:** You may have to add the events in your script using addEvent() if you want to use them.

### Server

| Name | Source | Parameters |
| --- | --- | --- |

| onSpeech | triggerFor | string text, string language |
| --- | --- | --- |

### Client

| onClientSpeech | root | string text, string language |
| --- | --- | --- |

## Exported functions

### Server

| boolean | speak | string text, string language, element triggerFor |
| --- | --- | --- |

### Client

| element | speak | string text, string language |
| --- | --- | --- |
| element | speak3D | string text, string language, float x, float y, float z |
