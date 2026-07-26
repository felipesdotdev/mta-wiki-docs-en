---
doc_id: "mta-wiki:4241"
title: "Modules/hashing/md5"
source_title: "Modules/hashing/md5"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/hashing/md5"
revision_id: 17702
language: "en"
categories: []
---

# Modules/hashing/md5

|  | This function is provided by the external module hashing . You must install this module to use this function. |
| --- | --- |
|  |  |

Calculate the **MD5** hash of a string

## Syntax

```
string md5( string str )
```

### Required arguments

- **str:** string of which you want to calculate the hash

### Returns

String containing calculated MD5 hash of **str** or nil if **str** wasn't string

## Example

**Example:** This calculates the hash of **"hello world"** and prints it in debug window

```
hash = md5( "hello world" ) -- calculate MD5 hash of "hello world"
outputDebugString( hash )
```

## See also

- [alder32](mta://reference/misc/modules-hashing-alder32.md)

- md5
