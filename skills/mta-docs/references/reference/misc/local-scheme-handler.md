---
doc_id: "mta-wiki:8412"
title: "Local Scheme Handler"
source_title: "Local Scheme Handler"
source_url: "https://wiki.multitheftauto.com/wiki/Local_Scheme_Handler"
revision_id: 81189
language: "en"
categories: ["Changes_in_1.5.1", "Changes_in_1.5.0-7439"]
---

# Local Scheme Handler

In many cases it is necessary to access files stored on the local disk from browsers.

## Scheme format

```
http://mta/resourceName/file.extension
```

- **resourceName**: The resource name, *local* is a special name for the current resource

- **file.extension**: The file path within *resourceName*

You can use this scheme format for [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md) as well as in HTML files e.g. <img> tags.

## Examples

### Example 1

```
http://mta/myResource/assets/myImage.png
```

Refers to the file *assets/myImage.png* in a resource named *myResource*

### Example 2

```
http://mta/local/assets/myImage.png
```

Refers to the file *assets/myImage.png* in the current resource
