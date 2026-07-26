---
doc_id: "mta-wiki:4240"
title: "Modules/hashing/alder32"
source_title: "Modules/hashing/alder32"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/hashing/alder32"
revision_id: 17701
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.320319+00:00"
---

# Modules/hashing/alder32

|  | This function is provided by the external module hashing . You must install this module to use this function. |
| --- | --- |
|  |  |

Calculate the **alder32** hash of the given string

## Syntax

```
string alder32( string str )
```

### Required arguments

- **str:** string of which you want to calculate the hash

### Returns

String containing calculated alder32 hash of **str** or nil if **str** wasn't string

## Example

**Example:** This calculates the hash of **"hello world"** and prints it in debug window

```
hash = alder32( "hello world" ) -- get alder32 hash of "hello world"
outputDebugString( hash )
```

## See also

- alder32

- [md5](mta://reference/misc/modules-hashing-md5.md)
